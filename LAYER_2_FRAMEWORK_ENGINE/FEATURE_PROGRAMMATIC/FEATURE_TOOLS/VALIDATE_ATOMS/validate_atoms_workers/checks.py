"""Stable carrier-check facade; unresolved meaning remains a coverage gap."""

from __future__ import annotations

from carrier_aliases import carrier_read_view

from .authority import AuthorityContext, Record, diagnostic
from .check_dispatch import ADAPTER_CODES as ADAPTER_CODES
from .check_dispatch import ADAPTERS as ADAPTERS
from .check_dispatch import _execute


def validate_carrier(
    metadata: Record, body: str, context: AuthorityContext, inputs: Record | None = None
) -> Record:
    raw_metadata = metadata
    try:
        metadata = carrier_read_view(metadata)
        alias_error = None
    except ValueError as error:
        alias_error = error
    inputs = dict(inputs or {})
    inputs.setdefault("_raw_metadata", raw_metadata)
    findings: list[Record] = []
    gaps = list(context.gaps)
    outcomes = []
    for obligation in context.obligations:
        outcome, found, missing = _execute(obligation, metadata, body, context, inputs)
        outcome["finding_indexes"] = list(range(len(findings), len(findings) + len(found)))
        findings.extend(found)
        gaps.extend(missing)
        outcomes.append(outcome)
    if alias_error is not None:
        findings.append(diagnostic("CARRIER_ALIAS_CONFLICT", str(alias_error), context.bindings))
    return {"outcomes": outcomes, "findings": findings, "gaps": gaps}
