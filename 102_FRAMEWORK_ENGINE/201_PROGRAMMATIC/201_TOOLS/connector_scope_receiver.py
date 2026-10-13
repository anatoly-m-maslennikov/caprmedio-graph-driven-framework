"""Private Scope receivers; the existing Session owns execution and recording."""

from __future__ import annotations

from collections.abc import Callable, Collection
import tomllib
from types import MappingProxyType

from connector_bindings import (
    ConnectorBindingError, ConnectorBindings, FileSource, admission_for_started_action,
)
from connector_scope_parsing import validate_scope_request
from connector_scope_reading import execute_scope_request
from FIND_AND_FETCH_ARTIFACTS.find_and_fetch_artifacts import _load_frontmatter
from project_selection import ProjectSelection, _validate_structure, bind_selection
from project_settings_reader import SCHEMA_PINS, read_project_settings


SCOPE_QUERY_PINS = MappingProxyType({
    "CA-R-1936": (1, "f37226d0ade90e8637b0b5dc4805ad256eeeeb555714d68024178a4a7db0f999"),
    "CA-R-1937": (4, "740a4f6df454347f30f31e6fa96a08c51c92336deb39728d5b274d00d0d082ad"),
    "CA-M-376": (1, "ed9ad36cd345878e8ee507a42f3713fecd68ffdda7a97e5578844b48bd6e6043"),
    "CA-M-377": (4, "2eecb1099bc75319b8af2ea7dc6b5210197aaa2bd9951e4fd11165b03d5b2973"),
    "CA-E-628": (1, "b7a79e9e68b4a79463d718016739c4ffee6cb98535045dc95c0713745531e458"),
    "CA-E-629": (3, "24cbac92dbd73c61fdfb2182c27c8acc0f67d7860a485f31859ccd996b8e445a"),
    "CA-D-625": (2, "e93771b7615b4c4ac74b36927196dc4f532ef8e598b7dbdf0ad23cc89e0fff38"),
    "CA-D-626": (3, "d11441faffe55da24cf641369b4ab67ab83fad2b537a0bc176407f3dd2e562f8"),
    "CA-D-441": (5, "30042a747a31e13c2618a7111a884c5af1ed2175c687645f9eaae9f6d5d10e81"),
    "CA-D-442": (6, "caa3df94215a7ae1e3e516c0bf94cae1295c79270f0f521e6f75a1eb51d70a2f"),
    "CA-O-211": (3, "cb55a19f11c8d0b653cce695b2829a21984b1738a48b5ae63397b899860232bd"),
})


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
    return _make_scope_receiver(selection, validate_settings, schema_sources, action_definition,
                                action_id="CA-O-212", operation="read")


def _make_scope_receiver(
    selection: ProjectSelection, validate_settings: Callable[[dict], None],
    schema_sources: Collection[FileSource], action_definition: FileSource,
    *, action_id: str, operation: str,
) -> Callable:
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
        raise TypeError(f"Selected {action_id.removeprefix('CA-')} source pin is required.")
    action = _metadata(action_definition)
    version = action.get("version")
    if (action.get("atom_id") != action_id or action.get("content_role") != "Operations"
            or action.get("type") != "Action" or action.get("status") != "Active"
            or type(version) is not int or version < 1):
        raise ValueError(f"Current {action_id.removeprefix('CA-')} Action definition is required.")
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
                raise ConnectorBindingError("input_invalid", f"Scope {operation.title()} admits no requested effects.", "delta")
            return outer["parameters"], outer["definition_manifest"]

        try:
            admission, request = admission_for_started_action(
                session, action_run_id, root=selection.root, action_definition=action_definition,
                action_atom_id=action_id, action_version=version,
                map_request=map_request,
            )
            bindings = ConnectorBindings(
                admission, supported_operations={operation}, supported_kinds={"Scope Unit"},
                validate_payload=validate_payload, resolve_sources=lambda _request: sources,
                authority_sources=(*schemas, action_definition),
            )
            with bind_selection(selection):
                return execute_scope_request(request, bindings=bindings,
                                             project_name=project_name, source_view="current")
        except ConnectorBindingError as error:
            return {"data": None, "current_state": None, "effects": [], "errors": [error.record()]}

    return receive


def make_scope_query_receiver(
    selection: ProjectSelection, *, schema_sources: Collection[FileSource],
    action_definition: FileSource,
) -> Callable:
    """Bind the accepted current Query and complete Settings schema privately.

    Schema-valid Settings observations suffice here; this receiver makes no
    verified-history claim and does not register a route or start another Run.
    """
    if not isinstance(selection, ProjectSelection):
        raise TypeError("Validated Project selection is required.")
    schemas = tuple(schema_sources)
    expected = {**SCHEMA_PINS, **SCOPE_QUERY_PINS}
    expected.pop("CA-O-211")
    by_identity = {}
    for source in schemas:
        if (not isinstance(source, FileSource) or source.root != selection.root
                or source.sha256 is None):
            raise ValueError("Exact selected Project schema sources are required.")
        metadata = _metadata(source)
        identity = metadata.get("atom_id")
        pin = expected.get(identity)
        if (pin is None or identity in by_identity or metadata.get("version") != pin[0]
                or source.sha256 != pin[1]):
            raise ValueError("Query schema differs from the complete accepted source frontier.")
        by_identity[identity] = source
    if by_identity.keys() != expected.keys():
        raise ValueError("The complete accepted Query and Settings schema frontier is required.")
    if (not isinstance(action_definition, FileSource) or action_definition.root != selection.root
            or action_definition.sha256 != SCOPE_QUERY_PINS["CA-O-211"][1]):
        raise ValueError("Exact accepted O211 Action definition is required.")
    settings_schemas = tuple(by_identity[identity] for identity in SCHEMA_PINS)
    relative = selection.settings_path.relative_to(selection.root)
    settings_source = FileSource(selection.root, relative,
                                selection.provenance.get(relative.as_posix(), {}).get("sha256"))

    def validate_settings(document: dict) -> None:
        observed = read_project_settings(settings_source, schema_sources=settings_schemas)
        if observed.snapshot is None:
            error = observed.errors[0]
            raise ConnectorBindingError(error.code, error.message, error.field)
        snapshot = observed.snapshot
        if (snapshot.to_document() != document or snapshot.name != selection.settings["project"]["name"]
                or snapshot.control_root != selection.control_relative.as_posix()):
            raise ConnectorBindingError("schema_invalid", "Settings differs from the selected Project.", "context")

    return _make_scope_receiver(selection, validate_settings, schemas, action_definition,
                                action_id="CA-O-211", operation="query")
