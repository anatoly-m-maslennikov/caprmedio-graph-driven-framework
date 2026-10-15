"""Private no-follow carrier observations; reads grant no storage permission."""

from __future__ import annotations

import hashlib
import os
import stat
from dataclasses import dataclass
from pathlib import Path

from connector_carrier_parsing import removal_guard


class CarrierError(ValueError):
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class Location:
    root: Path
    relative: str


def _fingerprint(value: os.stat_result) -> tuple[int, ...]:
    return (value.st_dev, value.st_ino, value.st_mode, value.st_uid, value.st_gid,
            value.st_size, value.st_mtime_ns, value.st_ctime_ns)


def open_parent(location: Location) -> tuple[int, tuple]:
    """Open every lexical ancestor, including approved-root ancestors, no-follow."""
    if not isinstance(location, Location) or not isinstance(location.root, Path):
        raise CarrierError("input_invalid", "A private resolved location is required.")
    relative = Path(location.relative)
    if (not location.root.is_absolute() or ".." in location.root.parts
            or not location.relative or relative.is_absolute() or ".." in relative.parts
            or not relative.parts or "\x00" in location.relative):
        raise CarrierError("input_invalid", "Carrier locator is outside its approved root.")
    flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW
    descriptor = os.open(location.root.anchor, flags)
    evidence = []
    try:
        for part in (*location.root.parts[1:], *relative.parts[:-1]):
            child = os.open(part, flags, dir_fd=descriptor)
            os.close(descriptor)
            descriptor = child
            evidence.append(_fingerprint(os.fstat(descriptor))[:5])
        evidence[-1] = _fingerprint(os.fstat(descriptor))
        return descriptor, tuple(evidence)
    except OSError as error:
        os.close(descriptor)
        raise CarrierError("input_invalid", "Carrier ancestor is missing, substituted or unsafe.") from error


def _entry(parent: int, name: str, inventory: dict | None, prefix: str = "") -> dict:
    descriptor = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
    try:
        before = os.fstat(descriptor)
        state = {"fingerprint": _fingerprint(before)}
        if stat.S_ISREG(before.st_mode):
            digest = hashlib.sha256()
            prefix = b""
            while chunk := os.read(descriptor, 65536):
                digest.update(chunk)
                if not prefix:
                    prefix = chunk
            state.update(kind="file", digest=digest.hexdigest(), removal_guard=removal_guard(prefix))
        elif stat.S_ISDIR(before.st_mode):
            if inventory is None:
                raise CarrierError("input_invalid", "Folder requires an explicit finite approved inventory.")
            names = sorted(os.listdir(descriptor))
            direct = sorted(key[len(prefix):] for key in inventory
                            if key.startswith(prefix) and "/" not in key[len(prefix):])
            if names != direct:
                raise CarrierError("stale_state", "Folder differs from the approved entry inventory.")
            entries = {}
            for child in names:
                key = prefix + child
                child_state = _entry(descriptor, child, inventory, key + "/")
                if inventory[key] != child_state:
                    raise CarrierError("stale_state", "An approved folder entry changed.")
                entries[child] = child_state
            state.update(kind="folder", entries=entries)
        else:
            raise CarrierError("input_invalid", "Carrier is neither a regular file nor a directory.")
        if _fingerprint(os.fstat(descriptor)) != _fingerprint(before):
            raise CarrierError("stale_state", "Carrier changed while it was observed.")
        return state
    except OSError as error:
        raise CarrierError("input_invalid", "Carrier is symlinked, unreadable or substituted.") from error
    finally:
        os.close(descriptor)


def observe(location: Location, inventory: dict | None = None) -> dict:
    if inventory is not None:
        if not isinstance(inventory, dict):
            raise CarrierError("input_invalid", "Approved inventory must be an exact entry map.")
        for key in inventory:
            if (not isinstance(key, str) or not key or Path(key).is_absolute()
                    or ".." in Path(key).parts or Path(key).as_posix() != key
                    or any(parent.as_posix() not in inventory for parent in Path(key).parents
                           if parent != Path("."))):
                raise CarrierError("input_invalid", "Approved inventory contains an invalid or orphan entry.")
    parent, ancestors = open_parent(location)
    try:
        try:
            os.stat(Path(location.relative).name, dir_fd=parent, follow_symlinks=False)
        except FileNotFoundError:
            return {"present": False, "ancestors": ancestors}
        return {"present": True, "ancestors": ancestors,
                "entry": _entry(parent, Path(location.relative).name, inventory)}
    finally:
        os.close(parent)


def preserved(entry: dict) -> dict:
    """A rename may change ctime; identity, bytes and declared metadata must survive."""
    return {key: (value[:-1] if key == "fingerprint" else
                  {name: preserved(child) for name, child in value.items()} if key == "entries"
                  else value) for key, value in entry.items()}
