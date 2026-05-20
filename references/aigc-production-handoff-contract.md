# AIGC Production Handoff Contract

Use this to connect upstream story/director work to downstream Image2 + Seedance production.

## Contract Rule

Every handoff must be specific enough that a downstream prompt factory can produce boards without reinterpreting the story.

## Required Sections

```markdown
# [Project] - AIGC Production Handoff

## Project Lock
- Format:
- Duration:
- Aspect ratio:
- Platform:
- Target model/platform:
- Style:
- Language:
- Delivery target:

## Approved Story Source
- Script file:
- Approved version:
- Do-not-change items:

## Source / Provenance Lock
| Source | Owner | Permission | Reuse Boundary | Notes |

## Global Look Lock
- Palette:
- Lens:
- Camera:
- Lighting:
- Texture:
- Forbidden drift:

## Asset Matrix
| Code | Type | Name | Must Preserve | May Clarify | Forbidden Drift |

## Scene Geography
| Code | Location | Fixed Anchors | Light | Entrances/Exits | Camera-Safe Zones |

## Prop / UI / Text Matrix
| Code | Item | Duty | Exact Text? | Generation Mode | Post Mode |

## Segment Plan
| Segment | Runtime | Beat | Function | References Needed | In State | Action | Out State | Next Handoff |

## Complexity Budget
| Segment | Characters | Actions | Camera | Text | VFX | Risk | Fix |

## Brand / Retention Lock
- Audience:
- Proposition / story promise:
- Hook:
- Brand memory / final image:
- CTA / next action:

## Downstream Instruction
Use `image2-seedance-control` as the prompt factory. It owns final Image2 asset prompts, Image2 storyboard prompts, Seedance prompts, lint, upload order, acceptance scoring, and repair SOP. The current master compatibility target is `image2-seedance-control-skill` v1.9.2; apply `image2-seedance-v192-downstream-contract.md` before final prompt delivery.
```

## Production Duty Vocabulary

- `CHAR_*`: recurring character identity board.
- `EXTRA_GROUP_*`: varied background people; never clone the hero face.
- `SCENE_*`: recurring environment and geography board.
- `PROP_*`: physical object board.
- `UI_TEXT_*`: exact phone/document/sign/title text plate.
- `STYLE_LOOK_SAFE`: optional abstract style image only; no people, geography, props, maps, or readable text.
- `SEG_*`: one Seedance generation unit, local 0:00-0:15.
- `POST_*`: subtitles, overlays, phone UI, title cards, exact typography, sound, music, VFX compositing.

## Handoff QA

Before downstream production:

- Every named character has a code.
- Every recurring scene has a code.
- Every hero prop has a code.
- Exact text is isolated or moved to post.
- Every segment has in/out state and one main job.
- Every high-risk segment is split, simplified, or assigned to post.
- Style reference does not override identity, wardrobe, geography, or story facts.
- Source/provenance and reuse boundaries are clear.
- Brand/ad/retention choices are locked when relevant.
- Target model/platform limits are known or defaulted.
