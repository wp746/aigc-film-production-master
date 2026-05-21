# AIGC Audio-Visual Grammar Bible (AIGC影视视听语言圣经)

This definitive specification establishes the industrial-grade audio-visual grammar and strict operational contracts for AIGC-enabled filmmaking (e.g. Image2 + Seedance 2.0 pipeline). Any collaborative agent or system operator must execute prompt engineering, scene blocking, asset tracking, and post-production integration in absolute alignment with these rules to eliminate style/character drift, preserve cinematic rhythm, and respect model capability ceilings.

---

## 1. Cinematography & Lens Grammar (运镜与切镜圣经)

Vague words like "cinematic," "movie style," or "epic camera angle" are forbidden. Every shot must define its project camera package, lens family, exact focal length, and motivated movement vector.

### 1.1 Camera and Lens Lock
- **A-Cam/Primary Package**: `ARRI Alexa 35 / Cooke Panchro/i Classic Prime` (delivers organic cinematic warmth, smooth roll-off, and painterly bokeh).
- **B-Cam/High-Contrast Package**: `RED V-RAPTOR / Panavision Primo` (delivers hyper-crisp, high-fidelity modern textures, perfect for high-speed motion or brand TVC).
- **Anamorphic Lens Lock**: `Sony Venice / Panavision Auto Panatar Anamorphic` (for film-grade wide narratives, 2.39:1 aspect ratio, horizontal blue lens flares, and oval bokeh).

### 1.2 Motivated Motion Formulas
Every camera movement must have a narrative reason. Forbid random handheld jitter and chaotic rotations.
- **Narrative Reveal (Slow Push-In)**: `A slow motivated slow dolly-in, 50mm, camera gradually pushing in on the protagonist's eyes, background compression, shallow depth of field.`
- **Dread/Suspense (Locked Static)**: `A locked-off tripod shot, 35mm wide angle, stable frame, capturing the eerie stillness of the environment, no camera movement.`
- **Action/Pursuit (Axis-Locked Pan)**: `A motivated whip pan, tracking motion parallel to the 180-degree axis, keeping character position left-to-right consistent.`

### 1.3 Shot Seams & Cutting Rules
- **One Segment, Dual Shots Max**: In a single 5-15s Seedance timeline, never exceed **2 shots** or **8 storyboard panels** to prevent semantic collapse.
- **Seam Matches**: If segment N ends in a medium close-up, segment N+1 must start in the exact same focal distance or transition using a clean visual match-cut (e.g. tracking eyes, matching movement velocity).
- **The Neutral-Axis Bridge**: Crossing the 180-degree line is strictly forbidden unless bridged by an exact neutral-axis shot (directly on the line of action) to maintain audience spatial legibility.

---

## 2. Composition & Lighting Grammar (构图与光影圣经)

AIGC models easily default to generic flat lighting or overly saturated game-engine graphics. This section binds all visual assets to motivative, painterly cinematic lighting.

### 2.1 motivated Lighting Rules
- **Chiaroscuro (明暗对比)**: Define a single clear key light source and contrast it with deep shadow zones (e.g. single candle, neon sign, desk lamp).
- **Volumetric Light**: Enforce realistic air density parameters: `volumetric haze, dust particles dancing in the light beam, soft light scattering.`
- **Color Temperature Lock**: Avoid random rainbows. Enforce a strict dual-tone palette: `restrained teal ambient night light contrasted with a warm orange key light from a single streetlamp, 3200k key / 5600k fill.`

### 2.2 Digital storyboard Board Substrate
Every Image2 storyboard layout must use the board-system lock to keep dimensions and aspect ratios stable:
- **Aspect Ratio Lock**: Specify aspect ratio in prompts: `2.39:1 cinemascope aspect ratio.`
- **Matte Warm-Gray Substrate**: Define the board background to prevent AI from adding mixed textures or kraft paper noise: `rendered on a clean, matte warm-gray production board substrate, minimalist presentation.`
- **Visible Frame Titles**: Use strict panel indexes: `S01 panel / S02 panel` corresponding to the timeline segments.

---

## 3. Character & Scene Continuity Preservation (角色与场景一致性圣经)

Consistency is the ultimate dividing line between amateur prompts and industrial-grade video production. We solve this by splitting asset definition from narrative actions and applying strict database keys.

### 3.1 Character Consistency Protocols (`CHAR_*`)
- **Visual Identity Locks**: Never redefine a character's face in the storyboard. Lock character anchors in `characters.csv` and refer to them:
  - Facial features: `worn eyes, sharp jawline, high cheekbones, asymmetrical brow.`
  - Fixed wardrobe: `signature yellow worn rainjacket, grey wool trenchcoat, never changing wardrobe.`
