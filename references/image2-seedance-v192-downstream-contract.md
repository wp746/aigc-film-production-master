# Image2 + Seedance 2.0 Downstream Contract v1.9.2

Use this when the master skill hands an approved AIGC production packet to the downstream Image2 + Seedance prompt factory, or when the downstream skill is unavailable and the master must emulate its current rules.

Source merged from `wp746/image2-seedance-control-skill` v1.9.2, latest reviewed commit `f20faa0`.

## Position

`image2-seedance-control-skill` is the downstream production engine. It owns Image2 asset boards, Image2 storyboard boards, Seedance 2.0 prompts, prompt lint, upload duties, acceptance scoring, and repair SOP.

The master skill must not ask downstream to invent the story brain. The master provides:

- locked story/script source
- AIGC director plan
- asset matrix
- segment plan
- text/post duties
- style and genre lock
- compliance and source boundaries

The downstream system converts those into operator-ready prompts.

## Mandatory Downstream Modules

If the downstream skill is available, invoke it and follow its `references/prompt-library-index.md`.

If the downstream skill is unavailable, emulate these mandatory modules:

```text
board-format-style-bible
bilingual-output-contract
text-rendering-boundary
visual-bible-reference-boundary
character-asset-layout-bible
scene-nine-view-layout-bible
prop-layout-bible
director-storyboard-layout-bible
dense-reference-stack-timeline
storyboard-seedance-pairing-principle
scene-type-playbook
segment-complexity-budget
dialogue-audio-subtitle-boundary
reference-upload-order
prompt-self-review-checklist
film-industry-master-checklist
```

For industrial, multi-segment, episode, asset-heavy, or client work, also emulate:

```text
project-continuity-bible
script-breakdown-segment-plan
shot-seam-review
production-runbook
department-signoff-gates
user-style-reference-sop
output-acceptance-scorecard
seedance-repair-sop
realism-clean-frame-rhythm-gate
```

## Updated Hard Rules

### Seedance Limit

Seedance 2.0 text prompts may use up to 5000 characters. Count before delivery when possible. Compress if over 5000.

Do not keep the old 2000-character limit.

### Board System Lock

Every Image2 board prompt must directly include a compact board-system lock:

- fixed aspect ratio
- matte warm-gray digital production board substrate
- fixed palette
- fixed sans-serif typography
- consistent margins, columns, arrows, labels, icons
- no kraft paper, newspaper, oil paper, parchment, scrapbook, random paper texture, mixed fonts, tiny text, long Chinese paragraphs, or corrupted text

Do not write `inherit PROJECT_BOARD_SYSTEM` in final prompts. Bake the board-system language into every Image2 prompt.

### Board Top Title Index

Every generated board image must start with a large visible title matching its prompt number:

- Asset boards: `A01 / ...`, `A02 / ...`
- Storyboard boards: `S01 / ...`, `S02 / ...`

Seedance upload notes must refer to those same `Prompt A01-EN`, `Prompt S01-EN` names so the user can find images in a crowded gallery.

### Bilingual Contract

Every Image2 board and Seedance prompt needs production-equivalent CN and EN versions:

- CN is for user review and Chinese production understanding.
- EN is for cleaner Image2 label rendering and downstream visual references.
- CN and EN must preserve the same asset codes, layout, modules, shot count, local timecodes, camera, action, dialogue intent, sound/VFX, continuity, and negative constraints.
- EN production boards must use English labels and asset codes only. Do not ask EN boards to render readable Chinese signs, documents, subtitles, or small Chinese labels.

### Text Boundary

Exact Chinese text, UI, documents, slogans, title cards, subtitles, maps, chat screens, and readable signs must be assigned to:

- `TEXT_PROP_PLATE`
- `UI_TEXT_PROP_BOARD`
- post-production typography

Seedance narrative footage must stay clean: no subtitles, captions, control-board labels, random Chinese/English text, watermarks, or corrupted text.

### Visual Bible Boundary

Do not upload a mixed global visual bible to Seedance if it contains people, faces, scene geography, vehicles, weapons, props, maps, signs, or readable text.

Split visual control into:

- `PROJECT_BOARD_SYSTEM`: prompt-only board layout rules, never uploaded.
- `STYLE_LOCK_TEXT`: compact written look lock repeated in every Image2 and Seedance prompt.
- `STYLE_LOOK_SAFE`: optional abstract style image only if it contains swatches, light, lens, grain, haze, rain, dust, smoke, material crops, and no story contamination.

### Asset / Storyboard Separation

Never merge full character design and storyboard into one recurring production board.

Asset boards control identity, wardrobe, scene geography, hero prop shape/material, and style-safe look.

Storyboard boards control shot order, blocking, camera, movement paths, light direction, emotion, sound/VFX cues, and handoff. Storyboards must not redesign faces, hair, age, wardrobe, gender, body type, or scene/prop identity.

### Storyboard Identity Firewall

Storyboard boards must be director sketch / previs line-art control boards, not photoreal production stills.

For named characters, storyboards should use:

- faceless silhouettes
- circles/squares/body blocks
- backs
- asset-code placeholders
- short labels such as `CHAR_A / MALE / GLASSES / SUITCASE`

They must not draw detailed faces, gendered facial features, hairstyles, braids, makeup, realistic portraits, or wardrobe detail that could override the character asset.

