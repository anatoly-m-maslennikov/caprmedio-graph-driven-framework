"""Effect-free Scope Unit adapter using private receiving-service bindings."""

from __future__ import annotations

import copy
import tomllib

from connector_bindings import ConnectorBindingError, ConnectorBindings
from connector_contract import validate_request, validate_result
from connector_scope_parsing import (
    ScopeDataError, parse_scope_sources, query_declarations, read_declaration, validate_scope_request,
)
from project_selection import ProjectSelectionError, _declaration_boundary_proof, _validate_structure, bound_selection
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


def _failure(code: str, message: str, field: str | None = None, *, data=None, state=None) -> dict:
    return {"data": data, "current_state": state, "effects": [],
            "errors": [{"code": code, "message": message, "field": field}]}


def execute_scope_request(
    request: object, *, bindings: ConnectorBindings, project_name: str, source_view: object,
) -> dict:
    """Read one receiver-bound view; no CLI, discovery, or public carrier locator.

    The receiver privately fixes project/view and returns exactly Settings then
    Structure sources. Its supplied schema validator owns all applicable schema
    authority, including Project Settings and declared binding eligibility.
    """
    errors = validate_request(request, supported_operations={"query", "read"}, supported_kinds={"Scope Unit"})
    if errors:
        return {"data": None, "current_state": None, "effects": [], "errors": errors}
    if not isinstance(bindings, ConnectorBindings):
        return _failure("permission_denied", "Receiving bindings are unavailable.", "authorization")
    state, data = None, None
    try:
        validate_scope_request(request)
        bound = bindings.bind(request)
        if len(bound.sources) != 2:
            code = "backend_failure" if len(bound.sources) < 2 else "target_ambiguous"
            raise ConnectorBindingError(code, "Scope source authority is missing or ambiguous.", "context")
        if bound.sources[0].root != bound.sources[1].root:
            raise ConnectorBindingError("target_ambiguous", "Scope sources belong to competing Projects.", "context")
        settings, structure = bound.sources
        if settings.sha256 is None or structure.sha256 is None:
            raise ConnectorBindingError("backend_failure", "Required Scope source view is unavailable.", "context")
        settings_text = settings.read_bytes().decode("utf-8")
        declarations = parse_scope_sources(settings_text, structure.read_bytes().decode("utf-8"))
        if not isinstance(project_name, str) or declarations.project_name != project_name or source_view is None:
            raise ConnectorBindingError("schema_invalid", "Source view differs from the bound owning Project.", "context")
        rows = list(declarations.rows.values())
        document = {"schema_version": 1, "scope_units": [
            {**row, "authority_path": row["authority_path"].rstrip("/")} for row in rows]}
        _validate_structure(document, settings.root)
        paths = tomllib.loads(settings_text).get("paths", {})
        boundary_reader = ReadContext(roots=[str(settings.root)], limits=dict(CEILINGS))
        selection = bound_selection(settings.root)
        if selection is not None:
            if not isinstance(paths, dict) or paths.get("control_root") != selection.control_relative.as_posix():
                raise ProjectSelectionError("Scope source control differs from the selected Project")
            selection._revalidate_boundary(reader=boundary_reader)
        boundary_proof = _declaration_boundary_proof(
            settings.root, paths.get("control_root") if isinstance(paths, dict) else None,
            rows, reader=boundary_reader,
        )
        state = {"project": project_name, "source_view": copy.deepcopy(source_view), "source_evidence": {
            "project_settings": {"sha256": settings.sha256}, "project_structure": {"sha256": structure.sha256}}}
        if request["expected_state"] is not None and request["expected_state"] != state:
            raise ScopeDataError("stale_state", "Requested source evidence differs from the observed view.", "expected_state")
        if source_view != "current" and request["expected_state"] is None:
            raise ScopeDataError("input_invalid", "A pinned or historical view requires its exact expected evidence.", "expected_state")
        if request["operation"] == "read":
            data = read_declaration(declarations, request["target"]["identity"])
        else:
            data = query_declarations(declarations, request["query"]["filters"])
        bound.revalidate_before_effect()
        boundary_proof.revalidate(reader=boundary_reader)
        reopened = parse_scope_sources(settings.read_bytes().decode("utf-8"), structure.read_bytes().decode("utf-8"))
        verified = (read_declaration(reopened, request["target"]["identity"]) if request["operation"] == "read"
                    else query_declarations(reopened, request["query"]["filters"]))
        if verified != data:
            raise ScopeDataError("stale_state", "Returned Scope data differs from reopened sources.", "expected_state")
        boundary_proof.revalidate(reader=boundary_reader)
        result = {"data": data, "current_state": state, "effects": [], "errors": []}
        result["errors"] = validate_result(result, request=request, postconditions_verified=True)
        if result["errors"]:
            result["data"] = None
        return result
    except (ConnectorBindingError, ScopeDataError) as error:
        if data is not None and request["operation"] == "query":
            data["coverage"]["complete"] = False
        else:
            data = None
        return _failure(error.code, str(error), error.field, data=data, state=state)
    except (ProjectSelectionError, UnicodeError, RecursionError):
        return _failure("schema_invalid", "Scope declaration source is invalid.", state=state)
    except OSError:
        return _failure("backend_failure", "Scope source could not be observed.", "context", state=state)