- **No Face Redesign in Storyboards**: Storyboards must treat characters as faceless silhouettes or outline blocks: `CHAR_HERO is a faceless grey outline, focusing purely on body language and physical blocking, preserving face reference.`

### 3.2 Spatial Geography & Scene Locks (`SCENE_*`)
- **Fixed Scene Anchors**: Scenes must establish unchanging physical landmarks to anchor the spatial math: `SCENE_ALLEY is locked with a prominent flashing red neon sign on the left wall and wet asphalt pavement reflecting the neon.`
- **Locked Axis Safe Zones**: Define where the camera can and cannot look: `Camera is locked within the 180-degree safe zone, viewing SCENE_ALLEY from a fixed 45-degree angle, background architecture remains stable.`

### 3.3 Prop Consistency & Hand Logic (`PROP_*`)
- **Prop Identity Code**: Lock crucial plot items: `PROP_CLOCK (wooden grandfather clock with three counter-clockwise hands).`
- **Hand Logic Guard**: Forbid distorted hands or overlapping fingers: `CHAR_HERO's hand is clean and anatomically correct, holding PROP_CLOCK by the wooden frame, no finger glitches, no distorted joints.`

---

## 4. Pacing, Sound Cues, VFX & Dialogue (台词、音效、特效与后期圣经)

Industrial pipelines do not expect AIGC video models to render high-fidelity text or lip-sync complex sentences out of the box. We split responsibilities between Seedance rendering and Post-Production.

### 4.1 Dialogue & Voice Lock (`VOICE_LOCK`)
- **Speech-Rate and Pause Cues**: Dialogue must translate to pacing and physical breathing in the prompt:
  ```text
  VOICE_LOCK: Lin (45yo male, low gravelly voice, slow breathy rhythm, pauses before key words).
  Performance beat: Lin hesitates, takes a sharp breath, eyes darting down, lips parting slightly, spoken line: “...太晚了。”
  ```
- **Lip-Sync Safe Prompts**: Keep jaw movement natural and simple. Forbid rapid mouth shapes that trigger model artifacting: `subtle lip movement, slow deliberate speech rhythm, no exaggerated jaw distortion.`

### 4.2 Integrated Sound Design Cues
Seedance prompts must write sound cues directly into the text code blocks to guide downstream sound effects (SFX) and ambient scoring:
- `Ambient Room Tone`: `heavy rain pouring outside, distant low rumbling thunder, room tone buzz.`
- `Foley Indicators`: `faint mechanical clicking of clock gears, footsteps splashing on wet pavement, deep breath.`

### 4.3 Visual Effects & Particle Separation (`VFX_*`)
- **Model Feasibility Check**: Heavy physics simulations (such as complex explosions, shattering glass, or swirling water vortexes) must be simplified or offloaded to Post-production overlay.
- **AIGC Feasible VFX**: Focus on simple particle paths: `subtle rising dust motes, thin drifting smoke trails, falling raindrops reflecting key light, no chaotic simulation.`

---

## 5. Model Cap & Complexity Budget Rules (模型上限与复杂度圣经)

Every Seedance prompt must specify a `SEGMENT_BUDGET` to balance elements and keep render success rates above 95%.

### 5.1 The Segment Budget
Before drafting a Seedance block, compute:
- **Maximum Named Characters**: 2 per segment.
- **Maximum Background Extras**: 5, locked with counts (`exactly 3 background extra figures, varied hairlines, no cloned faces`).
- **Maximum Active Physics**: 1 dynamic force (e.g. only rain, or only wind).

### 5.2 Clean Frame Rule
To prevent AI models from generating random watermark noise, caption gibberish, or text overlays, every prompt must enforce the Clean Frame Lock:
```text
不要字幕，无字幕，no subtitles, no captions, clean frame, no on-screen text, no watermarks, no captions.
```

---

## 6. Pipeline Handoff & Generation Scorecard (管线交接与评分机制)

Every completed project prompt file must include a **Downstream Acceptance Scorecard** for the operator to evaluate the rendered takes:

| Metric | Target | Evaluation Rule |
|---|---|---|
| **Identity Drift** | <5% | Do character features, wardrobe, or scene landmarks vary across segments? |
| **Linter Warnings** | 0 Critical | Does the final prompt contain timecodes ending after 0:15 or go over 5000 chars? |
| **Visual Pacing** | Cinematic | Do camera speeds match the dramatic tension of the screenplay? |
| **Clean Frame** | Pass | Is the footage free of random text, watermarks, or burned-in subtitles? |

This Holy Bible is the absolute operational law of AIGC Film Production Master. All agent reasoning and text generation must align with these parameters.
