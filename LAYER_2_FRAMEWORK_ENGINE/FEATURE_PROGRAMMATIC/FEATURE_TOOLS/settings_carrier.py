# CA-M-284@32
# CA-E-454@23
"""Shared TOML Settings Carrier I/O; callers retain their own schemas and paths."""

from pathlib import Path
import tomllib
import os
import tempfile
from collections.abc import Callable
from typing import Any


def parse_settings_carrier(raw: bytes) -> dict[str, Any]:
    return tomllib.loads(raw.decode("utf-8"))


def read_settings_carrier(path: Path, *, read_bytes: Callable[[Path], bytes] | None = None) -> dict[str, Any]:
    raw = read_bytes(path) if read_bytes is not None else path.read_bytes()
    return parse_settings_carrier(raw)


def write_settings_carrier(path: Path, text: str, *, validate: Callable[[dict[str, Any]], object]) -> None:
    """Validate the complete proposed TOML using the Carrier's schema before replacement."""
    document = parse_settings_carrier(text.encode("utf-8"))
    validate(document)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(text.encode("utf-8"))
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise
