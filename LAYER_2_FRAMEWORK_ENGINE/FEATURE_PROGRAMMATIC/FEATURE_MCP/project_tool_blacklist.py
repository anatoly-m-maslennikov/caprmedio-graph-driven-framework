"""Read gateway exclusions without loading a capability-discovery service."""

from pathlib import Path

from project_selection import (
    CEILINGS,
    SETTINGS_FILENAME,
    ProjectSelectionError,
    ReadContext,
    _control_candidates,
    _control_relative,
    _project_root,
    _read_toml,
    bound_selection,
)
from project_settings_schema import mcp_tool_blacklist


def project_tool_blacklist(root: str | Path) -> frozenset[str]:
    """Use startup-bound Settings, or read one local Settings carrier safely."""
    root = _project_root(root)
    selection = bound_selection(root)
    if selection is not None:
        return mcp_tool_blacklist(selection.settings)
    candidates = _control_candidates(root)
    if not candidates:
        return frozenset()
    if len(candidates) != 1:
        raise ProjectSelectionError("Project settings carrier is ambiguous")
    control = candidates[0]
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    settings = _read_toml(reader, root / control / SETTINGS_FILENAME)
    paths = settings.get("paths", {})
    if not isinstance(paths, dict):
        raise ProjectSelectionError("Invalid Project control root")
    declared = _control_relative(paths.get("control_root", control.as_posix()))
    if declared != control:
        raise ProjectSelectionError("Project Settings control_root contradicts the carrier")
    return mcp_tool_blacklist(settings)
