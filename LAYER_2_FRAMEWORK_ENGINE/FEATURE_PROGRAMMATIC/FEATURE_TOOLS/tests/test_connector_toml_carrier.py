"""Author controls for pure CST confinement and truthful layout refusals."""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from connector_toml_carrier import materialize_toml
from connector_toml_parse import TomlFailure


class TomlCarrierTests(unittest.TestCase):
    def call(self, source, edits, path=("x",)):
        delta = {"edits": edits}
        original = copy.deepcopy(delta)
        result = materialize_toml(source, delta, {"field": path})
        self.assertEqual(delta, original)
        return result

    def edit(self, action, mode="value", **values):
        return {"action": action, "mode": mode, "field": "field", **values}

    def test_crlf_add_remove_keep_unrelated_trivia(self):
        added = self.call(b'# keep\r\ny = 0x10\r\n', [self.edit("add", value=3)])
        self.assertEqual(added[0], b'# keep\r\ny = 0x10\r\nx = 3\r\n')
        removed = self.call(added[0], [self.edit("remove")])
        self.assertEqual(removed[0], b'# keep\r\ny = 0x10\r\n')

    def test_item_removal_retains_other_comment_and_spelling(self):
        source = b'x = [\n  1, # selected\n  0x10, # retained\n]\ny = "keep"\n'
        result = self.call(source, [self.edit("remove", "item", current=1)])
        self.assertEqual(result[0], b'x = [\n  0x10, # retained\n]\ny = "keep"\n')

    def test_multiple_edits_and_compensating_noop(self):
        source = b'x = 0x10 # keep\n'
        result = self.call(source, [self.edit("replace", value=17), self.edit("replace", value=18)])
        self.assertEqual(result[0], b'x = 18 # keep\n')
        self.assertEqual(len(result[2]), 1)
        self.assertEqual(result[2][0]["before"], 16)
        self.assertEqual(result[2][0]["after"], 18)
        self.assertEqual(self.call(source, [self.edit("replace", value=17),
                         self.edit("replace", value=16)]), (source, {"x": 16}, []))

    def test_unsupported_table_occurrence_refuses_instead_of_normalizing(self):
        source = b'[x]\na = 1 # keep\n[other]\nb = 2\n'
        with self.assertRaises(TomlFailure):
            self.call(source, [self.edit("replace", value={"a": 3})])

    def test_unsupported_intermediate_value_refuses_even_when_net_noop(self):
        with self.assertRaises(TomlFailure):
            self.call(b'x = 1\n', [self.edit("replace", value=None), self.edit("replace", value=1)])

    def test_dependency_trailing_delimiter_loss_refuses(self):
        with self.assertRaises(TomlFailure):
            self.call(b'x = [1, 2,]\n', [self.edit("remove", "item", current=1)])

    def test_multiline_crlf_item_add_preserves_line_convention(self):
        result = self.call(b'x = [\r\n  1,\r\n]\r\n', [self.edit("add", "item", value=2)])
        self.assertEqual(result[0], b'x = [\r\n  1,\r\n  2,\r\n]\r\n')


if __name__ == "__main__":
    unittest.main()
