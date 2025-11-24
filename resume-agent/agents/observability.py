# agents/observability.py
import logging
from pathlib import Path
import csv
from datetime import datetime

LOG_PATH = Path("logs")
LOG_PATH.mkdir(parents=True, exist_ok=True)
logging.basicConfig(filename=LOG_PATH / "pipeline.log",
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

METRICS_CSV = LOG_PATH / "metrics.csv"
if not METRICS_CSV.exists():
    with open(METRICS_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp","candidate_id","overall_score","metrics_achievement","action_verbs","quantification","relevance","readability"])

def record_metrics(candidate_id: str, report: dict):
    with open(METRICS_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        scores = report.get("scores", {})
        writer.writerow([
            datetime.now().isoformat(),
            candidate_id,
            report.get("overall_score", ""),
            scores.get("metrics_achievement",""),
            scores.get("action_verbs",""),
            scores.get("quantification",""),
            scores.get("relevance",""),
            scores.get("readability","")
        ])
    logging.info(f"Recorded metrics for {candidate_id}: overall={report.get('overall_score')}")
