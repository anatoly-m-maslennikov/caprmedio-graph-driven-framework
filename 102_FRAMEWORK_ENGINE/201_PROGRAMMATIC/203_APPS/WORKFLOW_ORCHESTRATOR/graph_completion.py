"""Pure reconciliation of graph observations with executor-owned Run evidence.

This module never constructs a graph, publishes a carrier, or writes a Journal.
Completion comes from the shared executor's actual terminal Run facts.
"""
from __future__ import annotations

from collections.abc import Mapping, Sequence
from copy import deepcopy
from pathlib import PurePosixPath
import re
from typing import Any


QUALITY_KEYS = {"coverage", "fidelity", "validity", "currentness", "permission", "persistence", "recording"}
RESULT_FIELDS = {
    "outcome", "source_frontier_evidence", "selection_evidence", "source_fact_context_evidence",
    "lineage", "quality_dispositions", "diagnostics", "non_authoritative", "output_effects",
    "completion",
}


class GraphCompletionError(ValueError):
    """Retained graph evidence cannot establish the claimed recording boundary."""


def _reference(value: object) -> bool:
    return (isinstance(value, str) and bool(value) and value != "." and "\\" not in value
            and "\x00" not in value and not PurePosixPath(value).is_absolute()
            and ".." not in PurePosixPath(value).parts and PurePosixPath(value).as_posix() == value)


def _carrier(value: object) -> bool:
    return (isinstance(value, Mapping) and set(value) == {"carrier_path", "carrier_sha256"}
            and _reference(value["carrier_path"]) and isinstance(value["carrier_sha256"], str)
            and re.fullmatch(r"[0-9a-f]{64}", value["carrier_sha256"]) is not None)


def _validated(observation: object) -> dict[str, Any]:
    if not isinstance(observation, Mapping):
        raise GraphCompletionError("graph observation is unavailable")
    namespaces = set(observation) & {"entities_graph", "terms_graph"}
    if len(namespaces) != 1 or set(observation) - (RESULT_FIELDS | namespaces | {"projection_revision", "run_receipt_refs"}) or not RESULT_FIELDS <= set(observation):
        raise GraphCompletionError("graph result fields are not closed")
    quality = observation["quality_dispositions"]
    effects = observation["output_effects"]
    completion = observation["completion"]
    if observation["outcome"] not in {"built", "no_op", "incomplete", "conflicting", "stale", "blocked", "failed", "canceled"}:
        raise GraphCompletionError("graph outcome is invalid")
    if not isinstance(observation["diagnostics"], list) or any(not isinstance(row, Mapping) for row in observation["diagnostics"]):
        raise GraphCompletionError("graph diagnostics are invalid")
    if not isinstance(quality, Mapping) or set(quality) != QUALITY_KEYS or any(value not in {"pass", "fail", "unresolved", "not_applicable"} for value in quality.values()):
        raise GraphCompletionError("graph quality dispositions are invalid")
    if not isinstance(effects, Mapping) or set(effects) != {"state", "paths", "before", "after"}:
        raise GraphCompletionError("graph output evidence is invalid")
    paths = effects["paths"]
    if not isinstance(paths, list) or any(not _reference(path) for path in paths) or paths != sorted(set(paths)):
        raise GraphCompletionError("graph effect paths are invalid")
    if effects["state"] not in {"none", "created", "replaced", "unchanged", "uncertain"} or any(value is not None and not _carrier(value) for value in (effects["before"], effects["after"])):
        raise GraphCompletionError("graph before/after evidence is invalid")
    if effects["state"] in {"none", "unchanged"} and paths:
        raise GraphCompletionError("unchanged graph evidence invents changed effects")
    if effects["state"] == "none" and (effects["before"] is not None or effects["after"] is not None):
        raise GraphCompletionError("no-effect graph evidence invents output observations")
    if effects["state"] == "unchanged" and (not _carrier(effects["before"]) or effects["before"] != effects["after"]):
        raise GraphCompletionError("unchanged graph evidence does not prove preserved bytes")
    if effects["state"] in {"created", "replaced"} and (not _carrier(effects["after"]) or paths != [effects["after"]["carrier_path"]] or (effects["state"] == "created" and effects["before"] is not None) or (effects["state"] == "replaced" and not _carrier(effects["before"]))):
        raise GraphCompletionError("changed graph evidence does not prove actual bytes")
    if effects["state"] == "replaced" and (effects["before"]["carrier_path"] != effects["after"]["carrier_path"] or effects["before"] == effects["after"]):
        raise GraphCompletionError("replacement does not prove changed bytes at the same destination")
    if "projection_revision" in observation and (not _carrier(effects["after"]) or observation["projection_revision"] != effects["after"]["carrier_sha256"]):
        raise GraphCompletionError("graph revision differs from observed output bytes")
    if not isinstance(completion, Mapping) or completion.get("state") not in {"construction_only", "awaiting_terminal_recording", "recording_pending", "recorded", "completed", "blocked"}:
        raise GraphCompletionError("graph completion evidence is invalid")
    if observation["non_authoritative"] is not True:
        raise GraphCompletionError("graph result lacks its non-authoritative boundary")
    return deepcopy(dict(observation))


