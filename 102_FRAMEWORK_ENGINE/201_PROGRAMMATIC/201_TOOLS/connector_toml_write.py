"""Private one-source TOML write mechanics; pure transforms live in the parser."""

from __future__ import annotations

import os
import hashlib
from collections.abc import Callable, Mapping
from pathlib import Path

from connector_bindings import BoundRequest, ConnectorBindingError, capture_source
from connector_contract import validate_result
from connector_toml_parse import apply_edits, equal_values, render_document
from connector_toml_read import TomlFailure, failure, observe
from project_runtime import TemporaryBoundaryError, atomic_tempfile




def replace_source(path: Path, payload: bytes) -> None:
    """Use the existing file backend's temp-file replacement, without a concurrency claim."""
    mode = path.stat().st_mode & 0o777
    try:
        descriptor, name = atomic_tempfile(path, "connector-toml")
    except TemporaryBoundaryError as error:
        raise OSError("The required Project Temporary State is unavailable.") from error
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(name, mode)
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def modify_configuration(
    request: dict, bound: BoundRequest, *, project: str, source_view: str,
    validate_document: Callable[[dict], None], keys: Mapping[str, tuple[str, ...]],
) -> dict:
    """Execute only an already-admitted explicit change and observe the boundary."""
    effects, state = [], None
    try:
        source = bound.sources[0]
        arguments = {"identity": request["target"]["identity"], "project": project, "source_view": source_view,
                     "validate_document": validate_document, "expected_state": request["expected_state"]}
        before, document, data, state = observe(source.read_bytes, **arguments)
        proposed, diff = apply_edits(document, request["delta"], keys)
        if validate_document(proposed) is not None:
            raise TomlFailure("schema_invalid", "The supplied complete validator returned a flag.", "context")
        payload = before if equal_values(document, proposed) else render_document(proposed)
        bound.revalidate_before_effect()
        if source.read_bytes() != before:
            raise TomlFailure("stale_state", "Source changed before the requested effect.", "expected_state")
        if payload == before:
            result = {"data": {**data, "effective_diff": []}, "current_state": state, "effects": [], "errors": []}
            result["errors"] = validate_result(result, request=request, postconditions_verified=True, unchanged_verified=True)
            return result
        write_error = None
        try:
            replace_source(source.root / source.relative_path, payload)
        except OSError as error:
            write_error = error
        proposed_digest = hashlib.sha256(payload).hexdigest()
        try:
            observed_source = capture_source(source.root, source.relative_path)
            after = observed_source.read_bytes()
        except ConnectorBindingError as error:
            effects = [{"operation": "modify", "target": request["target"], "state": "unknown",
                        "evidence": {"before_sha256": state["sha256"], "proposed_sha256": proposed_digest,
                                     "observation_error": error.record()}}]
            state = None
            raise TomlFailure("effect_uncertain", "The write boundary cannot be independently observed.") from error
        if after == before:
            raise TomlFailure("backend_failure", "Requested change was not observed; original bytes remain.")
        known = after == payload
        effects = [{"operation": "modify", "target": request["target"], "state": "known" if known else "unknown",
                    "evidence": {"before_sha256": state["sha256"], "after_sha256": hashlib.sha256(after).hexdigest(),
                                 "proposed_sha256": proposed_digest}}]
        if not known:
            state = None
            raise TomlFailure("effect_uncertain", "Observed bytes differ from the explicit proposed change.")
        state = {**state, "sha256": hashlib.sha256(after).hexdigest()}
        _, actual_document, actual_data, state = observe(
            observed_source.read_bytes, **{**arguments, "expected_state": None},
        )
        if not equal_values(actual_document, proposed):
            raise TomlFailure("effect_uncertain", "Observed values differ from the explicit proposed change.")
        result = {"data": {**actual_data, "effective_diff": diff}, "current_state": state,
                  "effects": effects, "errors": []}
        if write_error is not None:
            result["errors"] = [{"code": "backend_failure", "message": "Write reported failure after the observed effect.", "field": None}]
        result["errors"] = validate_result(result, request=request, postconditions_verified=True)
        return result
    except ConnectorBindingError as error:
        return failure(TomlFailure(error.code, error.message, error.field), state=state, effects=effects)
    except TomlFailure as error:
        return failure(error, state=state, effects=effects)
    except (OSError, ValueError, TypeError, RecursionError):
        return failure(TomlFailure("schema_invalid", "Supplied schema, delta or TOML value is invalid.", "delta"),
                       state=state, effects=effects)
