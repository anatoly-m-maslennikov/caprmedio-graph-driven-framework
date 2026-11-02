"""Read one privately bound complete Atom without storage mutation."""

from __future__ import annotations

from connector_section_parse import Section, SectionError, parse_sections


def read_section_source(bound) -> tuple[bytes, list[Section]]:
    """Read the source already resolved by its existing selected binding.

    The receiver owns complete Atom validation and expected-state interpretation.
    This helper adds no public identity, state schema or authorization protocol.
    """
    from connector_bindings import BoundRequest

    if not isinstance(bound, BoundRequest):
        raise SectionError("permission_denied", "An existing selected binding is required.", "authorization")
    if len(bound.sources) != 1:
        code = "target_ambiguous" if bound.sources else "target_not_found"
        raise SectionError(code, "Section edit requires exactly one bound Atom source.", "target")
    raw = bound.sources[0].read_bytes()
    sections = parse_sections(raw)
    bound.revalidate_before_effect()
    return raw, sections
