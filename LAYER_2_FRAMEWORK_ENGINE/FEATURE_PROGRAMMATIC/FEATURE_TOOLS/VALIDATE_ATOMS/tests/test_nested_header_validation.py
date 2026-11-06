"""Independent nested Header controls; the retained flat golden corpus is untouched."""

from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest

import yaml

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parents[1]), str(HERE.parent), str(HERE)]

from carrier_aliases import carrier_read_view  # noqa: E402
from header_groups import nested_header  # noqa: E402
from validate_atoms_workers.authority import AuthorityContext, Obligation, current_role_declaration  # noqa: E402
from validate_atoms_workers.check_fields import _common, _subjects, reviewed_encoding_profile  # noqa: E402
from validate_atoms_workers.check_schema_extended import ADAPTERS, type_definition_coordinate  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from validate_atoms_workers.parsing import CarrierError, parse_carrier  # noqa: E402
import test_proposed_carrier_admission_regressions as projects  # noqa: E402
from test_current_type_admission import role_declarations  # noqa: E402


ENCODING = HERE / 'fixtures/nested_encoding_d657_reviewed.md'
HEADER = {
    'identity': {'atom_id': 'CA-P-701', 'ref_id': 'CA-P-701'},
    'context': {'container': {'scope_unit': 'CA-SU-1'}, 'role': 'Plan', 'form': 'Plan',
                'topics': {'main_subject': 'Tool', 'dependencies': ['Plan']}, 'tier': 2},
    'state': {'status': 'Active', 'version': 1, 'updated_at': '2026-11-06 12:00:00 +0400'},
    'destination': {'file': {'name': 'CA-P-701--nested-plan.md', 'path': '03_plan'}},
}


def text_of(metadata, body=projects.PLAN_BODY):
    return '---\n' + yaml.safe_dump(metadata, sort_keys=False) + '---\n' + body


def row(text, path=ENCODING):
    parsed = parse_carrier(text.encode(), path)
    view = carrier_read_view(parsed.metadata)
    return {'metadata': parsed.metadata, 'text': text,
            'binding': {'atom_id': view['atom_id'], 'version': view['version'], 'path': str(path),
                        'sha256': hashlib.sha256(text.encode()).hexdigest()}}


def checked(metadata, code='frontmatter.common_encoding', source=None, raw=None):
    source = row(ENCODING.read_text()) if source is None else source
    context = AuthorityContext([source['binding']], 0, 0, 0, [], (), {}, False)
    check = Check(Obligation(code, [], True, 'reviewed nested Header'), context,
                  {'sources': [source], '_raw_metadata': metadata,
                   'parsed': parse_carrier((raw or text_of(metadata)).encode(), Path('/fixture/candidate.md'))})
    adapter = _common if code == 'frontmatter.common_encoding' else _subjects if code == 'frontmatter.subjects' else ADAPTERS[code]
    adapter(carrier_read_view(metadata), projects.PLAN_BODY, check)
    return check


