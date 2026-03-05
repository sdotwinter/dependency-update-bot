from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


def read_requirements(path: Path) -> Dict[str, str]:
    deps: Dict[str, str] = {}
    if not path.exists():
        return deps
    for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if "==" in s:
            name, version = s.split("==", 1)
            deps[name.strip()] = version.strip()
        else:
            deps[s] = ""
    return deps


def read_package_json(path: Path) -> Dict[str, str]:
    deps: Dict[str, str] = {}
    if not path.exists():
        return deps
    data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    for section in ("dependencies", "devDependencies"):
        for k, v in data.get(section, {}).items():
            deps[k] = str(v)
    return deps
