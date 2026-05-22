# AIGC Audio-Visual Grammar & Layout Holy Bible (AIGC影视视听语言与排版设计圣经)

本圣经为 AIGC（如 Image2 生图 与 Seedance 2.0 视频生成）工业级影视生产的最高技术规范与操作契约。所有协同智能体与操作员必须无条件、严丝合缝地执行本规范，以彻底杜绝面部/道具/空间漂移，确保电影级叙事呼吸感，最大化榨干模型性能。

---

## 1. 物理画布与中英文双轨输出规范 (Substrate & Dual-Track Standard)

AIGC 图像模型默认会产生随机的画布背景（如牛皮纸、报纸、油纸纹理等），并且模型在渲染中文小字时极其容易崩坏字形。为实现零缺陷工业化交接，特制定此画布与字形物理标准：

### 1.1 画板基底绝对锁定 (Storyboard Substrate Solid Lock)
* **硬性标准**：所有资产图（角色、场景、道具）及技术故事板的背景一律硬编码锁定为 **“黑曜石深灰色磨砂质感背景配极细网格线”**（Matte Obsidian Slate Gray with minimalist fine grid lines）。
* **技术价值**：彻底消除牛皮纸、羊皮纸等随机纸张噪声，保证所有分镜和资产图的色彩饱和度与背景灰阶绝对一致，便于视频模型（Seedance 2.0）读取。

### 1.2 图面字符绝对英文纯净化与双语对照 (Pure English Image Font Lock & Bilingual Mapping)
* **图面防崩溃硬红线**：无论是“中文参考轨”还是“英文运行轨”，生成的生图提示词（Image2）中**绝对禁止**指示模型在图片画布上渲染任何中文字体或复杂的英文长句。
* **英文标识统一锁定**：图面上所有面板、零件、视角一律只允许使用极其简单的英文符号/标签（如 `Panel A`, `B`, `C`, `FRONT`, `SIDE`, `BACK`, `GRID A1`, `Label_A`, `Label_B`），且字体声明为干净简约的 Sans-serif。必须添加负面关键字（`no Chinese text, no garbled letters, no distorted text labels, clean typography`）消音。
* **双轨字符策略**：
  1. **中文参考版提示词 (`*_prompts_CN_reference.md`)**：生成图片时同样使用英文标识，但必须在 Markdown 文本中提供 **“中英双语图面标识映射表” (Bilingual Structural Mapping Table)**，供导演/人类操作员完美对照和理解（如 `Panel A = 全身前视图`、`Label_A = 锁扣爆炸分解`）。
  2. **英文无损运行版提示词 (`*_prompts_EN_executable.md`)**：保持纯英文的极简排版与无损英文标签，直接用于模型跑图。

---

## 2. 角色资产设计圣经 (Character Asset Layout Bible)

为了彻底锁定角色面部 seed 并在不同镜头中无漂移复现，角色资产卡必须遵循以下严格的排版布局与剧情驱动模块：

### 2.1 角色卡标准网格排版 (Standard Layout Grid)
单张 16:9 画布必须严格划分为标准的模块化网络，排版严密锁定，拒绝任何随机堆砌：
* **模块一：全身四视图 (4-View Full Body Grid)**：从左到右依次为正视图（Front View）、侧视图（Side View）、后视图（Back View）、3/4 侧身斜视步态图（3/4 Walking Pose）。角色在此四视图中身着标准剧照服装（服装面料与颜色硬性声明），身体比例保持一致。
* **模块二：人脸中性特写 (Neutral Facial Close-up)**：高解析度的正面素颜/中性表情人脸特写，光影均匀（柔和三点光），作为最核心的 face seed 图像。
* **模块三：服装纹理特写 (Wardrobe & Texture Detail)**：局部微距镜头（Macro close-up），清晰展示服装材质（如“粗布长衫的经纬织纹”、“皮革旅行箱的磨损划痕”），供视频生成参考。