### 180-Degree Axis Lock

Dialogue, confrontation, pursuit, handoff, and exit scenes must include a screen-direction lock:

- action axis
- safe camera half
- forbidden camera half
- eyeline arrows
- entrance/exit direction
- neutral-axis bridge if crossing the line intentionally

Seedance prompts must repeat the same left/right relationship and forbid axis crossing, eyeline reversal, flipped geography, and reversed exit direction unless deliberately designed.

### Segment Complexity Budget

Every storyboard + Seedance pair needs one primary dramatic job.

Use a compact budget line in Seedance prompts:

```text
SEGMENT_BUDGET: 2 named chars / varied background extras / 1 main action / 2 shots / one slow push / no rendered text / low risk.
```

Split or simplify if a segment has:

- 4+ named characters
- large active crowd
- 3+ main actions
- many camera styles
- multiple locations
- long dialogue or overlapping lines
- multiple interacting VFX
- exact text rendering
- conflicting style references
- more than 8 shots in 15 seconds

### Dialogue / Voice Lock

When the user provides dialogue, treat it as a locked creative asset.

Preserve the original spoken line verbatim: wording, punctuation, dialect, pause marks, brackets, numbers, and parenthetical performance notes. Do not summarize, polish, shorten, merge, or delete.

Every speaking recurring character needs a `VOICE_LOCK` in Seedance prompts:

- age-range voice
- pitch
- timbre
- breath
- volume
- rhythm
- articulation
- accent/dialect level
- emotional variation
- forbidden wrong voices

Before each spoken line, write the speaker's VOICE_LOCK, current emotion, hidden intention, face/breath state, volume, tone, and the listener's reaction target. Dialogue is sound/performance timing, not subtitles. Subtitles are normally post.

### Reactive Performance

Every visible actor and extra must have reactive performance. Non-speaking people should blink, breathe, shift eye focus, change posture, hold tension, suppress reactions, or react to the current line/action according to the beat.

Forbid mannequin stillness, dead eyes, cloned background reactions, exaggerated nodding, constant smiling, theatrical overreaction, and everyone moving at the same time.

### Crowd / Extras Count Lock

If the story calls for a small group, lock the count:

```text
exactly 5-7 visible extras, no overview crowd, no parade formation, no assembly scene, no background mass, no duplicate rows, no extra uncounted figures.
```

Crowds/extras must vary age, face shape, height, body build, skin texture, hairline, posture, wardrobe wear, and micro-reactions while preserving era/unit continuity.

### Reference Upload Duties

Every Seedance prompt needs one upload note line before the fenced prompt. The note is not copied into Seedance.

Use platform-visible references:

```text
@图片1, @图片2, @图片3...
@Image1, @Image2, @Image3...
```

Bind each uploaded reference to:

- board identity
- asset code
- exact panel/module/label
- what to read
- what to ignore

Default reference stack:

```text
STYLE_LOCK_TEXT in prompt
-> character board(s) actually appearing
-> scene board for this exact scene
-> prop board(s) actually used
-> current storyboard
-> previous final frame only when continuing
```

### Storyboard + Seedance Pairing

The storyboard and Seedance prompt are a complementary dual-control pair:

- Storyboard visualizes movement paths, camera positions, light direction, emotional progression, sound/VFX markers, and handoff.
- Seedance prompt writes micro-expressions, camera texture, focus behavior, light quality, sound design, performance timing, start/end state, continuity, and negative constraints.

The pair must match shot order, local timecodes, character/scene/prop duties, dialogue intent, sound, and handoff.

### Camera And Lens

Every Seedance prompt must specify the project camera package and lens family, then focal length for every shot. Do not leave lensing at generic "cinematic".

Examples:

- ARRI Alexa 35 / Cooke Panchro/i Classic
- RED V-RAPTOR / Panavision Primo
- Sony Venice / Zeiss Supreme Prime

### Script Viability And Runtime

Before prompt writing, audit whether the requested duration can carry the script with breath, reaction, and emotional landing.

If duration is too short, do not squeeze dialogue unnaturally. Split the beat into more segments, recommend a longer runtime, or move exposition into post/voiceover. Protect the dramatic effect over the initial duration guess.

## Final File Requirements

Final prompt files should remain one operator-ready Markdown file, with no internal essays unless the user explicitly asks for SOP documentation.

Required sections:

```markdown
# [Project] - Image2 + Seedance Production Prompts

## Source Lock
## Language Strategy / 双语策略
## Asset Design Prompts
## Storyboard Prompts
## Seedance 2.0 Prompts
## Post Duties
## Generation Review Template
```

Optional only when user asks or project requires:

- Department Signoff
- Production Runbook
- Output Acceptance Scorecard
- Repair Log

## Lint

For local files, run:

```bash
python3 scripts/prompt_lint.py [prompt-file.md]
```

Hard failures include:

- no fenced Seedance prompt blocks
- Seedance prompt over 5000 characters
- missing local `0:00`
- timecodes ending after `0:15`
- missing clean-frame/no-subtitle/random-text guard
- historical/war/serious realism project without no-game/CG style guard
- crowd/group scene without varied-faces/no-cloned-faces guard
- style reference without style-lock text
- dialogue/voice without speech-rate/pause/no-subtitle guard
- more than 8 shots in one segment

Warnings should be judged by context. Do not mention them unless they materially affect production.
