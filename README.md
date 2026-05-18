# AIGC Film Production Master Skill

> v1.6.0 | 2026-05-19

一个面向 AIGC 影视创作者的工业级全链路总控 skill。

它不是单纯帮你写剧本，也不是直接生成几条 Seedance 提示词，而是把一句创意、现成剧本、参考片、角色图、场景图或品牌/宣传需求，整理成一套可以进入工业化生产的 AIGC 影视流程：

```text
创意 / 剧本 / 参考片 / 资产
-> 上游编剧与结构强化
-> AIGC 导演可生产化
-> Image2 + Seedance 生产交接包
-> 下游资产板 / 故事板 / Seedance 2.0 提示词
-> 出片验收 / 返修 / 后期交付
```

它默认服务 AIGC 创意短片、AI 真人短剧、AI 漫剧、广告片、TVC、文旅片、MV、比赛片和宣传视频。长篇系列和 90 分钟电影规划作为扩展能力保留，但不是当前默认生产重心。

## Quick Start

如果你现在就要把这个 skill 交给 Codex、OpenClaw、Hermes 或其他智能体工具，用下面这组信息就够了。

安装仓库地址：

```text
https://github.com/wp746/aigc-film-production-master.git
```

技能入口地址：

```text
https://raw.githubusercontent.com/wp746/aigc-film-production-master/main/SKILL.md
```

压缩包地址：

```text
https://github.com/wp746/aigc-film-production-master/archive/refs/heads/main.zip
```

推荐先看：

- [SKILL.md](SKILL.md)
- [入口识别与路由](references/intake-routing.md)
- [来源摄入与归一化](references/source-ingestion-normalization.md)
- [短片/短剧/广告电影级流水线](references/shortform-filmgrade-pipeline.md)
- [创意开发编排](references/creative-development-orchestration.md)
- [上游编剧与导演系统](references/upstream-screenwriting-director.md)
- [品牌 / 广告 Brief 引擎](references/brand-ad-brief-engine.md)
- [短视频留存与传播门禁](references/retention-performance-gate.md)
- [AIGC 导演系统](references/aigc-director-system.md)
- [AIGC 生产交接协议](references/aigc-production-handoff-contract.md)
- [模型与平台适配器](references/model-platform-adapter.md)
- [Universal Agent Adapter](references/universal-agent-adapter.md)
- [Image2 + Seedance 下游桥接](references/downstream-image2-seedance-bridge.md)
- [最终提示词交付协议](references/final-prompt-delivery-contract.md)
- [模块可见性与回装协议](references/module-visibility-and-reinsertion.md)
- [长片 / 系列控制](references/longform-series-film-control.md)
- [长片资产数据库与生产台账](references/asset-database-ledger.md)
- [后期交付](references/postproduction-delivery.md)
- [隐私 / 来源 / 复用治理](references/privacy-provenance-governance.md)
- [合规 / 版权 / IP 风险门](references/compliance-rights-ip-gate.md)
- [版本管理与反馈闭环](references/versioning-feedback-loop.md)
- [类型片 Playbook 索引](references/genre-playbook-index.md)
- [悬疑惊悚深度 Playbook](references/genre-playbooks/suspense-thriller.md)
- [文旅深度 Playbook](references/genre-playbooks/cultural-tourism.md)
- [广告/TVC 深度 Playbook](references/genre-playbooks/commercial-tvc.md)
- [短剧深度 Playbook](references/genre-playbooks/short-drama.md)
- [黑色幽默深度 Playbook](references/genre-playbooks/black-humor.md)
- [QA 与风险门禁](references/qa-risk-gates.md)

> 注意：如果仓库是 private，OpenClaw / Hermes / 其他智能体需要具备访问该 GitHub 仓库的权限。

## 它解决什么问题

这个 skill 主要解决 AIGC 影视生产里的 12 个关键问题：

