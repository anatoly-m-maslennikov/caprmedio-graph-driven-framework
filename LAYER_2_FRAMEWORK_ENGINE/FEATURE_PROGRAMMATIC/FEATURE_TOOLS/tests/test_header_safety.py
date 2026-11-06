"""Malformed Headers stop before scalar edits or YAML graph construction."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from artifact_metadata import update_atom
from carrier_aliases import carrier_read_view
from header_groups import nested_header
from header_yaml import header_scalar, parse_header


class HeaderSafetyTests(unittest.TestCase):
    def test_relations_must_be_a_mapping_before_any_header_consumer_proceeds(self):
        for value in ("CA-R-2", ["CA-R-2"], None, 2):
            metadata = {"relations": value}
            for consumer in (carrier_read_view, nested_header):
                with self.subTest(value=value, consumer=consumer.__name__), self.assertRaises(ValueError):
                    consumer(metadata)
        source = "relations: CA-R-2\nversion: 1\nupdated_at: old"
        with self.assertRaises(ValueError):
            parse_header(source)
        with self.assertRaises(RuntimeError):
            update_atom(source, "---", "2026-11-06 12:00:00 +0000", False)

    def test_empty_relations_mapping_remains_valid_and_unchanged(self):
        metadata = {"relations": {}}
        self.assertEqual(nested_header(metadata), metadata)
        self.assertEqual(parse_header("relations: {}"), metadata)

    def test_excessive_depth_stops_before_compose(self):
        for depth in (65, 10_000):
            source = "extra: " + "[" * depth + "0" + "]" * depth
            with self.subTest(depth=depth), patch("header_yaml_nodes.yaml.compose") as compose:
                with self.assertRaisesRegex(ValueError, "safety ceiling"):
                    header_scalar(source, "version")
                compose.assert_not_called()

    def test_excessive_events_stop_before_compose(self):
        source = "extra: [" + "0," * 100_001 + "]"
        with patch("header_yaml_nodes.yaml.compose") as compose:
            with self.assertRaisesRegex(ValueError, "safety ceiling"):
                parse_header(source)
            compose.assert_not_called()


if __name__ == "__main__":
    unittest.main()
