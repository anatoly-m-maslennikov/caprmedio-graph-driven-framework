"""Pure Scope Unit Declaration projection and logical selection (D626/D627)."""

from __future__ import annotations

from dataclasses import dataclass
import re


PROJECT = "PROJECT"
NAME = re.compile(r"^[A-Z0-9]+(?:_[A-Z0-9]+)*$")
QUERY_FIELDS = frozenset({
    "scope_unit_name", "scope_unit_id", "scope_unit_type", "label", "parent", "local_order",
})
PREDICATE_FIELDS = QUERY_FIELDS - {"scope_unit_id", "local_order"}
_PUBLIC_FIELDS = QUERY_FIELDS


class ScopeDataError(ValueError):
    def __init__(self, code: str, message: str, field: str | None = None):
        super().__init__(message)
        self.code, self.field = code, field


@dataclass(frozen=True)
class ScopeDeclarations:
    root: dict
    rows: dict[str, dict]

    @property
    def project_name(self) -> str:
        return self.root["scope_unit_name"]


def _schema(condition: bool, message: str) -> None:
    if not condition:
        raise ScopeDataError("schema_invalid", message)


def _name(value: object) -> bool:
    return isinstance(value, str) and bool(NAME.fullmatch(value)) and value != PROJECT


def _logical_identity(value: object) -> bool:
    return (isinstance(value, str) and bool(value.strip()) and value == value.strip()
            and value not in {".", "..", PROJECT} and not any(char in value for char in "/\\\x00"))


def _row(value: object, *, root: bool = False) -> dict:
    _schema(isinstance(value, dict), "Scope Unit Declaration is invalid.")
    row = dict(value)
    if "scope_unit_label" in row:
        _schema("label" not in row, "Scope Unit Declaration has duplicate Label fields.")
        row["label"] = row.pop("scope_unit_label")
    name = row.get("scope_unit_name")
    _schema(isinstance(name, str) and bool(name), "Scope Unit Name must be nonempty.")
    if not root:
        _schema(_name(name), "Scope Unit Name must be canonical.")
        _schema(row.get("parent") == PROJECT or _logical_identity(row.get("parent")), "Invalid Scope Unit parent.")
        _schema(isinstance(row.get("scope_unit_id"), str) and bool(row["scope_unit_id"]),
                "Scope Unit Declaration needs one direct Scope Unit ID.")
    _schema(row.get("scope_unit_type") in {"Ordered", "Unordered"}, "Invalid Scope Unit Type.")
    _schema(row.get("label") is None or isinstance(row.get("label"), str), "Invalid Scope Unit Label.")
    if row["scope_unit_type"] == "Ordered":
        _schema(type(row.get("local_order")) is int and row["local_order"] > 0,
                "Ordered Scope Unit requires a positive Local Order.")
    else:
        _schema(row.get("local_order") is None, "Unordered Scope Unit forbids Local Order.")
    return row


def parse_scope_declarations(declarations: object) -> ScopeDeclarations:
    """Project an already-read Scope Unit Declaration Atom set."""
    structure = getattr(declarations, "as_structure", None)
    if callable(structure):
        source_rows = structure().get("scope_units")
        _schema(isinstance(source_rows, list), "Scope Unit Declaration set is invalid.")
        normalized = [_row(value, root=value.get("scope_unit_id") is None if isinstance(value, dict) else False)
                      for value in source_rows]
        roots = [row for row in normalized if row.get("scope_unit_id") is None]
        _schema(len(roots) == 1, "Scope Unit Declaration set requires one Project root.")
        root = roots[0]
        unit_values = [row for row in normalized if row is not root]
    else:
        root = _row(getattr(declarations, "root", None), root=True)
        unit_values = getattr(declarations, "units", None)
        _schema(isinstance(unit_values, (tuple, list)), "Scope Unit Declaration set is invalid.")
    rows: dict[str, dict] = {}
    for value in unit_values:
        row = _row(value)
        if row["parent"] == root["scope_unit_name"]:
            row["parent"] = PROJECT
        name = row["scope_unit_name"]
        _schema(name not in rows and name != root["scope_unit_name"], "Duplicate Scope Unit identity.")
        rows[name] = row
    for name, row in rows.items():
        _schema(row["parent"] == PROJECT or row["parent"] in rows,
                "Scope Unit parent is undeclared.")
        seen = {name}
        parent = row["parent"]
        while parent != PROJECT:
            _schema(parent not in seen, "Scope Unit parentage contains a cycle.")
            seen.add(parent)
            parent = rows[parent]["parent"]
    orders = set()
    for row in rows.values():
        if row["scope_unit_type"] == "Ordered":
            order = (row["parent"], row["local_order"])
            _schema(order not in orders, "Duplicate Ordered Local Order under one parent.")
            orders.add(order)
    return ScopeDeclarations(root, rows)


