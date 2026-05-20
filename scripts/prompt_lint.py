#!/usr/bin/env python3
"""Lint Image2/Seedance prompt files for production-critical rules.

This script is intentionally lightweight: it catches hard mechanical issues
before a prompt file reaches Seedance, but it does not judge creative quality.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

SEEDANCE_CHAR_LIMIT = 5000

FENCE_RE = re.compile(
    r"^###\s+(?P<title>[^\n]*Seedance[^\n]*)\n(?:[ \t]*(?:>[^\n]*)?\n)*[ \t]*```text\n(?P<body>.*?)\n```",
    re.MULTILINE | re.DOTALL,
)
STORYBOARD_TITLE_RE = re.compile(r"^###\s+(?P<title>[^\n]*(?:Storyboard|故事板)[^\n]*)$", re.MULTILINE)
SHOT_RE = re.compile(r"\bS(?P<num>\d{2})\b")
CHINESE_DIALOGUE_RE = re.compile(r"[“\"『「](?P<line>[\u4e00-\u9fff，。！？、；：]{4,})[”\"』」]")
TIMECODE_RE = re.compile(
    r"(?P<start_min>\d+):(?P<start_sec>\d{2})(?:\.\d+)?\s*[-–]\s*(?P<end_min>\d+):(?P<end_sec>\d{2})(?:\.\d+)?"
)
ASSET_RE = re.compile(r"\b(?:CHAR|SCENE|PROP|PRODUCT|VEHICLE|STYLE)_[A-Z0-9]+\b")
CLEAN_FRAME_TOKENS = (
    "不要字幕",
    "无字幕",
    "no subtitles",
    "no captions",
    "不要画面内文字",
    "no on-screen text",
    "不要乱码",
)
STYLE_FORBID_TOKENS = (
    "不要游戏",
    "非游戏",
    "不是游戏",
    "no game",
    "not game",
    "不要CG",
    "非CG",
    "照片级",
    "真人电影写实",
)
CROWD_TOKENS = (
    "群众",
    "群像",
    "士兵们",
    "队列",
    "人群",
    "集会",
    "难民",
    "观众",
    "工作人员",
    "村民",
    "路人",
    "家属",
    "病人",
    "警察",
    "crowd",
    "extras",
    "bystanders",
    "soldiers",
)
CROWD_GUARD_TOKENS = (
    "不同的人",
    "不同年龄",
    "不同脸型",
    "不要同脸",
    "不要克隆",
    "no cloned",
    "no duplicate faces",
    "varied faces",
    "distinct faces",
)
STYLE_REFERENCE_TOKENS = (
    "参考风格",
    "风格参考",
    "参考片",
    "参考电影",
    "电影风格",
    "提取风格",
    "style reference",
    "reference style",
    "STYLE_REF",
)
STYLE_LOCK_TOKENS = (
    "STYLE_BIBLE",
    "STYLE_LOCK",
    "STYLE LOCK",
    "GLOBAL LOOK",
    "Global look",
    "Visual style",
    "风格圣经",
    "风格锁",
    "影像风格",
    "色彩/光线/镜头",
    "色彩、光线、镜头",
)
DIALOGUE_TOKENS = ("对白", "台词", "说", "voice", "dialogue", "line")
DIALOGUE_GUARD_TOKENS = (
    "语速",
    "停",
    "停顿",
    "呼吸",
    "不渲染成字幕",
    "不要字幕",
    "spoken",
    "speech rate",
    "pause",
)
COMPLEXITY_TOKENS = ("SEGMENT_BUDGET", "复杂度", "budget")


def seconds(minutes: str, secs: str) -> int:
    return int(minutes) * 60 + int(secs)


def is_local_timecode(match: re.Match[str]) -> bool:
    """Require unambiguous local mm:ss notation inside one Seedance segment."""
    if match.group("start_min") != "0" or match.group("end_min") != "0":
        return False
    return seconds(match.group("end_min"), match.group("end_sec")) <= 15


def line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def lint_file(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: not valid UTF-8 ({exc.reason}); decode/convert source text before prompt lint"]

    errors: list[str] = []
    warnings: list[str] = []

    seedance_blocks = list(FENCE_RE.finditer(text))
    if not seedance_blocks:
        errors.append(f"{path}: no fenced Seedance prompt blocks found")

    if "## Asset Design Prompts" not in text:
        warnings.append(f"{path}: missing '## Asset Design Prompts' section")
    if "## Storyboard Prompts" not in text and "## Storyboard Prompts + Seedance Prompts" not in text:
        warnings.append(f"{path}: missing storyboard section")

    declared_assets = set(ASSET_RE.findall(text))
    storyboard_titles = [m.group("title") for m in STORYBOARD_TITLE_RE.finditer(text)]

    for index, match in enumerate(seedance_blocks, start=1):
        title = match.group("title").strip()
        body = match.group("body").strip()
        line = line_for_offset(text, match.start())
        char_count = len(body)

        if char_count > SEEDANCE_CHAR_LIMIT:
            errors.append(f"{path}:{line}: {title}: {char_count} chars exceeds Seedance {SEEDANCE_CHAR_LIMIT}-char hard limit")

        if "0:00" not in body:
            errors.append(f"{path}:{line}: {title}: missing local start timecode 0:00")

        timecodes = list(TIMECODE_RE.finditer(body))
        if not timecodes:
            warnings.append(f"{path}:{line}: {title}: no mm:ss-mm:ss timecode ranges detected")
        for tc in timecodes:
            if not is_local_timecode(tc):
                errors.append(
                    f"{path}:{line}: {title}: timecode {tc.group(0)!r} ends after 0:15"
                )

        shots = [int(m.group("num")) for m in SHOT_RE.finditer(body)]
        if shots:
            unique = sorted(set(shots))
            expected = list(range(unique[0], unique[-1] + 1))
            if unique != expected:
                warnings.append(f"{path}:{line}: {title}: non-contiguous shot ids {unique}")
            if len(unique) > 8:
                errors.append(f"{path}:{line}: {title}: {len(unique)} shots in one segment; likely over-complex for 15s")
        else:
            warnings.append(f"{path}:{line}: {title}: no S01/S02 shot ids detected")

        refs = set(ASSET_RE.findall(body))
        missing = sorted(refs - declared_assets)
        if missing:
            warnings.append(f"{path}:{line}: {title}: references assets not seen elsewhere: {', '.join(missing)}")

        if not any(token in body for token in ("禁止", "DO NOT", "不得", "no ")):
            warnings.append(f"{path}:{line}: {title}: no negative/forbidden drift instruction detected")

        if not any(token.lower() in body.lower() for token in CLEAN_FRAME_TOKENS):
            errors.append(f"{path}:{line}: {title}: missing clean-frame/no-subtitle/no-random-text guard")

        if any(token in text for token in ("战争", "历史", "军", "战场", "部队")) and not any(
            token.lower() in body.lower() for token in STYLE_FORBID_TOKENS
        ):
            errors.append(f"{path}:{line}: {title}: possible realist war/historical project without game/CG/style guard")

        if any(token.lower() in body.lower() for token in CROWD_TOKENS) and not any(
            token.lower() in body.lower() for token in CROWD_GUARD_TOKENS
        ):
            errors.append(f"{path}:{line}: {title}: group/crowd scene without no-cloned-faces diversity guard")

        if any(token.lower() in text.lower() for token in STYLE_REFERENCE_TOKENS) and not any(
            token.lower() in body.lower() for token in STYLE_LOCK_TOKENS
        ):
            errors.append(f"{path}:{line}: {title}: style reference mentioned but Seedance block lacks STYLE_BIBLE/STYLE_LOCK")

        has_dialogue = any(token.lower() in body.lower() for token in DIALOGUE_TOKENS) or bool(CHINESE_DIALOGUE_RE.search(body))
        if has_dialogue and not any(token.lower() in body.lower() for token in DIALOGUE_GUARD_TOKENS):
            errors.append(f"{path}:{line}: {title}: dialogue/voice present without speech-rate/pause/no-subtitle guard")

        if "## Segment Plan" in text and not any(token in body for token in COMPLEXITY_TOKENS):
            warnings.append(f"{path}:{line}: {title}: segment plan present but Seedance block lacks SEGMENT_BUDGET/complexity note")

        if index > len(storyboard_titles):
            warnings.append(f"{path}:{line}: {title}: more Seedance prompts than storyboard headings")

    return [*errors, *warnings]


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint Image2 Seedance prompt markdown files.")
    parser.add_argument("files", nargs="+", type=Path, help="Prompt markdown files to lint")
    args = parser.parse_args()

    all_messages: list[str] = []
    for path in args.files:
        if not path.exists():
            all_messages.append(f"{path}: file not found")
            continue
        all_messages.extend(lint_file(path))

    for msg in all_messages:
        print(msg)

    has_error = any(
        "exceeds Seedance" in msg
        or "missing local start" in msg
        or "ends after" in msg
        or "no fenced" in msg
        or "file not found" in msg
        or "not valid UTF-8" in msg
        or "missing clean-frame" in msg
        or "without game/CG/style guard" in msg
        or "without no-cloned-faces" in msg
        or "lacks STYLE_BIBLE/STYLE_LOCK" in msg
        or "dialogue/voice present" in msg
        or "shots in one segment" in msg
        for msg in all_messages
    )
    if not all_messages:
        print("prompt_lint: PASS")
    elif not has_error:
        print("prompt_lint: PASS with warnings")
    return 1 if has_error else 0


if __name__ == "__main__":
    sys.exit(main())
