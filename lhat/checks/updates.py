from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    apt_lists = root / "var/lib/apt/lists"
    if apt_lists.exists():
        return [CheckResult("UPD-001", "APT metadata exists", Status.INFO, "APT metadata directory found")]
    return [CheckResult("UPD-001", "APT metadata exists", Status.INFO, "Package manager metadata not detected")]