1. 用户只有一句创意，不知道如何发展成可拍、可生成、可交付的短片或短剧。
2. 用户已有剧本，但剧本没有按 AIGC 生产能力拆成资产、场景、道具、分镜和段落。
3. 传统导演方案偏实拍思维，无法严丝合缝交给 Image2 + Seedance 2.0。
4. 上游编剧、导演、下游提示词生产各自独立，交接时丢失故事意图。
5. 一个好概念进入下游后，被模型能力限制拖垮，变成普通 AI 视频。
6. 复杂镜头没有提前判断可生成性，导致 Seedance 多人、多动作、多文本、多 VFX 同时失败。
7. 现成剧本直接丢给下游 SOP，缺少 AIGC 导演可生产化改造。
8. 长短剧、系列、电影没有项目圣经和状态追踪，越做越散。
9. 精确中文文字、手机 UI、倒计时、字幕、标题卡被错误交给视频模型生成。
10. 出片之后没有验收、返修和后期交付逻辑，只能凭感觉重生。
11. 编剧系统只管故事，下游系统只管提示词，中间缺少“制片总控层”。
12. 想把整套方法论放到 GitHub，在任何智能体上复用，但缺少统一入口。
13. 用户输入来源复杂：一句话、剧本、brief、参考图、参考片、资产图混在一起，容易没有统一事实来源。
14. 宣传广告项目只追求“好看”，缺少产品真相、受众、CTA、品牌记忆和宣传声明风险。
15. 短视频没有留存节奏，前 2 秒、5 秒、结尾记忆点不够明确。
16. 不同视频模型/平台能力不同，但提示词仍按同一套 Seedance 假设硬写。
17. 客户素材、私人照片、参考片、生成资产没有来源、权限和复用边界。
18. 用户改了某个模块后，下游提示词不知道该局部更新还是全量重做。

## 核心定位

`aigc-film-production-master` 是一个 **上游 + 中控 + 路由型 skill**。

v1.2.0 起，它的默认定位更明确：

```text
短片 / 短剧 / 宣传广告
-> 电影级创意
-> 电影级质感
-> AIGC可生产导演方案
-> Image2资产板与故事板
-> Seedance 2.0最终提示词
```

长电影能力保留，但只有用户明确要求“长片、90分钟电影、系列化长项目”时才进入长片模块。

v1.3.0 起，系统交互方式进一步明确：

```text
后台发生化学反应，
前台默认只交付最终下游双语提示词。
```

也就是说，创意判断、反套路、AIGC导演可行性、合规、QA、后期职责等过程默认都在后台完成，不把内部推演过程展示给用户。用户只有在明确要求“拎出某一模块看看”时，才展示该模块。

它不替代你已有的 `image2-seedance-control`。正确关系是：

```text
aigc-film-production-master = 总制片 / 主编剧 / AIGC 导演 / 生产路由
image2-seedance-control = 下游 Image2 资产板 + 故事板 + Seedance 2.0 提示词工厂
```

也就是说：

- 上游不成熟时，它负责创意孵化、剧本强化、结构设计和反套路。
- 剧本已存在时，它负责诊断、保留强项、做 AIGC 可生产化改造。
- 进入生产前，它负责输出 AIGC 导演方案和生产交接包。
- 下游真正写 Image2 / Seedance prompt 时，优先调用 `image2-seedance-control`。

## 核心能力

### 1. 输入识别与生产路由

自动判断用户输入属于：

- 一句话创意
- 现成剧本
- 短剧单集
- 60 集短剧
- 90 分钟电影
- 参考片复刻
- 已有角色 / 场景 / 道具资产
- 只需要下游提示词
- 需要完整工业级 SOP

然后决定先做故事、先做导演方案、先做资产交接，还是直接进入下游生产。

### 1.2 来源摄入与归一化

v1.4.0 起，任何输入先归一化为 `Source Packet`。

它会把一句话创意、现成剧本、客户 brief、参考图片、参考视频、已有角色/场景/道具资产、平台规则或比赛规则整理成统一事实源。这样系统后面的编剧、导演、合规、下游提示词都基于同一个来源，不会各说各话。

### 1.5 短片 / 短剧 / 广告默认闭环

系统默认执行 `shortform-filmgrade-pipeline.md`：

```text
任意创意输入
-> 创意判断
-> 故事/广告核心
-> 类型片与风格策略
-> AIGC导演可行性
-> 资产/场景/道具/文字职责
-> Image2资产板
-> Image2故事板
-> Seedance 2.0提示词
-> 后期交付提示
```

每个全流程任务必须经过：

