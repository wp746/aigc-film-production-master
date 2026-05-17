# Creative Development Orchestration

Use this to close the upstream gap: the master skill coordinates creative development, but should not rely on downstream prompt logic to invent story quality.

## Rule

Do not treat `image2-seedance-control` as the story brain. It is a downstream production engine.

For ideas, scripts, series, or movies, use the strongest available upstream method first:

- If `save-the-cat-screenwriting-skill` is available, use it for story structure, character arc, beat logic, anti-cliche pass, and aftertaste.
- If a dedicated genre skill is available, use it for genre conventions and audience expectation.
- If neither is available, apply the fallback framework below.

## Creative Brain Tasks

Before AIGC director work, lock:

- audience and platform promise
- protagonist engine: want / need / flaw / wound / false belief
- antagonist pressure: person / system / environment / moral trap
- stakes: external, emotional, social, irreversible cost
- story rule: what makes this concept more than a situation
- reversal pattern: how audience expectation is repeatedly updated
- aftertaste image: what remains after the plot ends
- production promise: what the viewer came to see in this format

## Anti-Cliche Pass

For every idea, generate and reject the obvious version:

| Layer | Question |
|---|---|
| Obvious Plot | What is the first version any model would write? |
| Obvious Moral | What easy lesson would make it dull? |
| Obvious Ending | What ending only closes plot but leaves no echo? |
| Cost Rule | What does the protagonist lose by using the premise power? |
| Moral Trap | What correct choice still hurts? |
| Misdirection | What does the viewer misunderstand at first? |
| Final Reframe | What final image changes the meaning of the opening? |

## Character Fate Arc

For shorts, use compact arc:

```text
mask -> pressure -> temptation -> cost -> irreversible choice -> image echo
```

For series, use progressive arc:

```text
want engine -> repeated wins -> hidden cost -> midpoint truth -> method collapse -> new self -> final trap
```

For features, use transformation arc:

```text
false belief -> refusal -> fun-house testing -> midpoint truth -> all-is-lost wound -> final proof
```

## Output Template

```markdown
# Creative Development Board

## Project Promise

## Story Engine

## Character Fate Arc

## Anti-Cliche Findings
| Obvious Version | Rejected Because | Stronger Choice |

## Surprise And Aftertaste

## AIGC Production Implications
```

## Handoff

Only after the creative board is coherent should the master skill move into `aigc-director-system.md`.
