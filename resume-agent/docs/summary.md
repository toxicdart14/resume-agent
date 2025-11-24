Title: Multi-Agent Resume Improvement System
Subtitle: Automated resume rewrite, scoring, and versioned memory for fast career polish.

Project overview:
This project builds a compact multi-agent pipeline that converts an input resume into an achievement-focused version, scores improvements using an automated rubric, and stores versioned artifacts for traceability. It demonstrates parser, rewriter (LLM), evaluator, memory, and observability in a clean architecture suitable for the Kaggle Capstone.

Architecture:
- Parser agent: extracts text from PDF → data/extracted.txt
- Rewriter agent: LLM prompt-driven rewrite → data/output/rewritten_resume.txt
- Evaluator agent: computes rubric, saves report.json
- Memory service: stores original & rewritten snapshots
- Observability: logs + metrics CSV

Demo & results:
Run `demo_script.py` or the included notebook to see an end-to-end demo with a sample resume. The evaluator outputs per-category scores and a change summary. This submission uses conservative numeric placeholders to avoid hallucination and documents all pipeline steps.

How to reproduce:
1. Clone repo, install requirements.
2. Add `data/candidate_raw.pdf`.
3. Run notebook or `demo_script.py`.
4. Inspect outputs in `data/output/` and `data/memory/`.

Why agents:
The multi-agent structure provides separation of concerns, traceability, and the ability to extend (e.g., add role-specific benchmark agents or deployable endpoints) without refactoring core logic.

Repository: [add GitHub repo URL here]
YouTube (optional): [add video URL here]
