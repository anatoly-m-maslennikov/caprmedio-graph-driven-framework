"""Private Atom Query/Read receiving connection for an already-started Session."""

from __future__ import annotations

import copy
from collections.abc import Collection
from pathlib import Path

from carrier_aliases import carrier_read_view
from connector_atom_dispatch import execute_atom_request
from connector_atom_parse import IDENTITY, LIFECYCLES, validate_filters
from connector_atom_read import AtomSourceView
from connector_bindings import ConnectorBindingError, ConnectorBindings, FileSource, admission_for_started_action
from project_selection import ProjectSelection, ProjectSelectionError, bind_selection
from subject_notation import GrammarPin, GrammarSource, get_profile
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier


_CONTRACTS = {
    "CA-D-625": "Delivery",
    "CA-R-1936": "Requirement",
    "CA-M-376": "Method",
}
_ACTIONS = {
    "CA-O-047": "read",
    "CA-O-046": "query",
}


def _metadata(source: FileSource) -> dict:
    return carrier_read_view(parse_carrier(source.read_bytes(), source.root / source.relative_path).metadata)


def _grammar_binding_matches(
    pin: GrammarPin | GrammarSource, values: dict[str, object], source: FileSource | None,
) -> bool:
    if source is None or type(values.get("version")) is not int or values["version"] < 1:
        return False
    if isinstance(pin, GrammarPin):
        return source.sha256 == pin.sha256 and values["version"] == pin.version
    return (source.relative_path.as_posix() == pin.path and values.get("status") == "Active"
            and values.get("content_role") ==
            {"R": "Requirement", "M": "Method", "E": "Evaluation"}.get(pin.atom_id[3:4]))


def _selected_project_sources(selection: ProjectSelection) -> tuple[FileSource, ...]:
    """Pin Settings plus each selected Scope Unit Declaration Atom."""
    relative = selection.settings_path.relative_to(selection.root)
    settings_digest = selection.provenance.get(relative.as_posix(), {}).get("sha256")
    pins = selection.declaration_source_pins
    sources = [FileSource(selection.root, relative, settings_digest)]
    for path in selection.declaration_paths:
        declaration_relative = path.relative_to(selection.root)
        digest = pins.get(declaration_relative.as_posix(), {}).get("sha256")
        sources.append(FileSource(selection.root, declaration_relative, digest))
    if (not isinstance(settings_digest, str) or len(settings_digest) != 64
            or any(source.sha256 is None or len(source.sha256) != 64 for source in sources)
            or len({source.relative_path for source in sources}) != len(sources)):
        raise ValueError("Selected Settings and Scope Unit Declaration provenance is required.")
    return tuple(sources)


