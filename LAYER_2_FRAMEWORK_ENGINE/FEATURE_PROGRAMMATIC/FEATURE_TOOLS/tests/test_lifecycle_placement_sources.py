"""The build selector uses Workbench and the compiler verifies its pins."""
from pathlib import Path
import json
import re
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from ATOM_LIFECYCLE.candidate_schema import compile_candidate_schema  # noqa: E402
from ATOM_LIFECYCLE.placement_sources import bootstrap_rows, inventory, pin, query_pins, read_selected, validate_selection  # noqa: E402
from test_lifecycle_formal_placement import RULES, carrier  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.query_store import QueryStore  # noqa: E402

ROOT = Path(__file__).resolve().parents[4]


class PlacementSourcesTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'CA-R-1.md').write_text(carrier('CA-R-1', 'Requirement', 'Active', '''## Claim
### Formal Claim
```CFEL
Atom.Header.Role :: Plan;
Atom.Header.Form :: Plan;
Atom.Header.ID:: [atom id]{::1};
Atom.Content.Summary:: {::1};
```
'''))
        self.delivery = self.root / 'CA-D-1.md'
        self.delivery.write_text(carrier('CA-D-1', 'Delivery', 'Active',
            '## Claim\n### Formal Claim\n```CFEL\n' + RULES + '\n```',
            'CAPRMEDIO_MODEL <+ Carrier'))
        (self.root / 'CA-D-2.md').write_text(carrier('CA-D-2', 'Delivery', 'Active',
            'irrelevant', 'CAPRMEDIO_MODEL <+ Other'))
        self.manifest = self.root.parent / (self.root.name + '-selection.json')
        self.addCleanup(self.manifest.unlink, missing_ok=True)

    def test_real_workbench_query_selects_and_compiles(self):
        extension = ROOT / '.caprmedio_tmp/workbench/extensions'
        queries = []

        class TracedStore(QueryStore):
            def __init__(self):
                super().__init__(extension_directory=extension)

            def run(self, sql, *args, **kwargs):
                queries.append(sql)
                return super().run(sql, *args, **kwargs)

        selected = query_pins(self.root, TracedStore)
        self.assertEqual([pin(row) for row in bootstrap_rows(inventory(self.root))], selected)
        self.assertEqual(1, len(queries))
        self.assertIn('FROM atoms', queries[0])
        self.manifest.write_text(json.dumps(selected))
        self.assertEqual(compile_candidate_schema(self.root),
                         compile_candidate_schema(self.root, self.manifest))

    def test_requirement_query_selects_role_and_subject_pins(self):
        (self.root / 'CA-R-1.md').write_text(carrier(
            'CA-R-1', 'Requirement', 'Active', 'body', 'Atom.Header.Status'))
        (self.root / 'CA-R-2.md').write_text(carrier(
            'CA-R-2', 'Requirement', 'Active', 'body', 'Atom.Content.Other'))
        extension = ROOT / '.caprmedio_tmp/workbench/extensions'

        class LocalStore(QueryStore):
            def __init__(self):
                super().__init__(extension_directory=extension)

        selected = query_pins(self.root, LocalStore, role='Requirement',
                              subject_pattern=re.compile(r'Atom\.Header\..*'))
        self.assertEqual([pin(inventory(self.root, 'R')[0])], selected)
        self.assertEqual('CA-R-1.md', selected[0]['source_path'])
        self.assertEqual(64, len(selected[0]['sha256']))
        pattern = re.compile(r'Atom\.Header\..*')
        self.assertEqual('CA-R-1', read_selected(
            self.root, selected, role='Requirement', subject_pattern=pattern)[0]['id'])
        (self.root / 'CA-R-1.md').write_text((self.root / 'CA-R-1.md').read_text() + 'changed')
        with self.assertRaises(ValueError):
            read_selected(self.root, selected, role='Requirement', subject_pattern=pattern)

    def test_compiler_reads_selected_delivery_only(self):
        selected = [pin(row) for row in bootstrap_rows(inventory(self.root))]
        self.manifest.write_text(json.dumps(selected))
        real_read = Path.read_bytes
        read_paths = []

        def observed_read(path):
            read_paths.append(path)
            return real_read(path)

        with patch.object(Path, 'read_bytes', observed_read):
            compile_candidate_schema(self.root, self.manifest)
        self.assertIn(self.delivery, read_paths)
        self.assertNotIn(self.root / 'CA-D-2.md', read_paths)

    def test_selector_still_rejects_incomplete_selection(self):
        with self.assertRaisesRegex(ValueError, 'all eligible'):
            validate_selection(inventory(self.root), [])

    def test_empty_selection_is_valid_for_minimal_model_without_placement(self):
        self.delivery.unlink()
        self.manifest.write_text('[]')
        self.assertNotIn('placement', json.loads(compile_candidate_schema(self.root, self.manifest)))

    def test_stale_missing_duplicate_and_unrelated_pins_fail(self):
        selected = [pin(row) for row in bootstrap_rows(inventory(self.root))]
        cases = [selected + selected, [{**selected[0], 'sha256': '0' * 64}],
                 [{**selected[0], 'version': 2}], [{**selected[0], 'id': 'CA-D-2'}],
                 [{**selected[0], 'source_path': '../CA-D-1.md'}],
                 [pin(row) for row in inventory(self.root)]]
        for case in cases:
            with self.subTest(case=case):
                self.manifest.write_text(json.dumps(case))
                with self.assertRaises(ValueError):
                    compile_candidate_schema(self.root, self.manifest)
        self.manifest.write_text(json.dumps(selected))
        self.delivery.write_text(self.delivery.read_text() + '\nchanged\n')
        with self.assertRaises(ValueError):
            compile_candidate_schema(self.root, self.manifest)


if __name__ == '__main__':
    unittest.main()
