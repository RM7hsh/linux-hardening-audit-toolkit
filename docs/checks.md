# Checks

## SSH

- `SSH-001` verifies that `sshd_config` exists.
- `SSH-002` checks whether root login is disabled.
- `SSH-003` checks whether password authentication is disabled.

## Firewall

- `FW-001` detects common firewall tooling such as nftables, firewalld or ufw.

## Users and sudo

- `USR-002` detects non-root users with UID 0.
- `SUDO-002` reminds the operator to review `NOPASSWD` usage.

## Services, ports, updates and disk

These checks provide baseline operational visibility and point the administrator to live commands that should be reviewed on a real server.
