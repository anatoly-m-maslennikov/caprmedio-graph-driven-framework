# CA-R-2792@3
# CA-R-2793@3
# CA-R-2902@5
# CA-M-476@4
# CA-D-681@8

"""Persistent Workspace documents; result tables remain process-local."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any
import uuid


class WorkspaceStore:
    """Own one Project's small Workspace documents, never query-result rows."""

    def __init__(self, root: Path) -> None:
        self._root = Path(root)
        self._directory = self._root / ".caprmedio_runtime" / "workbench" / "workspaces"

    @staticmethod
    def text(value: object, field: str, *, required: bool = True) -> str | None:
        if value is None and not required:
            return None
        if not isinstance(value, str) or required and not value.strip():
            raise ValueError(f"{field} must be a non-empty string" if required else f"{field} must be a string")
        try:
            value.encode("utf-8")
        except UnicodeEncodeError as error:
            raise ValueError(f"{field} must be valid UTF-8") from error
        return value

    @staticmethod
    def cursor(value: object) -> int:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("cursor_position must be a non-negative integer")
        return value

    @staticmethod
    def revision(value: object) -> int:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("expected_revision must be a non-negative integer")
        return value

    def _path(self, workspace_id: str) -> Path:
        return self._directory / f"{hashlib.sha256(workspace_id.encode()).hexdigest()}.json"

    def _write(self, document: dict[str, Any]) -> None:
        self._directory.mkdir(parents=True, exist_ok=True)
        path = self._path(document["workspace_id"])
        temporary = path.with_suffix(".tmp")
        temporary.write_text(json.dumps(document, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
        temporary.replace(path)

    def _read(self, workspace_id: object) -> dict[str, Any]:
        value = self.text(workspace_id, "workspace_id")
        assert isinstance(value, str)
        try:
            document = json.loads(self._path(value).read_text(encoding="utf-8"))
        except FileNotFoundError as error:
            raise ValueError("unknown workspace_id") from error
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            raise ValueError("workspace is unavailable") from error
        if not isinstance(document, dict) or document.get("workspace_id") != value or not isinstance(document.get("views"), list) or not document["views"]:
            raise ValueError("workspace is unavailable")
        return document

    @staticmethod
    def _view(document: dict[str, Any], view_id: object) -> dict[str, Any]:
        if not isinstance(view_id, str) or not view_id:
            raise ValueError("view_id must be a non-empty string")
        for view in document["views"]:
            if isinstance(view, dict) and view.get("id") == view_id:
                return view
        raise ValueError("unknown view_id")

    @staticmethod
    def _public_view(view: dict[str, Any], sql: bool) -> dict[str, Any]:
        value = {key: view[key] for key in ("id", "cursor_position", "revision")}
        if "name" in view:
            value["name"] = view["name"]
        if sql:
            value["sql"] = view["sql"]
        if "result" in view:
            value["result"] = dict(view["result"])
        return value

    def _state(self, document: dict[str, Any]) -> dict[str, Any]:
        return {
            "workspace_id": document["workspace_id"], "project_root": document["project_root"],
            "active_view_id": document["active_view_id"],
            "views": [self._public_view(view, True) for view in document["views"]],
        }

    def open(self, session_id: object) -> dict[str, Any]:
        workspace_id = self.text(session_id, "session_id")
        try:
            return self._state(self._read(workspace_id))
        except ValueError as error:
            if str(error) != "unknown workspace_id":
                raise
        view_id = str(uuid.uuid7())
        document = {"workspace_id": workspace_id, "project_root": str(self._root), "active_view_id": view_id,
                    "views": [{"id": view_id, "sql": "", "cursor_position": 0, "revision": 0}]}
        self._write(document)
        return self._state(document)

    def get(self, workspace_id: object) -> dict[str, Any]:
        return self._state(self._read(workspace_id))

    def list(self) -> dict[str, list[dict[str, str]]]:
        if not self._directory.is_dir():
            return {"items": []}
        ids: list[str] = []
        for path in self._directory.glob("*.json"):
            try:
                value = json.loads(path.read_text(encoding="utf-8"))
                if isinstance(value, dict) and isinstance(value.get("workspace_id"), str) and value["workspace_id"]:
                    ids.append(value["workspace_id"])
            except (OSError, UnicodeError, json.JSONDecodeError):
                continue
        return {"items": [{"workspace_id": value} for value in sorted(ids)]}

    def create(self, workspace_id: object, position: object, name: object) -> dict[str, Any]:
        if position not in {"first", "last"}:
            raise ValueError("position must be first or last")
        document = self._read(workspace_id)
        view_id = str(uuid.uuid7())
        view: dict[str, Any] = {"id": view_id, "sql": "", "cursor_position": 0, "revision": 0}
        value = self.text(name, "name", required=False)
        if value is not None and value.strip():
            view["name"] = value
        document["views"].insert(0 if position == "first" else len(document["views"]), view)
        document["active_view_id"] = view_id
        self._write(document)
        return self._state(document) | {"view_id": view_id}

    def duplicate(self, workspace_id: object, view_id: object) -> dict[str, Any]:
        document = self._read(workspace_id)
        source = self._view(document, view_id)
        source_index = document["views"].index(source)
        display_names = {
            view.get("name") if isinstance(view.get("name"), str) and view["name"].strip()
            else f"View {index + 1}"
            for index, view in enumerate(document["views"])
        }
        base_name = source.get("name") if isinstance(source.get("name"), str) and source["name"].strip() else f"View {source_index + 1}"
        suffix = 1
        while f"{base_name}({suffix})" in display_names:
            suffix += 1
        view_id = str(uuid.uuid7())
        duplicate = {
            "id": view_id,
            "sql": source["sql"],
            "cursor_position": source["cursor_position"],
            "revision": 0,
            "name": f"{base_name}({suffix})",
        }
        document["views"].insert(source_index + 1, duplicate)
        document["active_view_id"] = view_id
        self._write(document)
        return self._state(document) | {"view_id": view_id}

    def list_views(self, workspace_id: object) -> dict[str, Any]:
        document = self._read(workspace_id)
        return {"workspace_id": document["workspace_id"], "active_view_id": document["active_view_id"],
                "views": [self._public_view(view, False) for view in document["views"]]}

    def get_view(self, workspace_id: object, view_id: object) -> dict[str, Any]:
        document = self._read(workspace_id)
        view = self._view(document, view_id)
        return {"workspace_id": document["workspace_id"], "view_id": view["id"]} | self._public_view(view, True)

    def update(
        self, workspace_id: object, view_id: object, sql: object,
        expected_revision: object, cursor: object,
    ) -> dict[str, Any]:
        text = self.text(sql, "sql", required=False)
        if text is None:
            raise ValueError("sql must be a string")
        document = self._read(workspace_id)
        view = self._view(document, view_id)
        if view["revision"] != self.revision(expected_revision):
            raise ValueError("expected_revision does not match")
        view["sql"], view["revision"] = text, view["revision"] + 1
        if cursor is not None:
            view["cursor_position"] = self.cursor(cursor)
        self._write(document)
        return self.get_view(workspace_id, view_id)

    @staticmethod
    def _clear(view: dict[str, Any]) -> str | None:
        result = view.pop("result", None)
        query_id = result.get("query_id") if isinstance(result, dict) else None
        return query_id if isinstance(query_id, str) else None

    def clear_result(self, workspace_id: object, view_id: object) -> tuple[dict[str, Any], str | None]:
        document = self._read(workspace_id)
        view = self._view(document, view_id)
        prior = self._clear(view)
        self._write(document)
        return self.get_view(workspace_id, view_id), prior

    def set_result(self, workspace_id: object, view_id: object, result: dict[str, Any]) -> dict[str, Any]:
        document = self._read(workspace_id)
        self._view(document, view_id)["result"] = result
        self._write(document)
        return self.get_view(workspace_id, view_id)

    def focus(self, workspace_id: object, view_id: object) -> dict[str, str]:
        document = self._read(workspace_id)
        document["active_view_id"] = self._view(document, view_id)["id"]
        self._write(document)
        return {"workspace_id": document["workspace_id"], "active_view_id": document["active_view_id"]}

    def rename(self, workspace_id: object, view_id: object, name: object) -> dict[str, Any]:
        value = self.text(name, "name", required=False)
        if value is None:
            raise ValueError("name must be a string")
        document = self._read(workspace_id)
        view = self._view(document, view_id)
        if value.strip():
            view["name"] = value
        else:
            view.pop("name", None)
        self._write(document)
        return self.get_view(workspace_id, view_id)

    def remove(self, workspace_id: object, view_id: object) -> tuple[dict[str, Any], str | None]:
        document = self._read(workspace_id)
        if len(document["views"]) == 1:
            raise ValueError("cannot remove the last view")
        view = self._view(document, view_id)
        prior = self._clear(view)
        document["views"].remove(view)
        if document["active_view_id"] == view["id"]:
            document["active_view_id"] = document["views"][0]["id"]
        self._write(document)
        return self.list_views(workspace_id), prior

    def clear_transient_results(self) -> None:
        if not self._directory.is_dir():
            return
        for path in self._directory.glob("*.json"):
            try:
                document = json.loads(path.read_text(encoding="utf-8"))
                if not isinstance(document, dict) or not isinstance(document.get("views"), list):
                    continue
                for view in document["views"]:
                    if isinstance(view, dict):
                        view.pop("result", None)
                self._write(document)
            except (OSError, TypeError, UnicodeError, json.JSONDecodeError):
                continue