### 2.2 剧情驱动的可变模块 (Story-Driven Dynamic Sheets)
角色资产不能是无用的静态堆砌，必须紧密结合剧本需求设计以下**可变参考模块**：
* **表情情绪变化表 (Emotions Sheet)**：若剧本中有大喜、大悲、极度惊恐等情绪撕裂（如李侠得知战友牺牲），必须有一组 4-Grid 表情卡，展示特定情绪下眼睑、嘴角及面部肌肉的物理变化。
* **发型与时间跳跃变化表 (Hairstyle & Temporal Shifts)**：若剧情存在年代跨度（如李侠从1945年到1990年），角色卡必须设计并标出不同年龄、发型（黑发到全白）的对比视图。
* **物理状态与伤残装束表 (Physical Status & Costume Changes)**：若剧情需要角色处于受伤、被捕、或伪装状态，必须绘制对应的辅助资产模块（如“领口撕裂、脸上带有尘土与血痕的状态”）。

### 2.3 辅助角色与群像资产分化规范 (Group Swarm & Auxiliary Protocols)
* **人物密度上限**：单张 16:9 画布最多同时呈现 **2 个** 辅助角色。如果超过 2 人，必须自动分页在下一张画布上设计。
* **群像资产区分圣经 (Crucial Distinctions)**：
  1. **年龄区分**：皱纹深度、眼角耷拉度、面部肌肉松弛度必须有断代级差异。
  2. **职业区分**：服装粗糙度、配饰（如首长的布帽、报童的斜挎挎包、特务的皮手套）绝对区分。
  3. **发型服饰区分**：长短、发线、灰白比例、服装色相绝对不同。
  4. **高矮胖瘦区分**：骨架宽度、肩宽比、头身比在多视图中硬性拉开。
  5. **五官长相区分 (核心)**：对于“统一制服”（如八路军或国民党士兵）群像，必须将提示词重点锁死在**面部骨骼、眼距、颧骨高低、鼻梁弧度**的巨大差异上，拒绝克隆脸。

---

## 3. 场景设计圣经 (Scene Layout Bible)

场景参考图是视频生成保持空间感不缩水的唯一保障，必须遵守以下圣经级参数：

### 3.1 场景九宫格排版标准 (9-Angle Panorama Grid)
每个主场景必须以九宫格（3x3 Layout Grid）在一张画布上完美呈现，拒绝多余的标注：
* **1-3 格：全局空间视角**（远景、中景、俯拍鸟瞰图，明确划分室内布局与室外空间衔接）。
* **4-6 格：特定灯光日夜转换**（白天冷天光自然漫射、黄昏金色逆光、夜晚高反差明暗对比 Chiaroscuro 动机光）。
* **7-9 格：环境安全区与局部特写**（如“写字台上的玻璃烟灰缸特写”、“窑洞门前挂着的红辣椒与干玉米细节”）。

### 3.2 空间地理与人物占位锁定 (Spatial Mapping & Anchors)
* **人物占位安全区 (Character Placement Safe Zone)**：图上必须以英文网格坐标明确标注人物的站位界限。例如，声明 `CHAR_PLACEHOLDER_GREY is limited to Sector B2 (next to the wooden table) and Sector C2 (walking path)`。
* **防干扰静默标注**：九宫格内仅保留纯英文的格位代码（如 `Cam_A_Wide`, `Cam_B_Detail`），严禁标出任何杂乱的说明文字，防止 Seedance 在读取时误将文本识别为画面中的实物进行渲染。

---

## 4. 道具设计圣经 (Prop Layout Bible)

反复出现的重点道具是情节流转的线索，必须作为独立高精度资产锁定：

