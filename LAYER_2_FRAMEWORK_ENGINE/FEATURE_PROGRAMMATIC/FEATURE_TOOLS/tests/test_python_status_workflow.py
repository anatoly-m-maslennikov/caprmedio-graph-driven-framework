# CA-E-825
"""Exercise the Python Status Workflow through the lifecycle backend."""
from dataclasses import replace
from datetime import datetime, timedelta
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.append(str(TOOLS))

from ATOM_LIFECYCLE import backend, effects, state_actions, status_cascade, validation  # noqa: E402
from ATOM_LIFECYCLE import status_workflow_definition as definitions  # noqa: E402
from ATOM_LIFECYCLE.assets.change_current_status import SOURCE_SHA256  # noqa: E402
from ATOM_LIFECYCLE.placement_model import bind_placement  # noqa: E402
from ATOM_LIFECYCLE.source import bind_query_reader, select_source  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
from lifecycle_placement_test_support import fixture_rules  # noqa: E402
import test_lifecycle_shared_backlog  # noqa: E402
from test_lifecycle_source import IndexedReader  # noqa: E402
import test_lifecycle_state_actions  # noqa: E402


ROUTE = 'atom_lifecycle_change_status'
BINDING = {'workflow': 'CA-O-10011@4', 'step': 'CA-O-10010@1', 'action': 'CA-O-10007@1'}
PLAN_TARGET = {'ref_id': 'CA-P-20', 'version': 1}
PLAN_IDS = ('CA-P-20', 'CA-P-21', 'CA-P-22')
UPDATED = '2026-01-01T00:00:00+00:00'


