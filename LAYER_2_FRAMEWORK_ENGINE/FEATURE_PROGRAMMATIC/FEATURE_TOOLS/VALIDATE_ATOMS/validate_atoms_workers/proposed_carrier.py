"""Finite, source-bound admission for a proposed complete Atom carrier."""

from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from carrier_aliases import carrier_read_view

from .authority import (
    AuthorityContext, Obligation, Record, _verified, current_role_declaration, resolve_context,
)
from .check_operators import load_operators_registry
from .checks import validate_carrier
from .context import load_source
from .read_io import ReadContext
from .settings import CEILINGS
from .support_authority import matches_source_pin, support_sources
from .check_support import Check
from .check_graph_extended import relations_resolution, plan_resolution
from .check_schema_extended import TYPE_CONTRIBUTIONS, declared_type_coordinate
from .check_fields import reviewed_encoding_profile
from .check_sections import GRAPH_RULE_SOURCES, is_graph_rule
from .proposed_references import (
    ProposedReferenceError, ProposedReferenceInventory, _container_id, _plan_container,
    inventory_proposed_references,
)
from .parsing import CarrierError, parse_carrier
from .graph_authority_refresh import APPROVED_GRAPH_AUTHORITY_IDS
from artifact_metadata import project_identity
from authoritative_status_models import (
    StatusModelError, StatusModelIndex, capture_status_models,
    declarations_from_sources, resolve_status_domain, resolve_status_model, revalidate_status_models,
)
from project_selection import ProjectSelection, active_selection, bind_selection, bound_selection
from scope_unit_declarations import read_scope_unit_declarations


_REGISTRY_IDS = (
    "CA-D-276", "CA-D-269", "CA-D-268", "CA-D-270", "CA-D-446",
    "CA-D-479", "CA-D-483",
)
_LEGACY_REGISTRY_IDS = ("CA-D-274", "CA-D-482")
_SUPPORT_IDS = (
    "CA-D-494", "CA-D-442", "CA-R-1308", "CA-R-1313",
    "CA-D-324", "CA-D-466", "CA-D-461",
    "CA-D-288", "CA-D-378",
    *(identifier for identifier in TYPE_CONTRIBUTIONS if identifier not in GRAPH_RULE_SOURCES),
    "CA-R-1283", "CA-R-1700", "CA-R-1506",
)
_DEFERRED_SUPPORT_IDS = frozenset({"CA-D-378"})
_CURRENT_CONTAINMENT_SOURCE_IDS = ("CA-R-2508", "CA-R-2523", "CA-R-2511")
_EXACT_PIN_SOURCE_IDS = frozenset({"CA-D-378", *_CURRENT_CONTAINMENT_SOURCE_IDS})
_GRAPH_IDS = tuple(sorted(APPROVED_GRAPH_AUTHORITY_IDS))
_FRONTIER_STATUS_IDS = {
    "Concern": "CA-R-1608", "Analysis": "CA-R-1875", "Plan": "CA-R-1539",
    "Requirement": "CA-R-1309", "Method": "CA-R-1397", "Evaluation": "CA-R-1398",
    "Delivery": "CA-R-1399", "Operations": "CA-R-1874",
}
_FRONTIER_IDS = ("CA-D-434", "CA-D-467", "CA-D-460", "CA-D-481", *_FRONTIER_STATUS_IDS.values())
_LEGACY_CODES = frozenset(
    {
        "frontmatter.common_encoding", "frontmatter.version", "frontmatter.updated_at",
        "frontmatter.author", "author.resolution", "frontmatter.atom_id",
        "frontmatter.subjects", "frontmatter.relations", "frontmatter.claim_target_scope_unit",
        "target.resolution", "frontmatter.status",
        "body.sections", "model.domains",
    }
)
_CURRENT_CODES = _LEGACY_CODES - {
    "frontmatter.author", "author.resolution", "frontmatter.claim_target_scope_unit", "target.resolution",
} | {"domain.content_role"}


class ProposedCarrierError(ValueError):
    """The finite pre-write carrier boundary is unavailable or failed."""


@dataclass(frozen=True)
class VerifiedSourceContext:
    root: Path
    authority: AuthorityContext
    inputs: Record
    _selection: ProjectSelection
    _reader: ReadContext


@dataclass
class CarrierValidationScope:
    """Own one pure-preview or scratch-stage validation closure, never apply."""

    root: Path
    _context: VerifiedSourceContext | None = None
    _status_index: StatusModelIndex | None = None

    def validate(self, root: Path, metadata: Record, body: str, relative_path: Path,
                 *, allow_existing_relations: bool) -> Record:
        if root.resolve() != self.root:
            raise ProposedCarrierError("validation scope belongs to another Project")
        if self._context is None:
            self._context = source_context_from_project(self.root)
            with bind_selection(self._context._selection):
                self._status_index = capture_status_models(self.root, self._context._reader)
        if self._status_index is None:
            raise ProposedCarrierError("status-model validation scope is incomplete")
        return validate_proposed_carrier(metadata, body, self._context, relative_path,
                                         allow_existing_relations=allow_existing_relations,
                                         _status_index=self._status_index)

    def revalidate(self) -> None:
        if self._context is not None:
            _current(self._context._reader, self._context._selection)
            if self._status_index is None:
                raise ProposedCarrierError("status-model validation scope is incomplete")
            _status_current(self._context, self._status_index)
            _current(self._context._reader, self._context._selection)


def _status_current(context: VerifiedSourceContext, index: StatusModelIndex) -> None:
    try:
        with bind_selection(context._selection):
            revalidate_status_models(index, context._reader)
    except StatusModelError as error:
        raise ProposedCarrierError("status-model sources changed during admission") from error


