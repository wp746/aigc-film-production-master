#!/usr/bin/env python3
"""Create an AIGC film production folder skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


FOLDERS = [
    "00_brief",
    "00_script_breakdown",
    "01_story_bible",
    "01_style_bible",
    "01_asset_database",
    "02_assets",
    "03_aigc_director",
    "04_image2_storyboards",
    "05_seedance_prompts",
    "06_generations",
    "07_reviews",
    "08_repairs",
    "09_postproduction",
    "10_delivery",
]


def slugify(value: str) -> str:
    safe = []
    for ch in value.strip().lower():
        if ch.isalnum():
            safe.append(ch)
        elif ch in {" ", "-", "_"}:
            safe.append("_")
    slug = "".join(safe).strip("_")
    return slug or "aigc_project"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Project title")
    parser.add_argument("--root", default=".", help="Output root directory")
    args = parser.parse_args()

    project_dir = Path(args.root).expanduser().resolve() / slugify(args.title)
    project_dir.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        (project_dir / folder).mkdir(exist_ok=True)

    index = project_dir / "PROJECT_INDEX.md"
    if not index.exists():
        index.write_text(
            f"# {args.title}\n\n"
            "## Production Units\n\n"
            "| Unit | Status | Owner | Notes |\n"
            "|---|---|---|---|\n"
            "| Story Bible | TODO | | |\n"
            "| AIGC Director Package | TODO | | |\n"
            "| Image2/Seedance Prompts | TODO | | |\n"
            "| Postproduction | TODO | | |\n",
            encoding="utf-8",
        )

    database_dir = project_dir / "01_asset_database"
    templates = {
        "characters.csv": "char_id,name,identity_source,face_anchors,wardrobe_base,voice_rhythm,gesture_habit,version,status\n",
        "character_states.csv": "char_id,state_unit,wardrobe_state,body_state,emotion_state,forbidden_drift,version,status\n",
        "scenes.csv": "scene_id,location_name,geography_source,fixed_anchors,time_weather,camera_safe_zones,version,status\n",
        "scene_states.csv": "scene_id,state_unit,damage_or_change,time_weather,light_state,forbidden_drift,version,status\n",
        "props.csv": "prop_id,name,asset_source,shape_material,holder,hand_logic,exact_text_mode,version,status\n",
        "prop_states.csv": "prop_id,state_unit,state_change,holder,hand_logic,forbidden_drift,version,status\n",
        "shots.csv": "shot_id,segment_id,story_beat,function,assets_used,in_state,out_state,prompt_version,storyboard_version,status\n",
        "seedance_takes.csv": "take_id,prompt_version,reference_stack,score,verdict,hard_fail,best_frame,usable_range,defects,next_action\n",
        "reusable_assets.csv": "asset_id,type,source,version,status,reuse_rule,notes\n",
        "repair_log.csv": "repair_id,take_id,defect,root_cause,changed_variable,expected_fix,result,next_action\n",
    }
    for name, header in templates.items():
        path = database_dir / name
        if not path.exists():
            path.write_text(header, encoding="utf-8")

    print(project_dir)


if __name__ == "__main__":
    main()
