# CA-E-827@1
"""Lifecycle queries include retained carriers and update from file deltas."""
from pathlib import Path
import os
from types import SimpleNamespace
import sys
import threading
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))
import test_incremental_indexing
from smalltest_support import source_path, write_atom
from ATOM_LIFECYCLE.source import ArchiveNotLoadedError


class LifecycleAtomsTests(test_incremental_indexing.IncrementalIndexingTests):
    def test_archive_candidates_sort_numeric_versions_and_require_loaded_history(self):
        paths = [source_path(self.declarations, "ENGINE", "04_requirement", name).resolve() for name in (
            "archive/CA-R-001@2-old.md", "archive/CA-R-001@10-old.md",
            "archive/CA-R-01@20-old.md", "000_draft/CA-R-001@30-draft.md",
            "archive/other/CA-R-001@10-second.md",
        )]
        for path, atom_id, version, status in zip(paths, ("CA-R-001", "CA-R-001", "CA-R-01", "CA-R-001", "CA-R-001"),
                                                   (2, 10, 20, 30, 10),
                                                   ("Archived", "Archived", "Archived", "Draft", "Archived")):
            write_atom(path, atom_id, version=version, status=status)
        copied = source_path(self.declarations, "ENGINE", "04_requirement", "copies/CA-R-001.md")
        write_atom(copied, "CA-R-001", extra="projection: {source_atom_id: CA-R-001}\n")
        self.service._header_schema = None
        self.service._refresh()
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        self.assertEqual([], self.service.lifecycle_candidates(selection, references=("CA-R-001",)))
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_archive_candidates(selection, "CA-R-001")
        self.service.load_archives([{"scope_unit": "ENGINE", "role": "Requirement"}])
        with patch.object(self.service, "lifecycle_read", side_effect=AssertionError("body read")):
            self.assertEqual([("CA-R-001@10", paths[1]), ("CA-R-001@10", paths[4]), ("CA-R-001@2", paths[0])],
                             self.service.lifecycle_archive_candidates(selection, "CA-R-001"))
            self.assertEqual([("CA-R-01@20", paths[2])],
                             self.service.lifecycle_archive_candidates(selection, "CA-R-01"))

    def test_context_lookup_uses_projected_flat_and_grouped_metadata(self):
        flat = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-106.md").resolve()
        grouped = source_path(self.declarations, "ENGINE", "04_requirement", "copies/CA-R-106.md").resolve()
        write_atom(flat, "CA-R-106", extra="container: {scope_unit: ENGINE}\n")
        grouped.parent.mkdir(parents=True, exist_ok=True)
        grouped.write_text(
            '---\nidentity: {atom_id: CA-R-106}\ncontext:\n  role: Requirement\n  form: Definition\n'
            '  container: {atom: CA-P-123}\nstate: {status: Active, version: 2}\n'
            '---\n## Summary\n\nGrouped.\n', encoding="utf-8"
        )
        self.service._header_schema = None
        self.service._refresh()
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        with patch.object(self.service, "lifecycle_read", side_effect=AssertionError("body read")):
            rows = self.service.lifecycle_contexts(selection, "CA-R-106")
        self.assertEqual([flat, grouped], [row[0] for row in rows])
        self.assertEqual("CA-R-106", rows[0][1]["atom_id"])
        self.assertEqual({"scope_unit": "ENGINE"}, rows[0][1]["container"])
        self.assertEqual({"atom": "CA-P-123"}, rows[1][1]["container"])
        self.assertEqual(2, rows[1][1]["version"])
        with self.store._lock:
            self.store._connection.execute("UPDATE atoms SET status_group = 'Backlog' WHERE filename = ?", [grouped.name])
        self.assertEqual([flat, grouped], [row[0] for row in self.service.lifecycle_contexts(selection, "CA-R-106")])
        self.assertEqual([], self.service.lifecycle_contexts(selection, "CA-R-999"))
        flat.unlink()
        with self.assertRaisesRegex(ValueError, "index is stale"):
            self.service.lifecycle_contexts(selection, "CA-R-106")

    def test_request_scoped_read_reuses_bytes_and_invalidates_on_local_write(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-103.md").resolve()
        write_atom(current, "CA-R-103", version=1)
        original_fdopen = os.fdopen
        reads = []

        class Carrier:
            def __init__(self, wrapped):
                self.wrapped = wrapped

            def __enter__(self):
                self.wrapped.__enter__()
                return self

            def __exit__(self, *args):
                return self.wrapped.__exit__(*args)

            def fileno(self):
                return self.wrapped.fileno()

            def read(self, size):
                reads.append(size)
                return self.wrapped.read(size)

        def fdopen(*args, **kwargs):
            return Carrier(original_fdopen(*args, **kwargs))

        with patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service.os.fdopen", side_effect=fdopen):
            with self.service.lifecycle_read_scope():
                first = self.service.lifecycle_read(current)
                with self.service.lifecycle_read_scope():
                    self.assertEqual(first, self.service.lifecycle_read(current))
                self.assertEqual(1, len(reads))
                write_atom(current, "CA-R-103", version=2)
                with self.assertRaisesRegex(ValueError, "changed during lifecycle request"):
                    self.service.lifecycle_read(current)
                self.service.lifecycle_changed(current, current)
                second = self.service.lifecycle_read(current)
                self.assertNotEqual(first, second)
                self.assertEqual(second, self.service.lifecycle_read(current))
                self.assertEqual(2, len(reads))
            self.assertEqual(second, self.service.lifecycle_read(current))
            self.assertEqual(3, len(reads))

    def test_read_scope_cleans_up_after_exception(self):
        path = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-104.md").resolve()
        write_atom(path, "CA-R-104", version=1)
        with self.assertRaisesRegex(RuntimeError, "stop"):
            with self.service.lifecycle_read_scope():
                self.service.lifecycle_read(path)
                raise RuntimeError("stop")
        write_atom(path, "CA-R-104", version=2)
        with self.service.lifecycle_read_scope():
            self.assertEqual(path.read_bytes(), self.service.lifecycle_read(path))

    def test_concurrent_read_scopes_are_isolated(self):
        path = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-105.md").resolve()
        write_atom(path, "CA-R-105")
        barrier = threading.Barrier(2, timeout=5)
        contexts, errors = [], []

        def read():
            try:
                with self.service.lifecycle_read_scope():
                    contexts.append(self.service._lifecycle_reads.get())
                    barrier.wait()
                    self.service.lifecycle_read(path)
            except Exception as error:
                errors.append(error)

        threads = [threading.Thread(target=read) for _ in range(2)]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join(5)
        self.assertEqual([], errors)
        self.assertTrue(all(not thread.is_alive() for thread in threads))
        self.assertEqual(2, len(contexts))
        self.assertIsNot(contexts[0], contexts[1])

    def test_startup_drops_legacy_lifecycle_byte_cache(self):
        import duckdb

        database = self.root / 'legacy.duckdb'
        connection = duckdb.connect(str(database))
        connection.execute('CREATE SCHEMA lifecycle_private')
        connection.execute('CREATE TABLE lifecycle_private.content (raw BLOB)')
        connection.execute("INSERT INTO lifecycle_private.content VALUES ('old source')")
        connection.close()
        store = test_incremental_indexing.QueryStore(
            database_path=database,
            extension_directory=test_incremental_indexing.extension_directory(
                test_incremental_indexing.APP_ROOT.parents[2]
            ),
        )
        try:
            self.assertEqual([], store._connection.execute(
                "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'lifecycle_private'"
            ).fetchall())
        finally:
            store.close()

    def test_lifecycle_read_uses_current_bytes_without_retaining_them(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-102.md").resolve()
        write_atom(current, "CA-R-102", version=1)
        first = self.service.lifecycle_read(current)
        write_atom(current, "CA-R-102", version=2)
        second = self.service.lifecycle_read(current)
        self.assertNotEqual(first, second)
        self.assertEqual(current.read_bytes(), second)
        self.assertEqual([], self.store._connection.execute(
            "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'lifecycle_private'"
        ).fetchall())
        with self.assertRaises(ValueError):
            self.service.lifecycle_read(self.root / "outside.md")

    def test_archive_folder_reference_cannot_match_current_lookup(self):
        archived = source_path(self.declarations, "ENGINE", "04_requirement", "archive/CA-R-101.md").resolve()
        write_atom(archived, "CA-R-101", status="Active")
        self.service._refresh()
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        self.assertEqual([], self.service.lifecycle_candidates(selection, references=("CA-R-101",)))
        self.assertEqual([], self.service.lifecycle_candidates(selection, references=("CA-R-101@1",)))
        self.service.load_archives([{"scope_unit": "ENGINE", "role": "Requirement"}])
        self.assertEqual([("CA-R-101", archived)], self.service.lifecycle_candidates(
            selection, references=("CA-R-101@1",),
        ))
        write_atom(archived, "CA-R-101", status="Active", version=9)
        self.service.lifecycle_changed(archived, archived)
        self.assertEqual(9, self.service.lifecycle_latest_version(selection, "CA-R-101"))

    def test_archives_duplicates_and_immediate_changes_without_rescan(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-101.md").resolve()
        archived = source_path(self.declarations, "ENGINE", "04_requirement", "archive/CA-R-101@1-old.md").resolve()
        duplicate = source_path(self.declarations, "ENGINE", "04_requirement", "copies/CA-R-101.md").resolve()
        draft = source_path(self.declarations, "ENGINE", "04_requirement", "000_draft/CA-R-101@3-draft.md").resolve()
        write_atom(current, "CA-R-101", version=2)
        write_atom(archived, "CA-R-101", status="Archived")
        write_atom(duplicate, "CA-R-101", version=2)
        write_atom(draft, "CA-R-101", status="Draft", version=3)
        self.service._refresh()
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_candidates(selection, atom_ids=("CA-R-101",))
        self.service.load_archives([{"scope_unit": "ENGINE", "role": "Requirement"}])
        self.assertTrue(self.service.wait_for_audits(10))
        candidates = self.service.lifecycle_candidates(selection, atom_ids=("CA-R-101",))
        self.assertEqual({current, archived, duplicate, draft}, {path for _, path in candidates})
        self.assertEqual([["Archived", "CA-R-101@1", 1], ["Current", "CA-R-101", 2],
                          ["Draft", "CA-R-101@3-draft", 1]], self.store.run(
            "SELECT status_group, reference, count(*) FROM atoms WHERE starts_with(reference, 'CA-R-101') "
            "GROUP BY ALL ORDER BY status_group"
        )["rows"])
        self.assertEqual(1, self.service.project_consistency()["duplicate_references"])
        self.assertEqual("CA-R-990001", self.service.lifecycle_last_id(selection, "CA-R-"))
        self.assertEqual(current.read_bytes(), self.service.lifecycle_read(current))
        self.assertEqual(current.read_bytes(), self.service.lifecycle_read(current))
        self.assertEqual([], self.store._connection.execute(
            "SELECT schema_name FROM information_schema.schemata WHERE schema_name = 'lifecycle_private'"
        ).fetchall())
        with patch.object(self.service._reader, "_capture_full", side_effect=AssertionError("full scan")):
            moved = current.with_name("CA-R-101-renamed.md")
            current.rename(moved)
            self.service.lifecycle_changed(current, moved)
            after = self.service.lifecycle_candidates(selection, prefix="CA-R-", under=moved.parent)
            self.assertIn(("CA-R-101", moved), after)
            self.assertNotIn(("CA-R-101", current), after)
            moved.unlink()
            self.service.lifecycle_changed(moved, None)
            remaining = self.service.lifecycle_candidates(selection, atom_ids=("CA-R-101",))
            self.assertEqual({archived, duplicate, draft}, {path for _, path in remaining})
            archived.unlink()
            self.service._refresh([{"operation": "remove", "old_path": archived.relative_to(self.root.resolve()).as_posix(), "new_path": None}])
            self.assertEqual({duplicate, draft}, {path for _, path in
                            self.service.lifecycle_candidates(selection, atom_ids=("CA-R-101",))})

    def test_unloaded_archive_reserves_id_and_version_and_fresh_archive_is_visible(self):
        old = source_path(self.declarations, "ENGINE", "04_requirement", "archive/CA-R-999999999@7-old.md").resolve()
        write_atom(old, "CA-R-999999999", status="Archived", version=7)
        ordinary = old.with_name("CA-R-970@2-ordinary.md")
        write_atom(ordinary, "CA-R-970", status="Archived", version=2)
        self.service._refresh()
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        self.assertEqual("CA-R-999999999", self.service.lifecycle_last_id(selection, "CA-R-"))
        self.assertEqual("CA-R-970", self.service.lifecycle_last_id(selection, "CA-R-", ceiling=1000))
        self.assertEqual(7, self.service.lifecycle_latest_version(selection, "CA-R-999999999"))
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_candidates(selection, atom_ids=("CA-R-999999999",))
        fresh = old.with_name("CA-R-999999998@2-new.md")
        write_atom(fresh, "CA-R-999999998", status="Archived", version=2)
        self.service.lifecycle_changed(None, fresh)
        self.assertEqual([("CA-R-999999998", fresh)], self.service.lifecycle_candidates(
            selection, atom_ids=("CA-R-999999998",), references=("CA-R-999999998@2",),
        ))
        self.assertEqual([], self.service.sync_status()["loaded_archive_scopes"])

    def test_archive_allocation_tables_follow_membership_and_watcher_changes(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-501.md").resolve()
        old = current.parent / "archive" / "CA-R-501@4-old.md"
        legacy = current.parent / "archive" / "CA-R-501-legacy.md"
        unrelated = current.parent / "archive" / "CA-R-900@7-other.md"
        write_atom(current, "CA-R-501", version=5)
        write_atom(old, "CA-R-501", status="Archived", version=4)
        write_atom(legacy, "CA-R-501", status="Archived", version=3)
        write_atom(unrelated, "CA-R-900", status="Archived", version=7)
        self.service._refresh()
        def query(sql):
            with self.service._store._lock:
                return self.service._store._connection.execute(sql).fetchall()
        self.assertIn(("CA-R-501", "4", True), query("SELECT * FROM main.archive_version_max"))
        result = self.store.run("SELECT atom_id, max_version FROM archive_version_max WHERE atom_id = 'CA-R-501'")
        self.assertEqual([["CA-R-501", "4"]], result["rows"])
        self.assertNotIn("CA-R-900", {row[0] for row in query("SELECT * FROM main.archive_version_max")})
        self.assertEqual("900", query("SELECT max_id_number FROM main.archive_role_max WHERE role_marker = 'R'")[0][0])
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_latest_version(selection, "CA-R-501")
        moved = old.with_name("CA-R-501@6-moved.md")
        old.rename(moved)
        write_atom(moved, "CA-R-501", status="Archived", version=6)
        self.service._refresh([{"operation": "move", "old_path": old.relative_to(self.root.resolve()).as_posix(), "new_path": moved.relative_to(self.root.resolve()).as_posix()}])
        self.assertIn(("CA-R-501", "6", True), query("SELECT * FROM main.archive_version_max"))
        legacy.unlink()
        self.service._refresh([{"operation": "remove", "old_path": legacy.relative_to(self.root.resolve()).as_posix(), "new_path": None}])
        self.assertEqual(6, self.service.lifecycle_latest_version(selection, "CA-R-501"))
        unrelated.unlink()
        self.service._refresh([{"operation": "remove", "old_path": unrelated.relative_to(self.root.resolve()).as_posix(), "new_path": None}])
        self.assertEqual("501", query("SELECT max_id_number FROM main.archive_role_max WHERE role_marker = 'R'")[0][0])
        current.unlink()
        self.service._refresh([{"operation": "remove", "old_path": current.relative_to(self.root.resolve()).as_posix(), "new_path": None}])
        self.assertNotIn("CA-R-501", {row[0] for row in query("SELECT * FROM main.archive_version_max")})
        self.service._refresh()
        self.assertEqual("501", query("SELECT max_id_number FROM main.archive_role_max WHERE role_marker = 'R'")[0][0])

    def test_legacy_zero_padded_version_does_not_stop_filename_inventory(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-504.md").resolve()
        archive = current.parent / "archive" / "CA-R-504@02-old.md"
        write_atom(current, "CA-R-504", version=3)
        write_atom(archive, "CA-R-504", status="Archived", version=2)
        self.service._refresh()
        result = self.store.run("SELECT max_version, has_unknown_version FROM archive_version_max WHERE atom_id = 'CA-R-504'")
        self.assertEqual([[None, True]], result["rows"])

    def test_archive_summary_and_projection_publish_under_one_lock(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-503.md").resolve()
        archived = current.parent / "archive" / "CA-R-503@2-old.md"
        write_atom(current, "CA-R-503", version=3)
        write_atom(archived, "CA-R-503", status="Archived", version=2)
        entered, release, queried = threading.Event(), threading.Event(), threading.Event()
        original = self.service._reader._catalog.refresh_summaries
        def pause_summary(ids):
            original(ids)
            entered.set()
            if not release.wait(5):
                raise TimeoutError("publication test timed out")
        def run_query():
            self.store.run("SELECT count(*) FROM archive_version_max")
            queried.set()
        with patch.object(self.service._reader._catalog, "refresh_summaries", side_effect=pause_summary):
            refresh = threading.Thread(target=self.service._refresh)
            refresh.start()
            try:
                self.assertTrue(entered.wait(5))
                query = threading.Thread(target=run_query)
                query.start()
                self.assertFalse(queried.wait(0.1))
            finally:
                release.set()
                refresh.join(5)
            query.join(5)
            self.assertTrue(queried.is_set())

    def test_loaded_archive_version_uses_body_instead_of_filename(self):
        current = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-502.md").resolve()
        archived = current.parent / "archive" / "CA-R-502@11-old.md"
        legacy = current.parent / "archive" / "CA-R-502-legacy.md"
        write_atom(current, "CA-R-502", version=5)
        write_atom(archived, "CA-R-502", status="Archived", version=3)
        write_atom(legacy, "CA-R-502", status="Archived", version=4)
        self.service._refresh()
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_latest_version(selection, "CA-R-502")
        self.service.load_archives([{"scope_unit": "ENGINE", "role": "Requirement"}])
        self.assertEqual(5, self.service.lifecycle_latest_version(selection, "CA-R-502"))

    def test_relation_read_flushes_own_changes_as_one_batch(self):
        path = source_path(self.declarations, "ENGINE", "04_requirement", "CA-R-101.md").resolve()
        descendant = source_path(self.declarations, "ENGINE", "04_requirement", "B.md")
        write_atom(path, "CA-R-101", relations="{BLOCKS: 'CA-R-B'}")
        write_atom(descendant, "CA-R-B", relations="{BLOCKS: 'CA-R-C'}")
        self.service.lifecycle_changed(None, path.resolve())
        self.service.lifecycle_changed(None, descendant.resolve())
        with patch.object(self.service, "_refresh", wraps=self.service._refresh) as refresh:
            expected = {"CA-R-101", "CA-R-B", "CA-R-C"}
            self.assertEqual(expected, self.service.lifecycle_descendants(("CA-R-101",), "BLOCKS"))
            self.assertEqual(expected, self.service.lifecycle_descendants(("CA-R-101",), "BLOCKS"))
            self.assertEqual(set(), self.service.lifecycle_descendants(("CA-R-999",), "BLOCKS"))
            self.assertEqual(1, refresh.call_count)

    def test_one_loaded_version_does_not_hide_another_unloaded_version(self):
        atom_id = "CA-R-101"
        first = source_path(self.declarations, "ENGINE", "04_requirement", f"archive/{atom_id}@1-first.md")
        second = self.service._reader.control_root / "04_requirement" / "archive" / f"{atom_id}@2-second.md"
        write_atom(first, atom_id, status="Archived", version=1)
        write_atom(second, atom_id, status="Archived", version=2)
        self.service._refresh()
        self.service.load_archives([{"scope_unit": "ENGINE", "role": "Requirement"}])
        selection = SimpleNamespace(root=self.root.resolve(), control_root=self.service._reader.control_root)
        with self.assertRaises(ArchiveNotLoadedError):
            self.service.lifecycle_candidates(selection, atom_ids=(atom_id,), references=(f"{atom_id}@1", f"{atom_id}@2"))
