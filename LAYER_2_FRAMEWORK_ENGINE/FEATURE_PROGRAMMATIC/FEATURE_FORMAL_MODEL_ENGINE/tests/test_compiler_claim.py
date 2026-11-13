"""Native declarations retain the existing compilers' explicit inputs."""

from pathlib import Path
import sys
import unittest


FEATURE = Path(__file__).resolve().parents[1]
PROGRAMMATIC = FEATURE.parent
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
WORKBENCH = PROGRAMMATIC / "FEATURE_APPS" / "APP_WORKBENCH"
sys.path[:0] = [str(PROGRAMMATIC), str(TOOLS), str(WORKBENCH)]

from FEATURE_FORMAL_MODEL_ENGINE.compiler_claim import compiler_model_statements  # noqa: E402
from FEATURE_FORMAL_MODEL_ENGINE.native_model_claim import parse_native_model_claim  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.content_schema import compile_content_schema, declaration_statements  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.declared_header_rules import header_declaration_rules  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.relation_registry import compile_relation_registry, registry_contribution  # noqa: E402
from FEATURE_WORKBENCH_BACKEND.relations import _outgoing_facts  # noqa: E402
from ATOM_LIFECYCLE.content_constraints import compile_content_constraints  # noqa: E402
from ATOM_LIFECYCLE.header_constraints import compile_header_constraints, load_header_constraints  # noqa: E402
from ATOM_LIFECYCLE.role_form_schema import compile_role_form  # noqa: E402
from python_model_claim import compile_python_model_claim, compile_atom_dependencies_claim_with_check  # noqa: E402
from role_directory_rules import compile_role_folders  # noqa: E402


def _compile(source):
    return compiler_model_statements(parse_native_model_claim(source))


def _body(statements):
    return "## Claim\n\n### Formal Claim\n\n```CFEL\n" + ";\n".join(statements) + ";\n```\n"


def _row(statements):
    body = _body(statements)
    return {"id": "CA-R-1", "ref": "CA-R-1", "version": 1, "source_path": "source.md",
            "status_group": "Current", "role": "Requirement", "form": "Declaration",
            "_content_bytes": body.encode(), "content_markdown": body}


