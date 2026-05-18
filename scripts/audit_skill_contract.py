#!/usr/bin/env python3
"""Audit that master skill references are wired into SKILL.md and README.md."""

from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_REFERENCES = [
    "source-ingestion-normalization.md",
    "shortform-filmgrade-pipeline.md",
    "creative-development-orchestration.md",
    "upstream-screenwriting-director.md",
    "brand-ad-brief-engine.md",
    "retention-performance-gate.md",
    "aigc-director-system.md",
    "aigc-production-handoff-contract.md",
    "model-platform-adapter.md",
    "universal-agent-adapter.md",
    "downstream-image2-seedance-bridge.md",
    "final-prompt-delivery-contract.md",
    "module-visibility-and-reinsertion.md",
    "postproduction-delivery.md",
    "privacy-provenance-governance.md",
    "compliance-rights-ip-gate.md",
    "versioning-feedback-loop.md",
    "qa-risk-gates.md",
]

REQUIRED_GENRE_PLAYBOOKS = [
    "suspense-thriller.md",
    "cultural-tourism.md",
    "commercial-tvc.md",
    "short-drama.md",
    "black-humor.md",
]


def main() -> int:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing = []

    for ref in REQUIRED_REFERENCES:
        path = ROOT / "references" / ref
        if not path.exists():
            missing.append(f"missing file: references/{ref}")
        if ref not in skill:
            missing.append(f"not wired in SKILL.md: {ref}")
        if ref not in readme:
            missing.append(f"not documented in README.md: {ref}")

    index = (ROOT / "references" / "genre-playbook-index.md").read_text(encoding="utf-8")
    for ref in REQUIRED_GENRE_PLAYBOOKS:
        path = ROOT / "references" / "genre-playbooks" / ref
        if not path.exists():
            missing.append(f"missing genre playbook: references/genre-playbooks/{ref}")
        if ref not in index:
            missing.append(f"not wired in genre-playbook-index.md: {ref}")

    if "v1.6.0" not in readme:
        missing.append("README.md does not mention v1.6.0")

    if missing:
        print("Master skill contract audit failed:")
        for item in missing:
            print(f"- {item}")
        return 1

    print("Master skill contract audit passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
