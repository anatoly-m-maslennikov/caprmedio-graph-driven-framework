# CA-M-506@2
# CA-D-704@1

"""Load sealed MCP provider modules from one explicit installed package."""

from __future__ import annotations

import hashlib
import importlib.util
import os
from pathlib import Path, PurePosixPath
import stat
import sys
from types import ModuleType


_ENTRYPOINT_PREFIX = PurePosixPath("LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC")
_MODULE_CACHE: dict[Path, tuple[str, ModuleType]] = {}


class RegisteredToolError(ValueError):
    """A descriptor is not eligible for MCP projection."""


def _programmatic_root(package_root: str | Path) -> Path:
    root = Path(package_root).resolve()
    candidate = root.joinpath(*_ENTRYPOINT_PREFIX.parts)
    if not candidate.is_dir():
        raise RegisteredToolError("entrypoint: package root is unavailable")
    return candidate


def _normalise_entrypoint(package_root: str | Path, value: object) -> tuple[str, Path, Path]:
    """Resolve one normalized Python member under the selected package only."""

    if not isinstance(value, str) or not value or "\\" in value:
        raise RegisteredToolError("entrypoint: invalid")
    raw = PurePosixPath(value)
    if (
        raw.is_absolute()
        or raw.as_posix() != value
        or any(part in {"", ".", ".."} for part in raw.parts)
        or any(
            part.lower().startswith(".env") or part.lower().endswith(".env") for part in raw.parts
        )
        or tuple(raw.parts[: len(_ENTRYPOINT_PREFIX.parts)]) != _ENTRYPOINT_PREFIX.parts
    ):
        raise RegisteredToolError("entrypoint: outside trusted programmatic root")
    relative = raw.relative_to(_ENTRYPOINT_PREFIX)
    if not relative.parts or relative.suffix != ".py":
        raise RegisteredToolError("entrypoint: not a Python module")
    programmatic = _programmatic_root(package_root)
    candidate = programmatic.joinpath(*relative.parts)
    try:
        cursor = programmatic
        for part in relative.parts:
            cursor /= part
            if stat.S_ISLNK(os.lstat(cursor).st_mode):
                raise RegisteredToolError("entrypoint: symlink is not admitted")
        if not stat.S_ISREG(os.stat(candidate, follow_symlinks=False).st_mode):
            raise RegisteredToolError("entrypoint: not a regular file")
    except RegisteredToolError:
        raise
    except OSError as error:
        raise RegisteredToolError("entrypoint: unavailable") from error
    return raw.as_posix(), candidate, programmatic


def _read_entrypoint(candidate: Path) -> tuple[str, bytes]:
    """Read exact module bytes without accepting aliases or replacement races."""

    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0) | getattr(os, "O_NOFOLLOW", 0)
    try:
        descriptor = os.open(candidate, flags)
    except OSError as error:
        raise RegisteredToolError("entrypoint: unavailable") from error
    try:
        before = os.fstat(descriptor)
        if not stat.S_ISREG(before.st_mode) or before.st_size > 8 * 1024 * 1024:
            raise RegisteredToolError("entrypoint: not a bounded regular file")
        payload = bytearray()
        while len(payload) <= 8 * 1024 * 1024:
            chunk = os.read(descriptor, min(65536, 8 * 1024 * 1024 + 1 - len(payload)))
            if not chunk:
                break
            payload.extend(chunk)
        after = os.fstat(descriptor)
        if (
            len(payload) > 8 * 1024 * 1024
            or before.st_dev != after.st_dev
            or before.st_ino != after.st_ino
            or before.st_size != after.st_size
            or len(payload) != before.st_size
        ):
            raise RegisteredToolError("entrypoint: changed while being read")
        return hashlib.sha256(payload).hexdigest(), bytes(payload)
    finally:
        os.close(descriptor)


def load_provider(package_root: str | Path, entrypoint: object) -> tuple[str, str, ModuleType]:
    """Import the exact hashed provider bytes from ``package_root`` only."""

    canonical, candidate, programmatic = _normalise_entrypoint(package_root, entrypoint)
    code_hash, payload = _read_entrypoint(candidate)
    cached = _MODULE_CACHE.get(candidate)
    if cached is not None and cached[0] == code_hash:
        return canonical, code_hash, cached[1]

    module_name = f"_caprmedio_registered_{code_hash}"
    spec = importlib.util.spec_from_file_location(module_name, candidate)
    if spec is None or spec.loader is None:
        raise RegisteredToolError("entrypoint: implementation is unavailable")
    module = importlib.util.module_from_spec(spec)
    previous = sys.modules.get(module_name)
    tools_root = str(programmatic / "FEATURE_TOOLS")
    inserted_tools_root = tools_root not in sys.path
    try:
        sys.modules[module_name] = module
        if inserted_tools_root:
            sys.path.insert(0, tools_root)
        exec(compile(payload, str(candidate), "exec", dont_inherit=True), module.__dict__)
    except Exception as error:
        raise RegisteredToolError("entrypoint: descriptor import failed") from error
    finally:
        if inserted_tools_root:
            sys.path.remove(tools_root)
        if previous is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous
    _MODULE_CACHE[candidate] = (code_hash, module)
    return canonical, code_hash, module
