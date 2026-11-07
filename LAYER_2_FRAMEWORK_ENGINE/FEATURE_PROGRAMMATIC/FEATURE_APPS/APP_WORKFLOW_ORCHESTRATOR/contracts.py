# CA-M-504@2
"""Strict deterministic Workflow queue boundaries."""


from typing import Any, Literal, Self
from pydantic import BaseModel, ConfigDict, Field, model_validator


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


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


class Status(Strict):
    operation: Literal["status"] = "status"
    run_id: str = Field(pattern=r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")


__all__ = ["EnqueueSelected", "Status"]