def _entry(identifier: str, *, graph: bool = False) -> Record:
    registry = json.loads(Path(__file__).with_name("registry.json").read_text(encoding="utf-8"))["sources"]
    graph_entries = json.loads(Path(__file__).with_name("graph_authority.json").read_text(encoding="utf-8"))["sources"]
    if graph and identifier in APPROVED_GRAPH_AUTHORITY_IDS:
        return graph_entries.get(identifier) or {}
    return registry.get(identifier) or support_sources().get(identifier) or graph_entries.get(identifier) or {}


def _source(
    root: Path,
    identifier: str,
    reader: ReadContext,
    report: Record,
    *,
    graph: bool = False,
    locator: Any | None = None,
    exact_pin: bool = True,
) -> Record:
    entry = _entry(identifier, graph=graph)
    path = entry.get("source_path") if isinstance(entry, dict) else None
    if not isinstance(path, str) or not path or Path(path).is_absolute() or ".." in Path(path).parts:
        raise ProposedCarrierError("required source locator is unavailable")
    selection = bound_selection(root)
    if selection is not None and Path(path).is_relative_to('.caprmedio_caprmedio'):
        path = (selection.control_relative / Path(path).relative_to('.caprmedio_caprmedio')).as_posix()
    absolute = root / path
    if not absolute.exists() and not absolute.is_symlink():
        if locator is None:
            from current_atom_locator import CurrentAtomLocator
            locator = CurrentAtomLocator(root, reader=reader)
        path = locator.locate(identifier, path)
        absolute = root / path
    item = load_source(absolute, None, reader, report)
    if (item is None or item["metadata"].get("atom_id") != identifier
            or not _verified(item, entry)
            or (exact_pin and identifier in _EXACT_PIN_SOURCE_IDS and not matches_source_pin(item, entry))):
        raise ProposedCarrierError("required source is unreadable, changed, or inactive: " + identifier)
    return item


def _plan_folder(raw: object) -> str:
    if (not isinstance(raw, str) or raw.startswith(("/", "\\"))
            or re.match(r"^[A-Za-z]:[\\/]", raw)
            or any(part in {"", ".", ".."} or "\\" in part for part in raw.split("/"))):
        raise ProposedCarrierError("Plan status-directory authority is unsafe")
    parts = raw.split("/")
    if parts[0] == "03_plan":
        parts = parts[1:]
    if len(parts) != 1 or re.fullmatch(r"[A-Za-z0-9_-]+", parts[0]) is None:
        raise ProposedCarrierError("Plan status-directory authority has an invalid role path")
    return parts[0]


def _plan_mapping(source: str | dict[str, str]) -> dict[str, str]:
    """Read the finite Plan placement map without admitting arbitrary paths."""
    if isinstance(source, str):
        entries = re.findall(r"(?m)^-\s+([A-Za-z]+):.*?`([^`]+)`", source)
    elif isinstance(source, dict):
        entries = list(source.items())
    else:
        raise ProposedCarrierError("Plan status-directory authority is unavailable")
    mapping = {}
    for status, raw in entries:
        if not isinstance(status, str) or not status or status in mapping:
            raise ProposedCarrierError("Plan status-directory authority is ambiguous")
        mapping[status] = "" if status == "Active" and raw == "" else _plan_folder(raw)
    mapping.setdefault("Active", "")
    return mapping


def _encoding_source(root: Path, reader: ReadContext, report: Record, locator: Any) -> Record:
    from current_atom_locator import CurrentAtomLocatorError

    # Probe the new identity without treating an absent Current source as a
    # retired-ID alias. Historical disposable Projects still select D276.
    entry = json.loads(Path(__file__).with_name("registry.json").read_text())["sources"]["CA-D-657"]
    path = Path(entry["source_path"])
    selection = bound_selection(root)
    if selection is not None:
        path = selection.control_relative / path.relative_to(".caprmedio_caprmedio")
    try:
        locator.locate("CA-D-657", path)
    except CurrentAtomLocatorError as error:
        if error.code != "atom-identity-not-found":
            raise
        return _source(root, "CA-D-276", reader, report, locator=locator)
    source = _source(root, "CA-D-657", reader, report, locator=locator)
    try:
        _source(root, "CA-D-276", reader, report, locator=locator)
    except CurrentAtomLocatorError as error:
        if error.code != "atom-identity-not-found":
            raise
    else:
        raise ProposedCarrierError("frontmatter encoding authority is ambiguous")
    if reviewed_encoding_profile(source) != "current":
        raise ProposedCarrierError("Current frontmatter encoding authority is unreviewed")
    return source


def _current_role_sources(
    root: Path, reader: ReadContext, report: Record, locator: Any,
) -> list[Record]:
    """Bind the finite Current Role cases from their own active Declarations."""
    sources = []
    for path, _, carried, _ in locator._index("04_requirement"):
        if (
            not isinstance(carried, dict)
            or carried.get("atom_id") in _CURRENT_CONTAINMENT_SOURCE_IDS
            or carried.get("role") != "Requirement"
            or carried.get("form") != "Declaration"
        ):
            continue
        source = load_source(path, None, reader, report)
        if source is None or current_role_declaration(source) is None:
            continue
        locator.assert_unique_current_claim(source["binding"]["atom_id"], path)
        sources.append(source)
    return sources


