from __future__ import annotations

import json
from typing import List


def print_updates(updates: List[dict], as_json: bool = False) -> None:
    if as_json:
        print(json.dumps(updates, indent=2))
        return

    if not updates:
        print("✅ No outdated dependencies found.")
        return

    print("name                 current      latest       risk   reason")
    print("-" * 72)
    for u in updates:
        print(
            f"{u['name'][:20]:20} {u['current'][:12]:12} {u['latest'][:12]:12} {u.get('risk',''):6} {u.get('riskReason','')}"
        )
