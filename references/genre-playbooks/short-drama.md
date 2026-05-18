# Short Drama Playbook

Use this for竖屏短剧、AI真人短剧、漫剧单集、连续投流短剧、强冲突剧情广告。

## Audience Promise

The audience wants fast clarity, visible conflict, emotional payoff, and a reason to watch the next beat or episode.

## Episode Engine

| Element | Requirement |
|---|---|
| Cold open | conflict, shock, question, or humiliation within seconds |
| Desire | protagonist wants something visible |
| Pressure | antagonist/system blocks it now |
| Reversal | power/information changes before the end |
| Emotional hook | viewer chooses a side |
| Cliffhanger | next action becomes unavoidable |

## Scene Design

- Prefer 2-4 controllable locations per episode.
- Keep named characters per segment low. Two-person confrontation is more stable than crowded argument.
- Use props as power objects: phone, contract, ring, bag, medicine, key, document.
- Dialogue must be exact and performable; long speeches split across segments.
- The first frame must instantly show relationship pressure or consequence.

## Camera And Blocking

- 9:16: faces, hands, phones, documents, doors, tables become important vertical anchors.
- Use over-shoulder, close-up, insert shot, reaction hold.
- Avoid wide crowd scenes unless they are background texture.
- Make eyelines and power distance clear.
- Cliffhanger image should be simple enough to become a thumbnail.

## Rhythm

- 0-3s: hook.
- 3-15s: conflict rule.
- 15-45s: escalation and first reversal.
- 45-90s: emotional pressure or secret.
- final 3-8s: cliffhanger, reveal, threat, choice, or slap-back line.

## Sound

- Dialogue carries conflict, but silence after a line often sells the reversal.
- Use phone vibration, message ding, door slam, footsteps, document slap, breath.
- Subtitles are post, not generated in Seedance frames.

## AIGC Risks

| Risk | Fix |
|---|---|
| Too many characters | Split into smaller confrontation segments |
| Dialogue too long | Exact fragment continuation |
| Phone/document text corrupts | UI text plate or post |
| Face drift across episodes | Character boards and state table |
| Overacting | Micro-expression and reaction timing |

## Downstream Prompt Strategy

- Character boards for all recurring roles.
- Prop/UI boards for phones, contracts, medical reports, chat screens.
- Storyboards focus on confrontation blocking and reaction order.
- Seedance prompts include exact dialogue fragments as audio/performance, no subtitles.
- Use previous final frame only for opening state, not identity override.

## Prompt Locks

```text
短剧质感：开场即有关系压力；每段只承载一个冲突动作或信息反转；角色脸和服装连续，台词按声音表演处理，不生成字幕；结尾画面必须形成下一段钩子。
```

```text
Short-drama look: immediate relationship pressure, one conflict action or reveal per segment, locked faces and wardrobe, dialogue as spoken performance not rendered subtitles, final frame creates the next hook.
```

## Avoid

- 开头铺设世界观太久。
- 一段15秒塞三轮争吵。
- 让模型生成聊天记录全文。
- 每集都重新设计主角服装和脸。
