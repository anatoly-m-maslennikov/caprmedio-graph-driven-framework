"""Strict caller and replaceable Agent adapter boundaries."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-413

import json
from typing import Any, Literal, Self
from pydantic import BaseModel, ConfigDict, Field, model_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class Selected(Strict):
    atom_id: str = Field(min_length=1, max_length=256)
    path: str = Field(min_length=1)


class Enqueue(Strict):
    operation: Literal["enqueue"] = "enqueue"
    workflow_id: Literal["CA-O-104"] = "CA-O-104"
    run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
    selection: list[Selected] = Field(max_length=10000)
    criteria_paths: list[str] = Field(min_length=1, max_length=1000)
    author: str = Field(min_length=1)
    journal_author: str | None = Field(default=None, pattern=r"^[A-Za-z0-9][A-Za-z0-9-]{0,38}$")
    scope: str = Field(min_length=1)
    confidence_threshold: float = Field(default=90.0, ge=0, le=100)
    allow_fixes: bool = False
    allow_replacements: bool = False
    agent_timeout_seconds: int = Field(default=600, ge=1, le=3600)

    @model_validator(mode="after")
    def replacement_permission(self) -> Self:
        if self.allow_replacements and not self.allow_fixes:
            raise ValueError("allow_replacements requires allow_fixes=true")
        return self


class EnqueueSelected(Strict):
    """Tagged APPS queue request; shared RUN_SUPPORT owns inner request semantics."""

    operation: Literal["enqueue_selected"] = "enqueue_selected"
    run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
    execution: dict[str, Any]

    @model_validator(mode="after")
    def selected_execution_is_present(self) -> Self:
        if not self.execution:
            raise ValueError("execution is required")
        return self


class IntegratedActionResult(Strict):
    """The exact result envelope returned by one pending Integrated Action."""

    result: str = Field(min_length=1, max_length=128)
    outputs: dict[str, Any]
    evidence: list[Any]
    blockers: list[str]

    @model_validator(mode="after")
    def json_safe(self) -> Self:
        try:
            json.dumps(self.model_dump(), allow_nan=False)
        except (TypeError, ValueError) as error:
            raise ValueError("Integrated result must be JSON-safe") from error
        return self


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431, CA-M-413
class SubmitResult(Strict):
    """One source-bound response to a retained Integrated Action capture."""

    operation: Literal["submit_result"] = "submit_result"
    run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
    action_run_id: str = Field(min_length=1, max_length=256)
    continuation_id: str = Field(pattern=r"^[0-9a-f]{64}$")
    result: IntegratedActionResult


class Status(Strict):
    operation: Literal["status"] = "status"
    run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")


class AgentOutput(Strict):
    report_json: str
    candidate_content: str | None
    confidence: float = Field(ge=0, le=100)
