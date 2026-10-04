"""
srt-translator.py — translate SRT subtitle files with an LLM API, keeping timestamps intact.

Usage:
    python srt-translator.py input_zh.srt output_en.srt

Setup:
    pip install openai
    export OPENAI_API_KEY="sk-..."        # or any OpenAI-compatible endpoint
    # Or set BASE_URL to use an AI gateway, e.g. WorldRouter / OpenRouter:
    # export OPENAI_BASE_URL="https://router.worldclaw.ai/v1"

How it works:
    1. Parses the SRT into blocks (index, timestamp, text lines).
    2. Sends ONLY the text lines to the model in batches.
    3. Rebuilds the SRT with original timestamps + translated text.

Why batch + text-only:
    - Timestamps are never sent for "translation", so they can't be corrupted.
    - Batching keeps API calls cheap and preserves context between lines.
"""

import os
import re
import sys

try:
    from openai import OpenAI
except ImportError:
    sys.exit("Please run: pip install openai")

MODEL = os.getenv("TRANSLATE_MODEL", "gpt-4o-mini")
BATCH_SIZE = 20  # subtitle blocks per API call

SYSTEM_PROMPT = """You are a subtitle translator for Chinese cooking videos.
Translate the numbered text lines to natural English.
Rules:
- Output ONLY the translations, one per line, in the same order, numbered the same way.
- Never translate timestamps or numbers in brackets — translate only the given lines.
- Cooking terms: 生抽→light soy sauce, 老抽→dark soy sauce, 焯水→blanch,
  爆香→stir-fry until fragrant, 勾芡→thicken with starch.
- Keep it short and spoken-style."""


def parse_srt(path):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    blocks = re.split(r"\n\s*\n", content.strip())
    parsed = []
    for b in blocks:
        lines = b.strip().split("\n")
        if len(lines) >= 3:
            parsed.append({"idx": lines[0], "time": lines[1], "text": lines[2:]})
    return parsed


def translate_texts(client, texts):
    numbered = "\n".join(f"[{i+1}] {t}" for i, t in enumerate(texts))
    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": numbered},
        ],
        temperature=0.3,
    )
    out = resp.choices[0].message.content.strip().split("\n")
    cleaned = [re.sub(r"^\[\d+\]\s*", "", line).strip() for line in out]
    return cleaned


def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python srt-translator.py input_zh.srt output_en.srt")
    src, dst = sys.argv[1], sys.argv[2]

    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL"),  # optional, e.g. an AI gateway
    )
    blocks = parse_srt(src)

    for i in range(0, len(blocks), BATCH_SIZE):
        chunk = blocks[i : i + BATCH_SIZE]
        texts = [" ".join(b["text"]) for b in chunk]
        translated = translate_texts(client, texts)
        for b, t in zip(chunk, translated):
            b["text"] = [t] if t else b["text"]
        print(f"Translated {min(i + BATCH_SIZE, len(blocks))}/{len(blocks)} blocks...")

    with open(dst, "w", encoding="utf-8") as f:
        for b in blocks:
            f.write(f"{b['idx']}\n{b['time']}\n" + "\n".join(b["text"]) + "\n\n")
    print(f"Done → {dst}")


if __name__ == "__main__":
    main()
