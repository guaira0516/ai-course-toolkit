# AI Subtitle Translation Workflow

How I translate Chinese cooking video subtitles to English using AI, while keeping the timeline intact.

## Pipeline

1. **Film** the cooking tutorial (real footage, not AI-generated)
2. **Auto captions**: import footage into CapCut (剪映), use auto speech recognition to generate Chinese subtitles
3. **Export SRT**: export the Chinese subtitles as `.srt` (keeps timestamps)
4. **AI translate**: feed the SRT to an LLM with the prompt below — it translates only the text lines, never touches timestamps
5. **Proofread**: check cooking terms against my glossary (e.g. 生抽 → light soy sauce, 焯水 → blanch)
6. **Import back**: load the English SRT into the editor, render final video

## Translation Prompt Template

```
You are a professional Chinese-to-English subtitle translator for cooking videos.
Rules:
- Translate ONLY the subtitle text lines. NEVER modify timestamps, sequence numbers, or blank lines.
- Keep each translation on one line, roughly matching the original length so it fits the timing.
- Use natural cooking English: 生抽 → light soy sauce, 老抽 → dark soy sauce, 焯水 → blanch, 爆香 → stir-fry until fragrant.
- Keep it concise and spoken-style, suitable for video subtitles.

Input SRT:
[ paste SRT here ]
```

## Why This Works

- SRT is a plain-text format: LLMs handle it reliably without breaking structure
- Separating translation from timing avoids re-syncing work
- A fixed cooking-term glossary keeps terminology consistent across all videos in the course
