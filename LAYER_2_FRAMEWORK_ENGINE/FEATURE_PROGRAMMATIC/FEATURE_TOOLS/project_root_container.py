# CA-R-2779@1

"""Resolve the effective Container of the selected root Project Declaration."""
from collections.abc import Mapping
from hashlib import sha256

from header_groups import header_path, header_value
from scope_declaration_parse import ScopeDeclarationError, ScopeUnitDeclaration, parse_scope_unit_declaration


def is_logical_container(value):
    return (isinstance(value, Mapping) and set(value) in ({'scope_unit'}, {'atom'})
            and all(isinstance(ref, str) and ref.strip() for ref in value.values()))


def effective_root_container_header(
    metadata, *, path, raw, root_declaration_path, root_declaration_pin,
):
    """Return a validation Header without changing the stored carrier metadata."""
    if path != root_declaration_path or root_declaration_pin is None or header_value(metadata, 'container')[0]:
        return metadata
    if sha256(raw).hexdigest() != root_declaration_pin['sha256']:
        return metadata
    try:
        declaration = parse_scope_unit_declaration(raw, path)
    except ScopeDeclarationError:
        return metadata
    if (not isinstance(declaration, ScopeUnitDeclaration) or not declaration.is_root
            or declaration.atom_id != root_declaration_pin['atom_id']
            or declaration.version != root_declaration_pin['version']):
        return metadata

    container = {'scope_unit': 'CA-SU--1'}
    if header_path('container', metadata) == ('context', 'container'):
        return {**metadata, 'context': {**metadata.get('context', {}), 'container': container}}
    return {**metadata, 'container': container}
