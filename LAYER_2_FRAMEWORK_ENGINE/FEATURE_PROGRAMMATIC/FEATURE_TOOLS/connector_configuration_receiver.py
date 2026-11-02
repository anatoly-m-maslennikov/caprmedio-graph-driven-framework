"""Private O218 receiving binding for real current TOML configuration reads."""

from __future__ import annotations

import copy
import tomllib
from collections.abc import Callable, Collection

from artifact_metadata import one_value, split_frontmatter
from connector_bindings import (
    ConnectorBindingError, ConnectorBindings, FileSource, admission_for_started_action,
)
from connector_contract import validate_request
from connector_toml_parse import TomlFailure, equal_values
from connector_toml_read import failure
from connector_toml_shared import execute
from project_selection import ProjectSelection, ProjectSelectionError, bind_selection


def make_configuration_read_receiver(
    selection: ProjectSelection, *, validate_settings: Callable[[dict], None], schema_sources: Collection[FileSource],
    action_definition: FileSource, action_version: int = 2,
):
    """Read Project Settings; Scope Unit declarations are Atom sources, never TOML configuration."""
    if not isinstance(selection, ProjectSelection) or not callable(validate_settings):
        raise TypeError("An existing ProjectSelection and complete Settings validator are required.")
    authorities = tuple(schema_sources)
    if (not authorities or any(not isinstance(source, FileSource) or source.root != selection.root
                               or source.sha256 is None for source in authorities)
            or len({source.relative_path for source in authorities}) != len(authorities)
            or not isinstance(action_definition, FileSource) or action_definition.root != selection.root
            or action_definition.sha256 is None or type(action_version) is not int or action_version < 1):
        raise ValueError("Exact selected Action and complete Settings schema pins are required.")
    identifiers = []
    for source in authorities:
        delimiter, frontmatter, _ = split_frontmatter(
            source.read_bytes().decode("utf-8"), selection.root / source.relative_path,
        )
        identifiers.append(one_value(frontmatter, delimiter, "atom_id"))
    if (any(not isinstance(identity, str) or not identity for identity in identifiers)
            or len(set(identifiers)) != len(identifiers)):
        raise ValueError("Settings schema authority requires distinct declared source Atoms.")

    def retained_settings() -> FileSource:
        relative = selection.settings_path.relative_to(selection.root)
        pin = selection.provenance.get(relative.as_posix(), {}).get("sha256")
        if not isinstance(pin, str) or len(pin) != 64:
            raise ValueError("Selected Settings provenance is unavailable.")
        return FileSource(selection.root, relative, pin)

    settings = retained_settings()
    project = selection.settings["project"]["name"]

    def validate_action():
        delimiter, frontmatter, _ = split_frontmatter(
            action_definition.read_bytes().decode("utf-8"), selection.root / action_definition.relative_path,
        )
        expected = {"atom_id": "CA-O-218", "version": str(action_version),
                    "content_role": "Operations", "type": "Action", "status": "Active"}
        if any(one_value(frontmatter, delimiter, field) != value for field, value in expected.items()):
            raise ConnectorBindingError("permission_denied", "Selected source is not the exact active Configuration Read Action.", "context")

    def validate_document(document):
        source_text = settings.read_bytes().decode("utf-8")
        source = tomllib.loads(source_text)
        preserved = copy.deepcopy(source)
        if validate_settings(source) is not None or not equal_values(source, preserved):
            raise ConnectorBindingError("schema_invalid", "Complete Settings validation must refuse without flags or repair.", "context")
        if not equal_values(document, source):
            raise ConnectorBindingError("stale_state", "Validated Settings differs from the selected source.", "context")
        selection._revalidate_boundary()

    def receive(session, action_run_id):
        try:
            validate_action()
            admission, request = admission_for_started_action(
                session, action_run_id, root=selection.root, action_definition=action_definition,
                action_atom_id="CA-O-218", action_version=action_version,
                map_request=lambda outer: (outer["parameters"], outer["definition_manifest"]),
            )
            if session.request["effects"] != []:
                raise ConnectorBindingError("permission_denied", "Configuration Read requires an empty requested effect frontier.", "authorization")
            errors = validate_request(request, supported_operations={"read"}, supported_kinds={"Configuration"})
            if errors:
                return {"data": None, "current_state": None, "effects": [], "errors": errors}

            def validate_payload(value):
                validate_action()
                if value["target"] != {"kind": "Configuration", "identity": "Project Settings"}:
                    raise ConnectorBindingError("input_invalid", "This receiving binding requires Project Settings.", "target")
                settings.revalidate()
                validate_document(tomllib.loads(settings.read_bytes().decode("utf-8")))

            bindings = ConnectorBindings(
                admission, supported_operations={"read"}, supported_kinds={"Configuration"},
                validate_payload=validate_payload, resolve_sources=lambda _: (settings,),
                authority_sources=(*authorities, action_definition),
            )
            with bind_selection(selection):
                return execute(request, bindings=bindings, project=project, source_view="current",
                               validate_document=validate_document, keys={})
        except ConnectorBindingError as error:
            return failure(TomlFailure(error.code, str(error), error.field))
        except (ProjectSelectionError, UnicodeError, ValueError, TypeError, KeyError, RuntimeError) as error:
            return failure(TomlFailure("schema_invalid", str(error), "context"))

    return receive
