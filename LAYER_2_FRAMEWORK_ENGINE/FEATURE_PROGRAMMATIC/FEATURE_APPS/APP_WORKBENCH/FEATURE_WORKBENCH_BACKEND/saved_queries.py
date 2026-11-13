# CA-R-2776@10
# CA-M-470@13
# CA-D-673@15

"""Project-Journal saved SQL with read-only legacy-file fallback."""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
import re
import sys
from typing import Any
from urllib.parse import parse_qs, urlparse
import uuid


TOOLS = Path(__file__).resolve().parents[3] / "FEATURE_TOOLS"
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from work_journal import append_sealed_events, configured_journal_root  # noqa: E402


_LEGACY_ID = re.compile(r"^(?P<kind>[qw])_(?P<token>[0-9a-f]{32})$")
_LEGACY_FILE = re.compile(r"^(?P<id>[qw]_[0-9a-f]{32})\.(?P<extension>sql|json)$")
_JOURNAL_AUTHOR = "workbench-saved-items"


class SavedQueryStore:
    """Own saved items under one Project's Journal and legacy runtime files."""

    def __init__(self, root: Path) -> None:
        self._root = Path(root)
        self._legacy_directory = self._root / ".caprmedio_runtime" / "workbench" / "saved_queries"

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
    def _name(value: object) -> str | None:
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError("name must be a string")
        if not value.strip():
            return None
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as error:
            raise ValueError("name must be valid UTF-8") from error
        return value

    @staticmethod
    def _uuid7(value: object) -> str:
        if not isinstance(value, str):
            raise ValueError("saved query reference is invalid")
        try:
            parsed = uuid.UUID(value)
        except ValueError as error:
            raise ValueError("saved query reference is invalid") from error
        if parsed.version != 7 or str(parsed) != value:
            raise ValueError("saved query reference is invalid")
        return value

    @staticmethod
    def _legacy_id(value: object) -> tuple[str, str]:
        if not isinstance(value, str):
            raise ValueError("saved query reference is invalid")
        match = _LEGACY_ID.fullmatch(value)
        if match is None:
            raise ValueError("saved query reference is invalid")
        return match.group("kind"), value

    def _legacy_path(self, saved_query_id: str) -> Path:
        kind, value = self._legacy_id(saved_query_id)
        return self._legacy_directory / f"{value}.{'sql' if kind == 'q' else 'json'}"

    @staticmethod
    def _now() -> str:
        return dt.datetime.now(dt.UTC).isoformat()

    def _record(self, sql: object, kind: str, name: object) -> dict[str, Any]:
        value, saved_name, saved_at = self._sql(sql), self._name(name), self._now()
        record: dict[str, Any] = {
            "saved_query_id": str(uuid.uuid7()),
            "kind": kind,
            "sql": value,
            "saved_at": saved_at,
        }
        if saved_name is not None:
            record["name"] = saved_name
        try:
            append_sealed_events(
                self._root,
                [record],
                author=_JOURNAL_AUTHOR,
                local_date=saved_at[:10],
                timezone="UTC",
            )
        except Exception as error:
            raise ValueError(f"saved query failed: {error}") from error
        return record

    def save_query(self, sql: object, name: object = None) -> dict[str, Any]:
        return self._record(sql, "query", name)

    def save_view(self, sql: object, name: object = None) -> dict[str, Any]:
        return self._record(sql, "view", name)

    @staticmethod
    def _reference(value: object) -> str:
        if isinstance(value, str) and (_LEGACY_ID.fullmatch(value) or _is_uuid7(value)):
            return value
        if not isinstance(value, str):
            raise ValueError("saved query reference is invalid")
        values = parse_qs(urlparse(value).query).get("query", [])
        if len(values) != 1:
            raise ValueError("saved query reference is invalid")
        return values[0]

    def _journal_paths(self) -> list[Path]:
        directory = self._root / configured_journal_root(self._root)
        if not directory.is_dir():
            return []
        return sorted(directory.glob(f"{_JOURNAL_AUTHOR}-*-part-*.ndjson"))

    @staticmethod
    def _journal_record(value: object) -> dict[str, Any]:
        if not isinstance(value, dict):
            raise ValueError("saved query record is invalid")
        keys = set(value)
        expected = {"saved_query_id", "kind", "sql", "saved_at"}
        if keys not in (expected, expected | {"name"}):
            raise ValueError("saved query record is invalid")
        saved_query_id = SavedQueryStore._uuid7(value["saved_query_id"])
        if not isinstance(value["kind"], str) or value["kind"] not in {"query", "view", "worksheet"}:
            raise ValueError("saved query record is invalid")
        if not isinstance(value["saved_at"], str):
            raise ValueError("saved query record is invalid")
        record = {
            "saved_query_id": saved_query_id,
            "kind": "view" if value["kind"] == "worksheet" else value["kind"],
            "sql": SavedQueryStore._sql(value["sql"]),
            "saved_at": value["saved_at"],
        }
        name = SavedQueryStore._name(value.get("name"))
        if name is not None:
            record["name"] = name
        return record

    def _journal_items(self) -> list[dict[str, Any]]:
        items: list[dict[str, Any]] = []
        for path in self._journal_paths():
            try:
                lines = path.read_text(encoding="utf-8").splitlines()
            except (OSError, UnicodeError) as error:
                print(f"saved query skipped: {path}: {error}", file=sys.stderr)
                continue
            for line_number, line in enumerate(lines, 1):
                try:
                    items.append(self._journal_record(json.loads(line)))
                except (ValueError, json.JSONDecodeError) as error:
                    print(f"saved query skipped: {path}:{line_number}: {error}", file=sys.stderr)
        return items

    def _legacy_read(self, saved_query_id: str) -> dict[str, Any]:
        kind, _ = self._legacy_id(saved_query_id)
        try:
            if kind == "q":
                sql = self._legacy_path(saved_query_id).read_text(encoding="utf-8")
                return {"saved_query_id": saved_query_id, "kind": "query", "sql": sql}
            value = json.loads(self._legacy_path(saved_query_id).read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError("saved query is unavailable") from error
        if not isinstance(value, dict) or set(value) != {"sql"} or not isinstance(value["sql"], str):
            raise ValueError("saved query is unavailable")
        return {"saved_query_id": saved_query_id, "kind": "view", "sql": value["sql"]}

    def load(self, reference: object) -> dict[str, Any]:
        saved_query_id = self._reference(reference)
        if _LEGACY_ID.fullmatch(saved_query_id):
            return self._legacy_read(saved_query_id)
        for record in self._journal_items():
            if record["saved_query_id"] == saved_query_id:
                return record
        raise ValueError("saved query is unavailable")

    def _legacy_items(self) -> list[dict[str, Any]]:
        if not self._legacy_directory.is_dir():
            return []
        items: list[dict[str, Any]] = []
        for path in self._legacy_directory.iterdir():
            match = _LEGACY_FILE.fullmatch(path.name)
            if match is None or (match.group("id")[0] == "q") != (match.group("extension") == "sql"):
                print(f"saved query skipped: {path}: invalid filename", file=sys.stderr)
                continue
            try:
                item = self._legacy_read(path.stem)
                item["saved_at"] = dt.datetime.fromtimestamp(path.stat().st_mtime, tz=dt.UTC).isoformat()
                items.append(item)
            except (ValueError, OSError) as error:
                print(f"saved query skipped: {path}: {error}", file=sys.stderr)
        return items

    def list(self, limit: object = 20) -> dict[str, list[dict[str, Any]]]:
        if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= 1000:
            raise ValueError("limit must be an integer from 1 to 1000")
        items = self._journal_items() + self._legacy_items()
        items.sort(key=lambda item: item["saved_at"], reverse=True)
        return {"items": [
            {
                "saved_query_id": item["saved_query_id"],
                "kind": item["kind"],
                "preview": " ".join(item["sql"].split())[:150],
                "saved_at": item["saved_at"],
            }
            | ({"name": item["name"]} if "name" in item else {})
            for item in items[:limit]
        ]}


def _is_uuid7(value: str) -> bool:
    try:
        parsed = uuid.UUID(value)
    except ValueError:
        return False
    return parsed.version == 7 and str(parsed) == value
