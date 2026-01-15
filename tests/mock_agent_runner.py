#!/usr/bin/env python3
"""
Mock Evaluation Runner - Generates mock responses for evaluation testing.
Useful when network access is limited or for testing evaluation logic itself.
"""

import json
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime


def generate_mock_response(query_id: str, query_name: str, input_text: str) -> Dict[str, Any]:
    """Generate mock taxonomies and categories for a query"""
    
    # Mock taxonomy based on query type
    mock_taxonomies = {
        "query_001": {
            "primary": ["Frontend", "Backend", "DevOps", "Testing"],
            "secondary": ["Mobile Development", "Performance", "Error Handling", "Browser Compatibility"],
            "impact_score": 0.78
        },
        "query_002": {
            "primary": ["Architecture", "Security", "Infrastructure", "Frontend", "Backend"],
            "secondary": ["API Design", "Caching", "Monitoring", "Accessibility", "Performance Optimization"],
            "impact_score": 0.92
        },
        "query_003": {
            "primary": ["Features", "Backend", "Frontend", "Infrastructure"],
            "secondary": ["File Handling", "Real-time Communication", "Authentication", "Internationalization", "Search"],
            "impact_score": 0.85
        },
        "query_004": {
            "primary": ["Critical", "Security", "Performance", "Data Integrity"],
            "secondary": ["Payment Systems", "Session Management", "Storage Management", "Email Delivery"],
            "impact_score": 0.99
        },
        "query_005": {
            "primary": ["Backend", "Performance", "Scalability"],
            "secondary": ["Load Balancing", "Database Optimization", "Caching", "Network Latency"],
            "impact_score": 0.88
        },
        "query_006": {
            "primary": ["Security", "DevOps", "Backend"],
            "secondary": ["Encryption", "Access Control", "Vulnerability Assessment", "Incident Response"],
            "impact_score": 0.95
        },
        "query_007": {
            "primary": ["Infrastructure", "DevOps", "Backend"],
            "secondary": ["Containerization", "Orchestration", "Configuration Management", "CI/CD"],
            "impact_score": 0.82
        },
        "query_008": {
            "primary": ["Frontend", "Backend", "Organization"],
            "secondary": ["Team Communication", "Code Review", "Documentation", "Knowledge Sharing"],
            "impact_score": 0.72
        },
        "query_009": {
            "primary": ["Backend", "Data", "Analytics"],
            "secondary": ["Data Processing", "Reporting", "Query Optimization", "Visualization"],
            "impact_score": 0.80
        },
        "query_010": {
            "primary": ["Architecture", "Backend", "Security", "Scalability"],
            "secondary": ["Enterprise Integration", "Compliance", "Multi-tenancy", "High Availability"],
            "impact_score": 0.90
        }
    }
    
    taxonomy = mock_taxonomies.get(query_id, {
        "primary": ["General", "Other"],
        "secondary": ["Miscellaneous"],
        "impact_score": 0.5
    })
    
    # Mock categories
    categories = {
        "query_001": ["Mobile Bug", "API Performance", "Code Quality", "Browser Support"],
        "query_002": ["Debt Remediation", "Architecture Refactoring", "Performance Optimization", "DevOps Improvement"],
        "query_003": ["Feature Development", "Dependency Management", "Integration Planning"],
        "query_004": ["Critical Incident", "Revenue Impact", "Data Risk", "System Reliability"],
        "query_005": ["Scalability Issue", "Resource Constraint", "Geographic Distribution"],
        "query_006": ["Threat Assessment", "Vulnerability", "Security Hardening", "Compliance"],
        "query_007": ["Infrastructure Modernization", "Deployment Automation", "Container Orchestration"],
        "query_008": ["Team Coordination", "Process Improvement", "Documentation Need"],
        "query_009": ["Data Pipeline", "Analytics Enhancement", "Reporting Capability"],
        "query_010": ["Enterprise Architecture", "System Design", "Regulatory Compliance"]
    }
    
    return {
        "query_id": query_id,
        "query_name": query_name,
        "input": input_text,
        "output": {
            "taxonomy": taxonomy,
            "categories": categories.get(query_id, ["General"]),
            "priority_areas": [tax for tax in taxonomy.get("secondary", [])[:3]],
            "index_entries": [{"category": cat, "relevance": 0.8} for cat in categories.get(query_id, ["General"])[:3]],
            "audit_notes": "Mock response for testing - generated automatically"
        },
        "status": "success",
        "execution_time": 5.2,
        "timestamp": datetime.now().isoformat(),
        "metadata": {
            "source": "mock_generator",
            "categories_count": len(categories.get(query_id, ["General"])),
            "primary_count": len(taxonomy.get("primary", [])),
            "secondary_count": len(taxonomy.get("secondary", []))
        }
    }


async def generate_mock_responses():
    """Load queries and generate mock responses"""
    
    queries_file = Path(__file__).parent / "queries.json"
    responses_file = Path(__file__).parent / "responses.json"
    
    print("Loading queries...")
    with open(queries_file) as f:
        queries = json.load(f)
    
    print(f"Loaded {len(queries)} queries")
    
    responses = []
    for i, query_data in enumerate(queries, 1):
        query_id = query_data.get("id")
        query_name = query_data.get("name")
        query_input = query_data.get("input", "")
        
        print(f"[{i}/{len(queries)}] Generating response for {query_id}...")
        
        response = generate_mock_response(query_id, query_name, query_input)
        responses.append(response)
    
    # Save responses
    print(f"\nSaving {len(responses)} responses to {responses_file}...")
    with open(responses_file, 'w') as f:
        json.dump(responses, f, indent=2)
    
    print(f"✅ Mock responses generated: {responses_file}")
    return responses


if __name__ == "__main__":
    import asyncio
    responses = asyncio.run(generate_mock_responses())
    print(f"\nGenerated {len(responses)} responses ready for evaluation")