- `INTAKE_LOCK`
- `CREATIVE_LOCK`
- `GENRE_STYLE_LOCK`
- `AIGC_FEASIBILITY_LOCK`
- `PRODUCTION_HANDOFF_LOCK`
- `PROMPT_FACTORY_LOCK`
- `POST_LOCK`
- `QA_LOCK`

这些环节可以压缩，但不能跳过。

### 1.8 短视频留存与传播门禁

v1.4.0 起，短片、短剧、广告、文旅、比赛片会额外检查首帧、0-2 秒、5 秒理解、15 秒升级、结尾记忆点和平台气质。

这不是为了把所有作品都做成快餐，而是让电影级质感也能适配短视频消费。

### 2. 上游编剧强化

当用户只有创意或剧本不够强时，skill 会先补齐：

- 故事引擎
- 主角欲望
- 主角缺陷
- 对抗压力
- 主题
- 代价规则
- 反套路机制
- 误导与反转
- 结尾后劲
- 可视化场景结构

它不会只写“正确但普通”的故事，而是会主动检查最俗套版本，并设计更有惊喜和回味的版本。

### 2.5 创意开发编排

v1.1.0 起，系统明确规定：下游 `image2-seedance-control` 不能承担爆款故事、反套路结构、后劲设计和人物命运弧的主脑职责。

创意开发由 master 协调上游完成：

- 优先调用 `save-the-cat-screenwriting-skill`
- 必要时调用类型片专用 playbook
- 没有外部 skill 时，使用内置创意开发编排模块

核心产出包括：

- 项目观众承诺
- 故事引擎
- 人物命运弧
- 反套路检查
- 代价规则
- 道德陷阱
- 结尾后劲图像
- AIGC 生产影响判断

### 3. 现成剧本诊断

如果用户已经有剧本，不会直接重写。

先判断：

- 哪些戏已经有效，必须保留。
- 哪些结构弱，需要加强。
- 哪些台词、反转、母题、结尾不能乱动。
- 哪些段落对 AIGC 生产风险高。
- 哪些文字、UI、VFX、群戏、动作应拆分或放到后期。

然后输出：

- `Keep`
- `Sharpen`
- `AIGC Adapt`
- `Do Not Change`

### 4. AIGC 导演可生产化

传统导演会说“镜头要有压迫感”“这里要拍得震撼”。

这个 skill 要求导演语言必须转成生产职责：

- `Image2 Asset Duty`
- `Image2 Storyboard Duty`
- `Seedance Duty`
- `Post Duty`
- `Avoid / Split`

例如：

```text
倒计时数字不要交给 Seedance 精确生成，
应拆成 VFX_COUNTDOWN 视觉规则 + POST_OVERLAY 后期叠加。
```

### 5. AIGC 可行性判断

每个场景或段落都会判断：

- `DIRECT_GENERATABLE`
- `ASSET_REQUIRED`
- `BOARD_REQUIRED`
- `POST_REQUIRED`
- `SPLIT_REQUIRED`
- `AVOID`

这能防止把模型不擅长的内容硬塞给 Seedance，减少废片率。

### 6. 生产交接包

进入下游前，skill 会把故事和导演意图整理成结构化交接包：

- 项目锁定
- 已批准剧本版本
- 全局视觉风格
- 角色资产矩阵
- 场景空间矩阵
- 道具 / UI / 文字矩阵
- Seedance 段落计划
- 段落复杂度预算
- 上下段接缝状态
- 下游调用说明

这个交接包就是给 `image2-seedance-control` 使用的生产合同。

### 6.2 品牌 / 广告 Brief 引擎

对于宣传广告、TVC、产品片、文旅推广、公服片、比赛 brief，系统会先锁定产品/地点/品牌真相、目标受众、单一传播主张、情绪钩子、功能证明、品牌记忆装置、CTA、must include / must avoid，以及宣传声明和合规风险。

广告不是只要“拍得高级”，还要让用户记住、相信、想要或行动。

### 6.5 最终提示词交付

v1.2.0 起，如果用户要的是“全流程”“工业级”“最终提示词”“直接出图出视频”，系统不能停在生产交接包。

必须继续生成一个最终 Markdown 文件，包含：

