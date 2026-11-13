"""Tests for the static Python Claim lint entry point."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
from lint_python_model_claim import _names, lint_python_model_claim


class LintPythonModelClaimTests(unittest.TestCase):
    def lint(self, source):
        return lint_python_model_claim(source, declared_addresses=["CAPRMEDIO_MODEL <+ Atom.Name", "Atom"],
                                       relation_names=["HAS_PROPERTY"], path="test.md", first_line=10)

    def test_known_reference_and_relation(self):
        self.assertEqual(self.lint('relation(source="Atom", name="HAS_PROPERTY", target="Atom.Name")'), ())

    def test_unknown_reference_and_relation_with_location(self):
        self.assertIn('test.md:11:', self.lint('\nproperty_rule(address="Atom.Missing")')[0])
        self.assertIn('unknown address', self.lint('property_rule(address="Atom.Missing")')[0])
        self.assertIn('unknown Relation: WRONG', self.lint('relation(source="Atom", name="WRONG")')[0])

    def test_unsupported_qualification_is_explicit(self):
        self.assertIn('unknown address', self.lint('subject_path(address="Node.**")')[0])

    def test_qualifier_wildcard_and_bound_instance(self):
        addresses = ["Atom", "Atom.Header.Context.Role", "Atom.Content.Claim"]
        source = ("subject_path(address='Atom/(.Header.Context.Role := Method).Content.Claim')\n"
                  "subject_path(address='Atom.**')\n"
                  "subject_path(address='Atom//$a')\n"
                  "subject_path(address='a.Content.Claim')")
        self.assertEqual(lint_python_model_claim(source, declared_addresses=addresses, relation_names=[]), ())
        result = lint_python_model_claim(source, declared_addresses=["Atom", "Atom.Content.Claim"], relation_names=[])
        self.assertIn("unknown qualifier Property", result[0])

    def test_membership_and_named_scope_references(self):
        source = (
            "subject_path(address='Atom/(.Role in (Method, Evaluation)).Content.*')\n"
            "subject_path(address='(Atom, Atom.Content.**)')\n"
            "set_value(address='Scope Unit//TOOLS.Name', value='TOOLS')"
        )
        declared = ["Atom", "Atom.Role", "Atom.Content", "Scope Unit//TOOLS", "Scope Unit.Name"]
        self.assertEqual(lint_python_model_claim(source, declared_addresses=declared, relation_names=[]), ())
        diagnostics = lint_python_model_claim(source, declared_addresses=declared[:-2] + ["Scope Unit.Name"],
                                              relation_names=[])
        self.assertIn("unknown instance: Scope Unit//TOOLS", diagnostics[0])

    def test_graph_proven_short_and_exact_qualified_addresses(self):
        workflow = "Atom/(.Header.Context.Role:=Operations)/Workflow"
        step = "Atom/(.Header.Context.Role:=Operations)/Step"
        projected = workflow + ".Header.Context.Form"
        addresses = ["Atom", "Atom.Header.Context.Role", workflow, step, projected, "Workflow Run"]
        source = ("subject_path(address='Atom/(.Header.Context.Role in (Operations))/Workflow')\n"
                  "allowed_values(address='Workflow.Header.Context.Form', values=('Workflow',), occurrences='1')\n"
                  "relation(source='Workflow//$workflow', name='CONTAINS', target='Step//$step', source_count='1+')\n"
                  "relation(source='Workflow Run//$run', name='CONTAINS', target='Workflow//$workflow')")
        kwargs = dict(declared_addresses=addresses, relation_names=['CONTAINS'], python_class_bindings={},
                      address_bindings={'Workflow': workflow, 'Step': step})
        self.assertEqual((), lint_python_model_claim(source, **kwargs))
        self.assertEqual((), lint_python_model_claim(source, declared_addresses=addresses,
                                                     relation_names=['CONTAINS'],
                                                     address_bindings={'Workflow': workflow, 'Step': step}))
        self.assertTrue(lint_python_model_claim(source, declared_addresses=addresses,
                                               relation_names=['CONTAINS'], python_class_bindings={}))
        self.assertTrue(lint_python_model_claim("subject_path(address='Workflow.Header.Missing')", **kwargs))
        self.assertTrue(lint_python_model_claim("subject_path(address='Atom/(.Header.Context.Role in (Method))/Workflow')", **kwargs))
        self.assertTrue(lint_python_model_claim("subject_path(address='Atom/(.Header.Context.Role in (Operations, Method))/Workflow')", **kwargs))
        self.assertTrue(lint_python_model_claim("subject_path(address='Atom/(.Header.Context.Role:=Operations)/Missing')", **kwargs))

    def test_qualified_catalog_entry_requires_declared_qualifier_property(self):
        qualified = "Atom/(.Missing:=X)/Workflow"
        options = dict(declared_addresses=['Atom', qualified], relation_names=[],
                       address_bindings={'Workflow': qualified})
        for reference in (qualified, "Workflow", "Atom/(.Missing in (X))/Workflow//$x"):
            result = lint_python_model_claim(f"subject_path(address={reference!r})", **options)
            self.assertIn("unknown qualifier Property: Atom.Missing", result[0])
        chain = "Atom <+ " + qualified
        options['declared_addresses'].append(chain)
        result = lint_python_model_claim(f"subject_path(address={chain!r})", **options)
        self.assertIn("unknown qualifier Property: Atom.Missing", result[0])
        options['declared_addresses'].append('Atom.Missing')
        self.assertEqual((), lint_python_model_claim(f"subject_path(address={qualified!r})", **options))

    def test_graph_bindings_keep_variable_identity_and_local_property(self):
        workflow = "Atom/(.Header.Context.Role:=Operations)/Workflow"
        step = "Atom/(.Header.Context.Role:=Operations)/Step"
        addresses = ["Atom", "Atom.Header.Context.Role", workflow, step,
                     workflow + ".Content.Claim", "Workflow.Content.Claim"]
        kwargs = dict(declared_addresses=addresses, relation_names=[], python_class_bindings={},
                      address_bindings={'Workflow': workflow, 'Step': step})
        for source in (
            "subject_path(address='Workflow//$x')\n"
            "subject_path(address='Atom/(.Header.Context.Role:=Operations)/Workflow//$x')",
            "subject_path(address='Atom/(.Header.Context.Role:=Operations)/Workflow//$x')\n"
            "subject_path(address='Workflow//$x')",
        ):
            self.assertEqual((), lint_python_model_claim(source, **kwargs))
        self.assertEqual((), lint_python_model_claim("subject_path(address='Workflow.Content.Claim')", **kwargs))
        mismatch = ("subject_path(address='Workflow//$x')\n"
                    "subject_path(address='Step//$x')")
        self.assertIn("inconsistent binding", lint_python_model_claim(mismatch, **kwargs)[0])

    def test_graph_bindings_fail_closed_for_missing_and_conflicting_aliases(self):
        workflow = "Atom/(.Header.Context.Role:=Operations)/Workflow"
        options = dict(declared_addresses=['Atom', workflow], relation_names=[], python_class_bindings={})
        claim = "subject_path(address='Workflow')"
        self.assertTrue(lint_python_model_claim(claim, **options))
        self.assertTrue(lint_python_model_claim(claim, address_bindings={'Workflow': 'Missing'}, **options))
        self.assertTrue(lint_python_model_claim(claim, address_bindings={'Workflow': workflow},
                                                declared_addresses=['Atom', workflow, 'Workflow'],
                                                relation_names=[], python_class_bindings={}))
        self.assertTrue(lint_python_model_claim(claim, address_bindings={'Workflow': ['bad']}, **options))

    def test_set_value_validates_relation_alias_without_changing_expression(self):
        from python_model_claim import parse_grouped_python_model_claim
        options = dict(declared_addresses=['Relation'], relation_names=['NARROWER_THAN', 'HAS_NARROWER'])
        source = "# model\nset_value(address='alias(Relation//NARROWER_THAN)', value='\"/\"')"
        self.assertEqual((), lint_python_model_claim(source, **options))
        self.assertEqual((('alias(Relation//NARROWER_THAN) == \"/\"', 'model'),),
                         parse_grouped_python_model_claim(source))
        inverse = "set_value(address='alias(Relation//HAS_NARROWER)', value='/')"
        self.assertEqual((), lint_python_model_claim(inverse, **options))
        invalid = (
            "set_value(address='alias(Relation//narrower_than)', value='/')",
            "set_value(address='alias(Relation//MISSING)', value='/')",
            "set_value(address='alias(Relation/NARROWER_THAN)', value='/')",
            "set_value(address='alias(Relation//NARROWER_THAN', value='/')",
            "set_value(address='alias(Relation//NARROWER_THAN)', value='')",
            "set_value(address='alias(Relation//NARROWER_THAN)', value='\"\"')",
            "set_value(address='alias(Relation//NARROWER_THAN)', value=1)",
        )
        for claim in invalid:
            with self.subTest(claim=claim):
                self.assertTrue(lint_python_model_claim(claim, **options))

    def test_helpers_require_relation_registry_and_delivery_operator(self):
        addresses = ["Atom", "Atom.Name"]
        def lint(source, names, **kwargs):
            return lint_python_model_claim(source, declared_addresses=addresses, relation_names=names, **kwargs)
        self.assertIn("CONTAINS", lint('composition(container="Atom", parts=("Atom.Name",))', [])[0])
        self.assertIn("HAS_CLASSIFICATION", lint('classify(address="Atom", axis="Role", value="Method")', [])[0])
        self.assertIn("IS_ORDERED_RIGHT_BEFORE", lint('order_before(first="Atom", second="Atom.Name")', [])[0])
        delivery = 'deliver(source="Atom", carrier="Atom.Name")'
        self.assertIn("missing or ambiguous Delivery operator", lint(delivery, [])[0])
        self.assertEqual(lint(delivery, [], operator_catalog={"Delivery": [">>"]}), ())
        for symbols in ([], [">>", ">>"], [">>", "->"], ["->"]):
            self.assertIn("missing or ambiguous Delivery operator", lint(delivery, [], operator_catalog={"Delivery": symbols})[0])
        self.assertIn("unknown carrier", lint('deliver(source="Atom", carrier="Missing")', [], operator_catalog={"Delivery": [">>"]})[0])
        self.assertIn("missing or ambiguous Delivery operator", lint(delivery, ["DELIVERS"], relation_aliases={">>": "DELIVERS"})[0])
        self.assertEqual(lint('relation(source="Atom", name="*")', []), ())

    def test_cli_delivery_operator_catalog(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            addresses, relations, operators, claim = (root / name for name in ("addresses.json", "relations.json", "operators.json", "claim.py"))
            addresses.write_text(json.dumps(["Atom", "Carrier"]))
            relations.write_text("[]")
            operators.write_text(json.dumps({"Delivery": [">>"]}))
            claim.write_text('deliver(source="Atom", carrier="Carrier")')
            command = [sys.executable, str(TOOLS / "lint_python_model_claim.py"), str(claim), "--addresses", str(addresses), "--relations", str(relations), "--operators", str(operators)]
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            operators.write_text(json.dumps({"Delivery": [">>", ">>"]}))
            result = subprocess.run(command, capture_output=True, text=True)
            self.assertEqual(result.returncode, 1)
            self.assertIn("missing or ambiguous Delivery operator", result.stderr)

    def test_registry_inverse_alias_must_reference_registered_relation(self):
        with tempfile.TemporaryDirectory() as tmp:
            registry = Path(tmp) / "registry.json"
            registry.write_text(json.dumps({"registered_names": ["CONTAINS"], "inverse_aliases":
                                            [{"alias": "IS_IN", "canonical": "CONTAINS"}]}))
            self.assertEqual(_names(registry, registry=True), ["CONTAINS", "IS_IN"])
            registry.write_text(json.dumps({"registered_names": [], "inverse_aliases":
                                            [{"alias": "IS_IN", "canonical": "MISSING"}]}))
            with self.assertRaises(ValueError):
                _names(registry, registry=True)

    def test_python_is_never_executed(self):
        self.assertTrue(self.lint('__import__("os").system("exit 1")'))

    def test_cli_reads_markdown_formal_claim_and_relation_registry(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            addresses = tmp / 'addresses.json'
            relations = tmp / 'relations.json'
            claim = tmp / 'atom.md'
            addresses.write_text(json.dumps(["Atom"]))
            relations.write_text(json.dumps({"registered_names": ["KNOWN"]}))
            claim.write_text('## Claim\n### Formal Claim\n```python\nrelation(source="Atom", name="MISSING")\n```\n')
            result = subprocess.run([sys.executable, str(TOOLS / 'lint_python_model_claim.py'), str(claim),
                                     '--addresses', str(addresses), '--relations', str(relations)],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 1, result.stderr)
            self.assertIn(f'{claim}:4:', result.stderr)
            self.assertIn('unknown Relation: MISSING', result.stderr)


if __name__ == '__main__':
    unittest.main()
