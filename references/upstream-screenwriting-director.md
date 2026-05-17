# Upstream Screenwriting And Director System

Use this when the user has an idea, premise, unfinished script, or wants better story quality before production.

## Story Development Pipeline

1. Define format, audience, platform, duration, aspect ratio, and creative ambition.
2. Build the story engine: protagonist, want, need, flaw, pressure, stakes, theme, antagonist force.
3. Choose structural mode:
   - micro-short: hook -> escalation -> reversal -> sting
   - 3-5 minute short: cold image -> rule -> cost -> moral trap -> final echo
   - short-drama episode: cold open -> conflict squeeze -> reversal -> cliffhanger
   - 60-episode series: repeatable desire engine, episode reversals, long hooks
   - 90-minute movie: 15-beat feature structure and sequence outline
4. Run the anti-cliche pass:
   - name the obvious version
   - reject the obvious ending
   - add a cost rule
   - add a misdirection
   - add a moral trap
   - design a final image that reinterprets the opening
5. Convert beats into scene units with duration, visible action, conflict, emotional turn, and sound/image motif.
6. Write or revise the script in Markdown.

## Existing Script Diagnosis

Do not rewrite an existing script by reflex. First diagnose:

- Is the premise clear in the first 10-20 seconds?
- Does every scene change power, information, emotion, relationship, or physical situation?
- Is the protagonist active enough?
- Does the midpoint change the audience's understanding or stakes?
- Does the ending leave aftertaste, not just plot closure?
- Which scenes are AIGC-hard: crowd, exact text, complex action, long dialogue, continuity-heavy props?

Then propose:

- `Keep`: story elements that are working.
- `Sharpen`: small changes for surprise, pressure, visual clarity.
- `AIGC Adapt`: changes needed only for model producibility.
- `Do Not Change`: dialogue, twist, motif, or image the user has approved.

## AIGC-Aware Rewrite Rules

- Preserve strong human drama; simplify only production risk.
- Replace unfilmable psychology with visible behavior.
- Move exact subtitles, documents, phone text, countdowns, and title cards to post or text plates.
- Reduce large crowd specificity unless the crowd is the dramatic subject.
- Use motifs that can survive generation: objects, colors, repeated gestures, sound cues, framing.
- For surprise, prefer meaning reversal over random plot twist.

## Script Markdown Template

```markdown
# Title

## Format
- Type:
- Duration:
- Aspect ratio:
- Style:

## Logline

## Creative Assumptions

## Story Engine

## Surprise And Aftertaste Mechanism

## Characters

## Scene Structure

## Screenplay

## AIGC Adaptation Notes
```
