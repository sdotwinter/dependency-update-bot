from __future__ import annotations

import argparse
from pathlib import Path

from checker import check_outdated
from reporter import print_updates
from safety import annotate
from sources import read_package_json, read_requirements
from updater import write_plan


def run(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="dependency-update-bot", description="Scan and plan safe dependency updates.")
    sub = p.add_subparsers(dest="cmd", required=True)

    scan = sub.add_parser("scan", help="Scan dependency manifests")
    scan.add_argument("path", nargs="?", default=".")
    scan.add_argument("--json", action="store_true")

    plan = sub.add_parser("plan", help="Generate update plan markdown")
    plan.add_argument("path", nargs="?", default=".")
    plan.add_argument("--out", default="update-plan.md")

    args = p.parse_args(argv)
    root = Path(args.path).resolve()

    deps = {}
    deps.update(read_requirements(root / "requirements.txt"))
    deps.update(read_package_json(root / "package.json"))

    catalog = root / "latest_versions.json"
    updates = annotate(check_outdated(deps, catalog))

    if args.cmd == "scan":
        print_updates(updates, as_json=args.json)
    else:
        out = Path(args.out)
        if not out.is_absolute():
            out = root / out
        write_plan(out, updates)
        print(f"Wrote plan: {out}")
    return 0
