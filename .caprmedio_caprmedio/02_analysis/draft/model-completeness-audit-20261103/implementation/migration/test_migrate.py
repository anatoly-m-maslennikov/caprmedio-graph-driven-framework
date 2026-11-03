import contextlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import migrate


class MigrationTests(unittest.TestCase):
    def carrier(self, claim):
        return ('---\natom_id: CA-R-1\nstatus: Active\nversion: 3\nupdated_at: original\n---\n## Summary\nIdentity IS_DEFINED_BY Atom//\n## Claim\n### Formal Claim\n```CFEL\n' + claim + '\n```\n').encode()

    def test_model_descriptor_and_distinct_instance_endpoints(self):
        result = migrate.transform(self.carrier('Plan// ((BLOCKS)) Plan//;\nRelation//BLOCKS ((HAS_CLASSIFICATION)) Derivation == Direct'), {})
        self.assertIn(b'# model\nRelation//BLOCKS', result)
        self.assertIn(b'# instances\nPlan//$plan ((BLOCKS)) Plan//$plan_2;', result)
        self.assertLess(result.index(b'# model'), result.index(b'# instances'))
        self.assertEqual(migrate.transform(result, {}), result)
        self.assertIn(b'Identity IS_DEFINED_BY Atom//', result)
        self.assertIn(b'updated_at: original', result)

    def test_existing_bindings_named_addresses_and_literals(self):
        source = self.carrier('Relation//A ((HAS_INVERSE)) Relation//B;\nAtom//$atom.ID == "Kind// IS_DEFINED_BY";\nAtom// ((R)) Atom//')
        result = migrate.transform(source, {})
        self.assertIn(b'Relation//A ((HAS_INVERSE)) Relation//B;', result)
        self.assertIn(b'Atom//$atom.ID == "Kind// IS_DEFINED_BY"', result)
        self.assertIn(b'Atom//$atom_2 ((R)) Atom//$atom_3', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_compound_statement_remains_together(self):
        source = self.carrier('Relation//R ((HAS_CLASSIFICATION)) Derivation == Direct;\nIF ($atom.ID{=1})\nTHEN ($atom.ID > 0)\nAND ($atom.Label{=1})')
        result = migrate.transform(source, {})
        self.assertIn(b'# instances\nIF ($atom.ID{=1})\nTHEN ($atom.ID > 0)\nAND ($atom.Label{=1})', result)

    def test_model_relation_bindings_and_aggregate_binding(self):
        source = self.carrier('Relation// ((HAS_INVERSE)) Relation//;\nUNIQUE(Atom//, (.ID));')
        result = migrate.transform(source, {})
        self.assertIn(b'# model\nRelation//$relation ((HAS_INVERSE)) Relation//$relation_2;', result)
        self.assertIn(b'# instances\nUNIQUE(Atom//$atom, (.ID));', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_compound_preserves_existing_binder_with_unique_new_selection(self):
        source = self.carrier('IF (Scope Unit//$unit not in (Scope Unit/Project//))\nTHEN ($unit.ID{:1})')
        result = migrate.transform(source, {})
        self.assertIn(b'IF (Scope Unit//$unit not in (Scope Unit/Project//$scope_unit))\nTHEN ($unit.ID{:1})', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_union_and_filtered_population_compositions(self):
        filters = '(.object_output{=1}, .object_output.version{=0}, .object_output.id = $projection.ID, (.action = create OR .action = update))'
        source = self.carrier('Step// ((RUNS)) (in (Action, Workflow))//;\nProjection//$projection.Updated At == MAX(Event Record//' + filters + '.happened_at)')
        result = migrate.transform(source, {})
        self.assertIn(b'(in (Action, Workflow))//$selected', result)
        expected = 'MAX(Event Record//$event_record' + filters + '.happened_at)'
        self.assertIn(expected.encode(), result)
        self.assertEqual(result.count(b'MAX('), 1)
        self.assertEqual(result.count(filters.encode()), 1)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_data_constraints_bind_current_bearer_without_cross_statement_identity(self):
        source = self.carrier('IF (Atom.Header.Tier = 1) THEN (Atom.Header.Tier.Label == Core);\nCOUNT(Atom.Header.Subjects.Passive: $) = COUNT(DISTINCT Atom.Header.Subjects.Passive: $)')
        result = migrate.transform(source, {})
        self.assertIn(b'Atom//$atom;\n\nIF ($atom.Header.Tier = 1) THEN ($atom.Header.Tier.Label == Core);', result)
        self.assertIn(b'Atom//$atom_2;\n\nCOUNT($atom_2.Header.Subjects.Passive: $)', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_pure_model_variables_and_mixed_domain_hold(self):
        result = migrate.transform(self.carrier('$narrower ((NARROWER_THAN)) $broader;'), {})
        self.assertIn(b'# model\n$narrower', result)
        for relation, endpoint in [('IS_PROPERTY_OF', 'property'), ('HAS_CLASSIFICATION', 'classified'), ('IS_CONTAINED_BY', 'part')]:
            result = migrate.transform(self.carrier('$' + endpoint + ' ((' + relation + ')) $target;'), {})
            self.assertIn(b'# model', result)
            self.assertNotIn(b'# instances', result)

    def test_override_hash_and_identity_protection(self):
        source = self.carrier('A: [string]{:1};')
        payload = source.replace(b'A: [string]', b'B: [string]')
        row = {'before_sha256': migrate.guards.digest(source), 'candidate_sha256': migrate.guards.digest(payload), 'candidate': payload.decode()}
        result = migrate.transform(source, {'reviewed_source_overrides': [row]})
        self.assertIn(b'B: [string]', result)
        self.assertEqual(migrate.transform(result, {'reviewed_source_overrides': [row]}), result)
        with self.assertRaises(migrate.Ambiguous):
            migrate.transform(source, {'reviewed_source_overrides': [dict(row, candidate_sha256='bad')]})
        changed = source.replace(b'atom_id: CA-R-1', b'atom_id: CA-R-2')
        row.update(candidate=changed.decode(), candidate_sha256=migrate.guards.digest(changed))
        with self.assertRaises(migrate.Ambiguous): migrate.transform(source, {'reviewed_source_overrides': [row]})

    def test_opt_in_relation_rename_protects_identity_and_literals(self):
        result = migrate.transform(self.carrier('Relation//IS_DEFINED_BY ((R)) "IS_DEFINED_BY CA-R-1@2";'), {'rename_is_defined_by': True})
        self.assertIn(b'Relation//IS_DECLARED_BY', result)
        self.assertIn(b'Identity IS_DEFINED_BY Atom//', result)
        self.assertIn(b'"IS_DEFINED_BY CA-R-1@2"', result)

    def test_population_count_and_shared_step_binding(self):
        result = migrate.transform(self.carrier('Journal//{:1};\nIF Step// {=0}((RUNS)) THEN Step// ((R)) Action//'), {})
        self.assertIn(b'Journal//$journal{:1};', result)
        self.assertIn(b'Step//$step;', result)
        self.assertIn(b'IF $step {=0}((RUNS)) THEN $step ((R)) Action//$action', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_model_membership_nested_scope_and_instance_node_union(self):
        source = self.carrier('IF ((Node, Node.**) {=0}((IS_PROPERTY_OF)))\nTHEN ((Node, Node.**) >| (Independence == Primary Node));\n(Node//, (Node//).**) {:0}((*));')
        result = migrate.transform(source, {})
        self.assertIn(b'# model\nIF $model_node in (Node, Node.**) THEN (', result)
        self.assertIn(b'IF ($model_node {=0}((IS_PROPERTY_OF)))\nTHEN ($model_node >| (Independence == Primary Node))', result)
        self.assertIn(b'# instances\nNode//$node;\n\n($node, $node.**) {:0}((*));', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_bound_membership_remains_instance_filter(self):
        source = self.carrier('Atom//$x;\nIF $x in (Node, Node.**) THEN ($x.ID{:1});')
        result = migrate.transform(source, {})
        self.assertIn(b'# instances', result)
        self.assertNotIn(b'# model', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_comments_and_nested_membership_conclusion(self):
        source = self.carrier('# descriptor comment "literal; )"\nRelation//R ((HAS_CLASSIFICATION)) Derivation == Direct;\nIF $model in (Node, Node.**) THEN (\n# nested comment ; (\nIF ($model {=0}((IS_PROPERTY_OF))) THEN ($model >| Primary);\n);')
        result = migrate.transform(source, {})
        self.assertIn(b'# descriptor comment "literal; )"', result)
        self.assertIn(b'# nested comment ; (', result)
        self.assertIn(b'# model', result)
        self.assertNotIn(b'# instances', result)
        self.assertEqual(migrate.transform(result, {}), result)

    def test_apply_gate_preflight_idempotence_and_rollback(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            a, b = root / 'a.md', root / 'b.md'
            original = self.carrier('A: [string]{:1};')
            a.write_bytes(original); b.write_bytes(original)
            manifest = migrate.plan([a, b], {}, root)
            atomic = migrate.guards.atomic_replace
            calls = []
            def fail_second(path, data):
                calls.append(path)
                if len(calls) == 2: raise OSError('failed')
                atomic(path, data)
            with patch.object(migrate.guards, 'atom_identity_lock', return_value=contextlib.nullcontext()):
                with patch.object(migrate.guards, 'atomic_replace', side_effect=fail_second):
                    with self.assertRaises(OSError): migrate.apply_records(manifest, root)
                self.assertEqual(a.read_bytes(), original)
                self.assertEqual(b.read_bytes(), original)
                self.assertEqual(migrate.apply_records(manifest, root), 2)
                self.assertEqual(migrate.apply_records(manifest, root), 0)
                b.write_bytes(b'drift')
                with self.assertRaises(ValueError): migrate.apply_records(manifest, root)
            manifest['held'] = [{'reason': 'ambiguity'}]
            with self.assertRaises(ValueError): migrate.apply_records(manifest, root)


if __name__ == '__main__': unittest.main()
