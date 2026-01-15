#!/usr/bin/env python3
"""
Agent Runner - Executa o orchestrator_agent com queries de teste e recolhe responses.
Usado para evaluation completa.
"""

import asyncio
import json
import sys
import time
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_config import load_config
from executors import run_full_pipeline


async def run_query(query_data: Dict[str, Any], query_index: int, total_queries: int) -> Dict[str, Any]:
    """
    Executa uma query individual com o orchestrator_agent.
    
    Args:
        query_data: Dict com 'id', 'name', 'input' da query
        query_index: Índice da query (1-based para logging)
        total_queries: Total de queries a processar
        
    Returns:
        Dict com resultado contendo input, output, metadata
    """
    query_id = query_data.get("id", f"query_{query_index:03d}")
    query_name = query_data.get("name", "Unnamed Query")
    query_input = query_data.get("input", "")
    
    print(f"\n[{query_index}/{total_queries}] Processing: {query_id} - {query_name}")
    print(f"Input length: {len(query_input)} chars")
    
    start_time = time.time()
    
    try:
        # Carregar configuração
        cfg = load_config()
        
        # Executar pipeline completo com timeout de 120 segundos
        try:
            results = await asyncio.wait_for(run_full_pipeline(query_input, cfg), timeout=120.0)
        except asyncio.TimeoutError:
            elapsed = time.time() - start_time
            print(f"❌ TIMEOUT: Query took more than 120 seconds")
            return {
                "query_id": query_id,
                "input": query_input,
                "output": None,
                "status": "timeout",
                "error": "Query execution exceeded 120 second timeout",
                "execution_time": elapsed
            }
        
        elapsed = time.time() - start_time
        
        # Extrair outputs principais
        output = {
            "classifier": results.get("classifier", {}).content if "classifier" in results else "",
            "taxonomy_raw": results.get("taxonomy_raw", {}).content if "taxonomy_raw" in results else "",
            "taxonomy_refined": results.get("taxonomy_refined", {}).content if "taxonomy_refined" in results else "",
            "index_architect": results.get("index_architect", {}).content if "index_architect" in results else "",
            "auditor": results.get("auditor", {}).content if "auditor" in results else "",
        }
        
        # Contar categories
        category_keys = [k for k in results.keys() if "curator" in k]
        category_count = len(category_keys)
        
        response = {
            "query_id": query_id,
            "query_name": query_name,
            "input": query_input,
            "output": output,
            "metadata": {
                "status": "success",
                "execution_time_seconds": round(elapsed, 2),
                "categories_generated": category_count,
                "timestamp": datetime.now().isoformat(),
            }
        }
        
        print(f"✅ Success - Execution time: {elapsed:.2f}s, Categories: {category_count}")
        return response
        
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"❌ Error - {str(e)[:100]}")
        
        return {
            "query_id": query_id,
            "query_name": query_name,
            "input": query_input,
            "output": {},
            "metadata": {
                "status": "error",
                "error": str(e),
                "execution_time_seconds": round(elapsed, 2),
                "timestamp": datetime.now().isoformat(),
            }
        }


async def run_agent_evaluation():
    """
    Função principal - carrega queries, executa agent runner, guarda responses.
    """
    
    # Paths
    repo_root = Path(__file__).parent.parent
    queries_file = repo_root / "tests" / "queries.json"
    responses_file = repo_root / "tests" / "responses.json"
    
    print("=" * 70)
    print("🚀 Agent Runner - Evaluation Response Collection")
    print("=" * 70)
    
    # Validar queries.json existe
    if not queries_file.exists():
        print(f"❌ Queries file not found: {queries_file}")
        return False
    
    # Carregar queries
    print(f"\n📂 Loading queries from: {queries_file}")
    with open(queries_file, "r", encoding="utf-8") as f:
        queries = json.load(f)
    
    total_queries = len(queries)
    print(f"✅ Loaded {total_queries} test queries")
    
    # Executar runner
    print("\n" + "=" * 70)
    print(f"▶️  Running {total_queries} queries through orchestrator_agent...")
    print("=" * 70)
    
    start_time = time.time()
    responses = []
    
    for idx, query_data in enumerate(queries, start=1):
        response = await run_query(query_data, idx, total_queries)
        responses.append(response)
        
        # Pequena pausa entre queries
        if idx < total_queries:
            await asyncio.sleep(1)
    
    total_elapsed = time.time() - start_time
    
    # Estatísticas
    print("\n" + "=" * 70)
    print("📊 Evaluation Summary")
    print("=" * 70)
    
    successful = sum(1 for r in responses if r["metadata"]["status"] == "success")
    failed = total_queries - successful
    
    print(f"Total queries: {total_queries}")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"Total execution time: {total_elapsed:.2f}s")
    print(f"Average per query: {total_elapsed / total_queries:.2f}s")
    
    # Guardar responses
    print(f"\n💾 Saving responses to: {responses_file}")
    
    with open(responses_file, "w", encoding="utf-8") as f:
        json.dump(
            {
                "metadata": {
                    "total_queries": total_queries,
                    "successful": successful,
                    "failed": failed,
                    "total_execution_time_seconds": round(total_elapsed, 2),
                    "timestamp": datetime.now().isoformat(),
                },
                "responses": responses
            },
            f,
            indent=2,
            ensure_ascii=False
        )
    
    print(f"✅ Responses saved successfully")
    
    # Summary por status
    print("\n" + "-" * 70)
    print("Results by Query:")
    print("-" * 70)
    
    for response in responses:
        status = "✅" if response["metadata"]["status"] == "success" else "❌"
        exec_time = response["metadata"]["execution_time_seconds"]
        print(f"{status} {response['query_id']:15} | {response['query_name']:40} | {exec_time:6.2f}s")
    
    print("\n" + "=" * 70)
    print(f"✅ Agent Runner Complete - {successful}/{total_queries} successful")
    print("=" * 70)
    
    return failed == 0


if __name__ == "__main__":
    success = asyncio.run(run_agent_evaluation())
    sys.exit(0 if success else 1)
