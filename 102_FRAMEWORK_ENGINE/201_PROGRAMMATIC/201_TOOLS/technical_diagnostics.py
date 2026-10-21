"""Bounded structured diagnostics for the container stderr stream."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import re
import sys
import tomllib
from typing import TextIO

from project_settings_schema import _string


_FIELD_LIMIT = 512
_PATH_LIMIT = 512
_RECORD_LIMIT = 4_096
_SEVERITIES = frozenset({"ERROR", "WARNING", "INFO", "DEBUG"})
_SECRET = re.compile(
    r"(?i)\b(password|passwd|secret|token|api[_-]?key|authorization)\b\s*[:=]\s*[^\s,;]+"
)
_BEARER = re.compile(r"(?i)\bBearer\s+[^\s,;]+")


def _sanitize(value: object, *, limit: int = _FIELD_LIMIT, root: Path | None = None) -> str:
    text = str(value)
    if root is not None:
        text = text.replace(str(root), "<project>")
    text = _SECRET.sub(lambda match: f"{match.group(1)}=<redacted>", text)
    text = _BEARER.sub("Bearer <redacted>", text)
    text = "".join(character if character.isprintable() else " " for character in text)
    return text[:limit]


def _project_prefix(settings: Mapping[str, object]) -> str:
    artifacts = settings.get("artifacts")
    identity = artifacts.get("identity") if isinstance(artifacts, Mapping) else None
    value = identity.get("project_prefix") if isinstance(identity, Mapping) else None
    prefix: str = _string(value, "artifacts.identity.project_prefix")
    if prefix != prefix.upper():
        raise ValueError("validated Project Settings lack an uppercase project prefix")
    return prefix


def _runtime_version() -> str | None:
    source = Path(__file__).resolve().parents[3] / "version.toml"
    try:
        document = tomllib.loads(source.read_text(encoding="utf-8"))
        version = document.get("framework", {}).get("version")
        if type(version) is str and version:
            return _sanitize(version)
    except (OSError, UnicodeError, tomllib.TOMLDecodeError, AttributeError):
        return None
    return None


def _runtime_environment() -> str:
    namespace = os.environ.get("CAPRMEDIO_RUNTIME_NAMESPACE", "")
    if namespace:
        return _sanitize(namespace, limit=128)
    return "docker" if Path("/.dockerenv").is_file() else "host"


def _json_line(record: Mapping[str, str]) -> str:
    return json.dumps(record, ensure_ascii=False, separators=(",", ":"))


def _render(record: dict[str, str]) -> str:
    line = _json_line(record)
    if len((line + "\n").encode("utf-8")) > _RECORD_LIMIT:
        raise ValueError("technical diagnostic record exceeds bounded output size")
    return line


@dataclass(frozen=True)
class TechnicalDiagnosticLogger:
    """Emit one bounded diagnostic record without touching Project state."""

    project_prefix: str
    root: Path
    version: str
    stream: TextIO
    environment: str
    component: str = "ATOM_SEARCH"

    def _record(self, *, code: str, relative_path: str, reason: str,
                correlation_id: str | None, severity: str = "WARNING",
                event: str = "atom_schema_invalid", operation: str = "atom_search",
                outcome: str = "skipped", exception_class: str | None = None) -> dict[str, str]:
        record: dict[str, str] = {
            "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
            "severity": _sanitize(severity, limit=32),
            "event": _sanitize(event, limit=128),
            "component": _sanitize(self.component, limit=128),
            "environment": _sanitize(self.environment, limit=128),
            "version": _sanitize(self.version, limit=128),
            "project_prefix": self.project_prefix,
            "operation": _sanitize(operation, limit=128),
            "outcome": _sanitize(outcome, limit=64),
            "code": _sanitize(code, limit=128),
            "relative_path": _sanitize(relative_path, limit=_PATH_LIMIT, root=self.root),
            "reason": _sanitize(reason, limit=_FIELD_LIMIT, root=self.root),
        }
        if correlation_id is not None:
            record["correlation_id"] = _sanitize(correlation_id, limit=128)
        if exception_class is not None:
            record["exception_class"] = _sanitize(exception_class, limit=128)
        return record

    def emit(self, *, code: str, relative_path: str, reason: str,
             correlation_id: str | None = None, severity: str = "WARNING",
             event: str = "atom_schema_invalid", operation: str = "atom_search",
             outcome: str = "skipped", exception_class: str | None = None) -> str | None:
        if severity not in _SEVERITIES:
            return "invalid diagnostic severity"
        try:
            record = self._record(code=code, relative_path=relative_path, reason=reason,
                                  correlation_id=correlation_id, severity=severity,
                                  event=event, operation=operation, outcome=outcome,
                                  exception_class=exception_class)
            self.stream.write(_render(record) + "\n")
            self.stream.flush()
        except Exception as error:
            return _sanitize(error)
        return None


def make_technical_logger(settings: Mapping[str, object], root: Path, *,
                          stream: TextIO | None = None,
                          environment: str | None = None) -> tuple[TechnicalDiagnosticLogger | None, str | None]:
    """Build a logger from the already validated, bound Project Settings view."""

    try:
        prefix = _project_prefix(settings)
    except (TypeError, ValueError) as error:
        return None, _sanitize(error)
    version = _runtime_version()
    if version is None:
        return None, "framework version is unavailable"
    return TechnicalDiagnosticLogger(
        prefix, root, version,
        stream if stream is not None else sys.stderr,
        environment or _runtime_environment(),
    ), None


__all__ = ["TechnicalDiagnosticLogger", "make_technical_logger"]
