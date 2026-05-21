#!/usr/bin/env python3
"""Multi-Agent Collaborative Simulator for AIGC Film Production.

Demonstrates the 'chemical reaction' and collaborative handoffs between
the 6 specialized agents in the system.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

# ANSI Escape Colors
C_RED = "\033[91m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_MAGENTA = "\033[95m"
C_CYAN = "\033[96m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"


def print_agent_log(agent_name: str, color: str, message: str) -> None:
    print(f"{color}{C_BOLD}[{agent_name}]{C_RESET} {color}{message}{C_RESET}")
    time.sleep(0.8)  # Dramatic pause to simulate thinking & handoff


def main() -> int:
    parser = argparse.ArgumentParser(description="Simulate multi-agent AIGC production.")
    parser.add_argument("idea", help="The raw creative idea or title")
    parser.add_argument("--root", default="./projects", help="Output root directory")
    args = parser.parse_args()

    title = args.idea
    root_dir = Path(args.root).resolve()

    print(f"\n{C_BOLD}=== AIGC FILM PRODUCTION MULTI-AGENT SIMULATOR ==={C_RESET}")
    print(f"Project Title: '{title}'\n")

    # -------------------------------------------------------------
    # PHASE 0: 00 Master Producer (Intake & Routing)
    # -------------------------------------------------------------
    print_agent_log(
        "00 Master Producer",
        C_CYAN,
        "Ingested raw creative concept... Normalizing to Source Packet.",
    )
    slug = "".join([c.lower() if c.isalnum() else "_" for c in title]).strip("_")
    slug = slug or "aigc_project"
    project_dir = root_dir / slug

    print_agent_log(
        "00 Master Producer",
        C_CYAN,
        f"Initialized project skeleton workspace at: {project_dir}",
    )
    project_dir.mkdir(parents=True, exist_ok=True)

    # Invoke create_project_skeleton logic
    from create_project_skeleton import FOLDERS, slugify
    for folder in FOLDERS:
        (project_dir / folder).mkdir(exist_ok=True)

    # Write PROJECT_INDEX.md
    (project_dir / "PROJECT_INDEX.md").write_text(
        f"# {title}\n\nMulti-Agent Collaborative Production Workspace.\n",
        encoding="utf-8",
    )

    print_agent_log(
        "00 Master Producer",
        C_CYAN,
        "Identified pipeline type: SHORTFORM_FILMGRADE. Routing brief to Upstream Writer...",
    )

    # -------------------------------------------------------------
    # PHASE 1: 01 Upstream Writer (Creative & Script)
    # -------------------------------------------------------------
    print_agent_log(
        "01 Upstream Writer",
        C_YELLOW,
        "Received brief. Constructing story engine and character archetypes...",
    )
    print_agent_log(
        "01 Upstream Writer",
        C_YELLOW,
        "Refining themes... Actively checking clichés and designing the climax twist.",
    )
    print_agent_log(
        "01 Upstream Writer",
        C_YELLOW,
        "Locked narrative beats (Save the Cat format) and screenplay dialogue.",
    )

    script_md = (
        f"# Screenplay: {title}\n\n"
        "## Story Engine\n"
        "- **Protagonist**: Delivery Man (外卖员 CHAR_HERO), carries regret.\n"
        "- **Stakes**: Time is ticking; addresses lead to past regrets.\n\n"
        "## Scene Outline\n"
        "### SCENE 1 - Alley - Night (Rainy)\n"
        "Delivery Man rides through rain. Red neon light glimmers in puddles.\n"
    )
    script_path = project_dir / "01_story_bible" / "screenplay.md"
    script_path.write_text(script_md, encoding="utf-8")
    print_agent_log(
        "01 Upstream Writer",
        C_YELLOW,
        f"Saved locked screenplay to: {script_path.name}. Handing off to AIGC Director...",
    )

    # -------------------------------------------------------------
    # PHASE 2: 02 AIGC Director (Visuals & Feasibility)
    # -------------------------------------------------------------
    print_agent_log(
        "02 AIGC Director",
        C_MAGENTA,
        "Received script. Commencing scene blocking and screen orientation constraints...",
    )
    print_agent_log(
        "02 AIGC Director",
        C_MAGENTA,
        "Analyzing AIGC Feasibility. Mapping production duties (Asset / Storyboard / Seedance / Post).",
    )
    print_agent_log(
        "02 AIGC Director",
        C_MAGENTA,
        "Enforcing 180-degree axis lock. Set local timecode anchors (0:00-0:15) per segment.",
    )

    director_plan = (
        f"# Director Feasibility Plan: {title}\n\n"
        "## Feasibility Analysis\n"
        "- **Segment 1 (SEG_01)**: 0:00-0:05. [DIRECT_GENERATABLE] Rain, neon, driving.\n"
        "- **Segment 2 (SEG_02)**: 0:05-0:15. [ASSET_REQUIRED] Character micro-expression.\n"
    )
    (project_dir / "03_aigc_director" / "director_plan.md").write_text(
        director_plan, encoding="utf-8"
    )
    print_agent_log(
        "02 AIGC Director",
        C_MAGENTA,
        "Assigned Visual Look Lock (Rainy Cinematic Realism). Handing off to Continuity Manager...",
    )

    # -------------------------------------------------------------
    # PHASE 3: 03 Asset Continuity Manager (Ledgers & States)
    # -------------------------------------------------------------
    print_agent_log(
        "03 Asset Continuity Manager",
        C_GREEN,
        "Received Director visuals. Registering production database accounts...",
    )

    # Populate CSV ledger templates
    database_dir = project_dir / "01_asset_database"
    database_dir.mkdir(exist_ok=True)

    char_csv = (
        "char_id,name,identity_source,face_anchors,wardrobe_base,voice_rhythm,gesture_habit,version,status\n"
        "CHAR_HERO,外卖员,00_sources/hero_face.jpg,worn eyes,yellow rainjacket,slow,hand shake,v001,LOCKED\n"
    )
    (database_dir / "characters.csv").write_text(char_csv, encoding="utf-8")

    scene_csv = (
        "scene_id,location_name,geography_source,fixed_anchors,time_weather,camera_safe_zones,version,status\n"
        "SCENE_ALLEY,雨夜小巷,00_sources/alley_look.jpg,red neon sign,rain dusk,locked axis,v001,LOCKED\n"
    )
    (database_dir / "scenes.csv").write_text(scene_csv, encoding="utf-8")

    print_agent_log(
        "03 Asset Continuity Manager",
        C_GREEN,
        "Registered CHAR_HERO (worn eyes, yellow rainjacket) and SCENE_ALLEY in database.",
    )
    print_agent_log(
        "03 Asset Continuity Manager",
        C_GREEN,
        "Visual bibles locked! Verification complete. Sending to Prompt Factory...",
    )

    # -------------------------------------------------------------
    # PHASE 4: 04 Prompt Factory (Prompt Engineering)
    # -------------------------------------------------------------
    print_agent_log(
        "04 Prompt Factory",
        C_BLUE,
        "Received continuity assets and visual directives. Crafting prompt packages...",
    )
    print_agent_log(
        "04 Prompt Factory",
        C_BLUE,
        "Drafting CN/EN Image2 Asset board prompts and Seedance 2.0 timeline block...",
    )

    # Write final Markdown package complying with prompt_lint rules
    final_prompt_content = f"""# {title} - Image2 + Seedance Production Prompts

