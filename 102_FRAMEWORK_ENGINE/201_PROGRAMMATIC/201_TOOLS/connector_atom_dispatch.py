"""Private Atom dispatch through an existing receiver binding, not a new CLI."""

from __future__ import annotations

from connector_bindings import ConnectorBindingError, ConnectorBindings
from connector_contract import validate_request, validate_result
from connector_atom_read import AtomReadError, AtomSourceView, query_atoms, read_atom


def execute_atom_request(request: dict, bindings: ConnectorBindings, view: AtomSourceView) -> dict:
    """Use the receiver's sealed admission and exact complete source frontier.

    View/schema/private resolution belong to the receiving adapter. This helper
    never constructs a permission reference or supplies a runtime mapping.
    """
    result = {"data": None, "current_state": None, "effects": [], "errors": []}
    errors = validate_request(request, supported_operations={"query", "read"}, supported_kinds={"Atom"})
    if errors:
        return {**result, "errors": errors}
    if not isinstance(bindings, ConnectorBindings):
        return {**result, "errors": [{"code": "input_invalid", "message": "An existing receiver binding is required.", "field": "context"}]}
    try:
        bound = bindings.bind(request)
        if bound.request["operation"] == "query":
            result = query_atoms(bound.request["query"]["filters"], view, bound_sources=bound.sources)
            expected = bound.request["expected_state"]
            if expected is not None and expected != result["current_state"]:
                raise AtomReadError("stale_state", "Query source state differs from its supplied exact expectation.", "expected_state")
        else:
            result = read_atom(bound.request["target"]["identity"], view, bound.request["expected_state"], bound_sources=bound.sources)
        bound.revalidate_before_effect()
        result["errors"] = validate_result(result, request=bound.request, postconditions_verified=True)
        return result
    except (ConnectorBindingError, AtomReadError) as error:
        return {"data": None, "current_state": None, "effects": [], "errors": [
            {"code": error.code, "message": str(error), "field": error.field},
        ]}
    except (OSError, TypeError, ValueError) as error:
        return {"data": None, "current_state": None, "effects": [], "errors": [
            {"code": "backend_failure", "message": "Bound Atom observation could not complete.", "field": "context"},
        ]}
