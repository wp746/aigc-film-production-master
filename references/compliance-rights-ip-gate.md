# Compliance, Rights, And IP Gate

Use this for brand work, celebrities, public figures, reference remakes, platform publishing, contests, music, voice, likeness, minors, medical/legal/financial topics, or any IP-adjacent production.

This is not legal advice. It is a production risk gate that decides whether to proceed, revise, cite source rights, or ask the user for permission/clearance.

## When Mandatory

Run this gate when the project includes:

- brand names, logos, products, trademarks, client briefs
- celebrity, politician, public figure, influencer, or private person's likeness
- film/game/anime/IP world references
- "make it like [specific movie/video/creator]"
- reference video remake or shot-by-shot imitation
- music, lyrics, soundalike voice, voice cloning, artist style
- minors, schools, hospitals, weapons, police, military, disasters
- platform ads, contest submission, commercial delivery
- regional policy or cultural sensitivity

## Risk Categories

| Category | Check |
|---|---|
| Brand / Trademark | Is the logo/product authorized? Are claims accurate? |
| Celebrity / Likeness | Is identity use authorized? Avoid implying endorsement. |
| Private Person | Consent needed for recognizable likeness/voice. |
| Copyrighted IP | Avoid copying protected characters, scenes, dialogue, designs, music, or exact shots. |
| Style Reference | Extract broad craft traits; do not clone a living artist/creator identity or exact work. |
| Music / Lyrics | Do not include unlicensed lyrics or copyrighted track replication. |
| Voice | Avoid unauthorized voice cloning or soundalike impersonation. |
| Platform / Contest | Check required format, disclosure, brand safety, watermark, music rules, deadlines. |
| Claims | Product, health, finance, legal claims need verification and disclaimers. |
| Safety / Content | Apply platform and model safety constraints before prompt production. |

## Output Template

```markdown
# Compliance And Rights Gate

## Risk Summary
| Risk | Level | Reason | Required Action |

## Allowed

## Needs User Confirmation

## Must Avoid Or Redesign

## Downstream Prompt Constraints

## Post / Delivery Notes
```

## Reference Remake Rule

For reference videos:

- Allowed: pacing, camera grammar, lighting logic, edit density, mood, color, broad structural lessons.
- Avoid: exact copyrighted shot sequence, distinctive character design, protected dialogue, logo-heavy recreation, identifiable private people, unlicensed music.
- Deliver as transformation: "inspired by the craft logic", not "copy this exact work".

## Integration

If `compliance-review-skill` is available, use it as the dedicated checker before final prompt delivery or public release.

Hard stop if:

- user requests unauthorized celebrity/private-person impersonation
- exact copyrighted lyrics or music recreation is required
- brand claims cannot be supported
- contest/platform rules are unknown and materially affect delivery
