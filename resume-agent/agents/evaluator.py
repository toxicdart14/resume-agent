
# agents/evaluator.py
"""
Contracts:
- evaluate_resume(original_text: str, rewritten_text: str, candidate_id: str) -> dict
- saves report.json to data/output/
"""
import re
import json
from datetime import datetime
from pathlib import Path

OUTPUT_DIR = Path("data/output")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# small action-verb list (extendable)
ACTION_VERBS = {
    "led","managed","developed","implemented","optimized","designed",
    "built","created","improved","reduced","increased","streamlined",
    "automated","orchestrated","launched","drove"
}

def count_numbers(text: str) -> int:
    return len(re.findall(r"\b\d+%?|\b\d+\.\d+\b", text))

def count_action_verbs(text: str) -> int:
    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    return sum(1 for w in words if w in ACTION_VERBS)

def avg_sentence_length(text: str) -> float:
    sentences = re.split(r'[.!?]\s+', text.strip())
    sentences = [s for s in sentences if s]
    if not sentences:
        return 0.0
    word_counts = [len(re.findall(r"\b\w+\b", s)) for s in sentences]
    return sum(word_counts) / len(word_counts)

def score_bucket(value, thresholds):
    """
    thresholds: list of increasing thresholds mapping to bucket scores (0..max)
    Return 0..max_score scaled to 0-20 (max 20)
    """
    max_score = 20
    for i, th in enumerate(thresholds):
        if value <= th:
            return int((i / (len(thresholds)-1)) * max_score)
    return max_score

def evaluate_resume(original_text: str, rewritten_text: str, candidate_id: str="candidate") -> dict:
    # Metrics: number of quantified metrics in rewritten_text (numbers, %)
    metrics_count = count_numbers(rewritten_text)

    # Action verbs: count unique action verbs used
    action_count = count_action_verbs(rewritten_text)

    # Quantification: same as metrics_count but more weight if numbers present in bullets
    quant_count = metrics_count

    # Relevance: naive proxy = shared unique words between original and rewritten (higher implies rewritten preserved relevance)
    o_words = set(re.findall(r"\b[a-zA-Z]{3,}\b", original_text.lower()))
    r_words = set(re.findall(r"\b[a-zA-Z]{3,}\b", rewritten_text.lower()))
    if not o_words:
        relevance_pct = 0.0
    else:
        relevance_pct = (len(o_words & r_words) / len(o_words)) * 100

    # Readability: average sentence length; shorter is often clearer
    asl = avg_sentence_length(rewritten_text)

    # Convert raw measures to 0-20 buckets
    metrics_score = score_bucket(metrics_count, [0,1,2,4,8,999])
    action_score  = score_bucket(action_count, [0,1,3,6,10,999])
    quant_score   = score_bucket(quant_count, [0,1,2,4,8,999])
    relevance_score = int(min(20, round((relevance_pct/100)*20)))  # proportion of 20
    # readability: ideal avg sentence length ~12 -> give max near 8-14
    # lower than 8 or higher than 20 penalized
    if asl == 0:
        readability_score = 0
    elif 8 <= asl <= 14:
        readability_score = 20
    elif asl < 8:
        readability_score = int(max(0, 20 - (8-asl)*2))
    else:
        readability_score = int(max(0, 20 - (asl-14)*1.5))

    scores = {
        "metrics_achievement": metrics_score,
        "action_verbs": action_score,
        "quantification": quant_score,
        "relevance": relevance_score,
        "readability": readability_score
    }
    overall = sum(scores.values())

    # simple diff-like top changes: find lines that differ
    def top_changes(orig, rew, max_items=6):
        o_lines = [l.strip() for l in orig.splitlines() if l.strip()]
        r_lines = [l.strip() for l in rew.splitlines() if l.strip()]
        changes = []
        # naive: lines in rewritten not in original -> additions
        added = [l for l in r_lines if l not in o_lines]
        for i, l in enumerate(added[:max_items]):
            changes.append({"index": i, "type": "added_line", "summary": l[:200]})
        # lines removed
        removed = [l for l in o_lines if l not in r_lines]
        for i, l in enumerate(removed[:max_items]):
            changes.append({"index": i, "type": "removed_line", "summary": l[:200]})
        return changes

    changes = top_changes(original_text, rewritten_text, max_items=6)

    report = {
        "candidate_id": candidate_id,
        "overall_score": overall,
        "scores": scores,
        "top_changes": changes,
        "changed_lines": [],  # could be filled by a line-diff routine later
        "timestamp": datetime.now().astimezone().isoformat()
    }

    # save report
    out_path = OUTPUT_DIR / f"{candidate_id}_report.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    return report

if __name__ == "__main__":
    # quick local smoke test
    sample_o = "Worked on team. Responsible for debugging. Increased throughput by 10%."
    sample_r = "Led a 5-person team that increased throughput by 10% and reduced latency by 20%."
    r = evaluate_resume(sample_o, sample_r, candidate_id="sample")
    print("Report saved:", r)
