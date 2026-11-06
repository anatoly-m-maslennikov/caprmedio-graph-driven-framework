"""Resolve reviewed, byte-bound obligations independently of installed adapters."""

from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from carrier_aliases import carrier_read_view
import subject_notation as notation

Record = dict[str, Any]
_SOURCE_ROLES = {
    "C": "Concern",
    "A": "Analysis",
    "P": "Plan",
    "R": "Requirement",
    "M": "Method",
    "E": "Evaluation",
    "D": "Delivery",
    "O": "Operations",
}


def diagnostic(
    code: str, reason: str, authority: list[Record], property_name: str | None = None
) -> Record:
    return {
        "code": code,
        "severity": "error",
        "path": None,
        "span": None,
        "property": property_name,
        "authority": authority,
        "reason": reason,
        "evidence": None,
    }


@dataclass(frozen=True)
class Obligation:
    code: str
    authority: list[Record]
    supported: bool
    reason: str


@dataclass(frozen=True)
class AuthorityContext:
    bindings: list[Record]
    required: int
    supported: int
    unsupported: int
    gaps: list[Record]
    obligations: tuple[Obligation, ...]
    domains: dict[str, tuple[str, ...]]
    unclassified_sources: bool

    @property
    def status_domains(self) -> dict[str, list[str]]:
        """Exact role-qualified values, available only from verified domain sources."""
        return {
            code.rsplit(".", 1)[1].capitalize(): list(values)
            for code, values in self.domains.items()
            if code.startswith("domain.status.")
        }


def _binding_key(binding: Record) -> tuple[str, int, str, str]:
    return (binding["atom_id"], binding["version"], binding["path"], binding["sha256"])


def _verified(source: Record, entry: Record) -> bool:
    del entry  # Registry entries select obligations; observed Carrier bytes bind the Revision.
    binding, metadata = source.get("binding"), source.get("metadata")
    if not isinstance(binding, dict) or not isinstance(metadata, dict):
        return False
    try:
        metadata = carrier_read_view(metadata)
    except ValueError:
        return False
    version, text = binding.get("version"), source.get("text")
    identifier = binding.get("atom_id")
    identity = identifier.rsplit("-", 2) if isinstance(identifier, str) else []
    expected_role = _SOURCE_ROLES.get(identity[1]) if len(identity) == 3 else None
    return bool(
        type(version) is int
        and version > 0
        and type(metadata.get("version")) is int
        and metadata["version"] == version
        and isinstance(binding.get("atom_id"), str)
        and binding["atom_id"]
        and metadata.get("atom_id") == binding["atom_id"]
        and expected_role is not None
        and metadata.get("content_role") == expected_role
        and metadata.get("status") in {"Active", "active"}
        and "projection" not in metadata
        and isinstance(binding.get("path"), str)
        and binding["path"]
        and isinstance(text, str)
        and hashlib.sha256(text.encode("utf-8")).hexdigest() == binding.get("sha256")
    )


def _domain(text: str) -> tuple[str, ...]:
    """Extract only the reviewed finite-set syntax, never general prose inference."""
    claim = text.split("---", 2)[-1]
    match = re.search(
        r"\*\*must\*\* be (?:exactly )?\(([^()]+)\)|\*\*must\*\* include \(([^()]+)\)|\*\*in\*\* \(([^()]+)\)",
        claim,
    )
    if match is None:
        return ()
    raw = next(value for value in match.groups() if value is not None)
    return tuple(value.strip().strip("`") for value in raw.split(","))


def _header_qualification(step: Any, property_name: str) -> str | None:
    if step.operator != "/" or not isinstance(step.operand, notation.Qualification):
        return None
    path = step.operand.relative_path
    if (not isinstance(path.head, notation.Name) or path.head.value != "Header"
            or path.value_format or path.value_cardinality):
        return None
    steps = list(path.steps)
    if (steps and steps[0].operator == "." and isinstance(steps[0].operand, notation.Name)
            and steps[0].operand.value == "Context"):
        steps.pop(0)
    if len(steps) != 2:
        return None
    property_step, value_step = steps
    if (property_step.operator != "." or not isinstance(property_step.operand, notation.Name)
            or property_step.operand.value != property_name or value_step.operator != ":="
            or not isinstance(value_step.operand, notation.ValueLiteral)
            or not isinstance(value_step.operand.value, str) or not value_step.operand.value):
        return None
    return value_step.operand.value


