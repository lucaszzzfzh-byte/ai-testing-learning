# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

Personal AI testing self-study project by 樊泽豪. The learner is a 2026 CS graduate self-teaching AI testing over 3 months (6 stages). Claude serves as a **supplementary teaching assistant** — the user wants to do most operations themselves, with Claude providing guidance and debugging help only.

## Tech Stack

- **Python 3** with Anthropic SDK (`anthropic`) calling DeepSeek's Anthropic-compatible endpoint
- **Virtual environment**: `venv/` in project root
- **Dify** for Agent/chatflow workflows (Stage 1)
- **GitHub** repo: `https://github.com/lucaszzzfzh-byte/ai-testing-learning` (public)

## Environment Setup

```bash
# Activate venv (Git Bash, from project root)
source venv/Scripts/activate

# Deactivate
deactivate
```

## API Configuration Pattern

All API calls use the Anthropic SDK pointed at DeepSeek's endpoint. Copy this pattern for new scripts:

```python
from anthropic import Anthropic

client = Anthropic(
    api_key="<deepseek-api-key>",
    base_url="https://api.deepseek.com/anthropic"
)

response = client.messages.create(
    model="deepseek-chat",
    max_tokens=2000,
    temperature=0.3,
    thinking={"type": "disabled"},  # REQUIRED — DeepSeek has thinking ON by default
    system="<system prompt>",
    messages=[{"role": "user", "content": "<user message>"}]
)
```

Key gotchas:
- `thinking={"type": "disabled"}` is mandatory, otherwise API returns 400
- Use `deepseek-chat` model (not `deepseek-v4-pro` — that's only for Claude Code proxy)
- API keys are stored in-project (not environment variables) — do not commit real keys

## Git Workflow

```bash
git add <specific-files>
git commit -m "<message>"
git push origin main
```

Current commit history: `day1: prompt engineering basics`

## File Naming

Learning files follow pattern: `lesson<N>_<topic>.py` or `<topic>_practice.py`. All project files live in `F:/ClaudeData/ai-testing-learning/`.