### 4.1 道具三视图与爆炸图规范 (Multi-Angle Exploded View)
对于剧本中承载核心功能或出现频率极高的道具（如李侠的“收音机改装发报机 `PROP_RADIO_TRANSMITTER`”、“磨损复古皮革行李箱 `PROP_LEATHER_SUITCASE`”）：
* **排版规范**：在一张 16:9 画布上，展示道具的正面（Front）、侧面（Side）及**内部细节爆炸图/结构拆解图**（如收音机拆开后内部密密麻麻的真空管与电子元器件）。
* **精确定位引用机制 (Referencing Coordinates)**：
  在道具卡的英文版中，对重要部件使用标准坐标标签圈定（例如：在发报机电键处标注 `Label_Key`，在天线线圈处标注 `Label_Coil`）。后续 Seedance 提示词中即可精准引用：`@AssetCard_PROP_RADIO_TRANSMITTER(Label_Key)`。

---

## 5. 故事板设计圣经 (Storyboard Layout Bible)

故事板是连接导演思维与 AIGC 模型的桥梁。**它的核心作用是：用画面把 Seedance 提示词写不出来的物理轨迹和空间关系画出来，把文字容易产生歧义的视觉设计死死钉住！**

### 5.1 故事板角色无脸化灰格人偶占位符机制 (Faceless Silhouette Storyboard)
* **绝对红线**：为了防止故事板中的角色面部特征污染主角色卡（导致 Seedance 生成时角色五官融合变形），**故事板中绝对不允许画出任何角色的具体脸部与发型细节！**
* **人偶占位符标准**：所有人类角色一律用灰色无脸三维木偶或剪影（`CHAR_PLACEHOLDER_GREY`）表示。画面仅体现其高矮身材比例、肢体动作姿态（Body Language）与物理阻挡、运动轨迹。

### 5.2 故事板四象限技术网格排版 (4-Quadrant Technical Matrix)
故事板的每一步镜头，均在 Obsidian Slate Gray 背景上，以高度严密的**四象限网格**布局展示：

| 象限 | 英文名称 | 核心表现内容与运镜指示 |
| :--- | :--- | :--- |
| **第一象限** | **Top-View Motion Map** | 顶视运动平面图。用二维极坐标图展示本场景的墙壁、主要道具位置，用虚线画出角色与摄影机的移动轨迹。 |
| **第二象限** | **Camera Setup Diagram** | 机位设置图。以三维示意图展示摄像机的物理高度（低角度俯拍、仰拍、平拍）、镜头俯仰倾角、焦平面位置。 |
| **第三象限** | **Motivated Motion Vector** | 运镜路线图。通过纯英文的运动矢量剪头（如 `Dolly-in Vector`, `Whip-pan Axis`），可视化展示镜头的物理推进。 |
| **第四象限** | **Chiaroscuro Atmosphere** | 光影氛围图。无任何复杂材质，仅以高反差的黑白灰块面（Chiaroscuro），指明本镜头的唯一核心动机光源位置及阴影投射区。 |

### 5.3 15秒分镜技术引导表 (15-Second Segment Matrix)
故事板下方，必须配有严格对应 15 秒内的分镜技术细节矩阵。分镜的格数与划分必须**完全由剧情呼吸感和叙事节奏决定**（杜绝死板的一成不变划分为 5 格，允许 1 个极长镜头或 3 个中等镜头）：

* **镜号与时长锁 (Shot ID & Duration Lock)**：例如 `SEG_01 (0:00 - 0:07)`。
* **构图占位 (Composition Placement)**：标明角色占位网格（如 `CHAR_PLACEHOLDER_GREY located on left 1/3 grid`）。
* **景别与焦段 (Shot Size & Lens Lock)**：如 `Close-up, Cooke 75mm lens`。
* **运镜矢量 (Camera Motion)**：如 `motivated slow dolly-in parallel to 180-degree axis`。
* **台词与音效 (Dialogue & SFX)**：物理台词、画外音（VO）以及秒级 Foley 音效（如“`0:02` 关门碰撞声”、“`0:05` 风沙刮擦声”）。
* **物理特效 (VFX)**：模型可稳定渲染的微小粒子路径（如“细微飘雪”、“逆光中缓慢飞扬的微尘”、“徐徐升腾的香烟蓝烟”）。

