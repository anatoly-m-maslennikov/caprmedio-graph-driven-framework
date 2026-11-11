# CA-E-675@6
from __future__ import annotations

from pathlib import Path
import sys
import unittest


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import DeclarationSource  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.declared_header_rules import (  # noqa: E402
    compile_header_rules,
    header_declaration_rules,
    resolve_header_rules,
)


class DeclaredHeaderRulesTests(unittest.TestCase):
    @staticmethod
    def declaration(
        reference: str, statement: str, *, status_group: str = "Current", role: str = "Requirement",
        form: str = "Declaration", version: int = 1,
    ) -> dict:
        return {
            "ref": reference,
            "id": reference,
            "version": version,
            "source_path": f"model/{reference}.md",
            "status_group": status_group,
            "role": role,
            "form": form,
            "content_markdown": f"## Claim\n\n### Formal Claim\n\n```CFEL\n{statement}\n```\n",
        }

    def test_cfel_outside_formal_claim_does_not_contribute(self) -> None:
        declaration = self.declaration("CA-R-1", "Atom.Header.Priority:: [string]{::1};")
        declaration["content_markdown"] = "## Claim\n\n```CFEL\nAtom.Header.Priority:: [string]{::1};\n```\n"
        self.assertEqual((), compile_header_rules([declaration]))

    def test_declared_paths_replace_the_handwritten_property_list(self) -> None:
        rules = compile_header_rules([
            self.declaration("CA-R-1", "Atom.Header.Review State:: [bool]{::1};"),
        ])

        self.assertEqual(((("review_state",), "BOOLEAN"),), tuple((rule.path, rule.format) for rule in rules))
        self.assertNotIn(("label", "VARCHAR"), tuple((rule.path, rule.format) for rule in rules))

    def test_role_and_form_selectors_remain_on_the_rule(self) -> None:
        rules = header_declaration_rules(self.declaration(
            "CA-R-2",
            "Atom/(.Header.Context.Role in RMED)/(.Header.Context.Form: Policy).Header.Priority:: [string]{::1};",
        ))

        self.assertEqual(1, len(rules))
        self.assertEqual(frozenset({"Requirement", "Method", "Evaluation", "Delivery"}), rules[0].roles)
        self.assertEqual(frozenset({"Policy"}), rules[0].forms)

    def test_scalar_collection_grouping_and_updated_at_formats(self) -> None:
        rules = compile_header_rules([self.declaration(
            "CA-R-3",
            "Atom.Header.Version:: [int]{::1};\n"
            "Atom.Header.Enabled:: [bool]{::1};\n"
            "Atom.Header.Container.atom:: [atom id]{::0..1};\n"
            "Atom.Header.Topics{::1}:: []{::0};\n"
            "Atom.Header.Topics.Dependencies:: [string]{::0+};\n"
            "Atom.Header.Topics.Limited:: [string]{::0..2};\n"
            "Atom.Header.Updated At:: [datetime]{::1};",
        )])

        self.assertEqual(
            {
                ("version",): "BIGINT", ("enabled",): "BOOLEAN", ("container", "atom"): "VARCHAR",
                ("topics", "dependencies"): "JSON", ("topics", "limited"): "JSON",
                ("updated_at",): "TIMESTAMPTZ",
            },
            {rule.path: rule.format for rule in rules},
        )

    def test_wildcard_format_types_explicit_children_without_emitting_wildcard(self) -> None:
        rules = compile_header_rules([self.declaration(
            "CA-R-4",
            "Atom.Header.Carrier Destination.File{::1}:: []{::0};\n"
            "Atom.Header.Carrier Destination.File.*[in (Name, Path)]{::2};\n"
            "Atom.Header.Carrier Destination.File.*:: [string];\n"
            "Atom.Header.Carrier Destination.File.Name:: {::1};\n"
            "Atom.Header.Carrier Destination.File.Path:: {::1};",
        )])

        self.assertEqual(
            {("carrier_destination", "file", "name"): "VARCHAR", ("carrier_destination", "file", "path"): "VARCHAR"},
            {rule.path: rule.format for rule in rules},
        )

    def test_cross_source_wildcard_format_resolves_raw_child_contributions(self) -> None:
        wildcard = self.declaration(
            "CA-R-2716",
            "Atom.Header.Carrier Destination.File{::1}:: []{::0};\n"
            "Atom.Header.Carrier Destination.File.*[in (Name, Path)]{::2};\n"
            "Atom.Header.Carrier Destination.File.*:: [string];",
            version=2,
        )
        name = self.declaration(
            "CA-R-2717", "Atom.Header.Carrier Destination.File.Name:: {::1};", version=3,
        )
        path = self.declaration(
            "CA-R-2718", "Atom.Header.Carrier Destination.File.Path:: {::1};", version=3,
        )

        raw_name = header_declaration_rules(name)
        self.assertEqual(None, raw_name[0].format)
        self.assertEqual(DeclarationSource("CA-R-2717", 3, "model/CA-R-2717.md"), raw_name[0].source)
        self.assertEqual(
            {("carrier_destination", "file", "name"): "VARCHAR", ("carrier_destination", "file", "path"): "VARCHAR"},
            {rule.path: rule.format for rule in compile_header_rules([wildcard, name, path])},
        )
        self.assertEqual(
            compile_header_rules([wildcard, name, path]),
            resolve_header_rules((*header_declaration_rules(wildcard), *raw_name, *header_declaration_rules(path))),
        )

    def test_explicit_format_does_not_replace_an_inherited_wildcard_constraint(self) -> None:
        rules = compile_header_rules([
            self.declaration("CA-R-1", "Atom.Header.Details.*:: [string];"),
            self.declaration("CA-R-2", "Atom.Header.Details.Note:: [string];"),
        ])
        self.assertEqual(
            {
                ("CA-R-2", None, ("details", "note"), "VARCHAR"),
                ("CA-R-2", "CA-R-1", ("details", "note"), "VARCHAR"),
            },
            {
                (rule.source.reference, rule.format_source.reference if rule.format_source else None,
                 rule.path, rule.format)
                for rule in rules
            },
        )
        self.assertEqual(2, len(rules))

    def test_ignores_non_model_prose_formula_relations_and_noncurrent_sources(self) -> None:
        row = self.declaration(
            "CA-R-5",
            "Atom.Header.ID >= 1;\nAtom.Header.Relations:: [string]{::1};\nAtom.Header.ID:: [string]{::1};",
        )
        row["content_markdown"] += "\nAtom.Header.Escaped:: [string]{::1}\n"

        self.assertEqual((("id",),), tuple(rule.path for rule in header_declaration_rules(row)))
        self.assertEqual((), header_declaration_rules({**row, "status_group": "Draft"}))
        self.assertEqual((), header_declaration_rules({**row, "role": "Plan"}))

    def test_source_pin_is_preserved_exactly(self) -> None:
        row = self.declaration("CA-R-2701", "Atom.Header.ID:: [string]{::1};", version=7)

        self.assertEqual(
            DeclarationSource("CA-R-2701", 7, "model/CA-R-2701.md"),
            header_declaration_rules(row)[0].source,
        )


if __name__ == "__main__":
    unittest.main()
