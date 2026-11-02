"""Effect-free Scope Unit adapter over selected declaration Atom sources."""

from __future__ import annotations

import copy

from connector_bindings import ConnectorBindingError, ConnectorBindings
from connector_contract import validate_request, validate_result
from connector_scope_parsing import (
    ScopeDataError, parse_scope_declarations, query_declarations, read_declaration, validate_scope_request,
)
from project_selection import ProjectSelectionError, bound_selection
from scope_unit_declarations import ScopeDeclarationError, read_scope_unit_declarations
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


def _failure(code: str, message: str, field: str | None = None, *, data=None, state=None) -> dict:
    return {"data": data, "current_state": state, "effects": [],
            "errors": [{"code": code, "message": message, "field": field}]}


def _declaration_pins(sources) -> dict[str, str | None]:
    return {source.relative_path.as_posix(): source.sha256 for source in sources}


def execute_scope_request(
    request: object, *, bindings: ConnectorBindings, project_name: str, source_view: object,
) -> dict:
    """Read one receiver-bound Settings plus declaration-Atom source view."""
    errors = validate_request(request, supported_operations={"query", "read"}, supported_kinds={"Scope Unit"})
    if errors:
        return {"data": None, "current_state": None, "effects": [], "errors": errors}
    if not isinstance(bindings, ConnectorBindings):
        return _failure("permission_denied", "Receiving bindings are unavailable.", "authorization")
    state, data = None, None
    try:
        validate_scope_request(request)
        bound = bindings.bind(request)
        if not bound.sources:
            raise ConnectorBindingError("backend_failure", "Scope source authority is unavailable.", "context")
        settings, *declaration_sources = bound.sources
        if (settings.sha256 is None or not declaration_sources
                or any(source.root != settings.root or source.sha256 is None for source in declaration_sources)):
            raise ConnectorBindingError("backend_failure", "Settings and Scope Unit Declaration sources are required.", "context")
        selection = bound_selection(settings.root)
        if selection is None or settings.relative_path != selection.settings_path.relative_to(settings.root):
            raise ConnectorBindingError("schema_invalid", "Scope source view lacks its selected Project.", "context")
        reader = ReadContext(roots=[str(settings.root)], limits=dict(CEILINGS))
        selection._revalidate_boundary(reader=reader)
        declarations = read_scope_unit_declarations(settings.root, selection.control_root, reader=reader)
        source_pins = _declaration_pins(declaration_sources)
        observed_pins = {path: pin.get("sha256") for path, pin in declarations.source_pins.items()}
        if source_pins != observed_pins:
            raise ConnectorBindingError("stale_state", "Scope Unit Declaration frontier differs from the selected source view.", "context")
        parsed = parse_scope_declarations(declarations)
        if not isinstance(project_name, str) or parsed.project_name != project_name or source_view is None:
            raise ConnectorBindingError("schema_invalid", "Source view differs from the bound owning Project.", "context")
        state = {"project": project_name, "source_view": copy.deepcopy(source_view), "source_evidence": {
            "project_settings": {"sha256": settings.sha256},
            "scope_unit_declarations": {
                "digest": declarations.digest,
                "source_pins": {path: dict(pin) for path, pin in declarations.source_pins.items()},
            },
        }}
        if request["expected_state"] is not None and request["expected_state"] != state:
            raise ScopeDataError("stale_state", "Requested source evidence differs from the observed view.", "expected_state")
        if source_view != "current" and request["expected_state"] is None:
            raise ScopeDataError("input_invalid", "A pinned or historical view requires its exact expected evidence.", "expected_state")
        data = (read_declaration(parsed, request["target"]["identity"])
                if request["operation"] == "read" else query_declarations(parsed, request["query"]["filters"]))
        bound.revalidate_before_effect()
        selection._revalidate_boundary(reader=reader)
        reopened = read_scope_unit_declarations(settings.root, selection.control_root, reader=reader)
        if reopened.digest != declarations.digest:
            raise ScopeDataError("stale_state", "Returned Scope data differs from reopened sources.", "expected_state")
        verified = parse_scope_declarations(reopened)
        replay = (read_declaration(verified, request["target"]["identity"])
                  if request["operation"] == "read" else query_declarations(verified, request["query"]["filters"]))
        if replay != data:
            raise ScopeDataError("stale_state", "Returned Scope data differs from reopened sources.", "expected_state")
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
    except ProjectSelectionError:
        return _failure("stale_state", "Selected Scope declaration sources changed during observation.",
                        "context", state=state)
    except (ScopeDeclarationError, UnicodeError, RecursionError):
        return _failure("schema_invalid", "Scope Unit Declaration source is invalid.", state=state)
    except OSError:
        return _failure("backend_failure", "Scope source could not be observed.", "context", state=state)
