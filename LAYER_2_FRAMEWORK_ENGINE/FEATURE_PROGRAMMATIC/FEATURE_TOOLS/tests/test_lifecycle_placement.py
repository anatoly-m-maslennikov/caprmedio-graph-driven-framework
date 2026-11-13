from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.placement import derive_destination, PlacementError  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
from lifecycle_placement_test_support import bind_placement, fixture_rules  # noqa: E402


class PlacementTest(unittest.TestCase):
    def setUp(self):
        binding = bind_placement(fixture_rules())
        binding.__enter__()
        self.addCleanup(binding.__exit__, None, None, None)
        scratch = TOOLS.parents[2] / '.caprmedio_tmp/CA-P-2791/CA-P-2934/placement'
        scratch.mkdir(parents=True, exist_ok=True)
        self.tmp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.control = self.root / '.caprmedio_test'
        self.control.mkdir()
        (self.control / 'caprmedio_project_settings.toml').write_text('[project]\nname="TEST"\n[artifacts.identity]\nproject_prefix="CA"\n[paths]\ncontrol_root=".caprmedio_test"\n')
        self.units = write_scope_unit_declarations(self.root, control_root=self.control, rows=[{'scope_unit_name': 'OTHER', 'atom_id': 'CA-R-990001', 'scope_unit_id': 'CA-SU-1'}])
        self.selection = resolve_project(self.root)

    def place(self, **kwargs):
        args = dict(atom_id='CA-R-1', version=2, status='Active', role='Requirement', summary='Example text', scope_unit='TEST', form='Decision', tier=3)
        args.update(kwargs)
        return derive_destination(self.selection, **args)

    def test_current_draft_and_destination_scope(self):
        self.assertEqual(self.place(), self.control / '04_requirement/CA-R-1-DECISION--example-text.md')
        other = next(x for x in self.selection.structure['scope_units'] if x['scope_unit_name'] == 'OTHER')
        self.assertEqual(self.place(status='Draft', scope_unit='OTHER'), self.root / other['authority_path'] / '04_requirement/draft/CA-R-1@2-draft-OTHER-DECISION--example-text.md')
        self.assertIn('SCOPE_CONTRACT', self.place(tier=0).name)

    def test_leading_zero_identity_is_preserved(self):
        self.assertEqual('CA-R-096@2-draft-DECISION--example-text.md',
                         self.place(atom_id='CA-R-096', status='Draft').name)
        self.assertEqual('CA-R-000-DECISION--example-text.md', self.place(atom_id='CA-R-000').name)

    def test_effective_label_falls_back_to_form_for_empty_values(self):
        for label in (None, ''):
            with self.subTest(label=label):
                self.assertEqual(self.place(), self.place(label=label))
                self.assertEqual(
                    'CA-P-1-TASK--example-text.md',
                    self.place(atom_id='CA-P-1', role='Plan', form='Task', label=label).name,
                )
        self.assertEqual('CA-R-1-LOCAL--example-text.md', self.place(label='Local').name)
        with self.assertRaises(PlacementError):
            self.place(label=' ')

    def test_summary_punctuation_serializes_to_ascii_kebab_case(self):
        summaries = {
            'Deliver DuckDB Atom, Content Property, and relation records':
                'deliver-duckdb-atom-content-property-and-relation-records',
            'Preserve governed Atom data and reuse native SQL.':
                'preserve-governed-atom-data-and-reuse-native-sql',
            'Verify installed Workbench and query_run':
                'verify-installed-workbench-and-query-run',
            'hello / world': 'hello-world',
            "Follow the Operator's priorities": 'follow-the-operator-s-priorities',
        }
        for summary, slug in summaries.items():
            with self.subTest(summary=summary):
                self.assertEqual(f'CA-R-1-DECISION--{slug}.md', self.place(summary=summary).name)
                self.assertEqual(f'CA-R-1@2-draft-DECISION--{slug}.md',
                                 self.place(summary=summary, status='Draft').name)

    def test_archive_exact_predecessor_and_local_workflow_group(self):
        role = self.control / '09_operations'
        group = role / 'CA-O-9-WORKFLOW--example'
        group.mkdir(parents=True)
        old = group / 'CA-O-10-OLD-STEP--legacy-name.md'
        old.write_text('---\natom_id: CA-O-10\nversion: 2\nstatus: Active\n---\n')
        result = self.place(atom_id='CA-O-10', role='Operations', status='Archived', parent=group, source_path=old)
        self.assertEqual(result, role / 'archived/CA-O-10@2-OLD-STEP--legacy-name.md')
        with self.assertRaises(PlacementError):
            self.place(atom_id='CA-O-10', role='Operations', status='Archived', source_path=old)

    def test_workflow_step_current_and_draft_placement(self):
        role = self.control / '09_operations'
        group = role / 'CA-O-9-WORKFLOW--example'
        group.mkdir(parents=True)
        args = dict(atom_id='CA-O-10', role='Operations', form='Step', parent=group)
        self.assertEqual(self.place(**args), group / 'CA-O-10-STEP--example-text.md')
        self.assertEqual(self.place(**args, status='Draft'), role / 'draft/CA-O-10@2-draft-STEP--example-text.md')

    def test_archived_update_uses_shared_role_folder(self):
        self.assertEqual(self.place(status='Archived', archived_update=True),
                         self.control / '04_requirement/archived/CA-R-1@2-DECISION--example-text.md')
        self.assertEqual(self.place(atom_id='CA-P-10', role='Plan', form='Task', status='Archived', archived_update=True),
                         self.control / '03_plan/archived/CA-P-10@2-TASK--example-text.md')

    def test_plan_locations(self):
        parent = self.control / '03_plan/CA-P-9-EPIC--parent'
        parent.mkdir(parents=True)
        args = dict(atom_id='CA-P-10', role='Plan', form='Task', parent=parent)
        self.assertEqual(self.place(**args, status='Done'), parent / 'done/CA-P-10-TASK--example-text.md')
        self.assertEqual(self.place(**args, status='Draft'), self.control / '03_plan/draft/CA-P-10@2-draft-TASK--example-text.md')
        old = parent / 'CA-P-10-TASK--example-text.md'
        old.write_text('---\natom_id: CA-P-10\nversion: 2\nstatus: Active\n---\n')
        self.assertEqual(self.place(**args, status='Archived', source_path=old), self.control / '03_plan/archived/CA-P-10@2-TASK--example-text.md')
        self.assertEqual(self.place(atom_id='CA-P-10', role='Plan', form='Task', status='Done'),
                         self.control / '03_plan/done/CA-P-10-TASK--example-text.md')

    def test_project_scope_id_and_archive_current_status(self):
        self.assertEqual(self.place(scope_unit='CA-SU-00'), self.place(scope_unit='TEST'))
        concern = self.control / '01_concern/resolved/CA-C-20-QUESTION--old.md'
        concern.parent.mkdir(parents=True)
        concern.write_text('---\natom_id: CA-C-20\nversion: 2\nstatus: Resolved\n---\n')
        self.assertEqual(self.place(atom_id='CA-C-20', role='Concern', status='Archived', source_path=concern),
                         self.control / '01_concern/archived/CA-C-20@2-QUESTION--old.md')
        concern.write_text('---\natom_id: CA-C-20\nversion: 2\nstatus: Active\n---\n')
        with self.assertRaises(PlacementError):
            self.place(atom_id='CA-C-20', role='Concern', status='Archived', source_path=concern)
        parent = self.control / '03_plan/CA-P-9-EPIC--parent'
        old = parent / 'done/CA-P-10-TASK--child.md'
        old.parent.mkdir(parents=True)
        old.write_text('---\natom_id: CA-P-10\nversion: 2\nstatus: Done\n---\n')
        self.assertEqual(self.place(atom_id='CA-P-10', role='Plan', status='Archived', parent=parent, source_path=old),
                         self.control / '03_plan/archived/CA-P-10@2-TASK--child.md')

    def test_refuses_unsafe_and_stale(self):
        with self.assertRaises(PlacementError):
            self.place(scope_unit='missing')
        with self.assertRaises(PlacementError):
            self.place(summary='hello\nworld')
        with self.assertRaises(PlacementError):
            self.place(summary='!!!')
        with self.assertRaises(PlacementError):
            self.place(parent=self.root / 'outside')
        self.selection.declaration_paths[0].write_text('changed')
        with self.assertRaises(PlacementError):
            self.place()


if __name__ == '__main__':
    unittest.main()