---

## 6. Seedance 2.0 终极提示词专家规范 (Seedance Prompt Expert Bible)

Seedance 2.0 视频生成的成败完全取决于提示词的精密程度。**必须彻底抛弃简短的句子，全力以赴榨干 5000 字的字符上限**，写出融合全局设定、资产引用、秒级时间码微调及多维度负面约束的完美提示词包：

### 6.1 图像-视频双向解耦与安全切分圣经 (Image-to-Video Visual Reference Decoupling)
* **防噪防崩绝对红线**：**严禁直接将包含四视图、九宫格、坐标标签、黑底细网格等多面板的资产卡整体图喂入 Seedance 2.0 作为 I2V（图生视频）的参考图！** 否则，视频模型会误读拼贴排版，把多画面分割和灰色背景网格渲染进视频，导致画面极度混乱。
* **单幅参考图切割机制**：若需使用资产图作为 Seedance 2.0 的视觉参考，操作员必须采用以下两种机制之一：
  1. **单图裁剪 (Crop Reference)**：将多视图资产卡中的特定面板（如 `Panel B` 脸部特写或 `Panel A` 全身前视图）单独裁剪成单张 16:9 的干净无网格图像，作为 face seed / costume seed 的输入。
  2. **分镜关键帧生成 (Keyframe Reference)**：直接使用“故事板分镜提示词”生成单张 16:9 干净无网格的实拍级画面（不包含四象限网格和无脸占位符），以其作为 Seedance 的 I2V 首帧/参考帧。

### 6.2 全局视觉风格词段动态注入圣经 (Global Visual Style Block & Dynamic Prompt Injection)
单纯依赖图像参考不足以完全锁死视觉调性。为了实现 100% 电影级色彩与质感的一致性，系统必须定义一个高度浓缩的 **“全局视觉风格词段” (Global Visual Style Block)**，并在编译时**动态地注入到每一段 Seedance 2.0 分镜提示词的头部与尾部**。
* **全局视觉风格词段构成**：
  * 包含摄像机型号、镜头焦段、胶片型号、Chiaroscuro 动机光温与光比、环境氛围粒子等风格代码。
  * 示例：`[GLOBAL STYLE: 1930s cinematic spy-thriller look, Cooke Panchro prime lens, high-contrast chiaroscuro, desaturated military green and warm amber color grading, faded 1940s film grain, volumetric fog, organic micro dust particles, no game CG look, photo-realistic]`
* **动态注入机制**：
  * 智能体和提示词编译工厂在输出每一段 Segment 时，必须将该全局视觉风格词段无条件拼接到 Segment Prompts 的最前与最后，建立全方位的文法围栏，强力约束 Seedance 2.0 的生成空间，保证镜头之间不发生色彩与光影的漂移。

### 6.3 资产与故事板精准 `@圈图` 声明 (Precise Asset Referencing)
In describing movements, explicitly reference structural zones of the asset maps to prevent visual drift:
```text
[ASSET COORD REFERENCE DECLARATION]
- Character Reference: Referencing face seed from @AssetCard_CHAR_LIXIA(Panel B - Facial Close-up) and wardrobe base from @AssetCard_CHAR_LIXIA(Panel A - Grey gown).
- Scene Reference: Referencing spatial layout and architecture from @AssetCard_SCENE_YANAN_PAGODA(Sector A1 - Wide View) and environment assets from @AssetCard_SCENE_YANAN_PAGODA(Sector C1 - Pagoda bricks).
- Prop Reference: Referencing vintage suitcase from @AssetCard_PROP_LEATHER_SUITCASE(Panel A - Orthographic profile).
- Storyboard Reference: Ingesting movement vector and blocking coordinates from @StoryboardCard_SEG_01(Quadrant I & III).
```