def construction_outcome(observation: Mapping[str, Any]) -> str:
    """Describe the observed Action, without prematurely advertising built/no_op."""
    value = _validated(observation)
    if value["outcome"] == "failed":
        return "failed"
    if value["outcome"] == "canceled":
        return "cancelled"
    ready = (value["outcome"] in {"incomplete", "built", "no_op"}
             and value["completion"]["state"] in {"construction_only", "awaiting_terminal_recording", "recording_pending", "recorded", "completed"}
             and all(value["quality_dispositions"][key] == "pass" for key in QUALITY_KEYS - {"recording"})
             and all(value[key] for key in ("source_frontier_evidence", "selection_evidence", "source_fact_context_evidence"))
             and "projection_revision" in value
             and not any(row.get("severity") == "error" for row in value["diagnostics"]))
    if ready and value["output_effects"]["state"] in {"created", "replaced", "unchanged"}:
        return "no_op" if value["output_effects"]["state"] == "unchanged" else "completed"
    return "interrupted_pending"


def finalize_graph_result(observation: Mapping[str, Any], terminal: Mapping[str, Any] | None, *,
                          action_run_id: str, result_ref: str, effect_refs: list[str],
                          receipts: Sequence[Mapping[str, Any]] = (), pending_event_id: str | None = None) -> dict[str, Any]:
    """Finish retained construction evidence from the actual terminal Run."""
    del receipts, pending_event_id
    value = _validated(observation)
    expected = construction_outcome(value)
    value.pop("run_receipt_refs", None)
    value["quality_dispositions"]["recording"] = "not_applicable"
    if effect_refs != value["output_effects"]["paths"] or not _reference(result_ref):
        raise GraphCompletionError("terminal references differ from graph observation")
    if terminal is None:
        value["completion"] = {"state": "blocked"}
        if value["outcome"] in {"built", "no_op"}:
            value["outcome"] = "incomplete"
        return value
    if (terminal.get("run_id") != action_run_id or terminal.get("outcome") != expected
            or terminal.get("result_ref") != result_ref or terminal.get("effect_refs") != effect_refs):
        raise GraphCompletionError("actual Action recording does not bind saved graph observation")
    if terminal.get("disposition") not in {"terminal", "interrupted"}:
        raise GraphCompletionError("Action completion lacks its actual terminal Run")
    if terminal["disposition"] == "interrupted":
        value["completion"] = {"state": "blocked"}
        return value
    value["completion"] = {"state": "completed"}
    if expected in {"completed", "no_op"}:
        value["outcome"] = "built" if expected == "completed" else "no_op"
    return value
