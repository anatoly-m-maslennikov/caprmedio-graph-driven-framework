# CA-E-675@10
"""Content declarations apply to admitted Role/Form serializations."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tests"))
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / "FEATURE_TOOLS"))

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import ContentSchema, DeclarationSource, compile_content_schema
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declared_header_rules import HeaderRule
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.header_columns import HeaderColumn
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.relation_registry import carrier_read_view, compile_relation_registry, registry_contribution
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.query_store import QueryStore
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_reader import SourceReader
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.source_content_schema import SourceContentSchema
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.service import WorkbenchService
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.workbench_schema_asset import compile_schema
from scope_declaration_test_support import write_scope_unit_declarations
from smalltest_support import extension_directory, source_path, write_atom, write_settings


def atom(role, form, body):
    return {
        "role": role,
        "form": form,
        "status_group": "Current",
        "content_markdown": body,
    }


class CarrierSerializationTests(unittest.TestCase):
    def test_encoded_relation_declaration_is_admitted_without_changing_header(self):
        header = {"context": {"role": "requirement", "form": "relation_definition"}}
        row = atom("requirement", "relation_definition", "## Claim\n\n### Formal Claim\n\n```CFEL\nRelation//RELATES_TO;\n```\n") | {
            "source_path": "model.md", "id": "CA-R-1", "version": 1, "header_json": header,
        }
        self.assertIn("RELATES_TO", registry_contribution(row).names)
        self.assertEqual(header, {"context": {"role": "requirement", "form": "relation_definition"}})
        row["form"] = "Relation_Definition"
        self.assertFalse(registry_contribution(row).names)

    def test_current_model_presentation_headings_do_not_create_columns(self):
        model = Path.cwd() / (
            ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/"
            "CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement"
        )
        declarations = []
        for identifier in ("2498", "2499"):
            path = next(model.glob(f"CA-R-{identifier}-*.md"))
            _, head, body = path.read_text().split("---", 2)
            header = carrier_read_view(yaml.safe_load(head))
            declarations.append(atom(header["role"], header["form"], body))
        source = atom("Method", "Decision", "## Summary\n\nTop.\n\n### Note\n\nKeep.\n")
        schema = compile_content_schema([*declarations, source])
        self.assertNotIn("content.summary.note", schema.names)
        self.assertIn("### Note", schema.values(source)["content.summary"])

    def test_literal_child_declaration_does_not_invent_siblings(self):
        declaration = atom(
            "Requirement", "Declaration", "## Claim\n\n### Formal Claim\n\n```CFEL\n"
            "Atom.Content.**[string]{::0+};\n"
            "Atom.Content.Summary.*[]{::0};\n"
            "Atom.Content.Summary.Allowed:: {::1};\n```\n",
        )
        source = atom("Method", "Decision", "## Summary\n\n### Allowed\n\nYes.\n\n### Other\n\nNo.\n")
        schema = compile_content_schema([declaration, source])
        self.assertIn("content.summary.allowed", schema.names)
        self.assertNotIn("content.summary.other", schema.names)

    def test_validation_does_not_extract_all_content_columns(self):
        declaration = atom(
            "Requirement", "Declaration", "## Claim\n\n### Formal Claim\n\n```CFEL\n"
            "Atom.Content.*[string]{::0+};\nAtom.Content.Objective:: {::1};\n```\n",
        ) | {"source_path": "model.md"}
        source = atom("Plan", "Plan", "## Objective\n\nOne.\n\n## Objective\n\nTwo.\n") | {
            "source_path": "plan.md"
        }
        state = SourceContentSchema()
        with patch.object(ContentSchema, "values", side_effect=AssertionError("validation extracted every column")):
            errors = state.rebuild([declaration, source])
        self.assertIn("plan.md", errors)

    def test_mode_one_header_rule_matches_serialized_role_and_form(self):
        rule = HeaderRule(
            ("custom",), "VARCHAR", frozenset({"Method"}), frozenset({"Direct Policy"}),
            DeclarationSource("CA-R-1", 1, "model.md"),
        )
        column = HeaderColumn(("custom",), "header.custom", "VARCHAR", True, rules=(rule,))
        self.assertTrue(column.applies({"role": "method", "form": "direct_policy"}))
        self.assertFalse(column.applies({"role": "method", "form": "solution"}))

    def test_serialized_role_and_form_match_business_spelling(self):
        declaration = atom(
            "requirement", "entity_definition",
            "## Claim\n\n### Formal Claim\n\n```CFEL\n"
            "Atom/(.Header.Role := Method)/(.Header.Form := Direct Policy)"
            ".Content.Claim.Prose Claim:: {::1};\n```\n",
        )
        schema = compile_content_schema([declaration])
        body = "## Claim\n\n### Prose Claim\n\nThe method.\n"
        self.assertEqual(
            {"content.claim.prose_claim": "The method."},
            schema.values(atom("method", "direct_policy", body)),
        )
        self.assertEqual(
            {"content.claim.prose_claim": None}, schema.values(atom("Method", "Solution", body)),
        )

    def test_wildcard_constraints_do_not_declare_secret(self):
        declaration = atom(
            "Requirement", "Declaration",
            "## Claim\n\n### Formal Claim\n\n```CFEL\n"
            "Atom.Content.*[string]{::0+};\n"
            "Atom/(.Header.Role := Method).Content.Secret:: []{::0};\n```\n",
        )
        method = atom("Method", "Solution", "## Secret\n\nHidden.\n")
        plan = atom("Plan", "Plan", "## Secret\n\nVisible.\n")
        self.assertNotIn("content.secret", compile_content_schema([declaration, method, plan]).names)

    def test_filtered_wildcard_preserves_fences_and_role_boundaries(self):
        declaration = atom(
            "Requirement", "Declaration",
            "## Claim\n\n### Formal Claim\n\n```CFEL\n"
            "Atom/(.Header.Role in (Plan, Concern)).Content.**[string]{::0+};\n"
            "Atom/(.Header.Role in (Plan, Concern)).Content.Project Objective.Nested Scope:: {::1};\n```\n",
        )
        plan = atom(
            "plan", "Plan", "## Project Objective\n\nText.\n\n"
            "```md\n### Not A Heading\n```\n\n### Nested Scope\n\nInside.\n",
        )
        method = atom("Method", "Solution", "## Private Note\n\nHidden.\n")
        schema = compile_content_schema([declaration, plan, method])
        self.assertIn("content.project_objective.nested_scope", schema.names)
        self.assertNotIn("content.private_note", schema.names)
        self.assertNotIn("content.project_objective.not_a_heading", schema.names)
        self.assertEqual("Inside.", schema.values(plan)["content.project_objective.nested_scope"])

    def test_generic_declaration_exposes_content_for_every_role_and_new_role(self):
        declaration = atom(
            "Requirement", "Declaration",
            "## Claim\n\n### Formal Claim\n\n```CFEL\nAtom.Content.*[string]{::0+};\n"
            + "".join(f"Atom.Content.{name}:: {{::1}};\n" for name in (
                "Concern", "Report", "Objective", "Summary", "Method", "Evaluation", "Delivery", "Operation", "New Section"
            )) + "```\n",
        )
        examples = [
            ("Concern", "Problem", "Concern"),
            ("Analysis & Advisory", "Analysis Report", "Report"),
            ("Plan", "Plan", "Objective"),
            ("Requirement", "Definition", "Summary"),
            ("Method", "Decision", "Method"),
            ("Evaluation", "Eval Case", "Evaluation"),
            ("Delivery", "Decision", "Delivery"),
            ("Operations", "Action", "Operation"),
            ("Example New Role", "New Form", "New Section"),
        ]
        rows = [atom(role, form, f"## {heading}\n\nValue.\n") for role, form, heading in examples]
        schema = compile_content_schema([declaration, *rows])
        for row, (_, _, heading) in zip(rows, examples):
            name = "content." + heading.casefold().replace(" ", "_")
            self.assertEqual("Value.", schema.values(row)[name])

    def test_wildcards_do_not_expose_observed_paths_or_split_prose(self):
        declaration = atom(
            "Requirement", "Declaration",
            "## Claim\n\n### Formal Claim\n\n```CFEL\n"
            "Atom.Content.*[string]{::0+};\n"
            "Atom.Content.**[string]{::0+};\n"
            "Atom.Content.Claim:: []{::0};\n"
            "Atom/(.Header.Role in RMED).Content.Claim.Prose Claim:: {::1};\n```\n",
        )
        prose = atom(
            "Method", "Direct Policy",
            "## Claim\n\n### Prose Claim\n\nText.\n\n#### Note\n\nStill prose.\n",
        )
        legacy = atom(
            "Requirement", "Rule", "## Claim\n\nText.\n\n### Note\n\nStill prose.\n",
        )
        plan = atom("Plan", "Plan", "## Objective\n\nShip.\n\n### Scope\n\nInside.\n")
        schema = compile_content_schema([declaration, prose, legacy, plan])
        self.assertNotIn("content.objective", schema.names)
        self.assertNotIn("content.objective.scope", schema.names)
        self.assertNotIn("content.claim", schema.names)
        self.assertNotIn("content.claim.prose_claim.note", schema.names)
        self.assertNotIn("content.claim.note", schema.names)
        self.assertIn("#### Note", schema.values(prose)["content.claim.prose_claim"])
        self.assertIn("### Note", schema.values(legacy)["content.claim.prose_claim"])

    def test_observed_headings_do_not_change_wildcard_schema(self):
        declaration = atom(
            "Requirement", "Declaration",
            "## Claim\n\n### Formal Claim\n\n```CFEL\nAtom.Content.*[string]{::0+};\n```\n",
        ) | {"source_path": "model.md"}
        first = atom("Plan", "Plan", "## Objective\n\nShip.\n") | {"source_path": "plan.md"}
        changed = atom("Plan", "Plan", "## Objective\n\nShip later.\n") | {"source_path": "plan.md"}
        added = atom("Plan", "Plan", "## Objective\n\nShip.\n\n## Scope\n\nAll.\n") | {
            "source_path": "plan.md"
        }
        state = SourceContentSchema()
        state.rebuild([declaration, first])
        self.assertFalse(state.update({"plan.md": changed}))
        self.assertFalse(state.update({"plan.md": added}))
        state.rebuild([declaration, added])
        self.assertFalse(state.update({"plan.md": first}))

    def test_current_and_draft_in_both_schema_modes(self):
        temporary_root = Path.cwd() / ".caprmedio_tmp" / "tests"
        temporary_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as directory:
            root = Path(directory)
            control = write_settings(root)
            declarations = write_scope_unit_declarations(
                root, ({"scope_unit_name": "ENGINE", "scope_unit_label": "FEATURE"},),
                control_root=control,
            )
            model = source_path(declarations, "ENGINE", "04_requirement", "CA-R-900.md")
            write_atom(
                model, "CA-R-900",
                body="## Claim\n\n### Formal Claim\n\n```CFEL\n"
                "Atom/(.Header.Role := Method)/(.Header.Form := Direct Policy)"
                ".Content.Claim.Prose Claim:: {::1};\n```\n",
            )
            model.write_text(model.read_text().replace('form: "Definition"', 'form: "entity_definition"'))
            for version, directory_name in ((1, ""), (2, "draft")):
                path = source_path(
                    declarations, "ENGINE", "05_method",
                    str(Path(directory_name) / f"CA-M-514{'@2-draft' if version == 2 else ''}.md"),
                )
                write_atom(
                    path, "CA-M-514", status="Draft" if version == 2 else "Active",
                    version=version, body="## Claim\n\n### Prose Claim\n\nMethod text.\n",
                )
                path.write_text(path.read_text().replace('role: "Requirement"', 'role: "method"').replace(
                    'form: "Definition"', 'form: "direct_policy"',
                ))
            for mode in (1, 2):
                reader = SourceReader(root, control, schema_mode=mode)
                rows, _ = reader.capture()
                candidates = [row for row in rows if row["id"] == "CA-M-514"]
                self.assertEqual({"Current", "Draft"}, {row["status_group"] for row in candidates})
                self.assertEqual(
                    {"Method text."},
                    {reader.content_schema.values(row)["content.claim.prose_claim"] for row in candidates},
                )

    def test_declared_schema_refresh_is_visible_in_sql_for_both_modes(self):
        temporary_root = Path.cwd() / ".caprmedio_tmp" / "tests"
        temporary_root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary_root) as directory:
            root = Path(directory)
            control = write_settings(root)
            declarations = write_scope_unit_declarations(
                root, ({"scope_unit_name": "ENGINE", "scope_unit_label": "FEATURE"},),
                control_root=control,
            )
            model = source_path(declarations, "ENGINE", "04_requirement", "CA-R-900.md")
            write_atom(
                model, "CA-R-900", body="## Claim\n\n### Formal Claim\n\n```CFEL\n"
                "Atom.Content.*[string]{::0+};\nAtom.Content.**[string]{::0+};\n"
                "Atom.Content.Objective:: {::1};\nAtom.Content.Objective.Scope:: {::0..1};\n```\n",
            )
            model.write_text(model.read_text().replace('form: "Definition"', 'form: "Declaration"'))
            plan = source_path(declarations, "ENGINE", "03_plan", "CA-P-900.md")

            def write_plan(body):
                write_atom(plan, "CA-P-900", body=body)
                plan.write_text(plan.read_text().replace('role: "Requirement"', 'role: "Plan"'))

            def event():
                return {"operation": "update", "old_path": None, "new_path": plan.relative_to(root).as_posix()}

            for mode in (1, 2):
                write_plan("## Objective\n\nBefore.\n")
                builder = SourceReader(root, control)
                rows, _ = builder.capture()
                assert builder.content_schema is not None
                compiled = compile_schema(rows, builder.content_schema, builder.header_schema)
                service = WorkbenchService(
                    root, compiled_schema=compiled, relation_registry=compile_relation_registry(rows),
                )
                service._schema_mode = mode
                service._header_schema = compiled.mode_one if mode == 1 else None
                service._reader = SourceReader(
                    root, control, schema_mode=mode, compiled_schema=(compiled.content, compiled.mode_one),
                )
                service._store = QueryStore(
                    schema_mode=mode, extension_directory=extension_directory(Path.cwd()),
                )
                try:
                    service._refresh()
                    self.assertEqual([["Before."]], service._store.run(
                        'SELECT "content.objective" FROM atoms WHERE filename = \'CA-P-900.md\''
                    )["rows"])
                    write_plan("## Objective\n\nAfter.\n")
                    service._refresh([event()])
                    self.assertEqual([["After."]], service._store.run(
                        'SELECT "content.objective" FROM atoms WHERE filename = \'CA-P-900.md\''
                    )["rows"])
                    write_plan("## Objective\n\nAfter.\n\n### Scope\n\nAll.\n")
                    service._refresh([event()])
                    self.assertEqual([["All."]], service._store.run(
                        'SELECT "content.objective.scope" FROM atoms WHERE filename = \'CA-P-900.md\''
                    )["rows"])
                    self.assertEqual([["After."]], service._store.run(
                        'SELECT "content.objective" FROM atoms WHERE filename = \'CA-P-900.md\''
                    )["rows"])
                    write_plan("## Objective\n\nAfter.\n")
                    service._refresh([event()])
                    columns = service._store.schema()["tables"]["atoms"]
                    self.assertIn("content.objective.scope", {column["name"] for column in columns})
                    self.assertEqual([[None]], service._store.run(
                        'SELECT "content.objective.scope" FROM atoms WHERE filename = \'CA-P-900.md\''
                    )["rows"])
                finally:
                    service.close()


if __name__ == "__main__":
    unittest.main()
