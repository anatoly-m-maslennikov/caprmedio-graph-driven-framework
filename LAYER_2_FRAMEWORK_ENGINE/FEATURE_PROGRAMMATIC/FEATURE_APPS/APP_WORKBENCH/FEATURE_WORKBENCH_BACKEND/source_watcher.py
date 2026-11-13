# CA-R-2950@4
# CA-M-465@29
# CA-M-490@3
# CA-D-695@3

"""Translate native selected-source watcher callbacks into Workbench changes."""

from __future__ import annotations

from queue import Empty, Queue
from pathlib import Path
import time
from typing import Any, Callable

NativeObserver: Callable[[], Any] | None

try:
    from watchdog.events import FileSystemEventHandler
    from watchdog.observers import Observer
    NativeObserver = Observer
except ImportError:  # Tests can inject an Observer without an installed runtime dependency.
    FileSystemEventHandler = object  # type: ignore[assignment,misc]
    NativeObserver = None


Change = dict[str, str | None]


class SourceWatcher:
    """Watch selected Project roots; the service owns batch handling and refresh."""

    def __init__(
        self, root: Path, control_root: Path,
        *, implementation_root: Path | None = None, observer_factory: Callable[[], Any] | None = None,
    ) -> None:
        self._root = Path(root).absolute()
        self._control_root = Path(control_root).absolute()
        roots = (self._control_root,) if implementation_root is None else (self._control_root, implementation_root)
        self._roots = tuple(Path(path).absolute() for path in roots)
        self._resolved_roots = tuple(path.resolve() for path in self._roots)
        self._resolved_root = self._root.resolve()
        if any(not path.is_relative_to(self._root) for path in self._roots) or any(
            not path.is_relative_to(self._resolved_root) for path in self._resolved_roots
        ):
            raise ValueError("Workbench sources must be inside the selected repository")
        self._observer_factory = observer_factory
        self._observer: Any = None
        self._changes: Queue[Change] = Queue()
        self._watched_directories: dict[Path, Any] = {}

    def start(self) -> None:
        if self._observer is not None:
            return
        factory = self._observer_factory or NativeObserver
        if factory is None:
            raise RuntimeError("watchdog runtime is unavailable")
        observer = factory()
        self._watched_directories = {
            path: observer.schedule(_Handler(self), str(path), recursive=True)
            for path in self._roots
        }
        observer.start()
        self._observer = observer

    def changes(self, timeout: float) -> list[Change]:
        try:
            first = self._changes.get(timeout=timeout)
        except Empty:
            return []
        batch = [first]
        if timeout <= 0:
            return self._drain(batch)
        deadline = time.monotonic() + timeout
        while True:
            try:
                batch.append(self._changes.get(timeout=max(0, deadline - time.monotonic())))
            except Empty:
                return batch

    def _drain(self, batch: list[Change]) -> list[Change]:
        while True:
            try:
                batch.append(self._changes.get_nowait())
            except Empty:
                return batch

    def close(self) -> None:
        if self._observer is None:
            return
        self._observer.stop()
        self._observer.join()
        self._observer = None
        self._watched_directories = {}

    def _record(self, operation: str, old_path: str | None, new_path: str | None) -> None:
        self._changes.put({"operation": operation, "old_path": old_path, "new_path": new_path})

    def _relative(self, path: str) -> str | None:
        candidate = Path(path)
        if not candidate.is_absolute():
            return None
        if ".." in candidate.parts:
            return None
        if any(candidate.is_relative_to(root) for root in self._roots):
            return candidate.relative_to(self._root).as_posix()
        resolved = candidate.resolve(strict=False)
        for root, resolved_root in zip(self._roots, self._resolved_roots, strict=True):
            if resolved.is_relative_to(resolved_root):
                return (root.relative_to(self._root) / resolved.relative_to(resolved_root)).as_posix()
        return None

    def _created(self, path: str) -> None:
        if relative := self._relative(path):
            self._record("create", None, relative)

    def _watch_directory(self, path: str) -> None:
        """Watch a new directory when the native recursive watch misses its first child."""
        directory = Path(path).resolve(strict=False)
        if self._observer is None or directory in self._watched_directories:
            return
        if directory.is_dir() and any(directory.is_relative_to(root) for root in self._resolved_roots):
            watch = self._observer.schedule(_Handler(self), str(directory), recursive=False)
            self._watched_directories[directory] = watch

    def _watch_directory_tree(self, path: str) -> None:
        directory = Path(path).resolve(strict=False)
        if not any(directory.is_relative_to(root) for root in self._resolved_roots):
            return
        self._watch_directory(str(directory))
        if directory.is_dir():
            for child in directory.rglob("*"):
                if child.is_dir():
                    self._watch_directory(str(child))

    def _unwatch_directory(self, path: str) -> None:
        directory = Path(path).resolve(strict=False)
        for watched in [
            item for item in self._watched_directories
            if item not in self._roots and (item == directory or item.is_relative_to(directory))
        ]:
            watch = self._watched_directories.pop(watched)
            if hasattr(self._observer, "unschedule"):
                self._observer.unschedule(watch)

    def _modified(self, path: str, is_directory: bool) -> None:
        if not is_directory and (relative := self._relative(path)):
            self._record("update", None, relative)

    def _deleted(self, path: str) -> None:
        if relative := self._relative(path):
            self._record("remove", relative, None)

    def _moved(self, source: str, destination: str) -> None:
        self._unwatch_directory(source)
        old_path = self._relative(source)
        new_path = self._relative(destination)
        if old_path is None:
            if new_path is not None:
                self._record("create", None, new_path)
            return
        if new_path is None:
            self._record("remove", old_path, None)
            return
        operation = "rename" if Path(old_path).parent == Path(new_path).parent else "move"
        self._record(operation, old_path, new_path)


class _Handler(FileSystemEventHandler):
    def __init__(self, watcher: SourceWatcher) -> None:
        super().__init__()
        self._watcher = watcher

    def on_created(self, event: Any) -> None:
        # Docker bind mounts can report a directory as a file.
        if event.is_directory or Path(event.src_path).is_dir():
            self._watcher._watch_directory_tree(event.src_path)
        self._watcher._created(event.src_path)

    def on_modified(self, event: Any) -> None:
        self._watcher._modified(event.src_path, event.is_directory)

    def on_deleted(self, event: Any) -> None:
        self._watcher._deleted(event.src_path)
        self._watcher._unwatch_directory(event.src_path)

    def on_moved(self, event: Any) -> None:
        if event.is_directory or Path(event.dest_path).is_dir():
            self._watcher._watch_directory_tree(event.dest_path)
        self._watcher._moved(event.src_path, event.dest_path)
