import json
from pathlib import Path

from lhat.checks import disk, firewall, ports, services, ssh, sudo, updates, users
from lhat.models import CheckResult

CHECK_MODULES = [
    ssh,
    firewall,
    users,
    sudo,
    services,
    ports,
    updates,
    disk,
]


def run_all_checks(root: Path = Path("/")) -> list[CheckResult]:
    results: list[CheckResult] = []
    for module in CHECK_MODULES:
        results.extend(module.run(root=root))
    return results


def to_json(results: list[CheckResult]) -> str:
    return json.dumps([result.__dict__ for result in results], indent=2, ensure_ascii=False)


def to_markdown(results: list[CheckResult]) -> str:
    lines = ["# Linux Hardening Audit Report", ""]
    lines.append("| Check | Status | Message |")
    lines.append("|---|---|---|")
    for result in results:
        lines.append(f"| {result.check_id} | {result.status} | {result.message} |")
    return "\n".join(lines) + "\n"
