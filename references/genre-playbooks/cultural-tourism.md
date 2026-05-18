# Cultural Tourism Playbook

Use this for文旅宣传片、城市形象片、景区短片、非遗/地方文化视频、民宿酒店、地方美食、赛事/节庆宣传。

## Audience Promise

The place is the protagonist. The viewer should remember a texture, route, sound, human gesture, and reason to go, not just see pretty scenery.

## Story Moves

| Move | Function |
|---|---|
| Place hook | A first image only this place can own |
| Human anchor | One local person, visitor, craftsperson, child, guide, or traveler |
| Sensory proof | Food, sound, texture, weather, material, craft |
| Route logic | Arrival, discovery, participation, rest, night memory |
| Cultural detail | Specific local symbol used naturally, not as label |
| Invitation | Viewer imagines themselves there |
| Final memory | A repeatable image/sound/phrase that can become the campaign recall |

## Camera And Blocking

- Use geography: entrance, path, water/bridge/street/temple/market route.
- Combine wide establishing shots with tactile close-ups: hands, food steam, stone, fabric, tea, craft tools.
- Human scale prevents postcard emptiness.
- Movement should feel like walking, arriving, turning a corner, noticing.
- Avoid drone-only montage. Aerials can open or close, but not carry the whole film.

## Rhythm

- 30s: place hook -> sensory proof -> human moment -> invitation.
- 60-90s: arrival -> local detail -> activity -> emotional pause -> night/final memory.
- 3min: chaptered route. Each chapter needs one sensory anchor and one human action.

## Sound

- Local ambience is identity: water, market, footsteps, bells, wind, cooking, dialect fragments, festival drums.
- Music should support place, not drown it. Use sound bridges between locations.
- Voiceover must be sparse and image-led; avoid tourism-board slogans as narration.

## AIGC Risks

| Risk | Fix |
|---|---|
| Generic postcard montage | Lock specific geography and local details |
| Cultural symbols become costume cosplay | Use real craft/material/behavior anchors |
| Random signs/text artifacts | Blur background signs or handle exact text in post |
| Place continuity drifts | Scene boards for key locations |
| Crowds clone faces | Use varied extras guidance |

## Downstream Prompt Strategy

- Create `PLACE_*` or `SCENE_*` boards for recurring locations.
- Use prop boards for food, craft objects, local products, souvenirs.
- Create safe style look from weather/light/material, not from mixed crowd/location boards.
- Storyboards should show route and sensory beats.
- CTA, slogan, map labels, festival dates, QR codes go to post.

## Prompt Locks

```text
文旅质感：地点是主角，镜头跟随人的抵达与发现；真实地方材质、天气、声音、手作与食物细节；避免空洞航拍堆叠、假民俗、随机中文招牌和旅游宣传口号硬字幕。
```

```text
Cultural tourism look: the place is the protagonist; human-scale arrival and discovery, tactile local materials, weather, craft, food and ambient sound; avoid empty drone montage, fake folklore, random readable signs, and slogan subtitles inside generated frames.
```

## Avoid

- 全片只有风景，没有人。
- 只说“烟火气”“诗意”，没有具体材质和行为。
- 把所有地方拍成同一个古风滤镜。
- 让模型生成精确地图、招牌、活动日期。
