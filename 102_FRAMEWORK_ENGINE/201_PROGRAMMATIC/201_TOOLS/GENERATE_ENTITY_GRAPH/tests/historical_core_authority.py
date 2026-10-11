"""Exact historical Core carriers required by detached graph tests."""

from __future__ import annotations

import hashlib
from pathlib import Path, PurePosixPath


_ASSET_ROOT = Path(__file__).resolve().parent / "historical_core_authority"
_PINS = {
    "06_evaluation/CA-E-449-CORE_META_MODEL-GENERAL-EVALUATION_APPROACH--validate-entities-graph.md": (
        "29db3bbff5744963c4fc7960042e6267a826b2fe16198e954039f5b223f3b00a"
    ),
    "05_method/CA-M-310-CORE_META_MODEL--write-requirement-claims-with-the-requirement-cce-profile.md": (
        "b41cd2dfe70813a227d0253e717c5d39ac6d5cb842ea72524ce0582476ed0db6"
    ),
    "07_delivery/CA-D-478-CORE_META_MODEL-CORE-DELIVERY--store-every-atom-property-in-one-internal-location.md": (
        "a40ad3683ecddd536e5b7eb6c044e8da15806ab44946fa1354c408ce5e966464"
    ),
}


def historical_authority_bytes(relative: str, expected_sha256: str) -> bytes | None:
    """Return one committed historical carrier only when its fixed pin agrees."""

    if not isinstance(relative, str) or not isinstance(expected_sha256, str):
        raise ValueError("historical Core authority identity is invalid")
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError("historical Core authority path is unsafe")
    expected = _PINS.get(relative)
    if expected is None:
        return None
    if expected != expected_sha256:
        raise ValueError("historical Core authority pin differs from the test profile")
    root = _ASSET_ROOT
    if any(ancestor.is_symlink() for ancestor in (root, *root.parents)) or not root.is_dir():
        raise RuntimeError("historical Core authority asset root is unsafe")
    try:
        resolved_root = root.resolve(strict=True)
    except OSError as error:
        raise RuntimeError("historical Core authority asset root is unavailable") from error
    carrier = root
    for component in path.parts:
        carrier = carrier / component
        if carrier.is_symlink():
            raise RuntimeError("historical Core authority carrier is unsafe")
    if not carrier.is_file():
        raise RuntimeError("historical Core authority carrier is unavailable")
    try:
        carrier.resolve(strict=True).relative_to(resolved_root)
    except (OSError, ValueError) as error:
        raise RuntimeError("historical Core authority carrier escapes its asset root") from error
    payload = carrier.read_bytes()
    if hashlib.sha256(payload).hexdigest() != expected:
        raise RuntimeError("historical Core authority carrier digest differs from its pin")
    return payload
