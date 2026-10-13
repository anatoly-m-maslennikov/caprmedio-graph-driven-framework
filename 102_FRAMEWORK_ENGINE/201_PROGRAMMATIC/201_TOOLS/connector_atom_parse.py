"""Pure parsing and predicates for logical Atom Query/Read (not a Tool)."""

from __future__ import annotations

import re
from pathlib import Path

from atom_subject_lookup import _structured_subjects
from subject_notation import get_profile, parse_subject
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier


IDENTITY = re.compile(r"CA-[CAPRMEDO]-[0-9]+")
ROLES = {"C": "Concern", "A": "Analysis", "P": "Plan", "R": "Requirement",
         "M": "Method", "E": "Evaluation", "D": "Delivery", "O": "Operations"}
RESULT_FIELDS = frozenset({"atom_id", "version", "current_scope_unit", "status", "content_role",
                           "type", "updated_at", "subjects"})
LIFECYCLES = frozenset({"active", "done", "resolved", "canceled", "archived"})


def parse_atom(raw: bytes):
    """Preserve the complete supplied text; perform no storage access."""
    parsed = parse_carrier(raw, Path("supplied.md"))
    values = parsed.metadata
    identity = values.get("atom_id")
    if not isinstance(identity, str) or IDENTITY.fullmatch(identity) is None:
        raise CarrierError("ATOM_INVALID", "A full logical Atom ID is required.")
    if type(values.get("version")) is not int or values["version"] < 1:
        raise CarrierError("ATOM_INVALID", "Atom Version must be a positive integer.")
    for field in ("status", "current_scope_unit", "type", "updated_at"):
        if not isinstance(values.get(field), str) or not values[field]:
            raise CarrierError("ATOM_INVALID", f"Atom {field} is required.")
    if values.get("content_role") != ROLES[identity.split("-")[1]]:
        raise CarrierError("ATOM_INVALID", "Atom ID kind and Content Role disagree.")
    try:
        tuple(_structured_subjects(values, {"governs", "depends_on"}))
    except ValueError as error:
        raise CarrierError("ATOM_INVALID", str(error)) from error
    return parsed


def validate_filters(filters: object) -> None:
    required = {"scope_units", "lifecycles", "subjects", "result_fields"}
    optional = {"atom_ids", "statuses", "content_roles"}
    if not isinstance(filters, dict) or not required <= filters.keys() or not filters.keys() <= required | optional:
        raise ValueError("Query requires explicit scope_units, lifecycles, subjects and result_fields.")
    for field in required - {"subjects"} | (filters.keys() & optional):
        values = filters[field]
        if not isinstance(values, list) or not values or any(not isinstance(v, str) or not v for v in values) or len(set(values)) != len(values):
            raise ValueError(f"{field} must be an explicit nonempty set of strings.")
    if not set(filters["lifecycles"]) <= LIFECYCLES or not set(filters["result_fields"]) <= RESULT_FIELDS:
        raise ValueError("Unsupported lifecycle or requested result field.")
    if any(IDENTITY.fullmatch(v) is None for v in filters.get("atom_ids", [])):
        raise ValueError("Atom selectors must be logical IDs.")
    if not isinstance(filters["subjects"], list):
        raise ValueError("subjects must be an explicit predicate array.")
    for predicate in filters["subjects"]:
        if (not isinstance(predicate, dict) or predicate.keys() != {"fields", "match", "value"}
                or not isinstance(predicate["fields"], list) or not predicate["fields"]
                or any(v not in {"governs", "depends_on"} for v in predicate["fields"])
                or len(set(predicate["fields"])) != len(predicate["fields"])
                or predicate["match"] not in {"exact", "prefix", "suffix", "contains"}
                or not isinstance(predicate["value"], str) or not predicate["value"]):
            raise ValueError("A Subject predicate requires explicit fields, match and value.")


def subject_matches(value: str, criterion: str, mode: str, separators: tuple[str, ...]) -> bool:
    if mode == "exact":
        return value == criterion
    if mode == "prefix":
        return value == criterion or any(value.startswith(criterion + boundary) for boundary in separators)
    if mode == "suffix":
        return value.endswith(criterion)
    return criterion in value


def matches(properties: dict, filters: dict, subject_profile: str) -> bool:
    profile = get_profile(subject_profile)
    values = tuple(_structured_subjects(properties, {"governs", "depends_on"}))
    for _, _, value in values:
        parse_subject(value, subject_profile=profile.name)
    for field, source in (("atom_ids", "atom_id"), ("statuses", "status"), ("content_roles", "content_role")):
        if field in filters and properties[source] not in filters[field]:
            return False
    return all(any(field in predicate["fields"] and subject_matches(value, predicate["value"], predicate["match"], profile.separators)
                   for field, _, value in values) for predicate in filters["subjects"])
