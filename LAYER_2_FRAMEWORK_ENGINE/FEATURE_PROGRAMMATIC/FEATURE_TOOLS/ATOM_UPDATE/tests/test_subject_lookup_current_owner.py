"""Subject lookup binds Current containment without rewriting carriers."""
from __future__ import annotations

import argparse
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))
import test_nonarchived_subject_preview as fixtures  # noqa: E402
from atom_subject_lookup import run_subject_search  # noqa: E402


class SubjectLookupOwnerTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName='runTest')
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan('Active')

    def search(self):
        return run_subject_search(self.root, argparse.Namespace(subject='Atom/Status', content_role=['Plan']))

    def test_current_containment_without_legacy_scope(self):
        before = self.path.read_bytes()
        self.assertNotIn(b'current_scope_unit:', before)
        result = self.search()
        self.assertEqual(['CA-P-501'], [row['atom_id'] for row in result['occurrences']])
        self.assertEqual('full', result['coverage'])
        self.assertEqual(before, self.path.read_bytes())

    def test_missing_current_containment_is_limited(self):
        raw = self.path.read_bytes()
        raw = raw.replace(b'  IS_CONTAINED_BY:\r\n    scope_unit:', b'  OTHER:\r\n    scope_unit:')
        self.path.write_bytes(raw)
        result = self.search()
        self.assertFalse(result['occurrences'])
        self.assertEqual('limited', result['coverage'])
        self.assertTrue(any('owner is unresolved' in row['message'] for row in result['diagnostics']))

    def test_current_authority_context_is_loaded_once(self):
        from VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier import source_context_from_project
        self.fixture._plan('Active', number=502)
        with patch('VALIDATE_ATOMS.validate_atoms_workers.proposed_carrier.source_context_from_project',
                   wraps=source_context_from_project) as load:
            result = self.search()
        self.assertEqual(2, len(result['occurrences']))
        load.assert_called_once()

    def test_current_legacy_scope_cannot_replace_missing_containment(self):
        raw = self.path.read_bytes().replace(b'role: Plan\r\n', b'current_scope_unit: LIFECYCLE_FIXTURE\r\nrole: Plan\r\n')
        raw = raw.replace(b'  IS_CONTAINED_BY:\r\n    scope_unit:', b'  OTHER:\r\n    scope_unit:')
        self.path.write_bytes(raw)
        result = self.search()
        self.assertFalse(result['occurrences'])
        self.assertEqual('limited', result['coverage'])

    def test_conflicting_subject_aliases_are_limited(self):
        raw = self.path.read_bytes().replace(b'  active: "Atom/Status"\r\n',
                                             b'  active: "Atom/Status"\r\n  governs: Other\r\n')
        self.path.write_bytes(raw)
        result = self.search()
        self.assertFalse(result['occurrences'])
        self.assertEqual('limited', result['coverage'])
        self.assertTrue(any(row['code'] == 'source-invalid' for row in result['diagnostics']))

    def test_explicit_legacy_authority_uses_legacy_scope(self):
        owner = self.fixture.fixture.declarations[fixtures.lifecycle_fixture._FIXTURE_SCOPE]['scope_unit_name']
        raw = self.path.read_bytes().replace(b'role: Plan\r\n', f'current_scope_unit: {owner}\r\nrole: Plan\r\n'.encode())
        self.path.write_bytes(raw)
        reader = SimpleNamespace(currentness=lambda: {'state': 'unchanged'})
        context = SimpleNamespace(inputs={'sources': [{'binding': {'atom_id': 'CA-D-276'}}]}, _reader=reader)
        module = 'VALIDATE_ATOMS.validate_atoms_workers.'
        with patch(module + 'proposed_carrier.source_context_from_project', return_value=context), \
             patch(module + 'check_fields.reviewed_encoding_profile', return_value='legacy'):
            result = self.search()
        self.assertEqual(['CA-P-501'], [row['atom_id'] for row in result['occurrences']])
        self.assertEqual('full', result['coverage'])


if __name__ == '__main__':
    unittest.main()
