# CA-E-675@6
from __future__ import annotations

from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys
import unittest

import yaml


APP_ROOT = Path(__file__).resolve().parents[2]
REPOSITORY_ROOT = Path(__file__).resolve().parents[5]
sys.path[:0] = [str(APP_ROOT)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_columns import content_columns  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.content_schema import (  # noqa: E402
    compile_content_schema,
)
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.markdown_content import parse_content  # noqa: E402


class ContentDeclarationSchemaTests(unittest.TestCase):
    @staticmethod
    def atom(
        reference: str, *, role: str = "Requirement", form: str = "Declaration",
        status_group: str = "Current", body: str,
    ) -> dict:
        return {
            "ref": reference,
            "id": reference,
            "version": 1,
            "source_path": f"model/{reference}.md",
            "role": role,
            "form": form,
            "status_group": status_group,
            "content_markdown": body,
            "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
        }

    def declaration(self, reference: str, statement: str) -> dict:
        return self.atom(
            reference,
            body=f"## Claim\n\n```CFEL\n# model\n{statement}\n```\n",
        )

    def test_declaration_changes_add_remove_and_rename_columns(self) -> None:
        summary = self.declaration("CA-R-1", "Atom.Content.Summary{::1}:: {::1};")
        renamed = self.declaration("CA-R-1", "Atom.Content.Title{::1}:: {::1};")

        self.assertEqual(("content.summary",), compile_content_schema([summary]).names)
        self.assertEqual(("content.title",), compile_content_schema([renamed]).names)
        self.assertEqual((), compile_content_schema([{
            **summary, "status_group": "Draft",
        }]).names)

    def test_role_and_form_gate_the_declared_value(self) -> None:
        declaration = self.declaration(
            "CA-R-2",
            "Atom/(.Header.Role := Plan)/(.Header.Form := Epic).Content.Objective:: {::1};",
        )
        schema = compile_content_schema([declaration])
        plan = self.atom("CA-P-1", role="Plan", form="Epic", body="## Objective\n\nShip it.\n")
        task = self.atom("CA-P-2", role="Plan", form="Task", body="## Objective\n\nDo not expose.\n")

        self.assertEqual({"content.objective": "Ship it."}, content_columns(plan, schema))
        self.assertEqual({"content.objective": None}, content_columns(task, schema))

    def test_colon_and_literal_list_filters_are_not_global(self) -> None:
        declaration = self.declaration(
            "CA-R-2",
            "Atom/(.Header.Role: Plan).Content.Objective:: {::1};\n"
            "Atom/(.Header.Role in (Plan, Concern)).Content.Scope:: {::0..1};",
        )
        schema = compile_content_schema([declaration])
        plan = self.atom("CA-P-1", role="Plan", body="## Objective\n\nShip.\n\n## Scope\n\nAll.\n")
        concern = self.atom("CA-C-1", role="Concern", body="## Objective\n\nHidden.\n\n## Scope\n\nOnly this.\n")
        other = self.atom("CA-R-1", body="## Objective\n\nHidden.\n\n## Scope\n\nHidden.\n")

        self.assertEqual(
            {"content.objective": "Ship.", "content.scope": "All."}, content_columns(plan, schema),
        )
        self.assertEqual(
            {"content.objective": None, "content.scope": "Only this."}, content_columns(concern, schema),
        )
        self.assertEqual(
            {"content.objective": None, "content.scope": None}, content_columns(other, schema),
        )

    def test_context_role_and_form_filters_match_the_prepared_header_layout(self) -> None:
        declaration = self.declaration(
            "CA-R-2",
            "Atom/(.Header.Context.Role in RMED)/(.Header.Context.Form: Policy).Content.Objective:: {::1};",
        )
        schema = compile_content_schema([declaration])
        policy = self.atom("CA-M-1", role="Method", form="Policy", body="## Objective\n\nUse it.\n")
        rule = self.atom("CA-R-1", role="Requirement", form="Rule", body="## Objective\n\nDo not use it.\n")

        self.assertEqual({"content.objective": "Use it."}, content_columns(policy, schema))
        self.assertEqual({"content.objective": None}, content_columns(rule, schema))

    def test_unsupported_filter_refuses_to_widen_applicability(self) -> None:
        declaration = self.declaration(
            "CA-R-2",
            "Atom/(.Header.Role != Plan).Content.Objective:: {::1};",
        )

        with self.assertRaisesRegex(ValueError, "unsupported Content declaration Header.Role filter"):
            compile_content_schema([declaration])

    def test_unsupported_selector_refuses_to_widen_applicability(self) -> None:
        declaration = self.declaration(
            "CA-R-2",
            "Atom/(.Header.Status := Active).Content.Objective:: {::1};",
        )

        with self.assertRaisesRegex(ValueError, "unsupported Content declaration selector"):
            compile_content_schema([declaration])

    def test_hyphenated_declarations_and_headings_share_one_key(self) -> None:
        declaration = self.declaration(
            "CA-R-2", "Atom.Content.Formal-Claim:: {::1};",
        )
        schema = compile_content_schema([declaration])
        atom = self.atom("CA-R-3", body="## Formal Claim\n\nFormal content.\n")

        self.assertEqual(("content.formal_claim",), schema.names)
        self.assertEqual({"content.formal_claim": "Formal content."}, content_columns(atom, schema))

    def test_allowed_children_produce_rmed_claim_columns_and_keep_legacy_prose(self) -> None:
        declaration = self.declaration(
            "CA-R-3",
            "Atom/(.Header.Role in RMED).Content.Claim{::1}:: []{::0};\n"
            "Atom/(.Header.Role in RMED).Content.Claim.*[string, in (Formal Claim, Prose Claim)]{::1..2};",
        )
        schema = compile_content_schema([declaration])
        atom = self.atom(
            "CA-R-4",
            body="## Claim\n\nFirst line.\n### Unregistered heading\n\nSecond line.\n",
        )

        self.assertEqual(
            ("content.claim.formal_claim", "content.claim.prose_claim"), schema.names,
        )
        self.assertEqual(
            {
                "content.claim.formal_claim": None,
                "content.claim.prose_claim": "First line.\n### Unregistered heading\n\nSecond line.",
            },
            content_columns(atom, schema),
        )

    def test_prose_claim_keeps_undeclared_children_and_uses_exact_declared_spans(self) -> None:
        declaration = self.declaration(
            "CA-R-3",
            "Atom/(.Header.Role in RMED).Content.Claim.Prose Claim:: {::1};\n"
            "Atom/(.Header.Role in RMED).Content.Claim.Prose Claim.Structured Section:: {::0..1};",
        )
        schema = compile_content_schema([declaration])
        atom = self.atom(
            "CA-R-4",
            body="""## Claim

### Prose Claim

Intro.

```text
#### Structured Section
Must remain in the code fence.
```

#### Presentation Context

Keep this heading.

#### Structured Section

Expose separately.
""",
        )

        values = content_columns(atom, schema)
        self.assertEqual(
            """Intro.

```text
#### Structured Section
Must remain in the code fence.
```

#### Presentation Context

Keep this heading.""",
            values["content.claim.prose_claim"],
        )
        self.assertEqual("Expose separately.", values["content.claim.prose_claim.structured_section"])

    def test_undeclared_headings_stay_inside_markdown_and_normalized_declared_duplicates_fail(self) -> None:
        declaration = self.declaration("CA-R-5", "Atom.Content.Summary{::1}:: {::1};")
        schema = compile_content_schema([declaration])
        ordinary = self.atom("CA-R-6", body="## Summary\n\nOne\n\n## Unregistered Heading\n\nTwo\n")
        duplicate = self.atom("CA-R-7", body="## Summary\n\nOne\n\n## Summary\n\nTwo\n")

        self.assertEqual({"content.summary": "One"}, content_columns(ordinary, schema))
        with self.assertRaisesRegex(ValueError, "duplicate declared content property: summary"):
            content_columns(duplicate, schema)

    def test_real_current_model_declarations_compile_and_record_provenance(self) -> None:
        rows = self._current_model_rows()

        schema = compile_content_schema(rows)
        self.assertEqual(
            (
                "content.claim.formal_claim", "content.claim.prose_claim", "content.details",
                "content.semantics", "content.summary",
            ),
            schema.names,
        )
        asset = schema.asset()
        self.assertGreaterEqual(len(asset["content_declaration_sources"]), 6)
        self.assertIn("CA-R-2500", {source["reference"] for source in asset["content_declaration_sources"]})
        self.assertEqual("VARCHAR", next(
            item["format"] for item in asset["content_columns"] if item["name"] == "content.claim.formal_claim"
        ))
        json.dumps(asset)

    def test_prepared_header_grouping_keeps_the_real_content_schema(self) -> None:
        rows = self._current_model_rows()
        before = compile_content_schema(rows)
        transform = self._prepared_reference_transform()
        prepared = []
        for row in rows:
            body = transform(row["content_markdown"])
            prepared.append({
                **row,
                "content_markdown": body,
                "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
            })

        self.assertIn(
            ".Header.Context.Role in RMED",
            next(row["content_markdown"] for row in prepared if row["ref"] == "CA-R-2500"),
        )
        self.assertEqual(before.shape, compile_content_schema(prepared).shape)

    def test_declaration_provenance_does_not_change_the_schema_shape(self) -> None:
        first = self.declaration("CA-R-1", "Atom.Content.Summary{::1}:: {::1};")
        later = {**first, "version": 2, "source_path": "model/renamed.md"}
        original = compile_content_schema([first])
        replaced = compile_content_schema([later])

        self.assertEqual(original.shape, replaced.shape)
        self.assertNotEqual(original.asset(), replaced.asset())

    @staticmethod
    def _current_declaration(path: Path) -> dict:
        _opening, frontmatter, body = path.read_text(encoding="utf-8").split("---", 2)
        header = yaml.safe_load(frontmatter)
        return {
            "ref": header.get("ref_id"),
            "id": header.get("atom_id"),
            "version": header.get("version"),
            "source_path": path.as_posix(),
            "role": header.get("role"),
            "form": header.get("form"),
            "status_group": "Current",
            "content_markdown": body,
            "content_properties_json": parse_content(body, tolerate_duplicate_siblings=True),
        }

    @classmethod
    def _current_model_rows(cls) -> list[dict]:
        return [
            cls._current_declaration(path)
            for path in (REPOSITORY_ROOT / ".caprmedio_caprmedio").glob("**/04_requirement/*.md")
            if not {"archive", "archived", "draft", "drafts"} & {part.casefold() for part in path.parts}
            and cls._is_current(path)
        ]

    @staticmethod
    def _prepared_reference_transform():
        path = (
            REPOSITORY_ROOT / ".caprmedio_caprmedio/02_analysis/draft/"
            "header-groups-20261106/references/prepare_reference_impact.py"
        )
        spec = spec_from_file_location("prepared_header_impact", path)
        assert spec is not None and spec.loader is not None
        module = module_from_spec(spec)
        spec.loader.exec_module(module)
        return module.transform

    @staticmethod
    def _is_current(path: Path) -> bool:
        _opening, frontmatter, _body = path.read_text(encoding="utf-8").split("---", 2)
        header = yaml.safe_load(frontmatter) or {}
        return (
            header.get("status") not in {"Draft", "Archived", "archived"}
            and not str(header.get("atom_id", "")).endswith(("-draft", "@draft"))
        )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
