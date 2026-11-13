# CA-E-677@19
# CA-E-675@14
from __future__ import annotations

import datetime as dt
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


APP_ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(APP_ROOT)]

from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND import header_columns  # noqa: E402
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.header_columns import (  # noqa: E402
    HeaderSchemaState,
    infer_header_schema,
)


def row(path: str, header: dict) -> dict:
    return {"source_path": path, "header_json": header}


class HeaderSchemaDeltaTests(unittest.TestCase):
    def assert_parity(
        self,
        current: dict[str, dict],
        old_rows: dict[str, dict],
        new_rows: dict[str, dict],
    ) -> None:
        state = HeaderSchemaState.from_atoms(list(current.values()))
        expected = dict(current)
        for path in old_rows:
            expected.pop(path, None)
        expected.update(new_rows)
        candidate = state.updated(old_rows, new_rows)
        self.assertEqual(infer_header_schema(list(expected.values())), candidate.schema)
        self.assertNotIn("contributions", vars(candidate))

    def test_delta_matches_full_for_parent_mapping_empty_values_and_types(self) -> None:
        first = row("a.md", {
            "context": {"id": 123}, "nullable": None, "empty": "",
            "when": dt.date(2026, 11, 7), "flag": True, "relations": {},
        })
        second = row("b.md", {
            "context": {}, "nullable": None, "empty": None,
            "when": dt.date(2026, 11, 7), "flag": True,
        })
        changed = row("b.md", {
            "context": {}, "nullable": "", "empty": [],
            "when": "2026-11-07", "flag": 1,
        })
        current = {"a.md": first, "b.md": second}
        state = HeaderSchemaState.from_atoms(list(current.values()))
        candidate = state.updated({"b.md": second}, {"b.md": changed})
        current["b.md"] = changed

        self.assertEqual(infer_header_schema(list(current.values())), candidate.schema)
        context = next(column for column in candidate.schema.columns if column.name == "header.context")
        self.assertTrue(context.populated)
        self.assertEqual("JSON", context.format)

    def test_delta_removes_last_direct_path_and_keeps_empty_observed_path(self) -> None:
        current = {
            "a.md": row("a.md", {"kept": {}}),
            "b.md": row("b.md", {"obsolete": "value"}),
        }
        state = HeaderSchemaState.from_atoms(list(current.values()))
        candidate = state.updated({"b.md": current["b.md"]}, {})

        self.assertEqual(infer_header_schema([current["a.md"]]), candidate.schema)
        self.assertEqual(("header.kept",), candidate.schema.names)
        self.assertFalse(candidate.schema.columns[0].populated)

    def test_delta_detects_bool_integer_type_change_and_name_collision(self) -> None:
        initial = {"a.md": row("a.md", {"value": True, "same-name": "a"})}
        state = HeaderSchemaState.from_atoms(list(initial.values()))
        changed = row("a.md", {"value": 1, "same-name": "a", "same_name": "b"})
        self.assert_parity(
            initial,
            {"a.md": initial["a.md"]},
            {"a.md": row("a.md", {"value": 1, "same-name": "a"})},
        )
        with self.assertRaisesRegex(ValueError, "collision"):
            state.updated({"a.md": initial["a.md"]}, {"a.md": changed}).schema

    def test_delta_collects_only_changed_header(self) -> None:
        first = row("a.md", {"stable": {"nested": 1}})
        second = row("b.md", {"changed": "before"})
        state = HeaderSchemaState.from_atoms([first, second])
        changed = row("b.md", {"changed": "after"})

        with patch.object(header_columns, "_contribution", wraps=header_columns._contribution) as collect:
            candidate = state.updated({"b.md": second}, {"b.md": changed})

        self.assertEqual(2, collect.call_count)
        self.assertEqual(infer_header_schema([first, changed]), candidate.schema)

    def test_create_update_rename_and_delete_match_full_inference_without_source_map(self) -> None:
        original = row("a.md", {"stable": "kept", "nested": {"empty": {}}})
        current = {"a.md": original}
        state = HeaderSchemaState.from_atoms(list(current.values()))

        def apply(old_rows: dict[str, dict], new_rows: dict[str, dict]) -> None:
            nonlocal current, state
            candidate = state.updated(old_rows, new_rows)
            expected = dict(current)
            for path in old_rows:
                expected.pop(path, None)
            expected.update(new_rows)
            self.assertEqual(infer_header_schema(list(expected.values())), candidate.schema)
            self.assertNotIn("contributions", vars(candidate))
            current, state = expected, candidate

        created = row("b.md", {"stable": "new", "optional": None})
        apply({}, {"b.md": created})
        updated = row("b.md", {"stable": "edited", "optional": [], "flag": False})
        apply({"b.md": created}, {"b.md": updated})
        renamed = row("renamed.md", {"stable": "edited", "optional": [], "flag": False})
        apply({"b.md": updated}, {"renamed.md": renamed})
        apply({"renamed.md": renamed}, {})


if __name__ == "__main__":
    unittest.main()
