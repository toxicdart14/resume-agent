# agents/rewriter.py
import os
from pathlib import Path
from agents.prompts import REWRITE_PROMPT

def call_llm(prompt_text: str) -> str:
    try:
        import openai
        openai.api_key = os.getenv("OPENAI_API_KEY")
        resp = openai.ChatCompletion.create(model="gpt-4o-mini", messages=[{"role":"user","content":prompt_text}], temperature=0.2)
        return resp.choices[0].message.content
    except Exception:
        return "MOCK_REWRITE\n" + prompt_text[:800]  # fallback for offline testing

def rewrite_resume(original_text: str) -> str:
    prompt = REWRITE_PROMPT.format(original_text=original_text)
    rewritten = call_llm(prompt)
    out = Path("data/output/rewritten_resume.txt")
    out.write_text(rewritten, encoding="utf-8")
    return rewritten

if __name__ == "__main__":
    txt = Path("data/extracted.txt").read_text(encoding="utf-8")
    print(rewrite_resume(txt)[:400])
