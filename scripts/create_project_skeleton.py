#!/usr/bin/env python3
"""Create an AIGC film production folder skeleton."""

from __future__ import annotations

import argparse
from pathlib import Path


FOLDERS = [
    "00_sources",
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
    "11_versions",
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

FOLDER_READMES = {
    "00_sources": (
        "# 00 Sources\n\n"
        "Place all original source materials here, including:\n"
        "- Initial ideas or one-sentence concepts\n"
        "- Client briefs and brand guides\n"
        "- Reference images or video links\n\n"
        "Refer to `references/source-ingestion-normalization.md` for guidelines on source ingestion.\n"
    ),
    "01_story_bible": (
        "# 01 Story Bible\n\n"
        "Store story/project bibles, character designs, and worldbuilding documents here.\n\n"
        "Refer to:\n"
        "- `references/creative-development-orchestration.md`\n"
        "- `references/upstream-screenwriting-director.md`\n"
    ),
    "01_asset_database": (
        "# 01 Asset Database\n\n"
        "This folder contains the CSV tracking sheets for production continuity:\n"
        "- `characters.csv` / `character_states.csv`\n"
        "- `scenes.csv` / `scene_states.csv`\n"
        "- `props.csv` / `prop_states.csv`\n"
        "- `shots.csv` / `seedance_takes.csv`\n\n"
        "Refer to `references/asset-database-ledger.md` for schema details.\n"
    ),
    "03_aigc_director": (
        "# 03 AIGC Director\n\n"
        "Store AIGC Director Feasibility Plans, Segment Plans, and Handoff Packages here.\n\n"
        "Refer to:\n"
        "- `references/aigc-director-system.md`\n"
        "- `references/aigc-production-handoff-contract.md`\n"
    ),
    "04_image2_storyboards": (
        "# 04 Image2 Storyboards\n\n"
        "Store Image2 asset board prompts and storyboard prompts here.\n\n"
        "Refer to:\n"
        "- `references/downstream-image2-seedance-bridge.md`\n"
        "- `references/image2-seedance-v192-downstream-contract.md`\n"
    ),
    "05_seedance_prompts": (
        "# 05 Seedance Prompts\n\n"
        "Store finalized, copy-ready Seedance 2.0 text prompts here.\n\n"
        "Refer to:\n"
        "- `references/final-prompt-delivery-contract.md`\n"
        "- `references/image2-seedance-v192-downstream-contract.md`\n"
    ),
    "09_postproduction": (
        "# 09 Postproduction\n\n"
        "Store post-production specifications here, including:\n"
        "- EDL (Edit Decision Lists)\n"
        "- Voiceover / ADR cue sheets\n"
        "- Music and sound design cue sheets\n"
        "- SRT subtitles and VFX overlays\n\n"
        "Refer to `references/postproduction-delivery.md`.\n"
    ),
    "10_delivery": (
        "# 10 Delivery\n\n"
        "Store final master video files, platform-specific exports, and release approvals here.\n\n"
        "Refer to `references/postproduction-delivery.md`.\n"
    ),
}


def write_folder_readme(project_dir: Path, folder: str) -> None:
    if folder in FOLDER_READMES:
        f_dir = project_dir / folder
        f_dir.mkdir(exist_ok=True)
        readme_path = f_dir / "README.md"
        if not readme_path.exists():
            readme_path.write_text(FOLDER_READMES[folder], encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("title", help="Project title")
    parser.add_argument("--root", default=".", help="Output root directory")
    args = parser.parse_args()

    project_dir = Path(args.root).expanduser().resolve() / slugify(args.title)
    project_dir.mkdir(parents=True, exist_ok=True)

    for folder in FOLDERS:
        f_dir = project_dir / folder
        f_dir.mkdir(exist_ok=True)
        write_folder_readme(project_dir, folder)

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
        "source_provenance.csv": "source_id,type,owner,permission,reuse_boundary,public_private,notes\n",
        "version_log.csv": "version_id,module,changed_by,change_summary,affected_prompts,preserved_modules,date,notes\n",
    }
    for name, header in templates.items():
        path = database_dir / name
        if not path.exists():
            path.write_text(header, encoding="utf-8")

    print(project_dir)


if __name__ == "__main__":
    main()
