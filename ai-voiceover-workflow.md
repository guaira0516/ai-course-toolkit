# AI Voiceover Workflow

How I add English AI voiceover to Chinese cooking tutorials for overseas platforms.

## Pipeline

1. **Finalize the English script**: use the translated SRT text, merge short lines into natural spoken sentences
2. **Pick a voice**: choose a clear, friendly English TTS voice (consistent across the whole course)
3. **Generate**: run the script through a TTS tool, one paragraph per audio clip
4. **Align**: place each clip on the editing timeline to match the corresponding video segment
5. **Mix**: lower background kitchen sounds, keep voice prominent, export

## Script Prep Prompt

```
Rewrite the following subtitle lines into a natural English voiceover script.
- Merge fragmented lines into flowing sentences.
- Keep the cooking instructions accurate and in order.
- Tone: friendly teacher, speaking to a beginner.
- Mark pause points with [pause] where the video shows a key technique.

Subtitle lines:
[ paste lines here ]
```

## Tips

- One consistent voice = one consistent teacher identity for the whole course
- Short clips are easier to re-align than one long file
- Always listen once at 1x speed before final export — AI voices sometimes misread numbers and units
