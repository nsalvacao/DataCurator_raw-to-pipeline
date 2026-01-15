import asyncio
from pathlib import Path

from dotenv import load_dotenv
from openai import AsyncOpenAI

from executors import run_full_pipeline
from workflow_config import load_config


async def main():
    load_dotenv()
    cfg = load_config()

    sample_raw_notes_path = Path(cfg.paths.root / "samples" / "raw_notes.md")
    if sample_raw_notes_path.exists():
        raw_notes = sample_raw_notes_path.read_text(encoding="utf-8")
    else:
        raw_notes = """Provide the development notes content here.\n- Example: Login fails on Safari 16.\n- Example: API latency > 800ms P95 on /orders endpoint.\n"""

    results = await run_full_pipeline(raw_notes, cfg)

    out_dir = cfg.paths.root / "outputs"
    out_dir.mkdir(exist_ok=True)

    # Write a concise summary file
    summary_lines = []
    for name, res in results.items():
        summary_lines.append(f"## {name}\n\n{res.content}\n")
    (out_dir / "pipeline_summary.md").write_text("\n".join(summary_lines), encoding="utf-8")

    print("Pipeline finished. Results written to outputs/pipeline_summary.md")


if __name__ == "__main__":
    asyncio.run(main())