def validate_scope_request(request: dict) -> None:
    if request["operation"] == "read":
        identity = request["target"]["identity"]
        if not _logical_identity(identity):
            raise ScopeDataError("input_invalid", "Read requires one canonical Name.", "target")
        return
    filters = request["query"]["filters"]
    invalid = lambda message: ScopeDataError("input_invalid", message, "query")
    if not isinstance(filters, dict) or filters.keys() != {"frontier", "predicates", "result_fields"}:
        raise invalid("Query requires frontier, predicates and result_fields.")
    frontier = filters["frontier"]
    if (not isinstance(frontier, dict) or frontier.keys() != {"identity", "include_self", "include_descendants"}
            or not _logical_identity(frontier["identity"])
            or type(frontier["include_self"]) is not bool or type(frontier["include_descendants"]) is not bool
            or not (frontier["include_self"] or frontier["include_descendants"])):
        raise invalid("Query requires one explicit nonempty logical frontier.")
    fields = filters["result_fields"]
    if (not isinstance(fields, list) or any(not isinstance(field, str) or field not in QUERY_FIELDS for field in fields)
            or len(fields) != len(set(fields))):
        raise invalid("result_fields must be a duplicate-free array of admitted declaration facts.")
    predicates = filters["predicates"]
    if not isinstance(predicates, list):
        raise invalid("predicates must be an array.")
    for predicate in predicates:
        if not isinstance(predicate, dict) or predicate.keys() != {"field", "match", "value"}:
            raise invalid("Each predicate requires field, match and value.")
        field, mode, value = predicate["field"], predicate["match"], predicate["value"]
        if (not isinstance(field, str) or field not in PREDICATE_FIELDS
                or mode not in ("exact", "prefix", "suffix", "contains")
                or (field in {"parent", "scope_unit_type"} and mode != "exact")
                or not isinstance(value, str) or not value.strip()
                or (field == "parent" and not _logical_identity(value))
                or (field == "scope_unit_type" and value not in {"Ordered", "Unordered"})):
            raise invalid("Invalid literal predicate.")


def _public(row: dict) -> dict:
    return {field: row[field] for field in _PUBLIC_FIELDS if field in row and row[field] is not None}


def read_declaration(declarations: ScopeDeclarations, identity: str) -> dict:
    row = declarations.root if identity == declarations.project_name else declarations.rows.get(identity)
    if row is None:
        raise ScopeDataError("target_not_found", "Scope Unit target is not declared.", "target")
    return {"identity": identity, "declaration": _public(row)}


def query_declarations(declarations: ScopeDeclarations, filters: dict) -> dict:
    frontier = filters["frontier"]
    identity = frontier["identity"]
    if identity != declarations.project_name and identity not in declarations.rows:
        raise ScopeDataError("target_not_found", "Scope Unit frontier is not declared.", "query")
    names = {identity} if frontier["include_self"] else set()
    if frontier["include_descendants"]:
        pending = [identity]
        while pending:
            parent = pending.pop()
            children = [name for name, row in declarations.rows.items()
                        if (declarations.project_name if row["parent"] == PROJECT else row["parent"]) == parent]
            names.update(children)
            pending.extend(children)
    matches = []
    for name in sorted(names):
        facts = _public(declarations.rows.get(name, declarations.root))
        selected = True
        for predicate in filters["predicates"]:
            value = facts.get(predicate["field"])
            wanted, mode = predicate["value"], predicate["match"]
            if not isinstance(value, str) or not {"exact": value == wanted, "prefix": value.startswith(wanted),
                    "suffix": value.endswith(wanted), "contains": wanted in value}[mode]:
                selected = False
                break
        if selected:
            matches.append({"identity": name, "facts": {
                field: facts[field] for field in filters["result_fields"] if field in facts
            }})
    return {"matches": matches, "coverage": {"frontier": dict(frontier), "complete": True}}
