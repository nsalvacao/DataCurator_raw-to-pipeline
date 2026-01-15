#!/usr/bin/env python3
"""
Evaluation Runner - Executa evaluation completa sobre responses coletadas.
Gera relatório detalhado com métricas, scores e recomendações.
"""

import json
import sys
from pathlib import Path
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from evaluation_config import EvaluationRunner


def run_evaluation_report(responses_file: Path, output_file: Path = None) -> bool:
    """
    Executar evaluation e gerar relatório.
    
    Args:
        responses_file: Path para responses.json
        output_file: Path para guardar relatório (default: evaluation_report.json)
        
    Returns:
        True se evaluation passou, False caso contrário
    """
    
    if not responses_file.exists():
        print(f"❌ Responses file not found: {responses_file}")
        return False
    
    if output_file is None:
        output_file = responses_file.parent / "evaluation_report.json"
    
    print("=" * 80)
    print("📊 Evaluation Runner - Comprehensive Assessment")
    print("=" * 80)
    
    # Load responses
    print(f"\n📂 Loading responses from: {responses_file}")
    with open(responses_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    # Handle both list and dict formats
    if isinstance(data, list):
        responses = data
        metadata = {"total_queries": len(responses), "successful": len(responses)}
    else:
        responses = data.get("responses", [])
        metadata = data.get("metadata", {})
    
    total_responses = metadata.get("total_queries", len(responses))
    successful_runs = metadata.get("successful", 0)
    
    print(f"✅ Loaded {len(responses)} responses")
    print(f"   Successful agent runs: {successful_runs}/{total_responses}")
    
    # Run evaluation
    print(f"\n▶️  Running evaluation metrics...")
    evaluation_results = EvaluationRunner.evaluate_batch(responses)
    
    # Generate report
    report = {
        "timestamp": datetime.now().isoformat(),
        "evaluation_summary": {
            "total_queries": total_responses,
            "agent_runs_successful": successful_runs,
            "agent_runs_failed": total_responses - successful_runs,
            "total_responses_evaluated": len(responses),
        },
        "metrics_summary": {
            "overall_average_score": evaluation_results.get("overall_average_score", 0.0),
            "passed": evaluation_results.get("passed_count", 0),
            "failed": evaluation_results.get("failed_count", 0),
            "pass_rate": (
                evaluation_results.get("passed_count", 0) / len(responses) * 100
                if responses else 0.0
            ),
        },
        "detailed_results": evaluation_results.get("results", []),
    }
    
    # Print summary
    print("\n" + "=" * 80)
    print("📊 EVALUATION SUMMARY")
    print("=" * 80)
    
    print(f"\n🎯 Overall Average Score: {report['metrics_summary']['overall_average_score']:.2%}")
    print(f"✅ Passed: {report['metrics_summary']['passed']}/{len(responses)}")
    print(f"❌ Failed: {report['metrics_summary']['failed']}/{len(responses)}")
    print(f"📈 Pass Rate: {report['metrics_summary']['pass_rate']:.1f}%")
    
    # Breakdown by metric
    print("\n" + "-" * 80)
    print("Metrics Breakdown:")
    print("-" * 80)
    
    metric_scores = {}
    for result in evaluation_results.get("results", []):
        for metric_name, metric_data in result.get("metrics", {}).items():
            if metric_name not in metric_scores:
                metric_scores[metric_name] = []
            metric_scores[metric_name].append(metric_data.get("score", 0.0))
    
    for metric_name, scores in sorted(metric_scores.items()):
        avg_score = sum(scores) / len(scores) if scores else 0.0
        passed = sum(1 for score in scores if score >= 0.8)
        print(f"\n{metric_name.upper()}:")
        print(f"  Average Score: {avg_score:.2%}")
        print(f"  Passed: {passed}/{len(scores)}")
    
    # Detailed per-query results
    print("\n" + "=" * 80)
    print("Per-Query Results:")
    print("=" * 80)
    
    for result in sorted(
        evaluation_results.get("results", []),
        key=lambda x: x.get("overall_score", 0.0),
        reverse=True
    ):
        query_id = result.get("query_id", "unknown")
        score = result.get("overall_score", 0.0)
        status = "✅" if result.get("all_passed") else "❌"
        
        print(f"\n{status} {query_id:20} | Score: {score:.2%}")
        
        # Show issues if any
        for metric_name, metric_data in result.get("metrics", {}).items():
            issues = metric_data.get("issues", [])
            if issues:
                print(f"   Issues in {metric_name}:")
                for issue in issues:
                    print(f"     - {issue}")
    
    # Save report
    print("\n" + "=" * 80)
    print(f"💾 Saving evaluation report to: {output_file}")
    
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Report saved successfully")
    
    # Final verdict
    print("\n" + "=" * 80)
    overall_score = report["metrics_summary"]["overall_average_score"]
    
    if overall_score >= 0.8 and evaluation_results.get("passed_count", 0) == len(responses):
        print("🎉 EVALUATION PASSED - All metrics met targets!")
        verdict = "PASSED"
    elif overall_score >= 0.6:
        print("⚠️  EVALUATION PARTIAL - Some issues to address")
        verdict = "PARTIAL"
    else:
        print("❌ EVALUATION FAILED - Major issues detected")
        verdict = "FAILED"
    
    print(f"Overall Score: {overall_score:.2%}")
    print(f"Verdict: {verdict}")
    print("=" * 80)
    
    return overall_score >= 0.8


if __name__ == "__main__":
    repo_root = Path(__file__).parent
    responses_file = repo_root / "responses.json"
    
    success = run_evaluation_report(responses_file)
    sys.exit(0 if success else 1)
