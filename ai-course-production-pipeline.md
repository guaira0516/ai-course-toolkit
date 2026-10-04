# AI Course Production Pipeline

End-to-end pipeline of how I produce and sell Chinese cooking video courses overseas, with AI at every step.

```
 FILM (real footage)
   │
   ▼
 EDIT ──► CapCut auto captions (Chinese)
   │
   ▼
 SUBTITLES ──► Export SRT ──► AI translate (this repo: srt-translator.py)
   │                              keeps timestamps, EN glossary applied
   ▼
 VOICEOVER ──► EN script polish ──► TTS generation ──► timeline align
   │
   ▼
 PACKAGE ──► Gumroad listing (AI-written description + pricing)
   │
   ▼
 MARKET ──► TikTok / YouTube Shorts (AI scripts + titles)
```

## AI Touchpoints

| Stage | AI does | Tool type |
|---|---|---|
| Captions | speech-to-text (Chinese) | video editor |
| Translation | SRT text translation, timestamps preserved | LLM API |
| Voiceover | English narration | TTS |
| Copywriting | product page, promo scripts | LLM |
| Marketing | short-form scripts, titles | LLM |

## Design Principles

- **Real footage first**: AI video is only used for intro/atmosphere shots; the teaching itself is always real filming (trust = sales)
- **Timeline is sacred**: every automation step must preserve SRT timestamps — re-syncing is the most expensive mistake
- **One glossary everywhere**: cooking terms translated once, reused across subtitles, voiceover, and product pages
- **Digital product, zero inventory**: video course on Gumroad, no shipping, no stock pressure
