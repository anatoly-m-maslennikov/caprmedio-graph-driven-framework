# CA-M-470@1
# CA-R-2776@1
# CA-D-673@8

"""Immutable local saved SQL and Worksheet carriers."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import re
import sys
from urllib.parse import parse_qs, urlparse
import uuid


_SAVED_ID = re.compile(r"^(?P<kind>[qw])_(?P<token>[0-9a-f]{32})$")
_SAVED_FILE = re.compile(r"^(?P<id>[qw]_[0-9a-f]{32})\.(?P<extension>sql|json)$")


class SavedQueryError(RuntimeError):
    """Expose a completed save alongside the later execution failure."""

    def __init__(self, saved_query: dict[str, str], original_error: Exception) -> None:
        super().__init__(str(original_error))
        self.saved_query = saved_query
        self.original_error = original_error


class SavedQueryStore:
    """Own immutable query files under one Project runtime directory."""

    def __init__(self, root: Path) -> None:
        self._directory = Path(root) / ".caprmedio_runtime" / "workbench" / "saved_queries"

    @staticmethod
    def _sql(value: object) -> str:
        if not isinstance(value, str):
            raise ValueError("SQL must be a string")
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as error:
            raise ValueError("SQL must be valid UTF-8") from error
        return value

    @staticmethod
    def _id(value: object) -> tuple[str, str]:
        if not isinstance(value, str):
            raise ValueError("saved query reference is invalid")
        match = _SAVED_ID.fullmatch(value)
        if match is None:
            raise ValueError("saved query reference is invalid")
        return match.group("kind"), value

    def _path(self, saved_query_id: str) -> Path:
        kind, value = self._id(saved_query_id)
        return self._directory / f"{value}.{'sql' if kind == 'q' else 'json'}"

    def _save(self, sql: object, kind: str) -> dict[str, str]:
        value = self._sql(sql)
        saved_query_id = f"{kind}_{uuid.uuid4().hex}"
        path = self._path(saved_query_id)
        try:
            self._directory.mkdir(parents=True, exist_ok=True)
            if kind == "q":
                with path.open("x", encoding="utf-8", newline="") as target:
                    target.write(value)
                return {"saved_query_id": saved_query_id, "kind": "query", "sql": value}
            with path.open("x", encoding="utf-8", newline="") as target:
                json.dump({"sql": value}, target, ensure_ascii=False, separators=(",", ":"))
            return {"saved_query_id": saved_query_id, "kind": "worksheet", "sql": value}
        except OSError as error:
            raise ValueError(f"saved query failed: {error}") from error

    def save_query(self, sql: object) -> dict[str, str]:
        return self._save(sql, "q")

    def save_worksheet(self, sql: object) -> dict[str, str]:
        return self._save(sql, "w")

    @staticmethod
    def _reference(value: object) -> str:
        if isinstance(value, str) and _SAVED_ID.fullmatch(value):
            return value
        if not isinstance(value, str):
            raise ValueError("saved query reference is invalid")
        query = parse_qs(urlparse(value).query)
        values = query.get("query", [])
        if len(values) != 1:
            raise ValueError("saved query reference is invalid")
        return values[0]

    def _read(self, saved_query_id: str) -> dict[str, str]:
        kind, _ = self._id(saved_query_id)
        try:
            if kind == "q":
                sql = self._path(saved_query_id).read_text(encoding="utf-8")
                return {"saved_query_id": saved_query_id, "kind": "query", "sql": sql}
            value = json.loads(self._path(saved_query_id).read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError("saved query is unavailable") from error
        if not isinstance(value, dict) or set(value) != {"sql"} or not isinstance(value["sql"], str):
            raise ValueError("saved query is unavailable")
        return {"saved_query_id": saved_query_id, "kind": "worksheet", "sql": value["sql"]}

    def load(self, reference: object) -> dict[str, str]:
        return self._read(self._reference(reference))

    def list(self, limit: object = 20) -> dict[str, list[dict[str, str]]]:
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 1000:
            raise ValueError("limit must be an integer from 1 to 1000")
        if not self._directory.is_dir():
            return {"items": []}
        candidates: list[tuple[float, Path]] = []
        for path in self._directory.iterdir():
            match = _SAVED_FILE.fullmatch(path.name)
            if match is None or (match.group("id")[0] == "q") != (match.group("extension") == "sql"):
                print(f"saved query skipped: {path}: invalid filename", file=sys.stderr)
                continue
            try:
                candidates.append((path.stat().st_mtime, path))
            except OSError as error:
                print(f"saved query skipped: {path}: {error}", file=sys.stderr)
        items: list[dict[str, str]] = []
        for _saved_at, path in sorted(candidates, key=lambda value: value[0], reverse=True):
            saved_query_id = path.stem
            try:
                value = self._read(saved_query_id)
                saved_at = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.UTC).isoformat()
            except (ValueError, OSError) as error:
                print(f"saved query skipped: {path}: {error}", file=sys.stderr)
                continue
            items.append({
                "saved_query_id": value["saved_query_id"],
                "kind": value["kind"],
                "preview": " ".join(value["sql"].split()),
                "saved_at": saved_at,
            })
            if len(items) == limit:
                break
        return {"items": items}
