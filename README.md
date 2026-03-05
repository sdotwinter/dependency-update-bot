# Dependency Update Bot

[![Sponsor](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/sdotwinter)

Dependency Update Bot is a Python CLI that scans dependency files and creates a safe update plan with risk labels.

## Features
- Reads `requirements.txt` and `package.json`
- Compares installed versions against a version catalog
- Flags major-version updates as higher risk
- Outputs terminal report and markdown update plan

## Usage
```bash
python3 main.py scan .
python3 main.py scan . --json
python3 main.py plan . --out update-plan.md
```

## Sponsorware
Free for personal/non-commercial evaluation. Commercial/team usage and advanced integrations require sponsorship.
Suggested tiers: **$7 / $14 / $50**.
