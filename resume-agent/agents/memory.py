# agents/memory.py
from pathlib import Path
import json
from datetime import datetime

MEM_DIR = Path("data/memory")
MEM_DIR.mkdir(parents=True, exist_ok=True)

def save_version(candidate_id: str, stage: str, text: str) -> str:
    """
    stage: 'original' | 'rewritten' | 'final'
    Returns path to saved file.
    """
    ts = datetime.now().strftime("%Y%m%dT%H%M%S")
    fname = MEM_DIR / f"{candidate_id}__{stage}__{ts}.json"
    payload = {"candidate_id": candidate_id, "stage": stage, "timestamp": ts, "text": text}
    fname.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return str(fname)

def list_versions(candidate_id: str):
    return sorted([p.name for p in MEM_DIR.glob(f"{candidate_id}__*.json")])
