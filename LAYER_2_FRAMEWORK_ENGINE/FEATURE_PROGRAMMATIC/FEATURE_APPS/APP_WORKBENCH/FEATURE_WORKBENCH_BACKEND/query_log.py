# CA-R-2903@4
# CA-M-502@2
# CA-D-698@3

"""Two-day Workbench query-attempt log without result data."""

from __future__ import annotations

import datetime as dt
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import sys
import threading
from typing import Any
import uuid


class QueryLog:
    """Persist temporary attempt metadata for one selected Project."""

    _TTL = dt.timedelta(hours=48)

    def __init__(self, root: Path) -> None:
        runtime = Path(root) / ".caprmedio_runtime" / "workbench"
        self._directory = runtime / "query_log"
        self._legacy_path = runtime / "query-log.json"
        self._lock = threading.RLock()
        self._submit_lock = threading.Lock()
        self._writer = ThreadPoolExecutor(max_workers=1, thread_name_prefix="workbench-query-log")
        self._closed = False

    @staticmethod
    def _now() -> dt.datetime:
        return dt.datetime.now(dt.UTC)

    @staticmethod
    def _record(value: object) -> dict[str, Any]:
        keys = {"log_id", "at", "sql", "outcome", "error", "row_count", "column_count"}
        if not isinstance(value, dict) or set(value) != keys or not all(
            isinstance(value[key], str) for key in ("log_id", "at", "sql", "outcome")
        ):
            raise ValueError("query log is unavailable")
        if value["outcome"] not in {"success", "failed"} or value["error"] is not None and not isinstance(value["error"], str):
            raise ValueError("query log is unavailable")
        for key in ("row_count", "column_count"):
            if value[key] is not None and (isinstance(value[key], bool) or not isinstance(value[key], int)):
                raise ValueError("query log is unavailable")
        return dict(value)

    @staticmethod
    def _at(record: dict[str, Any]) -> dt.datetime:
        try:
            value = dt.datetime.fromisoformat(record["at"])
        except ValueError as error:
            raise ValueError("query log is unavailable") from error
        if value.tzinfo is None:
            raise ValueError("query log is unavailable")
        return value

    def _hour_path(self, at: dt.datetime) -> Path:
        value = at.astimezone(dt.UTC)
        return self._directory / value.strftime("query-log-%Y-%m-%d-%H.ndjson")

    def _read_hour(self, path: Path) -> list[dict[str, Any]]:
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (OSError, UnicodeError) as error:
            raise ValueError("query log is unavailable") from error
        try:
            return [self._record(json.loads(line)) for line in lines if line]
        except json.JSONDecodeError as error:
            raise ValueError("query log is unavailable") from error

    def _read_legacy(self) -> list[dict[str, Any]]:
        if not self._legacy_path.exists():
            return []
        try:
            value = json.loads(self._legacy_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError("query log is unavailable") from error
        if not isinstance(value, list):
            raise ValueError("query log is unavailable")
        return [self._record(item) for item in value]

    @classmethod
    def _retain(cls, records: list[dict[str, Any]], now: dt.datetime) -> list[dict[str, Any]]:
        cutoff = now - cls._TTL
        return [record for record in records if cls._at(record) > cutoff]

    @staticmethod
    def _write_hour(path: Path, records: list[dict[str, Any]]) -> None:
        if not records:
            path.unlink(missing_ok=True)
            return
        content = "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records)
        path.write_text(content, encoding="utf-8")

    def _hourly_records(self, now: dt.datetime) -> list[dict[str, Any]]:
        if not self._directory.is_dir():
            return []
        retained: list[dict[str, Any]] = []
        for path in sorted(self._directory.glob("query-log-*.ndjson")):
            records = self._read_hour(path)
            current = self._retain(records, now)
            if current != records:
                self._write_hour(path, current)
            retained.extend(current)
        return retained

    def _retained(self, now: dt.datetime) -> list[dict[str, Any]]:
        return self._hourly_records(now) + self._retain(self._read_legacy(), now)

    def _new_record(self, sql: str, result: dict[str, Any], now: dt.datetime) -> dict[str, Any]:
        if not isinstance(sql, str):
            raise ValueError("SQL must be a string")
        return {
            "log_id": str(uuid.uuid7()), "at": now.isoformat(), "sql": sql,
            "outcome": "success" if result["status"] == "success" else "failed",
            "error": result["error"], "row_count": result["row_count"], "column_count": result["column_count"],
        }

    def _append_record(self, record: dict[str, Any], now: dt.datetime) -> None:
        with self._lock:
            self._hourly_records(now)
            path = self._hour_path(self._at(record))
            try:
                path.parent.mkdir(parents=True, exist_ok=True)
                with path.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            except (OSError, UnicodeError) as error:
                raise ValueError("query log is unavailable") from error

    def append(self, sql: str, result: dict[str, Any]) -> dict[str, Any]:
        now = self._now()
        record = self._new_record(sql, result, now)
        self._append_record(record, now)
        return record

    def _append_background(self, record: dict[str, Any], now: dt.datetime) -> None:
        try:
            self._append_record(record, now)
        except Exception as error:
            print(f"query log failed: {error}", file=sys.stderr)

    def append_async(self, sql: str, result: dict[str, Any]) -> dict[str, Any]:
        now = self._now()
        record = self._new_record(sql, result, now)
        with self._submit_lock:
            if self._closed:
                raise ValueError("query log is unavailable")
            self._writer.submit(self._append_background, record, now)
        return record

    def close(self) -> None:
        with self._submit_lock:
            if self._closed:
                return
            self._closed = True
        self._writer.shutdown(wait=True)

    @staticmethod
    def _limit(value: object) -> int:
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 1000:
            raise ValueError("limit must be an integer from 1 to 1000")
        return value

    def list(self, limit: object = 20) -> dict[str, list[dict[str, Any]]]:
        limit = self._limit(limit)
        with self._lock:
            records = sorted(self._retained(self._now()), key=self._at, reverse=True)
        return {"items": records[:limit]}

    def get(self, log_id: object) -> dict[str, Any]:
        if not isinstance(log_id, str) or not log_id:
            raise ValueError("log_id must be a non-empty string")
        with self._lock:
            for record in self._retained(self._now()):
                if record["log_id"] == log_id:
                    return record
        raise ValueError("unknown log_id")