def make_atom_receiver(
    selection: ProjectSelection, *, source_view: AtomSourceView,
    source_frontier: Collection[FileSource], schema_sources: Collection[FileSource],
    action_definition: FileSource, frontier_references: Collection[str],
):
    """Retain one explicit view/frontier and accepted operation/schema revisions.

    This is a private Session receiver, not a source selector, permission grant,
    Run creator or runnable route. The existing Session owns all recording.
    """
    if not isinstance(selection, ProjectSelection) or not isinstance(source_view, AtomSourceView):
        raise TypeError("A genuine ProjectSelection and explicit Atom source view are required.")
    selection._revalidate_boundary()
    view = copy.deepcopy(source_view)
    owners = {row["scope_unit_name"]: selection.root / row["authority_path"]
              for row in selection.structure["scope_units"]
              if row.get("scope_unit_id") is not None and "authority_path" in row}
    if (view.root != selection.root or view.control != selection.control_root or view.owners != owners
            or not view.scope_units or len(set(view.scope_units)) != len(view.scope_units)
            or not set(view.scope_units) <= owners.keys() or not view.lifecycles
            or len(set(view.lifecycles)) != len(view.lifecycles) or not set(view.lifecycles) <= LIFECYCLES
            or view.source_view not in {"current", "history", "all"} or view.attribution is None
            or any(not path.is_relative_to(selection.root) or path.resolve() != path for path in view.installed_roots)):
        raise ValueError("The complete explicit Atom view must match the selected Project ownership.")
    frontier, schemas, references = tuple(source_frontier), tuple(schema_sources), tuple(frontier_references)
    if (not references or len(set(references)) != len(references)
            or any(not isinstance(reference, str) or not reference or Path(reference).is_absolute()
                   or ".." in Path(reference).parts for reference in references)):
        raise ValueError("An exact existing selected frontier reference mapping is required.")
    for sources in (frontier, schemas, (action_definition,)):
        if (any(not isinstance(source, FileSource) or source.root != selection.root or source.sha256 is None
                for source in sources)
                or len({source.relative_path for source in sources}) != len(sources)):
            raise ValueError("Distinct exact selected Project source pins are required.")
    metadata = {}
    for source in schemas:
        values = _metadata(source)
        metadata[values.get("atom_id")] = values, source
    if len(metadata) != len(schemas) or not _CONTRACTS.keys() <= metadata.keys():
        raise ValueError("Exact shared connector contract sources are required.")
    for identity, role in _CONTRACTS.items():
        values, source = metadata[identity]
        if (values.get("content_role") != role or values.get("status") != "Active"
                or type(values.get("version")) is not int or values["version"] < 1):
            raise ValueError("The supplied schema is not an active connector contract source.")
    action = _metadata(action_definition)
    identity = action.get("atom_id")
    if identity not in _ACTIONS:
        raise ValueError("An accepted Atom Read or Query Action is required.")
    operation = _ACTIONS[identity]
    version = action.get("version")
    if (action.get("content_role") != "Operations" or action.get("type") != "Action"
            or action.get("status") != "Active" or type(action.get("version")) is not int
            or action["version"] < 1):
        raise ValueError("An active Atom Read or Query Action source is required.")
    if operation == "query":
        for pin in get_profile(view.subject_profile).grammar_pins:
            values, source = metadata.get(pin.atom_id, ({}, None))
            if not _grammar_binding_matches(pin, values, source):
                raise ValueError("The explicit Subject profile requires its complete exact grammar pins.")
    selected_sources = _selected_project_sources(selection)

    def validate_payload(request):
        try:
            selection._revalidate_boundary()
        except ProjectSelectionError as error:
            raise ConnectorBindingError("stale_state", str(error), "context") from error
        if request["context"] != view.attribution:
            raise ConnectorBindingError("input_invalid", "Context does not identify the bound Atom source view.", "context")
        if any(not owners[name].is_dir() or owners[name].resolve() != owners[name]
               for name in view.scope_units):
            raise ConnectorBindingError("backend_failure", "The complete selected source ownership frontier is unavailable.", "context")
        if operation == "query":
            try:
                validate_filters(request["query"]["filters"])
            except (TypeError, ValueError) as error:
                raise ConnectorBindingError("input_invalid", str(error), "query") from error
        elif (not isinstance(request["target"]["identity"], str)
              or IDENTITY.fullmatch(request["target"]["identity"]) is None):
            raise ConnectorBindingError("input_invalid", "Read requires one full logical Atom ID.", "target")

    def receive(session, action_run_id):
        def map_request(outer):
            if outer["effects"]:
                raise ConnectorBindingError("permission_denied", "Atom Query/Read requires an empty requested effect frontier.", "authorization")
            if tuple(outer["target_frontier"]) != references:
                raise ConnectorBindingError("permission_denied", "Selected frontier does not map to the bound Atom source view.", "context")
            return outer["parameters"], outer["definition_manifest"]

        try:
            admission, request = admission_for_started_action(
                session, action_run_id, root=selection.root, action_definition=action_definition,
                action_atom_id=identity, action_version=version, map_request=map_request,
            )
            bindings = ConnectorBindings(
                admission, supported_operations={operation}, supported_kinds={"Atom"},
                validate_payload=validate_payload, resolve_sources=lambda _: frontier,
                authority_sources=(*schemas, action_definition, *selected_sources),
            )
            with bind_selection(selection):
                return execute_atom_request(request, bindings, view)
        except ConnectorBindingError as error:
            return {"data": None, "current_state": None, "effects": [], "errors": [error.record()]}
        except ProjectSelectionError as error:
            return {"data": None, "current_state": None, "effects": [], "errors": [
                {"code": "stale_state", "message": str(error), "field": "context"},
            ]}

    return receive
