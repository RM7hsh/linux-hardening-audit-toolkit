from pathlib import Path

from lhat.models import CheckResult, Status


def run(root: Path) -> list[CheckResult]:
    firewalld = root / "usr/bin/firewall-cmd"
    ufw = root / "usr/sbin/ufw"
    nft = root / "usr/sbin/nft"
    if firewalld.exists() or ufw.exists() or nft.exists():
        return [CheckResult("FW-001", "Firewall tooling present", Status.PASS, "Firewall tooling detected")]
    return [
        CheckResult(
            "FW-001",
            "Firewall tooling present",
            Status.WARN,
            "No common firewall tooling detected",
            "Install and enable nftables, firewalld or ufw",
        )
    ]
