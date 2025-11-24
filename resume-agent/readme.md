# Multi-Agent Resume Improvement System (Capstone)

## Summary
Lightweight multi-agent pipeline that ingests a resume PDF, rewrites it using an LLM-driven rewriter, evaluates improvements with a local evaluator, and stores versions in memory. Designed for fast reproducibility and presentation-quality deliverables for the Kaggle Google Agents Capstone.

## What it demonstrates (course concepts)
- Multi-agent flow: parser → rewriter → evaluator.
- Tools: LLM integration (with offline fallback), file I/O.
- Sessions & Memory: versioned candidate snapshots (data/memory).
- Observability: logs and metrics (logs/metrics.csv).
- Agent evaluation: automated rubric + report.json outputs.

## Quickstart
1. Install: `pip install -r requirements.txt`  
2. Place sample resume: `data/candidate_raw.pdf`  
3. Run demo cell or script: `python demo_script.py` (or run notebook)  
4. Outputs: `data/output/rewritten_resume.txt`, `data/output/<candidate>_report.json`, `data/memory/*.json`, `logs/metrics.csv`.

## Notes
- Do NOT commit API keys. Set `OPENAI_API_KEY` as env var to enable live LLM calls.
- License: MIT
