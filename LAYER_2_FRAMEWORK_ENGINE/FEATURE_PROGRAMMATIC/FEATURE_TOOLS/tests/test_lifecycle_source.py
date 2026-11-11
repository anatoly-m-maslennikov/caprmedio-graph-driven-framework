from pathlib import Path
import hashlib
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
import ATOM_LIFECYCLE.source as source_module  # noqa: E402
from ATOM_LIFECYCLE.source import select_source, SourceSelectionError  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from lifecycle_placement_test_support import bind_placement, fixture_rules  # noqa: E402


class SourceTest(unittest.TestCase):
    def setUp(self):
        binding = bind_placement(fixture_rules())
        binding.__enter__()
        self.addCleanup(binding.__exit__, None, None, None)
        scratch = TOOLS.parents[2] / '.caprmedio_tmp' / 'CA-P-2791' / 'CA-P-2934' / 'exact-carrier'
        scratch.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.control = self.root / '.caprmedio_test'
        self.control.mkdir()
        (self.control / 'caprmedio_project_settings.toml').write_text('[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n[paths]\ncontrol_root=".caprmedio_test"\n')
        write_scope_unit_declarations(self.root, control_root=self.control)
        self.folder = self.control / '04_requirement'
        self.folder.mkdir(exist_ok=True)
        self.selection = resolve_project(self.root)

    def carrier(self, name, *, identity='CA-R-10', version=1, status='Active', grouped=False, projection=False, folder=None):
        folder = folder or self.folder
        folder.mkdir(parents=True, exist_ok=True)
        if grouped:
            header = f'identity:\n  id: {identity}\nstate:\n  version: {version}\n  status: {status}\n'
        else:
            header = f'atom_id: {identity}\nversion: {version}\nstatus: {status}\n'
        if projection:
            header += 'projection: {}\n'
        path = folder / name
        path.write_text(f'---\n{header}---\n\n## Summary\n\nExample\n')
        return path

    def test_current_and_pinned_state(self):
        path = self.carrier('CA-R-10-example.md', grouped=True, version=2)
        with patch.object(source_module, 'read_scope_unit_declarations', wraps=source_module.read_scope_unit_declarations) as declarations:
            pin = select_source(self.selection, 'CA-R-10')
        self.assertEqual(declarations.call_count, 1)
        self.assertEqual((pin.path, pin.version, pin.sha256), (path, 2, hashlib.sha256(path.read_bytes()).hexdigest()))
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10', expected_version=1)

    def test_draft_and_archived(self):
        self.carrier('CA-R-10@2-draft-example.md', version=2, status='draft')
        self.carrier('CA-R-10-example@1.md', version=1, status='Archived', grouped=True)
        self.assertEqual(select_source(self.selection, 'CA-R-10@2-draft').version, 2)
        self.assertEqual(select_source(self.selection, 'CA-R-10@1').status, 'Archived')
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10')

    def test_ambiguity_projection_and_wrong_carrier(self):
        self.carrier('CA-R-10-first.md')
        self.carrier('CA-R-10-projection.md', projection=True)
        self.carrier('CA-R-10-copy.md', folder=self.root / 'delivery')
        self.assertEqual(select_source(self.selection, 'CA-R-10').path.name, 'CA-R-10-first.md')
        second = self.carrier('CA-R-10-second.md')
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10')
        second.unlink()
        self.carrier('CA-R-10-wrong.md', identity='CA-R-11')
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10')

    def test_project_prefix_and_root_local_authority(self):
        settings = self.control / 'caprmedio_project_settings.toml'
        settings.write_text(settings.read_text().replace('project_prefix="CA"', 'project_prefix="DEMO"'))
        selection = resolve_project(self.root)
        path = self.carrier('DEMO-R-10-goal.md', identity='DEMO-R-10', folder=self.control)
        self.assertEqual(select_source(selection, 'DEMO-R-10').path, path)
        archived = self.carrier('DEMO-R-10@1-goal.md', identity='DEMO-R-10', status='archived', folder=self.folder / 'archive')
        draft = self.carrier('DEMO-R-10@2-draft-goal.md', identity='DEMO-R-10', status='draft', version=2, folder=self.folder / 'draft')
        self.assertEqual(select_source(selection, 'DEMO-R-10@1').path, archived)
        self.assertEqual(select_source(selection, 'DEMO-R-10@2-draft').path, draft)
        with self.assertRaises(SourceSelectionError):
            select_source(selection, 'CA-R-10')

    def test_grouped_and_separately_placed_workflow_steps(self):
        operations = self.control / '09_operations'
        workflow = operations / 'CA-O-20-workflow'
        grouped = self.carrier('CA-O-21-step.md', identity='CA-O-21', folder=workflow, grouped=True)
        standalone = self.carrier('CA-O-22-step.md', identity='CA-O-22', folder=operations)
        self.assertEqual(select_source(self.selection, 'CA-O-21').path, grouped)
        self.assertEqual(select_source(self.selection, 'CA-O-22').path, standalone)

    def test_currentness_is_scoped_to_identity(self):
        selected = self.carrier('CA-R-10-first.md')
        other = self.carrier('CA-R-11-before.md', identity='CA-R-11')
        original = source_module.parse_carrier
        def rename_unrelated(raw, path):
            other.rename(other.with_name('CA-R-11-after.md'))
            return original(raw, path)
        with patch.object(source_module, 'parse_carrier', side_effect=rename_unrelated):
            self.assertEqual(select_source(self.selection, 'CA-R-10').path, selected)

        def add_duplicate(raw, path):
            self.carrier('CA-R-10-second.md')
            return original(raw, path)
        with patch.object(source_module, 'parse_carrier', side_effect=add_duplicate):
            with self.assertRaises(SourceSelectionError):
                select_source(self.selection, 'CA-R-10')

    def test_batch_current_sources_rechecks_all_candidates(self):
        first = self.carrier('CA-R-10-first.md')
        second = self.carrier('CA-R-11-first.md', identity='CA-R-11')
        with patch.object(source_module, '_inventory_paths', wraps=source_module._inventory_paths) as inventory:
            pins = source_module.select_current_sources(self.selection, ['CA-R-10', 'CA-R-11'])
        self.assertEqual({key: pin.path for key, pin in pins.items()}, {'CA-R-10': first, 'CA-R-11': second})
        self.assertEqual(inventory.call_count, 2)
        with self.assertRaisesRegex(SourceSelectionError, 'missing or ambiguous'):
            source_module.select_current_sources(self.selection, ['CA-R-10', 'CA-R-12'])
        with self.assertRaises(SourceSelectionError):
            source_module.select_current_sources(self.selection, ['CA-R-10@1'])
        original = source_module.parse_carrier

        def add_duplicate(raw, path):
            if path == second:
                self.carrier('CA-R-10-second.md')
            return original(raw, path)

        with patch.object(source_module, 'parse_carrier', side_effect=add_duplicate):
            with self.assertRaisesRegex(SourceSelectionError, 'candidates changed'):
                source_module.select_current_sources(self.selection, ['CA-R-10', 'CA-R-11'])

    def test_batch_selects_draft_and_archived_revisions_with_one_inventory(self):
        archived = self.carrier('CA-R-10@1-example.md', status='Archived')
        draft = self.carrier('CA-R-10@2-draft-example.md', version=2, status='Draft')
        with patch.object(source_module, '_inventory_paths', wraps=source_module._inventory_paths) as inventory:
            pins = source_module.select_sources(self.selection, ['CA-R-10@1', 'CA-R-10@2-draft'])
        self.assertEqual(inventory.call_count, 2)
        self.assertEqual(pins['CA-R-10@1'].path, archived)
        self.assertEqual(pins['CA-R-10@2-draft'].path, draft)
        self.carrier('CA-R-10@2-draft-other.md', version=2, status='Draft')
        with self.assertRaisesRegex(SourceSelectionError, 'missing or ambiguous'):
            source_module.select_sources(self.selection, ['CA-R-10@1', 'CA-R-10@2-draft'])

    def test_symlinked_role_directory_fails_closed(self):
        self.carrier('CA-R-10-first.md')
        (self.folder / 'linked').symlink_to(self.root, target_is_directory=True)
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10')

    def test_invalid_version_and_changed_declaration(self):
        self.carrier('CA-R-10@2-draft-example.md', version=3, status='draft')
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10@2-draft')
        self.selection.declaration_paths[0].write_text('changed')
        with self.assertRaises(SourceSelectionError):
            select_source(self.selection, 'CA-R-10')

    def test_declaration_changed_during_discovery_is_rejected(self):
        self.carrier('CA-R-10-first.md')
        original = source_module.parse_carrier

        def change_declaration(raw, path):
            self.selection.declaration_paths[0].write_text('changed')
            return original(raw, path)

        with patch.object(source_module, 'parse_carrier', side_effect=change_declaration):
            with self.assertRaises(SourceSelectionError):
                select_source(self.selection, 'CA-R-10')


if __name__ == '__main__':
    unittest.main()