def source_context_from_project(root: Path) -> VerifiedSourceContext:
    """Load just the finite checked authority closure and selected Project inputs."""

    from current_atom_locator import CurrentAtomLocator

    root = root.resolve()
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    try:
        selection = active_selection(root)
        selection._revalidate_boundary(reader=reader)
        control = selection.control_relative
        pins = {
            selection.settings_path.relative_to(root).as_posix():
                selection.provenance.get(selection.settings_path.relative_to(root).as_posix(), {}).get("sha256"),
            **{path: pin.get("sha256") for path, pin in selection.declaration_source_pins.items()},
        }
        for path in (selection.settings_path, *selection.declaration_paths):
            raw = reader.read(path)
            if hashlib.sha256(raw).hexdigest() != pins.get(path.relative_to(root).as_posix()):
                raise ProposedCarrierError("selected Project context changed after selection")
        declarations = read_scope_unit_declarations(root, selection.control_root, reader=reader)
        if declarations.digest != selection.declaration_digest:
            raise ProposedCarrierError("selected Scope Unit Declaration aggregate changed after selection")
        # Checks may deepcopy their inputs.  Keep the frozen Selection private
        # and provide a fresh, mutable derived view from the declaration model.
        structure = declarations.as_structure()
        operators = selection.control_root / "operators_registry.toml"
        operator_raw = reader.read(operators)
        with bind_selection(selection):
            identity = project_identity(root)
            locator = CurrentAtomLocator(root, reader=reader)
            encoding = _encoding_source(root, reader, report, locator)
            current_encoding = reviewed_encoding_profile(encoding) == "current"
            support_ids = (
                ("CA-D-494", "CA-D-442", "CA-R-1308", "CA-R-1313",
                 "CA-D-324", "CA-D-466", "CA-D-461", "CA-R-1283")
                if current_encoding else _SUPPORT_IDS
            )
            registry_ids = _REGISTRY_IDS if current_encoding else (*_REGISTRY_IDS, *_LEGACY_REGISTRY_IDS)
            source_ids = (*(identifier for identifier in registry_ids if identifier != "CA-D-276"),
                          *(identifier for identifier in support_ids if identifier not in _DEFERRED_SUPPORT_IDS),
                          *(_CURRENT_CONTAINMENT_SOURCE_IDS if current_encoding else ()))
            sources = [encoding, *[_source(root, identifier, reader, report, locator=locator)
                                   for identifier in source_ids]]
            if current_encoding:
                sources.extend(_current_role_sources(root, reader, report, locator))
    except (OSError, RuntimeError, UnicodeError, ValueError) as error:
        raise ProposedCarrierError("required Project context is unreadable") from error
    inputs: Record = {
        "sources": sources,
        "control_relative": control.as_posix(),
        "structure": structure,
        "scope_unit_declarations": declarations,
        "_project_identity": identity,
        "operators_registry": load_operators_registry(
            {"operators_registry": {"path": str(operators), "sha256": hashlib.sha256(operator_raw).hexdigest()}},
            reader,
        ),
    }
    # These three exact records prove Current containment only.  R2511's
    # Plan selector is not an additional Role-domain declaration.
    authority = resolve_context([
        source for source in sources
        if source["binding"]["atom_id"] not in _CURRENT_CONTAINMENT_SOURCE_IDS
    ])
    try:
        selection._revalidate_boundary(reader=reader)
        locator.revalidate()
    except (OSError, RuntimeError, ValueError) as error:
        raise ProposedCarrierError("selected Project inputs are unavailable") from error
    return VerifiedSourceContext(root, authority, inputs, selection, reader)


def _current(reader: ReadContext, selection: ProjectSelection | None = None) -> None:
    try:
        if selection is not None:
            selection._revalidate_boundary(reader=reader)
        if reader.currentness()["state"] != "unchanged":
            raise ProposedCarrierError("selected Project inputs changed during admission")
    except (OSError, RuntimeError, ValueError) as error:
        raise ProposedCarrierError("selected Project inputs are unavailable") from error


def _frontier_status_folders(context: VerifiedSourceContext, plan_mapping: dict[str, str],
                             status_index: StatusModelIndex | None = None) -> dict[str, dict[str, str]]:
    plan_mapping = _plan_mapping(plan_mapping)
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    with bind_selection(context._selection):
        for identifier in _FRONTIER_IDS:
            _source(context.root, identifier, context._reader, report, graph=identifier in _GRAPH_IDS)
        declarations = (status_index.declarations if status_index is not None
                        else capture_status_models(context.root, context._reader).declarations)
    mappings = {}
    for role, identifier in _FRONTIER_STATUS_IDS.items():
        try:
            statuses = resolve_status_domain(declarations, role)["statuses"]
        except StatusModelError as error:
            raise ProposedCarrierError("reference status-directory authority is unavailable") from error
        mappings[role] = {status: "" if status.casefold() == "active" else status.lower() for status in statuses}
    if set(plan_mapping) != set(mappings["Plan"]):
        raise ProposedCarrierError("reference Plan status-directory authority is incomplete")
    mappings["Plan"] = plan_mapping
    return mappings


def _assigned_identity(context: VerifiedSourceContext, metadata: Record) -> None:
    """Check assigned identity against exact encoding authority and Project Settings."""
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    with bind_selection(context._selection):
        source = _source(context.root, "CA-D-378", context._reader, report)
    letters = dict(re.findall(r"([A-Za-z]+): ([A-Z])(?:,|\))", source["text"]))
    prefix = context.inputs["_project_identity"]["identity"]["project_prefix"]
    identity = metadata.get("atom_id")
    role = metadata.get("role", metadata.get("content_role"))
    if letters:
        letter = letters.get(role)
        matches = (
            isinstance(letter, str)
            and isinstance(identity, str)
            and re.fullmatch(rf"{re.escape(prefix)}-{re.escape(letter)}-[0-9]+", identity) is not None
        )
    else:
        admitted = set(re.findall(r"`([A-Z])`", source["text"]))
        match = (
            re.fullmatch(rf"{re.escape(prefix)}-([A-Z])-[0-9]+", identity)
            if isinstance(identity, str) else None
        )
        matches = (
            match is not None
            and match.group(1) in admitted
            and isinstance(role, str)
            and bool(role)
            and any(current_role_declaration(item) == role for item in context.inputs["sources"])
            and match.group(1) == role[0].upper()
        )
    if not matches:
        raise ProposedCarrierError("assigned Atom identity disagrees with its Project prefix or carried content role")


