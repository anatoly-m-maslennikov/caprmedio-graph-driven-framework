"""Source-bound validation primitives for the current shared Workflow packet."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
import re
import tomllib
from typing import Any

from selected_execution_contracts import SelectedExecutionError
from selected_graph_sources import manifest_relative_path, safe_definition_path, validate_definition


CURRENT_ACTIONS = {
    "CA-O-231": "CA-O-017",
    "CA-O-232": "CA-O-018",
    "CA-O-233": "CA-O-019",
    "CA-O-094": "CA-O-020",
    "CA-O-234": "CA-O-089",
    "CA-O-096": "CA-O-024",
    "CA-O-099": "CA-O-021",
    "CA-O-230": "CA-O-225",
}

# Keep the reviewed O016 compatibility boundary in one place.  O016@17 is the
# retained legacy projection profile; O016@18 and the reviewed metadata-only
# O016@20 source are direct-Methods profiles.  A newer or unknown revision is
# never admitted merely because it is numerically newer.
WORKFLOW_VERSION_PROFILES = {
    17: "legacy_projection",
    18: "direct_methods",
    20: "direct_methods",
}
CURRENT_WORKFLOW_VERSIONS = frozenset(WORKFLOW_VERSION_PROFILES)
CURRENT_DIRECT_WORKFLOW_VERSIONS = frozenset(
    version
    for version, profile in WORKFLOW_VERSION_PROFILES.items()
    if profile == "direct_methods"
)


def workflow_version_profile(value: object) -> str | None:
    """Return the explicitly reviewed O016 profile for one exact version."""

    return WORKFLOW_VERSION_PROFILES.get(value) if type(value) is int else None


def is_direct_integrated_version(value: object) -> bool:
    """Whether one reviewed O016 version admits the direct Integrated path."""

    return workflow_version_profile(value) == "direct_methods"


@dataclass(frozen=True)
class ProjectSourceScope:
    """The selected Project's configured control-root and Atom prefix."""

    root: str
    prefix: str


class SharedContextPacketError(ValueError):
    """A caller-visible malformed, stale, or unauthorized packet condition."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


def project_source_scope(root: Path) -> ProjectSourceScope:
    """Read the one configured Project source root and identity prefix."""
    try:
        manifest = Path(manifest_relative_path(root))
        control = manifest.parents[1]
        settings = safe_definition_path(
            root, (control / "caprmedio_project_settings.toml").as_posix()
        )
        document = tomllib.loads(settings.read_bytes().decode("utf-8"))
        artifacts = document.get("artifacts")
        identity = artifacts.get("identity") if isinstance(artifacts, Mapping) else None
        prefix = identity.get("project_prefix") if isinstance(identity, Mapping) else None
        if not isinstance(prefix, str) or re.fullmatch(r"[A-Za-z0-9]+", prefix) is None:
            raise ValueError("Project Atom prefix is invalid")
    except (OSError, UnicodeError, ValueError, SelectedExecutionError) as error:
        raise SharedContextPacketError(
            "project_artifact", "Project settings are unavailable"
        ) from error
    return ProjectSourceScope(control.as_posix(), prefix)


def is_current_shared_workflow_profile(value: object) -> bool:
    """Recognize the reviewed O016@17, O016@18, or O016@20 profile shape."""
    if not isinstance(value, Mapping) or value.get("entry_step") != "CA-O-231":
        return False
    workflow, steps = value.get("workflow"), value.get("steps")
    if not isinstance(workflow, Mapping) or workflow.get("atom_id") != "CA-O-016":
        return False
    if workflow_version_profile(workflow.get("version")) is None or not isinstance(steps, Mapping):
        return False
    if set(steps) != set(CURRENT_ACTIONS):
        return False
    return all(
        isinstance(row, Mapping)
        and isinstance(row.get("step"), Mapping)
        and isinstance(row.get("action"), Mapping)
        and row["step"].get("atom_id") == step_id
        and row["action"].get("atom_id") == action_id
        for step_id, action_id in CURRENT_ACTIONS.items()
        for row in (steps[step_id],)
    )


def _definition(root: Path, value: object, kind: str) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise SharedContextPacketError("definition", f"current {kind} binding is missing")
    normalized = dict(value)
    if "source_path" in normalized and "digest" not in normalized:
        normalized["digest"] = normalized.get("sha256")
    try:
        return validate_definition(root, normalized, expected_kind=kind)
    except (OSError, UnicodeError, SelectedExecutionError) as error:
        raise SharedContextPacketError("definition", str(error)) from error


def validated_context(
    root: Path,
    profile: object,
    workflow_definition: object,
    step_definition: object,
    action_definition: object,
) -> tuple[str, str, tuple[dict[str, Any], ...]]:
    """Validate trusted O016 pins and reject every legacy or caller-selected Step."""
    if not is_current_shared_workflow_profile(profile):
        raise SharedContextPacketError("profile", "trusted current Workflow profile is invalid")
    assert isinstance(profile, Mapping)
    workflow = _definition(root, profile["workflow"], "workflow")
    supplied_workflow = _definition(root, workflow_definition, "workflow")
    if supplied_workflow != workflow:
        raise SharedContextPacketError(
            "workflow", "supplied Workflow differs from trusted O016 pin"
        )
    assert isinstance(profile["steps"], Mapping)
    step_id = _definition(root, step_definition, "step")["atom_id"]
    if step_id not in CURRENT_ACTIONS:
        raise SharedContextPacketError("step", "current Workflow does not admit this Step")
    row = profile["steps"][step_id]
    assert isinstance(row, Mapping)
    step = _definition(root, row["step"], "step")
    action = _definition(root, row["action"], "action")
    supplied_action = _definition(root, action_definition, "action")
    if _definition(root, step_definition, "step") != step or supplied_action != action:
        raise SharedContextPacketError("step_action", "Step or Action differs from trusted profile")
    pins = [workflow]
    for current_step in CURRENT_ACTIONS:
        entry = profile["steps"][current_step]
        assert isinstance(entry, Mapping)
        pins.extend(
            (_definition(root, entry["step"], "step"), _definition(root, entry["action"], "action"))
        )
    return step_id, action["atom_id"], tuple(pins)


def validate_source_bindings(
    root: Path, value: object, expected: tuple[dict[str, Any], ...]
) -> None:
    if not isinstance(value, list) or len(value) != len(expected):
        raise SharedContextPacketError("source_bindings", "current source bindings are incomplete")
    expected_by_id = {row["atom_id"]: row for row in expected}
    actual: dict[str, dict[str, Any]] = {}
    for row in value:
        if not isinstance(row, Mapping) or not isinstance(row.get("atom_id"), str):
            raise SharedContextPacketError("source_bindings", "current source binding is invalid")
        target = expected_by_id.get(row["atom_id"])
        if target is None or row["atom_id"] in actual:
            raise SharedContextPacketError(
                "source_bindings", "current source binding is not trusted"
            )
        try:
            actual[row["atom_id"]] = _definition(root, row, str(target["kind"]))
        except SharedContextPacketError as error:
            raise SharedContextPacketError("source_bindings", str(error)) from error
    if actual != expected_by_id:
        raise SharedContextPacketError("source_bindings", "current source bindings are stale")
