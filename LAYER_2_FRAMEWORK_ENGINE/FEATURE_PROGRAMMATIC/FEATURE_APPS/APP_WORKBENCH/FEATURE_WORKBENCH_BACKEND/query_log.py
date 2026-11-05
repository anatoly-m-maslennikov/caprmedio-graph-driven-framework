# CA-R-2903@1
# CA-M-476@1
# CA-D-681@1

"""Seven-day Workbench query-attempt log without result data."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from typing import Any
import uuid


class QueryLog:
    """Persist temporary attempt metadata for one selected Project."""

    _TTL = dt.timedelta(days=7)

    def __init__(self, root: Path) -> None:
        self._path = Path(root) / ".caprmedio_runtime" / "workbench" / "query-log.json"

    @staticmethod
    def _now() -> dt.datetime:
        return dt.datetime.now(dt.UTC)

    @staticmethod
    def _record(value: object) -> dict[str, Any]:
        keys = {"log_id", "at", "sql", "outcome", "error", "row_count", "column_count"}
        if not isinstance(value, dict) or set(value) != keys or not all(isinstance(value[key], str) for key in ("log_id", "at", "sql", "outcome")):
            raise ValueError("query log is unavailable")
        if value["outcome"] not in {"success", "failed"} or value["error"] is not None and not isinstance(value["error"], str):
            raise ValueError("query log is unavailable")
        for key in ("row_count", "column_count"):
            if value[key] is not None and (isinstance(value[key], bool) or not isinstance(value[key], int)):
                raise ValueError("query log is unavailable")
        return dict(value)

    def _read(self) -> list[dict[str, Any]]:
        if not self._path.exists():
            return []
        try:
            value = json.loads(self._path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError("query log is unavailable") from error
        if not isinstance(value, list):
            raise ValueError("query log is unavailable")
        return [self._record(item) for item in value]

    def _write(self, records: list[dict[str, Any]]) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self._path.with_suffix(".tmp")
        temporary.write_text(json.dumps(records, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        temporary.replace(self._path)

    def _retain(self, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
        cutoff = self._now() - self._TTL
        retained: list[dict[str, Any]] = []
        for record in records:
            try:
                observed = dt.datetime.fromisoformat(record["at"])
            except ValueError as error:
                raise ValueError("query log is unavailable") from error
            if observed.tzinfo is None:
                raise ValueError("query log is unavailable")
            if observed >= cutoff:
                retained.append(record)
        return retained

    def append(self, sql: str, result: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(sql, str):
            raise ValueError("SQL must be a string")
        record = {
            "log_id": str(uuid.uuid7()), "at": self._now().isoformat(), "sql": sql,
            "outcome": "success" if result["status"] == "success" else "failed",
            "error": result["error"], "row_count": result["row_count"], "column_count": result["column_count"],
        }
        records = self._retain(self._read())
        records.append(record)
        self._write(records)
        return record

    def list(self, limit: object = 20) -> dict[str, list[dict[str, Any]]]:
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 1000:
            raise ValueError("limit must be an integer from 1 to 1000")
        records = self._retain(self._read())
        self._write(records)
        return {"items": list(reversed(records[-limit:]))}

    def get(self, log_id: object) -> dict[str, Any]:
        if not isinstance(log_id, str) or not log_id:
            raise ValueError("log_id must be a non-empty string")
        records = self._retain(self._read())
        self._write(records)
        for record in records:
            if record["log_id"] == log_id:
                return record
        raise ValueError("unknown log_id")
