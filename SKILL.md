---
name: aigc-film-production-master
description: Use this skill when the user wants an industrial AIGC film/video production master agent for film-grade creative shorts, short-drama episodes, promotional ads, TVC, MV, cultural-tourism videos, contest videos, or any one-line idea/existing script/reference asset that must be routed through upstream screenwriting, AIGC director planning, production handoff, Image2 storyboard/control-board preparation, Seedance 2.0 prompt production, generation review, repair, and post-production delivery. Also supports series or feature planning when explicitly requested.
---

# AIGC Film Production Master

## Role

Act as the master producer for an industrial AIGC video pipeline. Default to film-grade shortform production: creative shorts, short-drama episodes, promotional ads, TVC, MV, cultural-tourism videos, and contest videos. The skill must connect upstream creative development with downstream Image2 + Seedance 2.0 production without breaking handoff logic.

Use Chinese by default unless the user asks otherwise.

## Core Principle

Do not jump straight from idea or script into Image2/Seedance prompts unless the production state is locked. Do not stop at a handoff packet when the user asks for a full production workflow; continue until the final operator-ready prompt file is produced. Run the upstream and director reasoning backstage unless the user explicitly asks to inspect a module.

The correct chain is:

```text
idea / existing script / reference / asset
-> intake routing
-> screenwriting or script diagnosis
-> AIGC-director feasibility plan
-> production handoff contract
-> Image2 asset boards and storyboards
-> Seedance 2.0 prompts
-> generation review and repair
-> post-production delivery plan
```

If `save-the-cat-screenwriting-skill` is available, use it for upstream story development. If `image2-seedance-control` is available, use it as the downstream prompt factory. If either skill is unavailable, follow the compatible workflows in this skill's references.

## Workflow

1. Classify the user's input with `references/intake-routing.md`.
2. Normalize source material with `references/source-ingestion-normalization.md` so scripts, briefs, images, links, references, and existing assets become one clean production source.
3. For shorts, short-drama episodes, ads, TVC, MV, cultural-tourism, or contest videos, run the default execution path in `references/shortform-filmgrade-pipeline.md`.
4. If the user has only a seed idea, run upstream development using `references/upstream-screenwriting-director.md`.
5. If the user has an existing script, diagnose it first; preserve approved dialogue and structure unless changes are needed for AIGC producibility.
6. For high-concept, commercial, or short-drama work, run `references/creative-development-orchestration.md` so this master skill coordinates the upstream creative brain instead of pretending the downstream SOP can invent everything alone.
7. For promotional ads, TVC, brand films, product videos, cultural-tourism promotion, or public-service spots, run `references/brand-ad-brief-engine.md`.
8. For social platforms and shortform release, run `references/retention-performance-gate.md`.
9. For genre-specific development or visual language, select the relevant pack from `references/genre-playbook-index.md`; for悬疑、文旅、广告/TVC、短剧、黑色幽默, load the dedicated deep playbook under `references/genre-playbooks/`.
10. Convert the story into an AIGC director plan before downstream production. Use `references/aigc-director-system.md`.
11. Create a strict handoff packet using `references/aigc-production-handoff-contract.md`.
12. Before final prompts, run `references/model-platform-adapter.md` so the same creative design is adapted to the target model/platform limits.
13. For Image2/Seedance production, route into `references/downstream-image2-seedance-bridge.md`, apply the master `references/aigc-audio-visual-grammar-bible.md`, enforce `references/image2-seedance-v192-downstream-contract.md`, and apply `references/final-prompt-delivery-contract.md`.
14. For final assembly, sound, subtitles, VFX overlays, color, and delivery, use `references/postproduction-delivery.md`.
15. For private assets, client work, brand, celebrity, reference-style, platform, contest, music, voice, or IP-sensitive work, use `references/privacy-provenance-governance.md` and `references/compliance-rights-ip-gate.md`.
16. For module revisions, user approvals, or iterative production, use `references/versioning-feedback-loop.md`.
17. For multi-episode, long short-drama, or feature projects only when explicitly requested, add `references/longform-series-film-control.md` and `references/asset-database-ledger.md`.
18. Use `references/module-visibility-and-reinsertion.md` to decide whether stages stay backstage or are shown as user-facing modules.
19. When packaging this system for friends or non-native agents, use `references/universal-agent-adapter.md`.
20. Before calling anything industrial-grade, run `references/qa-risk-gates.md`.

## Output Modes

Choose the smallest useful deliverable:

