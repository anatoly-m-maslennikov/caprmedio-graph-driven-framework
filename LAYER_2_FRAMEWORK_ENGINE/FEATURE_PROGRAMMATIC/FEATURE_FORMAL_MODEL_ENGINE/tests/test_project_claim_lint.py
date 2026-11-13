"""Exercise Python Claim linting against the internal Workbench query API."""

import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from watchdog.observers.polling import PollingObserver

PROGRAMMATIC = Path(__file__).resolve().parents[2]
APPS = PROGRAMMATIC / "FEATURE_APPS"
TOOLS = PROGRAMMATIC / "FEATURE_TOOLS"
sys.path[:0] = [str(PROGRAMMATIC), str(APPS), str(TOOLS), str(TOOLS / "tests"),
                str(APPS / "APP_WORKBENCH"), str(APPS / "APP_WORKBENCH" / "tests")]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService
from FEATURE_FORMAL_MODEL_ENGINE.project_claim_lint import lint_project_claim
from lifecycle_placement_test_support import fixture_rules
from project_selection import resolve_project
from scope_declaration_test_support import write_scope_unit_declarations
from smalltest_support import built_assets, extension_directory, write_settings


class ProjectClaimLintTests(unittest.TestCase):
    @patch("APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_watcher.NativeObserver", PollingObserver)
    def test_current_declarations_authorize_one_selected_claim(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            control = write_settings(root)
            units = write_scope_unit_declarations(root, [{"scope_unit_name": "MAIN"}], control_root=control)
            folder = Path(units["MAIN"]["authority_path"]) / "04_requirement"

            def write(number, subject, claim, *, status="Active", language="python", directory=folder,
                      form="Declaration"):
                directory.mkdir(parents=True, exist_ok=True)
                atom_id = f"CA-R-{number}"
                ref = atom_id if status == "Active" else f"{atom_id}@1-draft"
                if status == "Draft" and form == "Declaration" and number != 14:
                    form = "Rule"
                (directory / f"{ref}-{form.upper()}--fixture.md").write_text(
                    f'---\natom_id: {atom_id}\nrole: Requirement\nform: {form}\n'
                    f'status: {status}\nversion: 1\nupdated_at: "2026-01-01T00:00:00Z"\n'
                    f'subjects:\n  governs: {json.dumps("CAPRMEDIO_MODEL <+ " + subject)}\n---\n'
                    f'\n## Summary\n\nFixture\n\n## Claim\n\n### Formal Claim\n\n'
                    f'```{language}\n{claim}\n```\n', encoding="utf-8",
                )
                return ref

            write(10, "Atom", 'subject_path(address="Atom")')
            write(11, "Atom.Name", 'property_rule(address="Atom.Name", value_format="string")')
            write(12, "Relation//HAS_PROPERTY", "Relation//HAS_PROPERTY;", language="CFEL")
            write(13, "CFEL <+ Operator//Delivery", '# model\nOperator//Delivery == ">>"', language="CFEL",
                  form="Operator Declaration")
            write(14, "Atom.Unapproved", 'property_rule(address="Atom.Unapproved", value_format="string")',
                  status="Draft", directory=folder / "000_draft")
            # An installed copy cannot supply a missing declaration.
            write(15, "Atom.Unapproved", 'property_rule(address="Atom.Unapproved", value_format="string")',
                  directory=control / "installed" / "04_requirement")
            draft = folder / "000_draft"
            good = write(16, "Atom.Name",
                         'relation(source="Atom", name="HAS_PROPERTY", target="Atom.Name")\n'
                         'deliver(source="Atom", carrier="Atom.Name")', status="Draft", directory=draft)
            bad = write(17, "Atom.Name", 'property_rule(address="Atom.Unapproved", value_format="string")',
                        status="Draft", directory=draft)
            unknown_relation = write(18, "Atom.Name", 'relation(source="Atom", name="UNDECLARED")',
                                     status="Draft", directory=draft)
            syntax = write(19, "Atom.Name", 'property_rule(', status="Draft", directory=draft)
            write(20, "Relation//CONTAINS", 'Relation//CONTAINS;\nalias(Relation//CONTAINS) == "<+"', language="CFEL")
            composition = write(21, "Atom.Name", 'composition(container="Atom", parts=("Atom.Name",))',
                                status="Draft", directory=draft)
            write(22, "Relation//HAS_CLASSIFICATION", "Relation//HAS_CLASSIFICATION;", language="CFEL")
            unbound_alias = write(23, "Atom.Name", 'classify(address="Atom", axis="Role", value="Method")',
                                  status="Draft", directory=draft)
            write(24, "Atom.Ambiguous", 'property_rule(address="Atom.Ambiguous", value_format="string")')
            write(25, "Atom.Ambiguous", 'property_rule(address="Atom.Ambiguous", value_format="string")')
            ambiguous = write(26, "Atom.Name", 'subject_path(address="Atom.Ambiguous")',
                              status="Draft", directory=draft)
            operations = "Atom/(.Header.Context.Role := Operations)"
            write(28, "Atom.Header.Context.Role", 'subject_path(address="Atom.Header.Context.Role")')
            write(29, operations, 'subject_path(address="Atom")')
            write(30, operations + "/Workflow", 'subject_path(address="Atom")')
            write(31, operations + "/Step", 'subject_path(address="Atom")')
            write(34, operations + ".Name", 'property_rule(address="Atom.Name", value_format="string")')
            qualified = write(32, "Atom.Name",
                              'subject_path(address="Atom/(.Header.Context.Role in (Operations))/Workflow")\n'
                              'subject_path(address="Workflow.Name")\n'
                              'relation(source="Workflow//$workflow", name="CONTAINS", target="Step//$step")',
                              status="Draft", directory=draft)
            wrong_qualifier = write(33, "Atom.Name",
                                    'subject_path(address="Atom/(.Header.Context.Role in (Method))/Workflow")',
                                    status="Draft", directory=draft)
            sig = 'subject_path(address="Relation//WAVE_SIGNATURE")\nrelation(source="$host", name="WAVE_SIGNATURE", target="$target")'
            current_signature = write(35, "CFEL <+ Relation//WAVE_SIGNATURE", sig,
                                      form="Relation Declaration")
            draft_signature = write(35, "CFEL <+ Relation//WAVE_SIGNATURE", sig,
                                    status="Draft", directory=draft, form="Relation Declaration")
            invalid_signature = write(36, "CFEL <+ Relation//WAVE_SIGNATURE", sig,
                                      status="Draft", directory=draft, form="Rule")
            write(37, "Atom.Header.Context.Form", 'subject_path(address="Atom.Header.Context.Form")')
            requirement = "Atom/(.Header.Context.Role := Requirement)"
            write(38, requirement, 'subject_path(address="Atom")')
            for number, form in ((39, "Declaration"), (40, "Relation Declaration")):
                write(number, requirement + f"/(.Header.Context.Form := {form})", 'subject_path(address="Atom")')
            declaring_subject = "CFEL <+ Relation//IS_DECLARED_BY"
            target = (
                "Atom/(.Header.Context.Role: Requirement)"
                "/(.Header.Context.Form in (Declaration, Relation Declaration))//$atom"
            )
            signature = (
                'subject_path(address="Relation//IS_DECLARED_BY")\n'
                f'relation(source="$declared_subject", name="IS_DECLARED_BY", target={target!r})'
            )
            write(41, declaring_subject, signature, form="Relation Declaration")
            declared_by = write(
                41, declaring_subject, signature
                + '\nrelation(source="Atom", name="IS_DECLARED_BY", target="$atom")',
                status="Draft", directory=draft, form="Relation Declaration",
            )
            unregistered_form = write(
                42, declaring_subject, signature.replace("Relation Declaration))", "Imaginary Form))"),
                status="Draft", directory=draft, form="Relation Declaration",
            )
            unscoped_selector = write(
                43, declaring_subject, f"subject_path(address={target!r})",
                status="Draft", directory=draft, form="Relation Declaration",
            )
            selection = resolve_project(root)
            service = WorkbenchService(root, archive_placement=fixture_rules(),
                                       extension_directory=extension_directory(PROGRAMMATIC.parents[1]),
                                       **built_assets(root))
            try:
                run = service.run
                with patch.object(service, "run", side_effect=lambda sql, **kw: run(sql, page_size=2, **kw)), \
                        patch.object(service, "page", wraps=service.page) as page:
                    self.assertEqual(lint_project_claim(service, selection, current_signature), ())
                    self.assertEqual(lint_project_claim(service, selection, good), ())
                    self.assertGreater(page.call_count, 0)
                self.assertEqual(lint_project_claim(service, selection, draft_signature), ())
                self.assertIn("unknown source", lint_project_claim(service, selection, invalid_signature)[0])
                self.assertEqual((), lint_project_claim(service, selection, declared_by))
                self.assertIn("unknown target", lint_project_claim(service, selection, unregistered_form)[0])
                self.assertIn("unknown address", lint_project_claim(service, selection, unscoped_selector)[0])
                self.assertIn("unknown address", lint_project_claim(service, selection, bad)[0])
                self.assertIn("unknown Relation", lint_project_claim(service, selection, unknown_relation)[0])
                self.assertIn(f"{syntax}-RULE--fixture.md:21:", lint_project_claim(service, selection, syntax)[0])
                self.assertEqual(lint_project_claim(service, selection, composition), ())
                self.assertIn("unresolved Relation alias", lint_project_claim(service, selection, unbound_alias)[0])
                self.assertIn("unknown address", lint_project_claim(service, selection, ambiguous)[0])
                self.assertEqual(lint_project_claim(service, selection, qualified), ())
                self.assertIn("unknown address", lint_project_claim(service, selection, wrong_qualifier)[0])
                original = service.lifecycle_candidates

                def add_declaration(*args, **kwargs):
                    write(27, "Atom.New", 'subject_path(address="Atom.New")')
                    service._refresh()
                    return original(*args, **kwargs)

                with patch.object(service, "lifecycle_candidates", side_effect=add_declaration):
                    with self.assertRaisesRegex(ValueError, "inventory changed"):
                        lint_project_claim(service, selection, good)
            finally:
                service.close()


if __name__ == "__main__":
    unittest.main()
