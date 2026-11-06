# CA-E-677@14
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
    def assert_parity(self, current: dict[str, dict], delta: dict[str, dict | None]) -> None:
        state = HeaderSchemaState.from_atoms(list(current.values()))
        expected = dict(current)
        for path, changed in delta.items():
            if changed is None:
                expected.pop(path)
            else:
                expected[path] = changed
        self.assertEqual(infer_header_schema(list(expected.values())), state.updated(delta).schema)

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
        candidate = state.updated({"b.md": changed})
        current["b.md"] = changed

        self.assertEqual(infer_header_schema(list(current.values())), candidate.schema)
        context = next(column for column in candidate.schema.columns if column.name == "header_context")
        self.assertTrue(context.populated)
        self.assertEqual("JSON", context.format)

    def test_delta_removes_last_direct_path_and_keeps_empty_observed_path(self) -> None:
        current = {
            "a.md": row("a.md", {"kept": {}}),
            "b.md": row("b.md", {"obsolete": "value"}),
        }
        state = HeaderSchemaState.from_atoms(list(current.values()))
        candidate = state.updated({"b.md": None})

        self.assertEqual(infer_header_schema([current["a.md"]]), candidate.schema)
        self.assertEqual(("header_kept",), candidate.schema.names)
        self.assertFalse(candidate.schema.columns[0].populated)

    def test_delta_detects_bool_integer_type_change_and_name_collision(self) -> None:
        initial = {"a.md": row("a.md", {"value": True, "same-name": "a"})}
        state = HeaderSchemaState.from_atoms(list(initial.values()))
        changed = row("a.md", {"value": 1, "same-name": "a", "same_name": "b"})
        self.assert_parity(initial, {"a.md": row("a.md", {"value": 1, "same-name": "a"})})
        with self.assertRaisesRegex(ValueError, "collision"):
            state.updated({"a.md": changed}).schema

    def test_delta_collects_only_changed_header(self) -> None:
        first = row("a.md", {"stable": {"nested": 1}})
        second = row("b.md", {"changed": "before"})
        state = HeaderSchemaState.from_atoms([first, second])
        changed = row("b.md", {"changed": "after"})

        with patch.object(header_columns, "_contribution", wraps=header_columns._contribution) as collect:
            candidate = state.updated({"b.md": changed})

        self.assertEqual(1, collect.call_count)
        self.assertEqual(infer_header_schema([first, changed]), candidate.schema)


if __name__ == "__main__":
    unittest.main()
