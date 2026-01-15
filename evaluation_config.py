"""
Evaluation Setup - Métricas e validadores para avaliar o orchestrator_agent
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum


class MetricType(Enum):
    """Tipos de métricas de avaliação"""
    CORRECTNESS = "output_correctness"
    QUALITY = "content_quality"
    COMPLETENESS = "completeness"


@dataclass
class EvaluationMetric:
    """Definição de uma métrica de avaliação"""
    name: str
    type: MetricType
    description: str
    implementation: str  # Nome da função validadora
    target_score: float = 0.8  # Score mínimo esperado (0.0-1.0)


class OutputCorrectnessEvaluator:
    """
    Valida se as categorias extraídas, prioridades e roadmaps estão 
    estruturalmente corretos e coerentes.
    """
    
    @staticmethod
    def evaluate(response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Avaliar output correctness.
        
        Checks:
        - Output structure is valid
        - Categories have required fields
        - Taxonomies are consistent
        - No missing critical sections
        """
        issues = []
        score = 1.0
        
        output = response.get("output", {})
        
        # Check classifier output
        if not output.get("classifier"):
            issues.append("Missing classifier output")
            score -= 0.15
        
        # Check taxonomy outputs
        if not output.get("taxonomy_raw"):
            issues.append("Missing taxonomy_raw output")
            score -= 0.10
        
        if not output.get("taxonomy_refined"):
            issues.append("Missing taxonomy_refined output")
            score -= 0.10
        
        # Check index architect (roadmap master)
        if not output.get("index_architect"):
            issues.append("Missing index_architect (roadmap) output")
            score -= 0.20
        
        # Check audit report
        if not output.get("auditor"):
            issues.append("Missing auditor report")
            score -= 0.10
        
        # Verificar taxonomy refinement (refined deve ser > raw)
        taxonomy_raw = output.get("taxonomy_raw", "")
        taxonomy_refined = output.get("taxonomy_refined", "")
        
        if taxonomy_raw and taxonomy_refined:
            if len(taxonomy_refined) < len(taxonomy_raw) * 0.5:
                issues.append("Taxonomy refinement seems too concise")
                score -= 0.05
        
        # Verificar roadmap completeness
        roadmap = output.get("index_architect", "")
        roadmap_sections = [
            "Executive Dashboard",
            "Program Overview",
            "Category Portfolio",
            "Critical Path",
            "Risk",
        ]
        
        for section in roadmap_sections:
            if section not in roadmap:
                issues.append(f"Missing roadmap section: {section}")
                score -= 0.05
        
        return {
            "metric": "output_correctness",
            "score": max(0.0, min(1.0, score)),
            "passed": score >= 0.8,
            "issues": issues,
            "issue_count": len(issues),
        }


