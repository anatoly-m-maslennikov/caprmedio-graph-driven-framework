"""Evaluate a reviewed level Claim against explicitly declared Scope Unit data."""

from dataclasses import dataclass
from functools import cache
from typing import TYPE_CHECKING

from .reviewed_instance_check import bind_reviewed_instance_check

if TYPE_CHECKING:
    from scope_declaration_parse import ScopeUnitDeclarations


@dataclass(frozen=True)
class ScopeUnit:
    structural_level: int | None
    container: "ScopeUnit | None"


def check_scope_levels(
    declarations: "ScopeUnitDeclarations", claim: str, *, reference: str, reviewed_claim_sha256: str,
) -> dict[str, str]:
    """Return issues by Scope Unit name for a validated Scope declaration tree."""
    validate = bind_reviewed_instance_check(
        claim, reference=reference, reviewed_claim_sha256=reviewed_claim_sha256,
        model_types={"ScopeUnit": ScopeUnit},
    )

    return _evaluate_scope_levels(declarations, validate)


def _evaluate_scope_levels(declarations, validate):
    @cache
    def model(name: str) -> ScopeUnit:
        record = declarations.by_name[name]
        return ScopeUnit(record.structural_level, model(record.parent) if record.parent else None)

    issues = {}
    for name in declarations.by_name:
        unit = model(name)
        if unit.structural_level is None:
            issues[name] = "Missing structural_level"
        elif unit.container is not None and unit.container.structural_level is None:
            issues[name] = "Container is missing structural_level"
        elif not validate(unit):
            issues[name] = "Structural level violates the reviewed Claim"
    return issues


def check_scope_levels_with_packaged_check(declarations, *, instance_check):
    """Explicit Scope operation evaluation using an already reviewed fixed callable."""
    if not callable(instance_check):
        raise TypeError("a packaged Scope check is required")

    def validate(unit):
        result = instance_check(unit)
        if type(result) is not bool:
            raise TypeError("Scope check must return bool")
        return result

    return _evaluate_scope_levels(declarations, validate)
