# QA And Risk Gates

Use this before calling a package industrial-grade and after every major handoff.

Run gates backstage by default. Do not expose gate tables to the user unless they ask for audit, review, diagnosis, or a specific module.

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
- The final prompt Markdown file exists when the user requested full production.
- Every segment has a corresponding Image2 storyboard prompt and Seedance prompt.
- The user can copy the final prompts without reading internal SOP notes.

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
- Character state table, scene state table, prop state table, shot ledger, take score library, and reusable asset library exist for longform production.
- Only one production block is sent downstream at a time.
- Generated takes are scored and logged.

## Gate 7: Compliance / Rights / IP

- Brand, celebrity, public figure, private likeness, music, voice, platform, contest, and reference-remake risks are checked.
- Any unauthorized exact IP, logo, lyrics, voice clone, or private likeness request is redesigned or held.
- Platform or contest requirements are known before delivery.

## Gate 8: Genre Coverage

- Primary genre is selected.
- Genre promise changes story structure, visual language, sound, and downstream strategy.
- Genre-specific AIGC risks are named and controlled.

## Gate 9: Shortform Film-Grade Closure

- The work is optimized for the requested shortfilm/short-drama/ad format, not inflated into feature-film planning.
- The final output preserves film-grade creative quality: surprise, texture, motivated camera/light, sound, and aftertaste or brand memory.
- The chain from idea to final prompts is traceable without broken assumptions.

## Verdicts

- `PASS`: ready for next stage.
- `FIX`: repair before next stage.
- `SPLIT`: divide into smaller production units.
- `POST`: move exact text/VFX/audio/editing to post.
- `REWRITE`: story or director logic is not producible.