def _current_declaration_target(metadata: Record) -> Any:
    metadata = carrier_read_view(metadata)
    if metadata.get("role") != "Requirement" or metadata.get("form") != "Declaration":
        return None
    subjects = metadata.get("subjects")
    active = subjects.get("active") if isinstance(subjects, dict) else None
    if not isinstance(active, str):
        return None
    try:
        expression = notation.parse_subject_expression(active, subject_profile="approved").expression
    except notation.SubjectNotationError:
        return None
    if not isinstance(expression, notation.RelationChain) or len(expression.endpoints) != 2:
        return None
    model, target = expression.endpoints
    if (len(expression.links) != 1 or expression.links[0].operator != "<+"
            or not isinstance(model, notation.Path) or not isinstance(model.head, notation.Name)
            or model.head.value != "CAPRMEDIO_MODEL" or model.steps or model.value_format or model.value_cardinality
            or not isinstance(target, notation.Path) or not isinstance(target.head, notation.Name)
            or target.head.value != "Atom" or target.value_format or target.value_cardinality):
        return None
    return target


def current_role_declaration(source: Record) -> str | None:
    """Read one complete Role selector from a verified Current Declaration."""
    if not _verified(source, {}):
        return None
    target = _current_declaration_target(source["metadata"])
    return _header_qualification(target.steps[0], "Role") if target is not None and len(target.steps) == 1 else None


def current_form_coordinate(metadata: Record) -> tuple[str, str] | None:
    """Read only a whole Role/Form coordinate; no references or partial matches."""
    target = _current_declaration_target(metadata)
    if target is None or len(target.steps) != 2:
        return None
    role = _header_qualification(target.steps[0], "Role")
    form = _header_qualification(target.steps[1], "Form")
    return (role, form) if role is not None and form is not None else None


def _current_role_domain(sources: list[Record]) -> tuple[tuple[str, ...], list[Record], bool]:
    declarations = [(current_role_declaration(source), source) for source in sources]
    declarations = [(role, source) for role, source in declarations if role is not None]
    declarations.sort(key=lambda item: _binding_key(item[1]["binding"]))
    values = tuple(role for role, _ in declarations)
    bindings = [source["binding"] for _, source in declarations]
    # The adopted role model declares eight cases individually.  This bound is
    # a cardinality check, not a duplicate enumeration of their role names.
    complete = len(values) == 8 and len(set(values)) == 8
    return values if complete else (), bindings, complete


def _source_obligations(
    atom_id: str, entry: Record, candidates: list[Record], adapters: frozenset[str],
    sources: list[Record], current_role_domain: tuple[tuple[str, ...], list[Record], bool] | None,
) -> tuple[list[Obligation], list[Record], dict[str, tuple[str, ...]]]:
    bindings = sorted((s["binding"] for s in candidates), key=_binding_key)
    verified = len(candidates) == 1 and _verified(candidates[0], entry)
    reason = "Authority source is absent, changed, or ambiguous: " + atom_id + "."
    domains: dict[str, tuple[str, ...]] = {}
    obligations = []
    for code in entry["obligations"]:
        supported = verified and code in adapters
        if supported and code.startswith("domain."):
            if code == "domain.content_role" and current_role_domain is not None:
                values, role_bindings, complete = current_role_domain
                bindings = sorted(role_bindings, key=_binding_key)
                supported = complete
            else:
                values = _domain(candidates[0]["text"])
            if not values and code.startswith("domain.status."):
                from authoritative_status_models import (
                    StatusModelError, declarations_from_sources, resolve_status_domain,
                )
                try:
                    identities = [s["binding"]["atom_id"] for s in sources]
                    declarations = declarations_from_sources([
                        s for s in sources if _verified(s, {})
                        and identities.count(s["binding"]["atom_id"]) == 1
                    ])
                    domain = resolve_status_domain(declarations, code.rsplit(".", 1)[1].capitalize())
                    values = tuple(domain["statuses"])
                    bindings = sorted(domain["model_sources"], key=_binding_key)
                except StatusModelError:
                    values = ()
            supported = supported and bool(values)
            domains[code] = values
        why = "Verified exact source-bound adapter." if supported else reason
        if verified and not supported:
            why = (
                "Current Role domain requires exactly eight distinct verified Current R/Declaration sources."
                if code == "domain.content_role" and current_role_domain is not None
                else "No source-bound adapter supports obligation: " + code + "."
            )
        obligations.append(Obligation(code, bindings, supported, why))
    missing = [o.code for o in obligations if not o.supported]
    gaps = []
    if missing:
        why = (
            reason
            if not verified
            else "Unsupported obligations from " + atom_id + ": " + ", ".join(missing) + "."
        )
        gaps.append(diagnostic("AUTHORITY_UNSUPPORTED", why, bindings))
    return obligations, gaps, domains


