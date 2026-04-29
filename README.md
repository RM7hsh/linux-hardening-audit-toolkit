# Linux Hardening Audit Toolkit

![CI](https://github.com/RM7hsh/linux-hardening-audit-toolkit/actions/workflows/ci.yml/badge.svg)

Linux security baseline audit toolkit for checking **SSH**, **firewall tooling**, **users**, **sudo**, **services**, **ports**, **updates**, **disk visibility** and general server hardening posture.

The project is built as a portfolio-ready Linux administration and security auditing tool. It demonstrates Python CLI structure, baseline security checks, report generation, tests, GitHub Actions CI and clean documentation.

---

## Features

- SSH hardening checks
- UID 0 user detection
- sudo `NOPASSWD` review
- firewall tooling detection
- systemd/service visibility checks
- open ports review guidance
- updates/package metadata checks
- Markdown and JSON report output
- pytest tests
- ruff linting
- GitHub Actions CI

---

## Quick start

```bash
python -m lhat.cli --format markdown
python -m lhat.cli --format json --output reports/audit.json
```

---

## Example output

```text
# Linux Hardening Audit Report

| Check | Status | Message |
|---|---|---|
| SSH-002 | PASS | PermitRootLogin should be set to no |
| SSH-003 | WARN | PasswordAuthentication should be disabled when SSH keys are used |
```

---

## Repository structure

```text
.
├── .github/workflows/ci.yml
├── docs/
├── lhat/
│   ├── checks/
│   ├── cli.py
│   ├── models.py
│   └── runner.py
├── profiles/
├── reports/
├── tests/
└── pyproject.toml
```

---

## What this project demonstrates

- practical Linux security baseline thinking
- Python CLI development
- structured audit checks
- clean report generation
- CI with ruff and pytest
- Git workflow with feature branches, merge commits and tags

---

## Author

**Rajabali Rahimov**  
GitHub: [https://github.com/RM7hsh](https://github.com/RM7hsh)
