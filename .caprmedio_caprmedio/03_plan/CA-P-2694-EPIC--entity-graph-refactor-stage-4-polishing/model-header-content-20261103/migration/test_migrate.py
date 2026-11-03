import contextlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from claim import Ambiguous
from migrate import apply_records, digest, plan, remove_cfel_references, transform

MAP = {'full_property_paths': [{'old': 'Atom.ID', 'new': 'Atom.Header.ID'}], 'base_atom_id_replacements': {}, 'atom_id_replacements': {}}


class MigrationTests(unittest.TestCase):
    def test_subject_yaml_quotes_are_not_expression_literals(self):
        mapping = dict(MAP, atom_header_fields=['Role', 'Form'])
        source = b"---\nsubjects:\n  passive:\n  - 'Atom/(.Content Role: Operations)/(.Type: Workflow) {1+}<+ Atom'\n  active: 'Atom/(.Role := \"Atom.ID\")'\nrole: Rule\n---\n## Claim\nA\n"
        result = transform(source, mapping)
        self.assertIn(b"'Atom/(.Header.Role: Operations)/(.Header.Form: Workflow) {:1+}<+ Atom'", result)
        self.assertIn(b"'Atom/(.Header.Role := \"Atom.ID\")'", result)
        self.assertEqual(transform(result, mapping), result)

    def test_legacy_relation_cardinalities_only(self):
        source = b'---\nrole: Rule\n---\n## Claim\nEntity {0+}((HAS_PROPERTY)){1} Property; Step {1}+>{1+} Workflow; value{1}; "{1}((R)){2}"\n'
        result = transform(source, MAP)
        self.assertIn(b'Entity {:0+}((HAS_PROPERTY)){:1} Property', result)
        self.assertIn(b'Step {:1}+>{:1+} Workflow', result)
        self.assertIn(b'value{1}; "{1}((R)){2}"', result)

    def test_exact_legacy_atom_addresses(self):
        mapping = dict(MAP, atom_header_fields=['Status', 'Role', 'Form'])
        source = b"---\nrole: Rule\nsubjects:\n  active: 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow//Run'\n---\n## Claim\nAtom/Content Role Atom/Type Atom/Content Role: Plan.Content.Claim\nAtom/Content Role: Plan.Status Entity/Object/Continuant/Other/Atom/Content Role\nProjection/Type Type Content Role \"Atom/Content Role: Plan\"\n"
        result = transform(source, mapping)
        self.assertIn(b"'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)//Run'", result)
        self.assertIn(b'Atom.Header.Role Atom.Header.Form Atom/(.Header.Role := Plan).Content.Claim', result)
        self.assertIn(b'Atom/(.Header.Role := Plan).Header.Status', result)
        self.assertIn(b'Entity/Object/Continuant/Other/Atom/Content Role', result)
        self.assertIn(b'Projection/Type Type Content Role "Atom/Content Role: Plan"', result)
        self.assertEqual(transform(result, mapping), result)

    def test_projection_type_selector_alias(self):
        source = b'---\nrole: Rule\n---\n## Claim\nProjection.Type Projection/(.Type: A) Projection/(.Type := B) Projection/(.Type = C)\nOther.Type Other/(.Type: A) Type "Projection.Type"\n'
        result = transform(source, MAP)
        self.assertIn(b'Projection.Form Projection/(.Form: A) Projection/(.Form := B) Projection/(.Form = C)', result)
        self.assertIn(b'Other.Type Other/(.Type: A) Type "Projection.Type"', result)
        self.assertNotIn(b'Projection.Header', result)
        self.assertEqual(transform(result, MAP), result)

    def test_id_map_never_changes_carrier_identity(self):
        mapping = dict(MAP, base_atom_id_replacements={'CA-R-1': 'CA-R-999'})
        source = b'---\natom_id: CA-R-1\nstatus: Active\nrole: Rule\n---\n## Claim\nCA-R-1\n'
        result = transform(source, mapping)
        self.assertIn(b'atom_id: CA-R-1', result)
        self.assertIn(b'### Prose Claim\n\nCA-R-999', result)
        with self.assertRaises(Ambiguous): transform(source.replace(b'Active', b'Draft'), mapping)

    def test_claim_scope_property_address_only(self):
        source = b'---\nrole: Rule\n---\n## Claim\nAtom.Content.Claim Scope Claim Scope Other.Content.Claim Scope "Atom.Content.Claim Scope"\n'
        result = transform(source, MAP)
        self.assertIn(b'Atom.Content.Claim.Prose Claim Claim Scope Other.Content.Claim Scope "Atom.Content.Claim Scope"', result)

    def test_pinned_reviewed_override_and_idempotence(self):
        source = b'---\natom_id: CA-R-1\nrole: Rule\n---\n## Claim\nold notation Atom.ID\n'
        payload = source.replace(b'old notation', b'reviewed notation')
        row = {'before_sha256': digest(source), 'candidate_sha256': digest(payload),
               'candidate': payload.decode(), 'source_id': 'CA-R-1'}
        mapping = dict(MAP, reviewed_source_overrides=[row])
        result = transform(source, mapping)
        self.assertIn(b'reviewed notation Atom.Header.ID', result)
        self.assertEqual(transform(result, mapping), result)
        drifted = transform(source.replace(b'old notation', b'changed notation'), mapping)
        self.assertIn(b'changed notation', drifted)
        self.assertNotIn(b'reviewed notation', drifted)
        invalid = dict(MAP, reviewed_source_overrides=[dict(row, candidate_sha256='0' * 64)])
        with self.assertRaises(Ambiguous): transform(source, invalid)

    def test_summary_identity_preserved_and_absence_retained(self):
        mapping = dict(MAP, full_property_paths=[{'old': 'Atom.Status', 'new': 'Atom.Header.Status'}],
                       base_atom_id_replacements={'CA-R-1': 'CA-R-999'})
        summary = '\nDefine Atom.Status CA-R-1 "Atom.Status" \'CA-R-1\'\n\n### Unregistered\nAtom.Status CA-R-1\n\n'
        source = ('---\nrole: Rule\n---\n## Summary\n' + summary + '## Claim\nAtom.Status CA-R-1\n').encode()
        result = transform(source, mapping).decode()
        self.assertIn('## Summary\n' + summary + '## Claim', result)
        self.assertIn('Atom.Header.Status CA-R-999', result)
        self.assertEqual(transform(result.encode(), mapping).decode(), result)
        incomplete = transform(b'---\nstatus: Draft\nrole: Rule\n---\n## Claim\nA\n', mapping)
        self.assertNotIn(b'## Summary', incomplete)

    def test_id_map_preserves_frozen_references(self):
        mapping = dict(MAP, base_atom_id_replacements={'CA-R-1': 'CA-R-999'})
        source = b'---\nrole: Rule\n---\n## Claim\nCA-R-1 CA-R-1@2 CA-R-10 "CA-R-1"\n'
        result = transform(source, mapping)
        self.assertIn(b'CA-R-999 CA-R-1@2 CA-R-10 "CA-R-1"', result)

    def test_exact_receiver(self):
        text = b'---\nrole: Rule\n---\n## Claim\n\nAtom.ID Projection.ID EventRecord.ID\n'
        result = transform(text, MAP)
        self.assertIn(b'Atom.Header.ID Projection.ID EventRecord.ID', result)
        self.assertEqual(transform(result, MAP), result)

    def test_reference_marker_only_in_cfel_and_outside_literals(self):
        source = 'outside @Thing\n```CFEL\n@Node a@b.example CA-R-1@2 "@" \'@Thing\' @(Atom)\n```\n'
        result = remove_cfel_references(source)
        self.assertEqual(result, 'outside @Thing\n```CFEL\nNode a@b.example CA-R-1@2 "@" \'@Thing\' (Atom)\n```\n')

    def test_subject_reference_and_literal_preservation(self):
        source = b"---\nsubjects:\n  active: '@Node <+ Person'\n  passive: ['mail@domain.example', 'CA-R-1@2']\nrole: Rule\n---\n## Claim\n\nA\n"
        result = transform(source, MAP)
        self.assertIn(b"active: 'Node <+ Person'", result)
        self.assertIn(b"'mail@domain.example', 'CA-R-1@2'", result)

    def test_valid_right_bound_survives_and_outside_colon_is_held(self):
        source = b'---\nrole: Rule\n---\n## Claim\n\n```CFEL\nA ((R)){:1} B\n```\n'
        self.assertIn(b'((R)){:1}', transform(source, MAP))
        with self.assertRaises(Ambiguous):
            transform(source.replace(b'((R)){:1}', b'((R)):{:1}'), MAP)

    def test_ambiguous_atom_variable_held(self):
        with self.assertRaises(Ambiguous):
            transform(b'---\nrole: Rule\n---\n## Claim\n\n$x.ID\n', MAP)

    def test_optional_cardinality_relation_objects_and_literals(self):
        source = b'---\nrole: Rule\n---\n## Claim\n```CFEL\nRelation//R; A ((R)) B; A {:0..1}((R)){:1} B;\nalias(Relation//R) == "((R)): Atom.ID @Thing"\n```\n'
        result = transform(source, MAP)
        self.assertIn(b'A ((R)) B', result)
        self.assertIn(b'{:0..1}((R)){:1}', result)
        self.assertIn(b'"((R)): Atom.ID @Thing"', result)

    def test_typed_atom_variables_and_other_receivers(self):
        mapping = dict(MAP, atom_header_fields=['ID', 'Role', 'Form'])
        source = b'---\nrole: Rule\n---\n## Claim\n```CFEL\nAtom//$atom.ID == $atom.ID; Atom/(.Role := Rule).ID; Atom/(.Role := Rule)/(.Form := A);\nProjection//$projection.ID == $projection.ID; Scope Unit//$unit.ID == $unit.ID\n```\n'
        result = transform(source, mapping)
        self.assertIn(b'Atom//$atom.Header.ID == $atom.Header.ID', result)
        self.assertIn(b'Atom/(.Header.Role := Rule).Header.ID', result)
        self.assertIn(b'Atom/(.Header.Role := Rule)/(.Header.Form := A)', result)
        self.assertIn(b'Projection//$projection.ID == $projection.ID', result)
        self.assertIn(b'Scope Unit//$unit.ID == $unit.ID', result)
        self.assertEqual(transform(result, mapping), result)

    def test_conflicting_bindings_are_held(self):
        mapping = dict(MAP, atom_header_fields=['ID'])
        with self.assertRaises(Ambiguous):
            transform(b'---\nrole: Rule\n---\n## Claim\nAtom//$x.ID Projection//$x.ID $x.ID\n', mapping)

    def test_preconditions_checked_before_any_write(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, second = root / 'a.md', root / 'b.md'
            original = '---\nrole: Rule\n---\n## Claim\nA\n'
            first.write_text(original); second.write_text(original)
            manifest = plan([first, second], MAP, root)
            second.write_text('drift')
            with patch('migrate.atom_identity_lock', return_value=contextlib.nullcontext()):
                with self.assertRaises(ValueError): apply_records(manifest, root)
            self.assertEqual(first.read_text(), original)

    def test_guard_and_idempotence(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source.md'
            source.write_text('---\nrole: Rule\n---\n## Claim\n\nA\n')
            manifest = plan([source], MAP, root)
            with patch('migrate.atom_identity_lock', return_value=contextlib.nullcontext()):
                self.assertEqual(apply_records(manifest, root), 1)
                self.assertEqual(apply_records(manifest, root), 0)
                source.write_text('drift')
                with self.assertRaises(ValueError): apply_records(manifest, root)

    def test_failure_rolls_back_prior_write(self):
        from migrate import atomic_replace
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first, second = root / 'a.md', root / 'b.md'
            original = '---\nrole: Rule\n---\n## Claim\n\nA\n'
            first.write_text(original); second.write_text(original)
            manifest = plan([first, second], MAP, root)
            calls = []
            def fail_second(path, data):
                calls.append(path)
                if len(calls) == 2: raise OSError('simulated failure')
                atomic_replace(path, data)
            with patch('migrate.atom_identity_lock', return_value=contextlib.nullcontext()), patch('migrate.atomic_replace', side_effect=fail_second):
                with self.assertRaises(OSError): apply_records(manifest, root)
            self.assertEqual(first.read_text(), original)
            self.assertEqual(second.read_text(), original)

    def test_held_plan_cannot_apply(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / 'source.md'
            source.write_text('---\nrole: Rule\n---\n## Claim\n$x.ID\n')
            manifest = plan([source], MAP, root)
            self.assertEqual(len(manifest['held']), 1)
            with self.assertRaises(ValueError): apply_records(manifest, root)


if __name__ == '__main__': unittest.main()
