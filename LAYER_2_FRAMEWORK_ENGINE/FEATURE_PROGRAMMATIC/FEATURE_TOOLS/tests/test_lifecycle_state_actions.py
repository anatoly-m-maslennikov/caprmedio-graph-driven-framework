from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import effects, state_actions, status_cascade  # noqa: E402
from ATOM_LIFECYCLE.plan_cascade import select_archive_cascade  # noqa: E402
from ATOM_LIFECYCLE.placement import derive_destination  # noqa: E402
from ATOM_LIFECYCLE.source import select_source  # noqa: E402
from ATOM_LIFECYCLE.common import InputError  # noqa: E402
from ATOM_LIFECYCLE.status_model import StatusModel  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from lifecycle_placement_test_support import bind_placement, fixture_rules  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402


class StateActionsTest(unittest.TestCase):
    def setUp(self):
        binding = bind_placement(fixture_rules())
        binding.__enter__()
        self.addCleanup(binding.__exit__, None, None, None)
        scratch = TOOLS.parents[2] / '.caprmedio_tmp/CA-P-2791/CA-P-2934/state-actions'
        scratch.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        control = self.root / '.caprmedio_test'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text('[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n[paths]\ncontrol_root=".caprmedio_test"\n')
        write_scope_unit_declarations(self.root, control_root=control, rows=[{'scope_unit_name': 'OTHER', 'atom_id': 'CA-R-990001', 'scope_unit_id': 'CA-SU-1'}])
        self.folder = control / '04_requirement'
        self.folder.mkdir(exist_ok=True)
        self.path = self.folder / 'CA-R-10-RULE--example.md'
        self.path.write_text('---\natom_id: CA-R-10\nref_id: CA-R-10\ncontainer:\n  scope_unit: TEST\nrole: Requirement\nform: Rule\nstatus: Active\nversion: 2\nupdated_at: 2026-01-01\n---\n## Summary\n\nExample\n\n## Claim\n\nOriginal\n')
        self.selection = resolve_project(self.root)
        self.model = StatusModel(((None, None, 'Active'), (None, None, 'Archived'),
                                  (None, None, 'Draft'), (None, None, 'Resolved')))
        self.target = {'ref_id': 'CA-R-10', 'version': 2}
        patcher = patch.object(state_actions, 'validate_candidate')
        patcher.start()
        self.addCleanup(patcher.stop)

    def read(self, artifact):
        path = self.root / artifact['path']
        carrier = parse_carrier(path.read_bytes(), path)
        return carrier_read_view(carrier.metadata), carrier.body

    def test_archive_preserves_version_timestamp_and_body(self):
        result = state_actions.archive_atom(self.selection, self.model, {'target': self.target})
        self.assertEqual(result['outcome'], 'completed')
        view, body = self.read(result['artifact'])
        self.assertEqual((view['ref_id'], view['version'], view['status']), ('CA-R-10@2', 2, 'archived'))
        self.assertEqual(str(view['updated_at']), '2026-01-01')
        self.assertIn('Original', body)
        self.assertFalse(self.path.exists())

    def test_generic_status_actions_do_not_move_bound_scope_sources(self):
        source = next(path for path in self.selection.declaration_paths if path.name.startswith('CA-R-990001'))
        original = source.read_bytes()
        target = {'ref_id': 'CA-R-990001', 'version': 1}
        with self.assertRaisesRegex(InputError, 'bound Scope Unit source'):
            state_actions.archive_workflow(self.selection, self.model, {'target': target})
        with self.assertRaisesRegex(InputError, 'bound Scope Unit source'):
            state_actions.change_status(self.selection, self.model, {'target': target, 'targetStatus': 'Resolved'})
        self.assertEqual(original, source.read_bytes())

    def test_archived_scope_owned_direct_update_moves_and_preserves_legacy_name(self):
        archived = state_actions.archive_atom(self.selection, self.model, {'target': self.target})
        target = {'ref_id': 'CA-R-10@2', 'version': 2}
        old_path = self.root / archived['artifact']['path']
        legacy = old_path.with_name('CA-R-10@2-LEGACY--example.md')
        old_path.rename(legacy)
        updated = state_actions.direct_update(self.selection, self.model, {'target': target, 'changes': {'body': '## Summary\n\nExample\n\n## Claim\n\nChanged\n'}})
        self.assertEqual(self.root / updated['artifact']['path'], legacy)
        updated = state_actions.direct_update(self.selection, self.model, {'target': target, 'changes': {'summary': 'Revised example'}})
        path = self.root / updated['artifact']['path']
        self.assertEqual(path.name, 'CA-R-10@2-RULE--revised-example.md')
        self.assertFalse(legacy.exists())
        self.assertEqual(self.read(updated['artifact'])[0]['ref_id'], 'CA-R-10@2')
        moved = state_actions.direct_update(self.selection, self.model, {'target': target, 'changes': {'scope_unit': 'OTHER'}})
        other = next(row for row in self.selection.structure['scope_units'] if row['scope_unit_name'] == 'OTHER')
        self.assertEqual((self.root / moved['artifact']['path']).parent, self.root / other['authority_path'] / '04_requirement/archived')
        self.assertFalse(path.exists())

    def test_direct_update_cannot_diverge_published_summaries(self):
        previous = self.folder / 'archived/CA-R-10@1-RULE--example.md'
        previous.parent.mkdir()
        previous.write_text(self.path.read_text().replace('ref_id: CA-R-10\n', 'ref_id: CA-R-10@1\n')
                            .replace('status: Active', 'status: Archived').replace('version: 2', 'version: 1'))
        prior = {path: path.read_bytes() for path in (previous, self.path)}
        targets = (self.target, {'ref_id': 'CA-R-10@1', 'version': 1})
        for target in targets:
            with self.subTest(target=target), self.assertRaisesRegex(InputError, 'Summary conflicts'):
                state_actions.direct_update(self.selection, self.model, {'target': target, 'changes': {
                    'body': '## Summary\n\nDifferent\n\n## Claim\n\nChanged\n',
                }})
        self.assertEqual({path: path.read_bytes() for path in prior}, prior)

    def test_archived_child_direct_update_uses_shared_archive_after_parent_is_archived(self):
        group, _, _ = self._contained('Operations', 'Workflow', 'Step')
        archived = state_actions.archive_workflow(self.selection, self.model,
                                                   {'target': {'ref_id': 'CA-O-20', 'version': 1}})
        self.assertEqual(archived['outcome'], 'completed')
        target = {'ref_id': 'CA-O-21@2', 'version': 2}
        output = state_actions.direct_update(self.selection, self.model,
                                             {'target': target, 'changes': {'summary': 'Revised archived child'}})
        path = self.root / output['artifact']['path']
        self.assertEqual(path, group.parent / 'archived/CA-O-21@2-STEP--revised-archived-child.md')
        view, body = self.read(output['artifact'])
        self.assertEqual((view['ref_id'], view['version'], str(view['updated_at']), view['status']),
                         ('CA-O-21@2', 2, '2026-01-01', 'archived'))
        self.assertEqual(view['container'], {'atom': 'CA-O-20'})
        self.assertIn('Original', body)

        unbound = path.parent.parent / path.name
        path.rename(unbound)
        with self.assertRaisesRegex(InputError, 'outside a shared Role archive'):
            state_actions.direct_update(self.selection, self.model,
                                        {'target': target, 'changes': {'summary': 'Refuse wrong folder'}})

    def test_status_and_direct_update_preserve_unmodified_properties(self):
        with self.assertRaises(InputError):
            state_actions.change_status(self.selection, self.model, {'target': self.target, 'targetStatus': 'resolved'})
        with self.assertRaises(InputError):
            state_actions.direct_update(self.selection, self.model, {'target': self.target, 'changes': {'role': 'Plan'}})
        status = state_actions.change_status(self.selection, self.model, {'target': self.target, 'targetStatus': 'Resolved'})
        view, body = self.read(status['artifact'])
        self.assertEqual((view['status'], view['version'], str(view['updated_at'])), ('resolved', 2, '2026-01-01'))
        updated = state_actions.direct_update(self.selection, self.model, {'target': self.target, 'changes': {'body': body.replace('Original', 'New')}})
        view, body = self.read(updated['artifact'])
        self.assertEqual((view['status'], view['version']), ('resolved', 2))
        self.assertIn('New', body)
        with self.assertRaises(InputError):
            state_actions.direct_update(self.selection, self.model, {'target': self.target, 'changes': {'version': 3}})

    def _contained(self, role, parent_form, child_form, child_status='Active'):
        role_dir = self.folder.parent / ('03_plan' if role == 'Plan' else '09_operations')
        role_dir.mkdir(exist_ok=True)
        letter = 'P' if role == 'Plan' else 'O'
        parent = role_dir / f"{'1-' if role == 'Plan' else ''}CA-{letter}-20-{parent_form.upper()}--parent.md"
        sequence = 'work_sequence_number: 1\n' if role == 'Plan' else ''
        parent.write_text(f'---\n{sequence}atom_id: CA-{letter}-20\nref_id: CA-{letter}-20\ncontainer:\n  scope_unit: TEST\nrole: {role}\nform: {parent_form}\nstatus: Active\nversion: 1\nupdated_at: 2026-01-01\n---\n## Summary\n\nParent\n')
        group = parent.with_suffix('')
        group.mkdir()
        folder = group / 'done' if child_status == 'Done' else group
        folder.mkdir(exist_ok=True)
        child = folder / f"{'2-' if role == 'Plan' else ''}CA-{letter}-21-{child_form.upper()}--child.md"
        sequence = 'work_sequence_number: 2\n' if role == 'Plan' else ''
        child.write_text(f'---\n{sequence}atom_id: CA-{letter}-21\nref_id: CA-{letter}-21\ncontainer:\n  atom: CA-{letter}-20\nrole: {role}\nform: {child_form}\nstatus: {child_status}\nversion: 2\nupdated_at: 2026-01-01\n---\n## Summary\n\nChild\n\n## Claim\n\nOriginal\n')
        return group, child, {'ref_id': f'CA-{letter}-21', 'version': 2}

    def test_terminal_plan_child_archives_and_status_preserves_identity(self):
        group, child, target = self._contained('Plan', 'Epic', 'Task', 'Done')
        self.model = StatusModel(self.model._rows + ((None, None, 'Done'),))
        output = state_actions.change_status(self.selection, self.model, {'target': target, 'targetStatus': 'Active'})
        self.assertEqual(self.root / output['artifact']['path'], group / child.name)
        archived = state_actions.archive_atom(self.selection, self.model, {'target': target})
        self.assertEqual((self.root / archived['artifact']['path']).parent, group.parent / 'archived')
        self.assertEqual(self.read(archived['artifact'])[0]['version'], 2)

    def test_archive_terminal_plan_child(self):
        group, _, target = self._contained('Plan', 'Epic', 'Task', 'Done')
        result = state_actions.archive_atom(self.selection, self.model, {'target': target})
        self.assertEqual((self.root / result['artifact']['path']).parent, group.parent / 'archived')
        self.assertIn('2-CA-P-21@2-', result['artifact']['path'])

    def test_workflow_step_status_and_direct_edit(self):
        group, child, target = self._contained('Operations', 'Workflow', 'Step')
        result = state_actions.change_status(self.selection, self.model, {'target': target, 'targetStatus': 'Resolved'})
        self.assertEqual(self.root / result['artifact']['path'], group / 'resolved' / child.name)
        updated = state_actions.direct_update(self.selection, self.model, {'target': target, 'changes': {'summary': 'Revised child'}})
        self.assertEqual((self.root / updated['artifact']['path']).parent, group / 'resolved')
        self.assertIn('Revised child', self.read(updated['artifact'])[1])

    def test_reject_wrong_physical_parent_and_container_effects(self):
        group, child, target = self._contained('Operations', 'Workflow', 'Step')
        wrong = group.parent / child.name
        child.rename(wrong)
        with self.assertRaises(InputError):
            state_actions.change_status(self.selection, self.model, {'target': target, 'targetStatus': 'Resolved'})
        with self.assertRaises(InputError):
            state_actions.archive_atom(self.selection, self.model, {'target': {'ref_id': 'CA-O-20', 'version': 1}})

    def _retained_child(self, group, child):
        history = group / 'CA-O-21@1-STEP--old.md'
        history.write_bytes(child.read_bytes().replace(b'ref_id: CA-O-21\n', b'ref_id: CA-O-21@1\n')
                            .replace(b'status: Active\n', b'status: Archived\n')
                            .replace(b'version: 2\n', b'version: 1\n') + b'\nHistorical bytes.\n')
        return history, history.read_bytes()

    def test_parent_archive_moves_history_unchanged_without_selecting_it(self):
        group, child, _ = self._contained('Operations', 'Workflow', 'Step')
        history, original = self._retained_child(group, child)
        parent = select_source(self.selection, 'CA-O-20')
        pins = select_archive_cascade(self.selection, parent, self.model)
        self.assertEqual([('CA-O-21', 2), ('CA-O-20', 1)], [(pin.atom_id, pin.version) for pin in pins])

        result = state_actions.archive_workflow(self.selection, self.model,
                                                 {'target': {'ref_id': 'CA-O-20', 'version': 1}})
        self.assertEqual(result['outcome'], 'completed')
        moved_group = (self.root / result['artifact']['path']).with_suffix('')
        self.assertEqual(original, (moved_group / history.name).read_bytes())
        self.assertFalse(history.exists())

    def test_parent_current_status_move_preserves_history_bytes(self):
        group, child, _ = self._contained('Operations', 'Workflow', 'Step')
        history, original = self._retained_child(group, child)
        original = original.replace(b'atom_id: CA-O-21\n', b'atom_id: CA-O-21@1\n')
        self.assertIn(b'atom_id: CA-O-21@1\n', original)
        history.write_bytes(original)
        with patch.object(status_cascade, 'validate_candidate'):
            result = status_cascade.change_status_workflow(
                self.selection, self.model,
                {'target': {'ref_id': 'CA-O-20', 'version': 1}, 'targetStatus': 'Resolved'})
        self.assertEqual(result['outcome'], 'completed')
        moved_group = (self.root / result['artifact']['path']).with_suffix('')
        self.assertEqual(original, (moved_group / history.name).read_bytes())
        self.assertFalse(history.exists())
        self.assertEqual('resolved', self.read(result['artifact'])[0]['status'])

    def test_in_tree_draft_is_not_treated_as_history(self):
        group, child, _ = self._contained('Operations', 'Workflow', 'Step')
        history, _ = self._retained_child(group, child)
        history.write_bytes(history.read_bytes().replace(b'status: Archived', b'status: Draft'))
        with self.assertRaises(InputError):
            select_archive_cascade(self.selection, select_source(self.selection, 'CA-O-20'), self.model)

    def test_synthetic_placement_drives_source_predecessor_and_cascade(self):
        group, child, _ = self._contained('Operations', 'Workflow', 'Step')
        original_role = group.parent
        renamed_role = original_role.with_name('custom_operations')
        original_role.rename(renamed_role)
        group = renamed_role / group.name
        child = group / child.name
        with bind_placement(fixture_rules(operations_folder='custom_operations', resolved_folder='settled')):
            self.assertEqual(child, select_source(self.selection, 'CA-O-21').path)
            self.assertEqual(group / 'settled' / child.name,
                             derive_destination(self.selection, atom_id='CA-O-21', version=2,
                                 status='Resolved', role='Operations', form='Step', summary='Child',
                                 scope_unit='TEST', parent=group))
            target = {'ref_id': 'CA-O-20', 'version': 1}
            with patch.object(status_cascade, 'validate_candidate'):
                changed = status_cascade.change_status_workflow(
                    self.selection, self.model, {'target': target, 'targetStatus': 'Resolved'})
            self.assertEqual(changed['outcome'], 'completed', changed)
            moved_group = (self.root / changed['artifact']['path']).with_suffix('')
            moved_child = moved_group / 'settled' / child.name
            self.assertEqual(moved_child, select_source(self.selection, 'CA-O-21').path)
            archived_path = derive_destination(self.selection, atom_id='CA-O-21', version=2,
                status='Archived', role='Operations', form='Step', summary='Child',
                scope_unit='TEST', parent=moved_group, source_path=moved_child)
            self.assertEqual(renamed_role / 'archived/CA-O-21@2-STEP--child.md', archived_path)
            archived = state_actions.archive_workflow(self.selection, self.model, {'target': target})
            self.assertEqual(archived['outcome'], 'completed', archived)
            self.assertTrue(archived_path.exists())

    def test_partial_effects_reported_and_no_overwrite(self):
        with patch.object(effects, 'remove', return_value=effects.Result(errors=[{'code': 'backend_failure'}])):
            result = state_actions.archive_atom(self.selection, self.model, {'target': self.target})
        self.assertEqual(result['outcome'], 'failed')
        self.assertTrue(result['effects'])
        self.assertNotIn('artifact', result)
        self.assertTrue(self.path.exists())

    def test_plan_archive_reports_remaining_targets_after_child_commits(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task')
        parent_target = {'ref_id': 'CA-P-20', 'version': 1}
        publish = state_actions._publish

        def fail_parent(selection, pin, *args, **kwargs):
            if pin.atom_id == 'CA-P-20':
                return state_actions.result(errors=[{'code': 'backend_failure'}])
            return publish(selection, pin, *args, **kwargs)

        with patch.object(state_actions, '_publish', side_effect=fail_parent):
            outcome = state_actions.archive_workflow(self.selection, self.model, {'target': parent_target})
        self.assertEqual(outcome['outcome'], 'failed')
        self.assertEqual(outcome['remaining_targets'], [parent_target])
        self.assertTrue(outcome['effects'])
        self.assertFalse(child.exists())
        self.assertTrue(group.with_suffix('.md').exists())


if __name__ == '__main__':
    unittest.main()
