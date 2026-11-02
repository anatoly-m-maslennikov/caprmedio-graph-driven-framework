"""Shared TOML admission and dispatch; parsing and storage stay in their modules."""

from __future__ import annotations

from collections.abc import Callable, Mapping

from connector_bindings import ConnectorBindingError, ConnectorBindings
from connector_contract import validate_request, validate_result
from connector_toml_read import TomlFailure, failure, read_configuration
from connector_toml_write import modify_configuration


IDENTITIES = frozenset({"Project Structure", "Project Settings"})


def execute(
    request: dict, *, bindings: ConnectorBindings, project: str, source_view: str,
    validate_document: Callable[[dict], None], keys: Mapping[str, tuple[str, ...]],
) -> dict:
    """Receiver-owned parameters are not public logical fields or permission flags."""
    try:
        errors = validate_request(request, supported_operations={"read", "modify"}, supported_kinds={"Configuration"})
        if errors:
            return {"data": None, "current_state": None, "effects": [], "errors": errors}
        identity = request["target"]["identity"]
        if type(identity) is not str or identity not in IDENTITIES:
            raise TomlFailure("input_invalid", "Explicit logical configuration identity is required.", "target")
        if not isinstance(bindings, ConnectorBindings):
            raise TomlFailure("permission_denied", "Existing receiving admission is required.", "authorization")
        if type(project) is not str or not project or type(source_view) is not str or not source_view:
            raise TomlFailure("schema_invalid", "Project and source-view bindings are required.", "context")
        if request["operation"] == "modify" and source_view != "current":
            raise TomlFailure("input_invalid", "Modify requires the current source view.", "context")
        bound = bindings.bind(request)
        if not bound.sources:
            raise TomlFailure("target_not_found", "The configuration source was not resolved.", "target")
        if len(bound.sources) != 1:
            raise TomlFailure("target_ambiguous", "The configuration source is ambiguous.", "target")
        arguments = {"project": project, "source_view": source_view, "validate_document": validate_document}
        if request["operation"] == "modify":
            return modify_configuration(request, bound, keys=keys, **arguments)
        result = read_configuration(read_bytes=bound.sources[0].read_bytes, identity=identity,
                                    expected_state=request["expected_state"], **arguments)
        if not result["errors"]:
            bound.revalidate_before_effect()
        result["errors"] = validate_result(result, request=request, postconditions_verified=not result["errors"])
        return result
    except ConnectorBindingError as error:
        code = "backend_failure" if source_view != "current" and error.code == "target_not_found" else error.code
        return failure(TomlFailure(code, error.message, error.field))
    except TomlFailure as error:
        return failure(error)
