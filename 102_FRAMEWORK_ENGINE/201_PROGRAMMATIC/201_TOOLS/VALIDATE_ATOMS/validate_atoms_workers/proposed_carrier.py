"""Finite, source-bound admission for a proposed complete Atom carrier."""

from __future__ import annotations

import hashlib
import json
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

from .authority import AuthorityContext, Obligation, Record, _verified, resolve_context
from .check_operators import load_operators_registry
from .checks import validate_carrier
from .context import load_source
from .read_io import ReadContext
from .settings import CEILINGS
from .support_authority import support_sources
from .check_support import Check
from .check_graph_extended import relations_resolution, plan_resolution
from .check_schema_extended import TYPE_CONTRIBUTIONS
from .proposed_references import ProposedReferenceError, _container_id, inventory_proposed_references
from .parsing import CarrierError, parse_carrier
from .graph_authority_refresh import APPROVED_GRAPH_AUTHORITY_IDS
from artifact_metadata import project_identity
from authoritative_status_models import (
    StatusModelError, StatusModelIndex, capture_status_models,
    declarations_from_sources, resolve_status_domain, resolve_status_model, revalidate_status_models,
)
from project_selection import ProjectSelection, active_selection, bind_selection, bound_selection


_REGISTRY_IDS = (
    "CA-D-276", "CA-D-269", "CA-D-268", "CA-D-270", "CA-D-274", "CA-D-446",
    "CA-D-479", "CA-D-482", "CA-D-483",
)
_SUPPORT_IDS = (
    "CA-D-494", "CA-D-440", "CA-D-441", "CA-D-442", "CA-R-1308", "CA-R-1313",
    "CA-D-324", "CA-D-466", "CA-D-461",
    *TYPE_CONTRIBUTIONS, "CA-R-1283", "CA-R-1700", "CA-R-1506",
)
_GRAPH_IDS = tuple(sorted(APPROVED_GRAPH_AUTHORITY_IDS))
_FRONTIER_STATUS_IDS = {
    "Concern": "CA-R-1608", "Analysis": "CA-R-1875", "Plan": "CA-R-1539",
    "Requirement": "CA-R-1309", "Method": "CA-R-1397", "Evaluation": "CA-R-1398",
    "Delivery": "CA-R-1399", "Operations": "CA-R-1874",
}
_FRONTIER_IDS = ("CA-D-434", "CA-D-467", "CA-D-460", "CA-D-481", *_FRONTIER_STATUS_IDS.values())
_CODES = frozenset(
    {
        "frontmatter.common_encoding", "frontmatter.version", "frontmatter.updated_at",
        "frontmatter.author", "author.resolution", "frontmatter.atom_id",
        "frontmatter.subjects", "frontmatter.relations", "frontmatter.claim_target_scope_unit",
        "target.resolution", "frontmatter.status",
        "body.sections", "model.domains",
    }
)


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
            with bind_selection(self._context._selection):
                if self._status_index is None:
                    raise ProposedCarrierError("status-model validation scope is incomplete")
                revalidate_status_models(self._status_index, self._context._reader)
            _current(self._context._reader, self._context._selection)


def _entry(identifier: str, *, graph: bool = False) -> Record:
    registry = json.loads(Path(__file__).with_name("registry.json").read_text(encoding="utf-8"))["sources"]
    graph_entries = json.loads(Path(__file__).with_name("graph_authority.json").read_text(encoding="utf-8"))["sources"]
    if graph and identifier in APPROVED_GRAPH_AUTHORITY_IDS:
        return graph_entries.get(identifier) or {}
    return registry.get(identifier) or support_sources().get(identifier) or graph_entries.get(identifier) or {}


def _source(root: Path, identifier: str, reader: ReadContext, report: Record, *, graph: bool = False) -> Record:
    entry = _entry(identifier, graph=graph)
    path = entry.get("source_path") if isinstance(entry, dict) else None
    if not isinstance(path, str) or not path or Path(path).is_absolute() or ".." in Path(path).parts:
        raise ProposedCarrierError("required source locator is unavailable")
    selection = bound_selection(root)
    if selection is not None and Path(path).is_relative_to('.caprmedio_caprmedio'):
        path = (selection.control_relative / Path(path).relative_to('.caprmedio_caprmedio')).as_posix()
    absolute = root / path
    item = load_source(absolute, None, reader, report)
    if (item is None or item["metadata"].get("atom_id") != identifier
            or not _verified(item, entry)):
        raise ProposedCarrierError("required source is unreadable, changed, or inactive")
    return item