- Image2 资产板提示词
- Image2 故事板提示词
- Seedance 2.0 提示词
- CN 审阅版
- EN 生产版
- Segment 本地 0:00-0:15 时间码
- 每段参考图职责
- clean-frame 文字禁令
- in/out state
- post duties

默认文件名：

```text
outputs/[project-slug]-image2-seedance-prompts-v001.md
```

### 6.55 模型与平台适配

v1.4.0 起，最终提示词生成前会检查目标模型和平台：视频模型、图像模型、单段时长、提示词长度、多参考图能力、首尾帧能力、文字渲染能力、音频支持、画幅和平台安全边界。

默认仍以 Image2 + Seedance 2.0 为核心，但不会假设所有模型都一样。

### 6.6 模块可见性与回装

v1.3.0 起，系统新增模块可见性规则。

默认隐藏：

- 入口路由判断
- 创意开发编排
- 反套路与后劲判断
- 类型片 / 风格策略
- AIGC 导演可行性图
- 生产交接协议
- 合规 / 风险筛查
- 后期职责拆分
- QA 门禁
- 提示词完整性检查

这些模块的结果必须被烘焙进最终提示词，而不是作为一大堆过程说明展示给用户。

但当用户明确要求时，可以单独展示某个模块，例如：

```text
把导演模块拎出来看看
先看风格模块
展示生产交接包
这个模块我想改
先别进入下游
```

用户修改模块后，系统必须：

1. 把用户修改后的模块作为该层新的事实来源。
2. 判断它影响哪些下游资产板、故事板、Seedance 段落或后期职责。
3. 只重写受影响的提示词。
4. 保留已批准且未受影响的模块。
5. 再重新输出最终提示词文件。

### 6.7 版本管理与反馈闭环

v1.4.0 起，用户修改某个模块后，系统会判断影响范围。能局部更新就不全量推翻，已批准模块不随便重写。

例如：改角色身份会影响角色资产板、相关故事板和相关 Seedance prompt；改风格会影响全局 look lock 和所有视觉提示词；改台词会影响 Seedance 声音节奏、字幕/SRT 和后期。

### 7. 长片 / 系列控制

针对 12 集、24 集、60 集短剧或 90 分钟电影，skill 不会直接开始写每一集提示词。

它会先建立：

- 故事圣经
- 角色圣经
- 世界观圣经
- 资产圣经
- 分集 / 段落结构
- 人物状态追踪
- 伏笔 / 回收表
- 生产优先级

长项目默认只把一个生产块送入下游，例如：

- `EP01`
- `Sequence 01`
- `Act 1 sample`
- `Key trailer scenes`
- `Asset bible first`

这样可以控制成本、漂移和返修风险。

### 7.5 长片级资产数据库

v1.1.0 起，长项目不只依赖命名规则，而是要求建立资产数据库和生产台账。

内置数据库表包括：

- `characters.csv`
- `character_states.csv`
- `scenes.csv`
- `scene_states.csv`
- `props.csv`
- `prop_states.csv`
- `shots.csv`
- `seedance_takes.csv`
- `reusable_assets.csv`
- `repair_log.csv`

用于追踪：

- 角色状态
- 场景状态
- 道具状态
- 镜头台账
- 已生成 take 评分
- 可复用资产
- 返修历史

60 集短剧或 90 分钟电影，如果没有这些表，不允许称为工业级长片生产。

### 8. 后期交付规划

它会明确哪些任务不该交给视频模型，而该交给后期：

- 字幕
- 标题卡
- 手机 UI
- 合同 / 文件 / 招牌
- 倒计时
- 声音设计
- 旁白
- 音乐 cue
- VFX 叠加
- 剪辑节奏
- 调色统一
- 平台交付规格

v1.1.0 起，后期模块进一步补齐：

- EDL / 剪辑决策表
- 旁白 / 对白 / ADR cue sheet
- 音乐 cue sheet
- 声音设计 cue sheet
- SRT 字幕草稿
- VFX / UI overlay 清单
- 调色 / LUT 方向
- 最终导出规格

### 9. 合规 / 版权 / IP 风险门

当项目涉及品牌、名人、公众人物、参考片复刻、平台投放、比赛投稿、音乐、声音、肖像、IP 或风格参考时，必须运行合规风险门。

