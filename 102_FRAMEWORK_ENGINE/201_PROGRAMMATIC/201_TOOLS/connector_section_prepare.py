"""Private, effect-free section preparation; no receiver, writer or public route.

The receiver supplies an already admitted request and verified Project context.
The returned complete bytes are a proposal, not permission to publish them.
"""

from __future__ import annotations

import hashlib
import re

from connector_atom_parse import IDENTITY, ROLES
from connector_bindings import BoundRequest
from connector_section_parse import SectionError, edit_section, parse_sections
from connector_section_read import read_section_source
from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import (
    ProposedCarrierError, VerifiedSourceContext, _current, _source,
    validate_proposed_carrier,
)


SECTION_AUTHORITY_IDS = ("CA-R-1933", "CA-M-373", "CA-D-623")


def prepare_section(bound: BoundRequest, context: VerifiedSourceContext) -> bytes:
    """Validate one sealed section delta against its complete current Atom.

    Expected state uses the existing logical Atom version/source-token vocabulary.
    No path or delta is accepted separately from the admitted request. Unchanged
    bytes are returned exactly, with no lifecycle, Version, timestamp or Run effect.
    """
    if not isinstance(bound, BoundRequest):
        raise SectionError("permission_denied", "Section preparation requires an admitted request.", "authorization")
    if not isinstance(context, VerifiedSourceContext):
        raise SectionError("schema_invalid", "Section preparation requires verified Project authority.", "context")
    bound.revalidate_before_effect()
    request = bound.request
    target = request.get("target")
    if (request.get("operation") != "modify" or request.get("query") is not None
            or type(target) is not dict or target.keys() != {"kind", "identity"}
            or target["kind"] != "Atom" or not isinstance(target["identity"], str)
            or IDENTITY.fullmatch(target["identity"]) is None):
        raise SectionError("input_invalid", "Section preparation requires one exact logical Atom modification.", "target")
    expected = request.get("expected_state")
    if (type(expected) is not dict or not expected
            or not expected.keys() <= {"identity", "version", "source_token"}
            or not {"version", "source_token"}.intersection(expected)
            or ("version" in expected and (type(expected["version"]) is not int or expected["version"] < 1))
            or ("source_token" in expected and (type(expected["source_token"]) is not str
                or re.fullmatch(r"[0-9a-f]{64}", expected["source_token"]) is None))):
        raise SectionError("input_invalid", "An exact expected Version or source token is required.", "expected_state")
    raw, sections = read_section_source(bound)
    source = bound.sources[0]
    path = source.root / source.relative_path
    if source.root != context.root or not path.is_relative_to(context._selection.control_root):
        raise SectionError("schema_invalid", "The source is outside the verified Project control root.", "context")
    relative = path.relative_to(context._selection.control_root)
    try:
        with bind_selection(context._selection):
            report = {"bindings": {}, "coverage": {"gaps": []}}
            for identifier in SECTION_AUTHORITY_IDS:
                _source(context.root, identifier, context._reader, report)
        parsed = parse_carrier(raw, path)
        if parsed.metadata.get("atom_id") != target["identity"]:
            raise SectionError("target_not_found", "The bound source does not carry the requested Atom identity.", "target")
        if parsed.metadata.get("content_role") != ROLES[target["identity"].split("-")[1]]:
            raise SectionError("schema_invalid", "Atom ID kind and Content Role disagree.", "target")
        observed = {"identity": parsed.metadata["atom_id"], "version": parsed.metadata.get("version"),
                    "source_token": hashlib.sha256(raw).hexdigest()}
        if any(observed[key] != value for key, value in expected.items()):
            raise SectionError("stale_state", "The complete Atom differs from the expected state.", "expected_state")
        validate_proposed_carrier(parsed.metadata, parsed.body, context, relative)
        proposed = edit_section(raw, request.get("delta"))
        candidate = parse_carrier(proposed, path)
        candidate_sections = parse_sections(proposed)
        # Includes Type, ID, Version and updated_at: a section edit cannot alter
        # any Property. The pure editor independently protects Summary bytes.
        if (raw[:sections[0].start] != proposed[:candidate_sections[0].start]
                or candidate.metadata != parsed.metadata):
            raise SectionError("schema_invalid", "Section preparation cannot change Atom Properties.")
        validate_proposed_carrier(candidate.metadata, candidate.body, context, relative)
        _current(context._reader)
    except (CarrierError, ProposedCarrierError) as error:
        raise SectionError("schema_invalid", "Complete Atom validation or its source authority is unavailable.", "context") from error
    bound.revalidate_before_effect()
    return proposed