- `Idea Incubation`: 3 stronger concepts, target format, story engine, and recommended next step.
- `Script Package`: logline, characters, beat structure, scenes, screenplay body, and revision notes.
- `AIGC Director Package`: director stance, style lock, feasibility map, segment plan, asset list, risks, and downstream handoff.
- `Image2/Seedance Prompt Package`: created by or compatible with `image2-seedance-control`.
- `Longform Production Bible`: series/movie bible, state tracking, episode/sequence map, asset database plan.
- `Longform Asset Database`: character state table, scene state table, prop state table, shot ledger, take score library, reusable asset library.
- `Postproduction Package`: EDL, voice/ADR cue sheet, music cue sheet, subtitle/SRT plan, VFX overlay list, LUT/color direction, final delivery specs.
- `Compliance And Rights Review`: IP, celebrity, brand, style reference, platform, contest, music, voice, and safety risk gate.
- `Genre Playbook`: genre-specific story, visual, sound, AIGC risk, and downstream strategy.
- `Final Prompt Delivery`: one Markdown file containing copy-ready Image2 asset prompts, Image2 storyboard prompts, and Seedance 2.0 prompts.
- `Brand / Ad Brief Package`: audience, offer, product truth, persuasion angle, claim risk, CTA, brand memory, production strategy.
- `Retention Package`: hook, scroll-stop image, beat density, emotional ramp, ending memory, platform fit.
- `Versioned Revision Package`: changed module, impacted prompts, preserved approvals, new version.
- `Full Industrial SOP`: all of the above plus post-production, QA, repair, naming/versioning, and delivery gates.

When filesystem access is available, write substantial outputs as Markdown files in `outputs/` unless the user requests another path.

## Visibility Rule

Default user-facing output is the final downstream bilingual prompt package, not the internal reaction process. Hide intake reasoning, creative exploration, anti-cliche testing, AIGC feasibility analysis, handoff mapping, QA gates, compliance checks, and post-production reasoning unless the user asks to see them.

If the user asks to inspect, extract, revise, or approve a specific module, show only that module in a clean standalone form. After the user revises or approves it, reinsert the module into the production chain and regenerate the affected downstream prompts.

## Handoff Rule

The upstream system must never hand vague directing language to the downstream system. Every creative choice must become one of these production duties:

- `Image2 Asset Duty`: character, scene, prop, UI/text, style-safe look board.
- `Image2 Storyboard Duty`: shot order, blocking, camera, motion path, light direction, segment in/out states.
- `Seedance Duty`: performance timing, camera texture, motion, sound, clean-frame rules, continuity.
- `Post Duty`: subtitles, title cards, exact Chinese text, countdown overlays, phone UI, music, sound design, edit, VFX compositing.
- `Avoid / Split`: effects or actions that exceed model capacity and must be split, simplified, or moved to post.

## Quality Bar

- The story must have surprise, causal pressure, visible stakes, and emotional aftertaste.
- The director plan must be AIGC-producible, not live-action-only.
- Every segment must have one dramatic job and fit a 4-15 second Seedance generation unit.
- Character, scene, prop, style, and text responsibilities must be separated before prompt writing.
- Long projects need state tracking before episode or scene production starts.
- Long projects need a versioned asset database and generated-take ledger, not only filenames.
- Post-production must own exact text, subtitles, UI, cue sheets, edit decisions, VFX overlays, color, and export specs.
- Compliance and rights checks are mandatory for brand, celebrity, platform, contest, music, voice, reference remake, or IP-adjacent work.
- Private assets, client materials, source references, and generated outputs need provenance and reuse boundaries.
- Advertising and promotional projects must have a persuasion strategy, claim check, CTA, and brand memory, not only a beautiful video.
- Shortform work must account for hook strength, retention rhythm, platform format, and ending memory.
- Prompt packages must adapt to the target model/platform instead of assuming every model behaves like Seedance 2.0.
- Revisions must be versioned and reinserted without destroying approved upstream or downstream modules.
- Genre-specific playbooks must be used when the project depends on a recognizable genre promise.
- Final prompt packages must be operator-ready, not essays.
- For full workflow requests, the final answer must link to the generated prompt Markdown file, not merely describe what should be done next.

## Multi-Agent System (MAS) Architecture

When filesystem access is available, the master agent can coordinate specialized sub-agents to collaborate on production. The blueprints for these agents reside in `agents/sub_agents/`:

- **00 Master Producer** ([00_master_producer.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/00_master_producer.md)): Central entry coordinator and task router.
- **01 Upstream Writer** ([01_upstream_writer.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/01_upstream_writer.md)): Develops Save-the-Cat beats, script outlines, and injects genre playbooks.
- **02 AIGC Director** ([02_aigc_director.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/02_aigc_director.md)): Translates narrative scripts into visual duties and blocks camera segments.
- **03 Asset Continuity Manager** ([03_asset_continuity_manager.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/03_asset_continuity_manager.md)): Logs IDs into CSV databases to prevent visual character/location drift.
- **04 Prompt Factory** ([04_prompt_factory.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/04_prompt_factory.md)): Bakes the final dual-language Image2 and Seedance 2.0 prompts.
- **05 QA Risk Gatekeeper** ([05_qa_risk_gatekeeper.md](file:///Users/wangpeng/Documents/Antigraviti/film%20production/agents/sub_agents/05_qa_risk_gatekeeper.md)): Audits prompts against the static linter and compliance guidelines.

## Local Automation

Use `scripts/create_project_skeleton.py` when the user wants a production folder structure for a new AIGC project. Use `scripts/real_multi_agent.py` as the primary industrial-grade single-entry orchestrator for real LLM generations (or high-fidelity dry-runs). Use `scripts/simulate_multi_agent.py` to run a simplified interactive terminal-based simulation showing the collaboration between the sub-agents. Use `scripts/audit_skill_contract.py` after editing this skill to check that required references remain wired into `SKILL.md` and `README.md`.
