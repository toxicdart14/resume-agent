# Input / Output Formats

## Input (accepted by pipeline)
- `data/*.pdf` or `data/*.txt`
- Parser function signature: `extract_text(path: str) -> str`
- Supported encoding: UTF-8

## Primary Outputs (saved to `data/output/`)
1. `rewritten_resume.txt` — full rewritten resume text (plain text).
2. `rewritten_resume.pdf` — (optional) rendered PDF of rewritten resume.
3. `linkedin_summary.txt` — 1–3 sentence LinkedIn summary for candidate.
4. `report.json` — evaluator report with scores and highlights.

## report.json schema (example)
```json
{
  "candidate_id": "candidate_raw",
  "overall_score": 72,
  "scores": {
    "metrics_achievement": 18,
    "action_verbs": 14,
    "quantification": 16,
    "relevance": 12,
    "readability": 12
  },
  "top_changes": [
    {"line": 42, "type": "add_metric", "summary": "Added KPI: reduced costs by 12%"},
    {"line": 10, "type": "rewrite_bullet", "summary": "Converted duty to achievement"}
  ],
  "changed_lines": [10, 22, 42],
  "timestamp": "2025-11-24T12:00:00+05:30"
}

2. Create example outputs under `data/output/`:
- `data/output/rewritten_resume.txt` — paste a one-paragraph placeholder:  
  `Rewritten resume for Candidate Raw — highlights: increased sales 20%, led 5-member team...`
- `data/output/linkedin_summary.txt` — example:  
  `Product-focused software engineer with 3+ years building scalable web services and driving 20% YOY revenue growth.`
- `data/output/report.json` — use the JSON example above (fill `candidate_id` accordingly).

3. Add to `README.md` (brief line) — paste:


4. Code contract (place in `agents/parser.py` and `agents/evaluator.py` docstrings):
- `extract_text(path: str) -> str`
- `evaluate_resume(original_text: str, rewritten_text: str) -> dict`  # returns a dict matching report.json schema

Do these three file edits now. Once done, I’ll generate the `evaluate_resume` scaffold and a runnable example that writes `report.json`.
