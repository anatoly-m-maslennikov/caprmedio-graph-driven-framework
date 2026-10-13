"""Private O212 receiver; its existing Session owns execution and recording."""

from __future__ import annotations

from collections.abc import Callable, Collection
import tomllib

from connector_bindings import (
    ConnectorBindingError, ConnectorBindings, FileSource, admission_for_started_action,
)
from connector_scope_parsing import validate_scope_request
from connector_scope_reading import execute_scope_request
from FIND_AND_FETCH_ARTIFACTS.find_and_fetch_artifacts import _load_frontmatter
from project_selection import ProjectSelection, _validate_structure, bind_selection


def _metadata(source: FileSource) -> dict:
    text = source.read_bytes().decode("utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError("Source authority requires canonical frontmatter.")
    return _load_frontmatter(text[4:].split("\n---\n", 1)[0])


def make_scope_read_receiver(
    selection: ProjectSelection, validate_settings: Callable[[dict], None],
    schema_sources: Collection[FileSource], action_definition: FileSource,
) -> Callable:
    """Bind current sources and a supplied complete Settings validator privately.

    ``validate_settings`` must implement the accepted complete Settings schema,
    backed by ``schema_sources``. This factory neither supplies that policy nor
    admits a route. It invokes the validator on the entire pinned TOML document.
    """
    if not isinstance(selection, ProjectSelection) or not callable(validate_settings):
        raise TypeError("Validated Project selection and complete Settings validator are required.")
    schemas = tuple(schema_sources)
    if (not schemas or any(not isinstance(source, FileSource) or source.root != selection.root
                           or source.sha256 is None for source in schemas)
            or len({source.relative_path for source in schemas}) != len(schemas)):
        raise ValueError("Distinct selected Project schema pins are required.")
    if not {"CA-D-441", "CA-D-442"} <= {_metadata(source).get("atom_id") for source in schemas}:
        raise ValueError("Current Project Structure document and declaration schemas are required.")
    if not isinstance(action_definition, FileSource) or action_definition.root != selection.root:
        raise TypeError("Selected O212 source pin is required.")
    action = _metadata(action_definition)
    version = action.get("version")
    if (action.get("atom_id") != "CA-O-212" or action.get("content_role") != "Operations"
            or action.get("type") != "Action" or action.get("status") != "Active"
            or type(version) is not int or version < 1):
        raise ValueError("Current O212 Action definition is required.")
    sources = []
    for path in (selection.settings_path, selection.structure_path):
        relative = path.relative_to(selection.root)
        digest = selection.provenance.get(relative.as_posix(), {}).get("sha256")
        if not isinstance(digest, str) or len(digest) != 64:
            raise ValueError("Selected Settings and Structure provenance is required.")
        sources.append(FileSource(selection.root, relative, digest))
    sources = tuple(sources)
    project_name = selection.settings["project"]["name"]

    def validate_payload(request: dict) -> None:
        validate_scope_request(request)
        try:
            settings = tomllib.loads(sources[0].read_bytes().decode("utf-8"))
            structure = tomllib.loads(sources[1].read_bytes().decode("utf-8"))
            if validate_settings(settings) is not None:
                raise ConnectorBindingError("schema_invalid", "Settings validator must raise on refusal.", "context")
            _validate_structure(structure, selection.root)
        except (UnicodeError, ValueError) as error:
            if isinstance(error, ConnectorBindingError):
                raise
            raise ConnectorBindingError("schema_invalid", "Complete selected source schema is invalid.", "context") from error

    def receive(session, action_run_id: str) -> dict:
        def map_request(outer: dict) -> tuple[dict, object]:
            if outer["effects"]:
                raise ConnectorBindingError("input_invalid", "Scope Read admits no requested effects.", "delta")
            return outer["parameters"], outer["definition_manifest"]

        try:
            admission, request = admission_for_started_action(
                session, action_run_id, root=selection.root, action_definition=action_definition,
                action_atom_id="CA-O-212", action_version=version,
                map_request=map_request,
            )
            bindings = ConnectorBindings(
                admission, supported_operations={"read"}, supported_kinds={"Scope Unit"},
                validate_payload=validate_payload, resolve_sources=lambda _request: sources,
                authority_sources=(*schemas, action_definition),
            )
            with bind_selection(selection):
                return execute_scope_request(request, bindings=bindings,
                                             project_name=project_name, source_view="current")
        except ConnectorBindingError as error:
            return {"data": None, "current_state": None, "effects": [], "errors": [error.record()]}

    return receive