class ContentQualityEvaluator:
    """
    Avalia se as soluções propostas são apropriadas, detalhadas e executáveis.
    """
    
    @staticmethod
    def evaluate(response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Avaliar content quality.
        
        Checks:
        - Solutions are detailed enough
        - Recommendations are actionable
        - Multiple options provided where appropriate
        - Content is well-structured
        """
        issues = []
        score = 1.0
        
        output = response.get("output", {})
        input_text = response.get("input", "")
        
        # Check minimum content length
        total_output_length = sum(
            len(str(output.get(key, ""))) 
            for key in ["classifier", "taxonomy_raw", "taxonomy_refined", "index_architect", "auditor"]
        )
        
        input_length = len(input_text)
        
        # Output deve ser significativamente maior que input
        if total_output_length < input_length * 2:
            issues.append("Output length inadequate compared to input")
            score -= 0.15
        
        # Check for detailed analysis in classifier
        classifier = output.get("classifier", "")
        if classifier and len(classifier) < 200:
            issues.append("Classifier output too brief")
            score -= 0.10
        
        # Check for solutions/recommendations in refiner
        refiner = output.get("taxonomy_refined", "")
        quality_keywords = [
            "effort", "days", "owner", "solution", "recommendation",
            "priority", "p0", "p1", "p2", "phasecompletion",
        ]
        
        found_keywords = sum(
            1 for keyword in quality_keywords 
            if keyword.lower() in refiner.lower()
        )
        
        if found_keywords < len(quality_keywords) * 0.4:
            issues.append("Missing detailed solution recommendations")
            score -= 0.10
        
        # Check roadmap actionability
        roadmap = output.get("index_architect", "")
        actionable_keywords = [
            "timeline", "effort", "owner", "phase", "action", "task",
            "completion", "metric", "kpi", "success criteria",
        ]
        
        found_actionable = sum(
            1 for keyword in actionable_keywords 
            if keyword.lower() in roadmap.lower()
        )
        
        if found_actionable < len(actionable_keywords) * 0.5:
            issues.append("Roadmap lacks actionability")
            score -= 0.10
        
        return {
            "metric": "content_quality",
            "score": max(0.0, min(1.0, score)),
            "passed": score >= 0.8,
            "issues": issues,
            "issue_count": len(issues),
            "output_length": total_output_length,
            "input_length": input_length,
        }


class CompletenessEvaluator:
    """
    Verifica se todos os problemas foram processados e nenhum foi perdido.
    """
    
    @staticmethod
    def evaluate(response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Avaliar completeness.
        
        Checks:
        - All input problems are represented in output
        - Categories are generated from input
        - Taxonomy covers all problems
        - No data loss in pipeline
        """
        issues = []
        score = 1.0
        
        input_text = response.get("input", "")
        output = response.get("output", {})
        metadata = response.get("metadata", {})
        
        # Count problems in input
        problem_indicators = [
            "-", "bug", "issue", "error", "problem", "feature",
            "blocker", "critical", "high", "medium", "low",
        ]
        
        input_lines = input_text.split("\n")
        problem_lines = [
            line for line in input_lines 
            if any(indicator in line.lower() for indicator in problem_indicators)
        ]
        
        input_problem_count = len([l for l in problem_lines if l.strip()])
        
        # Check categories generated
        categories_generated = metadata.get("categories_generated", 0)
        
        if input_problem_count > 0 and categories_generated == 0:
            issues.append("No categories generated from input")
            score -= 0.25
        
        # Check taxonomy coverage
        taxonomy = output.get("taxonomy_raw", "") + output.get("taxonomy_refined", "")
        
        if input_problem_count > 0 and not taxonomy:
            issues.append("No taxonomy generated from problems")
            score -= 0.25
        
        # Verificar que roadmap menciona categorias
        roadmap = output.get("index_architect", "")
        
        if "CAT-" not in roadmap and categories_generated > 0:
            issues.append("Roadmap doesn't reference generated categories")
            score -= 0.15
        
        # Check execution status
        status = metadata.get("status", "")
        if status == "error":
            issues.append("Pipeline execution failed")
            score -= 0.50
        
        return {
            "metric": "completeness",
            "score": max(0.0, min(1.0, score)),
            "passed": score >= 0.8,
            "issues": issues,
            "issue_count": len(issues),
            "input_problem_count": input_problem_count,
            "categories_generated": categories_generated,
        }


class EvaluationRunner:
    """
    Execute evaluation on responses.
    """
    
    EVALUATORS = [
        OutputCorrectnessEvaluator(),
        ContentQualityEvaluator(),
        CompletenessEvaluator(),
    ]
    
    @classmethod
    def evaluate_response(cls, response: Dict[str, Any]) -> Dict[str, Any]:
        """
        Avaliar uma response individual.
        
        Args:
            response: Response dict com input, output, metadata
            
        Returns:
            Dict com resultados de evaluation
        """
        results = {
            "query_id": response.get("query_id"),
            "metrics": {},
            "overall_score": 0.0,
            "all_passed": True,
        }
        
        metric_scores = []
        
        for evaluator in cls.EVALUATORS:
            metric_result = evaluator.evaluate(response)
            metric_name = metric_result.get("metric")
            results["metrics"][metric_name] = metric_result
            
            metric_scores.append(metric_result.get("score", 0.0))
            
            if not metric_result.get("passed", False):
                results["all_passed"] = False
        
        # Calculate overall score
        if metric_scores:
            results["overall_score"] = sum(metric_scores) / len(metric_scores)
        
        return results
    
    @classmethod
    def evaluate_batch(cls, responses: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Avaliar um batch de responses.
        
        Args:
            responses: List de response dicts
            
        Returns:
            Dict com resultados agregados
        """
        evaluation_results = []
        scores = []
        
        for response in responses:
            result = cls.evaluate_response(response)
            evaluation_results.append(result)
            scores.append(result.get("overall_score", 0.0))
        
        return {
            "total_responses": len(responses),
            "overall_average_score": sum(scores) / len(scores) if scores else 0.0,
            "passed_count": sum(1 for r in evaluation_results if r["all_passed"]),
            "failed_count": sum(1 for r in evaluation_results if not r["all_passed"]),
            "results": evaluation_results,
        }


def run_evaluation(responses_file: Path) -> Dict[str, Any]:
    """
    Carregar responses e rodar evaluation.
    
    Args:
        responses_file: Path para ficheiro de responses.json
        
    Returns:
        Dict com resultados de evaluation
    """
    if not responses_file.exists():
        raise FileNotFoundError(f"Responses file not found: {responses_file}")
    
    with open(responses_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    responses = data.get("responses", [])
    
    if not responses:
        raise ValueError("No responses found in file")
    
    return EvaluationRunner.evaluate_batch(responses)
