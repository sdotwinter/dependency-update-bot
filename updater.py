from __future__ import annotations

from pathlib import Path
from typing import List


def write_plan(path: Path, updates: List[dict]) -> None:
    lines = ["# Dependency Update Plan", ""]
    if not updates:
        lines.append("No updates available.")
    else:
        for u in updates:
            lines.append(
                f"- {u['name']}: {u['current']} -> {u['latest']} (risk: {u.get('risk','unknown')}, {u.get('riskReason','')})"
            )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