def resolve_context(sources: list[Record]) -> AuthorityContext:
    # The inventory is loaded before adapter selection. Removing an adapter cannot
    # remove its source obligation, and unknown sources never vanish from coverage.
    registry: Record = json.loads(Path(__file__).with_name("registry.json").read_text())
    from .checks import ADAPTER_CODES
    from .support_authority import support_sources

    grouped: dict[str, list[Record]] = {}
    for source in sources:
        grouped.setdefault(source["binding"]["atom_id"], []).append(source)
    obligations: list[Obligation] = []
    gaps: list[Record] = []
    domains: dict[str, tuple[str, ...]] = {}
    current_encoding = "CA-D-657" in grouped
    role_domain = _current_role_domain(sources) if current_encoding else None
    # D657 makes the remaining Plan-, projection-, priority-, address-, and
    # retired-field rules conditional on the carried property.  A base Current
    # context cannot manufacture those conditions, so an omitted conditional
    # source is checked when its property is encountered rather than reported
    # as a missing universal closure member.  D276/D482 remain historical
    # contracts and are never successors of D657.
    current_deferred = frozenset({
        "CA-D-276", "CA-D-482", "CA-D-478", "CA-D-480", "CA-D-481",
        "CA-D-470", "CA-D-471", "CA-D-472", "CA-D-473", "CA-D-386",
        "CA-D-305", "CA-D-447",
    })
    for atom_id, entry in registry["sources"].items():
        candidates = grouped.pop(atom_id, [])
        if current_encoding and atom_id in current_deferred and not candidates:
            continue
        if not candidates and not entry["required"]:
            continue
        items, missing, values = _source_obligations(
            atom_id, entry, candidates, ADAPTER_CODES, sources, role_domain,
        )
        obligations.extend(items)
        gaps.extend(missing)
        domains.update(values)
    # Support definitions are not automatically universal candidate obligations.
    # Changed or ambiguous support sources still remain visibly unclassified.
    for atom_id, entry in support_sources().items():
        candidates = grouped.get(atom_id, [])
        if len(candidates) == 1 and _verified(candidates[0], entry):
            grouped.pop(atom_id)
    if current_encoding:
        for source in sources:
            if current_role_declaration(source) is not None:
                grouped.pop(source["binding"]["atom_id"], None)
    # A composed Status domain has already classified its verified base source.
    domain_dependencies = {
        binding["atom_id"] for obligation in obligations
        if obligation.supported and obligation.code.startswith("domain.status.")
        for binding in obligation.authority
    }
    for atom_id in domain_dependencies:
        grouped.pop(atom_id, None)
    for atom_id, candidates in sorted(grouped.items()):
        bindings = sorted((s["binding"] for s in candidates), key=_binding_key)
        why = "Unclassified source obligations require review: " + atom_id + "."
        obligations.append(Obligation("authority.unclassified." + atom_id, bindings, False, why))
        gaps.append(diagnostic("AUTHORITY_UNSUPPORTED", why, bindings))
    obligations.sort(key=lambda item: item.code)
    supported = sum(item.supported for item in obligations)
    bindings = sorted((s["binding"] for s in sources), key=_binding_key)
    return AuthorityContext(
        bindings,
        len(obligations),
        supported,
        len(obligations) - supported,
        gaps,
        tuple(obligations),
        domains,
        bool(grouped),
    )
