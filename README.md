# AIGC Film Production Master Skill

> v1.0.0 | 2026-05-17

一个面向 AIGC 影视创作者的工业级全链路总控 skill。

它不是单纯帮你写剧本，也不是直接生成几条 Seedance 提示词，而是把一句创意、现成剧本、参考片、角色图、场景图或长篇项目，整理成一套可以进入工业化生产的 AIGC 影视流程：

```text
创意 / 剧本 / 参考片 / 资产
-> 上游编剧与结构强化
-> AIGC 导演可生产化
-> Image2 + Seedance 生产交接包
-> 下游资产板 / 故事板 / Seedance 2.0 提示词
-> 出片验收 / 返修 / 后期交付
```

它适合 AIGC 创意短片、AI 真人短剧、AI 漫剧、广告片、TVC、文旅片、MV、比赛片、60 集短剧、长篇系列和 90 分钟电影项目的前期到生产总控。

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
- [上游编剧与导演系统](references/upstream-screenwriting-director.md)
- [AIGC 导演系统](references/aigc-director-system.md)
- [AIGC 生产交接协议](references/aigc-production-handoff-contract.md)
- [Image2 + Seedance 下游桥接](references/downstream-image2-seedance-bridge.md)
- [长片 / 系列控制](references/longform-series-film-control.md)
- [后期交付](references/postproduction-delivery.md)
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

## 核心定位

`aigc-film-production-master` 是一个 **上游 + 中控 + 路由型 skill**。

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

## 标准工作流

默认工业链路是：

```text
Intake
-> Story / Script Diagnosis
-> Screenwriting Enhancement
-> AIGC Director Package
-> AIGC Production Handoff
-> Image2 + Seedance Prompt Factory
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
    upstream-screenwriting-director.md
    aigc-director-system.md
    aigc-production-handoff-contract.md
    downstream-image2-seedance-bridge.md
    longform-series-film-control.md
    postproduction-delivery.md
    qa-risk-gates.md
  scripts/
    create_project_skeleton.py
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

## 怎么使用

### 1. 从一句创意生成 5 分钟 AIGC 短片

```text
请调用 $aigc-film-production-master。

创意：一个被裁员的中年男人发现自己能看见每个人人生剩余时间。
我想做成 5 分钟以内的创意短片。

请先强化故事和后劲，再输出 AIGC 导演方案和 Image2/Seedance 生产交接包。
```

### 2. 审查现成剧本并改成 AIGC 可生产方案

```text
请调用 $aigc-film-production-master。

下面是我的现成剧本。
不要直接重写，先判断哪些地方有效、哪些地方俗套、哪些地方 AIGC 生产风险高。
然后输出一版可进入 Image2 + Seedance SOP 的 AIGC 导演交接包。
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
先做 AIGC 生产交接包，再交给 image2-seedance-control 做下游提示词。
```

## 本地项目骨架脚本

仓库内置一个轻量脚本，用于创建 AIGC 项目生产目录：

```bash
python3 scripts/create_project_skeleton.py "项目名" --root ./projects
```

生成结构包括：

- `00_brief`
- `00_script_breakdown`
- `01_story_bible`
- `01_style_bible`
- `02_assets`
- `03_aigc_director`
- `04_image2_storyboards`
- `05_seedance_prompts`
- `06_generations`
- `07_reviews`
- `08_repairs`
- `09_postproduction`
- `10_delivery`

## 版本记录

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
- 60 集短剧
- 90 分钟电影开发
- 从现成剧本进入 Image2 + Seedance 工业生产

不建议单独用它替代：

- 专门的 Image2/Seedance prompt 生产：优先交给 `image2-seedance-control`
- 单纯资产板设计：可用 `aigc-asset-board-skill`
- 已经完整锁定的下游小任务：可直接使用对应下游 skill

## 未来计划

- 增加类型片专属 playbook：悬疑、恐怖、喜剧、科幻、国风、文旅、儿童动画、纪录片。
- 增加长片级资产数据库模板。
- 增加后期 EDL / SRT / 音乐 cue sheet 模板。
- 增加与更多视频模型的下游桥接规则。
- 增加多智能体协作版：编剧、导演、美术、分镜、Seedance、后期、质检。
