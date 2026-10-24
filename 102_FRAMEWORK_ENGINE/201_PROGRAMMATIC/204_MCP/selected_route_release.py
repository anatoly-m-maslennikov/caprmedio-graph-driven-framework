"""Direct release request validation and execution helpers."""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path
from typing import Any, Mapping, cast

from project_selection import bound_selection
from selected_route_spec import (
    _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME,
    _REQUEST_ID,
    SelectedRouteError,
)


def direct_release_request(root: Path, route: str, request: Any) -> dict[str, Any]:
    required = {"project_root", "run_id"}
    allowed = required | (
        {"content_draft"} if route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME else set()
    )
    if not isinstance(request, Mapping) or not required <= set(request) <= allowed:
        raise SelectedRouteError(
            "request requires only project_root and run_id, plus optional public content_draft"
        )
    run_id = request["run_id"]
    pattern = (
        _REQUEST_ID
        if route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME
        else re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]*\Z")
    )
    if not isinstance(run_id, str) or not pattern.fullmatch(run_id):
        raise SelectedRouteError("run_id is invalid")
    public = sys.modules.get("selected_routes")
    selection_lookup = (
        getattr(public, "bound_selection", bound_selection) if public else bound_selection
    )
    selection = selection_lookup(root)
    expected = (
        selection.host_root if selection is not None and selection.host_root is not None else root
    )
    if request["project_root"] != str(expected):
        raise SelectedRouteError("project_root does not match the bound Project root")
    if "content_draft" in request:
        draft = request["content_draft"]
        if (
            not isinstance(draft, Mapping)
            or set(draft) != {"description", "summary"}
            or not isinstance(draft["description"], str)
            or not isinstance(draft["summary"], list)
            or not all(isinstance(item, str) for item in draft["summary"])
        ):
            raise SelectedRouteError("content_draft is invalid")
    return dict(request)


def direct_release_call(root: Path, route: str, request: Mapping[str, Any]) -> dict[str, Any]:
    public = route == _OPTIONAL_PUBLIC_RELEASE_ROUTE_NAME
    relative = Path(
        "PROJECT_TOOLS/PUBLIC_RELEASE/public_release.py"
        if public
        else "PROJECT_TOOLS/RELEASE_VERSION/local_release.py"
    )
    current = root
    for part in relative.parts:
        current /= part
        if current.is_symlink():
            raise SelectedRouteError("Release implementation path is a symlink")
    if not current.is_file():
        raise SelectedRouteError("Release implementation is unavailable")
    spec = importlib.util.spec_from_file_location(
        "_caprmedio_direct_public_release" if public else "_caprmedio_direct_local_release", current
    )
    if spec is None or spec.loader is None:
        raise SelectedRouteError("Release implementation is unavailable")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    try:
        spec.loader.exec_module(module)
        kwargs = {"run_id": request["run_id"]}
        if public:
            kwargs["content_draft"] = request["content_draft"]
        result = getattr(module, "run_public_release" if public else "run_local_release")(
            root, **kwargs
        )
    finally:
        sys.modules.pop(spec.name, None)
    if not isinstance(result, Mapping):
        raise SelectedRouteError("Release returned an invalid result")
    return dict(result)


def direct_release_record(
    root: Path,
    route: str,
    request: Mapping[str, Any],
    event: str,
    preceding: str | None,
    outcome: str | None = None,
) -> tuple[str | None, str | None]:
    try:
        from work_journal import append_record, event_record

        record = event_record(
            root=root,
            event=event,
            action_id=request["run_id"],
            kind="workflow",
            scope="project",
            operation=route,
            session_id=request["run_id"],
            subjects=[],
            outputs=[],
            preceding_event=preceding,
            details={"outcome": outcome} if outcome is not None else {},
        )
        append_record(root, record)
        return cast(str | None, record.get("event_id")), None
    except (ImportError, OSError, RuntimeError, TypeError, ValueError) as error:
        return None, f"Release {event} recording failed: {error}"
