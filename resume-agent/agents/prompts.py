# agents/prompts.py
REWRITE_PROMPT = """
You are an expert resume writer. Rewrite the candidate's resume text to:
- Convert duties into achievements
- Add quantification when obvious (do NOT hallucinate exact numbers; suggest placeholders like <X>% if unsure)
- Use strong action verbs and concise bullets (max 14 words per bullet)
- Preserve factual content from the original
INPUT_RESUME:
{original_text}
OUTPUT_FORMAT:
Provide the rewritten resume as plain text. After the resume, include a short section "CHANGES_SUMMARY" with 5 concise change notes.
"""

LINKEDIN_PROMPT = """
You are a professional career copywriter. Based on the rewritten resume below, create a 1-2 sentence LinkedIn headline/summary emphasizing key strengths and metrics.
REWRITTEN_RESUME:
{rewritten_text}
OUTPUT:
1-2 sentence LinkedIn summary.
"""

EXPLAIN_CHANGES_PROMPT = """
You are an editor that explains rewrite decisions. Given ORIGINAL and REWRITTEN text, produce a JSON list of top 5 changes with:
- type: add_metric | rewrite_bullet | improved_verb
- location_hint: short excerpt from rewritten
- rationale: 1-line reason
ORIGINAL:
{original_text}
REWRITTEN:
{rewritten_text}
"""