class NestedHeaderChecks(unittest.TestCase):
    def assert_clean(self, check):
        self.assertEqual([], check.findings)
        self.assertEqual([], check.gaps)

    def test_reviewed_source_has_exact_seal_and_changed_details_are_unreviewed(self):
        source = row(ENCODING.read_text())
        self.assertEqual('current', reviewed_encoding_profile(source))
        changed = row(ENCODING.read_text().replace('A Plan Context has no Implementation Retry Limit Property',
                                                'A Plan Context has an Implementation Retry Limit Property'))
        self.assertIsNone(reviewed_encoding_profile(changed))
        self.assertTrue(checked(HEADER, source=changed).gaps)

    def test_nested_paths_and_source_mapping_are_preserved(self):
        original = copy.deepcopy(HEADER)
        self.assert_clean(checked(HEADER))
        self.assert_clean(checked(HEADER, 'frontmatter.subjects'))
        self.assert_clean(checked(HEADER, 'property.admission'))
        self.assertEqual(original, HEADER)
        parsed = parse_carrier(text_of(HEADER).encode(), Path('/fixture/candidate.md'))
        self.assertEqual(HEADER, parsed.metadata)
        self.assertNotIn('atom_id', parsed.metadata)

    def test_nested_unknown_keys_wrong_roles_and_wrong_values_fail(self):
        cases = [
            ('context', 'invented', True), ('context', 'role', None), ('context', 'form', []),
            ('context', 'tier', True), ('context', 'plan', {'unadmitted_form': {'x': 1}}),
            ('context', 'concern', {'priority': 'high'}),
            ('context', 'plan', {'ai_agent_confidence_threshold': True}),
            ('context', 'plan', {'work_sequence_number': '1'}),
            ('context', 'plan', {'work_sequence_number': 0}),
            ('context', 'plan', {'ai_agent_confidence_threshold': 101}),
            ('context', 'container', {'scope_unit': 'CA-SU-1', 'atom': 'CA-P-2'}),
            ('identity', 'unknown', 'value'), ('state', 'version', False),
            ('destination', 'file', {'name': 'missing-extension', 'path': '../outside'}),
        ]
        for group, field, value in cases:
            metadata = copy.deepcopy(HEADER)
            metadata[group][field] = value
            with self.subTest(group=group, field=field, value=value):
                self.assertTrue(checked(metadata).findings)
        for group in ('identity', 'context', 'state', 'destination'):
            for value in (None, [], {}, ''):
                metadata = copy.deepcopy(HEADER)
                metadata[group] = value
                with self.subTest(group=group, value=value):
                    if value == {}:
                        self.assertTrue(checked(metadata).findings)
                    else:
                        with self.assertRaises(CarrierError):
                            parse_carrier(text_of(metadata).encode(), Path('/fixture/a.md'))

    def test_declared_plan_fields_and_concern_priority(self):
        metadata = copy.deepcopy(HEADER)
        metadata['context']['plan'] = {'work_sequence_number': 1, 'ai_agent_confidence_threshold': 0}
        self.assert_clean(checked(metadata))
        metadata['identity']['atom_id'] = 'CA-C-701'
        metadata['context'].update(role='Concern', form='Question', concern={'priority': 'high'})
        metadata['context'].pop('plan')
        self.assert_clean(checked(metadata))
        metadata['context']['concern']['priority'] = 'urgent'
        self.assertTrue(checked(metadata).findings)

    def test_state_timestamp_quoting_uses_raw_nested_node(self):
        for quote in ('"', "'"):
            raw = '---\nstate:\n  updated_at: ' + quote + '2026-11-06T12:00:00Z' + quote + '\n---\n'
            self.assert_clean(checked({}, 'frontmatter.updated_at_quoting', raw=raw))
        for value in ('2026-11-06 12:00:00 +0400', '|-\n    2026-11-06T12:00:00Z'):
            raw = '---\nstate:\n  updated_at: ' + value + '\n---\n'
            self.assertTrue(checked({}, 'frontmatter.updated_at_quoting', raw=raw).findings)

    def test_nested_parser_duplicate_and_conflicting_alias_guards(self):
        for raw, code in [
            ('identity: {atom_id: CA-P-1, atom_id: CA-P-2}', 'YAML_DUPLICATE_KEY'),
            ('identity: {atom_id: CA-P-1}\natom_id: CA-P-2', 'CARRIER_ALIAS_CONFLICT'),
            ('state: {version: 1}\nversion: true', 'CARRIER_ALIAS_CONFLICT'),
            ('context: {role: Plan, plan: {ai_agent_confidence_threshold: 20}}\nautonomous_confidence_threshold: 10',
             'CARRIER_ALIAS_CONFLICT'),
        ]:
            with self.subTest(raw=raw), self.assertRaises(CarrierError) as caught:
                parse_carrier(('---\n' + raw + '\n---\n').encode(), Path('/fixture/a.md'))
            self.assertEqual(code, caught.exception.code)

    def test_nested_role_and_form_declaration_coordinates(self):
        source = role_declarations()[0]
        source = row(text_of(nested_header(source['metadata']), source['text'].split('---', 2)[-1]))
        source['metadata']['context']['topics'] = {'main_subject': 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Concern)'}
        source['metadata'].pop('subjects')
        source = row(text_of(source['metadata']))
        self.assertEqual('Concern', current_role_declaration(source))
        source['metadata']['context']['topics']['main_subject'] += '/(.Header.Context.Form := Question)'
        source = row(text_of(source['metadata']))
        self.assertEqual(('Concern', 'Question'), type_definition_coordinate(source))
        self.assertIsNone(current_role_declaration(source))




if __name__ == '__main__':
    unittest.main()