系统会检查：

- 品牌 / 商标
- 名人 / 肖像
- 私人图像 / 声音
- 版权 IP
- 风格参考
- 音乐 / 歌词
- 声音克隆
- 平台 / 比赛规则
- 产品宣传声明
- 安全与内容风险

如果本地有 `compliance-review-skill`，优先让它做专项审核。

### 9.5 隐私 / 来源 / 复用治理

v1.4.0 起，用户上传的私人照片、客户素材、参考片、品牌文件和生成资产都要记录来源和复用边界。

最终分享给外部智能体或客户的提示词文件，不应暴露私人路径、客户机密、未授权素材来源或用户敏感信息。

### 10. 类型片 Playbook

v1.1.0 起，新增类型片索引，不再默认所有片子都用同一种“电影感”。

v1.5.0 起，最常用的五类已经从索引升级为深度 playbook：

- 悬疑惊悚：[suspense-thriller.md](references/genre-playbooks/suspense-thriller.md)
- 文旅：[cultural-tourism.md](references/genre-playbooks/cultural-tourism.md)
- 广告/TVC：[commercial-tvc.md](references/genre-playbooks/commercial-tvc.md)
- 短剧：[short-drama.md](references/genre-playbooks/short-drama.md)
- 黑色幽默：[black-humor.md](references/genre-playbooks/black-humor.md)

每个深度 playbook 都包含：

- 观众承诺
- 故事动作
- 镜头与调度
- 节奏结构
- 声音策略
- AIGC 风险
- 下游提示词策略
- CN/EN prompt locks
- 避坑清单

已覆盖：

- 悬疑
- 恐怖
- 黑色电影
- 喜剧
- 科幻
- 赛博
- 国风
- 年代戏
- 纪录片
- 儿童动画
- 文旅
- 实验短片
- 音乐剧
- 爱情
- 动作
- 黑色幽默

每个类型都会定义：

- 观众承诺
- 故事动作
- 视觉语言
- 声音语言
- AIGC 风险
- 下游生产策略

## 标准工作流

默认工业链路是：

```text
Intake
-> Story / Script Diagnosis
-> Screenwriting Enhancement
-> AIGC Director Package
-> AIGC Production Handoff
-> Image2 + Seedance Prompt Factory
-> Final Prompt Markdown File
-> Generation Review
-> Repair Loop
-> Postproduction Delivery
```

关键原则：

- 没有故事引擎，不进入长项目生产。
- 没有 AIGC 导演方案，不把复杂剧本丢给下游。
- 没有生产交接包，不开始 Image2/Seedance 提示词。
- 没有资产职责，不写故事板。
- 没有 in/out state，不进入多段生成。
- 精确文字、字幕、UI、倒计时优先交给后期。
- 用户要求全流程时，不允许只给交接包，必须给最终可复制提示词文件。

## 与其他 skill 的关系

### 与 save-the-cat-screenwriting-skill

`save-the-cat-screenwriting-skill` 更偏上游编剧：创意、结构、剧本、反套路、后劲。

`aigc-film-production-master` 会吸收它的思路，并把结果继续推进到 AIGC 导演和下游生产。

### 与 image2-seedance-control

`image2-seedance-control` 是成熟下游 SOP，负责：

- Image2 资产板提示词
- Image2 故事板提示词
- Seedance 2.0 prompt
- CN/EN 提示词
- 多参考图上传顺序
- prompt lint
- 出片验收
- Seedance 返修

`aigc-film-production-master` 不替代它，而是把上游意图整理成它能直接使用的交接包。

### 与 aigc-asset-board-skill

如果项目只需要先做角色、场景、道具资产板，可以单独使用 `aigc-asset-board-skill`。

如果项目要从创意或剧本进入完整生产，应使用本 skill 作为总控。

## 输出物

根据用户需求，最终可以输出：

- 一句话创意孵化方案
- 故事方案
- 剧本 Markdown 文件
- AIGC 导演方案
- AIGC 生产交接包
- 长片 / 系列项目圣经
- Image2 + Seedance 下游输入包
- 后期剪辑交付计划
- QA 风险门禁报告
- 项目生产目录结构

## 仓库结构

仓库根目录就是 skill 根目录，已经可直接分发：

