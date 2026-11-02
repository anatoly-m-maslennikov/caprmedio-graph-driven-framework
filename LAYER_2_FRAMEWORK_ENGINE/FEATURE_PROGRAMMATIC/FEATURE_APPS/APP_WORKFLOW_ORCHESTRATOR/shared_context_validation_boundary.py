"""The narrow Pydantic boundary for untrusted shared-context packets."""

from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict


class SharedContextPacketBoundary(BaseModel):
    """Type the closed current O016 packet envelope at its untrusted boundary."""

    model_config = ConfigDict(extra="forbid", strict=True)

    context: Literal["Integrated"]
    selected_project: dict[str, Any]
    source_bindings: list[dict[str, Any]]
    requirements: list[dict[str, Any]]
    delivery: list[dict[str, Any]]
    evaluations: list[dict[str, Any]]
    methods: list[dict[str, Any]] | None = None
    method_projection: dict[str, Any] | None = None
    permissions: dict[str, Any]
    retry: dict[str, Any]
    workspace: str | None = None
    candidate: str | dict[str, Any]
    phase: str | dict[str, Any]
    owned_paths: list[str]
    plan_item: dict[str, Any] | None = None
    red: dict[str, Any]
    golden_e2e: list[str]
    baseline_command: str
    confidence: dict[str, Any]
    coverage: dict[str, Any]
    retained_state: dict[str, Any]
    step_marker: str
    step_binding: dict[str, Any]
    action_binding: dict[str, Any]
    prior_results: list[dict[str, Any]] = []
    review_phase: Literal["preliminary", "final"] | None = None
    required_obligation_map: dict[str, list[str]] | None = None
    operator_authorization: dict[str, Any] | None = None
