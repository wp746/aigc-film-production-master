# Commercial / TVC Playbook

Use this for品牌广告、产品短片、TVC、宣传广告、公益广告、招商片、产品发布、社交媒体投流广告。

## Audience Promise

The viewer should remember one product/place/brand truth and one visual memory. Beauty without persuasion is not enough.

## Strategy Lock

| Field | Question |
|---|---|
| Audience | Who must care? |
| Single-minded proposition | What one thing should they believe? |
| Functional proof | What visible action proves it? |
| Emotional hook | What feeling makes it matter? |
| Brand memory | What image/sound/action recalls the brand? |
| CTA | What should the viewer do next? |
| Claim boundary | What must not be exaggerated? |

## Story Patterns

| Pattern | Use When | Structure |
|---|---|---|
| Problem-Solution | Pain is clear | pain image -> product action -> relief/proof |
| Ritual Upgrade | Lifestyle/premium | ordinary ritual -> sensory upgrade -> brand memory |
| Before-After | Visible transformation | before state -> product intervention -> after state |
| Symbolic Brand Film | Image/values | metaphor -> human moment -> brand mark in post |
| Demonstration | Function matters | product board -> hand logic -> macro proof |
| Place/Product Invitation | Tourism/venue | arrival -> sensory detail -> CTA |

## Camera And Product Handling

- Product must have clear scale, material, hand relationship, and hero angle.
- Macro shots need specific tactile detail: condensation, fabric grain, steam, reflection, button press.
- If logo/text must be exact, use post or text plate.
- Avoid random glossy beauty shots that do not prove the proposition.
- Keep product readable, not overburied in mood.

## Rhythm

- 15s: hook 0-2s, proposition 2-5s, proof 5-11s, brand/CTA 11-15s.
- 30s: problem/context, product action, sensory proof, emotional payoff, CTA.
- 60s: mini story, repeated product memory, final brand image.

## Sound

- Product sound can be the mnemonic: click, pour, fizz, fabric, engine, notification, footsteps.
- Voiceover should carry proposition, not explain every image.
- Music drop or silence can reveal the brand moment.

## AIGC Risks

| Risk | Fix |
|---|---|
| Product shape/logo drifts | Dedicated product/prop board |
| Unreadable brand text | Post typography or UI text plate |
| Claim exaggeration | Compliance gate and softened language |
| Generic luxury look | Brand-specific palette/material/action |
| Product not memorable | Define brand memory device |

## Downstream Prompt Strategy

- Product asset board is mandatory for hero products.
- Storyboard must define product reveal and hand interaction.
- Seedance prompt must keep product shape, material, and scale stable.
- CTA, price, discount, legal line, logo lockup, QR code handled in post.

## Prompt Locks

```text
广告质感：每个镜头服务一个传播主张；产品/品牌记忆必须可见；材质、手部交互、声音和最终CTA明确；不把精确Logo、价格、二维码、法律声明交给视频模型生成。
```

```text
Commercial look: every shot serves one proposition; visible product/brand memory, precise material and hand interaction, clear sound mnemonic and post-owned CTA; do not ask the video model to generate exact logos, prices, QR codes, or legal text.
```

## Avoid

- 高级但不知道卖什么。
- 只堆形容词：高级、质感、大片。
- 把品牌主张写成字幕让模型渲染。
- 产品只出现一瞬间，没有使用证明。
