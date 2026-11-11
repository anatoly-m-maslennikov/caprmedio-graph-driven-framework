from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declaration_ancestry import compile_ancestry
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import DeclarationSource, content_schema_from_statements

class AncestryTests(unittest.TestCase):
    def project(self, *statements):
        return compile_ancestry((statement, str(i)) for i, statement in enumerate(statements))

    def test_native_form_population_role_constraints(self):
        statements = [
            ('Atom/(.Header.Form := Code Synopsis).Content.Claim{::1}:: []{::0}', 'code'),
            ('Atom/(.Header.Form := Code Synopsis)//$synopsis.Header.Role:: [in ("Analysis & Advisory")]{::1}', 'code'),
            ('Atom/(.Header.Form := Work Report).Content.Details:: {::1}', 'report'),
            ('$report[<Atom>, (.Header.Form = Work Report)]', 'report'),
            ('$report.Header.Role == Plan', 'report'),
            ('Atom/(.Header.Form := Work Report).Content.Other:: {::1}', 'other'),
        ]
        projected = compile_ancestry(statements)
        code = next(p for p in projected if '.Content.Claim{' in p.statement)
        report = next(p for p in projected if '.Content.Details::' in p.statement)
        other = next(p for p in projected if '.Content.Other::' in p.statement)
        self.assertEqual(frozenset({'Analysis & Advisory'}), code.roles)
        self.assertEqual(frozenset({'Plan'}), report.roles)
        self.assertIsNone(other.roles)

    def test_local_role_constraints_intersect(self):
        source = 'same source'
        projected = compile_ancestry((statement, source) for statement in (
            'Atom/(.Header.Form := Work Report).Content.Details:: {::1}',
            '$report[<Atom>, (.Header.Form = Work Report)]',
            '$report.Header.Role == Plan',
            '$report.Header.Role == Method',
        ))
        self.assertEqual(frozenset(), next(p for p in projected if '.Content.Details::' in p.statement).roles)

    def test_grouped_context_matches_flat_bindings(self):
        fixtures = (
            ('Atom/(.Header.Role: Operations)/Workflow',
             'Workflow.Header.Form:: [in (Workflow)]',
             'Workflow.Content.Steps[string]'),
            ('Atom/(.Header.Role: Operations)/Workflow/Step',
             'Step.Header.Form:: [in (Step)]',
             'Step.Content.Detail[string]'),
            ('Atom/(.Header.Form := Code Synopsis).Content.Claim{::1}:: []{::0}',
             'Atom/(.Header.Form := Code Synopsis)//$synopsis.Header.Role:: [in ("Analysis & Advisory")]{::1}'),
            ('Atom/(.Header.Form := Work Report).Content.Details:: {::1}',
             '$report[<Atom>, (.Header.Form = Work Report)]', '$report.Header.Role == Plan'),
        )
        for statements in fixtures:
            with self.subTest(statements=statements):
                flat = compile_ancestry((statement, 'source') for statement in statements)
                grouped = compile_ancestry((statement.replace('.Header.Form', '.Header.Context.Form')
                                             .replace('.Header.Role', '.Header.Context.Role'), 'source')
                                            for statement in statements)
                flat_property = next(p for p in flat if '.Content.' in p.statement)
                grouped_property = next(p for p in grouped if '.Content.' in p.statement)
                self.assertEqual((flat_property.roles, flat_property.forms),
                                 (grouped_property.roles, grouped_property.forms))
                self.assertNotEqual(frozenset(), grouped_property.roles)
                self.assertIsNotNone(grouped_property.roles)

    def test_named_workflow_requires_form_binding(self):
        base = ('Atom/(.Header.Role: Operations)/Workflow', 'Workflow.Content.Steps[string]')
        self.assertEqual(frozenset(), self.project(*base)[-1].roles)
        bound = next(p for p in self.project(*base, 'Workflow.Header.Form:: [in (Workflow)]') if p.statement.endswith('.Content.Steps[string]'))
        self.assertEqual(frozenset({'Operations'}), bound.roles)
        self.assertEqual(frozenset({'Workflow'}), bound.forms)
        self.assertEqual({'0', '1', '2'}, set(bound.provenance))

    def test_arbitrary_mixed_ancestry_and_explicit_relation(self):
        result = self.project('Atom/A//B/C', 'D ((NARROWER_THAN)) C',
                              'D//E/F', 'F.Header.Form:: [in (Special)]',
                              'F.Content.One.Two[string]')
        prop = next(p for p in result if p.statement.endswith('.Content.One.Two[string]'))
        self.assertEqual(frozenset({'Special'}), prop.forms)
        self.assertEqual({'0', '1', '2', '3', '4'}, set(prop.provenance))

    def test_named_edge_with_qualified_parent_projects_and_inherits(self):
        result = self.project(
            'Workflow ((NARROWER_THAN)) Atom/(.Header.Context.Role in (Operations))',
            'Workflow.Header.Context.Form:: [in (Workflow)]',
            'Workflow.Content.Steps[string]',
            'Step ((INSTANCE_OF)) Workflow',
            'Step.Header.Context.Form:: [in (Workflow)]',
            'Step.Content.Detail[string]',
        )
        workflow = next(p for p in result if p.statement.endswith('.Content.Steps[string]'))
        step = next(p for p in result if p.statement.endswith('.Content.Detail[string]'))
        self.assertEqual((frozenset({'Operations'}), frozenset({'Workflow'})), (workflow.roles, workflow.forms))
        self.assertEqual((frozenset({'Operations'}), frozenset({'Workflow'})), (step.roles, step.forms))
        self.assertIn('0', step.provenance)

    def test_named_edge_rejects_variable_and_unsupported_parent(self):
        for parent in ('Atom//$variable', 'Atom/*/Workflow', 'Atom/(.Header.Role != Operations)'):
            with self.subTest(parent=parent):
                result = self.project(f'Workflow ((NARROWER_THAN)) {parent}',
                                      'Workflow.Header.Form:: [in (Workflow)]',
                                      'Workflow.Content.Steps[string]')
                self.assertFalse(any(p.roles not in (None, frozenset()) and p.statement.endswith('.Content.Steps[string]')
                                     for p in result))

    def test_named_edge_projects_workflow_content_schema(self):
        source = DeclarationSource('CA-R-1', 1, 'workflow.md')
        schema = content_schema_from_statements((statement, source) for statement in (
            'Workflow ((NARROWER_THAN)) Atom/(.Header.Context.Role in (Operations))',
            'Workflow.Header.Context.Form:: [in (Workflow)]',
            'Workflow.Content.Steps:: {::1}',
        ))
        rule = next(rule for rule in schema.rules if rule.path == ('steps',))
        self.assertEqual((frozenset({'Operations'}), frozenset({'Workflow'})), (rule.roles, rule.forms))

    def test_unrelated_and_lists_do_not_create_names(self):
        result = self.project('Atom.Header.Form:: [in (Workflow)]', 'Workflow.Content.X[string]',
                              'Atom/*/Workflow', 'Atom/(.Header.Form in (Workflow))/Other')
        self.assertFalse(any(p.statement.endswith('.Content.X[string]') for p in result))

    def test_ancestry_added_later_is_seen(self):
        prop = 'Workflow.Content.X[string]'
        self.assertFalse(self.project(prop))
        self.assertTrue(self.project(prop, 'Atom/Workflow'))

    def test_role_only_binding_does_not_identify_named_form(self):
        result = self.project('Atom/Workflow', 'Workflow.Header.Role:: [in (Operations)]',
                              'Workflow.Content.X[string]')
        prop = next(p for p in result if p.statement.endswith('.Content.X[string]'))
        self.assertEqual(frozenset(), prop.roles)

    def test_direct_named_owner_is_projected_and_wildcard_rejected(self):
        result = self.project('Atom/Workflow.Content.X[string]',
                              'Atom/*/Workflow.Content.Bad[string]')
        prop = next(p for p in result if p.statement.endswith('.Content.X[string]'))
        self.assertEqual(frozenset(), prop.roles)
        self.assertFalse(any(p.statement.endswith('.Content.Bad[string]') for p in result))

    def test_repeated_names_do_not_merge_addresses(self):
        result = self.project('Atom/X//A//B', 'Y//A//B',
                              'Y//A//B.Content.Wrong[string]',
                              'X//A//B.Content.Right[string]')
        self.assertFalse(any(p.statement.endswith('.Content.Wrong[string]') for p in result))
        self.assertTrue(any(p.statement.endswith('.Content.Right[string]') for p in result))

    def test_constraints_intersect(self):
        result = self.project('Atom/(.Header.Role in (Operations, Method))/Workflow',
                              'Workflow.Header.Form:: [in (Workflow)]',
                              'Workflow.Header.Role:: [in (Method)]',
                              'Workflow.Content.X[string]')
        prop = next(p for p in result if p.statement.endswith('.Content.X[string]'))
        self.assertEqual(frozenset({'Method'}), prop.roles)

if __name__ == '__main__':
    unittest.main()
