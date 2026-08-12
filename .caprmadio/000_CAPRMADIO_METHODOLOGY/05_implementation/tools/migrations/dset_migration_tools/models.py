"""Operation and plan models shared by active migration recipes."""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path


class MigrationError(RuntimeError):
    """A bounded migration cannot proceed without guessing or data loss."""


@dataclass(frozen=True)
class WriteOperation:
    """One exact file replacement or creation."""

    path: Path
    before_sha256: str | None
    content: bytes
    reason: str
    mode: int | None = None


@dataclass(frozen=True)
class DeleteOperation:
    """One exact deletion after its replacement has been staged."""

    path: Path
    before_sha256: str
    reason: str


@dataclass(frozen=True)
class MigrationPlan:
    """A complete fail-closed set of carrier operations."""

    root: Path
    writes: tuple[WriteOperation, ...]
    deletes: tuple[DeleteOperation, ...]

    def digest(self) -> str:
        """Bind one preview to the exact relative operations and bytes."""
        payload = {
            "writes": [_write_digest_record(self.root, item) for item in self.writes],
            "deletes": [
                _delete_digest_record(self.root, item) for item in self.deletes
            ],
        }
        encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
        return hashlib.sha256(encoded).hexdigest()

    def summary(self) -> str:
        """Render the stable human-readable dry-run summary."""
        lines = ["META/GOV carrier migration plan", f"root: {self.root}"]
        lines.extend((f"writes: {len(self.writes)}", f"deletes: {len(self.deletes)}"))
        lines.append(f"plan-digest: {self.digest()}")
        lines.extend(_write_summary(self.root, self.writes))
        lines.extend(_delete_summary(self.root, self.deletes))
        return "\n".join(lines)


def _write_digest_record(
    root: Path, item: WriteOperation
) -> dict[str, str | int | None]:
    record: dict[str, str | int | None] = {
        "path": item.path.relative_to(root).as_posix(),
        "before": item.before_sha256,
        "after": hashlib.sha256(item.content).hexdigest(),
        "reason": item.reason,
    }
    if item.mode is not None:
        record["mode"] = item.mode
    return record


def _delete_digest_record(root: Path, item: DeleteOperation) -> dict[str, str]:
    return {
        "path": item.path.relative_to(root).as_posix(),
        "before": item.before_sha256,
        "reason": item.reason,
    }


def _write_summary(root: Path, operations: tuple[WriteOperation, ...]) -> list[str]:
    return [
        f"{'CREATE' if item.before_sha256 is None else 'UPDATE'} "
        f"{item.path.relative_to(root).as_posix()} — {item.reason}"
        for item in operations
    ]


def _delete_summary(root: Path, operations: tuple[DeleteOperation, ...]) -> list[str]:
    return [
        f"DELETE {item.path.relative_to(root).as_posix()} — {item.reason}"
        for item in operations
    ]
