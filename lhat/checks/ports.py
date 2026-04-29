from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    return [
        CheckResult(
            "PORT-001",
            "Open ports review",
            Status.INFO,
            "Run ss -tulpen on a live system to review listening services",
        )
    ]