def _operations_placement(
    context: VerifiedSourceContext, metadata: Record, path: Path, role_root: Path,
    owner: str, rows: list[Record], owner_authority: Path, status_index: StatusModelIndex | None = None,
) -> None:
    """Authenticate only the Workflow/Step ancestors named by this carrier path."""
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    try:
        with bind_selection(context._selection):
            sources = {
                identifier: _source(context.root, identifier, context._reader, report)
                for identifier in ("CA-D-467", "CA-R-1874")
            }
        declarations = (status_index.declarations if status_index is not None
                        else declarations_from_sources(list(sources.values())))
        statuses = resolve_status_domain(declarations, "Operations")["statuses"]
        folders = {status: "" if status == "Active" else status.lower() for status in statuses}
        current, local, nested = role_root, "", False
        for part in path.relative_to(role_root).parts[:-1]:
            if not local and part in {folder for folder in folders.values() if folder}:
                local = part
                current = current / part
                continue
            parent_path = context.root / current / (part + ".md")
            parent = parse_carrier(context._reader.read(parent_path), parent_path).metadata
            _assigned_identity(context, parent)
            if (_container_id(parent, "Operations", owner, folders, local) is None
                    or nested and parent.get("type") != "Step"):
                raise ProposedCarrierError("Operations container parent identity, type, owner, or status is unresolved")
            if parent.get("status") == "Archived":
                with bind_selection(context._selection):
                    _source(context.root, "CA-D-289", context._reader, report)
                if not parent_path.stem.endswith(f"@{parent['version']}"):
                    raise ProposedCarrierError("Archived Operations parent lacks its carried Version suffix")
            current = current / part
            context._reader.allowed(context.root / current)
            nested, local = True, ""
        if nested and metadata.get("type") != "Step":
            raise ProposedCarrierError("Workflow and Step containers admit only Step carriers")
        if folders.get(metadata.get("status")) != local:
            raise ProposedCarrierError("carrier path disagrees with its carried status")
        if metadata.get("status") == "Archived":
            with bind_selection(context._selection):
                _source(context.root, "CA-D-289", context._reader, report)
            if not path.stem.endswith(f"@{metadata['version']}"):
                raise ProposedCarrierError("Archived Operations carrier lacks its carried Version suffix")
        if any(row.get("scope_unit_name") != owner
               and Path(row["authority_path"]).is_relative_to(owner_authority)
               and path.is_relative_to(Path(row["authority_path"]))
               for row in rows):
            raise ProposedCarrierError("Operations container crosses a declared Scope Unit authority")
    except (OSError, RuntimeError, CarrierError, ValueError) as error:
        if isinstance(error, ProposedCarrierError):
            raise
        raise ProposedCarrierError("Operations containment authority or parent carrier is unavailable") from error


def _current_type_source(context: VerifiedSourceContext, metadata: Record) -> Record:
    """Resolve the actual Type definition, including newly allocated identities."""
    from current_atom_locator import CurrentAtomLocator

    coordinate = metadata.get("content_role"), metadata.get("type")
    locator = CurrentAtomLocator(context.root, reader=context._reader)
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    matches = []
    with bind_selection(context._selection):
        # Reuse the locator's bounded registered Requirement-family inventory;
        # path order and references never declare a Type or its authority.
        for path, _, carried, _ in locator._index("04_requirement"):
            if (not isinstance(carried, dict) or carried.get("type") != "Entity Definition"
                    or declared_type_coordinate(carried) != coordinate):
                continue
            source = load_source(path, None, context._reader, report)
            if source is None or not _verified(source, {}):
                raise ProposedCarrierError("Current Type owner is unreadable or inactive")
            locator.assert_unique_current_claim(source["binding"]["atom_id"], path)
            matches.append(source)
        locator.revalidate()
    if len(matches) != 1:
        raise ProposedCarrierError("Current qualified Type requires exactly one Active Entity Definition owner")
    return matches[0]


def _type_inputs(context: VerifiedSourceContext, metadata: Record) -> Record:
    """Load only the additional authority required by the actual proposed Type."""
    inputs = dict(context.inputs)
    known = {row["binding"]["atom_id"] for row in inputs["sources"]}
    if (
        any(reviewed_encoding_profile(row) == "current" for row in context.inputs["sources"])
        and isinstance(metadata.get("type"), str)
        and metadata["type"]
    ):
        source = _current_type_source(context, metadata)
        if source["binding"]["atom_id"] not in known:
            inputs["sources"] = [*inputs["sources"], source]
            known.add(source["binding"]["atom_id"])
    if (metadata.get("content_role"), metadata.get("type")) == ("Requirement", "Goal"):
        identifiers = ("CA-R-924", "CA-R-925", "CA-R-926", "CA-R-947", "CA-R-1392",
                       "CA-R-1389", "CA-R-1390", "CA-R-1391")
    elif is_graph_rule(metadata):
        identifiers = GRAPH_RULE_SOURCES
    else:
        return inputs
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    with bind_selection(context._selection):
        sources = [_source(context.root, identifier, context._reader, report)
                   for identifier in identifiers]
    inputs["sources"] = [*inputs["sources"],
                         *[source for source in sources if source["binding"]["atom_id"] not in known]]
    return inputs


def _validation_inputs(context: VerifiedSourceContext, metadata: Record) -> Record:
    """Load identity authority at validation time, after initial context selection."""
    inputs = _type_inputs(context, metadata)
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    current_profile = any(
        reviewed_encoding_profile(source) == "current" for source in inputs["sources"]
    )
    with bind_selection(context._selection):
        identity_source = _source(
            context.root, "CA-D-378", context._reader, report, exact_pin=current_profile,
        )
    known = {item["binding"]["atom_id"] for item in inputs["sources"]}
    if identity_source["binding"]["atom_id"] in known:
        return inputs
    result = dict(inputs)
    result["sources"] = [*inputs["sources"], identity_source]
    return result


