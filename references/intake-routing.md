# Intake Routing

Use this first. The goal is to decide what must be created before downstream Image2/Seedance work begins.

## Input Types

| Type | Signal | Next Action |
|---|---|---|
| `IDEA_ONLY` | One sentence, theme, character, object, or image seed | Clarify only production-critical choices, then develop story |
| `EXISTING_SCRIPT` | Finished or partial script, episode, scene, dialogue | Diagnose and convert to AIGC director plan |
| `BRAND_OR_AD_BRIEF` | Product, brand, city, venue, campaign, public-service brief | Normalize brief, run brand/ad engine, then produce prompts |
| `SERIES_OR_FEATURE` | 12/24/60 episodes, long movie, IP bible | Build longform control before scene production |
| `ASSET_READY` | Character/scene/prop images exist | Preserve assets as source truth, then plan boards |
| `REFERENCE_REMAKE` | User provides reference video/image/style | Extract style/structure without copying protected identity or exact copyrighted expression |
| `DOWNSTREAM_ONLY` | User asks only for Image2/Seedance prompts | Verify handoff is sufficient; if not, make minimal missing handoff |

## Compact Intake

Ask only what blocks production. If the user says "你定" or the creative direction is obvious, choose defaults and state assumptions.

- `作品形态`: 创意短片 / 竖屏短剧 / 广告 / MV / 文旅 / 漫剧 / 60集短剧 / 90分钟电影
- `时长`: 15秒 / 1分钟 / 3-5分钟 / 8-12分钟 / 单集 / 长片
- `画幅`: 16:9 / 9:16 / 2.39:1 / 4:3
- `风格`: 写实电影 / 黑色幽默 / 悬疑惊悚 / 治愈 / 国风 / 科幻 / 动画 / 用户参考风格
- `素材`: 无 / 有角色图 / 有场景图 / 有道具图 / 有参考片 / 有完整剧本
- `来源与权限`: 私人素材 / 客户素材 / 网络参考 / 自有资产 / 未确认
- `交付`: 只要故事 / 剧本MD / AIGC导演方案 / Image2+Seedance提示词 / 全链路SOP

## Default Assumptions

When unspecified:

- Short film: 3-5 minutes, 16:9, cinematic realism, 6-18 Seedance segments.
- Short-drama episode: 3 minutes, 9:16, fast hook, dialogue conflict, cliffhanger.
- Commercial: 15-30 seconds, product-first, minimal characters, strong visual mnemonic.
- Promotional/cultural-tourism: 30-90 seconds, place/product as protagonist, local texture, brand memory, post-owned text/CTA.
- Feature or series: build bible first; do not start final prompts from a single scene.

## Stop Conditions

Hold production if:

- The intended output is longform but there is no story engine or continuity bible.
- The user wants exact readable Chinese text in generated footage instead of post/text plates.
- The scene requires too many named characters, simultaneous actions, or long dialogue in one 15-second segment.
- Reference images conflict on identity, wardrobe, geography, or style.
- Private/client/source rights are unclear and the output is public/commercial.
