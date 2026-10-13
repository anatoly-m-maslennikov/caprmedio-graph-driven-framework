from __future__ import annotations

import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_toml_parse import apply_edits, equal_values, parse_source, render_document
from connector_toml_read import TomlFailure


class SemanticEditsTests(unittest.TestCase):
    keys = {"name": ("config", "name"), "members": ("config", "members"), "added": ("added",)}
    document = {"config": {"name": "before", "members": ["a", "b"]}, "other": {"flag": True}}

    def edit(self, **edit):
        return apply_edits(self.document, {"edits": [edit]}, self.keys)

    def test_scalar_add_replace_remove_and_unrelated_values(self):
        for action, field, value in (("add", "added", 3), ("replace", "name", "after"), ("remove", "name", None)):
            edit = {"action": action, "field": field, "mode": "value"}
            if action != "remove":
                edit["value"] = value
            after, diff = self.edit(**edit)
            self.assertEqual(after["other"], self.document["other"])
            self.assertEqual(len(diff), 1)
            self.assertTrue(equal_values(parse_source(render_document(after))[1], after))
        self.assertEqual(self.document["config"]["name"], "before")

    def test_item_value_selection_and_full_set_operations(self):
        for edit, expected in (
            ({"action": "add", "mode": "item", "value": "c"}, ["a", "b", "c"]),
            ({"action": "replace", "mode": "item", "current": "b", "value": "c"}, ["a", "c"]),
            ({"action": "remove", "mode": "item", "current": "a"}, ["b"]),
            ({"action": "add", "mode": "set", "value": ["c", "d"]}, ["a", "b", "c", "d"]),
            ({"action": "replace", "mode": "set", "value": ["z"]}, ["z"]),
            ({"action": "remove", "mode": "set", "value": ["a", "b"]}, []),
        ):
            after, diff = self.edit(field="members", **edit)
            self.assertEqual(after["config"]["members"], expected)
            self.assertEqual(len(diff), 1)

    def test_exact_noop_and_type_distinction(self):
        after, diff = self.edit(action="replace", mode="value", field="name", value="before")
        self.assertEqual(after, self.document)
        self.assertEqual(diff, [])
        after, diff = self.edit(action="add", mode="item", field="members", value="a")
        self.assertEqual(diff, [])
        document = {"config": {"members": [1, True]}}
        after, _ = apply_edits(document, {"edits": [{"action": "remove", "mode": "item", "field": "members", "current": True}]}, self.keys)
        self.assertEqual(after["config"]["members"], [1])

    def test_missing_duplicate_unknown_fields_and_positions_fail_before_mutation(self):
        cases = [
            ({"action": "remove", "mode": "item", "field": "members", "current": "absent"}, "target_not_found"),
            ({"action": "replace", "mode": "item", "field": "members", "index": 0, "value": "z"}, "input_invalid"),
            ({"action": "replace", "mode": "value", "field": "protected", "value": 3}, "schema_invalid"),
        ]
        for edit, code in cases:
            with self.assertRaises(TomlFailure) as raised:
                self.edit(**edit)
            self.assertEqual(raised.exception.code, code)
        with self.assertRaises(TomlFailure) as raised:
            apply_edits({"config": {"members": ["a", "a"]}}, {"edits": [{"action": "remove", "mode": "item", "field": "members", "current": "a"}]}, self.keys)
        self.assertEqual(raised.exception.code, "target_ambiguous")
        self.assertEqual(self.document["config"]["members"], ["a", "b"])

    def test_typed_toml_values_roundtrip(self):
        document = {"quoted key": "line\n\t\"\\\x00", "date": datetime.date(2026, 10, 13),
                    "datetime": datetime.datetime(2026, 10, 13, 2, 3, tzinfo=datetime.timezone.utc),
                    "time": datetime.time(2, 3), "float": float("nan"), "infinity": -float("inf"),
                    "empty": {}, "array": [{"x": 1}, {"x": 2}]}
        self.assertTrue(equal_values(parse_source(render_document(document))[1], document))
        with self.assertRaises(ValueError):
            render_document({"invalid": None})


if __name__ == "__main__":
    unittest.main()
