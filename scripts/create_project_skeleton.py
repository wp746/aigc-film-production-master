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

    print(project_dir)


if __name__ == "__main__":
    main()
