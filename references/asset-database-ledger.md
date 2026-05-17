# Asset Database And Production Ledger

Use this for long shorts, 12/24/60-episode projects, feature films, or any project with recurring assets and generated takes.

## Rule

Longform AIGC production cannot rely on memory. Every durable element must have an ID, version, source, status, and owner.

## Database Files

Recommended files:

```text
01_asset_database/
  characters.csv
  character_states.csv
  scenes.csv
  scene_states.csv
  props.csv
  prop_states.csv
  style_bible.csv
  shots.csv
  seedance_takes.csv
  reusable_assets.csv
  repair_log.csv
```

## Character State Table

| Field | Meaning |
|---|---|
| `char_id` | `CHAR_A` |
| `name` | story name |
| `identity_source` | original image / asset board / text design |
| `face_anchors` | face, age, hair, body anchors |
| `wardrobe_base` | base costume |
| `voice_rhythm` | speaking rhythm and tone |
| `gesture_habit` | repeated physical habit |
| `state_unit` | episode / scene / segment |
| `wardrobe_state` | clean, wet, damaged, changed |
| `body_state` | injury, fatigue, dirt, makeup |
| `emotion_state` | current emotional state |
| `forbidden_drift` | what must not change |
| `version` | `v001` |
| `status` | TODO / LOCKED / NEEDS_REPAIR / RETIRED |

## Scene State Table

| Field | Meaning |
|---|---|
| `scene_id` | `SCENE_01` |
| `location_name` | office lobby, street, apartment |
| `geography_source` | scene board / floor plan / original photo |
| `fixed_anchors` | doors, windows, desks, roads, light sources |
| `time_weather` | day/night/weather |
| `camera_safe_zones` | stable camera areas |
| `state_unit` | episode / scene / segment |
| `damage_or_change` | broken glass, rain, crowd, moved object |
| `forbidden_drift` | layout, light, weather, scale |
| `version` | `v001` |
| `status` | TODO / LOCKED / NEEDS_REPAIR / RETIRED |

## Prop State Table

| Field | Meaning |
|---|---|
| `prop_id` | `PROP_PHONE` |
| `name` | phone, letter, box, ring |
| `asset_source` | prop board / original photo |
| `shape_material` | shape, color, material, wear |
| `holder` | who holds it |
| `hand_logic` | left hand / right hand / table position |
| `state_unit` | episode / scene / segment |
| `state_change` | cracked, opened, wet, missing |
| `exact_text_mode` | none / text plate / post |
| `forbidden_drift` | shape, color, scale, logo, text |
| `version` | `v001` |
| `status` | TODO / LOCKED / NEEDS_REPAIR / RETIRED |

## Shot Ledger

| Field | Meaning |
|---|---|
| `shot_id` | `EP01_SC02_SEG03_SH01` |
| `segment_id` | local Seedance segment |
| `story_beat` | source beat |
| `function` | dialogue / action / suspense / transition / product / atmosphere |
| `assets_used` | CHAR / SCENE / PROP / STYLE refs |
| `in_state` | start state |
| `out_state` | end state |
| `prompt_version` | prompt version |
| `storyboard_version` | board version |
| `status` | PLANNED / PROMPTED / GENERATED / PASSED / REPAIR |

## Seedance Take Score Library

| Field | Meaning |
|---|---|
| `take_id` | `EP01_SC02_SEG03_T02` |
| `prompt_version` | prompt used |
| `reference_stack` | uploaded refs and order |
| `score` | 0-100 |
| `verdict` | PASS / CONDITIONAL / REPAIR / FAIL |
| `hard_fail` | yes/no and reason |
| `best_frame` | frame path or description |
| `usable_range` | time range usable in edit |
| `defects` | identity, scene, prop, motion, camera, emotion, seam |
| `next_action` | keep, trim, repair, regenerate, rebuild |

## Reusable Asset Library

Track what can be reused:

- locked character board
- locked scene board
- locked prop board
- safe style look image
- best previous final frame
- approved VFX overlay
- approved music/sound motif
- approved subtitle style

## Gate

Do not call a series or feature industrialized unless:

- the database exists
- current production block assets are locked
- generated takes are scored
- state changes are written back to the ledger
- failed takes are preserved for diagnosis