def _target_type_sources(
    context: VerifiedSourceContext, base_sources: list[Record], inventory: ProposedReferenceInventory,
) -> list[Record]:
    sources = list(base_sources)
    known = {source["binding"]["atom_id"] for source in sources}
    items = (*inventory.direct_targets, *inventory.plan_parent_closure, *inventory.plan_prerequisite_closure)
    for item in items:
        for source in _type_inputs(context, item.metadata)["sources"]:
            identifier = source["binding"]["atom_id"]
            if identifier not in known:
                sources.append(source)
                known.add(identifier)
    return sources


def _current_containment_target(metadata: Mapping[str, Any], *, label: str) -> tuple[str, str]:
    """Return one literal Current containment target without creating legacy aliases."""
    relations = metadata.get("relations")
    if not isinstance(relations, Mapping):
        raise ProposedCarrierError(label + " relation is malformed")
    containment = relations.get("IS_CONTAINED_BY")
    if not isinstance(containment, Mapping):
        raise ProposedCarrierError(label + " lacks one canonical containment relation")
    fields = set(containment)
    if fields not in ({"scope_unit"}, {"atom"}):
        raise ProposedCarrierError(label + " is unresolved or ambiguous")
    field = next(iter(fields))
    value = containment.get(field)
    if not isinstance(value, str) or not value:
        raise ProposedCarrierError(label + " is unresolved or ambiguous")
    return field, value


def _current_containment_owner(
    context: VerifiedSourceContext, raw_metadata: Record, *, status_index: StatusModelIndex | None = None,
) -> str:
    """Resolve one Current carrier's structural owner from its direct containment."""
    from GENERATE_ENTITY_GRAPH.cfel_claim_constraints import extract_claim_constraints

    selected = [
        source for source in context.inputs["sources"]
        if source.get("binding", {}).get("atom_id") in _CURRENT_CONTAINMENT_SOURCE_IDS
    ]
    sources = {source["binding"]["atom_id"]: source for source in selected}
    if (set(sources) != set(_CURRENT_CONTAINMENT_SOURCE_IDS)
            or len(selected) != len(_CURRENT_CONTAINMENT_SOURCE_IDS)):
        raise ProposedCarrierError("Current containment authority is unavailable")

    def records(identifier: str) -> list[Record]:
        source = sources[identifier]
        binding = source.get("binding")
        text = source.get("text")
        if not isinstance(binding, Mapping) or not isinstance(text, str):
            raise ProposedCarrierError("Current containment authority is unavailable")
        try:
            body = parse_carrier(text.encode("utf-8"), Path(binding["path"])).body
        except (CarrierError, KeyError, TypeError, UnicodeError) as error:
            raise ProposedCarrierError("Current containment authority is unavailable") from error
        extracted, _ = extract_claim_constraints({"source": binding, "body": body})
        return extracted

    def exactly_one(identifier: str, **expected: object) -> None:
        matches = [
            record for record in records(identifier)
            if all(record.get(key) == value for key, value in expected.items())
        ]
        if len(matches) != 1:
            raise ProposedCarrierError("Current containment authority is unresolved")

    exactly_one(
        "CA-R-2508",
        kind="relation_cardinality",
        source_selector="Atom//$atom",
        relation="IS_CONTAINED_BY",
        target_selector=None,
        source_cardinality={"minimum": 1, "maximum": 1},
        selection="named_relation",
    )
    exactly_one(
        "CA-R-2523",
        kind="classification_condition",
        subject_selector="Scope Unit",
        axis="Container",
        operator="==",
        value="yes",
    )
    exactly_one(
        "CA-R-2523",
        kind="relation_cardinality",
        source_selector="Scope Unit//$scope_unit",
        relation="CONTAINS",
        target_selector="Atom//$atom",
        source_cardinality={"minimum": 0, "maximum": None},
    )
    exactly_one(
        "CA-R-2511",
        kind="classification_condition",
        subject_selector="Atom/(.Header.Role: Plan)",
        axis="Container",
        operator="==",
        value="yes",
    )
    exactly_one(
        "CA-R-2511",
        kind="relation_cardinality",
        source_selector="Atom/(.Header.Role: Plan)//$plan",
        relation="CONTAINS",
        target_selector="Atom/(.Header.Role: Plan)//$contained_plan",
        source_cardinality={"minimum": 0, "maximum": None},
    )

    def scope_owner(identifier: str) -> str:
        rows = context.inputs.get("structure", {}).get("scope_units", [])
        id_matches = [
            row for row in rows
            if isinstance(row, Mapping) and row.get("scope_unit_id") == identifier
        ]
        project = context.inputs.get("_project_identity", {}).get("project", {})
        project_name = project.get("name") if isinstance(project, Mapping) else None
        roots = [
            row for row in rows
            if isinstance(row, Mapping) and row.get("scope_unit_name") == project_name
        ]
        if identifier == project_name and len(roots) == 1:
            selected = {id(row) for row in (*id_matches, *roots)}
            if len(selected) != 1:
                raise ProposedCarrierError("Current containment Scope Unit is ambiguous")
            return identifier
        if len(id_matches) == 1 and isinstance(id_matches[0].get("scope_unit_name"), str):
            return id_matches[0]["scope_unit_name"]
        raise ProposedCarrierError("Current containment Scope Unit is unresolved")

    field, target = _current_containment_target(raw_metadata, label="Current containment relation")
    if field == "scope_unit":
        return scope_owner(target)

    if re.fullmatch(r"CA-[CAPRMEDO]-[0-9]+", target) is None:
        raise ProposedCarrierError("Current containment Atom identity is invalid")
    identity = raw_metadata.get("atom_id")
    if target == identity:
        raise ProposedCarrierError("Current containment cannot target the carrier itself")
    from current_atom_locator import CurrentAtomLocator, CurrentAtomLocatorError

    locator = CurrentAtomLocator(context.root, reader=context._reader)
    seen = {identity} if isinstance(identity, str) else set()

    if raw_metadata.get("role") != "Plan" or raw_metadata.get("form") != "Plan":
        raise ProposedCarrierError("Current containment Atom eligibility is unresolved")

    if status_index is None:
        try:
            status_index = capture_status_models(context.root, context._reader)
        except StatusModelError as error:
            raise ProposedCarrierError("Current containment Atom status is unavailable or unadmitted") from error

    def resolve_atom(atom_id: str) -> str:
        current = atom_id
        for _ in range(64):
            if current in seen:
                raise ProposedCarrierError("Current containment graph is cyclic")
            seen.add(current)
            try:
                path = locator.locate(current, Path(".current-containment") / f"{current}.md")
                absolute = context.root / path
                metadata = parse_carrier(context._reader.read(absolute), absolute).metadata
            except (CurrentAtomLocatorError, OSError, RuntimeError, CarrierError) as error:
                raise ProposedCarrierError("Current containment Atom is unavailable or ambiguous") from error
            if metadata.get("role") != "Plan" or metadata.get("form") != "Plan":
                raise ProposedCarrierError("Current containment Atom eligibility is unresolved")
            try:
                resolve_status_model(context.root, metadata, metadata.get("status"), _index=status_index)
            except StatusModelError as error:
                raise ProposedCarrierError("Current containment Atom status is unavailable or unadmitted") from error
            field, nested = _current_containment_target(metadata, label="Current containment Atom")
            if field == "scope_unit":
                return scope_owner(nested)
            if re.fullmatch(r"CA-[CAPRMEDO]-[0-9]+", nested) is None:
                raise ProposedCarrierError("Current containment Atom identity is invalid")
            current = nested
        raise ProposedCarrierError("Current containment graph exceeds the supported depth")

    try:
        owner = resolve_atom(target)
        locator.revalidate()
        return owner
    except CurrentAtomLocatorError as error:
        raise ProposedCarrierError("Current containment Atom is unavailable or ambiguous") from error