def source_context_from_project(root: Path) -> VerifiedSourceContext:
    """Load just the finite checked authority closure and selected Project inputs."""

    root = root.resolve()
    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    try:
        selection = active_selection(root)
        selection._revalidate_boundary(reader=reader)
        control = selection.control_relative
        for path in (selection.settings_path, selection.structure_path):
            raw = reader.read(path)
            pin = selection.provenance.get(path.relative_to(root).as_posix(), {})
            if hashlib.sha256(raw).hexdigest() != pin.get("sha256"):
                raise ProposedCarrierError("selected Project context changed after selection")
        structure = tomllib.loads(raw.decode("utf-8"))
        operators = selection.control_root / "operators_registry.toml"
        operator_raw = reader.read(operators)
        with bind_selection(selection):
            identity = project_identity(root)
            sources = [_source(root, identifier, reader, report) for identifier in (*_REGISTRY_IDS, *_SUPPORT_IDS)]
    except (OSError, RuntimeError, UnicodeError, ValueError) as error:
        raise ProposedCarrierError("required Project context is unreadable") from error
    inputs: Record = {
        "sources": sources,
        "control_relative": control.as_posix(),
        "structure": structure,
        "_project_identity": identity,
        "operators_registry": load_operators_registry(
            {"operators_registry": {"path": str(operators), "sha256": hashlib.sha256(operator_raw).hexdigest()}},
            reader,
        ),
    }
    _current(reader, selection)
    return VerifiedSourceContext(root, resolve_context(sources), inputs, selection, reader)


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
    report: Record = {"bindings": {}, "coverage": {"gaps": []}}
    with bind_selection(context._selection):
        sources = {
            identifier: _source(context.root, identifier, context._reader, report, graph=identifier in _GRAPH_IDS)
            for identifier in _FRONTIER_IDS
        }
    mappings = {}
    declarations = (status_index.declarations if status_index is not None
                    else declarations_from_sources(list(sources.values())))
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
    letter = letters.get(metadata.get("content_role"))
    identity = metadata.get("atom_id")
    if (not isinstance(letter, str) or not isinstance(identity, str)
            or re.fullmatch(rf"{re.escape(prefix)}-{re.escape(letter)}-[0-9]+", identity) is None):
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
    _current(verified_source_context._reader, verified_source_context._selection)
    owns_status_index = _status_index is None
    selected = tuple(item for item in verified_source_context.authority.obligations if item.code in _CODES)
    if {item.code for item in selected} != _CODES or any(not item.supported for item in selected):
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
    relations = metadata.get("relations", {})
    if not isinstance(relations, dict):
        raise ProposedCarrierError("relations are malformed")
    role = metadata.get("content_role")
    status = metadata.get("status")
    plan_parts = relative_path.parts
    plan_tail = plan_parts[plan_parts.index("03_plan") + 1 : -1] if "03_plan" in plan_parts else ()
    plan_deep = (
        role == "Plan"
        and "03_plan" in plan_parts
        and len(plan_tail) > (0 if status == "Active" else 1)
    )
    if plan_deep and not relations.get("is_decomposition_of"):
        raise ProposedCarrierError("deep Plan placement requires an admitted decomposition parent")
    plan_source = next(
        (item for item in verified_source_context.inputs["sources"] if item["binding"]["atom_id"] == "CA-D-461"),
        None,
    )
    plan_mapping = (
        {"Active": "", **dict(re.findall(r"- ([A-Za-z]+): .*?`([^`]+)`", plan_source["text"]))}
        if plan_source is not None
        else {}
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
    result = validate_carrier(metadata, body, context, verified_source_context.inputs)
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
        graph_inputs = dict(verified_source_context.inputs)
        graph_inputs.update(
            sources=[
                *[
                    source for source in verified_source_context.inputs["sources"]
                    if source["binding"]["atom_id"] not in APPROVED_GRAPH_AUTHORITY_IDS
                ],
                *graph_sources,
            ],
            reader=graph_reader,
            reference_complete=True,
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
        domains = (
            {"domain.status.plan": tuple(resolve_status_domain(_status_index.declarations, "Plan")["statuses"])}
            if plan_status_source is not None
            else {}
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
    owner = metadata.get("current_scope_unit")
    rows = verified_source_context.inputs.get("structure", {}).get("scope_units", [])
    row = next((item for item in rows if item.get("scope_unit_name") == owner), None)
    project_relative_path = control / relative_path
    if owner == verified_source_context.inputs["_project_identity"]["project"]["name"]:
        authority_path = control / expected_role_directory
        if any(project_relative_path.is_relative_to(Path(item["authority_path"])) for item in rows):
            raise ProposedCarrierError("Project-owned carrier is inside a declared Scope Unit authority")
    elif isinstance(row, dict) and isinstance(row.get("authority_path"), str):
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
            with bind_selection(verified_source_context._selection):
                revalidate_status_models(_status_index, verified_source_context._reader)
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
        with bind_selection(verified_source_context._selection):
            revalidate_status_models(_status_index, verified_source_context._reader)
    if inventory is not None:
        try:
            inventory.assert_current()
        except ProposedReferenceError as error:
            raise ProposedCarrierError("relation inventory changed during admission") from error
    return result
