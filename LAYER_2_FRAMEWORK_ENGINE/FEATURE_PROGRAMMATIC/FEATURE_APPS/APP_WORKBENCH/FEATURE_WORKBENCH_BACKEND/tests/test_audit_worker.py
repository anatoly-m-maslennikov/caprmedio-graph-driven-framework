"""The background audit never publishes a stale source snapshot."""
from pathlib import Path
import sys
import threading
import time
from types import SimpleNamespace
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.audit_worker import AuditSnapshot, AuditWorker
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.audit_tables import TABLES


class Store:
    def __init__(self):
        self.published = []

    def audit_content_rows(self, paths):
        return {}

    def publish_audit(self, issues, paths, publication):
        with publication as current:
            if current:
                self.published.append((issues, paths))
            return current


class Snapshot:
    root = Path('/project')

    def __init__(self, label, paths, started=None, release=None):
        self.label = label
        self.source_paths = frozenset(self.root / p for p in paths)
        self.started, self.release = started, release

    def collect(self, rows, paths):
        if self.started:
            self.started.set()
            if not self.release.wait(5):
                raise TimeoutError('test audit not released')
        return {'atom_parse_issues': [(self.label, path) for path in sorted(paths)]}


class AuditWorkerTests(unittest.TestCase):
    def test_delta_snapshot_captures_only_selected_sources_and_parent_chain(self):
        root = Path('/project')
        child, parent, grandparent, unrelated = (root / name for name in ('child', 'parent', 'grandparent', 'unrelated'))
        rows = {
            child: {'header_json': {'container': {'atom': 'P'}}},
            parent: {'header_json': {'container': {'atom': 'G'}}, 'status_group': 'Current'},
            grandparent: {'header_json': {'container': {'scope_unit': 'SU'}}, 'status_group': 'Current'},
            unrelated: {'header_json': {}},
        }
        batches = []
        def paths_by_reference(refs):
            batches.append(set(refs))
            return {ref: {'P': {parent}, 'G': {grandparent}}.get(ref, set()) for ref in refs}
        reader = SimpleNamespace(
            root=root, control_root=root, _source_paths=set(rows),
            _cached={path: (None, row) for path, row in rows.items()}, _diagnostics={},
            _references=SimpleNamespace(
                paths_by_reference=paths_by_reference,
                accepted_paths=lambda paths: set(rows) & paths,
            ),
            _declarations=SimpleNamespace(as_structure=lambda: {'scope_units': []}, root=SimpleNamespace(name='SU')),
            _project_scope_id='SU', content_schema=None, _role_folders=None, _audit_model=None,
            _content_invalid=set(), _header_invalid=set(),
        )
        snapshot = AuditSnapshot.capture(reader, {'child', 'deleted'})
        self.assertEqual({child}, snapshot.source_paths)
        self.assertEqual({child, parent, grandparent}, set(snapshot.cached))
        self.assertEqual([{'P'}, {'G'}], batches)
        rows[parent]['status_group'] = 'Archived'
        self.assertEqual('Current', snapshot.current_row('P')['status_group'])
        self.assertEqual('Current', snapshot.current_row('G')['status_group'])

    def test_capture_paths_includes_inflight_delta(self):
        worker = AuditWorker(Store())
        started, release = threading.Event(), threading.Event()
        try:
            worker.invalidate()
            worker.submit(Snapshot('old', ['a'], started, release), {'a'})
            self.assertTrue(started.wait(2))
            worker.invalidate()
            self.assertEqual({'a', 'b'}, worker.capture_paths({'b'}))
            worker.submit(Snapshot('new', ['a', 'b']), {'b'})
            release.set()
            self.assertTrue(worker.wait(5))
        finally:
            release.set()
            worker.close()

    def test_failure_is_visible_and_later_submissions_do_not_raise(self):
        class FailingSnapshot(Snapshot):
            def collect(self, rows, paths):
                raise ValueError('broken declaration')

        worker = AuditWorker(Store())
        try:
            self.assertEqual({'audits_pending': False, 'last_audit_ms': None, 'audit_error': None}, worker.status())
            worker.invalidate()
            worker.submit(FailingSnapshot('bad', ['a']), {'a'})
            with self.assertRaisesRegex(RuntimeError, 'audit worker failed'):
                worker.wait(5)
            self.assertEqual({'audits_pending': False, 'last_audit_ms': None,
                              'audit_error': 'ValueError: broken declaration'}, worker.status())
            worker.invalidate()
            worker.submit(Snapshot('new', ['a']), {'a'})
            self.assertEqual('ValueError: broken declaration', worker.status()['audit_error'])
        finally:
            worker.close()

    def test_real_projection_matches_synchronous_audits(self):
        sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'tests'))
        from test_incremental_indexing import IncrementalIndexingTests
        fixture = IncrementalIndexingTests()
        fixture.setUp()
        worker = AuditWorker(fixture.store)
        try:
            before = {table: fixture.store.run(f'SELECT * FROM {table}')['rows'] for table in TABLES}
            worker.invalidate()
            worker.submit(AuditSnapshot.capture(fixture.service._reader), None)
            self.assertTrue(worker.wait(10))
            self.assertIsNotNone(worker.status()['last_audit_ms'])
            after = {table: fixture.store.run(f'SELECT * FROM {table}')['rows'] for table in TABLES}
            self.assertEqual(before, after)
        finally:
            worker.close()
            fixture.doCleanups()

    def test_full_finishes_once_then_coalesced_newer_deltas_publish(self):
        store = Store()
        worker = AuditWorker(store)
        started, release = threading.Event(), threading.Event()
        try:
            worker.invalidate()
            worker.submit(Snapshot('old', ['a'], started, release), None)
            self.assertTrue(started.wait(2))
            before = time.monotonic()
            worker.invalidate()
            worker.submit(Snapshot('new', ['a', 'b']), {'b'})
            worker.invalidate()
            worker.submit(Snapshot('latest', ['a', 'b', 'c']), {'c'})
            self.assertLess(time.monotonic() - before, 0.5)
            self.assertTrue(worker.status()['audits_pending'])
            release.set()
            self.assertTrue(worker.wait(5))
            self.assertEqual(2, len(store.published))
            issues, paths = store.published[0]
            self.assertIsNone(paths)
            self.assertEqual([('old', 'a')], issues['atom_parse_issues'])
            issues, paths = store.published[1]
            self.assertEqual({'b', 'c'}, paths)
            self.assertEqual([('latest', 'b'), ('latest', 'c')], issues['atom_parse_issues'])
            self.assertFalse(worker.status()['audits_pending'])
        finally:
            release.set()
            worker.close()

    def test_overlapping_deltas_are_combined_including_deleted_paths(self):
        store = Store()
        worker = AuditWorker(store)
        started, release = threading.Event(), threading.Event()
        try:
            worker.invalidate()
            worker.submit(Snapshot('old', ['a'], started, release), {'a'})
            self.assertTrue(started.wait(2))
            worker.invalidate()
            worker.submit(Snapshot('new', ['b']), {'b'})
            release.set()
            self.assertTrue(worker.wait(5))
            self.assertEqual({'a', 'b'}, store.published[0][1])
            self.assertEqual([('new', 'a'), ('new', 'b')], store.published[0][0]['atom_parse_issues'])
        finally:
            release.set()
            worker.close()

    def test_structural_change_queues_another_full_audit(self):
        store = Store()
        worker = AuditWorker(store)
        started, release = threading.Event(), threading.Event()
        try:
            worker.invalidate()
            worker.submit(Snapshot('old', ['a'], started, release), None)
            self.assertTrue(started.wait(2))
            worker.invalidate()
            worker.submit(Snapshot('new', ['a', 'b']), None)
            release.set()
            self.assertTrue(worker.wait(5))
            self.assertEqual([None, None], [paths for _, paths in store.published])
            self.assertEqual([('new', 'a'), ('new', 'b')], store.published[-1][0]['atom_parse_issues'])
        finally:
            release.set()
            worker.close()

    def test_invalidated_full_stays_pending_until_new_work_is_submitted(self):
        store = Store()
        worker = AuditWorker(store)
        started, release = threading.Event(), threading.Event()
        try:
            worker.invalidate()
            worker.submit(Snapshot('old', ['a'], started, release), None)
            self.assertTrue(started.wait(2))
            worker.invalidate()
            release.set()
            self.assertFalse(worker.wait(0.1))
            self.assertTrue(worker.status()['audits_pending'])
            worker.submit(Snapshot('new', ['a']), {'a'})
            self.assertTrue(worker.wait(5))
        finally:
            release.set()
            worker.close()

    def test_close_discards_inflight_results(self):
        store = Store()
        worker = AuditWorker(store)
        started, release = threading.Event(), threading.Event()
        worker.invalidate()
        worker.submit(Snapshot('old', ['a'], started, release), None)
        self.assertTrue(started.wait(2))
        closer = threading.Thread(target=worker.close)
        closer.start()
        release.set()
        closer.join(5)
        self.assertFalse(closer.is_alive())
        self.assertEqual([], store.published)


if __name__ == '__main__':
    unittest.main()
