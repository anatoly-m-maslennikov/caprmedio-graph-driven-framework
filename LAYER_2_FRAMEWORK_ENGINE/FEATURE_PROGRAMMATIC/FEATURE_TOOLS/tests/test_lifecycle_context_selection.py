"""Indexed context checks never read the containing Atom Carrier."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from ATOM_LIFECYCLE.carrier import render_carrier  # noqa: E402
from ATOM_LIFECYCLE.common import InputError  # noqa: E402
from ATOM_LIFECYCLE.placement import resolve_container  # noqa: E402
from ATOM_LIFECYCLE.source import (ArchiveNotLoadedError, SourceSelectionError, bind_query_reader, select_context)  # noqa: E402
from ATOM_LIFECYCLE.status_model import StatusModel  # noqa: E402
from ATOM_LIFECYCLE.validation import validate_candidate  # noqa: E402
import test_lifecycle_source as source_fixture  # noqa: E402


class ContextReader:
    def __init__(self, declarations):
        self.declarations = declarations
        self.rows = {}
        self.calls = []

    def lifecycle_contexts(self, selection, ref_id):
        self.calls.append(ref_id)
        return self.rows.get(ref_id, [])

    def lifecycle_declarations(self):
        return self.declarations

    def lifecycle_read(self, path):
        raise AssertionError(f'Context attempted a Carrier byte read: {path}')


class ContextSelectionTests(unittest.TestCase):
    def setUp(self):
        from scope_unit_declarations import read_scope_unit_declarations
        self.fixture = source_fixture.SourceTest()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.selection
        declarations = read_scope_unit_declarations(self.selection.root, self.selection.control_relative)
        self.reader = ContextReader(declarations)
        self.plan_root = self.selection.control_root / '03_plan'
        self.plan_root.mkdir(exist_ok=True)

    def add_plan(self, atom_id, path, container, *, status='Active', summary='Same work'):
        metadata = {'atom_id': atom_id, 'ref_id': atom_id, 'version': 1, 'status': status,
                    'role': 'Plan', 'form': 'Plan', 'container': container}
        self.reader.rows[atom_id] = [(path, metadata, summary)]
        return metadata

    def test_nested_container_and_ancestor_checks_use_only_indexed_context(self):
        top = self.plan_root / 'CA-P-10-PLAN--top.md'
        top_dir = top.with_suffix('')
        top_dir.mkdir()
        child = top_dir / 'CA-P-11-PLAN--child.md'
        child.with_suffix('').mkdir()
        self.add_plan('CA-P-10', top, {'scope_unit': 'TEST'})
        child_metadata = self.add_plan('CA-P-11', child, {'atom': 'CA-P-10'})
        model = StatusModel(((None, None, 'Active'), (None, None, 'Done')))
        view = {'role': 'Plan', 'form': 'Plan', 'container': {'atom': 'CA-P-11'}}
        fields = {'atom_id': 'CA-P-12', 'ref_id': 'CA-P-12', 'role': 'Plan', 'form': 'Plan',
                  'status': 'Active', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.atom': 'CA-P-11'}
        with bind_query_reader(self.reader):
            scope, parent = resolve_container(self.selection, view, 'CA-P-12', model=model)
            self.assertEqual(('TEST', child.with_suffix('')), (scope, parent.path))
            validate_candidate(self.selection, model, render_carrier(None, fields, body='## Summary\n\nChild\n'),
                               child.with_suffix('') / 'CA-P-12.md')
            child_metadata['status'] = 'Done'
            with self.assertRaisesRegex(InputError, 'inside a Done or Canceled Plan'):
                validate_candidate(self.selection, model, render_carrier(None, fields, body='## Summary\n\nChild\n'),
                                   child.with_suffix('') / 'CA-P-12.md')
        self.assertIn('CA-P-10', self.reader.calls)
        self.assertIn('CA-P-11', self.reader.calls)

    def test_work_report_uses_indexed_summary_and_container(self):
        target = self.plan_root / 'done/CA-P-30-PLAN--same-work.md'
        self.add_plan('CA-P-30', target, {'scope_unit': 'TEST'}, status='Done', summary='Same work')
        fields = {'atom_id': 'CA-P-31', 'ref_id': 'CA-P-31', 'role': 'Plan', 'form': 'Work Report',
                  'status': 'Done', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.scope_unit': 'TEST', 'relations': {'IS_WORK_REPORT_FOR': ['CA-P-30']}}
        model = StatusModel(((None, None, 'Done'),))
        with bind_query_reader(self.reader):
            validate_candidate(self.selection, model, render_carrier(None, fields, body='## Summary\n\nSame work\n'),
                               self.plan_root / 'done/CA-P-31.md')
            with self.assertRaisesRegex(InputError, 'same Summary'):
                validate_candidate(self.selection, model, render_carrier(None, fields, body='## Summary\n\nOther work\n'),
                                   self.plan_root / 'done/CA-P-31.md')
            self.reader.rows['CA-P-30'][0] = (target, self.reader.rows['CA-P-30'][0][1], None)
            with self.assertRaisesRegex(InputError, 'Exactly one Summary'):
                validate_candidate(self.selection, model, render_carrier(None, fields, body='## Summary\n\nSame work\n'),
                                   self.plan_root / 'done/CA-P-31.md')

    def test_missing_or_invalid_context_fails_without_fallback(self):
        path = self.plan_root / 'CA-P-30-PLAN--same-work.md'
        metadata = self.add_plan('CA-P-30', path, {'scope_unit': 'TEST'})
        with bind_query_reader(self.reader), patch('ATOM_LIFECYCLE.source.select_source',
                                                   side_effect=AssertionError('unexpected fallback')):
            self.assertEqual(path, select_context(self.selection, 'CA-P-30', expected_version=1).path)
            projected = self.plan_root / '_projection/CA-P-30-PLAN--copy.md'
            self.reader.rows['CA-P-30'] = [(projected, metadata | {'projection': {}}, 'Copy'),
                                           (path, metadata, 'Same work')]
            self.assertEqual(path, select_context(self.selection, 'CA-P-30').path)
            self.reader.rows['CA-P-30'] = [(path, metadata, 'Same work')]
            with self.assertRaises(SourceSelectionError):
                select_context(self.selection, 'CA-P-30', expected_version=2)
            metadata['ref_id'] = 'CA-P-31'
            with self.assertRaises(SourceSelectionError):
                select_context(self.selection, 'CA-P-30')
            metadata['ref_id'] = 'CA-P-30'
            for status in ('Draft', 'Archived'):
                metadata['status'] = status
                with self.subTest(status=status), self.assertRaises(SourceSelectionError):
                    select_context(self.selection, 'CA-P-30')
            metadata['status'] = 'Done'
            self.reader.rows['CA-P-30'] = [(self.selection.root / 'elsewhere/CA-P-30.md', metadata, 'Same work')]
            with self.assertRaises(SourceSelectionError):
                select_context(self.selection, 'CA-P-30')
            with patch.object(self.reader, 'lifecycle_contexts', side_effect=ArchiveNotLoadedError('load archive')):
                with self.assertRaises(ArchiveNotLoadedError):
                    select_context(self.selection, 'CA-P-30')

    def test_competing_current_contexts_fail_even_with_expected_version(self):
        first = self.plan_root / 'CA-P-30-first.md'
        second = self.plan_root / 'CA-P-30-second.md'
        metadata = self.add_plan('CA-P-30', first, {'scope_unit': 'TEST'})
        self.reader.rows['CA-P-30'].append((second, metadata | {'version': 2}, 'Other'))
        with bind_query_reader(self.reader):
            for version in (None, 1, 2):
                with self.subTest(version=version), self.assertRaisesRegex(SourceSelectionError, 'ambiguous'):
                    select_context(self.selection, 'CA-P-30', expected_version=version)
            self.reader.rows['CA-P-30'] = [(first, metadata, 'Same work')] * 2
            self.assertEqual(first, select_context(self.selection, 'CA-P-30').path)

    def test_real_workbench_context_serves_plan_without_carrier_byte_reads(self):
        from watchdog.observers.polling import PollingObserver
        from project_selection import bind_selection
        app = TOOLS.parent / 'FEATURE_APPS'
        sys.path[:0] = [str(app), str(app / 'APP_WORKBENCH/tests')]
        from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService
        from smalltest_support import built_assets, extension_directory

        model = self.fixture.folder / 'CA-R-700-DECLARATION--summary.md'
        model.write_text('---\natom_id: CA-R-700\nrole: Requirement\nform: Declaration\n'
                         'status: Active\nversion: 1\n---\n## Claim\n\n### Formal Claim\n\n'
                         '```CFEL\nAtom.Content.Summary:: {::1};\n```\n')
        target = self.plan_root / 'done/CA-P-30-PLAN--same-work.md'
        target.parent.mkdir()
        fields = {'atom_id': 'CA-P-30', 'ref_id': 'CA-P-30', 'role': 'Plan', 'form': 'Plan',
                  'status': 'Done', 'version': 1, 'updated_at': '2026-01-01T00:00:00+00:00',
                  'container.scope_unit': 'TEST'}
        target.write_bytes(render_carrier(None, fields, body='## Summary\n\nSame work\n'))
        observer = patch('APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher.NativeObserver', PollingObserver)
        observer.start()
        self.addCleanup(observer.stop)
        with bind_selection(self.selection):
            service = WorkbenchService(self.selection.root, extension_directory=extension_directory(TOOLS.parents[2]),
                                       **built_assets(self.selection.root))
            self.addCleanup(service.close)
            service.run('SELECT 1', result_delivery='inline')
            with bind_query_reader(service), patch.object(service, 'lifecycle_read',
                                                           side_effect=AssertionError('unexpected byte read')):
                context = select_context(self.selection, 'CA-P-30')
                self.assertEqual((target, 'Done', 'Same work'), (context.path, context.status, context.summary))