```text
aigc-film-production-master/
  SKILL.md
  README.md
  agents/
    openai.yaml
  references/
    intake-routing.md
    source-ingestion-normalization.md
    shortform-filmgrade-pipeline.md
    creative-development-orchestration.md
    upstream-screenwriting-director.md
    brand-ad-brief-engine.md
    retention-performance-gate.md
    aigc-director-system.md
    aigc-production-handoff-contract.md
    model-platform-adapter.md
    universal-agent-adapter.md
    downstream-image2-seedance-bridge.md
    final-prompt-delivery-contract.md
    module-visibility-and-reinsertion.md
    longform-series-film-control.md
    asset-database-ledger.md
    postproduction-delivery.md
    privacy-provenance-governance.md
    compliance-rights-ip-gate.md
    versioning-feedback-loop.md
    genre-playbook-index.md
    genre-playbooks/
      suspense-thriller.md
      cultural-tourism.md
      commercial-tvc.md
      short-drama.md
      black-humor.md
    qa-risk-gates.md
  scripts/
    create_project_skeleton.py
    audit_skill_contract.py
```

## 安装地址

如果 Codex / OpenClaw / Hermes 支持直接从 GitHub 仓库安装 skill，优先填：

```text
https://github.com/wp746/aigc-film-production-master.git
```

也可以填仓库页面地址：

```text
https://github.com/wp746/aigc-film-production-master
```

如果对方支持用原始入口文件识别 skill，可以填：

```text
https://raw.githubusercontent.com/wp746/aigc-film-production-master/main/SKILL.md
```

如果对方更适合下载压缩包安装，可以用：

```text
https://github.com/wp746/aigc-film-production-master/archive/refs/heads/main.zip
```

## OpenClaw / Hermes 使用建议

如果它们支持“从 Git 仓库安装 skill”，一般直接填仓库地址即可：

```text
https://github.com/wp746/aigc-film-production-master.git
```

如果它们支持“从 skill 入口文件识别”，就填：

```text
https://raw.githubusercontent.com/wp746/aigc-film-production-master/main/SKILL.md
```

如果它们支持“先导入仓库，再读取根目录 skill”，这个仓库本身已经是 skill 根目录，不需要再额外指定子路径。

如果仓库保持 private，需要确保对应智能体或平台有 GitHub 访问权限。

## 给朋友复用的万能调用卡

把下面这一段直接发给朋友。无论他用 Codex、OpenClaw、Hermes、Cursor、Claude、Gemini，还是任何支持读取 GitHub / 粘贴文件的 Agent，都可以按这个协议调用：

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

如果对方的 Agent 不能联网，就把 `SKILL.md` 和 [Universal Agent Adapter](references/universal-agent-adapter.md) 复制给它，再按任务补充必要 references。

## 怎么使用

### 1. 从一句创意生成 5 分钟 AIGC 短片

```text
请调用 $aigc-film-production-master。

创意：一个被裁员的中年男人发现自己能看见每个人人生剩余时间。
我想做成 5 分钟以内的创意短片。

请在后台完成创意强化、AIGC导演和生产交接，最终交付可复制的 Image2 + Seedance 双语提示词 Markdown 文件。
```

### 2. 审查现成剧本并改成 AIGC 可生产方案

```text
请调用 $aigc-film-production-master。

下面是我的现成剧本。
不要直接重写，先判断哪些地方有效、哪些地方俗套、哪些地方 AIGC 生产风险高。
然后在后台完成 AIGC 导演交接，并最终输出可进入生产的 Image2 + Seedance 双语提示词文件。
```

### 3. 60 集短剧项目

```text
请调用 $aigc-film-production-master。

我想做一个 60 集 AI 真人短剧。
题材：现实逆袭 + 悬疑反转。
先不要写全部提示词，先做长线故事引擎、角色圣经、分集结构和第一集生产块。
```

### 4. 90 分钟 AIGC 电影

```text
请调用 $aigc-film-production-master。

我想把这个故事发展成 90 分钟 AIGC 电影。
请先做 logline、主题、人物弧光、15 节拍、8 sequence outline，
再判断哪些段落适合先进入 AIGC 生产测试。
```

### 5. 已有角色图和剧本

