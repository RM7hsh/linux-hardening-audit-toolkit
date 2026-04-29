from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    passwd = root / "etc/passwd"

    if not passwd.exists():
        return [
            CheckResult(
                "USR-001",
                "passwd file exists",
                Status.WARN,
                "/etc/passwd not found",
            )
        ]

    risky = []
    for line in passwd.read_text(encoding="utf-8", errors="ignore").splitlines():
        parts = line.split(":")
        if len(parts) >= 7 and parts[2] == "0" and parts[0] != "root":
            risky.append(parts[0])

    if risky:
        return [
            CheckResult(
                "USR-002",
                "Only root has UID 0",
                Status.FAIL,
                f"UID 0 users: {', '.join(risky)}",
            )
        ]

    return [
        CheckResult(
            "USR-002",
            "Only root has UID 0",
            Status.PASS,
            "No extra UID 0 users found",
        )
    ]
