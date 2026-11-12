"""Private directory carrier relocation under the lifecycle writer lock."""
from __future__ import annotations

import hashlib
import os
import stat
from pathlib import Path

from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS

from . import effects


def _read_asset(fd: int, name: str, root: Path | None = None, path: Path | None = None) -> bytes:
    reader = effects._reader(path) if path is not None else None
    if reader is not None:
        if os.stat(name, dir_fd=fd, follow_symlinks=False).st_size > CEILINGS["max_file_bytes"]:
            raise ValueError("directory asset exceeds max_file_bytes")
        data = effects._query_read(reader, root, path, fd, name)
        if len(data) > CEILINGS["max_file_bytes"]:
            raise ValueError("directory asset exceeds max_file_bytes")
        return data
    asset = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=fd)
    with os.fdopen(asset, "rb") as stream:
        info = os.fstat(stream.fileno())
        if not stat.S_ISREG(info.st_mode):
            raise ValueError("carrier is not a regular file")
        limit = CEILINGS["max_file_bytes"]
        if info.st_size > limit:
            raise ValueError("directory asset exceeds max_file_bytes")
        data = stream.read(limit + 1)
        if len(data) > limit:
            raise ValueError("directory asset exceeds max_file_bytes")
        return data


def _snapshot(fd: int, prefix: Path = Path(), total: list[int] | None = None, *,
              root: Path | None = None, base: Path | None = None) -> tuple[list[Path], dict[Path, str]]:
    if total is None:
        total = [0]
    directories = []
    files = {}
    for name in sorted(os.listdir(fd)):
        path = prefix / name
        mode = os.stat(name, dir_fd=fd, follow_symlinks=False).st_mode
        if stat.S_ISDIR(mode):
            child = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            try:
                nested_dirs, nested_files = _snapshot(child, path, total, root=root, base=base)
            finally:
                os.close(child)
            directories.append(path)
            directories.extend(nested_dirs)
            files.update(nested_files)
        elif stat.S_ISREG(mode):
            data = _read_asset(fd, name, root, base / path if base is not None else None)
            total[0] += len(data)
            if total[0] > CEILINGS["max_total_read_bytes"]:
                raise ValueError("directory assets exceed max_total_read_bytes")
            files[path] = hashlib.sha256(data).hexdigest()
        else:
            raise ValueError("directory carrier contains a symlink or non-regular asset")
    return directories, files


def _read_tree(root: Path, path: Path) -> tuple[list[Path], dict[Path, str]]:
    parent, name, _ = effects._parent(root, path)
    try:
        fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
        try:
            return _snapshot(fd, root=root, base=path)
        finally:
            os.close(fd)
    finally:
        os.close(parent)


def _directory_change(root: Path, path: Path, result: effects.Result, create: bool) -> None:
    parent = None
    committed = False
    target = None
    operation = "create" if create else "remove"
    try:
        parent, name, target = effects._parent(root, path)
        if create:
            os.mkdir(name, dir_fd=parent)
        else:
            os.rmdir(name, dir_fd=parent)
        committed = True
        if create:
            fd = os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
            os.close(fd)
        else:
            try:
                os.stat(name, dir_fd=parent, follow_symlinks=False)
            except FileNotFoundError:
                pass
            else:
                raise OSError("directory remains after removal")
        effects._effect(result, operation, target, "known", "directory created" if create else "directory absent after removal")
    except (OSError, ValueError) as exc:
        if committed:
            effects._effect(result, operation, target, "unknown", "directory change occurred but readback failed")
            effects._error(result, "effect_uncertain", effects._message(exc))
        else:
            effects._error(result, "stale_state" if isinstance(exc, (ValueError, FileExistsError)) else "backend_failure", effects._message(exc))
    finally:
        if parent is not None:
            os.close(parent)


def _copy_tree(root: Path, source: Path, destination: Path, directories: list[Path],
               files: dict[Path, str], rewrites: dict[Path, tuple[str, bytes]],
               result: effects.Result) -> None:
    _directory_change(root, destination, result, True)
    for directory in directories:
        if result.errors:
            return
        _directory_change(root, destination / directory, result, True)
    for path, digest in files.items():
        if result.errors:
            return
        parent = None
        try:
            parent, name, _ = effects._parent(root, source / path)
            content = _read_asset(parent, name, root, source / path)
            if hashlib.sha256(content).hexdigest() != digest:
                raise ValueError("directory asset changed")
        except (OSError, ValueError, RuntimeError) as exc:
            effects._error(result, "stale_state" if isinstance(exc, ValueError) else "backend_failure", effects._message(exc))
            return
        finally:
            if parent is not None:
                os.close(parent)
        if path in rewrites:
            content = rewrites[path][1]
        created = effects.create(root, destination / path, content)
        result.effects.extend(created.effects)
        result.errors.extend(created.errors)


def _remove_tree(root: Path, source: Path, directories: list[Path],
                 files: dict[Path, str], result: effects.Result) -> None:
    for path, digest in files.items():
        removed = effects.remove(root, source / path, digest)
        result.effects.extend(removed.effects)
        result.errors.extend(removed.errors)
        if result.errors:
            return
    for directory in reversed(directories):
        _directory_change(root, source / directory, result, False)
        if result.errors:
            return
    _directory_change(root, source, result, False)


def _rewrite_pins(files: dict[Path, str], rewrites: dict[Path, tuple[str, bytes]]) -> dict[Path, str]:
    target = files.copy()
    for path, replacement in rewrites.items():
        if (not isinstance(path, Path) or path.is_absolute() or not path.parts or
                ".." in path.parts or path not in files or not isinstance(replacement, tuple) or
                len(replacement) != 2 or not isinstance(replacement[1], bytes) or
                replacement[0] != files[path]):
            raise ValueError("invalid or stale directory asset rewrite")
        if len(replacement[1]) > CEILINGS["max_file_bytes"]:
            raise ValueError("directory asset exceeds max_file_bytes")
        target[path] = hashlib.sha256(replacement[1]).hexdigest()
    return target


def move_directory(root: Path, source: Path, destination: Path, *, rewrites=None) -> effects.Result:
    """Copy and verify the complete tree before removing the pinned source tree."""
    root, source, destination = Path(root), Path(source), Path(destination)
    result = effects.Result()
    try:
        source_parent, _, source_target = effects._parent(root, source)
        os.close(source_parent)
        destination_parent, _, destination_target = effects._parent(root, destination)
        os.close(destination_parent)
        if destination_target == source_target or destination_target.startswith(source_target + "/"):
            raise ValueError("destination is inside source")
        directories, files = _read_tree(root, source)
        if rewrites is None:
            rewrites = {}
        if not isinstance(rewrites, dict):
            raise ValueError("invalid directory asset rewrites")
        targets = _rewrite_pins(files, rewrites)
    except (OSError, ValueError, RuntimeError) as exc:
        effects._error(result, "stale_state" if isinstance(exc, ValueError) else "backend_failure", effects._message(exc))
        return result

    _copy_tree(root, source, destination, directories, files, rewrites, result)
    if result.errors:
        return result
    try:
        if _read_tree(root, destination) != (directories, targets) or _read_tree(root, source) != (directories, files):
            raise ValueError("directory carrier changed or readback differs")
    except (OSError, ValueError, RuntimeError) as exc:
        effects._error(result, "stale_state" if isinstance(exc, ValueError) else "backend_failure", effects._message(exc))
        return result
    _remove_tree(root, source, directories, files, result)
    return result
