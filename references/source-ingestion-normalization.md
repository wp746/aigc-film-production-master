# Source Ingestion And Normalization

Use this before creative development or downstream prompt production. The goal is to turn messy user input into one stable production source.

## Source Types

| Source | What To Extract | Risk |
|---|---|---|
| One-line idea | premise, emotion, hook, implied format | too vague |
| Existing script | exact dialogue, scenes, characters, props, rhythm | accidental rewrite |
| Brief / client doc | objective, audience, claims, deliverables, restrictions | missing brand truth |
| Reference image | visible invariants, style traits, asset identity | over-copying |
| Reference video | structure, pacing, camera, sound, edit grammar | copyright imitation |
| Existing asset | identity, wardrobe, scene geography, prop shape | redesign drift |
| Web link / platform brief | rules, specs, deadlines, allowed materials | stale or incomplete info |

## Normalized Source Packet

```markdown
# Source Packet

## User Goal

## Input Type

## Locked Source Material
- exact script/dialogue:
- user-provided assets:
- client/brand constraints:
- reference material:

## Missing But Needed

## Assumptions

## Do Not Change

## Needs User Confirmation
```

## Script Preservation

When the user gives a script:

- preserve exact dialogue unless the user asks for rewrite
- distinguish "creative improvement" from "AIGC production adaptation"
- mark exact lines that must survive into Seedance as spoken audio timing
- mark exact text that must move to post or text plates

## Reference Material Boundary

Extract craft, not protected expression:

- allowed: broad pacing, camera grammar, light direction, palette, sound mood, structural lessons
- avoid: exact shot-by-shot copy, recognizable private people, distinctive copyrighted designs, protected dialogue, logos, unlicensed music

## Handoff

The normalized source packet is the source of truth for all later modules. If the user changes it, affected modules must be regenerated through `versioning-feedback-loop.md`.
