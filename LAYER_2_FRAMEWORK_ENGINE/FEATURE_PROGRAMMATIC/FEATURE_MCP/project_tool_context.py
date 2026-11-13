# CA-R-1113@23
# CA-M-175@19
# CA-D-593@17
# CA-M-512@2

"""Validate the optional single-Project MCP envelope without selecting Projects."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from project_selection import ProjectSelection


def native_arguments(arguments: Any, selection: ProjectSelection | None, root: Path) -> Any:
    """Accept only the bound host/container root, then remove the outer assertion."""
    if not isinstance(arguments, dict) or "project_root" not in arguments:
        return arguments
    value = arguments["project_root"]
    if not isinstance(value, str) or not value or "\x00" in value:
        raise ValueError("project_root must be a canonical bound Project root")
    try:
        path = Path(value)
    except (TypeError, ValueError) as error:
        raise ValueError("project_root must be a canonical bound Project root") from error
    if not path.is_absolute() or ".." in path.parts or path.as_posix() != value:
        raise ValueError("project_root must be a canonical bound Project root")
    allowed = {str(root)} if selection is None else {str(selection.root)} | (
        {str(selection.host_root)} if selection.host_root is not None else set()
    )
    if value not in allowed:
        raise ValueError("project_root does not match the bound Project")
    return {key: item for key, item in arguments.items() if key != "project_root"}


__all__ = ["native_arguments"]
