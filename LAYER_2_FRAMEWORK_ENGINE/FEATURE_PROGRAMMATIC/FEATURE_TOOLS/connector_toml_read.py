"""Private complete-read mechanics for the shared TOML connector.

The receiving binding supplies the source and complete schema. This
module does not grant admission, choose authority or resolve a logical identity.
"""

from __future__ import annotations

import hashlib
from collections.abc import Callable

from connector_toml_parse import TomlFailure, equal_values, parse_source, represent_document


def failure(error: TomlFailure, *, state: dict | None = None, effects: list | None = None) -> dict:
    return {"data": None, "current_state": state, "effects": effects or [], "errors": [
        {"code": error.code, "message": str(error), "field": error.field},
    ]}


def observe(
    read_bytes: Callable[[], bytes], *, identity: str, project: str, source_view: str,
    validate_document: Callable[[dict], None], expected_state: dict | None,
) -> tuple[bytes, dict, dict, dict]:
    """Observe one coherent source; unavailable historical sources never fall back."""
    try:
        payload = read_bytes()
    except FileNotFoundError as error:
        code = "target_not_found" if source_view == "current" else "backend_failure"
        raise TomlFailure(code, "The bound configuration source is unavailable.", "target") from error
    except OSError as error:
        raise TomlFailure("backend_failure", "Cannot read the bound configuration source.") from error
    state = {"identity": identity, "project": project, "source_view": source_view,
             "sha256": hashlib.sha256(payload).hexdigest()}
    if expected_state is not None and not equal_values(expected_state, state):
        raise TomlFailure("stale_state", "Expected state does not match the observed source.", "expected_state")
    try:
        source_text, document = parse_source(payload)
        if validate_document(document) is not None:
            raise ValueError("The supplied validator must raise on refusal, not return a flag.")
        represented = represent_document(document)
    except (ValueError, TypeError, RecursionError) as error:
        raise TomlFailure("schema_invalid", "The complete source, supplied schema or value representation is invalid.", "context") from error
    try:
        if read_bytes() != payload:
            raise TomlFailure("stale_state", "The source changed during observation.", "expected_state")
    except OSError as error:
        raise TomlFailure("backend_failure", "Cannot confirm the observed configuration source.") from error
    data = {"identity": identity, "source_text": source_text, "document": represented}
    return payload, document, data, state


def read_configuration(**arguments) -> dict:
    try:
        _, _, data, state = observe(**arguments)
        return {"data": data, "current_state": state, "effects": [], "errors": []}
    except TomlFailure as error:
        return failure(error)
