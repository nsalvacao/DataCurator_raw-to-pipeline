import asyncio
from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import logging

from openai import AsyncOpenAI
from opentelemetry import trace

from workflow_config import WorkflowConfig, load_prompt

# Setup logging
logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


@dataclass
class AgentResult:
    name: str
    content: str


class BaseAgentExecutor:
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig, prompt_name: str):
        self.client = client
        self.cfg = cfg
        self.prompt_name = prompt_name
        self.system_prompt = load_prompt(prompt_name, cfg)

    async def run(self, user_input: str, **kwargs: Any) -> AgentResult:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input},
        ]
        
        with tracer.start_as_current_span(f"executor.{self.prompt_name}") as span:
            span.set_attribute("executor.name", self.prompt_name)
            span.set_attribute("input.length", len(user_input))
            
            logger.debug(f"Running {self.prompt_name} with input length: {len(user_input)}")
            
            completion = await self.client.chat.completions.create(
                model=self.cfg.model.model,
                messages=messages,
                temperature=0.1,
            )
            
            result = AgentResult(name=self.prompt_name, content=completion.choices[0].message.content)
            
            span.set_attribute("output.length", len(result.content))
            logger.info(f"✅ {self.prompt_name} completed - output length: {len(result.content)}")
            
            return result


class ProblemClassifierExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "problem_classifier")


class RawTaxonomistExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "raw_taxonomist")


class TaxonomyRefinerExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "taxonomy_refiner")


class CategoryExtractorExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "category_extractor")


class CategoryCuratorExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "category_curator")


class IndexArchitectExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "index_architect")


class StructureAuditorExecutor(BaseAgentExecutor):
    def __init__(self, client: AsyncOpenAI, cfg: WorkflowConfig):
        super().__init__(client, cfg, "structure_auditor")


async def run_category_pipeline(
    client: AsyncOpenAI,
    cfg: WorkflowConfig,
    category_payload: str,
) -> List[AgentResult]:
    extractor = CategoryExtractorExecutor(client, cfg)
    curator = CategoryCuratorExecutor(client, cfg)

    extract_res = await extractor.run(category_payload)
    curate_res = await curator.run(extract_res.content)
    return [extract_res, curate_res]


async def run_full_pipeline(raw_notes: str, cfg: WorkflowConfig) -> Dict[str, AgentResult]:
    client = AsyncOpenAI(api_key=cfg.model.api_key, base_url=cfg.model.base_url)

    classifier = ProblemClassifierExecutor(client, cfg)
    taxonomist = RawTaxonomistExecutor(client, cfg)
    refiner = TaxonomyRefinerExecutor(client, cfg)
    index_architect = IndexArchitectExecutor(client, cfg)
    auditor = StructureAuditorExecutor(client, cfg)

    results: Dict[str, AgentResult] = {}
    
    with tracer.start_as_current_span("pipeline.full") as span:
        span.set_attribute("pipeline.input_length", len(raw_notes))
        logger.info("Starting full pipeline execution")

        # Phase 1: Classification
        with tracer.start_as_current_span("pipeline.phase1_classification"):
            results["classifier"] = await classifier.run(raw_notes)
        
        # Phase 2: Raw Taxonomy
        with tracer.start_as_current_span("pipeline.phase2_taxonomy"):
            results["taxonomy_raw"] = await taxonomist.run(results["classifier"].content)
        
        # Phase 3: Refinement
        with tracer.start_as_current_span("pipeline.phase3_refinement"):
            results["taxonomy_refined"] = await refiner.run(results["taxonomy_raw"].content)

        # Phase 4: Category Extraction & Curation (Parallel)
        with tracer.start_as_current_span("pipeline.phase4_categories"):
            category_payloads = [results["taxonomy_refined"].content]
            cat_runs = await asyncio.gather(
                *[run_category_pipeline(client, cfg, payload) for payload in category_payloads]
            )
            for idx, run in enumerate(cat_runs):
                results[f"category_{idx}_extractor"] = run[0]
                results[f"category_{idx}_curator"] = run[1]

        # Phase 5: Index Architecture
        with tracer.start_as_current_span("pipeline.phase5_index"):
            curated_text = "\n\n".join(r.content for k, r in results.items() if "curator" in k)
            results["index_architect"] = await index_architect.run(curated_text)

        # Phase 6: Audit
        with tracer.start_as_current_span("pipeline.phase6_audit"):
            auditor_input = (
                "RAW_NOTES:\n" + raw_notes + "\n\nINDEX_OUTPUT:\n" + results["index_architect"].content
            )
            results["auditor"] = await auditor.run(auditor_input)
        
        span.set_attribute("pipeline.total_results", len(results))
        logger.info(f"✅ Pipeline completed with {len(results)} results")

    return results
