# Dependency Update Bot

Dependency Update Bot is a Python CLI that scans dependency files and creates a safe update plan with risk labels.

## Features
- Reads `requirements.txt` and `package.json`
- Compares installed versions against a version catalog
- Flags major-version updates as higher risk
- Outputs terminal report and markdown update plan

## Usage
```bash
cd /home/sean/.openclaw/workspace/app-factory-hub/projects/dependency-update-bot
python3 main.py scan .
python3 main.py scan . --json
python3 main.py plan . --out update-plan.md
```

## Notes
- This MVP uses `latest_versions.json` as a local version source.
- No auto-apply is performed; it only proposes updates.

## Sponsorship

This project follows the App Factory sponsorship model:

### $5/month - Supporter
- Sponsor badge on your GitHub profile
- Monthly sponsor update

### $25/month - Builder Circle
- Everything in Supporter
- Name listed in project Sponsors section (monthly refresh)
- Access to private sponsor Discord channel

### $100/month - Priority Maintainer
- Everything in Builder Circle
- Priority bug triage for your reports (max 2 issues/month)
- Response target: within 5 business days

### $1,000/month - Operator Advisory
- Everything in Priority Maintainer
- Dedicated async advisory support
- Service boundary: guidance and review only (no custom development included)

### $5,000 one-time - Custom Project Engagement
- Custom contract engagement
- Discovery required before kickoff
- Scope, timeline, and deliverables agreed in writing

Sponsor: https://github.com/sponsors/sdotwinter