```text
请调用 $aigc-film-production-master。

我已经有主角图、场景图和一版剧本。
请把已有资产作为最高优先级，不要重设角色。
后台先做 AIGC 生产交接，再直接生成最终 Image2 + Seedance 双语提示词文件。
```

## 本地项目骨架脚本

仓库内置一个轻量脚本，用于创建 AIGC 项目生产目录：

```bash
python3 scripts/create_project_skeleton.py "项目名" --root ./projects
```

生成结构包括：

- `00_brief`
- `00_sources`
- `00_script_breakdown`
- `01_story_bible`
- `01_style_bible`
- `01_asset_database`
- `02_assets`
- `03_aigc_director`
- `04_image2_storyboards`
- `05_seedance_prompts`
- `06_generations`
- `07_reviews`
- `08_repairs`
- `09_postproduction`
- `10_delivery`
- `11_versions`

其中 `01_asset_database` 会自动生成：

- `characters.csv`
- `character_states.csv`
- `scenes.csv`
- `scene_states.csv`
- `props.csv`
- `prop_states.csv`
- `shots.csv`
- `seedance_takes.csv`
- `reusable_assets.csv`
- `repair_log.csv`
- `source_provenance.csv`
- `version_log.csv`

## 版本记录

### v1.6.0 | 2026-05-19

将系统封装为更适合朋友和外部 Agent 复用的分发形态。

新增：

- `references/universal-agent-adapter.md`：定义 Native Skill、GitHub 仓库读取、纯复制粘贴三种复用方式。
- 万能调用卡：朋友可直接粘贴到任意支持 GitHub 或文件读取的 Agent 中。
- 外部 Agent 执行契约：要求它执行 skill，而不是只总结仓库；默认后台推理，最终交付下游双语提示词文件。

更新：

- `SKILL.md`：接入 universal agent adapter。
- `agents/openai.yaml`：更新为更明确的可分发描述。
- `audit_skill_contract.py`：把 universal adapter 纳入审计。

### v1.1.0 | 2026-05-17

补齐第一轮系统审查中发现的五个关键缺口：

1. 上游创意开发不能交给下游 SOP 单独承担  
   新增 `creative-development-orchestration.md`，明确 master 负责协调编剧 skill、类型片 playbook 和创意开发框架。

2. 长片级资产数据库不够硬  
   新增 `asset-database-ledger.md`，定义角色状态表、场景状态表、道具状态表、镜头台账、Seedance take 评分库、可复用资产库和返修日志。

3. 后期系统偏弱  
   扩展 `postproduction-delivery.md`，加入 EDL、ADR/voice cue sheet、music cue sheet、SRT、VFX overlay、LUT/color direction 和最终交付规格。

4. 合规 / 版权 / IP 风险不是主模块  
   新增 `compliance-rights-ip-gate.md`，覆盖品牌、名人、IP、参考片、平台、比赛、音乐、声音、肖像和安全风险。

5. 风格覆盖需要类型片包  
   新增 `genre-playbook-index.md`，覆盖悬疑、恐怖、黑色电影、儿童动画、文旅、科幻、赛博、国风、年代戏、纪录片、实验短片、音乐剧、喜剧等类型。

同时更新：

- `SKILL.md` 工作流路由
- `qa-risk-gates.md` 风险门禁
- `longform-series-film-control.md` 长片控制
- `create_project_skeleton.py`，新增 `01_asset_database` 和 10 个 CSV 台账模板

### v1.2.0 | 2026-05-17

根据当前实际项目方向，将默认重心从“长片也能覆盖”收紧为“短片 / 短剧 / 宣传广告的电影级闭环生产”。

新增：

- `shortform-filmgrade-pipeline.md`：短片、短剧、广告、TVC、MV、文旅、比赛片的默认电影级执行链路。
- `final-prompt-delivery-contract.md`：最终提示词交付协议，规定全流程任务不能停在交接包，必须产出可复制的 Image2 + Seedance 提示词 Markdown 文件。

更新：

- `SKILL.md` 默认工作流
- `downstream-image2-seedance-bridge.md`，新增端到端执行规则
- `qa-risk-gates.md`，新增最终提示词文件和短片电影级闭环检查

核心变化：

