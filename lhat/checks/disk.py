from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    return [CheckResult("DISK-001", "Disk usage review", Status.INFO, f"Audit root path: {root}")]
