from lhat.models import CheckResult, Status
from lhat.shell import run_command


def collect_open_ports() -> CheckResult:
    code, stdout, stderr = run_command(["ss", "-tulpen"])

    if code == 0:
        lines = len(stdout.splitlines())
        return CheckResult(
            "LIVE-PORTS",
            "Live open ports",
            Status.INFO,
            f"ss returned {lines} lines",
        )

    return CheckResult(
        "LIVE-PORTS",
        "Live open ports",
        Status.WARN,
        stderr or "ss command failed",
    )


def collect_failed_units() -> CheckResult:
    code, stdout, stderr = run_command(["systemctl", "--failed", "--no-pager"])

    if code == 0:
        return CheckResult(
            "LIVE-SYSTEMD",
            "Failed systemd units",
            Status.INFO,
            stdout or "No output",
        )

    return CheckResult(
        "LIVE-SYSTEMD",
        "Failed systemd units",
        Status.WARN,
        stderr or "systemctl failed",
    )