## Asset Design Prompts
- **CHAR_HERO** (CN): 黄色外卖雨衣，带着疲惫眼神的中年外卖员，写实电影。
- **CHAR_HERO** (EN): A cinematic portrait of a middle-aged delivery man in a yellow rainjacket, tired eyes, cinematic realism.
- **SCENE_ALLEY** (CN): 雨夜小巷，闪烁着红色霓虹招牌。
- **SCENE_ALLEY** (EN): A narrow wet alley at night, rain pouring, glimmers of a red neon sign.

## Storyboard Prompts + Seedance Prompts

### Segment 1 Seedance Prompt
```text
0:00 - 0:05: [S01] A delivery man CHAR_HERO rides through SCENE_ALLEY.
镜头推近，雨水拍打在他的头盔上。
禁止任何动作漂移，画面保持绝对稳定。
不要字幕，无字幕，no subtitles, no captions, clean frame.
影像风格锁：STYLE_BIBLE, STYLE_LOCK.
```

### Segment 2 Seedance Prompt
```text
0:00 - 0:10: [S02] CHAR_HERO stares at a phone screen showing a map location.
特写镜头，眼神流露出难以置信的震惊。
禁止手部扭曲变形。
不要字幕，无字幕，no subtitles, no captions, clean frame.
影像风格锁：STYLE_BIBLE, STYLE_LOCK.
```
"""
    prompt_path = project_dir / "05_seedance_prompts" / f"{slug}_prompts_v001.md"
    prompt_path.write_text(final_prompt_content, encoding="utf-8")

    print_agent_log(
        "04 Prompt Factory",
        C_BLUE,
        f"Bilingual prompts assembled and saved to: {prompt_path.name}. Handing off to QA Gatekeeper...",
    )

    # -------------------------------------------------------------
    # PHASE 5: 05 QA Risk Gatekeeper (Quality and Linter Check)
    # -------------------------------------------------------------
    print_agent_log(
        "05 QA Risk Gatekeeper",
        C_RED,
        "Received finalized prompt Markdown file. Running Quality Gates and Linter...",
    )

    # Programmatically invoke prompt_lint functions to demonstrate integration
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from prompt_lint import lint_file

    results = lint_file(prompt_path)
    errors = [
        r
        for r in results
        if "exceeds" in r
        or "missing" in r
        or "ends after" in r
        or "no fenced" in r
    ]
    warnings = [r for r in results if r not in errors]

    print_agent_log(
        "05 QA Risk Gatekeeper",
        C_RED,
        f"Linter complete. Found {len(errors)} critical errors, {len(warnings)} warnings.",
    )

    if errors:
        print_agent_log(
            "05 QA Risk Gatekeeper",
            C_RED,
            "AUDIT VERDICT: FIX. Critical lint failures must be corrected.",
        )
        for err in errors:
            print(f"  {C_RED}- [ERROR] {err}{C_RESET}")
        return 1
    else:
        print_agent_log(
            "05 QA Risk Gatekeeper",
            C_GREEN,
            "AUDIT VERDICT: PASS. Enforcing platform compliance checks passed.",
        )
        print_agent_log(
            "05 QA Risk Gatekeeper",
            C_GREEN,
            "Production Green Light granted. Master Producer approved final handoff.",
        )

    # -------------------------------------------------------------
    # INTEGRATION & FINISH
    # -------------------------------------------------------------
    # Write a copy to outputs/ for direct access
    outputs_dir = Path("outputs")
    outputs_dir.mkdir(exist_ok=True)
    out_file = outputs_dir / f"{slug}-image2-seedance-prompts-v001.md"
    out_file.write_text(final_prompt_content, encoding="utf-8")

    print(f"\n{C_GREEN}{C_BOLD}✔ SIMULATION COMPLETED SUCCESSFULLY!{C_RESET}")
    print(f"Outputs written to project skeleton at: {C_BOLD}{project_dir}{C_RESET}")
    print(f"Final operator-ready prompts compiled to: {C_BOLD}{out_file}{C_RESET}")
    print("\n==================================================\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
