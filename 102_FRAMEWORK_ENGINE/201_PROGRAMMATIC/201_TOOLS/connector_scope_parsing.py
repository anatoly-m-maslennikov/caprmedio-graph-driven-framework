"""Pure declared Scope Unit parsing and logical selection (D626/D627)."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import PurePosixPath
import re
import tomllib

DECLARATION_FIELDS = frozenset({
    "scope_unit_name", "parent", "scope_unit_type", "scope_unit_label", "structural_level",
    "local_order", "navigational_order_number", "authority_path", "delivery_path", "authority_mode",
})
NAME = re.compile(r"^[A-Z0-9]+(?:_[A-Z0-9]+)*$")

QUERY_FIELDS = frozenset({
    "scope_unit_name", "scope_unit_type", "scope_unit_label", "parent",
    "structural_level", "local_order", "navigational_order_number",
})
PREDICATE_FIELDS = QUERY_FIELDS - {"structural_level", "local_order", "navigational_order_number"}


class ScopeDataError(ValueError):
    def __init__(self, code: str, message: str, field: str | None = None):
        super().__init__(message)
        self.code, self.field = code, field


@dataclass(frozen=True)
class ScopeDeclarations:
    project: dict
    rows: dict[str, dict]

    @property
    def project_name(self) -> str:
        return self.project["name"]


def _schema(condition: bool, message: str) -> None:
    if not condition:
        raise ScopeDataError("schema_invalid", message)


def _name(value: object) -> bool:
    return isinstance(value, str) and bool(NAME.fullmatch(value)) and value != "PROJECT"


def _logical_identity(value: object) -> bool:
    return (isinstance(value, str) and bool(value.strip()) and value == value.strip()
            and value not in {".", "..", "PROJECT"} and not any(char in value for char in "/\\\x00"))


def _path(value: object) -> bool:
    if not isinstance(value, str) or not value or "\\" in value or "\x00" in value:
        return False
    path = PurePosixPath(value)
    return not path.is_absolute() and value not in {".", ".."} and ".." not in path.parts


def parse_scope_sources(settings_source: str, structure_source: str) -> ScopeDeclarations:
    """Parse supplied text only; retain complete rows without normalizing them."""
    try:
        settings, structure = tomllib.loads(settings_source), tomllib.loads(structure_source)
    except (tomllib.TOMLDecodeError, TypeError) as error:
        raise ScopeDataError("schema_invalid", "Scope source is not valid TOML.") from error
    project = settings.get("project")
    _schema(isinstance(project, dict) and isinstance(project.get("name"), str)
            and bool(project["name"].strip()), "Project Settings requires the canonical Project Name.")
    _schema(set(structure) == {"schema_version", "scope_units"}
            and type(structure.get("schema_version")) is int and structure["schema_version"] == 1,
            "Project Structure requires only schema_version=1 and scope_units.")
    rows = structure["scope_units"]
    _schema(isinstance(rows, list), "scope_units must be an array of tables.")
    by_name = {}
    required = set(DECLARATION_FIELDS) - {"local_order", "authority_mode"}
    for row in rows:
        _schema(isinstance(row, dict) and required <= row.keys()
                and row.keys() <= set(DECLARATION_FIELDS), "Invalid Scope Unit declaration fields.")
        name = row["scope_unit_name"]
        _schema(isinstance(name, str) and bool(name), "Scope Unit Name must be nonempty.")
        if name in by_name or name == project["name"]:
            raise ScopeDataError("target_ambiguous", "Duplicate or colliding Scope Unit identity.")
        _schema(_name(name), "Scope Unit Name must be canonical.")
        _schema(row["parent"] == "PROJECT" or _name(row["parent"]), "Invalid Scope Unit parent.")
        _schema(isinstance(row["scope_unit_type"], str) and row["scope_unit_type"] in {"Ordered", "Unordered"},
                "Invalid Scope Unit Type.")
        _schema(isinstance(row["scope_unit_label"], str) and bool(NAME.fullmatch(row["scope_unit_label"])),
                "Invalid Scope Unit Label.")
        for field in ("structural_level", "navigational_order_number"):
            _schema(type(row[field]) is int and row[field] >= (1 if field == "structural_level" else 0),
                    f"Invalid {field}.")
        if row["scope_unit_type"] == "Ordered":
            _schema(type(row.get("local_order")) is int and row["local_order"] >= 0,
                    "Ordered Scope Unit requires a nonnegative Local Order.")
        else:
            _schema("local_order" not in row, "Unordered Scope Unit forbids Local Order.")
        _schema(all(_path(row[field]) for field in ("authority_path", "delivery_path")),
                "Invalid declared binding path.")
        _schema("authority_mode" not in row or (isinstance(row["authority_mode"], str)
                and row["authority_mode"] in {"strict", "casual"}),
                "Invalid explicit authority mode.")
        by_name[name] = dict(row)
    depths = {}
    def depth(name: str, visited: set[str]) -> int:
        _schema(name not in visited, "Scope Unit parentage contains a cycle.")
        if name in depths:
            return depths[name]
        parent = by_name[name]["parent"]
        _schema(parent == "PROJECT" or parent in by_name, "Scope Unit parent is undeclared.")
        value = 1 if parent == "PROJECT" else depth(parent, visited | {name}) + 1
        _schema(by_name[name]["structural_level"] == value, "Structural Level differs from parent depth.")
        depths[name] = value
        return value
    orders = set()
    for name, row in by_name.items():
        depth(name, set())
        if row["scope_unit_type"] == "Ordered":
            order = (row["parent"], row["local_order"])
            _schema(order not in orders, "Duplicate Ordered Local Order under one parent.")
            orders.add(order)
    return ScopeDeclarations(dict(project), by_name)


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
        raise invalid("result_fields must be a duplicate-free array of admitted facts.")
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


def read_declaration(declarations: ScopeDeclarations, identity: str) -> dict:
    row = declarations.project if identity == declarations.project_name else declarations.rows.get(identity)
    if row is None:
        raise ScopeDataError("target_not_found", "Scope Unit target is not declared.", "target")
    return {"identity": identity, "declaration": dict(row)}


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
                        if (declarations.project_name if row["parent"] == "PROJECT" else row["parent"]) == parent]
            names.update(children)
            pending.extend(children)
    matches = []
    for name in sorted(names):
        facts = dict(declarations.rows.get(name, declarations.project))
        facts["scope_unit_name"] = name
        if name == declarations.project_name:
            facts["structural_level"] = 0
        elif facts["parent"] == "PROJECT":
            facts["parent"] = declarations.project_name
        selected = True
        for predicate in filters["predicates"]:
            value = facts.get(predicate["field"])
            wanted, mode = predicate["value"], predicate["match"]
            if not isinstance(value, str) or not {"exact": value == wanted, "prefix": value.startswith(wanted),
                    "suffix": value.endswith(wanted), "contains": wanted in value}[mode]:
                selected = False
                break
        if selected:
            matches.append({"identity": name, "facts": {field: facts[field] for field in filters["result_fields"] if field in facts}})
    return {"matches": matches, "coverage": {"frontier": dict(frontier), "complete": True}}
