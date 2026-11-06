"""Real nested carrier admission, exact predecessor preservation and read-only reports."""

from __future__ import annotations

import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path
import unittest

from test_nested_header_validation import HEADER, ENCODING, text_of
from header_groups import nested_header
from project_selection import bind_selection
from validate_atoms_workers.authority import AuthorityContext
from validate_atoms_workers.parsing import parse_carrier
from validate_atoms_workers.read_io import ReadContext
from validate_atoms_workers.settings import CEILINGS
from validate_atoms_workers.assessment import apply_checks, read_candidate
from validate_atoms_workers.context import load_source
from validate_atoms_workers.reference_context import references
from validate_atoms_workers.selection import matching_selectors, status_filter
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission
import test_proposed_carrier_admission_regressions as projects
from test_current_type_admission import role_declarations, fresh_owner


class NestedHeaderFunctionalTests(unittest.TestCase):
    def setUp(self):
        self.fixture = projects.ProposedCarrierAdmissionRegressions('runTest')
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.project()
        self.root = self.selection.root
        self.core = self.root / next(Path(r['authority_path']) for r in self.selection.structure['scope_units']
                                     if r['scope_unit_name'] == 'CORE_META_MODEL')
        (self.core / '07_delivery/CA-D-657.md').write_text(ENCODING.read_text())
        requirements = self.core / '04_requirement'
        for source in [*role_declarations(), fresh_owner('CA-R-55555', 'Plan', 'Plan')]:
            (requirements / (source['binding']['atom_id'] + '--authority.md')).write_text(source['text'])
        # Exercise the complete source binding/status/locator closure on nested authority bytes.
        for source_path in self.core.rglob('*.md'):
            parsed = parse_carrier(source_path.read_bytes(), source_path)
            source_path.write_text(text_of(nested_header(parsed.metadata), parsed.body))
        self.metadata = copy.deepcopy(HEADER)
        unit = next(r for r in self.selection.structure['scope_units'] if r['scope_unit_name'] == 'CORE_META_MODEL')
        self.metadata['context']['container']['scope_unit'] = unit['scope_unit_id']
        self.relative = self.core.relative_to(self.selection.control_root) / '03_plan/CA-P-701--nested-plan.md'
        self.path = self.selection.control_root / self.relative
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.metadata['destination']['file']['path'] = self.path.parent.relative_to(self.root).as_posix()

    def context(self):
        with bind_selection(self.selection):
            return admission.source_context_from_project(self.root)

    def validate(self, metadata=None, predecessor=None):
        with bind_selection(self.selection):
            return admission.validate_proposed_carrier(
                self.metadata if metadata is None else metadata, projects.PLAN_BODY, self.context(), self.relative,
                allow_existing_relations=True, predecessor=predecessor)

    def test_complete_nested_admission_keeps_entire_frontier_unchanged(self):
        before = projects.snapshot(self.root)
        self.validate()
        self.assertEqual(before, projects.snapshot(self.root))

    def test_semantic_selection_binding_reference_and_report_identity(self):
        self.path.write_text(text_of(self.metadata))
        reader = ReadContext([str(self.root)], dict(CEILINGS))
        parsed, view = read_candidate(reader, self.path)
        self.assertEqual([0], matching_selectors(str(self.path), view, [{'atom_id': 'CA-P-701', 'version': 1}]))
        self.assertEqual(('selected', ''), status_filter(view, {'statuses': ['Active']}, {'Plan': ['Active']}))
        source_path = self.core / '07_delivery/CA-D-657.md'
        source = load_source(source_path, None, reader, {'coverage': {'gaps': []}})
        self.assertEqual('CA-D-657', source['binding']['atom_id'])
        refs, complete = references({'reference_roots': [str(self.path.parent)]}, reader, [], [])
        self.assertTrue(complete)
        self.assertEqual('CA-P-701', refs[0]['metadata']['atom_id'])
        context = AuthorityContext([], 0, 0, 0, [], (), {}, False)
        report = {'carriers': [], 'findings': [], 'coverage': {'gaps': []}}
        apply_checks(self.path, parsed, context, reader, report)
        self.assertEqual('CA-P-701', report['carriers'][0]['atom_id'])
        self.assertEqual(1, report['carriers'][0]['version'])
        self.assertEqual(self.metadata, parsed.metadata)

    def test_preserved_residue_requires_exact_live_predecessor_and_cannot_change(self):
        self.metadata['priority'] = 'high'
        self.metadata['legacy_unmapped'] = {'flag': False, 'count': 0}
        self.path.write_text(text_of(self.metadata))
        predecessor = admission.CarrierPredecessor(self.path, hashlib.sha256(self.path.read_bytes()).hexdigest())
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate()
        self.validate(predecessor=predecessor)
        changed = copy.deepcopy(self.metadata)
        changed['legacy_unmapped']['count'] = True
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate(changed, predecessor)
        changed = copy.deepcopy(self.metadata)
        changed.pop('legacy_unmapped')
        with self.assertRaisesRegex(admission.ProposedCarrierError, 'changed or disappeared'):
            self.validate(changed, predecessor)
        changed = copy.deepcopy(self.metadata)
        changed['new_unadmitted_field'] = 1
        with self.assertRaises(admission.ProposedCarrierError):
            self.validate(changed, predecessor)
        self.path.write_text(self.path.read_text() + '\nChanged predecessor.\n')
        with self.assertRaisesRegex(admission.ProposedCarrierError, 'predecessor changed'):
            self.validate(predecessor=predecessor)

    def test_public_command_nested_identity_golden_spine_is_read_only(self):
        self.path.write_text(text_of(self.metadata))
        request = {
            "schema_version": 1, "source_roots": [str(self.path.parent)],
            "allowed_read_roots": [str(self.root)],
            "methodology": {"kind": "sources", "roots": [str(self.core)]},
            "selection": {"atoms": [{"atom_id": "CA-P-701", "version": 1}], "statuses": "all"},
            "limits": dict(CEILINGS),
        }
        before = projects.snapshot(self.root)
        command = Path(__file__).resolve().parents[1] / 'validate_atoms.py'
        result = subprocess.run([sys.executable, '-B', str(command), '--input', '-'],
                                input=json.dumps(request), text=True, capture_output=True, timeout=30)
        self.assertEqual('', result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual('incomplete', report['result'])
        self.assertEqual(2, result.returncode)
        self.assertEqual([], report['selection']['unresolved'])
        self.assertEqual([('CA-P-701', 1, 'source')],
                         [(r['atom_id'], r['version'], r['representation']) for r in report['carriers']])
        self.assertEqual('unchanged', report['currentness']['state'])
        self.assertEqual(before, projects.snapshot(self.root))


if __name__ == '__main__':
    unittest.main()
