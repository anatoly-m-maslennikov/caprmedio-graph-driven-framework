import os
from pathlib import Path
import unittest
from unittest.mock import patch
import sys

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_lifecycle_state_actions as fixtures  # noqa: E402
from ATOM_LIFECYCLE.common import InputError  # noqa: E402
from ATOM_LIFECYCLE.plan_cascade import select_archive_cascade  # noqa: E402
from ATOM_LIFECYCLE.source import bind_query_reader, select_source  # noqa: E402
from test_lifecycle_source import IndexedReader  # noqa: E402


class PlanCascadeTest(unittest.TestCase):
    setUp = fixtures.StateActionsTest.setUp
    _contained = fixtures.StateActionsTest._contained

    def test_child_first_and_assets(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task', 'Done')
        (group / 'notes.md').write_text('Asset')
        child_group = child.with_suffix('')
        child_group.mkdir()
        grandchild = child_group / '3-CA-P-22-TASK--grandchild.md'
        grandchild.write_text(child.read_text().replace('CA-P-21', 'CA-P-22').replace('CA-P-20', 'CA-P-21').replace('status: Done', 'status: Active'))
        pins = select_archive_cascade(self.selection, select_source(self.selection, 'CA-P-20'), self.model)
        self.assertEqual([pin.atom_id for pin in pins], ['CA-P-22', 'CA-P-21', 'CA-P-20'])

    def test_query_backed_containment_does_not_scan_the_carrier_tree(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task', 'Done')
        parent = group.with_suffix('.md')
        indexed = IndexedReader(self.selection, [('CA-P-20', parent), ('CA-P-21', child)])
        indexed.lifecycle_descendants = lambda refs, relation: {'CA-P-20', 'CA-P-21'}
        with bind_query_reader(indexed), \
             patch('ATOM_LIFECYCLE.source._inventory_paths', side_effect=AssertionError('unexpected scan')), \
             patch('ATOM_LIFECYCLE.plan_cascade.os.walk', side_effect=AssertionError('unexpected walk')):
            pins = select_archive_cascade(self.selection, select_source(self.selection, 'CA-P-20'), self.model)
        self.assertEqual([pin.atom_id for pin in pins], ['CA-P-21', 'CA-P-20'])

    def test_mismatched_containment_rejected(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task')
        parent = select_source(self.selection, 'CA-P-20')
        child.write_text(child.read_text().replace('atom: CA-P-20', 'atom: CA-P-99'))
        with self.assertRaises(InputError):
            select_archive_cascade(self.selection, parent, self.model)

    def test_unsafe_asset_and_scan_error_fail_preflight(self):
        group, _, _ = self._contained('Plan', 'Epic', 'Task')
        parent = select_source(self.selection, 'CA-P-20')
        fifo = group / 'pipe'
        os.mkfifo(fifo)
        with self.assertRaises(InputError):
            select_archive_cascade(self.selection, parent, self.model)
        fifo.unlink()
        with patch('ATOM_LIFECYCLE.plan_cascade.os.walk', side_effect=OSError('unreadable')):
            with self.assertRaises(InputError):
                select_archive_cascade(self.selection, parent, self.model)

    def test_operations_workflow_step_substep_and_status_placement(self):
        group, child, _ = self._contained('Operations', 'Workflow', 'Step')
        folder = group / 'resolved'
        folder.mkdir()
        moved = folder / child.name
        child.write_text(child.read_text().replace('status: Active', 'status: Resolved'))
        child.rename(moved)
        child = moved
        child_group = child.with_suffix('')
        child_group.mkdir()
        grandchild = child_group / 'CA-O-22-SUBSTEP--grandchild.md'
        grandchild.write_text(child.read_text().replace('CA-O-21', 'CA-O-22').replace('CA-O-20', 'CA-O-21').replace('form: Step', 'form: Substep').replace('status: Resolved', 'status: Active'))
        parent = select_source(self.selection, 'CA-O-20')
        pins = select_archive_cascade(self.selection, parent, self.model)
        self.assertEqual([pin.atom_id for pin in pins], ['CA-O-22', 'CA-O-21', 'CA-O-20'])
        grandchild.write_text(grandchild.read_text().replace('form: Substep', 'form: Workflow'))
        with self.assertRaises(InputError):
            select_archive_cascade(self.selection, parent, self.model)

    def test_operations_rejects_malformed_history_and_wrong_placement(self):
        group, child, _ = self._contained('Operations', 'Workflow', 'Step')
        parent = select_source(self.selection, 'CA-O-20')
        history = group / 'CA-O-21@1-STEP--old.md'
        history.write_text('retained')
        with self.assertRaises(InputError):
            select_archive_cascade(self.selection, parent, self.model)
        history.unlink()
        child.write_text(child.read_text().replace('status: Active', 'status: Resolved'))
        with self.assertRaises(InputError):
            select_archive_cascade(self.selection, parent, self.model)