def _current_plan_parent_placement(
    context: VerifiedSourceContext,
    *,
    parent_id: str,
    child_status: object,
    relative_path: Path,
    plan_status_folders: Mapping[str, str],
) -> None:
    """Bind a nested Current Plan directory to its typed containment Atom."""
    from current_atom_locator import CurrentAtomLocator, CurrentAtomLocatorError

    if child_status in {"Draft", "Archived"}:
        raise ProposedCarrierError(
            "nested Current Draft or Archived Plan must use the shared Scope Unit placement"
        )
    try:
        locator = CurrentAtomLocator(context.root, reader=context._reader)
        parent_relative = Path(locator.locate(parent_id, Path(".current-plan-parent") / f"{parent_id}.md"))
        expected_parent = _plan_container(
            context.root / parent_relative, child_status, plan_status_folders,
        )
        candidate = context.root / context._selection.control_relative / relative_path
        if candidate.parent != expected_parent:
            raise ProposedCarrierError(
                "nested Current Plan path does not use its typed containment Atom parent"
            )
        locator.revalidate()
    except ProposedCarrierError:
        raise
    except (CurrentAtomLocatorError, ProposedReferenceError, OSError, RuntimeError, ValueError) as error:
        raise ProposedCarrierError("Current Plan containment parent placement is unresolved") from error


def _current_draft_filename(metadata: Mapping[str, Any], relative_path: Path) -> None:
    """Bind an ordinary Current Draft filename to its canonical ID and Version."""
    if metadata.get("status") != "Draft":
        return
    identity = metadata.get("atom_id")
    version = metadata.get("version")
    if not isinstance(identity, str) or type(version) is not int or version < 1:
        raise ProposedCarrierError("Current Draft identity or Version is unresolved")
    from atom_operations import CURRENT_FILENAME

    if CURRENT_FILENAME.fullmatch(relative_path.name) is None:
        raise ProposedCarrierError("Current Draft filename is malformed")
    head = re.sub(r"^[0-9]+-", "", relative_path.stem.split("--", 1)[0])
    expected = f"{identity}@{version}-draft"
    if head.count("@") != 1 or (head != expected and not head.startswith(expected + "-")):
        raise ProposedCarrierError("Current Draft filename must carry its exact canonical ID and Version marker")


