from pathlib import Path
import hashlib
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
APP_TESTS = TOOLS.parent / "FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/tests"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(APP_TESTS))

from atom_operations import ToolError, frontmatter_scalar
from carrier_aliases import carrier_read_view
from connector_atom_parse import parse_atom
from VALIDATE_ATOMS.validate_atoms_workers.parsing import CarrierError, parse_carrier
from frozen_selected_workflows import frozen_complete_carrier_authority, frozen_graph_authority, frozen_source_bytes


class CarrierAliasesTests(unittest.TestCase):
    def carrier(self, fields):
        return ("---\natom_id: CA-R-123\nversion: 1\nstatus: Active\n"
                "current_scope_unit: CORE_META_MODEL\nupdated_at: '2026-01-01'\n" + fields + "\n---\n# Summary\nExample\n").encode()

    def test_legacy_new_and_equal_mixed(self):
        old = "content_role: Requirement\ntype: Rule\nsubjects:\n  governs: Node\n  depends_on: [Property]"
        new = "role: Requirement\nform: Rule\nsubjects:\n  active: Node\n  passive: [Property]"
        mixed = ("content_role: Requirement\nrole: Requirement\ntype: Rule\nform: Rule\n"
                 "subjects:\n  governs: Node\n  active: Node\n  depends_on: [Property]\n  passive: [Property]")
        for fields in (old, new, mixed):
            with self.subTest(fields=fields):
                raw = self.carrier(fields)
                parsed = parse_carrier(raw, Path('example.md'))
                actual = parse_atom(raw)
                view = carrier_read_view(actual.metadata)
                self.assertEqual(view['content_role'], 'Requirement')
                self.assertEqual(view['type'], 'Rule')
                self.assertEqual(view['subjects']['governs'], 'Node')
                self.assertEqual(view['subjects']['depends_on'], ['Property'])
                self.assertEqual(actual.metadata, parsed.metadata)
                self.assertEqual(parsed.text.encode(), raw)
                if fields == new:
                    self.assertNotIn('content_role', parsed.metadata)
                    self.assertNotIn('governs', parsed.metadata['subjects'])
                self.assertEqual(frontmatter_scalar(parsed.frontmatter, 'content_role'), 'Requirement')
                self.assertEqual(frontmatter_scalar(parsed.frontmatter, 'type'), 'Rule')

    def test_canonical_carrier_does_not_require_legacy_location_or_form(self):
        raw = (
            "---\natom_id: CA-A-335\nversion: 1\nstatus: Active\nupdated_at: '2026-01-01'\n"
            "role: Analysis & Advisory\nsubjects:\n  active: Scope Unit//CORE\n---\n# Summary\nExample\n"
        ).encode()
        parsed = parse_atom(raw)
        self.assertEqual("Analysis & Advisory", carrier_read_view(parsed.metadata)["content_role"])

    def test_legacy_analysis_role_remains_readable(self):
        raw = (
            "---\natom_id: CA-A-336\nversion: 1\nstatus: Active\nupdated_at: '2026-01-01'\n"
            "content_role: Analysis\nsubjects:\n  governs: Scope Unit//CORE\n---\n# Summary\nExample\n"
        ).encode()
        self.assertEqual("Analysis", carrier_read_view(parse_atom(raw).metadata)["content_role"])

    def test_each_conflicting_pair_rejected(self):
        base = {'content_role': 'Requirement', 'role': 'Method', 'type': 'Rule',
                'subjects': {'governs': 'Node', 'depends_on': []}}
        conflicts = [base, {'type': 'Rule', 'form': 'Goal'},
                     {'subjects': {'governs': 'Node', 'active': 'Property'}},
                     {'subjects': {'depends_on': ['Node'], 'passive': ['Property']}}]
        for metadata in conflicts:
            with self.subTest(metadata=metadata), self.assertRaises(ValueError):
                carrier_read_view(metadata)
        fields = 'content_role: Requirement\nrole: Method\ntype: Rule\nsubjects: {governs: Node}'
        with self.assertRaises(CarrierError) as cm:
            parse_carrier(self.carrier(fields), Path('example.md'))
        self.assertEqual(cm.exception.code, 'CARRIER_ALIAS_CONFLICT')
        with self.assertRaises(ToolError):
            frontmatter_scalar(fields, 'content_role')
        for fields in ('type: Rule\nform: Goal', 'subjects: {governs: Node, active: Property}',
                       'subjects: {depends_on: [Node], passive: [Property]}'):
            with self.subTest(fields=fields), self.assertRaises(CarrierError) as error:
                parse_carrier(self.carrier(fields), Path('example.md'))
            self.assertEqual(error.exception.code, 'CARRIER_ALIAS_CONFLICT')

    def test_frozen_source_pins_match_exact_corpus_bytes(self):
        for name, entries, identities in (
            ('complete', frozen_complete_carrier_authority(), ('CA-D-269', 'CA-D-274', 'CA-R-1283')),
            ('graph', frozen_graph_authority(), ('CA-D-269',)),
        ):
            for identity in identities:
                with self.subTest(name=name, identity=identity):
                    entry = entries[identity]
                    raw = frozen_source_bytes(entry['source_path'], entry['sha256'])
                    parsed = parse_carrier(raw, Path(entry['source_path']))
                    self.assertEqual(parsed.metadata['atom_id'], identity)
                    self.assertEqual(parsed.metadata['version'], entry['version'])
                    self.assertEqual(hashlib.sha256(raw).hexdigest(), entry['sha256'])

    def test_subject_authority_still_rejects_new_authored_keys(self):
        from VALIDATE_ATOMS.validate_atoms_workers.check_fields import _subjects
        class Check:
            def __init__(self): self.failures = []
            def require(self, mapping, key, predicate):
                if key not in mapping or not predicate(mapping[key]): self.failures.append(key)
            def fail(self, code, field, message): self.failures.append(field)
            def gap(self, field, message): self.failures.append(field)
        old, new = Check(), Check()
        _subjects({'subjects': {'governs': 'Node', 'depends_on': []}}, '', old)
        _subjects({'subjects': {'active': 'Node', 'passive': []}}, '', new)
        self.assertEqual(old.failures, [])
        self.assertIn('subjects', new.failures)

    def test_equal_alias_check_is_type_sensitive_and_does_not_mutate(self):
        value = {'subjects': {'governs': 'Node', 'active': 'Node'}}
        view = carrier_read_view(value)
        self.assertIsNot(view['subjects'], value['subjects'])
        self.assertEqual(value, {'subjects': {'governs': 'Node', 'active': 'Node'}})
        with self.assertRaises(ValueError):
            carrier_read_view({'subjects': {'depends_on': [True], 'passive': [1]}})
