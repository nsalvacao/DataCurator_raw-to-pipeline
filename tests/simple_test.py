#!/usr/bin/env python3
"""
Simple test - One-query execution for debugging
"""

import asyncio
import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from workflow_config import load_config
from executors import run_full_pipeline


async def main():
    """Test one query"""
    
    # Load first query
    with open(Path(__file__).parent / "queries.json") as f:
        queries = json.load(f)
    
    query_data = queries[0]
    print(f"Testing: {query_data['name']}")
    print(f"Input: {query_data['input'][:100]}...")
    
    # Load config and run
    cfg = load_config()
    
    print("\nRunning pipeline...")
    try:
        results = await asyncio.wait_for(
            run_full_pipeline(query_data['input'], cfg),
            timeout=120.0
        )
        print("\n✅ SUCCESS!")
        print(f"Results keys: {results.keys()}")
        if 'classifier' in results:
            print(f"Classifier result: {str(results['classifier'])[:200]}...")
    except asyncio.TimeoutError:
        print("❌ TIMEOUT: Query exceeded 120 seconds")
    except Exception as e:
        print(f"❌ ERROR: {type(e).__name__}: {str(e)[:200]}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