def validate_proposed_carrier(
    metadata: Record, body: str, verified_source_context: VerifiedSourceContext, relative_path: Path,
    *, allow_existing_relations: bool = False, reference_roles: tuple[str, ...] | None = None,
    _status_index: StatusModelIndex | None = None,
) -> Record:
    """Reject every failed, unresolved, or unsupported finite carrier obligation.

    Explicit reference roles bound traversal, not authority or rule coverage.
    Scoped results certify only this carrier and its named reference closure.
    """

    if relative_path.is_absolute() or ".." in relative_path.parts:
        raise ProposedCarrierError("carrier path is outside the selected Project")
    raw_metadata = metadata
    try:
        metadata = carrier_read_view(metadata)
    except ValueError as error:
        raise ProposedCarrierError("carrier aliases conflict") from error
    _current(verified_source_context._reader, verified_source_context._selection)
    owns_status_index = _status_index is None
    profiles = {
        reviewed_encoding_profile(row)
        for row in verified_source_context.inputs["sources"]
        if row.get("binding", {}).get("atom_id") in {"CA-D-276", "CA-D-657"}
    }
    required_codes = (
        _CURRENT_CODES
        if profiles == {"current"}
        else _LEGACY_CODES if profiles == {"legacy"} else None
    )
    if required_codes is None:
        raise ProposedCarrierError("complete-carrier frontmatter authority is unsupported or ambiguous")
    selected = tuple(item for item in verified_source_context.authority.obligations if item.code in required_codes)
    if {item.code for item in selected} != required_codes or any(not item.supported for item in selected):
        raise ProposedCarrierError("complete-carrier authority is unsupported or incomplete")
    try:
        with bind_selection(verified_source_context._selection):
            if _status_index is None:
                _status_index = capture_status_models(verified_source_context.root, verified_source_context._reader)
            status_model = resolve_status_model(
                verified_source_context.root, metadata, metadata.get("status"), _index=_status_index,
            )
    except StatusModelError as error:
        raise ProposedCarrierError("status model is missing, ambiguous, or unadmitted") from error
    domains = dict(verified_source_context.authority.domains)
    domains["domain.status." + status_model["content_role"].lower()] = tuple(status_model["statuses"])
    context = AuthorityContext(
        bindings=verified_source_context.authority.bindings,
        required=len(selected),
        supported=len(selected),
        unsupported=0,
        gaps=[],
        obligations=selected,
        domains=domains,
        unclassified_sources=False,
    )
    current_profile = profiles == {"current"}
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        raise ProposedCarrierError("relations are malformed")
    current_containment = (
        _current_containment_target(raw_metadata, label="Current containment relation")
        if current_profile else None
    )
    owner = (
        _current_containment_owner(verified_source_context, raw_metadata, status_index=_status_index)
        if current_profile else metadata.get("current_scope_unit")
    )
    if current_profile:
        metadata = dict(metadata)
        # The typed containment's shape and resolved owner were checked above.
        # It remains in raw metadata; legacy adapters cannot parse this
        # non-runtime Current encoding, while they still receive every other relation.
        relations = {kind: targets for kind, targets in relations.items() if kind != "IS_CONTAINED_BY"}
        metadata["relations"] = relations
    role = metadata.get("content_role")
    status = metadata.get("status")
    if current_profile:
        _current_draft_filename(raw_metadata, relative_path)
    plan_parts = relative_path.parts
    plan_tail = plan_parts[plan_parts.index("03_plan") + 1 : -1] if "03_plan" in plan_parts else ()
    plan_deep = (
        role == "Plan"
        and "03_plan" in plan_parts
        and len(plan_tail) > (0 if status == "Active" else 1)
    )
    if plan_deep and not current_profile and not relations.get("is_decomposition_of"):
        raise ProposedCarrierError("deep Plan placement requires an admitted decomposition parent")
    plan_source = next(
        (item for item in verified_source_context.inputs["sources"] if item["binding"]["atom_id"] == "CA-D-461"),
        None,
    )
    plan_mapping = _plan_mapping(plan_source["text"]) if plan_source is not None else {}
    if current_profile and plan_deep:
        if current_containment is None or current_containment[0] != "atom":
            raise ProposedCarrierError("nested Current Plan requires a typed containment Atom parent")
        _current_plan_parent_placement(
            verified_source_context,
            parent_id=current_containment[1],
            child_status=status,
            relative_path=relative_path,
            plan_status_folders=plan_mapping,
        )
    source = next((row for row in verified_source_context.inputs["sources"] if row["binding"]["atom_id"] == "CA-D-324"), None)
    if source is None or not isinstance(role, str):
        raise ProposedCarrierError("role-directory authority is unavailable")
    mapping = dict(re.findall(r"- ([A-Za-z]+): `([0-9]{2}_[a-z_]+)/`[;.]", source["text"]))
    reference_mapping = mapping
    if reference_roles is not None:
        if (type(reference_roles) is not tuple or not reference_roles
                or any(type(item) is not str or item not in mapping for item in reference_roles)
                or len(set(reference_roles)) != len(reference_roles)):
            raise ProposedCarrierError("reference roles must be a nonempty unique tuple of canonical admitted roles")
        if role not in reference_roles:
            raise ProposedCarrierError("carrier role is outside the explicit reference scope")
        reference_mapping = {key: value for key, value in mapping.items() if key in reference_roles}
    control = verified_source_context._selection.control_relative
    carrier_inputs = _validation_inputs(verified_source_context, metadata)
    carrier_inputs["_raw_metadata"] = raw_metadata
    result = validate_carrier(metadata, body, context, carrier_inputs)
    if result["findings"] or result["gaps"] or any(item["outcome"] != "passed" for item in result["outcomes"]):
        raise ProposedCarrierError("complete-carrier validation failed or is unresolved")
    if reference_roles is not None:
        result["reference_scope"] = {
            "extent": "finite-proposed-carrier",
            "project": verified_source_context.inputs["_project_identity"]["project"]["name"],
            "roles": list(reference_mapping),
            "role_folders": dict(reference_mapping),
            "authority_paths": sorted([
                control.as_posix(),
                *[row["authority_path"] for row in verified_source_context.inputs["structure"]["scope_units"]],
            ]),
            "direct_targets": [],
            "plan_parent_closure": [],
        }
    inventory = None
    if relations and (not allow_existing_relations or plan_deep or reference_roles is not None):
        targets = list(dict.fromkeys(target for values in relations.values() if isinstance(values, list) for target in values))
        status_folders = _frontier_status_folders(verified_source_context, plan_mapping, _status_index)
        try:
            inventory = inventory_proposed_references(
                verified_source_context.root,
                verified_source_context.inputs["structure"],
                targets,
                admitted_role_folders=reference_mapping,
                admitted_status_folders={key: value for key, value in status_folders.items() if key in reference_mapping},
                project_authority_paths=(control,),
                project_name=verified_source_context.inputs["_project_identity"]["project"]["name"],
                candidate_metadata=metadata,
                candidate_path=control / relative_path,
                admitted_plan_status_folders=plan_mapping or None,
                current_target_ids=relations.get("concern_about", ()),
            )
        except ProposedReferenceError as error:
            raise ProposedCarrierError("relation targets are missing, inactive, ambiguous, or cyclic") from error
        graph_reader = ReadContext(roots=[str(verified_source_context.root)], limits=dict(CEILINGS))
        graph_report: Record = {"bindings": {}, "coverage": {"gaps": []}}
        with bind_selection(verified_source_context._selection):
            graph_sources = [
                _source(verified_source_context.root, identifier, graph_reader, graph_report, graph=True)
                for identifier in _GRAPH_IDS
            ]
            identity_source = (
                _source(verified_source_context.root, "CA-D-378", graph_reader, graph_report)
                if relations.get("concern_about") else None
            )
        graph_inputs = dict(verified_source_context.inputs)
        graph_source_inputs = _target_type_sources(
            verified_source_context,
            carrier_inputs.get("sources", verified_source_context.inputs["sources"]),
            inventory,
        )
        graph_inputs.update(
            sources=[
                *[
                    source for source in graph_source_inputs
                    if source["binding"]["atom_id"] not in (*APPROVED_GRAPH_AUTHORITY_IDS, "CA-D-378")
                ],
                *([identity_source] if identity_source is not None else []),
                *graph_sources,
            ],
            reader=graph_reader,
            reference_complete=True,
            status_root=verified_source_context.root,
            status_index=_status_index,
            path=verified_source_context.root / control / relative_path,
            references=[
                {"path": verified_source_context.root / item.path, "metadata": item.metadata}
                for item in (*inventory.direct_targets, *inventory.plan_parent_closure, *inventory.plan_prerequisite_closure)
            ],
        )
        if (role, metadata.get("type")) == ("Plan", "Plan") and relations.get("blocks"):
            for item in (*inventory.direct_targets, *inventory.plan_parent_closure, *inventory.plan_prerequisite_closure):
                if item.metadata.get("content_role") == "Plan":
                    _assigned_identity(verified_source_context, item.metadata)
        if reference_roles is not None:
            resolved = (*inventory.direct_targets, *inventory.plan_parent_closure, *inventory.plan_prerequisite_closure)
            target_ids = {item.atom_id for item in resolved}
            if any(source["binding"]["atom_id"] in target_ids
                   and source["metadata"].get("content_role") not in reference_mapping
                   for source in graph_inputs["sources"]):
                raise ProposedCarrierError("bound authority target is outside the explicit reference scope")
            result["reference_scope"]["direct_targets"] = [item.atom_id for item in inventory.direct_targets]
            result["reference_scope"]["plan_parent_closure"] = [item.atom_id for item in inventory.plan_parent_closure]
        plan_status_source = next(
            (source for source in graph_sources if source["binding"]["atom_id"] == "CA-R-1539"), None
        )
        domains = dict(verified_source_context.authority.domains)
        if plan_status_source is not None:
            domains["domain.status.plan"] = tuple(
                resolve_status_domain(_status_index.declarations, "Plan")["statuses"]
            )
        graph_context = AuthorityContext([], 0, 0, 0, [], (), domains, False)
        adapters = [("relations.resolution", relations_resolution), ("plan.decomposition_resolution", plan_resolution)]
        if relations.get("blocks"):
            adapters.append(("plan.blocking_resolution", plan_resolution))
        for code, adapter in adapters:
            check = Check(Obligation(code, [], True, "verified graph authority"), graph_context, graph_inputs)
            adapter(metadata, body, check)
            if check.findings or check.gaps:
                raise ProposedCarrierError("relation or Plan decomposition admission failed or is unresolved")
        _current(graph_reader, verified_source_context._selection)
    role = metadata.get("content_role")
    status = metadata.get("status")
    expected_role_directory = mapping.get(role)
    if expected_role_directory is None or expected_role_directory not in relative_path.parts[:-1]:
        raise ProposedCarrierError("carrier path disagrees with its carried content role")
    rows = verified_source_context.inputs.get("structure", {}).get("scope_units", [])
    row = next((item for item in rows if item.get("scope_unit_name") == owner), None)
    project_relative_path = control / relative_path
    if owner == verified_source_context.inputs["_project_identity"]["project"]["name"]:
        authority_path = control / expected_role_directory
        if any(
            isinstance(item, Mapping)
            and item.get("scope_unit_name") != owner
            and isinstance(item.get("authority_path"), str)
            and project_relative_path.is_relative_to(Path(item["authority_path"]))
            for item in rows
        ):
            raise ProposedCarrierError("Project-owned carrier is inside a declared Scope Unit authority")
    elif isinstance(row, Mapping) and isinstance(row.get("authority_path"), str):
        authority_path = Path(row["authority_path"])
    else:
        raise ProposedCarrierError("carrier owner authority is unresolved")
    if not project_relative_path.is_relative_to(authority_path):
        raise ProposedCarrierError("carrier path is outside its carried owner authority")
    expected_status_directory = (
        "" if isinstance(status, str) and status.casefold() == "active"
        else status.lower() if isinstance(status, str) else None
    )
    if role == "Plan":
        if plan_source is None:
            raise ProposedCarrierError("Plan placement authority is unavailable")
        expected_status_directory = "" if status == "Active" else plan_mapping.get(status)
    role_index = relative_path.parts.index(expected_role_directory)
    tail = relative_path.parts[role_index + 1 : -1]
    if role == "Operations" and len(tail) > (0 if status == "Active" else 1):
        role_root = control / Path(*relative_path.parts[:role_index + 1])
        _operations_placement(verified_source_context, metadata, project_relative_path, role_root, owner, rows,
                              authority_path, _status_index)
        _current(verified_source_context._reader, verified_source_context._selection)
        if owns_status_index:
            _status_current(verified_source_context, _status_index)
        if inventory is not None:
            try:
                inventory.assert_current()
            except ProposedReferenceError as error:
                raise ProposedCarrierError("relation inventory changed during admission") from error
        return result
    if len(tail) > 1 and role != "Plan":
        raise ProposedCarrierError("deeper carrier placement is unsupported")
    actual_status_directory = "" if role == "Plan" and status == "Active" else (tail[-1] if tail else "")
    if expected_status_directory is None or actual_status_directory != expected_status_directory:
        raise ProposedCarrierError("carrier path disagrees with its carried status")
    _current(verified_source_context._reader, verified_source_context._selection)
    if owns_status_index:
        _status_current(verified_source_context, _status_index)
    if inventory is not None:
        try:
            inventory.assert_current()
        except ProposedReferenceError as error:
            raise ProposedCarrierError("relation inventory changed during admission") from error
    return result
