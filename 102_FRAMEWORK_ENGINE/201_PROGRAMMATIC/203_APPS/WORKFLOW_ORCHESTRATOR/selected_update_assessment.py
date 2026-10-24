"""Update-identity assessment and receipt matching for selected Workflows."""

from __future__ import annotations

from collections.abc import Callable, Mapping
from typing import Any, Protocol


Action = Callable[..., Mapping[str, Any]]


class LifecycleIntents(Protocol):
    """The fixed native Action surface used by lifecycle dispatch."""

    create_atom_action: Action
    update_atom_action: Action
    replace_atom_action: Action
    change_status_atom_action: Action
    move_atom_action: Action
    update_assessment_seal: Action


def admitted_update_assessment(
    lifecycle_intents: LifecycleIntents, context: Mapping[str, Any]
) -> dict[str, Any] | None:
    """Accept exactly one same-session terminal O145 assessment."""
    prior_results = context.get("lifecycle_prior_results")
    if not isinstance(prior_results, list):
        return None
    seal = lifecycle_intents.update_assessment_seal(context["parameters"])
    digest = seal["request_digest"]
    matches = [
        dict(assessment)
        for prior in prior_results
        if _matches_update_assessment(prior, digest)
        for native in [prior["native_result"]]
        for assessment in [native.get("assessment")]
        if isinstance(assessment, Mapping)
    ]
    return matches[0] if len(matches) == 1 else None


def _matches_update_assessment(prior: object, digest: object) -> bool:
    if not isinstance(prior, Mapping):
        return False
    native = prior.get("native_result")
    receipt = prior.get("completed_receipt")
    if (
        prior.get("step_definition_id") != "CA-O-145"
        or prior.get("action_definition_id") != "CA-O-067"
        or prior.get("result") != "identity-preserving"
        or not isinstance(native, Mapping)
        or not isinstance(receipt, Mapping)
    ):
        return False
    assessment = native.get("assessment")
    return (
        receipt.get("disposition") == "terminal"
        and receipt.get("outcome") == "completed"
        and isinstance(assessment, Mapping)
        and assessment.get("request_digest") == digest
    )


def assess_update_identity(
    lifecycle_intents: LifecycleIntents, context: Mapping[str, Any]
) -> dict[str, Any]:
    """Execute CA-O-067's read-only assessment before the O145 edge."""
    result = dict(
        lifecycle_intents.update_atom_action(
            context["project_root"],
            context["parameters"],
            execute=False,
            authorized=True,
        )
    )
    outcome = result.get("outcome")
    if outcome == "replace_handoff":
        return _assessment_result("replacement-required", result)
    if outcome not in {"preview", "no-op"}:
        return _assessment_result(str(outcome or "blocked"), result)
    evidence = result.get("assessment_evidence")
    if not isinstance(evidence, Mapping):
        return _assessment_result("unresolved", result)
    result["assessment"] = lifecycle_intents.update_assessment_seal(context["parameters"], evidence)
    return {"result": "identity-preserving", "effect_refs": [], "native_result": result}


def _assessment_result(result: str, native_result: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "result": result,
        "terminal_outcome": "interrupted_pending",
        "effect_refs": [],
        "native_result": native_result,
    }
