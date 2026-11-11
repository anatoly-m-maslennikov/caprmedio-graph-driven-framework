"""Integration coverage for shared Plan Backlog and logical containment."""
from dataclasses import replace
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / 'tests')]

from ATOM_LIFECYCLE import common, state_actions, status_cascade  # noqa: E402
from ATOM_LIFECYCLE.placement_model import bind_placement  # noqa: E402
from ATOM_LIFECYCLE.plan_cascade import select_archive_cascade  # noqa: E402
from ATOM_LIFECYCLE.source import select_source  # noqa: E402
from ATOM_LIFECYCLE.status_model import StatusModel  # noqa: E402
from carrier_aliases import carrier_read_view  # noqa: E402
from lifecycle_placement_test_support import fixture_rules  # noqa: E402
import test_lifecycle_state_actions as fixtures  # noqa: E402


class SharedBacklogAcceptance(unittest.TestCase):
    _contained = fixtures.StateActionsTest._contained
    # This synthetic first-level placement is only a test seam. Nested Backlog
    # needs the contextual rule once the compiled grammar and API support it.
    def setUp(self):
        fixtures.StateActionsTest.setUp(self)
        rules = fixture_rules()
        placements = dict(rules._placements)
        self.backlog_folder = rules.placement('Plan', 'Backlog')[1]
        self.archive_folder = rules.placement('Plan', 'Archived')[1]
        placements[('plan', 'backlog')] = ('role', self.backlog_folder)
        binding = bind_placement(replace(rules, _placements=placements))
        binding.__enter__()
        self.addCleanup(binding.__exit__, None, None, None)
        self.model = StatusModel(self.model._rows + ((None, None, 'Backlog'),
                                                    (None, None, 'Done'),
                                                    (None, None, 'Canceled')))
        patcher = patch.object(status_cascade, 'validate_candidate')
        patcher.start()
        self.addCleanup(patcher.stop)

    def tree(self, *, mixed=False):
        group, child, _ = self._contained('Plan', 'Epic', 'Task')
        shared = group.parent / self.backlog_folder
        shared.mkdir()
        child.write_text(child.read_text().replace('status: Active', 'status: Backlog'))
        child = child.rename(shared / child.name)
        if mixed:
            physical = group / '6-CA-P-25-TASK--physical.md'
            physical.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 6')
                                .replace('CA-P-21', 'CA-P-25').replace('status: Backlog', 'status: Active')
                                .replace('\nChild\n', '\nPhysical\n'))
        else:
            group.rmdir()  # Parent has a logical child without a companion directory.
        self.role_root = group.parent
        nested_dir = child.with_suffix('')
        nested_dir.mkdir()
        nested = nested_dir / '3-CA-P-22-TASK--nested.md'
        nested.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 3')
                          .replace('CA-P-21', 'CA-P-22').replace('CA-P-20', 'CA-P-21')
                          .replace('\nChild\n', '\nNested\n'))
        sibling = shared / '4-CA-P-24-TASK--sibling.md'
        sibling.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 4')
                           .replace('CA-P-21', 'CA-P-24').replace('CA-P-20', 'CA-P-23'))
        other = group.parent / '5-CA-P-23-EPIC--other.md'
        other.write_text((group.with_suffix('.md')).read_text().replace('work_sequence_number: 1', 'work_sequence_number: 5')
                         .replace('CA-P-20', 'CA-P-23'))
        return child, nested, sibling, sibling.read_bytes()

    def assert_sibling_unchanged(self, sibling, original):
        self.assertEqual(original, sibling.read_bytes())

    def _terminal_tree(self, *, outer=False):
        group, child, _ = self._contained('Plan', 'Epic', 'Task', 'Done')
        parent = group.with_suffix('.md')
        parent.write_text(parent.read_text().replace('status: Active', 'status: Done')
                          .replace('updated_at: 2026-01-01', 'updated_at: 2026-01-01T00:00:00+00:00'))
        child.write_text(child.read_text().replace('updated_at: 2026-01-01', 'updated_at: 2026-01-01T00:00:00+00:00'))
        child_group = child.with_suffix('')
        child_group.mkdir()
        nested_dir = child_group / 'canceled'
        nested_dir.mkdir()
        nested = nested_dir / '3-CA-P-22-TASK--nested.md'
        nested.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 3')
                          .replace('CA-P-21', 'CA-P-22').replace('CA-P-20', 'CA-P-21')
                          .replace('status: Done', 'status: Canceled').replace('\nChild\n', '\nNested\n'))
        role = group.parent
        if outer:
            top = role / 'done/9-CA-P-19-EPIC--outer.md'
            top.parent.mkdir(parents=True)
            top.write_text(parent.read_text().replace('CA-P-20', 'CA-P-19')
                           .replace('work_sequence_number: 1', 'work_sequence_number: 9')
                           .replace('\nParent\n', '\nOuter\n'))
            destination = top.with_suffix('') / 'done'
            destination.mkdir(parents=True)
            parent.write_text(parent.read_text().replace('scope_unit: TEST', 'atom: CA-P-19'))
        else:
            destination = role / 'done'
            destination.mkdir(exist_ok=True)
        parent.rename(destination / parent.name)
        group.rename(destination / group.name)

    def test_reopening_parent_first_preserves_containment_and_versions(self):
        from ATOM_LIFECYCLE.validation import validate_candidate

        self._terminal_tree()
        order = []
        apply = status_cascade._apply
        def record(*args, **kwargs):
            order.append(args[2].atom_id)
            return apply(*args, **kwargs)
        with patch.object(status_cascade, '_apply', side_effect=record), \
                patch.object(state_actions, 'validate_candidate', validate_candidate), \
                patch.object(status_cascade, 'validate_candidate', validate_candidate):
            output = status_cascade.change_status_workflow(self.selection, self.model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Active'})
        self.assertEqual('completed', output['outcome'], output)
        self.assertEqual(['CA-P-20', 'CA-P-21', 'CA-P-22'], order)
        for ref, version, container in (('CA-P-20', 1, {'scope_unit': 'TEST'}),
                                        ('CA-P-21', 2, {'atom': 'CA-P-20'}),
                                        ('CA-P-22', 2, {'atom': 'CA-P-21'})):
            pin = select_source(self.selection, ref)
            view = carrier_read_view(pin.metadata)
            self.assertEqual(('active', version, container), (pin.status, pin.version, view['container']))
            self.assertEqual('2026-01-01T00:00:00+00:00', view['updated_at'].isoformat())

    def test_reopening_refuses_terminal_ancestor_outside_selected_tree(self):
        from ATOM_LIFECYCLE.validation import validate_candidate

        self._terminal_tree(outer=True)
        before = {path: path.read_bytes() for path in self.role_files()}
        with patch.object(state_actions, 'validate_candidate', validate_candidate), \
                patch.object(status_cascade, 'validate_candidate', validate_candidate), \
                self.assertRaisesRegex(common.InputError, 'inside a Done or Canceled Plan'):
            status_cascade.change_status_workflow(self.selection, self.model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Active'})
        self.assertEqual(before, {path: path.read_bytes() for path in self.role_files()})

    def test_reopening_preflights_each_descendant_status(self):
        self._terminal_tree()
        before = {path: path.read_bytes() for path in self.role_files()}
        model = StatusModel(((None, None, 'Done'), ('Plan', 'Epic', 'Active'), ('Plan', None, 'Canceled')))
        with self.assertRaisesRegex(common.InputError, 'not admitted'):
            status_cascade.change_status_workflow(self.selection, model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Active'})
        self.assertEqual(before, {path: path.read_bytes() for path in self.role_files()})

    def test_reopening_to_backlog_uses_new_parent_locations(self):
        from ATOM_LIFECYCLE.validation import validate_candidate

        self._terminal_tree()
        with patch.object(state_actions, 'validate_candidate', validate_candidate), \
                patch.object(status_cascade, 'validate_candidate', validate_candidate):
            output = status_cascade.change_status_workflow(self.selection, self.model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Backlog'})
        self.assertEqual('completed', output['outcome'], output)
        parent, child, nested = (select_source(self.selection, ref) for ref in ('CA-P-20', 'CA-P-21', 'CA-P-22'))
        self.assertTrue(all(pin.status == 'backlog' for pin in (parent, child, nested)))
        self.assertEqual(child.path.parent, parent.path.with_suffix(''))
        self.assertEqual(nested.path.parent, child.path.with_suffix(''))

    def test_reopening_stops_and_reports_remaining_after_parent(self):
        self._terminal_tree()
        apply = status_cascade._apply
        def fail_child(*args, **kwargs):
            if args[2].atom_id == 'CA-P-21':
                raise common.InputError('target', 'Injected failure.')
            return apply(*args, **kwargs)

        with patch.object(status_cascade, '_apply', side_effect=fail_child):
            result = status_cascade.change_status_workflow(self.selection, self.model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Active'})
        self.assertEqual('failed', result['outcome'])
        self.assertTrue(result['effects'])
        self.assertEqual(['CA-P-21', 'CA-P-22'], [item['ref_id'] for item in result['remaining_targets']])
        self.assertEqual('active', select_source(self.selection, 'CA-P-20').status)
        self.assertEqual('done', select_source(self.selection, 'CA-P-21').status.casefold())

    def role_files(self):
        return (self.folder.parent / '03_plan').rglob('*.md')

    def test_selection_finds_logical_children_without_a_companion(self):
        self.tree()
        parent = select_source(self.selection, 'CA-P-20')
        pins = select_archive_cascade(self.selection, parent, self.model)
        self.assertEqual(['CA-P-22', 'CA-P-21', 'CA-P-20'], [pin.atom_id for pin in pins])

    def test_done_closes_logical_tree_child_first(self):
        _, _, sibling, original = self.tree()
        result = status_cascade.change_status_workflow(
            self.selection, self.model, {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Done'})
        self.assertEqual('completed', result['outcome'], result)
        self.assertEqual('canceled', select_source(self.selection, 'CA-P-22').status.casefold())
        self.assertEqual('canceled', select_source(self.selection, 'CA-P-21').status.casefold())
        self.assertEqual('done', select_source(self.selection, 'CA-P-20').status.casefold())
        child, nested = (select_source(self.selection, ref) for ref in ('CA-P-21', 'CA-P-22'))
        self.assertEqual({'atom': 'CA-P-20'}, carrier_read_view(child.metadata)['container'])
        self.assertEqual({'atom': 'CA-P-21'}, carrier_read_view(nested.metadata)['container'])
        creates = [effect['target'] for effect in result['effects'] if effect['operation'] == 'create' and effect['target'].endswith('.md')]
        indices = [next(i for i, target in enumerate(creates) if ref in Path(target).name) for ref in ('CA-P-22', 'CA-P-21', 'CA-P-20')]
        self.assertEqual(sorted(indices), indices)
        self.assert_sibling_unchanged(sibling, original)

    def test_archive_moves_logical_tree_and_excludes_sibling(self):
        _, _, sibling, original = self.tree()
        result = state_actions.archive_workflow(self.selection, self.model,
                                                {'target': {'ref_id': 'CA-P-20', 'version': 1}})
        self.assertEqual('completed', result['outcome'], result)
        for ref, version in [('CA-P-22', 2), ('CA-P-21', 2), ('CA-P-20', 1)]:
            pin = select_source(self.selection, f'{ref}@{version}')
            self.assertEqual('archived', pin.status.casefold())
            view = carrier_read_view(pin.metadata)
            self.assertEqual((ref, version, '2026-01-01'), (view['atom_id'], view['version'], str(view['updated_at'])))
            self.assertEqual(self.role_root / self.archive_folder, pin.path.parent)
            self.assertEqual({'name': pin.path.name, 'path': pin.path.parent.relative_to(self.root).as_posix()},
                             view['destination']['file'])
            self.assertIn(f'{ref}@{version}-', pin.path.name)
        self.assert_sibling_unchanged(sibling, original)

    def test_archive_includes_both_physical_and_shared_backlog_children(self):
        _, _, sibling, original = self.tree(mixed=True)
        result = state_actions.archive_workflow(self.selection, self.model,
                                                {'target': {'ref_id': 'CA-P-20', 'version': 1}})
        self.assertEqual('completed', result['outcome'], result)
        for ref, version in [('CA-P-22', 2), ('CA-P-21', 2), ('CA-P-25', 2), ('CA-P-20', 1)]:
            pin = select_source(self.selection, f'{ref}@{version}')
            self.assertEqual(self.role_root / self.archive_folder, pin.path.parent)
            self.assertEqual('archived', pin.status.casefold())
        self.assert_sibling_unchanged(sibling, original)

    def test_active_plan_tree_moved_to_backlog_is_nested(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task')
        child_group = child.with_suffix('')
        child_group.mkdir()
        nested = child_group / '3-CA-P-22-TASK--nested.md'
        nested.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 3')
                          .replace('CA-P-21', 'CA-P-22').replace('CA-P-20', 'CA-P-21')
                          .replace('\nChild\n', '\nNested\n'))
        role = group.parent
        parent_name = group.with_suffix('.md').name
        result = status_cascade.change_status_workflow(self.selection, self.model,
            {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Backlog'})
        self.assertEqual('completed', result['outcome'], result)
        parent_path = role / self.backlog_folder / parent_name
        child_path = parent_path.with_suffix('') / child.name
        nested_path = child_path.with_suffix('') / nested.name
        for ref, version, path, container in [
            ('CA-P-20', 1, parent_path, {'scope_unit': 'TEST'}),
            ('CA-P-21', 2, child_path, {'atom': 'CA-P-20'}),
            ('CA-P-22', 2, nested_path, {'atom': 'CA-P-21'}),
        ]:
            pin = select_source(self.selection, ref)
            view = carrier_read_view(pin.metadata)
            self.assertEqual(path, pin.path)
            self.assertEqual((version, 'backlog', container, '2026-01-01'),
                             (pin.version, pin.status.casefold(), view['container'], str(view['updated_at'])))

    def test_mixed_active_and_shared_tree_enters_backlog_with_validation(self):
        child, nested, sibling, _ = self.tree(mixed=True)
        for path in self.role_root.rglob('*.md'):
            path.write_bytes(path.read_bytes().replace(b'2026-01-01\n', b'2026-01-01T00:00:00+00:00\n'))
        sibling_before = sibling.read_bytes()
        with (patch.object(state_actions, 'validate_candidate', common.validate_candidate),
              patch.object(status_cascade, 'validate_candidate', common.validate_candidate)):
            result = status_cascade.change_status_workflow(self.selection, self.model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Backlog'})
        self.assertEqual('completed', result['outcome'], result)
        parent_path = self.role_root / self.backlog_folder / '1-CA-P-20-EPIC--parent.md'
        child_path = parent_path.with_suffix('') / child.name
        expected = {'CA-P-20': parent_path, 'CA-P-21': child_path,
                    'CA-P-22': child_path.with_suffix('') / nested.name,
                    'CA-P-25': parent_path.with_suffix('') / '6-CA-P-25-TASK--physical.md'}
        for ref, path in expected.items():
            pin = select_source(self.selection, ref)
            self.assertEqual(path, pin.path)
            self.assertEqual('backlog', pin.status.casefold())
            view = carrier_read_view(pin.metadata)
            self.assertEqual({'name': path.name, 'path': path.parent.relative_to(self.root).as_posix()},
                             view['destination']['file'])
            self.assertEqual('2026-01-01 00:00:00+00:00', str(view['updated_at']))
        self.assert_sibling_unchanged(sibling, sibling_before)

    def test_done_refuses_child_added_after_tree_selection(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task')
        shared = group.parent / self.backlog_folder
        shared.mkdir()
        original_plan = status_cascade._plan

        def add_child_after_plan(*args, **kwargs):
            actions = original_plan(*args, **kwargs)
            newcomer = shared / '7-CA-P-27-TASK--new.md'
            newcomer.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 7')
                                .replace('CA-P-21', 'CA-P-27').replace('status: Active', 'status: Backlog')
                                .replace('\nChild\n', '\nNew\n'))
            return actions

        with patch.object(status_cascade, '_plan', side_effect=add_child_after_plan):
            result = status_cascade.change_status_workflow(self.selection, self.model,
                {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Done'})
        self.assertEqual('failed', result['outcome'], result)
        self.assertEqual('active', select_source(self.selection, 'CA-P-20').status.casefold())
        self.assertIn({'ref_id': 'CA-P-20', 'version': 1, 'target_status': 'Done'}, result['remaining_targets'])
        self.assertEqual('backlog', select_source(self.selection, 'CA-P-27').status.casefold())

    def test_retired_decomposition_link_without_container_is_not_a_child(self):
        group, child, _ = self._contained('Plan', 'Epic', 'Task')
        shared = group.parent / self.backlog_folder
        shared.mkdir()
        legacy = shared / '7-CA-P-27-TASK--legacy.md'
        legacy.write_text(child.read_text().replace('work_sequence_number: 2', 'work_sequence_number: 7')
                          .replace('CA-P-21', 'CA-P-27').replace('status: Active', 'status: Backlog')
                          .replace('container:\n  atom: CA-P-20\n',
                                   'relations:\n  is_decomposition_of: [CA-P-20]\n')
                          .replace('\nChild\n', '\nLegacy\n'))
        original = legacy.read_bytes()
        result = status_cascade.change_status_workflow(self.selection, self.model,
            {'target': {'ref_id': 'CA-P-20', 'version': 1}, 'targetStatus': 'Done'})
        self.assertEqual('completed', result['outcome'], result)
        self.assertEqual('done', select_source(self.selection, 'CA-P-20').status.casefold())
        self.assertEqual('canceled', select_source(self.selection, 'CA-P-21').status.casefold())
        self.assertEqual(original, legacy.read_bytes())

    def test_single_atom_archive_must_not_ignore_logical_children(self):
        self.tree()
        with self.assertRaises(ValueError):
            state_actions.archive_atom(self.selection, self.model,
                                       {'target': {'ref_id': 'CA-P-20', 'version': 1}})


