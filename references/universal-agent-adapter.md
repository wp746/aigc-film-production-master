# Universal Agent Adapter

Use this when the user wants friends, clients, or another AI agent to reuse this system outside the original local Codex environment.

## Purpose

This repository is the skill root. Any capable agent can reuse it if it can read:

- `SKILL.md`
- the referenced files under `references/`
- optional helper scripts under `scripts/`

The agent does not need to expose the full workflow to the end user. It should behave like an AIGC film production master and deliver the smallest useful output, usually a final Image2 + Seedance bilingual prompt Markdown file.

## Three Reuse Modes

### Native Skill Mode

Use this when the target agent supports installing or importing skills from GitHub.

Give the agent or platform:

```text
https://github.com/wp746/aigc-film-production-master.git
```

The skill entry is:

```text
SKILL.md
```

The trigger name is:

```text
$aigc-film-production-master
```

### Repository Reading Mode

Use this when the target agent cannot install skills, but can browse or read GitHub files.

Give it this instruction:

```text
请把 https://github.com/wp746/aigc-film-production-master 当成一个可执行 skill 仓库。
先读取根目录 SKILL.md，再按 SKILL.md 的路由只读取必要 references。
你要按该 skill 的规则执行，不要只总结仓库内容。
默认中文交流，内部推理后台完成，最终优先交付可复制的 Image2 + Seedance 双语提示词 Markdown 文件。
```

### Copy-Paste Agent Prompt Mode

Use this when the target agent cannot access GitHub directly. Give the friend the copied `SKILL.md` plus only the necessary reference files for the task.

Minimum file set for most shortfilm, short-drama, ad, or cultural-tourism jobs:

```text
SKILL.md
references/intake-routing.md
references/source-ingestion-normalization.md
references/shortform-filmgrade-pipeline.md
references/creative-development-orchestration.md
references/upstream-screenwriting-director.md
references/aigc-director-system.md
references/aigc-production-handoff-contract.md
references/downstream-image2-seedance-bridge.md
references/image2-seedance-v192-downstream-contract.md
references/final-prompt-delivery-contract.md
references/model-platform-adapter.md
references/postproduction-delivery.md
references/qa-risk-gates.md
```

Add genre files only when relevant:

```text
references/genre-playbook-index.md
references/genre-playbooks/suspense-thriller.md
references/genre-playbooks/cultural-tourism.md
references/genre-playbooks/commercial-tvc.md
references/genre-playbooks/short-drama.md
references/genre-playbooks/black-humor.md
```

Add brand, compliance, or longform files only when the project requires them.

## Friend-Facing Invocation Card

The user can paste this into any agent:

```text
请调用 aigc-film-production-master。

如果你支持 skill/GitHub 仓库读取，请使用：
https://github.com/wp746/aigc-film-production-master

执行规则：
1. 先读取 SKILL.md。
2. 按任务类型读取必要 references，不要一次性展开全部文件。
3. 默认后台完成创意强化、AIGC导演、生产交接、合规/QA、模型适配。
4. 如果我没有特别要求，不要展示内部推演过程。
5. 最终交付可复制的 Image2 + Seedance 双语提示词 Markdown 文件。
6. 如果我只要求某一模块，就只展示该模块；我修改后再回装进主链路。

我的创意 / 剧本 / brief：
[在这里粘贴]
```

## Agent Execution Contract

When another agent uses this repository, it must follow these rules:

1. Do not merely summarize the skill. Execute it.
2. Do not skip source normalization, AIGC feasibility, handoff, downstream prompt formatting, or QA gates for full workflow requests.
3. Do not expose hidden chain-of-thought or internal reasoning. Show only requested modules or final deliverables.
4. Do not invent unavailable external dependencies. If `image2-seedance-control` is unavailable, emulate the compatibility contract in `downstream-image2-seedance-bridge.md`.
5. Store substantial outputs as Markdown files when filesystem access exists. Otherwise provide a clean Markdown artifact in chat.
6. For public sharing, remove private file paths, client secrets, unpublished personal images, and unauthorized brand/IP claims.

## Minimal Test

Ask the target agent:

```text
请调用 aigc-film-production-master，把这个创意做成 3 分钟 AIGC 创意短片，并最终输出 Image2 + Seedance 双语提示词：
一个雨夜，外卖员发现每一单配送地址都是自己人生里后悔过的一个地点。
```

Expected behavior:

- The agent asks only essential missing questions or makes explicit assumptions.
- It does not show the whole internal workflow by default.
- It returns or writes one Markdown prompt package.
- The package contains asset prompts, storyboard prompts, Seedance prompts, post duties, and review template.
