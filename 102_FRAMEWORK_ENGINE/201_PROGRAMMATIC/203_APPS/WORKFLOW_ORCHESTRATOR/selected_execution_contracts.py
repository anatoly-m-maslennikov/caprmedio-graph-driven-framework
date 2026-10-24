"""Contracts shared by the selected Workflow execution components."""

from __future__ import annotations

from collections.abc import Callable, Mapping
import hashlib
import json
import re
from typing import Any, cast


MANIFEST_DEFAULT = "_projection/selected_workflow_bindings.json"
RUN_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
SECRET_TERMS = {"secret", "password", "token", "credential", "api_key", "apikey"}
ActionHandler = Callable[[dict[str, Any]], Mapping[str, Any]]


class SelectedExecutionError(RuntimeError):
    """A selected request cannot safely progress through the queue."""


class LifecycleAdmissionError(SelectedExecutionError):
    """A source-derived lifecycle refusal before queue or Run admission."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(message)

    def record(self) -> dict[str, str]:
        return {"code": self.code, "message": self.message}


def canonical_json(value: object) -> bytes:
    """Stable JSON bytes used only for frozen request and manifest comparisons."""
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )


def _sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _contains_secret(value: object) -> bool:
    if isinstance(value, Mapping):
        return any(
            str(key).lower().replace("-", "_") in SECRET_TERMS or _contains_secret(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return any(_contains_secret(item) for item in value)
    return False


def _contains_execution_secret(execution: Mapping[str, Any]) -> bool:
    from workflow_run_support import SelectedRunError, _reject_parameter_secrets

    parameters = execution.get("parameters")
    if not isinstance(parameters, Mapping):
        return _contains_secret(execution)
    try:
        checked_parameters = _reject_parameter_secrets(
            parameters,
            cast(str, execution.get("operation_route")),
        )
    except SelectedRunError as error:
        raise SelectedExecutionError("selected execution carries a secret field") from error
    return _contains_secret({**execution, "parameters": checked_parameters})
