"""Fixed byte-exact graph test inputs, never live authoritative Projections."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path, PurePosixPath


_ASSET_ROOT = Path(__file__).resolve().parent / "historical_core_authority"
_PINS: dict[str, str] = json.loads((_ASSET_ROOT / "pins.json").read_text(encoding="utf-8"))


def _asset_path(path: PurePosixPath) -> Path:
    """Resolve one fixed input without following root or carrier aliases."""
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
    return carrier


def historical_authority_bytes(relative: str, expected_sha256: str) -> bytes:
    """Return one committed test input only when its fixed pin agrees."""
    if not isinstance(relative, str) or not isinstance(expected_sha256, str):
        raise ValueError("historical Core authority identity is invalid")
    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts or not path.parts:
        raise ValueError("historical Core authority path is unsafe")
    expected = _PINS.get(relative)
    if expected is None:
        raise ValueError("historical Core authority is not a fixed test input")
    if expected != expected_sha256:
        raise ValueError("historical Core authority pin differs from the test profile")
    payload = _asset_path(path).read_bytes()
    if hashlib.sha256(payload).hexdigest() != expected:
        raise RuntimeError("historical Core authority carrier digest differs from its pin")
    return payload
