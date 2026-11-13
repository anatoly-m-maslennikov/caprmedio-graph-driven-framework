"""Population constraints remain source-bound structured data, without evaluation."""
from pathlib import Path
import sys
import unittest

PROGRAMMATIC = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(PROGRAMMATIC), str(PROGRAMMATIC / 'FEATURE_TOOLS'),
                str(PROGRAMMATIC / 'FEATURE_TOOLS' / 'GENERATE_ENTITY_GRAPH')]
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import NativeModelClaimError, parse_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from FEATURE_FORMAL_MODEL_ENGINE.native_model_lint import lint_native_model_claim
from lint_python_model_claim import lint_python_model_claim
from cfel_claim_constraints import _native_constraints

CLAIM = '''from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="ID", relation_name="IS_PROPERTY_OF", base_path="Projection",
    property_occurrence_cardinality=1, value_format=str, value_cardinality=1,
    dependent_property_cardinality=0,
    population_functional_dependencies=(
        {"keys": ("Form", "Scope Unit"), "dependents": ("ID",)},
        {"keys": ("ID",), "dependents": ("Form", "Scope Unit")},
    ))'''
ADDRESSES = {'Projection', 'Projection.Form', 'Projection.Scope Unit', 'Projection.ID'}
SOURCE = {'atom_id':'CA-R-1','version':1,'path':'fixture.md','sha256':'fixture'}

class PopulationDependenciesTests(unittest.TestCase):
    def lint(self, text=CLAIM, addresses=ADDRESSES):
        return lint_python_model_claim(text, declared_addresses=addresses,
                                      relation_names={'IS_PROPERTY_OF'}, path='fixture')
    def test_exact_ordered_rules_and_provenance(self):
        declaration = parse_native_model_claim(CLAIM)
        self.assertEqual((), self.lint())
        self.assertEqual(('Projection.ID{::1} :: [string]{::1}', 'Projection.ID.*[]{::0}'),
                         compiler_model_statements(declaration))
        records = _native_constraints(declaration, SOURCE, CLAIM)
        properties = [r for r in records if r['kind'] == 'property_constraint']
        self.assertEqual(2, len(properties))
        rules = [r for r in records if r['kind'] == 'population_functional_dependency']
        self.assertEqual([(('Form', 'Scope Unit'), ('ID',)), (('ID',), ('Form', 'Scope Unit'))],
                         [(r['keys'], r['dependents']) for r in rules])
        for row in rules:
            self.assertEqual(SOURCE, row['source'])
            self.assertEqual('Projection', row['population_selector'])
            self.assertEqual('instances', row['group'])
            self.assertNotIn('status_group', row)
    def test_lint_requires_exact_bearer_and_every_property(self):
        for missing in ADDRESSES:
            with self.subTest(missing=missing):
                errors = self.lint(addresses=ADDRESSES - {missing} | {'Other.Form', 'Other.Scope Unit', 'Other.ID'})
                self.assertTrue(errors, missing)
        wrong = CLAIM.replace('base_path="Projection"', 'base_path="Other"')
        self.assertTrue(self.lint(wrong, ADDRESSES | {'Other'}))
    def test_reject_malformed_rules(self):
        for bad in (CLAIM.replace('"keys": ("Form", "Scope Unit")', '"keys": ()'),
                    CLAIM.replace('"keys": ("Form", "Scope Unit")', '"keys": ("../Form",)'),
                    CLAIM.replace('"keys": ("Form", "Scope Unit")', '"keys": (" Form",)'),
                    CLAIM.replace('"keys": ("Form", "Scope Unit")', '"keys": ("Form", "Form")'),
                    CLAIM.replace('"dependents": ("ID",)', '"dependent": ("ID",)', 1),
                    CLAIM.replace('base_path="Projection",', '')):
            with self.subTest(bad=bad), self.assertRaises(NativeModelClaimError):
                parse_native_model_claim(bad)
if __name__ == '__main__': unittest.main()
