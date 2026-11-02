"""Private Modify adapter; the receiver owns logical-to-carrier admission."""

from dataclasses import replace
from collections.abc import Callable

from connector_bindings import BoundRequest, ConnectorBindingError, ConnectorBindings
from connector_carrier_reading import CarrierError
from connector_carrier_writing import CarrierPlan, execute
from connector_contract import validate_result


def modify(request: dict, *, bindings: ConnectorBindings,
           resolve_plan: Callable[[BoundRequest], CarrierPlan]) -> dict:
    """Use the receiver's exact admitted schema and private plan, never public paths.

    The resolver must bind the selected logical delta to ownership, classification,
    cleanup or lifecycle/history evidence. No receiving schema or transport route
    is selected here. Missing receiving admission remains a refusal.
    """
    try:
        if not isinstance(bindings, ConnectorBindings) or not callable(resolve_plan):
            raise ConnectorBindingError("input_invalid", "Concrete receiving bindings are required.")
        if not isinstance(request, dict) or request.get("operation") != "modify":
            raise ConnectorBindingError("unsupported_operation", "Private carrier adapter supports Modify only.")
        bound = bindings.bind(request)
        plan = resolve_plan(bound)
        if not isinstance(plan, CarrierPlan):
            raise ConnectorBindingError("input_invalid", "Receiving carrier plan is unresolved.")
        original = plan.admission_evidence
        def revalidate(current_plan):
            bound.revalidate_before_effect()
            return original(current_plan)
        if not callable(original):
            raise ConnectorBindingError("permission_denied", "Carrier ownership and admission evidence is unresolved.")
        result = execute(replace(plan, admission_evidence=revalidate), logical_target=bound.request["target"])
        result["errors"] = validate_result(
            result, request=bound.request, postconditions_verified=not result["errors"],
            unchanged_verified=result["data"] is not None and result["data"]["no_op"],
        )
        return result
    except (ConnectorBindingError, CarrierError, ValueError, TypeError, OSError) as error:
        return {"data": None, "current_state": None, "effects": [], "errors": [
            {"code": error.code if isinstance(error, (ConnectorBindingError, CarrierError)) else "backend_failure",
             "message": "Private receiving binding or admission could not be established.",
             "field": getattr(error, "field", "context") if isinstance(error, (ConnectorBindingError, CarrierError)) else "context"}
        ]}
