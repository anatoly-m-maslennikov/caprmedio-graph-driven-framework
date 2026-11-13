"""Native Model Claims are inspected as syntax and never executed."""

from pathlib import Path
import sys
import unittest


FEATURE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEATURE))
from native_model_claim import NativeModelClaimError, parse_native_model_claim, validate_aspect_instance  # noqa: E402


class NativeModelClaimTests(unittest.TestCase):
    def test_unknown_declaration_and_constraint_keys_fail_closed(self):
        prefix = "from caprmedio.formal_claims import declare_entity, declare_relation\n"
        cases = (
            "declare_entity(entity_name='A', value_cardinailty=1)",
            "declare_relation(relation_name='R', source_endpoint={'level': 'instances'}, "
            "target_endpoint={'level': 'instances'}, target_per_source=1)",
            "declare_entity(entity_name='A', instance_relation_constraints={'R': {'target_entity_pathz': ('A',)}})",
            "declare_entity(entity_name='A', instance_property_constraints={'P': {'value_cardinailty': 1}})",
        )
        for case in cases:
            with self.subTest(case=case), self.assertRaisesRegex(NativeModelClaimError, 'unsupported'):
                parse_native_model_claim(prefix + case)

    def test_typed_instance_is_static_and_requires_trusted_symbols(self):
        prefix = ('from caprmedio.formal_claims import declare_entity\n'
                  'from caprmedio.model import ScopeUnit\n')
        call = ('declare_entity(entity_name="ENGINE", instance=ScopeUnit('
                'id="CA-SU-14", name="ENGINE", ordered=False, container="caprmedio"))')
        result = parse_native_model_claim(prefix + call)
        self.assertEqual("ScopeUnit", result["arguments"]["instance"]["type"])
        self.assertEqual("CA-SU-14", result["arguments"]["instance"]["fields"]["id"])
        invalid = (
            call.replace('name="ENGINE", ordered', 'name="ENGINE", name="ENGINE", ordered'),
            call.replace('id="CA-SU-14"', 'id=open("file")'),
            call + '\nprint("side effect")',
            call.replace('instance=ScopeUnit', 'instance=Untrusted'),
        )
        for item in invalid:
            with self.subTest(item=item), self.assertRaises(NativeModelClaimError):
                parse_native_model_claim(prefix + item)
        with self.assertRaises(NativeModelClaimError):
            parse_native_model_claim('from caprmedio.formal_claims import declare_entity\n' + call)

    def test_aspect_instance_requires_full_matching_structure_address(self):
        prefix = ('from caprmedio.formal_claims import declare_entity\n'
                  'from caprmedio.model import Aspect\n')
        address = 'PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Schema'
        call = f'declare_entity(entity_name="Schema", instance=Aspect(address={address!r}))'
        result = parse_native_model_claim(prefix + call)
        self.assertEqual({"type": "Aspect", "fields": {"address": address}},
                         result["arguments"]["instance"])
        self.assertEqual(address, validate_aspect_instance(result["arguments"]))
        spaced = call.replace(address, 'PROJECT STRUCTURE // CAPRMEDIO  <+  Aspects <+ Engineering <+ Schema')
        self.assertEqual(address, validate_aspect_instance(parse_native_model_claim(prefix + spaced)["arguments"]))
        invalid = (
            call.replace('entity_name="Schema"', 'entity_name="Other"'),
            call.replace(address, 'Engineering <+ Schema'),
            call.replace(address, 'CAPRMEDIO_MODEL <+ Aspects <+ Schema'),
            call.replace(address, 'CAPRMEDIO_STRUCTURE <+ Aspects <+ Schema'),
            call.replace('entity_name="Schema",', 'entity_name="Schema", value_cardinality=1,'),
            call.replace(address, 'PROJECT STRUCTURE//CAPRMEDIO <+ Engineering <+ Schema'),
            call.replace(address, 'PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Schema/X'),
            call.replace('Aspect(address=', 'Aspect(name="Schema", address='),
            call.replace('address=', 'address=read(').replace('))', ')))'),
        )
        for item in invalid:
            with self.subTest(item=item), self.assertRaises(NativeModelClaimError):
                parse_native_model_claim(prefix + item)
        with self.assertRaises(NativeModelClaimError):
            parse_native_model_claim('from caprmedio.formal_claims import declare_entity\n' + call)

    def test_named_instance_check_is_preserved_without_execution(self):
        claim = '''
from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

def check_scope_unit(unit: ScopeUnit) -> bool:
    raise RuntimeError("must not run while reading")

declare_entity(entity_name="Scope Unit", instance_check=check_scope_unit)
'''
        result = parse_native_model_claim(claim)
        check = result["instance_check"]
        self.assertEqual(result["arguments"]["instance_check"], "check_scope_unit")
        self.assertEqual((check["name"], check["parameter"], check["parameter_type"]),
                         ("check_scope_unit", "unit", "ScopeUnit"))
        self.assertIn('raise RuntimeError("must not run while reading")', check["source"])
        self.assertNotIn("caprmedio.model", sys.modules)

    def test_invalid_instance_checks_are_rejected(self):
        prefix = ("from caprmedio.formal_claims import declare_entity\n"
                  "from caprmedio.model import ScopeUnit\n")
        cases = (
            'def check(unit: ScopeUnit) -> bool:\n    return True\n'
            'declare_entity(entity_name="Scope Unit", instance_check="check")',
            'def check(unit: ScopeUnit) -> bool:\n    return True\n'
            'declare_entity(entity_name="Scope Unit", instance_check=ScopeUnit)',
            'def check(unit: ScopeUnit) -> str:\n    return "yes"\n'
            'declare_entity(entity_name="Scope Unit", instance_check=check)',
            'def check(unit: str) -> bool:\n    return True\n'
            'declare_entity(entity_name="Scope Unit", instance_check=check)',
            'def check(unit: ScopeUnit, other: ScopeUnit) -> bool:\n    return True\n'
            'declare_entity(entity_name="Scope Unit", instance_check=check)',
            'def check(unit: ScopeUnit = None) -> bool:\n    return True\n'
            'declare_entity(entity_name="Scope Unit", instance_check=check)',
            'def check(unit: ScopeUnit) -> bool:\n    return True\n'
            'declare_entity(entity_name="Scope Unit")',
        )
        for case in cases:
            with self.subTest(case=case), self.assertRaises(NativeModelClaimError):
                parse_native_model_claim(prefix + case)

    def test_nested_cardinality_and_dataclass_fields_are_preserved(self):
        claim = '''
from dataclasses import dataclass, field
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Atom

@dataclass(kw_only=True)
class Method(Atom):
    label: str | None = None
    tags: list[str] = field(default_factory=list)

declare_entity(
    entity_class=Method,
    entity_name="Method",
    value_cardinality=Cardinality(minimum=0, maximum=1),
    instance_relation_constraints={"HAS_PROPERTY": {"targets_per_source": 1}},
)
'''
        result = parse_native_model_claim(claim)
        self.assertEqual({"minimum": 0, "maximum": 1}, result["arguments"]["value_cardinality"])
        self.assertEqual({"HAS_PROPERTY": {"targets_per_source": 1}},
                         result["arguments"]["instance_relation_constraints"])
        self.assertEqual(("Atom",), result["classes"][0]["bases"])
        self.assertEqual("str | None", result["classes"][0]["fields"][0]["annotation"])
        self.assertEqual({"default_factory": "list"}, result["classes"][0]["fields"][1]["field"])
        self.assertEqual({"kw_only": True}, result["classes"][0]["dataclass"])

    def test_root_class_and_nested_dataclass_records(self):
        claim = '''
from dataclasses import dataclass
from caprmedio.formal_claims import declare_entity

@dataclass(kw_only=True)
class AtomHeader:
    label: str | None = None

@dataclass(kw_only=True)
class Atom:
    header: AtomHeader

declare_entity(entity_class=Atom, entity_name="Atom")
'''
        result = parse_native_model_claim(claim)
        self.assertEqual((), result["classes"][0]["bases"])
        self.assertEqual((), result["classes"][1]["bases"])
        self.assertEqual("AtomHeader", result["classes"][1]["fields"][0]["annotation"])

    def test_relation_endpoint_flags_and_model_scopes(self):
        claim = '''
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name="CARRIES",
    source_endpoint={"level": "model_entities", "classification_axis": True},
    target_endpoint={"level": "instances", "ephemeral": False},
)
'''
        result = parse_native_model_claim(claim)
        self.assertIs(result["arguments"]["source_endpoint"]["classification_axis"], True)
        self.assertIs(result["arguments"]["target_endpoint"]["ephemeral"], False)

    def test_legacy_claim_is_identified_for_existing_reader(self):
        self.assertIsNone(parse_native_model_claim('property_rule(address="Atom.Name", values="1")'))

    def test_invalid_and_executable_forms_are_rejected(self):
        claims = (
            'from caprmedio.formal_claims import declare_entity\n'
            'declare_entity(entity_name="Name", base_path=__import__("os").getcwd())',
            'from caprmedio.formal_claims import declare_entity\n'
            'declare_entity(entity_name="A")\nopen("/tmp/pwned", "w")',
            'from caprmedio.formal_claims import declare_entity\n'
            'if True:\n    declare_entity(entity_name="A")',
            'from caprmedio.formal_claims import declare_entity\n'
            'declare_entity(entity_name="A")\ndeclare_entity(entity_name="B")',
            'from caprmedio.formal_claims import Cardinality, declare_entity\n'
            'declare_entity(entity_name="A", value_cardinality=Cardinality(minimum=2, maximum=1))',
            'from caprmedio.formal_claims import declare_entity\n'
            'class Bad(object):\n    x = open("/tmp/pwned", "w")\n'
            'declare_entity(entity_name="Bad", entity_class=Bad)',
        )
        for claim in claims:
            with self.subTest(claim=claim):
                with self.assertRaises(NativeModelClaimError):
                    parse_native_model_claim(claim)

    def test_unknown_names_and_duplicate_keyword_fail_with_line(self):
        source = ('from caprmedio.formal_claims import declare_entity\n'
                  'declare_entity(entity_name="Name", value_format=Missing)\n')
        with self.assertRaisesRegex(NativeModelClaimError, "line 2.*unbound symbol: Missing"):
            parse_native_model_claim(source)
        source = ('from caprmedio.formal_claims import declare_entity\n'
                  'declare_entity(entity_name="Name", entity_name="Name")\n')
        with self.assertRaisesRegex(NativeModelClaimError, "duplicate argument"):
            parse_native_model_claim(source)

    def test_invalid_cardinality_and_property_bearer_are_rejected(self):
        prefix = 'from caprmedio.formal_claims import declare_entity\n'
        invalid = (
            'declare_entity(entity_name="Name", relation_name="IS_PROPERTY_OF")',
            'declare_entity(entity_name="Name", relation_name="IS_PROPERTY_OF", base_path=" ")',
            'declare_entity(entity_name="Name", value_cardinality=-1)',
            'declare_entity(entity_name="Name", value_cardinality=True)',
            'declare_entity(entity_name="Name", value_cardinality="1")',
            'declare_entity(entity_name="Name", '
            'instance_relation_constraints={"CONTAINS": {"targets_per_source": -1}})',
            'declare_entity(entity_name="Name", '
            'instance_property_constraints={"Name": {"value_cardinality": {"minimum": 2, "maximum": 1}}})',
        )
        for claim in invalid:
            with self.subTest(claim=claim), self.assertRaises(NativeModelClaimError):
                parse_native_model_claim(prefix + claim)

    def test_invalid_relation_endpoints_are_rejected(self):
        prefix = 'from caprmedio.formal_claims import declare_relation\n'
        valid = '{"level": "instances"}'
        invalid = (
            'None',
            '{"level": "unknown"}',
            '{"level": "instances", "extra": "unexpected"}',
            '{"level": "instances", "entity_paths": "Atom"}',
            '{"level": "instances", "entity_paths": ("",)}',
            '{"level": "instances", "classification_axis": 1}',
            '{"level": "instances", "ephemeral": "false"}',
        )
        for endpoint in invalid:
            for side in ("source_endpoint", "target_endpoint"):
                other = "target_endpoint" if side == "source_endpoint" else "source_endpoint"
                claim = (f'declare_relation(relation_name="R", {side}={endpoint}, '
                         f'{other}={valid})')
                with self.subTest(side=side, endpoint=endpoint), self.assertRaises(NativeModelClaimError):
                    parse_native_model_claim(prefix + claim)


if __name__ == "__main__":
    unittest.main()
