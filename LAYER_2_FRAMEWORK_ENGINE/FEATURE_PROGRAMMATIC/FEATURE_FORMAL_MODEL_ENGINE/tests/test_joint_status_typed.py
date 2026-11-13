import unittest
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim
from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements
from test_native_status_qualifiers import PLAN, ANALYSIS

class JointClaims(unittest.TestCase):
    def test_typed_reference_and_status_qualifiers_and_classifications(self):
        typed='''from caprmedio.formal_claims import declare_entity
from caprmedio.model import NamedSelection
declare_entity(entity_name="Named Selection", relation_name="IS_PROPERTY_OF", base_path="Projection.Source", value_format=NamedSelection, value_cardinality=1)'''
        statements=compiler_model_statements(parse_native_model_claim(typed),model_class_bindings={'NamedSelection':{'Named Selection'}})
        self.assertTrue(any('[Named Selection//]' in statement for statement in statements))
        plan=compiler_model_statements(parse_native_model_claim(PLAN))
        self.assertTrue(any('Status Group == Backlog' in statement for statement in plan))
        analysis=compiler_model_statements(parse_native_model_claim(ANALYSIS))
        self.assertEqual(len(analysis),2)
        role='''from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom
class Method(Atom):
    pass
declare_entity(entity_class=Method, entity_name="Method", qualification_property_path="Atom.Header.Context.Role", classifications={"Role Order Number": 3})'''
        self.assertTrue(any('Role Order Number == 3' in statement for statement in compiler_model_statements(parse_native_model_claim(role))))
