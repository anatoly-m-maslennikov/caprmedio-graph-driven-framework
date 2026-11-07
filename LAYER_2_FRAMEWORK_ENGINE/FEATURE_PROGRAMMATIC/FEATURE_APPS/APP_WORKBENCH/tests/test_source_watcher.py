# CA-R-2950@1
# CA-M-490@1
# CA-D-695@1
# CA-E-780@4
# CA-E-677@22
"""Watcher callback translation is deterministic before service batch handling."""

from pathlib import Path
from types import SimpleNamespace
import sys
import tempfile
import threading
import time
import unittest


sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher import SourceWatcher  # noqa: E402


class _Observer:
    def __init__(self) -> None:
        self.handler = None
        self.path = None
        self.recursive = None
        self.started = False
        self.stopped = False
        self.joined = False
        self.schedules = []
        self.unscheduled = []
        self.pending_changes = None

    def schedule(self, handler, path: str, recursive: bool) -> str:
        if not recursive:
            assert self.pending_changes is not None
            assert not self.pending_changes(0), "change published before directory watch registration"
        self.schedules.append((path, recursive))
        self.handler, self.path, self.recursive = handler, path, recursive
        return path

    def unschedule(self, watch: str) -> None:
        self.unscheduled.append(watch)

    def start(self) -> None:
        self.started = True

    def stop(self) -> None:
        self.stopped = True

    def join(self) -> None:
        self.joined = True


class SourceWatcherTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.control = self.root / ".caprmedio_example"
        self.control.mkdir()
        self.observer = _Observer()
        self.watcher = SourceWatcher(
            self.root, self.control, observer_factory=lambda: self.observer,
        )
        self.observer.pending_changes = self.watcher.changes
        self.watcher.start()

    def event(self, source: Path, *, destination: Path | None = None, directory: bool = False):
        return SimpleNamespace(
            src_path=str(source), dest_path=str(destination) if destination is not None else None,
            is_directory=directory,
        )

    def test_file_callbacks_keep_selected_repository_relative_paths(self) -> None:
        path = self.control / "04_requirement/CA-R-1.md"
        self.observer.handler.on_created(self.event(path))
        self.observer.handler.on_modified(self.event(path))
        self.observer.handler.on_deleted(self.event(path))

        self.assertEqual([
            {"operation": "create", "old_path": None, "new_path": ".caprmedio_example/04_requirement/CA-R-1.md"},
            {"operation": "update", "old_path": None, "new_path": ".caprmedio_example/04_requirement/CA-R-1.md"},
            {"operation": "remove", "old_path": ".caprmedio_example/04_requirement/CA-R-1.md", "new_path": None},
        ], self.watcher.changes(0))

    def test_moves_keep_native_boundary_and_parent_meaning(self) -> None:
        old = self.control / "04_requirement/CA-R-1.md"
        renamed = self.control / "04_requirement/CA-R-2.md"
        moved = self.control / "05_method/CA-R-2.md"
        outside = self.root / "outside.md"
        self.observer.handler.on_moved(self.event(old, destination=renamed))
        self.observer.handler.on_moved(self.event(renamed, destination=moved))
        self.observer.handler.on_moved(self.event(outside, destination=old))
        self.observer.handler.on_moved(self.event(moved, destination=outside))
        self.observer.handler.on_moved(self.event(outside, destination=self.root / "elsewhere.md"))

        self.assertEqual([
            {"operation": "rename", "old_path": ".caprmedio_example/04_requirement/CA-R-1.md", "new_path": ".caprmedio_example/04_requirement/CA-R-2.md"},
            {"operation": "move", "old_path": ".caprmedio_example/04_requirement/CA-R-2.md", "new_path": ".caprmedio_example/05_method/CA-R-2.md"},
            {"operation": "create", "old_path": None, "new_path": ".caprmedio_example/04_requirement/CA-R-1.md"},
            {"operation": "remove", "old_path": ".caprmedio_example/05_method/CA-R-2.md", "new_path": None},
        ], self.watcher.changes(0))

    def test_directory_create_move_remove_are_kept_but_modify_is_ignored(self) -> None:
        directory = self.control / "04_requirement"
        other = self.control / "nested/05_method"
        self.observer.handler.on_created(self.event(directory, directory=True))
        self.observer.handler.on_modified(self.event(directory, directory=True))
        self.observer.handler.on_moved(self.event(directory, destination=other, directory=True))
        self.observer.handler.on_deleted(self.event(other, directory=True))

        self.assertEqual([
            {"operation": "create", "old_path": None, "new_path": ".caprmedio_example/04_requirement"},
            {"operation": "move", "old_path": ".caprmedio_example/04_requirement", "new_path": ".caprmedio_example/nested/05_method"},
            {"operation": "remove", "old_path": ".caprmedio_example/nested/05_method", "new_path": None},
        ], self.watcher.changes(0))

    def test_directory_reported_as_file_gets_a_child_watch_and_removal_cleans_it_up(self) -> None:
        directory = self.control / "new"
        directory.mkdir()
        self.observer.handler.on_created(self.event(directory))

        self.assertIn((str(directory.resolve()), False), self.observer.schedules)
        self.observer.handler.on_deleted(self.event(directory))
        self.assertIn(str(directory.resolve()), self.observer.unscheduled)

    def test_native_directory_events_reuse_the_recursive_observer(self) -> None:
        directory = self.control / "new"
        directory.mkdir()
        self.observer.handler.on_created(self.event(directory, directory=True))
        self.watcher.changes(0)
        destination = self.control / "renamed"
        directory.rename(destination)
        self.observer.handler.on_moved(self.event(directory, destination=destination, directory=True))
        self.assertEqual([(str(self.control), True)], self.observer.schedules)
        self.assertEqual(1, len(self.watcher._watched_directories))

    def test_moved_in_directory_gets_a_child_watch_before_move_is_recorded(self) -> None:
        source = self.root / "outside"
        destination = self.control / "moved"
        source.mkdir()
        source.rename(destination)

        self.observer.handler.on_moved(self.event(source, destination=destination))

        self.assertIn((str(destination.resolve()), False), self.observer.schedules)
        self.assertEqual([
            {"operation": "create", "old_path": None, "new_path": ".caprmedio_example/moved"},
        ], self.watcher.changes(0))

    def test_close_stops_the_native_observer(self) -> None:
        self.watcher.close()
        self.assertTrue(self.observer.stopped)
        self.assertTrue(self.observer.joined)

    def test_positive_timeout_collects_one_fixed_event_window(self) -> None:
        self.watcher._record("create", None, ".caprmedio_example/first.md")

        def add_update() -> None:
            time.sleep(0.01)
            self.watcher._record("update", None, ".caprmedio_example/first.md")

        worker = threading.Thread(target=add_update)
        worker.start()
        batch = self.watcher.changes(0.05)
        worker.join(timeout=1)

        self.assertEqual(["create", "update"], [event["operation"] for event in batch])

    def test_control_root_outside_project_is_refused(self) -> None:
        with self.assertRaisesRegex(ValueError, "inside the selected repository"):
            SourceWatcher(self.root, self.root.parent / "other")


if __name__ == "__main__":
    unittest.main()
