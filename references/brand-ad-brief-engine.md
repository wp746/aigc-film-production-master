# Brand / Ad / Promotional Brief Engine

Use this for promotional ads, TVC, brand films, product videos, cultural-tourism promotion, public-service videos, contest briefs, and commercial social videos.

## Rule

An ad is not just a beautiful short film. It must make the audience remember, desire, trust, act, or feel differently about the product/place/brand.

## Brief Lock

```markdown
# Brand / Ad Brief Lock

## Product / Place / Brand Truth

## Audience

## Single-Minded Proposition

## Emotional Hook

## Functional Proof

## Brand Memory Device

## Call To Action

## Must Include

## Must Avoid

## Claim / Compliance Risk
```

## Persuasion Patterns

| Pattern | Use When | AIGC Strategy |
|---|---|---|
| Problem-Solution | product solves pain | show pain briefly, product action clearly |
| Before-After | visible transformation | lock before/after state, avoid exaggerated claims |
| Ritual Upgrade | daily life becomes premium | tactile close-ups, sound, product hand logic |
| Place Invitation | tourism / city / venue | place as protagonist, local human texture |
| Symbolic Film | brand image / luxury / culture | strong visual motif, fewer claims |
| Social Proof | audience trusts use-case | avoid fake testimonials unless fictionalized |
| Demonstration | product function matters | prop/product board first, exact action split |

## Ad-Specific Handoff

For downstream prompts, always define:

- `PRODUCT_*` or `PLACE_*` asset
- hero visual mnemonic
- product/place must-never-drift list
- claim text owner: post, subtitle, voice, or UI plate
- CTA owner: post/title card unless visually embedded safely
- brand color and logo usage boundary

## Ad QA

- Can the viewer recall the product/place after one viewing?
- Is the brand memory visual, not just a line of copy?
- Are claims supported or softened?
- Is the CTA handled in post if exact typography matters?
- Does the video still work if watched muted?
- Does the first 2 seconds stop the scroll?
