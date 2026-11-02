from __future__ import annotations

import datetime
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_toml_parse import equal_values, parse_source, represent_document


class TomlParsingTests(unittest.TestCase):
    def test_complete_text_and_values(self):
        source = b'# unchanged\r\nschema_version = 1\r\n[extra]\r\nitems = ["a", "b"]\r\n'
        text, document = parse_source(source)
        self.assertEqual(text.encode(), source)
        self.assertEqual(document, {"schema_version": 1, "extra": {"items": ["a", "b"]}})
        self.assertEqual(represent_document(document), document)

    def test_duplicate_and_invalid_utf8_fail(self):
        for source in (b'x = 1\nx = 2\n', b'x = "\xff"'):
            with self.subTest(source=source), self.assertRaises(ValueError):
                parse_source(source)

    def test_typed_values_remain_native_and_fail_unresolved_json_representation(self):
        _, document = parse_source(b'day = 2026-10-13\n')
        self.assertEqual(document["day"], datetime.date(2026, 10, 13))
        with self.assertRaises(ValueError):
            represent_document(document)

    def test_exact_value_equality_retains_types(self):
        self.assertFalse(equal_values(1, True))
        self.assertFalse(equal_values(1, 1.0))
        self.assertTrue(equal_values({"x": [float("nan")]}, {"x": [float("nan")]}))


if __name__ == "__main__":
    unittest.main()
