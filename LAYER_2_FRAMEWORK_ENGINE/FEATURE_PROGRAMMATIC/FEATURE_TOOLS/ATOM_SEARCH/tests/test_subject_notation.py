from __future__ import annotations

import sys
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path as FilePath

TOOLS = FilePath(__file__).resolve().parents[2]
sys.path.insert(0, str(TOOLS))

from subject_notation import (  # noqa: E402
    DeclaredReference, GrammarPin, InitialAtomSelector, Name, Path,
    Qualification, RelationChain, Span, SubjectNotationError, ValueLiteral,
    get_profile, parse_initial_atom_selector, parse_subject,
    namespace_local_expression, parse_subject_expression, profile_evidence, render_subject,
)


class SubjectNotationTest(unittest.TestCase):
    def test_inverse_binding_keeps_distinct_relation_endpoints(self) -> None:
        source = 'Relation//NARROWER_THAN <--> Relation//BROADER_THAN'
        expression = parse_subject_expression(source).expression
        self.assertIsInstance(expression, RelationChain)
        self.assertEqual('<-->', expression.links[0].operator)
        self.assertEqual(['Relation//NARROWER_THAN', 'Relation//BROADER_THAN'],
                         [render_subject(endpoint) for endpoint in expression.endpoints])
        self.assertEqual(source, render_subject(expression))
        self.assertIn('<-->', get_profile('approved').separators)

    def test_namespace_local_expression_only_unwraps_explicit_namespace_chains(self) -> None:
        model = parse_subject_expression('CAPRMEDIO <+ MODEL <+ Node/Atom').expression
        component = parse_subject_expression('CAPRMEDIO <+ MODEL <+ CFEL <+ Format').expression
        structure = parse_subject_expression('CAPRMEDIO <+ STRUCTURE').expression
        self.assertEqual('Node/Atom', render_subject(namespace_local_expression(model)))
        self.assertEqual('CFEL <+ Format', render_subject(namespace_local_expression(component)))
        self.assertEqual('STRUCTURE', render_subject(namespace_local_expression(structure)))
        self.assertEqual('Node/Atom', render_subject(namespace_local_expression(
            parse_subject_expression('CAPRMEDIO_MODEL <+ Node/Atom').expression)))
        self.assertEqual('Scope Unit//UNIT', render_subject(namespace_local_expression(
            parse_subject_expression('CAPRMEDIO_STRUCTURE <+ Scope Unit//UNIT').expression)))
        self.assertIsNone(namespace_local_expression(parse_subject_expression('CAPRMEDIO_MODEL +> Node').expression))
        self.assertIsNone(namespace_local_expression(parse_subject_expression('MODEL').expression))
        self.assertIsNone(namespace_local_expression(parse_subject_expression('Other <+ MODEL <+ Node').expression))

    def test_legacy_tuple_contract_and_pins_are_unchanged(self) -> None:
        self.assertEqual(parse_subject(' Atom.Content / Carrier : Delivery.Policy '),
                         [('Atom.Content', None), ('Carrier', '/'), ('Delivery.Policy', ':')])
        self.assertEqual(parse_subject('Atom..Content'), [('Atom..Content', None)])
        self.assertEqual(parse_subject('Atom"Quoted"/Carrier'), [('Atom"Quoted"', None), ('Carrier', '/')])
        legacy = get_profile()
        self.assertEqual(legacy.separators, ('/', ':'))
        self.assertEqual([(pin.atom_id, pin.version) for pin in legacy.grammar_pins],
                         [('CA-R-1204', 14), ('CA-R-1321', 12), ('CA-R-1324', 10), ('CA-M-228', 14), ('CA-E-383', 13)])
        for value in ('', ' ', '/Atom', 'Atom/', 'Atom//Carrier', 'Atom/:Value', 'Atom::Value',
                      'Atom@3', 'Atom[format]', 'Atom&Carrier', 'atom(atom_id="CA-O-135")'):
            with self.subTest(value=value), self.assertRaises(SubjectNotationError):
                parse_subject(value)
        with self.assertRaises(FrozenInstanceError):
            legacy.name = 'approved'  # type: ignore[misc]

    def test_flat_adapter_refuses_approved_grammar(self) -> None:
        with self.assertRaises(SubjectNotationError) as caught:
            parse_subject('Atom.Status', subject_profile='approved')
        self.assertEqual(caught.exception.code, 'subject-flat-adapter-unsupported')

    def test_approved_path_distinguishes_names_values_and_qualifications(self) -> None:
        expression = parse_subject_expression('Entity/Workflow//Operations.Status:Daily').expression
        self.assertIsInstance(expression, Path)
        self.assertEqual([step.operator for step in expression.steps], ['/', '//', '.', ':'])
        self.assertIsInstance(expression.steps[-1].operand, ValueLiteral)
        qualified = parse_subject_expression('Atom/(.Content Role: Operations)/(.Type: Step)').expression
        self.assertIsInstance(qualified.head, Name)
        self.assertEqual(qualified.head.value, 'Atom')
        self.assertEqual([step.operator for step in qualified.steps], ['/', '/'])
        self.assertTrue(all(isinstance(step.operand, Qualification) for step in qualified.steps))
        relative = qualified.steps[0].operand.relative_path
        self.assertEqual(relative.head.value, 'Content Role')
        self.assertEqual(relative.steps[0].operand.value, 'Operations')
        self.assertEqual(render_subject(qualified), 'Atom/(.Content Role:Operations)/(.Type:Step)')

    def test_quoted_allowed_values_preserve_literal_and_condition_boundaries(self) -> None:
        text = 'Atom/(.Role := "Analysis & Advisory")/(.Form := FPF Analysis Report)'
        expression = parse_subject_expression(text).expression
        self.assertEqual(render_subject(expression), 'Atom/(.Role:="Analysis & Advisory")/(.Form:=FPF Analysis Report)')
        role, form = (step.operand.relative_path for step in expression.steps)
        self.assertEqual((role.steps[0].operator, role.steps[0].operand.value), (':=', 'Analysis & Advisory'))
        self.assertEqual((form.steps[0].operator, form.steps[0].operand.value), (':=', 'FPF Analysis Report'))
        for invalid in ('Atom/(.Role := "Analysis & Advisory)',
                        'Atom/(.Role := Analysis & Advisory)'):
            with self.subTest(invalid=invalid), self.assertRaises(SubjectNotationError):
                parse_subject_expression(invalid)

    def test_declared_reference_and_logical_grouping(self) -> None:
        for text in ('@Atom', '@(Atom)', '@(Entity/Object/Atom.Status)', 'Scope Unit <+ @(Scope Unit)', '@Atom.Status'):
            with self.subTest(text=text):
                expression = parse_subject_expression(text).expression
                self.assertEqual(render_subject(parse_subject_expression(render_subject(expression))), render_subject(expression))
        self.assertIsInstance(parse_subject_expression('@Atom').expression.head, DeclaredReference)
        reference = parse_subject_expression('@(Entity/Object/Atom.Status)').expression.head
        self.assertIsInstance(reference.entity, Path)
        self.assertEqual(render_subject(reference.entity), 'Entity/Object/Atom.Status')
        self.assertEqual(render_subject(parse_subject_expression('@(Entity/Object/Atom.Status)')),
                         '@(Entity/Object/Atom.Status)')
        self.assertIsInstance(parse_subject_expression('(Atom.Status)/Detail').expression.head, Path)
        self.assertIsInstance(parse_subject_expression('(A +> B).Status').expression.head, RelationChain)

    def test_relations_preserve_direction_and_independent_count_slots(self) -> None:
        for text, operator, counts in (
            ('Step {1}+>{1+} Workflow', '+>', ((1, 1), (1, None))),
            ('Workflow {1+}<+{1} Step', '<+', ((1, None), (1, 1))),
            ('Atom.Status >| Status Group', '>|', (None, None)),
            ('Status Group |< Atom.Status', '|<', (None, None)),
            ('Property {1}((IS_PROPERTY_OF)) Bearer', '((', ((1, 1), None)),
            ('Property ((IS_PROPERTY_OF)){1} Bearer', '((', (None, (1, 1))),
        ):
            with self.subTest(text=text):
                chain = parse_subject_expression(text).expression
                self.assertIsInstance(chain, RelationChain)
                link = chain.links[0]
                self.assertEqual(link.operator, operator)
                actual = tuple(None if count is None else (count.minimum, count.maximum)
                               for count in (link.forward_cardinality, link.reverse_cardinality))
                self.assertEqual(actual, counts)
                self.assertIsNone(chain.endpoints[0].value_cardinality)
        chain = parse_subject_expression('Package <+ Module <+ Code Unit').expression
        self.assertEqual(len(chain.endpoints), 3)
        self.assertEqual([link.operator for link in chain.links], ['<+', '<+'])
        self.assertEqual(parse_subject_expression('A ((REL_TYPE)) B').expression.links[0].relation_type.value, 'REL_TYPE')

    def test_property_format_and_direct_value_cardinality_remain_separate(self) -> None:
        path = parse_subject_expression('Atom.Subjects.Governs[string]{0..1}').expression
        self.assertEqual(path.value_format.value, 'string')
        self.assertEqual((path.value_cardinality.minimum, path.value_cardinality.maximum), (0, 1))
        chain = parse_subject_expression('Atom.P[string]{0..1} {1}+>{2} Target').expression
        self.assertEqual(chain.endpoints[0].value_cardinality.minimum, 0)
        self.assertEqual(chain.links[0].forward_cardinality.minimum, 1)
        self.assertEqual(chain.links[0].reverse_cardinality.minimum, 2)
        self.assertEqual(render_subject(path), 'Atom.Subjects.Governs[string]{0..1}')

    def test_reserved_characters_need_escapes_and_round_trip(self) -> None:
        texts = (r'Name\.With\/Characters\:\@\(\)\[\]\{\}\+\<\>\|\*\&\?\,\=\"\'\\',
                 r'Atom/(.Property\:Name:Value\+\>Literal)', r'\ Name\ ', 'Ёж.Status:Готов',
                 ' ( A +> B ) . Status ', 'A[format]{2+}', 'A {0..2}>|{1} B')
        for text in texts:
            with self.subTest(text=text):
                canonical = render_subject(parse_subject_expression(text))
                self.assertEqual(render_subject(parse_subject_expression(canonical)), canonical)
        path = parse_subject_expression(r'Name\/Literal').expression
        self.assertEqual(path.head.value, 'Name/Literal')
        self.assertEqual(path.steps, ())

    def test_spans_are_character_offsets_and_errors_have_spans(self) -> None:
        text = '  Ёж.Status: Готов  '
        parsed = parse_subject_expression(text)
        self.assertEqual(parsed.span, Span(2, 18))
        self.assertEqual(parsed.expression.head.span, Span(2, 4))
        self.assertEqual(parsed.expression.steps[-1].operand.span, Span(13, 18))
        with self.assertRaises(FrozenInstanceError):
            parsed.span = Span(0, 0)  # type: ignore[misc]
        for text in ('', '/A', 'A/', 'A..B', 'A///B', 'A////B', 'A//:B', 'A::B',
                     'A + B', 'A > B', 'A | B', 'A & B', 'A?B', 'A,B', 'A"B',
                     'A\\', '(A', 'A)', 'A/(.B:C', 'A/(B:C', 'A[]', 'A[x',
                     'A{2..1}', 'A{-1}', 'A{n}', 'A{1', 'A {1}+>', 'A ((REL))',
                     'A ((REL) B', 'A +>{1}{2} B', '* not in (Draft, Archived)',
                     'A/(.P:V)junk', 'A/(.Property)', 'A/(.Property.Child)', 'A\x00B'):
            with self.subTest(text=text), self.assertRaises(SubjectNotationError) as caught:
                parse_subject_expression(text)
            self.assertIsNotNone(caught.exception.span)
            self.assertLessEqual(caught.exception.span.end, len(text))

    def test_initial_selector_contract_is_preserved_and_position_limited(self) -> None:
        for text in ('Entity/Term//atom', r'Entity/Term//atom\.content\.claim', 'Entity.Name:atom'):
            with self.subTest(text=text):
                canonical = render_subject(parse_subject_expression(text))
                self.assertEqual(render_subject(parse_subject_expression(canonical)), canonical)
        for literal, mapping in (
            ('atom(content_role="Plan")', {'content_role': 'Plan'}),
            ('atom( content_role = "Plan/Type: Blue.Green" , type = "Plan" )',
             {'content_role': 'Plan/Type: Blue.Green', 'type': 'Plan'}),
        ):
            with self.subTest(literal=literal):
                selector = parse_initial_atom_selector(literal, subject_profile='approved')
                self.assertEqual(dict(selector.selector), mapping)
                parsed = parse_subject_expression(literal + '.Status')
                self.assertIsInstance(parsed.expression.head, InitialAtomSelector)
                self.assertEqual(parsed.expression.head.entity_type_term, 'Atom')
                self.assertEqual(dict(parsed.expression.head.selector), mapping)
                self.assertEqual(render_subject(parse_subject_expression(render_subject(parsed))), render_subject(parsed))
                with self.assertRaises(TypeError):
                    selector.selector['type'] = 'Other'  # type: ignore[index]
        for text in ('atom', 'Atom(content_role="Plan")', 'atom()', 'atom(type="Plan")',
                     'atom(atom_id="CA-O-135")',
                     'atom(type="Plan",content_role="Plan")', 'atom(atom_id="X",content_role="Plan")',
                     'atom(content_role="Plan",unknown="Other")', 'atom(content_role="")',
                     'atom(content_role="Plan\\Role")', 'atom(content_role="Plan*")',
                     'Atom.atom(atom_id="CA-O-135")', 'A +> atom(atom_id="CA-O-135")'):
            with self.subTest(text=text), self.assertRaises(SubjectNotationError) as caught:
                parse_subject_expression(text)
            self.assertIsNotNone(caught.exception.span)

    def test_profile_evidence_uses_fresh_exactly_scoped_pins(self) -> None:
        sources = get_profile('approved').grammar_pins
        pins = [GrammarPin(source.atom_id, 2, source.path, '1' * 64) for source in sources]
        with self.assertRaises(SubjectNotationError) as unbound:
            profile_evidence('approved')
        self.assertEqual(unbound.exception.code, 'profile-evidence-unbound')
        first = profile_evidence('approved', grammar_pins=pins)
        second = profile_evidence('approved', grammar_pins=pins)
        self.assertEqual(first['native_admission'], 'not_performed')
        first['grammar_pins'][0]['atom_id'] = 'altered'
        self.assertEqual(second['grammar_pins'][0]['atom_id'], 'CA-R-1931')
        for profile in ('legacy ', '', None):
            with self.subTest(profile=profile), self.assertRaises(SubjectNotationError):
                parse_subject_expression('Atom', subject_profile=profile)  # type: ignore[arg-type]


if __name__ == '__main__':
    unittest.main()
