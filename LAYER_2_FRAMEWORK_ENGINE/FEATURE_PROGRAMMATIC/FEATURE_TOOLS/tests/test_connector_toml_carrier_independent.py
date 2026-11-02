"""Independent literal-byte acceptance for the private TOML materializer."""

from __future__ import annotations

import builtins
import copy
import datetime
import importlib
import os
import sys
import tomllib
import unittest
from pathlib import Path
from unittest.mock import patch
from contextlib import ExitStack

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import connector_toml_carrier as carrier
from connector_toml_carrier import materialize_toml
from connector_toml_parse import TomlFailure


def edit(action, mode, **values):
    return {"action": action, "mode": mode, "field": "selected", **values}


def typed(value):
    """An independent complete native-type oracle, not producer equality."""
    if type(value) is dict:
        return (dict, {key: typed(item) for key, item in value.items()})
    if type(value) is list:
        return (list, [typed(item) for item in value])
    return (type(value), value)


class IndependentTomlCarrierTests(unittest.TestCase):
    def call(self, source, edits, path=("x",)):
        delta, keys = {"edits": edits}, {"selected": path}
        before = copy.deepcopy((delta, keys))
        try:
            return materialize_toml(source, delta, keys)
        finally:
            self.assertEqual((delta, keys), before)

    def assert_materialized(self, result, expected_bytes, expected_values, expected_diff):
        proposed, values, changes = result
        self.assertEqual(proposed, expected_bytes)
        self.assertEqual(typed(tomllib.loads(proposed.decode())), typed(expected_values))
        self.assertEqual(typed(values), typed(expected_values))
        self.assertEqual(typed(changes), typed(expected_diff))

    def assert_change(self, source, change, expected_bytes, expected_values, before, after,
                      path=("x",), before_present=True, after_present=True):
        self.assert_materialized(self.call(source, [change], path), expected_bytes,
            expected_values, [{"field": "selected", "action": change["action"],
                "mode": change["mode"], "before_present": before_present,
                "after_present": after_present, "before": before, "after": after}])

    def test_scalar_replace_preserves_quoted_dotted_table_and_comments_lf_crlf(self):
        for nl in (b"\n", b"\r\n"):
            with self.subTest(newline=nl):
                source = nl.join([b'# top', b'"a.b".x = 0x10 # selected', b'',
                                  b'[other]', b'keep = "# literal" # keep', b''])
                expected = nl.join([b'# top', b'"a.b".x = 17 # selected', b'',
                                    b'[other]', b'keep = "# literal" # keep', b''])
                self.assert_change(source, edit("replace", "value", value=17), expected,
                    {"a.b": {"x": 17}, "other": {"keep": "# literal"}}, 16, 17,
                    path=("a.b", "x"))

    def test_value_add_and_remove_preserve_unrelated_bytes(self):
        self.assert_change(b'# keep\ny = 2\n', edit("add", "value", value=3),
            b'# keep\ny = 2\nx = 3\n', {"y": 2, "x": 3}, None, 3, before_present=False)
        self.assert_change(b'# keep\nx = 1\ny = 2\n', edit("remove", "value"),
            b'# keep\ny = 2\n', {"y": 2}, 1, None, after_present=False)

    def test_item_add_replace_remove_have_literal_occurrence_ledgers(self):
        cases = [
            (edit("add", "item", value=4), b'x = [1, 2, 3, 4] # keep\n', [1, 2, 3, 4]),
            (edit("replace", "item", current=2, value=4), b'x = [1, 4, 3] # keep\n', [1, 4, 3]),
            (edit("remove", "item", current=2), b'x = [1, 3] # keep\n', [1, 3]),
        ]
        for change, expected, values in cases:
            with self.subTest(change=change):
                self.assert_change(b'x = [1, 2, 3] # keep\n', change, expected,
                    {"x": values}, [1, 2, 3], values)

    def test_item_replace_does_not_rebuild_commented_array(self):
        self.assert_change(b'x = [\n  1, # first\n  2, # second\n]\ny = 0x10\n',
            edit("replace", "item", current=2, value=3),
            b'x = [\n  1, # first\n  3, # second\n]\ny = 0x10\n',
            {"x": [1, 3], "y": 16}, [1, 2], [1, 3])

    def test_full_set_add_replace_remove_have_separate_explicit_ledgers(self):
        for change, expected, values in [
            (edit("add", "set", value=[2, 3]), b'x = [1, 2, 3]\ny = 0x10 # keep\n', [1, 2, 3]),
            (edit("replace", "set", value=[3, 4]), b'x = [3, 4]\ny = 0x10 # keep\n', [3, 4]),
            (edit("remove", "set", value=[1, 2]), b'x = []\ny = 0x10 # keep\n', []),
        ]:
            with self.subTest(change=change):
                self.assert_change(b'x = [1, 2]\ny = 0x10 # keep\n', change,
                    expected, {"x": values, "y": 16}, [1, 2], values)

    def test_native_dates_and_numeric_type_distinctions(self):
        source = b'x = 2026-10-13\nstamp = 2026-10-13T12:30:00Z\nclock = 12:30:00\nflag = true\ncount = 1\nratio = 1.0\n'
        expected = b'x = 2026-10-14\nstamp = 2026-10-13T12:30:00Z\nclock = 12:30:00\nflag = true\ncount = 1\nratio = 1.0\n'
        values = {"x": datetime.date(2026, 10, 14),
            "stamp": datetime.datetime(2026, 10, 13, 12, 30, tzinfo=datetime.timezone.utc),
            "clock": datetime.time(12, 30), "flag": True, "count": 1, "ratio": 1.0}
        self.assert_change(source, edit("replace", "value", value=values["x"]), expected,
            values, datetime.date(2026, 10, 13), values["x"])
        for old, new, expected in [(1, True, b'x = true\n'), (1, 1.0, b'x = 1.0\n')]:
            self.assert_change(b'x = 1\n', edit("replace", "value", value=new),
                expected, {"x": new}, old, new)

    def test_noop_uses_original_spelling_without_library_or_effects(self):
        real_import = builtins.__import__
        def without_tomlkit(name, *args, **kwargs):
            if name == "tomlkit" or name.startswith("tomlkit."):
                raise AssertionError("No-op must not load TOMLKit")
            return real_import(name, *args, **kwargs)
        with patch("builtins.__import__", side_effect=without_tomlkit):
            importlib.reload(carrier)
            source = b'# keep\r\nx = 0x10\r\n'
            self.assert_materialized(self.call(source, [edit("replace", "value", value=16)]),
                source, {"x": 16}, [])
            self.assert_materialized(self.call(source, [edit("replace", "value", value=17),
                edit("replace", "value", value=16)]), source, {"x": 16}, [])

    def test_missing_duplicate_and_malformed_inputs_refuse(self):
        cases = [
            (b'x = [1, 1]\n', [edit("remove", "item", current=1)], ("x",)),
            (b'x = [1]\n', [edit("replace", "item", current=2, value=3)], ("x",)),
            (b'x = 1\nx = 2\n', [edit("replace", "value", value=3)], ("x",)),
            (b'x = [\n', [edit("replace", "value", value=3)], ("x",)),
            (b'x = "\xff"\n', [], ("x",)),
            (b'x = 1\n', [{**edit("replace", "value", value=2), "index": 0}], ("x",)),
            (b'x = 1\n', [edit("replace", "value", value=2)], ()),
            (b'x = 1\n', [edit("replace", "value", value=2)], "x"),
            (b'x = 1\n', [edit("replace", "value", value=None)], ("x",)),
            (b'x = 1\n', [edit("replace", "value", value={1, 2})], ("x",)),
        ]
        for source, changes, path in cases:
            with self.subTest(source=source, changes=changes, path=path), self.assertRaises(TomlFailure):
                self.call(source, changes, path)

    def test_independent_oracle_detects_wrong_bytes_values_types_and_diff(self):
        expected = [{"field": "selected", "action": "replace", "mode": "value",
            "before_present": True, "after_present": True, "before": 1, "after": 2}]
        for forged in [
            (b'x = 3\ny = 0\n', {"x": 2, "y": 0}, expected),
            (b'x = 2\ny = 1\n', {"x": 2, "y": 1}, expected),
            (b'x = 2\ny = 0\n', {"x": 2.0, "y": 0}, expected),
            (b'x = 2\ny = 0\n', {"x": 2, "y": 0}, []),
            (b'x = 2\ny = 0\n', {"x": 2, "y": 0}, expected + expected),
        ]:
            with self.subTest(forged=forged), self.assertRaises(AssertionError):
                self.assert_materialized(forged, b'x = 2\ny = 0\n', {"x": 2, "y": 0}, expected)

    def test_lossy_baseline_and_wrong_complete_proposal_refuse(self):
        import tomlkit

        source = b'x = 1\ny = 0\n'
        with patch.object(tomlkit, "dumps", return_value="x = 1\ny = 0 # normalized\n"):
            with self.assertRaises(TomlFailure):
                self.call(source, [edit("replace", "value", value=2)])
        for proposal in ("x = 2\ny = 9\n", "x = 2.0\ny = 0\n", "x = [\n"):
            with self.subTest(proposal=proposal), patch.object(tomlkit, "dumps",
                    side_effect=[source.decode(), proposal]), self.assertRaises(TomlFailure):
                self.call(source, [edit("replace", "value", value=2)])

    def test_calls_never_access_filesystem_effect_apis(self):
        import tomlkit  # Load the selected dependency before denying effect APIs.

        with ExitStack() as denied:
            for owner, name in [(builtins, "open"), (os, "open"), (os, "unlink"),
                    (os, "remove"), (os, "rename"), (os, "replace"), (os, "mkdir"),
                    (Path, "write_bytes"), (Path, "write_text"), (Path, "read_bytes"),
                    (Path, "read_text"), (Path, "open")]:
                denied.enter_context(patch.object(owner, name,
                    side_effect=AssertionError("Pure materialization attempted filesystem access")))
            self.assert_change(b'x = 1\n', edit("replace", "value", value=2),
                b'x = 2\n', {"x": 2}, 1, 2)
            self.assert_materialized(self.call(b'x = 1\n', []), b'x = 1\n', {"x": 1}, [])
            with self.assertRaises(TomlFailure):
                self.call(b'x = [1, 1]\n', [edit("remove", "item", current=1)])

    def test_alias_bindings_cannot_turn_complete_noop_into_normalization(self):
        source = b'x = 0x10 # keep\n'
        delta = {"edits": [
            {**edit("replace", "value", value=17), "field": "a"},
            {**edit("replace", "value", value=16), "field": "b"},
        ]}
        keys = {"a": ("x",), "b": ("x",)}
        supplied = copy.deepcopy((delta, keys))
        try:
            result = materialize_toml(source, delta, keys)
        except TomlFailure:
            pass  # Ambiguous bindings may be refused, never normalized.
        else:
            self.assert_materialized(result, source, {"x": 16}, [])
        finally:
            self.assertEqual((delta, keys), supplied)

    def test_item_removal_preserves_retained_whitespace_or_refuses(self):
        source = b'x = [1,  2 ,  3]\n'
        try:
            result = self.call(source, [edit("remove", "item", current=1)])
        except TomlFailure:
            return  # A known lossy dependency layout must fail closed.
        self.assert_materialized(result, b'x = [  2 ,  3]\n', {"x": [2, 3]}, [
            {"field": "selected", "action": "remove", "mode": "item",
             "before_present": True, "after_present": True,
             "before": [1, 2, 3], "after": [2, 3]}])


if __name__ == "__main__":
    unittest.main()
