"""Author membership in the Project's authoritative Operator registry."""

from operator_registry import OperatorRegistryError, parse_operators_registry

from .authority import Record
from .check_support import Check, _string
from .read_io import ReadContext
from .settings import bound_file
from .support_authority import require_sources


def load_operators_registry(request: Record, reader: ReadContext) -> Record:
    """Load once per assessment through the existing bounded, fingerprinted reader."""
    if "operators_registry" not in request:
        return dict(names=None, error="Author membership needs a selected Operator registry.")
    try:
        raw = bound_file(reader, request["operators_registry"])
        registry = parse_operators_registry(raw)
    except (OSError, ValueError, OperatorRegistryError):
        return dict(
            names=None,
            error="Operator registry is unavailable, stale, malformed, or has ambiguous entries.",
        )
    return dict(names=frozenset(entry.name for entry in registry), error=None)


def author_membership(metadata: Record, body: str, check: Check) -> None:
    del body
    check.require(metadata, "author", _string)
    if check.findings or not require_sources(check, ("CA-D-494",)):
        return
    registry = check.inputs.get("operators_registry", {})
    names = registry.get("names")
    if names is None:
        check.gap(
            "author",
            registry.get("error") or "Author membership needs the selected Operator registry.",
        )
    elif metadata["author"] not in names:
        check.fail(
            "AUTHOR_UNREGISTERED",
            "author",
            "Author is not an exact registered Operator name in the selected Operator registry.",
        )