class PythonStatusWorkflowTest(unittest.TestCase):
    _contained = test_lifecycle_state_actions.StateActionsTest._contained
    tree = test_lifecycle_shared_backlog.SharedBacklogAcceptance.tree

    def setUp(self):
        test_lifecycle_state_actions.StateActionsTest.setUp(self)
        rules = fixture_rules()
        self.backlog_folder = rules.placement('Plan', 'Backlog')[1]
        rules = replace(rules, _placements={**rules._placements,
                                          ('plan', 'backlog'): ('role', self.backlog_folder)})
        role_form = SimpleNamespace(decode=lambda field, value: value, encode=lambda field, value: value)
        self.model = replace(self.model, _rows=self.model._rows + ((None, None, 'Backlog'),
                             (None, None, 'Done'), (None, None, 'Canceled')),
                             candidate_schema=SimpleNamespace(placement=rules, role_form=role_form))
        self.enterContext(bind_placement(rules))
        self.enterContext(patch.object(state_actions, 'validate_candidate', validation.validate_candidate))
        self.enterContext(patch.object(validation, '_validate_declared_schema'))
        self._add_timestamp(self.path)

    def _add_timestamp(self, path):
        path.write_text(path.read_text().replace('updated_at: 2026-01-01\n', f'updated_at: {UPDATED}\n'))

    def _backlog_tree(self):
        child, nested, _, _ = self.tree()
        parent = self.role_root / '1-CA-P-20-EPIC--parent.md'
        parent.write_text(parent.read_text().replace('status: Active', 'status: Backlog'))
        parent = parent.rename(self.role_root / self.backlog_folder / parent.name)
        parent_group = parent.with_suffix('')
        parent_group.mkdir()
        child.with_suffix('').rename(parent_group / child.stem)
        child = child.rename(parent_group / child.name)
        nested = child.with_suffix('') / nested.name
        for path in (parent, child, nested):
            self._add_timestamp(path)
        draft = self.role_root / 'draft/2-CA-P-26@1-draft-TASK--draft.md'
        draft.parent.mkdir()
        draft.write_text(child.read_text().replace('atom_id: CA-P-21', 'atom_id: CA-P-26')
                         .replace('ref_id: CA-P-21', 'ref_id: CA-P-26@1-draft')
                         .replace('status: Backlog', 'status: Draft').replace('version: 2', 'version: 1')
                         .replace('\nChild\n', '\nDraft\n'))
        return parent, child, nested, draft

    def _indexed(self, paths):
        indexed = IndexedReader(self.selection, list(zip((*PLAN_IDS, 'CA-P-26'), paths, strict=True)))
        children = {'CA-P-20': {*PLAN_IDS, 'CA-P-26@1-draft'}, 'CA-P-21': set(PLAN_IDS[1:]),
                    'CA-P-22': {'CA-P-22'}}
        indexed.lifecycle_descendants = lambda seeds, relation: set().union(*(children[seed] for seed in seeds))

        def changed(old, new):
            indexed.rows = [(identity, path) for identity, path in indexed.rows if path not in (old, new)]
            if new is not None:
                indexed.rows.extend((identity, new) for identity in PLAN_IDS if f'{identity}-' in new.name)

        indexed.lifecycle_changed = changed
        return indexed

    def _run_status(self, target, status):
        return backend.execute(self.selection, self.model, ROUTE, {'target': target, 'targetStatus': status})

    def _pins(self):
        return tuple(select_source(self.selection, identity) for identity in PLAN_IDS)

    @property
    def _journal(self):
        return self.selection.control_root / '_journal'

    def _journal_rows(self):
        return [json.loads(line) for path in sorted(self._journal.glob('atom-lifecycle-*.ndjson'))
                for line in path.read_text().splitlines()]

    def _assert_journal(self, outcome, events, *, rows=None):
        if rows is None:
            rows = self._journal_rows()
        self.assertEqual(list(events), [row['event'] for row in rows])
        self.assertTrue(outcome['workflow_run_id'])
        for row in rows:
            self.assertEqual(outcome['workflow_run_id'], row['workflow_run_id'])
            self.assertEqual(BINDING, row['workflow_binding'])
            self.assertEqual(SOURCE_SHA256, row['source_sha256'])
            self.assertEqual(timedelta(0), datetime.fromisoformat(row['occurred_at']).utcoffset())
        steps = [row for row in rows if row['event'].startswith('step_')]
        ids = [row['step_run_id'] for row in steps]
        self.assertTrue(all(ids))
        self.assertEqual(len(ids), len(set(ids)))
        for observed, applied in zip(steps, outcome['action_results'], strict=True):
            for field in ('step_run_id', 'step', 'action', 'target', 'effects'):
                self.assertEqual(applied[field], observed[field], field)
            self.assertEqual([{key: error[key] for key in ('code', 'field') if key in error}
                              for error in applied['errors']], observed['errors'])

    def _definition_fixture(self):
        code_root = Path(definitions.__file__).resolve().parents[4]
        sources = definitions._installed_model(code_root)
        self.assertIsNotNone(sources)
        install = self.root / 'fixture-engine'
        fixture_sources = install / 'METHODOLOGY/sources'
        paths = {}
        for form, _, _, relative in definitions.SOURCES:
            destination = fixture_sources / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes((sources / relative).read_bytes())
            paths[form] = destination
        snapshot = install / definitions.SNAPSHOT.relative_to(code_root)
        snapshot.parent.mkdir(parents=True)
        snapshot.write_bytes(definitions.SNAPSHOT.read_bytes())
        self.enterContext(patch.object(status_cascade, 'bind_definition_check',
                                      side_effect=lambda: definitions._bind_definition_check(install)))
        return paths

    def test_activate_backlog_tree_with_attached_draft(self):
        paths = self._backlog_tree()
        draft_bytes = paths[-1].read_bytes()
        with bind_query_reader(self._indexed(paths)):
            outcome = self._run_status(PLAN_TARGET, 'Active')
        self.assertEqual('completed', outcome['outcome'], outcome)
        self.assertEqual(BINDING, outcome['workflow_binding'])
        self.assertEqual(list(PLAN_IDS), [entry['artifact']['ref_id'] for entry in outcome['action_results']])
        parent, child, nested = self._pins()
        self.assertEqual([(ref, version, 'active') for ref, version in zip(PLAN_IDS, (1, 2, 2), strict=True)],
                         [(pin.ref_id, pin.version, pin.status.casefold()) for pin in (parent, child, nested)])
        self.assertEqual((self.role_root, parent.path.with_suffix(''), child.path.with_suffix('')),
                         tuple(pin.path.parent for pin in (parent, child, nested)))
        self.assertEqual([UPDATED] * 3, [carrier_read_view(pin.metadata)['updated_at'].isoformat()
                                        for pin in (parent, child, nested)])
        self.assertEqual(str(parent.path.relative_to(self.root)), outcome['artifact']['path'])
        writes = [(effect['operation'], Path(effect['target']).name) for effect in outcome['effects']]
        order = [writes.index((op, pin.path.name)) for op, pin in zip(('create', 'modify', 'modify'),
                                                                     (parent, child, nested), strict=True)]
        self.assertEqual(sorted(order), order)
        self.assertEqual(draft_bytes, paths[-1].read_bytes())
        self._assert_journal(outcome, ('workflow_started', 'step_completed', 'step_completed',
                                       'step_completed', 'workflow_completed'))

    def test_single_atom_returns_saved_reference_and_effects(self):
        outcome = self._run_status(self.target, 'Resolved')
        self.assertEqual('completed', outcome['outcome'], outcome)
        self.assertEqual(BINDING, outcome['workflow_binding'])
        artifact = outcome['artifact']
        self.assertEqual(('CA-R-10', 2, 'Resolved'), (artifact['ref_id'], artifact['version'], artifact['status']))
        self.assertEqual(self.path.parent / 'resolved' / self.path.name, self.root / artifact['path'])
        self.assertTrue(outcome['effects'])
        self.assertTrue(all(effect['state'] == 'known' for effect in outcome['effects']))
        events = ('workflow_started', 'step_completed', 'workflow_completed')
        self._assert_journal(outcome, events)
        subsequent = self._run_status(self.target, 'Active')
        rows = self._journal_rows()
        self.assertEqual(6, len(rows))
        self._assert_journal(subsequent, events, rows=rows[3:])
        self.assertNotEqual(outcome['workflow_run_id'], subsequent['workflow_run_id'])
        self.assertNotEqual(rows[1]['step_run_id'], rows[4]['step_run_id'])

    def test_invalid_invocation_identifies_fields_before_effects(self):
        before = self.path.read_bytes()
        cases = (({'target': {'ref_id': 'CA-R-10', 'version': True}, 'targetStatus': 'Resolved'}, {'target'}),
                 ({'target': self.target, 'targetStatus': 'Not a Status'}, {'targetStatus'}),
                 ({'targetStatus': 'Draft', 'extra': True}, {'extra', 'target', 'targetStatus'}))
        for arguments, fields in cases:
            with self.subTest(fields=fields):
                outcome = backend.execute(self.selection, self.model, ROUTE, arguments)
                self.assertEqual('needs_input', outcome['outcome'], outcome)
                self.assertEqual(fields, set(outcome['requested_input']))
                self.assertEqual([], outcome['effects'])
                self.assertEqual(before, self.path.read_bytes())
                self.assertEqual([], self._journal_rows())

    def _fail_readback(self, atom_id, status):
        read = effects._read

        def fail_after_write(parent, name):
            data = read(parent, name)
            if atom_id in name and f'\nstatus: {status}\n'.encode() in data:
                raise OSError('injected readback failure after the write')
            return data

        return patch.object(effects, '_read', side_effect=fail_after_write)

    def test_partial_failure_preserves_effects_and_reports_unrun_action(self):
        self._backlog_tree()
        with self._fail_readback('CA-P-21', 'active'):
            outcome = self._run_status(PLAN_TARGET, 'Active')
        self.assertEqual('failed', outcome['outcome'], outcome)
        self.assertEqual(BINDING, outcome['workflow_binding'])
        self.assertEqual('effect_uncertain', outcome['errors'][0]['code'])
        self.assertEqual({'known', 'unknown'}, {effect['state'] for effect in outcome['effects']})
        self.assertEqual('CA-P-20', outcome['action_results'][0]['artifact']['ref_id'])
        self.assertEqual({'step': BINDING['step'], 'action': BINDING['action'],
                          'target': {'ref_id': 'CA-P-21', 'version': 2, 'target_status': 'Active'}},
                         outcome['failed_action'])
        self.assertEqual(['CA-P-22'], [item['target']['ref_id'] for item in outcome['unrun_actions']])
        self.assertEqual(['CA-P-21', 'CA-P-22'], [item['ref_id'] for item in outcome['remaining_targets']])
        self.assertEqual(['active', 'active', 'backlog'], [pin.status.casefold() for pin in self._pins()])
        self._assert_journal(outcome, ('workflow_started', 'step_completed', 'step_failed', 'workflow_failed'))

    def test_failure_with_no_selected_next_action(self):
        with self._fail_readback('CA-R-10', 'resolved'):
            outcome = self._run_status(self.target, 'Resolved')
        self.assertEqual('failed', outcome['outcome'], outcome)
        self.assertEqual('CA-R-10', outcome['failed_action']['target']['ref_id'])
        self.assertEqual([], outcome['unrun_actions'])
        self.assertIn('unknown', [effect['state'] for effect in outcome['effects']])

    def test_changed_withdrawn_and_unavailable_definitions_block_first_action(self):
        definitions = self._definition_fixture()
        before = self.path.read_bytes()
        for form, fault in (('workflow', 'changed'), ('step', 'withdrawn'), ('action', 'unavailable')):
            with self.subTest(fault=fault), patch.object(status_cascade, '_apply') as apply:
                source = definitions[form]
                raw = source.read_bytes()
                self.addCleanup(source.write_bytes, raw)
                if fault == 'unavailable':
                    source.unlink()
                elif fault == 'withdrawn':
                    withdrawn = raw.replace(b'  status: Active\n', b'  status: Archived\n')
                    self.assertNotEqual(raw, withdrawn)
                    source.write_bytes(withdrawn)
                else:
                    source.write_bytes(raw + b'\nChanged source.\n')
                outcome = self._run_status(self.target, 'Resolved')
                source.write_bytes(raw)
                self.assertEqual('blocked', outcome['outcome'], outcome)
                self.assertEqual('definition_revalidation_required', outcome['errors'][0]['code'])
                self.assertIn(BINDING[form], outcome['errors'][0]['message'])
                self.assertEqual(([], []), (outcome['effects'], outcome['action_results']))
                self.assertEqual(['CA-R-10'], [item['target']['ref_id'] for item in outcome['unrun_actions']])
                self.assertNotIn('failed_action', outcome)
                self.assertNotIn('workflow_run_id', outcome)
                self.assertEqual(before, self.path.read_bytes())
                self.assertEqual([], self._journal_rows())
                apply.assert_not_called()

    def test_definition_changed_between_actions_preserves_committed_effects(self):
        source = self._definition_fixture()['action']
        self._backlog_tree()
        apply = status_cascade._apply

        def change_definition(*args, **kwargs):
            outcome = apply(*args, **kwargs)
            source.write_bytes(source.read_bytes() + b'\nChanged during Action.\n')
            return outcome

        with patch.object(status_cascade, '_apply', side_effect=change_definition) as dispatch:
            outcome = self._run_status(PLAN_TARGET, 'Active')
        self.assertEqual('blocked', outcome['outcome'], outcome)
        self.assertEqual('definition_revalidation_required', outcome['errors'][0]['code'])
        dispatch.assert_called_once()
        self.assertEqual(['active', 'backlog', 'backlog'], [pin.status.casefold() for pin in self._pins()])
        self.assertTrue(outcome['effects'])
        self.assertEqual({'known'}, {effect['state'] for effect in outcome['effects']})
        self.assertEqual('CA-P-20', outcome['action_results'][0]['artifact']['ref_id'])
        self.assertEqual(list(PLAN_IDS[1:]), [item['target']['ref_id'] for item in outcome['unrun_actions']])
        self.assertNotIn('failed_action', outcome)
        self._assert_journal(outcome, ('workflow_started', 'step_completed', 'workflow_blocked'))

    def test_journal_append_failure_is_only_a_warning(self):
        self._journal.write_text('A file prevents the Journal directory from opening.')
        outcome = self._run_status(self.target, 'Resolved')
        self.assertEqual('completed', outcome['outcome'], outcome)
        self.assertIn('journal_append_failed', {warning['code'] for warning in outcome['warnings']})
        self.assertTrue(outcome['effects'])
        self.assertEqual('resolved', select_source(self.selection, 'CA-R-10').status.casefold())
        self.assertTrue(self._journal.is_file())


if __name__ == '__main__':
    unittest.main()
