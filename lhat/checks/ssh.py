from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    config = root / "etc/ssh/sshd_config"
    if not config.exists():
        return [CheckResult("SSH-001", "SSH config exists", Status.WARN, "sshd_config not found")]

    content = config.read_text(encoding="utf-8", errors="ignore")
    checks = []
    checks.append(
        CheckResult(
            "SSH-002",
            "Root login disabled",
            Status.PASS if "PermitRootLogin no" in content else Status.FAIL,
            "PermitRootLogin should be set to no",
            "Set PermitRootLogin no in /etc/ssh/sshd_config",
        )
    )
    checks.append(
        CheckResult(
            "SSH-003",
            "Password authentication disabled",
            Status.PASS if "PasswordAuthentication no" in content else Status.WARN,
            "PasswordAuthentication should be disabled when SSH keys are used",
            "Set PasswordAuthentication no after confirming key-based access",
        )
    )
    return checks
