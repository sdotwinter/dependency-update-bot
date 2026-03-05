from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List


def _load_catalog(catalog_path: Path) -> Dict[str, str]:
    if not catalog_path.exists():
        return {}
    return json.loads(catalog_path.read_text(encoding="utf-8"))


def check_outdated(deps: Dict[str, str], catalog_path: Path) -> List[dict]:
    catalog = _load_catalog(catalog_path)
    out = []
    for name, current in deps.items():
        latest = catalog.get(name)
        if latest and current and latest != current:
            out.append({"name": name, "current": current, "latest": latest})
    return out
