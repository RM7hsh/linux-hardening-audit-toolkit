from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    systemd_dir = root / "etc/systemd/system"

    if systemd_dir.exists():
        return [
            CheckResult(
                "SVC-001",
                "systemd configuration exists",
                Status.INFO,
                "systemd directory detected",
            )
        ]

    return [
        CheckResult(
            "SVC-001",
            "systemd configuration exists",
            Status.WARN,
            "systemd directory not found",
        )
    ]
