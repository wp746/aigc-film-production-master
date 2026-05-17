# Model And Platform Adapter

Use this before final prompt writing. The system is optimized for Image2 + Seedance 2.0, but production must adapt to the actual target model/platform when specified.

## Rule

Do not assume every model supports the same reference behavior, text limit, duration, motion quality, or safety boundary.

## Default Target

If unspecified:

- Image generation/control boards: GPT Image 2 / Image2 style control boards
- Video generation: Seedance 2.0
- Segment length: 4-15 seconds
- Output: CN review + EN production prompt pairs

## Adapter Checklist

| Dimension | Ask / Infer |
|---|---|
| Video model | Seedance / Kling / Sora / Veo / other |
| Image model | Image2 / Nano Banana / Midjourney / other |
| Max duration | per generation |
| Prompt limit | characters/tokens |
| Reference mode | image upload, first/last frame, multi-reference, style ref |
| Text rendering | reliable / unreliable / post only |
| Aspect ratios | 16:9, 9:16, 1:1, 2.39 |
| Audio support | silent, generated, external post |
| Safety limits | platform/model limits |
| Delivery target | social, client review, contest, ad platform |

## Adaptation Actions

- If duration is shorter than Seedance default, split segments more aggressively.
- If reference support is weaker, simplify asset count and increase prompt clarity.
- If text rendering is weak, move all exact text to post or text plates.
- If model handles motion poorly, reduce action complexity and use more edit cuts.
- If platform compresses vertical video, protect safe margins and close framing.
- If model supports audio poorly, write audio as post cue sheet rather than video prompt expectation.

## Output

The final prompt file should state the target model/platform in `Source Lock` and adapt the prompt structure accordingly.
