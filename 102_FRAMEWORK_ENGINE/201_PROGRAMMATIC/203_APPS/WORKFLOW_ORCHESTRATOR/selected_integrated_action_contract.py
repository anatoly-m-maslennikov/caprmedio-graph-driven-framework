"""Prompt and response contracts for the current Integrated Action bridge."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
import copy
import hashlib
import json
from pathlib import Path
import re
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[4]
PROMPT_ROOT = (
    ROOT / "102_FRAMEWORK_ENGINE/202_AGENTIC/202_PROMPTS/ACTION_PROMPTS/"
    "IMPLEMENTATION_WORKFLOW/SHARED_CONTEXT"
)
_RESULT_BLOCK = re.compile(r"Results:\s*(.*?)(?:\n\n|\Z)", re.DOTALL)
_LABEL = re.compile(r"`([a-z_]+)`")
CORE_FIELDS = frozenset({"result", "outputs", "evidence", "blockers"})


def _frontier() -> dict[str, Any]:
    path = PROMPT_ROOT / "definition_frontier.projection.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if value.get("kind") != "definition_only_source_frontier":
        raise ValueError("current Integrated Action frontier is invalid")
    steps = value.get("steps")
    if not isinstance(steps, Mapping) or len(steps) != 8:
        raise ValueError("current Integrated Action frontier is incomplete")
    return cast(dict[str, Any], value)


def prompt_spec(step_id: str, action_id: str) -> dict[str, Any]:
    frontier = _frontier()
    if frontier["steps"].get(step_id) != action_id:
        raise ValueError("Step and Action are not a current Integrated binding")
    path = PROMPT_ROOT / f"{step_id}.prompt.md"
    prompt = path.read_text(encoding="utf-8")
    header = f"Step: {step_id} | Action: {action_id} | Context: Integrated"
    if not prompt.startswith(f"# System Prompt\n\n{header}\n"):
        raise ValueError("current Integrated prompt header is stale")
    match = _RESULT_BLOCK.search(prompt)
    labels = tuple(dict.fromkeys(_LABEL.findall(match.group(1)))) if match else ()
    if not labels:
        raise ValueError("current Integrated prompt has no result contract")
    schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "result": {"type": "string", "enum": list(labels)},
            "outputs": {"type": "object"},
            "evidence": {"type": "array"},
            "blockers": {"type": "array", "items": {"type": "string"}},
        },
        "required": sorted(CORE_FIELDS),
    }
    return {
        "prompt": prompt,
        "prompt_path": path.as_posix(),
        "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
        "allowed_results": labels,
        "output_schema": schema,
    }


def validate_response(
    response: object, allowed_results: Sequence[str], output_schema: Mapping[str, Any]
) -> dict[str, Any]:
    if not isinstance(response, Mapping):
        raise ValueError("Integrated Action response must be a mapping")
    if set(response) != CORE_FIELDS:
        raise ValueError("Integrated Action response has an invalid shape")
    if response.get("result") not in allowed_results:
        raise ValueError("Integrated Action result is not admitted by the current Step")
    if not isinstance(response.get("outputs"), Mapping):
        raise ValueError("Integrated Action outputs must be an object")
    if not isinstance(response.get("evidence"), list):
        raise ValueError("Integrated Action evidence must be an array")
    blockers = response.get("blockers")
    if not isinstance(blockers, list) or not all(isinstance(item, str) for item in blockers):
        raise ValueError("Integrated Action blockers must be an array of strings")
    required = output_schema.get("required", ())
    if not isinstance(required, list) or any(key not in response for key in required):
        raise ValueError("Integrated Action response misses required fields")
    return dict(response)


def validate_capture_contract(capture: Mapping[str, Any], spec: Mapping[str, Any]) -> None:
    """Reject a pending capture whose response contract was changed."""
    if (
        capture.get("allowed_results") != list(spec["allowed_results"])
        or capture.get("output_schema") != spec["output_schema"]
    ):
        raise ValueError("Integrated Action capture result contract is stale")


def build_capture(
    prompt: str,
    packet: Mapping[str, Any],
    *,
    step_id: str,
    action_id: str,
    context: str,
    allowed_results: Sequence[str],
    output_schema: Mapping[str, Any],
    prompt_path: str | None,
    prompt_sha256: str | None,
    selected_project_root: Path,
    definitions: Mapping[str, object | None],
) -> dict[str, Any]:
    return {
        "prompt": prompt,
        "prompt_path": prompt_path,
        "prompt_sha256": prompt_sha256,
        "packet": copy.deepcopy(dict(packet)),
        "step_id": step_id,
        "action_id": action_id,
        "context": context,
        "allowed_results": list(allowed_results),
        "output_schema": copy.deepcopy(dict(output_schema)),
        "selected_project_root": str(selected_project_root),
        "source_bindings": copy.deepcopy(packet.get("source_bindings", [])),
        "definitions": copy.deepcopy(dict(definitions)),
    }


# implementation of:
# Method: CA-M-405
def normalise_result(result: Mapping[str, Any], capture: Mapping[str, Any]) -> dict[str, Any]:
    from selected_integrated_action_outcome import binding_digest, validate_outcome

    packet = capture.get("packet")
    if not isinstance(packet, Mapping):
        raise ValueError("Integrated Action capture packet is invalid")
    core = {key: result.get(key) for key in CORE_FIELDS}
    response = validate_response(core, capture["allowed_results"], capture["output_schema"])
    validate_outcome(packet, response)
    result_value = dict(result)
    result_value.update(
        {
            "step": capture["step_id"],
            "action": capture["action_id"],
            "context": capture["context"],
            "source_bindings": copy.deepcopy(packet.get("source_bindings", [])),
            "retained_state": copy.deepcopy(packet.get("retained_state", {})),
            "candidate": copy.deepcopy(packet["candidate"]),
            "binding_digest": binding_digest(packet),
        }
    )
    return result_value
