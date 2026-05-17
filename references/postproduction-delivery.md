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

- edit assembly list / EDL
- segment order
- in/out state notes
- subtitle/SRT plan
- voiceover/dialogue/ADR cue sheet
- music cue sheet
- sound design cue sheet
- VFX overlay list
- UI/text replacement list
- color/LUT direction
- final export specs
- version review log

## Post Template

```markdown
# [Project] - Postproduction Plan

## Edit Decision List / EDL
| Order | Source Segment | Take | Source In | Source Out | Timeline In | Timeline Out | Transition | Reason |

## Segment Assembly
| Order | Segment | Use | Cut In | Cut Out | Hold/Trim | Notes |

## Sound Cue Sheet
| Timeline Time | Layer | Cue | Source | Purpose | Mix Note |

## Voice / ADR Cue Sheet
| Time | Character/Voice | Line | Delivery | Sync | Notes |

## Music Cue Sheet
| Time | Cue Name | Mood | Start/End | Rights/Source | Mix Note |

## Subtitle / Text Plan
| Time | Text | Mode | Safe Area | Owner |

## SRT Draft
```srt
1
00:00:00,000 --> 00:00:02,000
[subtitle text]
```

## VFX / UI Overlay Plan
| Time | Element | Source | Composite Rule | Tracking | Owner |

## Color / LUT Direction
| Scene | Look | Contrast | Saturation | Grain | Notes |

## Final Delivery Specs
| Version | Aspect | Resolution | FPS | Codec | Audio | Platform | Filename |
```

## Hard Rules

- Do not force Seedance to render final subtitles.
- Do not bury exact Chinese text in Image2 storyboards.
- Do not treat generated clip order as final edit rhythm; editing may need trims, holds, or sound bridges.
- If a generated segment is visually strong but story timing is weak, repair in edit before regenerating.
- AIGC clips are source footage, not the final film. Final meaning is often created by edit, sound, text, and color.
