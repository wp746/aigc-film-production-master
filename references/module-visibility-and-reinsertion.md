# Module Visibility And Reinsertion

Use this to control what the user sees.

## Core Rule

The system's internal stages should happen backstage. The default final deliverable is the downstream bilingual prompt package.

Do not show the full chain of reasoning, creative debate, feasibility gates, QA tables, or handoff logic unless the user explicitly asks for a module.

## Default Hidden Modules

These modules run internally by default:

- intake routing
- creative development orchestration
- anti-cliche and aftertaste pass
- genre/style strategy
- AIGC director feasibility map
- production handoff contract
- compliance/risk screening
- post-production duty split
- QA gates
- prompt completeness checks

Their decisions must be baked into the final prompts, not explained as process notes.

## Default Visible Deliverable

For full workflow requests, show only:

- link to final Markdown prompt file
- material assumptions if they affect generation
- unresolved risks if they require user choice

The final Markdown file should contain the bilingual Image2 + Seedance prompt package, not a long essay about how the system thought.

## User-Requested Module Extraction

If the user asks to inspect a module, show that module only.

Triggers:

- "把导演模块拎出来"
- "我看看创意判断"
- "先看风格模块"
- "展示生产交接包"
- "只要合规模块"
- "把后期计划单独给我"
- "这个模块我想改"
- "先别进入下游"

## Module Output Formats

### Creative Module

```markdown
# Creative Module
## Project Promise
## Story Engine
## Anti-Cliche Choice
## Surprise / Aftertaste
## Notes For Reinsertion
```

### AIGC Director Module

```markdown
# AIGC Director Module
## Director Stance
## Feasibility Map
## Segment Strategy
## Asset / Storyboard / Seedance / Post Duties
## Notes For Reinsertion
```

### Genre / Style Module

```markdown
# Genre / Style Module
## Primary Genre
## Visual Language
## Sound Language
## AIGC Risks
## Downstream Prompt Locks
```

### Handoff Module

```markdown
# Production Handoff Module
## Asset Matrix
## Scene Matrix
## Prop / UI / Text Matrix
## Segment Plan
## Complexity Budget
```

### Compliance Module

```markdown
# Compliance / Rights Module
## Risk Summary
## Allowed
## Needs Confirmation
## Must Avoid
## Downstream Constraints
```

### Post Module

```markdown
# Postproduction Module
## Edit / EDL
## Sound / Voice / Music
## Subtitle / Text / UI
## VFX Overlay
## Color / Delivery
```

## Reinsertion Rule

When the user modifies a module:

1. Treat the user's edited module as the new source of truth for that layer.
2. Identify downstream artifacts affected by the change.
3. Regenerate only affected prompts when possible.
4. Preserve unchanged approved modules.
5. Mention briefly what was reinserted and where it affects the final prompt file.

## Do Not Leak Backstage Work

Avoid wording like:

- "I ran Gate 1, Gate 2, Gate 3..."
- "My hidden reasoning was..."
- "Here is the full internal chain..."

Prefer:

- "已按你的修改重新装回导演层，并更新了对应的故事板和 Seedance 段落。"
- "这个模块会影响角色资产板、SEG03 故事板和 SEG03/SEG04 的提示词。"