class CompilerClaimTests(unittest.TestCase):
    def test_explicit_atom_dependencies_consumer_keeps_callback_metadata(self):
        claim = """from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Atom

def dependencies_are_distinct(atom: Atom) -> bool:
    return len(atom.dependencies) == len(set(atom.dependencies))

declare_entity(entity_name="Dependencies", relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context.Topics",
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_format=str, value_cardinality=Cardinality(minimum=0, maximum=None),
    dependent_property_cardinality=0, instance_check=dependencies_are_distinct)
"""
        statements, check = compile_atom_dependencies_claim_with_check(claim)
        self.assertEqual(statements, (
            "Atom.Header.Context.Topics.Dependencies{::0..1} :: [string]{::0+}",
            "Atom.Header.Context.Topics.Dependencies.*[]{::0}",
        ))
        self.assertEqual(check["name"], "dependencies_are_distinct")
        self.assertEqual(check["parameter_type"], "Atom")
        self.assertEqual(statements, compile_python_model_claim(claim))
        with self.assertRaisesRegex(ValueError, "typed Atom Dependencies validator"):
            compile_atom_dependencies_claim_with_check(claim.replace('entity_name="Dependencies"', 'entity_name="Other"'))
        with self.assertRaisesRegex(ValueError, "typed Atom Dependencies validator"):
            compile_atom_dependencies_claim_with_check(claim.replace("dependencies_are_distinct", "other_check"))

    def test_aspect_instance_compiles_exact_structure_facts(self):
        address = "PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Query Processing"
        claim = ("from caprmedio.formal_claims import declare_entity\n"
                 "from caprmedio.model import Aspect\n"
                 f"declare_entity(entity_name='Query Processing', instance=Aspect(address={address!r}))\n")
        self.assertEqual((address, f"({address}) ((INSTANCE_OF)) Aspect"), _compile(claim))
        from lint_python_model_claim import lint_python_model_claim
        self.assertEqual((), lint_python_model_claim(claim, declared_addresses=["Aspect"], relation_names=[], python_class_bindings={"Aspect": ["Aspect"]}))
        invalid_claim = claim.replace("<+ Aspects <+", "<+ Invalid <+")
        self.assertTrue(lint_python_model_claim(invalid_claim, declared_addresses=["Aspect"], relation_names=[], python_class_bindings={"Aspect": ["Aspect"]}))
        from copy import deepcopy
        parsed = parse_native_model_claim(claim)
        for invalid in ("Atom <+ Aspects <+ Query Processing", "PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Other"):
            modified = deepcopy(parsed)
            modified["arguments"]["instance"]["fields"]["address"] = invalid
            with self.assertRaisesRegex(ValueError, "invalid Aspect instance address"):
                compiler_model_statements(modified)

    def test_allowed_classification_values_are_not_fixed_classifications(self):
        claim = """from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Node", allowed_classification_values={"Container": ("yes", "no")})
"""
        self.assertEqual(("Node >| Container: yes", "Node >| Container: no"), _compile(claim))
        for bad in ('("yes", "yes")', '()', '["yes"]'):
            with self.assertRaises(ValueError):
                _compile(claim.replace('("yes", "no")', bad))
        with self.assertRaises(ValueError):
            _compile(claim.replace('entity_name="Node",', 'entity_name="Node", classifications={"Container": "yes"},'))

    def test_same_bearer_fallback_requires_a_declared_property(self):
        from lint_python_model_claim import lint_python_model_claim

        claim = """from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Label", relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context", value_format=str, fallback_property_name="Form")
"""
        self.assertIn("$atom.Header.Context.Label ?== $atom.Header.Context.Form", _compile(claim))
        addresses = {"Atom.Header.Context", "Atom.Header.Context.Label", "Atom.Header.Context.Form"}
        relations = {"IS_PROPERTY_OF"}
        self.assertEqual((), lint_python_model_claim(claim, declared_addresses=addresses, relation_names=relations))
        missing = addresses - {"Atom.Header.Context.Form"} | {"Other.Header.Context.Form"}
        diagnostics = lint_python_model_claim(claim, declared_addresses=missing, relation_names=relations)
        self.assertIn("unknown declared fallback Property: Atom.Header.Context.Form", diagnostics[0])

    def test_base_status_claim_preserves_values_and_order_numbers(self):
        claim = """from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Status", relation_name="IS_PROPERTY_OF", base_path="Atom.Header.State",
               property_occurrence_cardinality=1, value_format=str, value_cardinality=1,
               dependent_property_cardinality=0, allowed_values=("Draft", "Active", "Archived"),
               status_order_numbers={"Draft": 0, "Archived": 99})
"""
        self.assertEqual((
            "Atom.Header.State.Status{::1} :: [string]{::1}",
            "Atom.Header.State.Status.*[]{::0}",
            "Atom.Header.State.Status :: Draft",
            "Atom.Header.State.Status :: Active",
            "Atom.Header.State.Status :: Archived",
            "Atom/(.Header.State.Status := Draft).Header.State.Status >| (Status Order Number == 0)",
            "Atom/(.Header.State.Status := Archived).Header.State.Status >| (Status Order Number == 99)",
        ), _compile(claim))
        with self.assertRaisesRegex(ValueError, "invalid base Status Order Numbers"):
            _compile(claim.replace('"Archived": 99', '"Archived": 0'))

    def test_projection_form_preserves_admitted_value_and_selector(self):
        claim = """from caprmedio.formal_claims import declare_entity
from caprmedio.model import Projection

class Map(Projection):
    pass

declare_entity(entity_class=Map, entity_name="Map", qualification_property_path="Projection.Form")
"""
        self.assertEqual(("Projection.Form :: Map", "Projection/(.Form in (Map))"), _compile(claim))
        with self.assertRaisesRegex(ValueError, "Projection as its sole base"):
            _compile(claim.replace("import Projection", "import Atom").replace("Map(Projection)", "Map(Atom)"))

    def test_property_bearer_uses_a_qualified_model_path(self):
        def compile_property(base):
            return _compile(
                "from caprmedio.formal_claims import declare_entity\n"
                f"declare_entity(entity_name='Mermaid Scheme', relation_name='IS_PROPERTY_OF', base_path={base!r})"
            )

        base = "Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step).Content.Claim"
        self.assertEqual((f"{base}.Mermaid Scheme",), compile_property(base))
        self.assertEqual(("Step.Content.Claim.Mermaid Scheme",), compile_property("Step.Content.Claim"))
        for invalid in ("Atom//Step", f"{base};Injected", f"{base}{{::1}}"):
            with self.subTest(invalid=invalid), self.assertRaisesRegex(ValueError, "unsupported compiler name"):
                compile_property(invalid)

    def test_content_property_contributes_same_roles_and_cardinalities(self):
        native = '''
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Requirement, Method, Evaluation, Delivery
declare_entity(entity_name="Semantics", relation_name="IS_PROPERTY_OF", base_path="Atom.Content",
    value_cardinality=Cardinality(minimum=0, maximum=1), dependent_property_cardinality=0,
    applies_to_entity_classes=(Requirement, Method, Evaluation, Delivery))
'''
        old = _row(("Atom/(.Header.Context.Role in RMED).Content.Semantics :: {::0..1}",
                    "Atom/(.Header.Context.Role in RMED).Content.Semantics.*[]{::0}"))
        new = _row(_compile(native))
        self.assertEqual(compile_content_schema([old]), compile_content_schema([new]))
        self.assertEqual(compile_content_constraints([old]), compile_content_constraints([new]))

    def test_recursive_content_and_role_scoped_ordering(self):
        native = '''
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Requirement, Method, Evaluation, Delivery
declare_entity(entity_name="Content", relation_name="IS_PROPERTY_OF", base_path="Atom",
    property_occurrence_cardinality=1, value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=0, maximum=None), dependent_property_name_format=str,
    recursive_dependent_property_cardinality=Cardinality(minimum=0, maximum=None),
    recursive_dependent_property_name_format=str, recursive_dependent_property_value_format="markdown",
    ordered_dependent_property_roles=(Requirement, Method, Evaluation, Delivery),
    ordered_dependent_property_pairs=(("Summary", "Claim"), ("Claim", "Semantics"), ("Semantics", "Details")))
'''
        prefix = "Atom/(.Header.Context.Role in (Requirement, Method, Evaluation, Delivery)).Content"
        expected = (
            "Atom.Content{::1} :: []{::0}",
            "Atom.Content.*[string]{::0+}",
            "Atom.Content.**[string]{::0+}",
            "Atom.Content.** :: [markdown]",
            f"{prefix}.Summary ;> {prefix}.Claim",
            f"{prefix}.Claim ;> {prefix}.Semantics",
            f"{prefix}.Semantics ;> {prefix}.Details",
        )
        self.assertEqual(expected, _compile(native))
        legacy_prefix = "Atom/(.Header.Context.Role in RMED).Content"
        legacy = (*expected[:4], f"{legacy_prefix}.Summary ;> {legacy_prefix}.Claim",
                  f"{legacy_prefix}.Claim ;> {legacy_prefix}.Semantics",
                  f"{legacy_prefix}.Semantics ;> {legacy_prefix}.Details")
        self.assertEqual(compile_content_schema([_row(legacy)]), compile_content_schema([_row(expected)]))
        self.assertEqual(compile_content_constraints([_row(legacy)]), compile_content_constraints([_row(expected)]))
        with self.assertRaisesRegex(ValueError, "invalid recursive_dependent_property_cardinality cardinality"):
            _compile(native.replace("recursive_dependent_property_cardinality=Cardinality(minimum=0, maximum=None)",
                                    "recursive_dependent_property_cardinality=-1"))
        with self.assertRaisesRegex(ValueError, "name format requires cardinality"):
            _compile(native.replace("recursive_dependent_property_cardinality=Cardinality(minimum=0, maximum=None),", ""))
        with self.assertRaisesRegex(ValueError, "must be acyclic"):
            _compile(native.replace('("Semantics", "Details")', '("Semantics", "Summary")'))
        with self.assertRaisesRegex(ValueError, "must name distinct allowed children"):
            _compile(native.replace('ordered_dependent_property_roles=(Requirement, Method, Evaluation, Delivery),',
                                    'allowed_dependent_property_names=("Summary", "Claim"),'))

    def test_nested_content_property_preserves_role_selection(self):
        native = """
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Requirement, Method, Evaluation, Delivery

declare_entity(
    entity_name="Prose Claim",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Content.Claim",
    value_cardinality=Cardinality(minimum=0, maximum=1),
    dependent_property_cardinality=0,
    applies_to_entity_classes=(Requirement, Method, Evaluation, Delivery),
)
"""
        old = _row(("Atom/(.Header.Context.Role in RMED).Content.Claim.Prose Claim:: {::0..1}",
                    "Atom/(.Header.Context.Role in RMED).Content.Claim.Prose Claim.*[]{::0}"))
        new = _row(_compile(native))
        self.assertEqual(compile_content_schema([old]), compile_content_schema([new]))
        self.assertEqual(compile_content_constraints([old]), compile_content_constraints([new]))

    def test_nested_header_constraints_and_wildcard_formats(self):
        native = '''
from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="File", relation_name="IS_PROPERTY_OF", base_path="Atom.Header.Destination",
    property_occurrence_cardinality=1, value_cardinality=0, dependent_property_cardinality=2,
    allowed_dependent_property_names=("Name", "Path"), dependent_property_value_format=str)
'''
        old = _row(("Atom.Header.Destination.File{::1} :: []{::0}",
                    "Atom.Header.Destination.File.*[in (Name, Path)]{::2}",
                    "Atom.Header.Destination.File.* :: [string]"))
        new = _row(_compile(native))
        self.assertEqual(header_declaration_rules(old), header_declaration_rules(new))
        self.assertEqual(compile_header_constraints([old]), compile_header_constraints([new]))

    def test_header_relations_child_value_cardinality(self):
        native = '''
from caprmedio.formal_claims import Cardinality, declare_entity
declare_entity(entity_name="Relations", relation_name="IS_PROPERTY_OF", base_path="Atom.Header",
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1), value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=1, maximum=None),
    dependent_property_name_format=str, dependent_property_value_format=str,
    dependent_property_value_cardinality=Cardinality(minimum=1, maximum=None))
'''
        expected = (
            "Atom.Header.Relations{::0..1} :: []{::0}",
            "Atom.Header.Relations.*[string]{::1+}",
            "Atom.Header.Relations.* :: [string]{::1+}",
        )
        self.assertEqual(expected, _compile(native))
        constraints = compile_header_constraints([_row(_compile(native))])
        self.assertEqual(compile_header_constraints([_row(expected)]), constraints)
        validator = load_header_constraints(constraints, {"CA-R-1"})
        valid = {"role": "Requirement", "relations": {"related": ["CA-R-2"]}}
        empty = {"role": "Requirement", "relations": {"related": []}}
        self.assertEqual([], validator.validate(valid, metadata=valid))
        self.assertTrue(any(field == "relations.related" for field, _, _ in validator.validate(empty, metadata=empty)))
        self.assertEqual(
            "Atom.Header.Relations.* :: [string]",
            _compile(native.replace("    dependent_property_value_cardinality=Cardinality(minimum=1, maximum=None)", ""))[-1],
        )
        bounded = native.replace("dependent_property_value_cardinality=Cardinality(minimum=1, maximum=None)",
                                 "dependent_property_value_cardinality=Cardinality(minimum=1, maximum=2)")
        self.assertEqual("Atom.Header.Relations.* :: [string]{::1..2}", _compile(bounded)[-1])
        with self.assertRaisesRegex(ValueError, "invalid dependent_property_value_cardinality cardinality"):
            _compile(native.replace("dependent_property_value_cardinality=Cardinality(minimum=1, maximum=None)",
                                    "dependent_property_value_cardinality=-1"))
        with self.assertRaisesRegex(ValueError, "requires a Property Declaration and value format"):
            _compile(native.replace("dependent_property_value_format=str,", ""))

    def test_nested_header_property_preserves_single_role(self):
        native = """
from caprmedio.formal_claims import Cardinality, declare_entity
from caprmedio.model import Plan

declare_entity(
    entity_name="Plan",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.Context",
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=1, maximum=2),
    allowed_dependent_property_names=("Work Sequence Number", "AI Agent Confidence Threshold"),
    applies_to_entity_classes=(Plan,),
)
"""
        old = _row(("Atom/(.Header.Context.Role in (Plan)).Header.Context.Plan{::0..1} :: []{::0}",
                    "Atom/(.Header.Context.Role in (Plan)).Header.Context.Plan.*"
                    "[in (Work Sequence Number, AI Agent Confidence Threshold)]{::1..2}"))
        new = _row(_compile(native))
        self.assertEqual(header_declaration_rules(old), header_declaration_rules(new))
        self.assertEqual(compile_header_constraints([old]), compile_header_constraints([new]))
        with self.assertRaisesRegex(ValueError, "unsupported Property class selection"):
            _compile(native.replace("(Plan,)", "(Plan, Plan)"))

    def test_role_status_values_inherit_property_shape(self):
        native = """
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Concern

declare_entity(
    entity_name="Status",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom.Header.State",
    applies_to_entity_classes=(Concern,),
    allowed_values=("Resolved", "Canceled"),
    status_order_numbers={"Resolved": 21},
)
"""
        self.assertEqual(
            (
                "Atom/(.Header.Context.Role in (Concern)).Header.State.Status :: Resolved",
                "Atom/(.Header.Context.Role in (Concern)).Header.State.Status :: Canceled",
                "Atom/(.Header.State.Status := Resolved).Header.State.Status >| (Status Order Number == 21)",
            ),
            _compile(native),
        )

    def test_role_order_and_form_are_qualified_by_role(self):
        role = '''
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom
class Method(Atom):
    pass
declare_entity(entity_class=Method, entity_name="Method", qualification_property_path="Atom.Header.Context.Role",
    classifications={"Role Order Number": 5})
'''
        form = '''
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Method
class Decision(Method):
    pass
declare_entity(entity_class=Decision, entity_name="Decision", qualification_property_path="Atom.Header.Context.Form")
'''
        role_row, form_row = _row(_compile(role)), _row(_compile(form))
        expected_role = _row(("Atom.Header.Context.Role :: Method",
                              "Atom/(.Header.Context.Role := Method) >| (Role Order Number == 5)"))
        self.assertEqual(compile_role_form([expected_role]), compile_role_form([role_row]))
        self.assertEqual(compile_role_folders(declaration_statements(expected_role)),
                         compile_role_folders(declaration_statements(role_row)))
        self.assertIn({"kind": "qualified", "value": "Decision", "role": "Method", "source": "CA-R-1"},
                      compile_role_form([form_row]))

    def test_relation_registry_keeps_instance_reverse_views(self):
        native = '''
from caprmedio.formal_claims import declare_relation
declare_relation(relation_name="IS_PROPERTY_OF", inverse_alias="HAS_PROPERTY",
    source_endpoint={"level": "model_entities_or_instances"},
    target_endpoint={"level": "model_entities_or_instances"})
'''
        result = registry_contribution(_row(_compile(native)))
        self.assertEqual(frozenset({"IS_PROPERTY_OF", "HAS_PROPERTY"}), result.names)
        self.assertEqual((), result.aliases)
        self.assertEqual((("IS_PROPERTY_OF", "HAS_PROPERTY"),), result.inverses)

    def test_legacy_and_native_inverses_produce_same_reverse_row(self):
        for relation, inverse in (("CARRIES", "IS_CARRIED_BY"), ("IS_PROPERTY_OF", "HAS_PROPERTY")):
            with self.subTest(relation=relation):
                source = (
                    "from caprmedio.formal_claims import declare_relation\n"
                    f"declare_relation(relation_name='{relation}', inverse_alias='{inverse}', "
                    "source_endpoint={'level': 'instances'}, "
                    "target_endpoint={'level': 'model_entities_or_instances'})"
                )
                native = _row(_compile(source))
                native.update(id="CA-R-2", ref="CA-R-2", source_path="native.md")
                legacy = _row((f"Relation//{relation} ((HAS_INVERSE)) Relation//{inverse}",))
                old = compile_relation_registry([legacy])
                both = compile_relation_registry([legacy, native])
                alone = compile_relation_registry([native])
                self.assertEqual(old.inverse, {relation: inverse})
                self.assertEqual(old.inverse, both.inverse)
                self.assertEqual(old.inverse, alone.inverse)
                self.assertEqual(both.aliases, {})
                fact = ("atom", "CA-R-1", relation, "atom", "CA-R-2")
                expected = ("atom", "CA-R-2", inverse, "atom", "CA-R-1", True)
                self.assertIn(expected, _outgoing_facts([], alone, {"source.md": (fact,)})[("atom", "CA-R-2")])
                self.assertIn(expected, _outgoing_facts([], both, {"source.md": (fact,)})[("atom", "CA-R-2")])

    def test_model_only_inverse_remains_an_alias(self):
        native = '''
from caprmedio.formal_claims import declare_relation
declare_relation(relation_name="IS_ORDERED_RIGHT_AFTER", inverse_alias="IS_ORDERED_RIGHT_BEFORE",
    source_endpoint={"level": "model_entities"},
    target_endpoint={"level": "model_entities"})
'''
        result = registry_contribution(_row(_compile(native)))
        self.assertEqual(frozenset({"IS_ORDERED_RIGHT_AFTER"}), result.names)
        self.assertEqual((("IS_ORDERED_RIGHT_BEFORE", "IS_ORDERED_RIGHT_AFTER"),), result.aliases)
        self.assertEqual((), result.inverses)

    def test_unsafe_or_unsupported_compiler_values_fail(self):
        native = '''
from caprmedio.formal_claims import declare_entity
declare_entity(entity_name="Name", relation_name="IS_PROPERTY_OF", base_path="Atom.Header;Other")
'''
        with self.assertRaisesRegex(ValueError, "unsupported compiler name"):
            _compile(native)

    def test_instance_check_cannot_be_silently_dropped(self):
        native = '''
from caprmedio.formal_claims import declare_entity
from caprmedio.model import Atom

def is_valid_atom(atom: Atom) -> bool:
    return atom.version > 0

declare_entity(entity_name="Atom", instance_check=is_valid_atom)
'''
        parsed = parse_native_model_claim(native)
        self.assertEqual("is_valid_atom", parsed["arguments"]["instance_check"])
        with self.assertRaisesRegex(ValueError, "instance_check requires a typed validator"):
            compiler_model_statements(parsed)
        row = _row(())
        row["_content_bytes"] = (
            "## Claim\n\n### Formal Claim\n\n```python\n" + native + "```\n"
        ).encode()
        with self.assertRaisesRegex(ValueError, "instance_check requires a typed validator"):
            compile_content_schema([row])

    def test_scope_level_schema_compiles_without_calling_its_check(self):
        claim = '''from caprmedio.formal_claims import declare_entity
from caprmedio.model import ScopeUnit

def check_structural_level(unit: ScopeUnit) -> bool:
    return unit.structural_level == 0

declare_entity(entity_name="structural_level", relation_name="IS_PROPERTY_OF",
               base_path="Scope Unit", property_occurrence_cardinality=1,
               value_format=int, value_cardinality=1, instance_check=check_structural_level)
'''
        self.assertEqual(
            ("Scope Unit.structural_level{::1} :: [int]{::1}",),
            compile_python_model_claim(claim),
        )
        with self.assertRaisesRegex(ValueError, "instance_check requires a typed validator"):
            _compile(claim)


if __name__ == "__main__":
    unittest.main()
