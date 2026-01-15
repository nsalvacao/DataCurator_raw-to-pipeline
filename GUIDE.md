# Orchestrator Agent - Complete Guide

Orquestrador multi-agente para análise, categorização e roadmap generation de problemas técnicos usando GitHub Models.

## 📋 Table of Contents

1. [Quick Start](#quick-start)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Tracing & Monitoring](#tracing--monitoring)
5. [Logging](#logging)
6. [Evaluation](#evaluation)
7. [Configuration](#configuration)
8. [Development](#development)

---

## Quick Start

### Prerequisites

- Python 3.10+
- GitHub Personal Access Token (PAT Classic) with models access
- Virtual environment

### Installation

```bash
# Create and activate venv
python -m venv .venv
source .venv/Scripts/activate  # Windows
# or
source .venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create `.env` file in project root:

```env
GITHUB_TOKEN=your_github_pat_here
BASE_URL=https://models.inference.ai.azure.com
MODEL_ID=gpt-4o
```

### Run Pipeline

```bash
python orchestrator_agent.py
```

Output saved to: `outputs/pipeline_summary.md`

---

## Features

### 7-Agent Pipeline

1. **Problem Classifier** - Classifica problemas brutos em categorias iniciais
2. **Raw Taxonomist** - Organiza problemas em taxonomia por tema
3. **Taxonomy Refiner** - Otimiza taxonomia para execução
4. **Category Extractor** - Extrai problemas detalhados com soluções (paralelo)
5. **Category Curator** - Cura roadmaps de execução por categoria (paralelo)
6. **Index Architect** - Cria roadmap master com coordenação cross-categoria
7. **Structure Auditor** - Audita integridade estrutural e completude

### Outputs

- **Taxonomia Refinada** - Problemas organizados e priorizados
- **Categorias Estruturadas** - Problemas extraídos com análise detalhada
- **Roadmaps Curados** - Planos de execução por categoria
- **Roadmap Master** - Coordenação global de execução (GANTT, dependências, riscos, KPIs)
- **Audit Report** - Validação de qualidade e completude

---

## Architecture

### Pipeline Flow

```
Raw Notes
    ↓
[1] Classifier → [2] Raw Taxonomist → [3] Refiner
                                            ↓
                                   [4,5] Category Pipeline (parallel)
                                    ↙            ↘
                          Extractor          Curator
                            ↓                  ↓
                                Curated Categories
                                    ↓
                          [6] Index Architect
                                    ↓
                              Master Roadmap
                                    ↓
                          [7] Structure Auditor
                                    ↓
                            Audit Report
```

### File Structure

```
orchestrator-agents/
├── orchestrator_agent.py      # Main entrypoint
├── executors.py               # Agent executors (sync/parallel)
├── workflow_config.py         # Configuration loader
├── tracing_config.py          # OpenTelemetry setup
├── logging_config.py          # Logging configuration
├── evaluation_config.py       # Evaluation metrics
├── agent.json                 # Agent Builder metadata
├── requirements.txt           # Dependencies
├── .env                       # GitHub token & model config
├── .gitignore                 # Git ignore rules
├── prompts/                   # System prompts (7 agents)
├── samples/                   # Example inputs
├── outputs/                   # Generated outputs
├── tests/                     # Test suite
│   ├── queries.json           # 10 test scenarios
│   ├── responses.json         # Agent responses (auto-generated)
│   ├── evaluation_report.json # Evaluation results
│   ├── agent_runner.py        # Batch execution runner
│   └── evaluation_runner.py   # Evaluation executor
└── logs/                      # Log files
    ├── orchestrator_agent_all.log      # All logs (JSON)
    └── orchestrator_agent_errors.log   # Error logs only
```

---

## Tracing & Monitoring

### OpenTelemetry Integration

Automatic tracing via `opentelemetry-instrumentation-openai-v2`:

**Setup (Automatic):**

```python
from tracing_config import setup_tracing
setup_tracing(service_name="orchestrator_agent")
```

**What's Traced:**

- Each agent executor execution
- Pipeline phases (classification → curation → indexing → audit)
- OpenAI API calls (prompts, completions, token usage)
- Execution times and performance metrics

### View Traces

**AI Toolkit:**

```bash
# In VS Code: Open command palette
ai-mlstudio.tracing.open
```

**Or start OTLP collector manually:**

```bash
# Terminal 1: Start OTLP collector
docker run -d --name otel-collector \
  -p 4317:4317 \
  -p 4318:4318 \
  otel/opentelemetry-collector:latest

# Terminal 2: View traces (via localhost:4318)
```

### Span Attributes

Each span includes:

- `executor.name` - Agent name
- `input.length` - Input text size
- `output.length` - Output text size
- `pipeline.total_results` - Aggregated results

---

## Logging

### Setup

Automatic JSON logging to file + human-readable to console:

```python
from logging_config import setup_logging
logger = setup_logging(log_dir="logs", console_level=logging.INFO)
```

### Log Files

- **`logs/orchestrator_agent_all.log`** - All logs (JSON format, rotating 10MB)
- **`logs/orchestrator_agent_errors.log`** - Errors only

### Log Format

**Console (human-readable):**
```
2026-01-15 14:30:45 | INFO     | orchestrator_agent | ✅ Pipeline completed with 8 results
```

**File (JSON structured):**
```json
{
  "timestamp": "2026-01-15T14:30:45.123456",
  "level": "INFO",
  "logger": "orchestrator_agent",
  "message": "✅ Pipeline completed with 8 results",
  "module": "executors",
  "function": "run_full_pipeline",
  "line": 125,
  "extra_fields": {
    "query_id": "query_001",
    "execution_time": 45.2
  }
}
```

### Custom Logging

```python
from logging_config import log_with_context, get_logger

logger = get_logger("my_module")
log_with_context(
    logger,
    logging.INFO,
    "Processing completed",
    query_id="q001",
    duration_seconds=45.2,
    categories_created=3
)
```

---

## Evaluation

### 3-Tier Evaluation System

#### 1. Output Correctness

Valida estrutura, coerência e integridade:

- ✅ Estrutura válida (classifier, taxonomies, roadmap, audit)
- ✅ Secções obrigatórias presentes no roadmap
- ✅ Consistência entre taxonomy raw e refined
- ✅ Completude de dados críticos

**Target Score:** ≥ 80%

#### 2. Content Quality

Avalia qualidade e detalhes das soluções:

- ✅ Output suficientemente detalhado (2x tamanho de input)
- ✅ Recomendações solucionar problemas (múltiplas opções)
- ✅ Roadmap é acionável (timelines, esforço, ownership, métricas)
- ✅ Keywords importantes presentes (solution, effort, priority, completion)

**Target Score:** ≥ 80%

#### 3. Completeness

Verifica que nada foi perdido na pipeline:

- ✅ Todos os problemas do input foram processados
- ✅ Categorias geradas do input
- ✅ Taxonomia cobre todos os problemas
- ✅ Roadmap referencia categorias geradas

**Target Score:** ≥ 80%

### Running Evaluation

#### 1. Collect Responses

```bash
# Run agent against test queries (10 scenarios)
python tests/agent_runner.py
```

Output: `tests/responses.json`

#### 2. Run Evaluation

```bash
# Evaluate responses
python tests/evaluation_runner.py
```

Output: `tests/evaluation_report.json`

#### Example Report

```
================================================================================
📊 Evaluation Summary
================================================================================

Overall Average Score: 87.5%
✅ Passed: 9/10
❌ Failed: 1/10
📈 Pass Rate: 90.0%

Metrics Breakdown:

output_correctness:
  Average Score: 92.5%
  Passed: 9/10

content_quality:
  Average Score: 85.0%
  Passed: 8/10

completeness:
  Average Score: 85.0%
  Passed: 8/10

Per-Query Results:

✅ query_001  | Score: 95.0%
✅ query_002  | Score: 88.3%
✅ query_003  | Score: 92.5%
...
```

---

## Configuration

### Environment Variables

```env
# Required
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Optional (defaults shown)
BASE_URL=https://models.inference.ai.azure.com
MODEL_ID=gpt-4o
```

### Agent Configuration

See `agent.json` for full metadata:

- Service name & version
- Model provider & model ID
- 7 executor definitions
- Input/output schemas
- Pipeline flow
- Capabilities & tags

### Executor Configuration

In `executors.py`:

```python
# Temperature (0-1, lower = deterministic)
temperature=0.1

# Model selection in .env
MODEL_ID=gpt-4o  # or gpt-4.1, etc
```

---

## Development

### Project Structure

```python
# Main pipeline
orchestrator_agent.py     # Entry point, reads samples/raw_notes.md
executors.py             # 7 agent executors + pipeline orchestration
workflow_config.py       # Config loader, prompt paths

# Observability
tracing_config.py        # OpenTelemetry setup
logging_config.py        # Logging configuration

# Quality assurance
evaluation_config.py     # Evaluation metrics & runners

# System prompts
prompts/
  ├── problem_classifier_agent.md
  ├── raw_taxonomist_agent.md
  ├── taxonomy_refiner_agent.md
  ├── category_extractor_agent.md
  ├── category_curator_agent.md
  ├── index_architect_agent.md
  └── structure_auditor_agent.md

# Testing
tests/
  ├── queries.json            # 10 test scenarios
  ├── agent_runner.py         # Batch execution (agent responses)
  ├── evaluation_runner.py    # Evaluation execution
  └── responses.json          # Generated responses (auto)
```

### Adding New Tests

1. **Add query to `tests/queries.json`:**

```json
{
  "id": "query_011",
  "name": "Your test scenario",
  "input": "Problem description here..."
}
```

2. **Run agent runner:**

```bash
python tests/agent_runner.py
```

3. **Run evaluation:**

```bash
python tests/evaluation_runner.py
```

### Extending Evaluation

Add new evaluator to `evaluation_config.py`:

```python
class CustomEvaluator:
    @staticmethod
    def evaluate(response: Dict[str, Any]) -> Dict[str, Any]:
        # Your logic here
        return {
            "metric": "custom_metric",
            "score": 0.85,
            "passed": True,
            "issues": []
        }

# Register in EvaluationRunner.EVALUATORS
```

---

## API Examples

### Basic Usage

```python
import asyncio
from executors import run_full_pipeline
from workflow_config import load_config

async def main():
    cfg = load_config()
    
    raw_notes = """
    - Login fails on Safari
    - API latency > 800ms
    - Missing feature: CSV export
    """
    
    results = await run_full_pipeline(raw_notes, cfg)
    
    for name, result in results.items():
        print(f"{name}: {len(result.content)} chars")

asyncio.run(main())
```

### With Tracing

```python
from tracing_config import setup_tracing

setup_tracing(service_name="my_app")

# Now all traces auto-export to localhost:4318
await run_full_pipeline(raw_notes, cfg)
```

### With Logging

```python
from logging_config import setup_logging, get_logger

logger = setup_logging()

logger.info("Starting processing...")
await run_full_pipeline(raw_notes, cfg)
logger.info("Completed!")
```

---

## Troubleshooting

### Model Not Found

```
Error: Unknown model: openai/gpt-5.1
```

✅ Update `.env`:
```env
MODEL_ID=gpt-4o
```

### Token Limit Exceeded

```
Error: Request body too large for gpt-4o-mini
```

✅ Use higher-context model:
```env
MODEL_ID=gpt-4o
```

### No Tracing Data

✅ Ensure OTLP collector running:
```bash
docker run -d -p 4318:4318 otel/opentelemetry-collector:latest
```

✅ Check `setup_tracing()` called:
```python
from tracing_config import setup_tracing
setup_tracing()
```

### Logs Not Appearing

✅ Ensure logging configured:
```python
from logging_config import setup_logging
setup_logging()
```

✅ Check log directory exists: `logs/`

---

## Performance

### Typical Execution Times

| Query Complexity | Execution Time | Output Size |
|------------------|----------------|------------|
| Simple (1-2 issues) | 15-20s | 5-10KB |
| Medium (5-10 issues) | 35-45s | 15-25KB |
| Complex (15+ issues) | 60-90s | 30-50KB |

### Optimization Tips

1. **Batch Queries**: Use `agent_runner.py` for multiple inputs
2. **Parallel Categories**: Extractor/Curator run in parallel (already optimized)
3. **Model Selection**: `gpt-4o` is fastest with good quality
4. **Reduce Prompts**: Customize system prompts for your domain

---

## License

MIT

## Support

For issues or questions:

1. Check logs: `logs/orchestrator_agent_errors.log`
2. View traces: AI Toolkit tracing viewer
3. Review evaluation: `tests/evaluation_report.json`

---

**Last Updated:** January 15, 2026  
**Version:** 1.0.0
