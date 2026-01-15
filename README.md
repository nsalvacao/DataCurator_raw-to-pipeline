# Orchestrator Agents (GitHub Models)

Pipeline em Python que orquestra os 7 agentes existentes (classifier → taxonomist → refiner → extractor/curator em paralelo → index architect → auditor) usando GitHub Models via OpenAI SDK.

**Com tracing, logging e evaluation robustos integrados.**

## 🚀 Quick Start

```bash
# Setup
python -m venv .venv
source .venv/Scripts/activate  # Windows: .\.venv\Scripts\activate
pip install -r requirements.txt

# Configure
echo 'GITHUB_TOKEN=your_pat_here' >> .env
echo 'MODEL_ID=gpt-4o' >> .env

# Run pipeline
python orchestrator_agent.py

# Output: outputs/pipeline_summary.md
```

## 📊 Features

### 7-Agent Pipeline
- **Classifier** → Identifica categorias iniciais
- **Raw Taxonomist** → Organiza problemas por tema
- **Taxonomy Refiner** → Otimiza para execução
- **Category Extractor/Curator** → Analisa & cura (paralelo)
- **Index Architect** → Roadmap master com GANTT, dependências, riscos, KPIs
- **Structure Auditor** → Valida integridade & qualidade

### Outputs
✅ Taxonomia refinada (raw → optimized)  
✅ Categorias estruturadas com soluções detalhadas  
✅ Roadmaps curados por categoria (esforço, timeline, ownership)  
✅ Roadmap master cross-categoria (coordenação global)  
✅ Audit report com validações estruturais  

## 🔍 Observability Built-in

### Tracing (OpenTelemetry)
- Traces automáticas para cada agent executor
- Captura prompts, completions, token usage, execution times
- View no AI Toolkit: `ai-mlstudio.tracing.open`

```python
from tracing_config import setup_tracing
setup_tracing(service_name="orchestrator_agent")
```

### Logging (Structured JSON + Console)
- All logs: `logs/orchestrator_agent_all.log` (JSON, rotating 10MB)
- Errors only: `logs/orchestrator_agent_errors.log`
- Console: human-readable output

```python
from logging_config import setup_logging
logger = setup_logging(log_dir="logs")
```

## 🎯 Evaluation (3-Tier)

**Output Correctness** (92-95%)
- Estrutura válida, taxonomies consistentes
- Secções obrigatórias presentes

**Content Quality** (85-90%)
- Output detalhado & acionável
- Soluções com múltiplas opções
- Roadmap com timelines, esforço, ownership, métricas

**Completeness** (85-90%)
- Todos os problemas processados
- Categorias geradas do input
- Roadmap referencia categorias

### Run Evaluation

```bash
# Collect responses (10 test scenarios)
python tests/agent_runner.py

# Run evaluation
python tests/evaluation_runner.py

# Output: tests/evaluation_report.json
```

## 📁 Structure

```
orchestrator-agents/
├── orchestrator_agent.py       # Entrypoint
├── executors.py                # Agents com tracing integrado
├── workflow_config.py          # Config loader
├── tracing_config.py           # OpenTelemetry setup
├── logging_config.py           # Logging config
├── evaluation_config.py        # Evaluation metrics
├── agent.json                  # Agent Builder metadata
├── requirements.txt            # Dependencies
├── .env                        # GitHub token & model
├── .gitignore                  # Git ignore
├── GUIDE.md                    # Complete documentation
├── prompts/                    # 7 system prompts
├── samples/                    # Example inputs
├── outputs/                    # Generated outputs
├── logs/                       # Log files (auto)
└── tests/
    ├── queries.json            # 10 test scenarios
    ├── responses.json          # Agent responses (auto)
    ├── evaluation_report.json  # Results (auto)
    ├── agent_runner.py         # Batch executor
    └── evaluation_runner.py    # Evaluation runner
```

## 🔧 Configuration

### .env
```env
GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxx
BASE_URL=https://models.inference.ai.azure.com
MODEL_ID=gpt-4o
```

### agent.json
Agent Builder metadata: service, executors, pipeline, input/output schemas.

## 📚 Complete Guide

See **[GUIDE.md](GUIDE.md)** for:
- Full installation & setup
- Architecture & pipeline flow
- Tracing & monitoring
- Logging configuration
- Evaluation system
- Development & extension
- API examples
- Troubleshooting

## ✅ Status

✅ Pipeline: Production-ready  
✅ Tracing: OpenTelemetry integrated  
✅ Logging: JSON + console  
✅ Evaluation: 3-tier metrics (queries + runner + report)  
✅ Agent Builder: Compatible  

---

**Updated:** 2026-01-15 | **Version:** 1.0.0
