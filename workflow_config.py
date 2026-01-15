import os
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv

# Load .env from the project root
load_dotenv()


@dataclass
class ModelConfig:
    api_key: str
    base_url: str
    model: str


@dataclass
class PathConfig:
    root: Path
    prompts_dir: Path


@dataclass
class WorkflowConfig:
    model: ModelConfig
    paths: PathConfig


PROMPT_FILES = {
    "problem_classifier": "problem_classifier_agent.md",
    "raw_taxonomist": "raw_taxonomist_agent.md",
    "taxonomy_refiner": "taxonomy_refiner_agent.md",
    "category_extractor": "category_extractor_agent.md",
    "category_curator": "category_curator_agent.md",
    "index_architect": "index_architect_agent.md",
    "structure_auditor": "structure_auditor_agent.md",
}


def load_config(project_root: Optional[str] = None) -> WorkflowConfig:
    root_path = Path(project_root) if project_root else Path(__file__).parent
    prompts_dir = root_path / "prompts"

    api_key = os.getenv("GITHUB_TOKEN", "")
    base_url = os.getenv("BASE_URL", "https://models.inference.ai.azure.com")
    model_id = os.getenv("MODEL_ID", "openai/gpt-5.1")

    if not api_key:
        raise RuntimeError("GITHUB_TOKEN not set. Please add it to .env")

    return WorkflowConfig(
        model=ModelConfig(api_key=api_key, base_url=base_url, model=model_id),
        paths=PathConfig(root=root_path, prompts_dir=prompts_dir),
    )


def load_prompt(name: str, cfg: WorkflowConfig) -> str:
    filename = PROMPT_FILES.get(name)
    if not filename:
        raise KeyError(f"Unknown prompt name: {name}")
    path = cfg.paths.prompts_dir / filename
    if not path.exists():
        raise FileNotFoundError(f"Prompt file not found: {path}")
    return path.read_text(encoding="utf-8")
