from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    sudoers = root / "etc/sudoers"

    if not sudoers.exists():
        return [
            CheckResult(
                "SUDO-001",
                "sudoers file exists",
                Status.WARN,
                "/etc/sudoers not found",
            )
        ]

    content = sudoers.read_text(encoding="utf-8", errors="ignore")
    status = Status.WARN if "NOPASSWD" in content else Status.PASS

    return [
        CheckResult(
            "SUDO-002",
            "Passwordless sudo review",
            status,
            "Check NOPASSWD usage in sudoers",
        )
    ]
