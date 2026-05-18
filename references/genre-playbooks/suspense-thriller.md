# Suspense / Thriller Playbook

Use this for悬疑、惊悚、心理压力、反转短片、悬疑短剧、都市怪谈、隐秘真相类广告或文旅悬念片。

## Audience Promise

The audience comes for information pressure: they know something is wrong, but not exactly what. Suspense should make the viewer lean forward, not wait for exposition.

## Story Moves

| Move | Function |
|---|---|
| Ordinary surface | Make the first image believable and specific |
| Wrong detail | One object/gesture/sound that does not belong |
| Restricted knowledge | Decide what the audience knows vs protagonist knows |
| Pressure loop | Every beat increases risk or narrows choice |
| False explanation | Give one plausible but incomplete answer |
| Moral reveal | The final truth changes how we judge someone |
| Aftertaste image | Last image reinterprets the opening object/detail |

## Camera And Blocking

- Use partial information: door gaps, reflections, half-lit faces, foreground obstruction.
- Prefer slow push-in, locked-off frames, and motivated pans over random handheld chaos.
- Keep geography legible. Suspense fails if the viewer cannot understand where danger or truth is.
- Close-ups should reveal clues, not only faces.
- Reaction shots must have time to register suspicion, denial, calculation, or dread.

## Rhythm

- 0-2s: unsettling ordinary image.
- Early beat: establish the rule or missing fact.
- Middle: repeat one clue with changed meaning.
- Final: reveal without overexplaining.
- Use silence and holds. Do not cut every two seconds unless the pressure is panic, not mystery.

## Sound

- Room tone, small foley, distant mechanical sounds, breath, phone vibration, elevator ding, fluorescent buzz.
- Music should be restrained. A single tonal bed or pulse is often stronger than horror scoring.
- Use sound bridges to connect Seedance segments.

## AIGC Risks

| Risk | Fix |
|---|---|
| Overexplaining with text | Move clue text to post or prop plate |
| Random scary imagery | Keep one consistent wrong detail |
| Unclear geography | Use scene board and floor plan |
| Emotion jumps too fast | Add reaction holds and micro-expression timing |
| Style becomes generic dark blue | Lock motivated light source and palette |

## Downstream Prompt Strategy

- Asset-first for clue props: `PROP_KEY`, `PROP_PHONE`, `PROP_PHOTO`, `PROP_TIMER`.
- Storyboard must show clue placement, eyeline, camera route, and reveal timing.
- Seedance prompt should write micro-reaction, breath, hesitation, and sound cues.
- Exact messages, documents, countdowns, CCTV UI, or phone screens go to `UI_TEXT_*` or `POST_*`.

## Prompt Locks

```text
悬疑质感：普通现实空间中出现一个不合理细节；克制光线，真实环境声，镜头缓慢接近真相；不使用随机恐怖元素，不用夸张鬼脸，不用解释性字幕；每个镜头只揭示一点信息。
```

```text
Suspense look: believable ordinary space with one wrong detail; restrained motivated light, natural room tone, slow camera pressure, no random horror imagery, no explanatory subtitles, each shot reveals only one new piece of information.
```

## Avoid

- 开头就把真相说完。
- 用大段旁白解释悬疑。
- 每个镜头都黑漆漆。
- 为了“刺激”加入和故事无关的血、怪物、尖叫。
- 让 Seedance 渲染关键中文证据文本。
