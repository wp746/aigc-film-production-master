# AIGC Director System

Use this after story/script development and before Image2/Seedance prompts.

## Purpose

The AIGC director does not merely describe how a live-action crew would shoot. The director must translate story intent into model-producible visual and temporal control.

## Director Pass

For each scene or sequence, define:

- `Dramatic Job`: what the viewer must understand or feel.
- `POV`: whose knowledge/emotion leads.
- `AIGC Feasibility`: direct / asset-first / storyboard-first / post-first / split / avoid.
- `Visual Rule`: color, lens, light, composition, recurring object, or body behavior.
- `Performance Rule`: breath, silence, micro-expression, gesture, speech rhythm.
- `Segment Strategy`: one-take, 2-shot, 3-shot, montage, split action, post overlay.
- `In State`: character, prop, scene, emotion at segment start.
- `Out State`: exact state handed to the next segment.

## Feasibility Labels

| Label | Meaning | Action |
|---|---|---|
| `DIRECT_GENERATABLE` | One action, few characters, clear space | Can move downstream |
| `ASSET_REQUIRED` | Identity/prop/scene must be locked first | Build asset board |
| `BOARD_REQUIRED` | Camera/blocking/action must be drawn | Build storyboard board |
| `POST_REQUIRED` | Exact text/UI/VFX/audio better in post | Add post duty |
| `SPLIT_REQUIRED` | Too much for one 15s segment | Split into smaller segments |
| `AVOID` | Unstable or not worth generating directly | Redesign beat |

## AIGC Director Deliverable

```markdown
# [Project] - AIGC Director Package

## Director Stance

## Visual And Sound Lock

## AIGC Feasibility Map
| Scene/Beat | Dramatic Job | Feasibility | Production Choice |

## Segment Plan
| Segment | Duration | Beat | Function | Characters | Main Action | In State | Out State | Risk | Control |

## Asset Requirements
| Code | Type | Duty | State Changes | Notes |

## Post Duties
| Item | Why Post | Source | Timing |

## Downstream Handoff
```

## Director Guardrails

- A director idea is not finished until it becomes an asset, storyboard, Seedance, post, split, or avoid duty.
- Do not require Seedance to generate exact Chinese paragraphs, subtitles, phone UI, contracts, or precise countdown text.
- Do not put more than one major emotional turn into one segment.
- Slow scenes can be powerful; do not overcut emotional beats.
- The final image must pay off the opening image or motif whenever possible.
