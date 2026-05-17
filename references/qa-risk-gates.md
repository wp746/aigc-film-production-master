# QA And Risk Gates

Use this before calling a package industrial-grade and after every major handoff.

## Gate 1: Story

- Premise is understandable quickly.
- Protagonist has visible desire and pressure.
- Scenes are causal, not decorative.
- Ending pays off opening or central motif.
- Surprise is earned, not random.
- Emotional aftertaste remains after plot explanation.

## Gate 2: AIGC Feasibility

- Every scene/segment has a feasibility label.
- High-risk effects are split, simplified, or moved to post.
- No segment carries too many named characters, actions, text duties, or emotional turns.
- Exact text has post/text-plate plan.
- Dialogue has timing and listener reaction.

## Gate 3: Handoff

- Every character, scene, prop, style, VFX, UI/text element has a code or owner.
- Every segment has in state, main action, out state, next handoff.
- The downstream system can produce prompts without guessing story meaning.
- Director choices are translated into production duties.

## Gate 4: Prompt Production

- Asset prompts and storyboard prompts are separate.
- Storyboard and Seedance prompt match shot order and timecodes.
- Seedance prompt is within model limit.
- References have one clear duty each.
- Narrative frames forbid random text, subtitles, watermarks, labels, and corrupted UI.

## Gate 5: Generation Review

Hard fail if:

- wrong identity
- wrong recurring scene
- wrong hero prop
- unreadable or corrupted text appears in clean frame
- style becomes a different medium
- emotion or action no longer tells the beat
- segment cannot connect to previous/next segment

## Gate 6: Longform

- Character states are tracked after every episode/sequence.
- Plant/payoff ledger exists.
- Asset database is versioned.
- Only one production block is sent downstream at a time.
- Generated takes are scored and logged.

## Verdicts

- `PASS`: ready for next stage.
- `FIX`: repair before next stage.
- `SPLIT`: divide into smaller production units.
- `POST`: move exact text/VFX/audio/editing to post.
- `REWRITE`: story or director logic is not producible.
