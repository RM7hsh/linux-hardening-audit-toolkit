from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    PASS = "PASS"
    WARN = "WARN"
    FAIL = "FAIL"
    INFO = "INFO"


@dataclass(frozen=True)
class CheckResult:
    check_id: str
    title: str
    status: Status
    message: str
    remediation: str = ""
