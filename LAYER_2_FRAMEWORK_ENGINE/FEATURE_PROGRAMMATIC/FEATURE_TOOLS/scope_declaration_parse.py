"""Pure model and bounded CFEL parser for Scope Unit Declaration Atoms."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from dataclasses import dataclass
import json
from pathlib import Path
import re
from types import MappingProxyType
from typing import Any

import yaml
from yaml.events import AliasEvent, MappingEndEvent, MappingStartEvent, SequenceEndEvent, SequenceStartEvent
from yaml.nodes import MappingNode

from carrier_aliases import carrier_read_view
import subject_notation as notation


PROJECT = "PROJECT"
_ROLE_LETTERS = {"Requirement": "R", "Method": "M", "Evaluation": "E", "Delivery": "D", "Operations": "O"}
_SUBJECT = r'(?:"(?:[^"\\]|\\.)*"|[^.\n]+?)'
_PROPERTY = re.compile(
    rf"Scope Unit//(?P<name>{_SUBJECT})\.(?P<field>ID|Name|Label|order\.ordered|order\.number)"
    r"\s*==\s*(?P<value>.+);\Z"
)
_CONTAINMENT = re.compile(
    rf"Scope Unit//(?P<name>{_SUBJECT})\s+\(\(IS_CONTAINED_BY\)\)\s+"
    rf"(?P<kind>Scope Unit|Project)//(?P<parent>{_SUBJECT});?\Z"
)
_ROOT_NAME = re.compile(rf"Project//(?P<name>{_SUBJECT})\.Name\s*==\s*(?P<value>.+)\Z")
_QUOTED = r'"(?:[^"\\]|\\.)*"'
_PAIR_LITERAL = rf'(?:{_QUOTED}|[^"();\n]+?)'
_DELEGATION_RECEIVER = re.compile(
    rf'Atom//(?P<atom>{_QUOTED})\s+\(\(HAS_ACTIVE_SUBJECT\)\)\s+'
    rf'Scope Unit//(?P<name>{_PAIR_LITERAL});?\Z'
)
_ADMITTED_PAIR = re.compile(
    rf"Atom/\(\.Header\.(?:Context\.)?Container\.scope_unit in \("
    rf"(?:Scope Unit//(?P<scope>{_PAIR_LITERAL})|(?P<scope_id>{_QUOTED}))\)\)"
    rf"/\(\.Header\.(?:Context\.)?Role in \((?P<role>{_PAIR_LITERAL})\)\)\.Header\.(?:Context\.)?Form :: (?P<form>{_PAIR_LITERAL});?\Z"
)
_CLAIM = re.compile(r"(?ms)^## Claim\s*\n+```CFEL\n(?P<cfel>.*?)\n```\s*\Z")
_NAMESPACE_BRANCH = "STRUCTURE"


class ScopeDeclarationError(ValueError):
    """A Scope Unit Declaration is not one exact admitted source."""


_SAFE_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)


class _UniqueSafeLoader(_SAFE_LOADER):
    """The bounded reader needs no project-aware metadata import to parse YAML."""

    def construct_mapping(self, node: MappingNode, deep: bool = False) -> dict[Any, Any]:
        result: dict[Any, Any] = {}
        for key_node, value_node in node.value:
            if key_node.tag == "tag:yaml.org,2002:merge":
                raise ScopeDeclarationError("YAML merge keys are unsupported")
            key = self.construct_object(key_node, deep=deep)
            if not isinstance(key, str) or key in result:
                raise ScopeDeclarationError("frontmatter keys must be unique strings")
            result[key] = self.construct_object(value_node, deep=deep)
        return result


def _carrier(raw: bytes, source: Path) -> tuple[dict[str, Any], str]:
    """Safely parse one carrier without importing project selection through metadata helpers."""
    try:
        text = raw.decode("utf-8").replace("\r\n", "\n")
        if not text.startswith("---\n"):
            raise ScopeDeclarationError(f"{source}: declaration requires YAML frontmatter")
        closing = text.find("\n---\n", 4)
        if closing < 0:
            raise ScopeDeclarationError(f"{source}: declaration frontmatter is unterminated")
        frontmatter, body = text[4:closing], text[closing + 5:]
        depth = 0
        for count, event in enumerate(yaml.parse(frontmatter, Loader=_SAFE_LOADER), 1):
            if isinstance(event, AliasEvent):
                raise ScopeDeclarationError(f"{source}: YAML aliases are unsupported")
            if isinstance(event, (MappingStartEvent, SequenceStartEvent)):
                depth += 1
            if isinstance(event, (MappingEndEvent, SequenceEndEvent)):
                depth -= 1
            if depth > 64 or count > 100_000:
                raise ScopeDeclarationError(f"{source}: YAML exceeds parser safety limits")
        metadata = yaml.load(frontmatter, Loader=_UniqueSafeLoader)
        if not isinstance(metadata, dict):
            raise ScopeDeclarationError(f"{source}: frontmatter must contain one mapping")
        return carrier_read_view(metadata), body
    except ScopeDeclarationError:
        raise
    except (UnicodeError, yaml.YAMLError, RuntimeError, ValueError) as error:
        raise ScopeDeclarationError(f"{source}: invalid declaration carrier") from error


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def _string(value: str) -> str:
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError as error:
        raise ScopeDeclarationError("declaration strings must use JSON double quotes") from error
    if not isinstance(parsed, str):
        raise ScopeDeclarationError("declaration value must be a string")
    return parsed


def _subject(value: str) -> str:
    value = value.strip()
    if value.startswith('"'):
        return _string(value)
    if not value or '"' in value:
        raise ScopeDeclarationError("declaration Subject is invalid")
    return value


def _safe_component(value: object, field: str) -> str:
    if (not isinstance(value, str) or not value or value in {".", ".."}
            or any(character in value for character in ("/", "\\", "\x00"))):
        raise ScopeDeclarationError(f"{field} must be a nonempty safe path component")
    return value


def _metadata(value: Mapping[str, Any], path: Path) -> tuple[str, int, str | None, str, str]:
    role = value.get("role", value.get("content_role"))
    if isinstance(role, str):
        role = next((name for name in _ROLE_LETTERS if name.lower() == role.lower()), role)
    raw_form = value.get("form", value.get("type"))
    form = ({"scope_unit_declaration": "Scope Unit Declaration", "scope_delegation": "Scope Delegation"}.get(raw_form, raw_form)
            if isinstance(raw_form, str) else raw_form)
    atom_id, version, status = value.get("atom_id"), value.get("version"), value.get("status")
    if status == "active":
        status = "Active"
    if not isinstance(role, str) or role not in _ROLE_LETTERS or form not in ("Scope Unit Declaration", "Scope Delegation") or status != "Active":
        raise ScopeDeclarationError(f"{path}: not an active Requirement Scope Unit Declaration or Scope Delegation")
    if not isinstance(atom_id, str) or re.fullmatch(rf"CA-{_ROLE_LETTERS[role]}-[1-9][0-9]*", atom_id) is None:
        raise ScopeDeclarationError(f"{path}: declaration requires an assigned identity matching its Role")
    if form == "Scope Unit Declaration" and role != "Requirement":
        raise ScopeDeclarationError(f"{path}: Scope Unit Declaration requires Requirement Role")
    if type(version) is not int or version < 1:
        raise ScopeDeclarationError(f"{path}: declaration Version must be a positive integer")
    topics = value.get("topics")
    subjects = value.get("subjects")
    has_main_subject = isinstance(topics, Mapping) and "main_subject" in topics
    has_legacy_active = isinstance(subjects, Mapping) and "active" in subjects
    if has_main_subject and has_legacy_active and topics["main_subject"] != subjects["active"]:
        raise ScopeDeclarationError(f"{path}: declaration has ambiguous main Subject metadata")
    active = topics["main_subject"] if has_main_subject else subjects.get("active") if has_legacy_active else None
    if active is None and not has_main_subject and not has_legacy_active:
        return atom_id, version, None, form, role
    if not isinstance(active, str):
        raise ScopeDeclarationError(f"{path}: declaration requires one main Subject")
    active = _local_subject(active, path)
    for encoded, canonical in (("scope_unit//", "Scope Unit//"), ("project//", "Project//")):
        if active.startswith(encoded):
            active = canonical + active[len(encoded):]
            break
    return atom_id, version, active, form, role


def _local_subject(active: str, path: Path) -> str:
    """Unwrap one exact structural namespace while retaining legacy bare Subjects."""
    try:
        expression = notation.parse_subject_expression(active, subject_profile="approved").expression
    except notation.SubjectNotationError:
        return active
    local = notation.namespace_local_expression(expression)
    if local is None:
        return active
    if not isinstance(expression, notation.RelationChain):
        return active
    root = expression.endpoints[0]
    new_root = isinstance(root.head, notation.Name) and (
        root.head.value.startswith("CAPRMEDIO_") or root.head.value in {"MODEL", "PROJECT STRUCTURE"}
    )
    namespace = root if new_root else expression.endpoints[1]
    expected = {"CAPRMEDIO_STRUCTURE", "PROJECT STRUCTURE"} if new_root else {_NAMESPACE_BRANCH}
    if not isinstance(namespace.head, notation.Name) or namespace.head.value not in expected:
        raise ScopeDeclarationError(f"{path}: declaration active Subject uses an invalid namespace branch")
    if any(
        link.forward_cardinality is not None or link.reverse_cardinality is not None
        for link in expression.links[:1 if new_root else 2]
    ):
        raise ScopeDeclarationError(f"{path}: declaration active Subject uses an invalid namespace chain")
    return notation.render_subject(local)


def _cfel(body: str, path: Path, *, allow_claim_prose: bool = False) -> list[str]:
    lines = body.splitlines()
    headings = []
    fence = None
    cfel_count = 0
    for index, line in enumerate(lines):
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            token, suffix = marker.groups()
            if fence is None:
                fence = (token[0], len(token))
                cfel_count += suffix.strip() == "CFEL"
            elif token[0] == fence[0] and len(token) >= fence[1] and not suffix.strip():
                fence = None
            continue
        if fence is None:
            heading = re.fullmatch(r"(#{1,6}) (.+)", line)
            if heading:
                headings.append((len(heading[1]), heading[2], index))
    if fence is None and cfel_count == 0 and allow_claim_prose:
        claims = [row for row in headings if row[:2] == (2, "Claim")]
        prose = [row for row in headings if row[:2] == (3, "Prose Claim")]
        formal = [row for row in headings if row[:2] == (3, "Formal Claim")]
        if len(claims) == len(prose) == 1 and not formal and prose[0][2] > claims[0][2]:
            end = next((row[2] for row in headings if row[2] > prose[0][2] and row[0] <= 3), len(lines))
            if "\n".join(lines[prose[0][2] + 1:end]).strip():
                return []
    if fence is not None or cfel_count != 1:
        raise ScopeDeclarationError(f"{path}: declaration requires one unambiguous CFEL block")
    claims = [row for row in headings if row[:2] == (2, "Claim")]
    if len(claims) != 1:
        raise ScopeDeclarationError(f"{path}: declaration requires one CFEL Claim")
    start = claims[0][2]
    boundaries = {(2, name) for name in ("Summary", "Scope", "Claim scope", "Claim", "Semantics", "Details")}
    end = next((row[2] for row in headings if row[2] > start and row[:2] in boundaries), len(lines))
    children = [row for row in headings if start < row[2] < end
                and row[:2] in {(3, "Formal Claim"), (3, "Prose Claim")}]
    claim = "\n".join(lines[start + 1:end]).strip()
    if children:
        formal = [row for row in children if row[1] == "Formal Claim"]
        if len(formal) != 1 or len({row[1] for row in children}) != len(children):
            raise ScopeDeclarationError(f"{path}: declaration requires one Formal Claim")
        formal_start = formal[0][2]
        formal_end = next((row[2] for row in children if row[2] > formal_start), end)
        if not allow_claim_prose and "\n".join(lines[start + 1:children[0][2]]).strip():
            raise ScopeDeclarationError(f"{path}: ambiguous Claim container")
        claim = "\n".join(lines[formal_start + 1:formal_end]).strip()
    matched = re.fullmatch(r"```CFEL\n(?P<cfel>.*?)\n```", claim, re.DOTALL)
    if matched is None:
        raise ScopeDeclarationError(f"{path}: declaration requires one CFEL Claim")
    statements = [line.strip() for line in matched["cfel"].splitlines() if line.strip() and not line.lstrip().startswith("#")]
    if not statements:
        raise ScopeDeclarationError(f"{path}: declaration Claim is empty")
    return statements


@dataclass(frozen=True)
class ScopeDelegation:
    name: str
    atom_id: str
    version: int
    source: Path
    admitted_role_forms: tuple[tuple[str, str], ...]
    pair_receivers: tuple[tuple[str, str], ...]
    parent_id: str | None = None
    role: str = "Requirement"


@dataclass(frozen=True)
class ScopeUnitDeclaration:
    """One parsed source; paths are derived only after the complete tree is known."""

    name: str
    atom_id: str
    version: int
    source: Path
    form: str = "Scope Unit Declaration"
    scope_unit_id: str | None = None
    label: str | None = None
    ordered: bool = False
    local_order: int | None = None
    parent: str | None = None
    admitted_role_forms: tuple[tuple[str, str], ...] = ()
    delegations: tuple[ScopeDelegation, ...] = ()

    @property
    def scope_unit_type(self) -> str:
        return "Ordered" if self.ordered else "Unordered"

    @property
    def is_root(self) -> bool:
        return self.scope_unit_id is None


def parse_scope_unit_declaration(raw: bytes, source: Path) -> ScopeUnitDeclaration | ScopeDelegation:
    """Parse one already-read carrier without traversing, evaluating, or writing."""
    metadata, body = _carrier(raw, source)
    atom_id, version, active, form, role = _metadata(metadata, source)
    statements = _cfel(body, source, allow_claim_prose=form == "Scope Delegation")

    root = _ROOT_NAME.fullmatch(statements[0]) if len(statements) == 1 else None
    if root is not None:
        if form != "Scope Unit Declaration":
            raise ScopeDeclarationError(f"{source}: Project Scope Unit must use Scope Unit Declaration")
        name = _subject(root["name"])
        if (active is not None and active != f"Project//{name}") or _string(root["value"]) != name:
            raise ScopeDeclarationError(f"{source}: root declaration identity is contradictory")
        return ScopeUnitDeclaration(name=name, atom_id=atom_id, version=version, source=source, form=form)

    values: dict[str, str | bool | int] = {}
    parent: str | None = None
    name: str | None = None
    formal_receiver: str | None = None
    pair_receivers: list[tuple[str, str]] = []
    admitted_pairs: list[tuple[str, str]] = []
    for statement in statements:
        receiver_match = _DELEGATION_RECEIVER.fullmatch(statement)
        if receiver_match is not None and form == "Scope Delegation":
            if formal_receiver is not None or _string(receiver_match["atom"]) != atom_id:
                raise ScopeDeclarationError(f"{source}: duplicate or incorrect delegation receiver binding")
            formal_receiver = _safe_component(_subject(receiver_match["name"]), "Scope Unit Name")
            continue
        pair_match = _ADMITTED_PAIR.fullmatch(statement)
        if pair_match is not None and form == "Scope Delegation":
            pair = (_subject(pair_match["role"]), _subject(pair_match["form"]))
            if not all(pair):
                raise ScopeDeclarationError(f"{source}: admitted Role/Form values must be nonempty")
            if pair in admitted_pairs:
                raise ScopeDeclarationError(f"{source}: duplicate admitted Role/Form pair")
            if pair_match["scope_id"] is not None:
                pair_receivers.append(("ID", _string(pair_match["scope_id"])))
            else:
                pair_receivers.append(("Name", _subject(pair_match["scope"])))
            admitted_pairs.append(pair)
            continue
        property_match = _PROPERTY.fullmatch(statement)
        if property_match is not None:
            candidate, field, raw_value = _subject(property_match["name"]), property_match["field"], property_match["value"]
            if name is None:
                name = candidate
            if candidate != name or field in values:
                raise ScopeDeclarationError(f"{source}: duplicate or mixed Scope Unit Claim")
            if field in {"ID", "Name", "Label"}:
                values[field] = _string(raw_value)
            elif field == "order.ordered":
                if raw_value not in {"true", "false"}:
                    raise ScopeDeclarationError(f"{source}: order.ordered must be true or false")
                values[field] = raw_value == "true"
            else:
                if re.fullmatch(r"[1-9][0-9]*", raw_value) is None:
                    raise ScopeDeclarationError(f"{source}: order.number must be a positive integer")
                values[field] = int(raw_value)
            continue
        containment = _CONTAINMENT.fullmatch(statement)
        if containment is None or parent is not None:
            raise ScopeDeclarationError(f"{source}: unsupported or ambiguous declaration Claim")
        candidate = _subject(containment["name"])
        if name is None:
            name = candidate
        if candidate != name:
            raise ScopeDeclarationError(f"{source}: mixed Scope Unit Claim")
        parent = _subject(containment["parent"])

    if form == "Scope Delegation" and not values and parent is None:
        if formal_receiver is not None:
            if active is not None and active != f"Scope Unit//{formal_receiver}":
                raise ScopeDeclarationError(f"{source}: delegation Main Subject contradicts its formal receiver")
            receiver_name = formal_receiver
        elif active is not None and active.startswith("Scope Unit//") and active[len("Scope Unit//"):]:
            receiver_name = active[len("Scope Unit//"):]
        else:
            raise ScopeDeclarationError(f"{source}: delegation requires a Scope Unit receiver")
        container = metadata.get("container")
        parent_id = container.get("scope_unit") if isinstance(container, Mapping) else None
        return ScopeDelegation(
            name=receiver_name, atom_id=atom_id, version=version, source=source,
            admitted_role_forms=tuple(admitted_pairs), pair_receivers=tuple(pair_receivers), parent_id=parent_id,
            role=role,
        )

    if role != "Requirement":
        raise ScopeDeclarationError(f"{source}: structural topology requires Requirement Role")
    if formal_receiver is not None:
        raise ScopeDeclarationError(f"{source}: structural Claim cannot contain a delegation receiver binding")

    if (name is None or (active is not None and active != f"Scope Unit//{name}")
            or set(values) - {"ID", "Name", "Label", "order.ordered", "order.number"}):
        raise ScopeDeclarationError(f"{source}: invalid Scope Unit declaration identity")
    scope_unit_id, declared_name, ordered = values.get("ID"), values.get("Name"), values.get("order.ordered")
    label, local_order = values.get("Label"), values.get("order.number")
    if (declared_name != name or not isinstance(ordered, bool) or parent is None):
        raise ScopeDeclarationError(f"{source}: declaration lacks an exact ID, Name, order, or parent")
    scope_unit_id = _safe_component(scope_unit_id, "Scope Unit ID")
    if any(values[field] != receiver for field, receiver in pair_receivers):
        raise ScopeDeclarationError(f"{source}: admitted Role/Form pair names another Scope Unit")
    _safe_component(name, "Scope Unit Name")
    if label is not None:
        _safe_component(label, "Scope Unit Label")
    if ordered != isinstance(local_order, int):
        raise ScopeDeclarationError(f"{source}: order.number is required only for ordered Scope Units")
    return ScopeUnitDeclaration(
        name=name, atom_id=atom_id, version=version, source=source, form=form, scope_unit_id=scope_unit_id,
        label=label, ordered=ordered, local_order=local_order, parent=parent,
        admitted_role_forms=tuple(admitted_pairs),
    )


def _component(declaration: ScopeUnitDeclaration, *, authority: bool) -> str:
    parts = [declaration.scope_unit_id] if authority else []
    if declaration.label:
        parts.append(declaration.label)
    if declaration.ordered:
        parts.append(str(declaration.local_order))
    parts.append(declaration.name)
    return "_".join(part for part in parts if part)


@dataclass(frozen=True)
class ScopeUnitDeclarations:
    """Validated declaration tree plus the selected-source provenance."""

    root: ScopeUnitDeclaration
    units: tuple[ScopeUnitDeclaration, ...]
    by_name: Mapping[str, ScopeUnitDeclaration]
    paths: tuple[Path, ...]
    source_pins: Mapping[str, Mapping[str, Any]]
    digest: str
    _authority_paths: Mapping[str, Path]
    _delivery_paths: Mapping[str, Path]

    def __post_init__(self) -> None:
        object.__setattr__(self, "by_name", MappingProxyType(dict(self.by_name)))
        object.__setattr__(self, "source_pins", MappingProxyType({
            path: MappingProxyType(dict(pin)) for path, pin in self.source_pins.items()
        }))
        object.__setattr__(self, "_authority_paths", MappingProxyType(dict(self._authority_paths)))
        object.__setattr__(self, "_delivery_paths", MappingProxyType(dict(self._delivery_paths)))

    def as_structure(self) -> dict[str, list[dict[str, Any]]]:
        """Return the former private structure view, derived from declarations."""
        declarations = (self.root, *self.units)
        return {"scope_units": [
            {
                "scope_unit_name": declaration.name,
                "parent": PROJECT if declaration.is_root else declaration.parent,
                "scope_unit_id": declaration.scope_unit_id,
                "scope_unit_label": declaration.label,
                "scope_unit_type": declaration.scope_unit_type,
                "admitted_role_forms": declaration.admitted_role_forms,
                **({"local_order": declaration.local_order} if declaration.ordered else {}),
                "authority_path": self._authority_paths[declaration.name].as_posix(),
                "delivery_path": self._delivery_paths[declaration.name].as_posix(),
            }
            for declaration in declarations
        ]}

    def __deepcopy__(self, memo: dict[int, Any]) -> ScopeUnitDeclarations:
        """Keep the immutable declaration aggregate shared across copied inputs."""
        memo[id(self)] = self
        return self


def assemble_scope_unit_declarations(
    declarations: Iterable[ScopeUnitDeclaration], *, project_root: Path, control_root: Path,
    source_pins: Mapping[str, Mapping[str, Any]], digest: str,
) -> ScopeUnitDeclarations:
    """Validate one complete tree and derive its authority/delivery paths."""
    rows = tuple(declarations)
    roots = [row for row in rows if row.is_root]
    if len(roots) != 1:
        raise ScopeDeclarationError("exactly one Project root declaration is required")
    root = roots[0]
    if root.name in {row.name for row in rows if not row.is_root}:
        raise ScopeDeclarationError("Project name cannot also name a Scope Unit")
    units = tuple(sorted((row for row in rows if not row.is_root), key=lambda row: row.name))
    by_name = {root.name: root}
    identifiers: set[str] = set()
    for row in units:
        if row.name in by_name or row.scope_unit_id in identifiers:
            raise ScopeDeclarationError("Scope Unit names and IDs must be unique")
        by_name[row.name] = row
        identifiers.add(str(row.scope_unit_id))
    for row in units:
        if row.parent not in by_name or row.parent == row.name:
            raise ScopeDeclarationError(f"Scope Unit parent is missing or self-referential: {row.name}")
    resolving: set[str] = set()
    resolved: set[str] = {root.name}

    def validate_parent(name: str) -> None:
        if name in resolved:
            return
        if name in resolving:
            raise ScopeDeclarationError("Scope Unit containment is cyclic")
        resolving.add(name)
        parent = by_name[name].parent
        if parent is None:
            raise ScopeDeclarationError("nonroot Scope Unit lacks a parent")
        validate_parent(parent)
        resolving.remove(name)
        resolved.add(name)

    for row in units:
        validate_parent(row.name)
    sibling_orders: set[tuple[str, int]] = set()
    for row in units:
        if row.ordered:
            key = (str(row.parent), int(row.local_order))
            if key in sibling_orders:
                raise ScopeDeclarationError("ordered siblings cannot share order.number")
            sibling_orders.add(key)
    authority_paths = {root.name: control_root.relative_to(project_root)}
    delivery_paths = {root.name: Path(".")}
    pending = list(units)
    while pending:
        remaining = []
        for row in pending:
            parent = str(row.parent)
            if parent not in authority_paths:
                remaining.append(row)
                continue
            authority_paths[row.name] = authority_paths[parent] / _component(row, authority=True)
            delivery_paths[row.name] = delivery_paths[parent] / _component(row, authority=False)
        if len(remaining) == len(pending):
            raise ScopeDeclarationError("Scope Unit containment cannot derive paths")
        pending = remaining
    return ScopeUnitDeclarations(
        root=root, units=units, by_name=by_name,
        paths=tuple(sorted({row.source for row in rows} | {
            delegation.source for row in rows for delegation in row.delegations
        }, key=lambda path: path.as_posix())),
        source_pins=source_pins, digest=digest,
        _authority_paths=authority_paths, _delivery_paths=delivery_paths,
    )


__all__ = [
    "PROJECT", "ScopeDeclarationError", "ScopeDelegation", "ScopeUnitDeclaration", "ScopeUnitDeclarations",
    "assemble_scope_unit_declarations", "parse_scope_unit_declaration",
]
