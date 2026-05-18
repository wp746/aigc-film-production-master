# Genre Playbook Index

Use this when the project depends on a recognizable genre promise. The playbook prevents every AIGC film from collapsing into the same generic cinematic style.

## Selection Rule

Pick one primary genre and at most two secondary flavors. The primary genre controls story promise and audience expectation. Secondary flavors only modify tone, pacing, or visual treatment.

For the five high-priority production genres below, load the dedicated deep playbook after selecting the primary genre:

| Primary Genre | Load |
|---|---|
| Suspense / Thriller / 悬疑惊悚 | `genre-playbooks/suspense-thriller.md` |
| Cultural Tourism / 文旅 | `genre-playbooks/cultural-tourism.md` |
| Commercial / TVC / 广告 | `genre-playbooks/commercial-tvc.md` |
| Short Drama / 短剧 | `genre-playbooks/short-drama.md` |
| Black Humor / 黑色幽默 | `genre-playbooks/black-humor.md` |

## Playbook Table

| Genre | Story Promise | Visual / Sound Strategy | AIGC Risk | Downstream Strategy |
|---|---|---|---|---|
| Suspense / 悬疑 | information gap, delayed reveal, suspicion | withheld frames, negative space, quiet sound cues | too much explanation | use close reactions, object clues, slow reveals |
| Horror / 恐怖 | dread, violation of safety, unseen threat | restricted light, off-screen sound, stillness | monster overdesign, random gore | show less, post sound, split reveal |
| Noir / 黑色电影 | moral rot, fatal choice, ambiguity | hard side light, rain, reflections, smoke, low-key contrast | shallow cosplay look | lock motivated light and moral trap |
| Comedy / 喜剧 | expectation break, timing, status flip | clean framing, reaction holds, rhythm cuts | overacting, joke text rendered | protect pauses and reaction shots |
| Sci-Fi / 科幻 | speculative rule changes life | controlled design language, UI in post, practical world texture | generic neon, unreadable UI | asset-first tech props, post UI overlays |
| Cyberpunk / 赛博 | identity, surveillance, body/city pressure | neon contrast, wet streets, screens as environment | neon soup, text garbage | UI/text plates, strict palette, scene anchors |
| Guofeng / 国风 | cultural texture, ritual, poetic image | textile/material detail, architecture, restrained motion | costume/era drift | wardrobe boards, prop boards, era gate |
| Period / 年代戏 | time-specific social texture | production design, props, hair, signage as texture | modern objects leak in | scene/prop bible, blurred background text |
| Documentary / 纪录片 | observed truth and restraint | handheld breath, natural light, ambient sound | too polished or fake news look | reduce stylization, clean claims gate |
| Children's Animation / 儿童动画 | clarity, warmth, safety, readable emotion | simple shapes, bright but controlled palette, clear gestures | overstimulation | simple action, consistent characters |
| Travel / 文旅 | place as protagonist | geography, food, craft, local sound, human scale | postcard montage | location boards, cultural details, rhythm map |
| Experimental / 实验短片 | form as meaning | controlled visual rule, repetition, abstraction | random chaos | define one formal rule and strict constraints |
| Musical / 音乐剧 | emotion expressed through rhythm/song | choreography, musical beats, body staging | lip-sync and crowd complexity | segment choreography, post music/voice |
| Romance / 爱情 | distance, longing, choice | eyeline, silence, touch restraint, soft motivated light | generic beauty shots | micro-performance and handoff states |
| Action / 动作 | readable force and consequence | clean geography, impact sound, fewer actions | physics melt, identity drift | previs board, split action beats |
| Black Humor / 黑色幽默 | comic surface, cruel truth | ordinary realism plus moral absurdity | tone confusion | keep performance dry, final image sting |

## Genre Output Template

```markdown
# Genre Playbook

## Primary Genre

## Audience Promise

## Required Story Moves

## Visual Language

## Sound Language

## AIGC Risks

## Downstream Production Strategy
```

## Hard Rule

Do not use genre as decoration. If the genre does not change story structure, camera rhythm, sound, production design, or audience expectation, it is not doing work.

## Deep Playbook Handoff

When a deep playbook is loaded, bake its decisions into downstream prompts as:

- story promise and hook
- visual language lock
- sound language lock
- shot rhythm and segment strategy
- asset/prop priorities
- AIGC risk controls
- post duties for text, sound, UI, claims, CTA, subtitles, or overlays
