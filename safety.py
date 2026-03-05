from __future__ import annotations

from typing import List, Tuple


def _major(v: str) -> int:
    try:
        return int(v.strip().lstrip("^~>=< ").split(".")[0])
    except Exception:
        return -1


def assess_risk(current: str, latest: str) -> Tuple[str, str]:
    cmaj = _major(current)
    lmaj = _major(latest)
    if cmaj >= 0 and lmaj >= 0 and lmaj > cmaj:
        return "high", "Major version bump"
    return "low", "Safe/patch-level candidate"


def annotate(updates: List[dict]) -> List[dict]:
    out = []
    for u in updates:
        sev, reason = assess_risk(u.get("current", ""), u.get("latest", ""))
        x = dict(u)
        x["risk"] = sev
        x["riskReason"] = reason
        out.append(x)
    return out
