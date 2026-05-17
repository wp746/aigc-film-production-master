# Final Prompt Delivery Contract

Use this whenever the user wants the system to carry the work through to usable Image2/Seedance output.

## Rule

The final production deliverable is a Markdown file with copy-ready prompts. It must not be only a strategy, handoff, critique, or explanation. Internal modules should not be exposed in the final file unless the user explicitly asks for them.

## Required Final File

Default filename:

```text
outputs/[project-slug]-image2-seedance-prompts-v001.md
```

Required structure:

```markdown
# [Project] - Image2 + Seedance Production Prompts

## Source Lock
- normalized source packet version
- target model/platform
- asset/provenance code policy
- do-not-change items

## Asset Design Prompts
### A01-CN - Character / Scene / Prop
```text
...
```
### A01-EN - Character / Scene / Prop
```text
...
```

## Storyboard Prompts
### S01-CN - Scene / Segment Storyboard
```text
...
```
### S01-EN - Scene / Segment Storyboard
```text
...
```

## Seedance 2.0 Prompts
### SEG01-CN
```text
...
```
### SEG01-EN
```text
...
```

## Post Duties

## Generation Review Template
```

Do not include visible sections such as `Creative Reasoning`, `Internal Feasibility Gate`, `QA Chain`, `Compliance Reasoning`, or `Why I Chose This`. Their results must be baked into the prompts.

## Prompt Completeness

Every final prompt package must include:

- enough asset prompts to lock all recurring characters, scenes, hero props, product, UI/text plates, and style-safe look needs
- storyboard prompts for every Seedance segment
- one matching Seedance prompt per storyboard
- CN review version and EN production version when Image2 labels are involved
- local 0:00-0:15 timecode for every Seedance segment
- reference duties in every Seedance prompt
- clean-frame text ban
- in/out state for segment continuity
- post duties for exact text, subtitles, UI, title cards, sound, music, VFX, color, and delivery
- target model/platform assumptions
- no private source paths or client secrets in shareable prompt files

## No-Handoff-Only Rule

If the user asks for final production prompts, do not end with "下一步交给 image2-seedance-control". Actually use or emulate that downstream SOP and create the final prompt file.

## Final Response

After creating the file, respond with the file link and only mention material assumptions or risks. Do not paste the entire prompt package in chat unless asked.

If the user requested a standalone module, show that module separately, not inside the final prompt package unless they ask to archive it there.
