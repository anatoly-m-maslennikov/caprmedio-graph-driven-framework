# CA-M-517@1
"""Validate and remove the MCP caller-context envelope."""

from typing import Any

from pydantic import BaseModel, ConfigDict

from runtime_request_context import RuntimeRequestContext, current_request_context


class CallerContextError(ValueError):
    """The supplied caller context is invalid or disagrees with its parent."""


class _CallerContext(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)

    session_id: str


def take_caller_context(arguments: Any) -> tuple[Any, RuntimeRequestContext | None]:
    if not isinstance(arguments, dict) or "caller_context" not in arguments:
        return arguments, None
    value = arguments["caller_context"]
    try:
        context = RuntimeRequestContext(session_id=_CallerContext.model_validate(value).session_id)
    except (TypeError, ValueError) as error:
        raise CallerContextError("invalid_caller_context") from error
    current = current_request_context()
    if current is not None and current != context:
        raise CallerContextError("caller_context_conflict")
    return {key: value for key, value in arguments.items() if key != "caller_context"}, context
