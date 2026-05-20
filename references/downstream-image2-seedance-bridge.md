# Downstream Image2 + Seedance Bridge

Use this when a handoff packet is ready and the next step is actual prompt production. For full workflow requests, combine this with `final-prompt-delivery-contract.md` and create the final prompt Markdown file.

## Preferred Path

If the `image2-seedance-control` skill is available, invoke it and pass the approved AIGC production handoff. Do not rewrite its mature downstream SOP.

Use `image2-seedance-v192-downstream-contract.md` as the current compatibility contract for this master skill. It reflects `wp746/image2-seedance-control-skill` v1.9.2.

If the user asked for final prompts, do not stop after saying this. Invoke the downstream skill or emulate its required output contract and produce the prompt file.

The downstream system owns:

- Image2 asset board prompts.
- Image2 storyboard/control-board prompts.
- Seedance 2.0 text prompts.
- CN/EN board pairs.
- Reference upload order.
- 5000-character Seedance prompt limit.
- Prompt lint.
- Output acceptance scoring.
- Repair SOP.

## Compatibility Rules For Any Agent

If `image2-seedance-control` is unavailable, follow these minimum rules:

1. Split outputs into asset prompts, storyboard prompts, and Seedance prompts.
2. Never merge full character design and storyboard into one recurring production board.
3. Use asset codes consistently across all prompts.
4. Keep Image2 board text large and short; avoid long Chinese text.
5. Use English production labels for cleaner downstream image labels when needed.
6. Seedance segment prompts use local 0:00-0:15 timecode only.
7. Each Seedance prompt must name reference duties compactly:

```text
@参考: CHAR_A=身份/服装 SCENE_01=空间/光 PROP_PHONE=形状/持握 当前故事板=镜头/动线 上段末帧=首帧状态
```

8. Narrative frames must be clean: no subtitles, labels, random text, watermarks, or corrupted UI unless explicitly requested.
9. If exact text matters, use `UI_TEXT_*` or `POST_*`.
10. After generation, score the take before repair or acceptance.
11. Use the v1.9.2 downstream contract for board-system lock, storyboard identity firewall, dialogue/voice lock, reactive performance, crowd count lock, 180-degree axis lock, segment complexity budget, and visual-bible reference boundary.

## Downstream File Contract

Final downstream prompt file should be one operator-ready Markdown file:

```markdown
# Image2 Seedance Control Prompts

## Asset Design Prompts

## Storyboard Prompts

## Seedance 2.0 Prompts
```

Do not include internal essays unless the user explicitly asks for SOP documentation.

## Current Downstream Version

- Downstream source: `wp746/image2-seedance-control-skill`
- Reviewed version: v1.9.2
- Reviewed commit: `f20faa0`
- Local compatibility file: `image2-seedance-v192-downstream-contract.md`

## End-To-End Execution Rule

The master pipeline is only complete when the user can copy prompts into Image2 and Seedance 2.0. A production handoff is an intermediate artifact, not the final artifact, unless the user explicitly asks to stop there.

## Repair Loop

When a generated take fails:

- Diagnose root cause: script beat / overload / asset unreadable / storyboard impossible / prompt ambiguous / reference conflict / model limitation / edit issue / sound issue.
- Repair the smallest unit.
- Change one primary variable per patch when possible.
- Keep bad takes for diagnosis.