### 6.3 毫秒级时间轴动作与细节拆解 (Milisecond Timeline Breakdown)
将 15 秒内的分镜切分为精细的秒级动作指示，将镜头移动、人物微表情、物理特效、声响 Foley 高度融合：
```text
[TIMELINE MOTION & PERFORMANCE BEAT]
- 0:00 - 0:03: Camera begins in a tight close-up on CHAR_LIXIA's eyes. Cooke 75mm lens, shallow depth of field. CHAR_LIXIA stands still on the loess dirt road of SCENE_YANAN_PAGODA, looking toward the distant Pagoda Mountain. Fine yellow sand dust particles slowly drift from left to right across his face in the wind. Subtle jaw muscles clenching, eyes unwavering.
- 0:03 - 0:07: Motivated slow dolly-out camera movement, expanding to a medium shot. The Chief CHAR_SHOUZHANG enters the frame from the right side, strictly respecting the 180-degree axis line. His hand, covered in a faded cotton sleeve, slowly reaches out and pats CHAR_LIXIA's shoulder gently, twice. CHAR_LIXIA’s lips part slightly as he takes a deep, calm breath (VOICE_LOCK: slow gravelly breathing), showing emotional restraint.
- 0:07 - 0:11: Cut to an over-the-shoulder shot from behind CHAR_SHOUZHANG's shoulder, looking at CHAR_LIXIA. Li Xia CHAR_LIXIA grips the vintage leather suitcase PROP_LEATHER_SUITCASE tightly with his right hand (no hand distortion, five distinct fingers clearly visible). He bows deeply at 45 degrees towards the Chief and the exactly three comrades standing in a perfect row in the background.
- 0:11 - 0:15: Dolly-in slowly behind CHAR_LIXIA as he straightens up, turns his back resolutely, and walks away along the center of the dusty road. In the background, the Chief and the three comrades simultaneously raise their right hands to execute a synchronized, crisp military salute. Golden sunset glow forms a warm rim light around their silhouettes, creating a powerful, epic historical farewell atmosphere.
```

### 6.4 多维度严苛负面提示词约束 (Multidimensional Negative Constraints)
在提示词结尾，根据剧本特征和模型易犯的毛病，定制全方位的负面过滤，绝对杜绝画面崩坏：
```text
[MULTIDIMENSIONAL NEGATIVE PROMPT GUARDS]
Negative Prompt: Deformed hands, overlapping fingers, mutated limbs, distorted facial features, face melting, extra fingers, merging bodies, mismatched eyes. Text, burned-in subtitles, captions, on-screen watermarks, logos, dates, timestamps. Kraft paper texture, oil paper background, colorful glowing halos, random lens flares, neon flashes, game engine style, highly saturated cartoon illustration. Camera axis crossing, sudden cuts within the timeline segment, spatial warping, morphing architectures, cloning background characters, identical cloned faces.
```

---

## 7. 验收与评分卡 (Downstream Verification Scorecard)

操作员在拿到渲染输出后，根据此卡进行严苛评分，未达到 90 分以上的 take 必须无条件重跑：

| 评估指标 | 工业级权重 | 完美合格标准（0-100分评判） |
| :--- | :--- | :--- |
| **基底与色彩漂移** | 20% | 资产与分镜背景是否全为 **Obsidian Slate Gray**？视频与前一镜色相误差是否小于 5%？ |
| **面部一致性** | 25% | 主角李侠在各镜头的五官特征、眼镜框、发型是否漂移？是否有“瞬变脸”现象？ |
| **手部与道具逻辑** | 20% | 提行李箱、拍肩膀等手部与道具接触面是否有指关节畸变（无 overlapping fingers）？ |
| **镜头运动与轴线规避** | 15% | 镜头是否匀速有动机平移？是否严格遵守 180° 轴线，没有出现方向错乱的越轴？ |
| **画幅干净度 (Clean Frame)** | 20% | 视频全长是否 100% 无任何杂乱英文字母、汉字水印或 AI 自动烧录的字幕？ |

---
本圣经为最高开发标准，任何智能体在处理微短剧生成时，必须绝对贯彻上述物理背景与双轨提示词编译算法。
