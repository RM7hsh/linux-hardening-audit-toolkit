from pathlib import Path

from lhat.runner import run_all_checks, to_markdown


def test_runner_returns_results(tmp_path: Path) -> None:
    etc_ssh = tmp_path / "etc/ssh"
    etc_ssh.mkdir(parents=True)
    (etc_ssh / "sshd_config").write_text("PermitRootLogin no\nPasswordAuthentication no\n", encoding="utf-8")
    results = run_all_checks(root=tmp_path)
    assert results
    assert "Linux Hardening Audit Report" in to_markdown(results)
