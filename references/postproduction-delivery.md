# Postproduction Delivery

Use this after Seedance prompt production or after generated clips are reviewed.

## Why This Exists

AIGC production does not end at generated clips. Exact text, voice, subtitles, music, sound bridges, overlays, and final rhythm usually belong in post.

## Post Duties

| Duty | Handles |
|---|---|
| `EDIT` | assembly, pacing, cut points, transitions, reaction holds |
| `SOUND` | room tone, ambience, foley, breath, impact, silence |
| `VOICE` | voiceover, dialogue recording, ADR, narration timing |
| `MUSIC` | motif, cue, rise/drop, ending resonance |
| `SUBTITLE` | exact Chinese subtitles, typography, safe margins |
| `TEXT_UI` | phone screens, documents, countdowns, title cards |
| `VFX_POST` | overlays, compositing, screen replacement, particles, glow, time displays |
| `COLOR` | unified grade, contrast, grain, shot matching |
| `DELIVERY` | aspect ratio, platform specs, naming, versions |

## Deliverables

For production-ready projects, create:

- edit assembly list
- segment order
- in/out state notes
- subtitle/SRT plan
- voiceover/dialogue cue sheet
- music and sound cue sheet
- VFX overlay list
- final export specs
- version review log

## Post Template

```markdown
# [Project] - Postproduction Plan

## Edit Assembly
| Order | Segment | Use | Cut In | Cut Out | Transition | Notes |

## Sound Cue Sheet
| Time | Layer | Cue | Purpose |

## Subtitle / Text Plan
| Time | Text | Mode | Owner |

## VFX / UI Overlay Plan
| Time | Element | Source | Composite Rule |

## Color And Finish

## Delivery Versions
```

## Hard Rules

- Do not force Seedance to render final subtitles.
- Do not bury exact Chinese text in Image2 storyboards.
- Do not treat generated clip order as final edit rhythm; editing may need trims, holds, or sound bridges.
- If a generated segment is visually strong but story timing is weak, repair in edit before regenerating.
