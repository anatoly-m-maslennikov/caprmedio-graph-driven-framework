# CA-E-827@1
# CA-E-826@4
from datetime import datetime
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE import common, draft  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from lifecycle_placement_test_support import bind_placement, fixture_rules  # noqa: E402


class Model:
    def allowed(self, role, form):
        return {'Draft'}


class DraftTest(unittest.TestCase):
    def setUp(self):
        binding = bind_placement(fixture_rules())
        binding.__enter__()
        self.addCleanup(binding.__exit__, None, None, None)
        scratch = TOOLS.parents[2] / '.caprmedio_tmp/CA-P-2791/CA-P-2934/draft'
        scratch.mkdir(parents=True, exist_ok=True)
        tmp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        control = self.root / '.caprmedio_test'
        control.mkdir()
        (control / 'caprmedio_project_settings.toml').write_text(
            '[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n'
            '[paths]\ncontrol_root=".caprmedio_test"\n')
        write_scope_unit_declarations(self.root, control_root=control, rows=[])
        self.selection = resolve_project(self.root)
        self.source = control / '04_requirement/CA-R-1-DECLARATION--example.md'
        self.source.parent.mkdir()
        self.source.write_text('---\nidentity:\n  atom_id: CA-R-1\n  ref_id: CA-R-1\n'
                               'context:\n  container:\n    scope_unit: TEST\n  role: Requirement\n'
                               '  form: Declaration\nstate:\n  status: Active\n  version: 2\n'
                               '  updated_at: 2026-01-01\n---\n## Summary\n\nExample\n\n## Claim\n\nRetain me.\n')
        self.selector = {'ref_id': 'CA-R-1', 'version': 2}
        self.allocation = patch.object(common, 'allocate_id', return_value='CA-R-9')
        self.allocation.start()
        self.addCleanup(self.allocation.stop)

    def test_copy_from_draft_keeps_source_and_body(self):
        result = draft.create_draft(self.selection, Model(), {'sourceCurrent': self.selector, 'changes': {}})
        self.assertFalse(result['errors'])
        saved = result['savedDraft']
        self.assertEqual((saved['atom_id'], saved['version']), ('CA-R-1', 3))
        path = self.root / saved['path']
        first = path.read_text()
        self.assertIn('Retain me.', first)
        result = draft.create_draft(self.selection, Model(), {
            'sourceCurrent': {'ref_id': 'CA-R-1@3-draft', 'version': 3}, 'changes': {'label': 'Declaration'}})
        self.assertFalse(result['errors'])
        self.assertEqual(result['savedDraft']['version'], 4)
        self.assertEqual(first, path.read_text())
        self.assertIn('Retain me.', (self.root / result['savedDraft']['path']).read_text())
        self.assertEqual(self.source.read_text().count('status: Active'), 1)

    def test_independent_copy_preserves_relations_and_source(self):
        from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

        self.source.write_text(self.source.read_text().replace(
            'state:\n', 'relations:\n  IS_REPLACEMENT_FOR: [CA-R-8]\n  DEPENDS_ON: [CA-R-7]\nstate:\n'))
        before = self.source.read_bytes()
        result = draft.create_draft(self.selection, Model(), {'copyFrom': 'CA-R-1'})
        self.assertFalse(result['errors'])
        saved = result['savedDraft']
        self.assertEqual((saved['atom_id'], saved['version']), ('CA-R-9', 1))
        copied = parse_carrier((self.root / saved['path']).read_bytes(), Path(saved['path']))
        self.assertEqual(copied.metadata['relations'],
                         {'IS_REPLACEMENT_FOR': ['CA-R-8'], 'DEPENDS_ON': ['CA-R-7']})
        self.assertEqual(self.source.read_bytes(), before)
        self.assertIn('Retain me.', copied.body)

    def test_independent_copy_from_exact_archive_and_draft(self):
        archive = self.source.parent / 'archived' / 'CA-R-1@1-DECLARATION--example.md'
        archive.parent.mkdir()
        archive.write_text(self.source.read_text().replace('ref_id: CA-R-1', 'ref_id: CA-R-1@1')
                           .replace('status: Active', 'status: Archived').replace('version: 2', 'version: 1')
                           .replace('Retain me.', 'Historical claim.'))
        before_archive = archive.read_bytes()
        old = draft.create_draft(self.selection, Model(), {'copyFrom': {'ref_id': 'CA-R-1', 'version': 1}})
        self.assertEqual((old['savedDraft']['atom_id'], old['savedDraft']['version']), ('CA-R-9', 1))
        copied = self.root / old['savedDraft']['path']
        self.assertIn('Historical claim.', copied.read_text())
        self.assertEqual(archive.read_bytes(), before_archive)
        before_draft = copied.read_bytes()
        with patch.object(common, 'allocate_id', return_value='CA-R-10'):
            other = draft.create_draft(self.selection, Model(), {
                'copyFrom': {'ref_id': 'CA-R-9@1-draft', 'version': 1},
                'changes': {'summary': 'Independent copy', 'tier': 2}})
        self.assertEqual((other['savedDraft']['atom_id'], other['savedDraft']['version']), ('CA-R-10', 1))
        self.assertEqual(copied.read_bytes(), before_draft)
        self.assertIn('Historical claim.', (self.root / other['savedDraft']['path']).read_text())

    def test_independent_copy_requires_one_valid_source(self):
        with self.assertRaises(common.InputError) as caught:
            draft.prepare_draft(self.selection, Model(), {'copyFrom': {'version': 1}})
        self.assertEqual(caught.exception.field, 'copyFrom')
        with self.assertRaises(common.InputError):
            draft.prepare_draft(self.selection, Model(), {'copyFrom': 'CA-R-1', 'sourceCurrent': 'CA-R-1'})

    def test_current_without_version_and_historical_version_selection(self):
        no_version = draft.prepare_draft(self.selection, Model(), {'sourceCurrent': 'CA-R-1'})
        self.assertEqual((no_version['pin'].version, no_version['version']), (2, 3))
        archived = self.source.parent / 'archived' / 'CA-R-1@1-DECLARATION--example.md'
        archived.parent.mkdir()
        archived.write_text(self.source.read_text().replace('ref_id: CA-R-1', 'ref_id: CA-R-1@1')
                            .replace('status: Active', 'status: Archived').replace('version: 2', 'version: 1')
                            .replace('Retain me.', 'Historical claim.'))
        result = draft.create_draft(self.selection, Model(),
                                    {'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 1}})
        self.assertEqual(result['savedDraft']['version'], 3)
        self.assertIn('Historical claim.', (self.root / result['savedDraft']['path']).read_text())
        self.assertIn('Retain me.', self.source.read_text())

    def test_historical_source_skips_existing_revision_numbers(self):
        archived = self.source.parent / 'archived' / 'CA-R-1@1-DECLARATION--example.md'
        archived.parent.mkdir()
        archived.write_text(self.source.read_text().replace('ref_id: CA-R-1', 'ref_id: CA-R-1@1')
                            .replace('status: Active', 'status: Archived').replace('version: 2', 'version: 1'))
        other = archived.with_name('CA-R-1@8-DECLARATION--example.md')
        other.write_text(archived.read_text().replace('CA-R-1@1', 'CA-R-1@8').replace('version: 1', 'version: 8'))
        plan = draft.prepare_draft(self.selection, Model(), {'sourceCurrent': 'CA-R-1@1'})
        self.assertEqual(plan['version'], 9)

    def test_base_id_and_version_copy_an_existing_draft(self):
        original = draft.create_draft(self.selection, Model(), {'sourceCurrent': 'CA-R-1'})['savedDraft']
        source_path = self.root / original['path']
        before = source_path.read_bytes()
        result = draft.create_draft(self.selection, Model(), {
            'sourceCurrent': {'ref_id': 'CA-R-1', 'version': 3}, 'changes': {'tier': 2},
        })
        self.assertEqual(result['savedDraft']['version'], 4)
        self.assertEqual(source_path.read_bytes(), before)
        self.assertIn('Retain me.', (self.root / result['savedDraft']['path']).read_text())

    def test_changed_summary_allocates_new_identity(self):
        result = draft.create_draft(self.selection, Model(), {'sourceCurrent': self.selector,
                                                               'changes': {'summary': 'New example'}})
        self.assertFalse(result['errors'])
        self.assertEqual((result['savedDraft']['atom_id'], result['savedDraft']['version']), ('CA-R-9', 1))
        self.assertIn('New example', (self.root / result['savedDraft']['path']).read_text())

    def test_replacement_preserves_explicit_predecessors_and_rejects_conflicting_aliases(self):
        from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

        text = self.source.read_text().replace('state:\n', 'relations:\n  IS_REPLACEMENT_FOR:\n  - CA-R-8\nstate:\n')
        self.source.write_text(text)
        source_pin = draft._source(self.selection, self.selector)
        plan = draft.prepare_draft(self.selection, Model(), {'sourceCurrent': self.selector,
                                   'changes': {'summary': 'New example', 'relations': {
                                       'is_replacement_for': ['CA-R-7']}}}, source_pin=source_pin)
        parsed = parse_carrier(plan['raw'], plan['destination'])
        self.assertNotIn('IS_REPLACEMENT_FOR', parsed.metadata['relations'])
        self.assertEqual(parsed.metadata['relations']['is_replacement_for'], ['CA-R-8', 'CA-R-7', 'CA-R-1'])
        with self.assertRaises(common.InputError):
            draft.prepare_draft(self.selection, Model(), {'sourceCurrent': self.selector,
                                'changes': {'summary': 'New example', 'relations': {
                                    'is_replacement_for': ['CA-R-7'], 'IS_REPLACEMENT_FOR': ['CA-R-8']}}},
                                source_pin=source_pin)

    def test_create_draft_changes_only_supplied_relations(self):
        from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

        plan = draft.prepare_draft(self.selection, Model(), {'sourceCurrent': self.selector,
                                   'changes': {'summary': 'New example', 'relations': {
                                       'is_replacement_for': ['CA-R-7']}}})
        parsed = parse_carrier(plan['raw'], plan['destination'])
        self.assertEqual({'is_replacement_for': ['CA-R-7']}, parsed.metadata['relations'])

    def test_empty_input_requests_new_atom(self):
        with self.assertRaises(common.InputError) as caught:
            draft.prepare_draft(self.selection, Model(), {})
        self.assertEqual(caught.exception.field, 'newAtom')

    def test_incomplete_atom_returns_all_independent_missing_fields(self):
        with self.assertRaises(common.InputError) as caught:
            draft.prepare_draft(self.selection, Model(), {'newAtom': {'role': 'Requirement'}})
        self.assertEqual(set(caught.exception.requested_input), {'form', 'scope_unit', 'summary'})

    def test_new_atom(self):
        from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier

        result = draft.create_draft(self.selection, Model(), {'newAtom': {
            'role': 'Requirement', 'form': 'Declaration', 'scope_unit': 'TEST',
            'summary': 'Brand new', 'body': '## Summary\n\nBrand new\n'}})
        self.assertFalse(result['errors'])
        self.assertEqual((result['savedDraft']['atom_id'], result['savedDraft']['version']), ('CA-R-9', 1))
        path = self.root / result['savedDraft']['path']
        updated_at = parse_carrier(path.read_bytes(), path).metadata['state']['updated_at']
        self.assertIsInstance(updated_at, str)
        self.assertIsNotNone(datetime.fromisoformat(updated_at).utcoffset())

    def test_create_draft_uses_ordinary_range_with_probe_present(self):
        self.allocation.stop()
        settings = self.selection.control_root / 'caprmedio_project_settings.toml'
        settings.write_text(settings.read_text().replace('project_prefix="CA"',
                                                         'project_prefix="CA"\nautomatic_number_ceiling=2'))
        self.selection = resolve_project(self.root)
        probe = self.source.with_name('CA-R-970308622-DECLARATION--probe.md')
        probe.write_text(self.source.read_text().replace('CA-R-1', 'CA-R-970308622'))
        request = {'newAtom': {'role': 'Requirement', 'form': 'Declaration',
                               'scope_unit': 'TEST', 'summary': 'New Atom'}}
        result = draft.create_draft(self.selection, Model(), request)
        self.assertEqual(result['savedDraft']['atom_id'], 'CA-R-2')
        self.assertTrue((self.root / result['savedDraft']['path']).is_file())
        with self.assertRaisesRegex(ValueError, 'reached its configured ceiling'):
            draft.create_draft(self.selection, Model(), request)

    def test_copy_draft_derives_destination_after_form_change(self):
        initial = draft.create_draft(self.selection, Model(), {'sourceCurrent': self.selector, 'changes': {}})
        previous = self.root / initial['savedDraft']['path']
        result = draft.create_draft(self.selection, Model(), {
            'sourceCurrent': {'ref_id': 'CA-R-1@3-draft', 'version': 3},
            'changes': {'form': 'Rule', 'filename': 'ignored.md'}})
        self.assertFalse(result['errors'])
        self.assertTrue(previous.exists())
        self.assertTrue((self.root / result['savedDraft']['path']).exists())
        self.assertEqual(result['savedDraft']['version'], 4)
        self.assertTrue(result['warnings'])

    def test_prepare_has_no_effect_and_forbidden_metadata_fails(self):
        plan = draft.prepare_draft(self.selection, Model(), {'sourceCurrent': self.selector, 'changes': {}})
        self.assertFalse(plan['destination'].exists())
        with self.assertRaises(common.InputError):
            draft.prepare_draft(self.selection, Model(), {'sourceCurrent': self.selector, 'changes': {'version': 5}})


if __name__ == '__main__':
    unittest.main()