```text
计划 / 交接包不是终点。
用户要出图出视频时，最终必须给到可复制提示词文件。
```

### v1.3.0 | 2026-05-17

新增“后台反应 / 模块可见性 / 修改后回装”交互协议。

新增：

- `module-visibility-and-reinsertion.md`

核心规则：

- 默认不展示内部创意推演、导演判断、合规门禁、QA 过程。
- 默认最终交付是下游双语提示词 Markdown 文件。
- 用户点名要看某一模块时，只展示该模块。
- 用户修改模块后，把模块重新装回主链路，并只更新受影响的下游提示词。

这让系统既能保持后台的完整工业链路，又不会让用户被过程文档淹没。

### v1.4.0 | 2026-05-17

全局系统审计后的第二轮补强，补齐真实项目里容易被忽略的工业化缺口。

新增：

- `source-ingestion-normalization.md`：把一句话创意、剧本、brief、参考图、参考片、资产统一成 Source Packet。
- `brand-ad-brief-engine.md`：补齐宣传广告/TVC/文旅/产品片的品牌真相、受众、传播主张、CTA、声明风险。
- `retention-performance-gate.md`：补齐短视频平台的首帧、0-2秒、5秒理解、结尾记忆点和平台气质。
- `model-platform-adapter.md`：补齐不同图像/视频模型和平台限制的适配层。
- `privacy-provenance-governance.md`：补齐私人素材、客户素材、参考素材、生成资产的来源、授权和复用边界。
- `versioning-feedback-loop.md`：补齐用户修改模块后的版本管理、影响范围判断和局部回装。
- `scripts/audit_skill_contract.py`：新增本地审计脚本，检查关键引用文件是否接入 SKILL.md 和 README.md。

核心纠正：

```text
电影级短片/广告不只需要好故事和好提示词，
还需要来源统一、品牌说服、留存节奏、平台适配、素材治理和版本回滚。
```

### v1.5.0 | 2026-05-19

将类型片能力从“索引级”升级为“深度执行级”。

新增五个高优先级类型片深度 playbook：

- `references/genre-playbooks/suspense-thriller.md`
- `references/genre-playbooks/cultural-tourism.md`
- `references/genre-playbooks/commercial-tvc.md`
- `references/genre-playbooks/short-drama.md`
- `references/genre-playbooks/black-humor.md`

每个 playbook 都细化到：

- 观众承诺
- 故事结构动作
- 镜头语言
- 节奏
- 声音
- AIGC 常见失败
- 下游 Image2 / Seedance 提示词策略
- CN/EN 风格锁
- 避免事项

同时更新：

- `genre-playbook-index.md`：新增深度 playbook 路由表。
- `SKILL.md`：明确悬疑、文旅、广告/TVC、短剧、黑色幽默要加载独立 playbook。
- `audit_skill_contract.py`：新增深度 playbook 接入审计。

### v1.0.0 | 2026-05-17

初始工业级总控版本。

已包含：

- 入口识别与路由
- 上游编剧与剧本诊断
- AIGC 导演可生产化系统
- AIGC 生产交接协议
- Image2 + Seedance 下游桥接规则
- 长片 / 系列控制
- 后期交付规划
- QA 与风险门禁
- 项目骨架创建脚本

## 适用边界

适合：

- AIGC 短片
- AI 真人短剧
- AI 漫剧
- AI 广告 / TVC
- AI MV
- 文旅片
- 比赛片
- 宣传片
- 电影级质感短视频
- 60 集短剧开发（显式请求时）
- 90 分钟电影开发（显式请求时）
- 从现成剧本进入 Image2 + Seedance 工业生产

不建议单独用它替代：

- 专门的 Image2/Seedance prompt 生产：优先交给 `image2-seedance-control`
- 单纯资产板设计：可用 `aigc-asset-board-skill`
- 已经完整锁定的下游小任务：可直接使用对应下游 skill

## 未来计划

- 将类型片 playbook 从索引扩展为每个类型独立文件。
- 增加可视化资产数据库模板。
- 增加自动生成 EDL / SRT / cue sheet 的脚本。
- 增加与更多视频模型的下游桥接规则。
- 增加多智能体协作版：编剧、导演、美术、分镜、Seedance、后期、质检。
