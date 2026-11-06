# CA-R-2950@1
# CA-M-490@1
# CA-D-695@1

"""Bounded durable watcher observations for one Workbench Project."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path, PurePosixPath


_OPERATIONS = {"create", "update", "rename", "move", "remove"}


def _path_value(value: object, field: str, *, required: bool) -> str | None:
    if value is None and not required:
        return None
    if not isinstance(value, str) or not value:
        raise ValueError(f"{field} must be a non-empty string" if required else f"{field} must be a string or null")
    try:
        value.encode("utf-8")
    except UnicodeEncodeError as error:
        raise ValueError(f"{field} must be valid UTF-8") from error
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{field} must be repository-relative")
    return value


def validate_change_record(value: object) -> dict[str, str | None]:
    """Validate the one four-field record shape shared by file and DuckDB."""
    fields = {"observed_at", "operation", "old_path", "new_path"}
    if not isinstance(value, dict) or set(value) != fields:
        raise ValueError("watcher change log is unavailable")
    observed_at, operation = value["observed_at"], value["operation"]
    if not isinstance(observed_at, str) or not isinstance(operation, str) or operation not in _OPERATIONS:
        raise ValueError("watcher change log is unavailable")
    try:
        timestamp = dt.datetime.fromisoformat(observed_at)
    except ValueError as error:
        raise ValueError("watcher change log is unavailable") from error
    if timestamp.tzinfo is None:
        raise ValueError("watcher change log is unavailable")
    old_path = _path_value(value["old_path"], "old_path", required=operation in {"remove", "rename", "move"})
    new_path = _path_value(value["new_path"], "new_path", required=operation in {"create", "update", "rename", "move"})
    if (operation in {"create", "update"} and old_path is not None) or (operation == "remove" and new_path is not None):
        raise ValueError("watcher change log is unavailable")
    return {"observed_at": observed_at, "operation": operation, "old_path": old_path, "new_path": new_path}


class WatcherChangeLog:
    """Own the runtime NDJSON file; QueryStore mirrors returned retained rows."""

    TTL = dt.timedelta(hours=48)
    MAX_ROWS = 100_000

    def __init__(self, root: Path) -> None:
        self._path = Path(root) / ".caprmedio_runtime" / "workbench" / "watcher-change-log.ndjson"
        self._rows: list[dict[str, str | None]] | None = None
        self._next_expiry: dt.datetime | None = None

    @staticmethod
    def _now() -> dt.datetime:
        return dt.datetime.now(dt.UTC)

    def _read(self) -> list[dict[str, str | None]]:
        if not self._path.exists():
            return []
        try:
            lines = self._path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as error:
            raise ValueError("watcher change log is unavailable") from error
        try:
            return [validate_change_record(json.loads(line)) for line in lines if line]
        except json.JSONDecodeError as error:
            raise ValueError("watcher change log is unavailable") from error

    def _write(self, rows: list[dict[str, str | None]]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self._path.with_suffix(".tmp")
        content = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows)
        temporary.write_text(content, encoding="utf-8")
        temporary.replace(self._path)

    def _append(self, rows: list[dict[str, str | None]]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        with self._path.open("a", encoding="utf-8") as handle:
            for row in rows:
                handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")

    def _set_rows(self, rows: list[dict[str, str | None]]) -> None:
        self._rows = rows
        self._next_expiry = min(
            (dt.datetime.fromisoformat(str(row["observed_at"])) + self.TTL for row in rows),
            default=None,
        )

    def _cached_rows(self) -> list[dict[str, str | None]]:
        if self._rows is None:
            self._set_rows(self._read())
        assert self._rows is not None
        return self._rows

    @classmethod
    def _retain(cls, rows: list[dict[str, str | None]], now: dt.datetime) -> list[dict[str, str | None]]:
        cutoff = now - cls.TTL
        dated: list[tuple[dt.datetime, int, dict[str, str | None]]] = []
        for index, row in enumerate(rows):
            timestamp = dt.datetime.fromisoformat(str(row["observed_at"]))
            if timestamp >= cutoff:
                dated.append((timestamp, index, row))
        if len(dated) > cls.MAX_ROWS:
            retained_indexes = {index for _at, index, _row in sorted(dated)[:-cls.MAX_ROWS]}
            dated = [item for item in dated if item[1] not in retained_indexes]
        return [row for _at, _index, row in dated]

    def append_delta(
        self, events: object,
    ) -> tuple[list[dict[str, str | None]], list[dict[str, str | None]], bool]:
        """Append a batch, reporting whether retention required a full replacement."""
        if not isinstance(events, list):
            raise ValueError("watcher events must be a list")
        now = self._now()
        original = self._cached_rows()
        before = original
        replace_required = False
        if self._next_expiry is not None and now >= self._next_expiry:
            before = self._retain(before, now)
            replace_required = before != original
        observed_at = now.isoformat()
        additions: list[dict[str, str | None]] = []
        for event in events:
            if not isinstance(event, dict) or set(event) - {"operation", "old_path", "new_path"} or "operation" not in event:
                raise ValueError("watcher event is invalid")
            additions.append(validate_change_record({"observed_at": observed_at, "operation": event["operation"], "old_path": event.get("old_path"), "new_path": event.get("new_path")}))
        retained = self._retain(before + additions, now)
        replace_required = replace_required or retained != before + additions
        if replace_required:
            self._write(retained)
        elif additions:
            self._append(additions)
        self._set_rows(retained)
        return retained, additions, replace_required

    def append(self, events: object) -> tuple[list[dict[str, str | None]], bool]:
        rows, additions, replace_required = self.append_delta(events)
        return rows, bool(additions) or replace_required

    def prune(self) -> tuple[list[dict[str, str | None]], bool]:
        before = self._cached_rows()
        now = self._now()
        if self._next_expiry is None or now < self._next_expiry:
            return before, False
        retained = self._retain(before, now)
        changed = retained != before
        if changed:
            self._write(retained)
        self._set_rows(retained)
        return retained, changed
