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

    def test_helpers_require_relation_registry_and_explicit_delivery_alias(self):
        addresses = ["Atom", "Atom.Name"]
        def lint(source, names, **kwargs):
            return lint_python_model_claim(source, declared_addresses=addresses, relation_names=names, **kwargs)
        self.assertIn("CONTAINS", lint('composition(container="Atom", parts=("Atom.Name",))', [])[0])
        self.assertIn("HAS_CLASSIFICATION", lint('classify(address="Atom", axis="Role", value="Method")', [])[0])
        self.assertIn("IS_ORDERED_RIGHT_BEFORE", lint('order_before(first="Atom", second="Atom.Name")', [])[0])
        delivery = 'deliver(source="Atom", carrier="Atom.Name")'
        self.assertIn("unresolved Relation alias: >>", lint(delivery, [])[0])
        self.assertEqual(lint(delivery, ["DELIVERS"], relation_aliases={">>": "DELIVERS"}), ())
        self.assertEqual(lint('relation(source="Atom", name="*")', []), ())

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
