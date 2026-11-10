# CA-E-676@15
"""Result-file format and failure checks at the real filesystem boundary."""

from __future__ import annotations

import csv
from datetime import date
from decimal import Decimal
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import toon_format

sys.path.insert(0, str(Path(__file__).resolve().parents[3]))
from APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.result_files import write_result_file  # noqa: E402


class ResultFileTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.columns = [
            "same",
            "same",
            "integer",
            "flag",
            "claim",
            "nested",
            "amount",
            "date",
            "blob",
        ]
        self.claim = "Привет 世界\n```CFEL\nAtom.Content.Claim{::1};\n```"
        self.rows = [
            [
                None,
                "",
                0,
                False,
                self.claim,
                {"items": [None, "", 3]},
                Decimal("1.20"),
                date(2026, 11, 11),
                b"\x00\xff",
            ],
            ["null", "NULL", 2**53, True, "second\nline", [], Decimal("2"), date(2026, 1, 1), b""],
        ]
        self.expected = {
            "columns": self.columns,
            "rows": [
                [
                    None,
                    "",
                    0,
                    False,
                    self.claim,
                    {"items": [None, "", 3]},
                    "1.20",
                    "2026-11-11",
                    "base64:AP8=",
                ],
                [
                    "null",
                    "NULL",
                    str(2**53),
                    True,
                    "second\nline",
                    [],
                    "2",
                    "2026-01-01",
                    "base64:",
                ],
            ],
        }

    def read(self, descriptor: dict, result_format: str) -> object:
        path = self.root / descriptor["path"]
        if result_format == "json_matrix":
            return json.loads(path.read_text(encoding="utf-8"))
        if result_format == "toon":
            return toon_format.loads(path.read_text(encoding="utf-8"))
        with path.open(encoding="utf-8", newline="") as stream:
            return list(csv.reader(stream, quoting=csv.QUOTE_NOTNULL))

    def test_json_and_official_toon_round_trip_matrix_types_and_duplicate_names(self) -> None:
        paths = set()
        for result_format in ("json_matrix", "toon"):
            with self.subTest(result_format=result_format):
                descriptor = write_result_file(
                    self.root,
                    self.columns,
                    iter(self.rows),
                    result_format=result_format,
                    offset=4,
                    has_more=True,
                )
                self.assertEqual(self.expected, self.read(descriptor, result_format))
                self.assertEqual(
                    (2, len(self.columns), 4, True),
                    (
                        descriptor["row_count"],
                        descriptor["column_count"],
                        descriptor["offset"],
                        descriptor["has_more"],
                    ),
                )
                self.assertEqual(result_format, descriptor["format"])
                self.assertTrue(
                    descriptor["path"].startswith(".caprmedio_tmp/workbench/query_results/")
                )
                self.assertNotIn(descriptor["path"], paths)
                paths.add(descriptor["path"])

    def test_csv_distinguishes_null_and_empty_and_preserves_multiline_data(self) -> None:
        descriptor = write_result_file(
            self.root, self.columns, iter(self.rows), result_format="csv"
        )
        path = self.root / descriptor["path"]
        raw = path.read_bytes()
        self.assertIn(b'\r\n,"",', raw)
        self.assertTrue(raw.endswith(b"\r\n"))
        rows = self.read(descriptor, "csv")
        self.assertEqual(self.columns, rows[0])
        self.assertIsNone(rows[1][0])
        self.assertEqual("", rows[1][1])
        self.assertEqual(self.claim, rows[1][4])
        self.assertEqual({"items": [None, "", 3]}, json.loads(rows[1][5]))
        self.assertEqual(str(2**53), rows[2][2])
        self.assertEqual("False", rows[1][3])

    def test_zero_rows_keep_headers_and_default_is_json_matrix(self) -> None:
        default = write_result_file(self.root, ["x", "x"], [])
        self.assertEqual("json_matrix", default["format"])
        self.assertEqual({"columns": ["x", "x"], "rows": []}, self.read(default, "json_matrix"))
        for result_format in ("csv", "toon"):
            descriptor = write_result_file(self.root, ["x", "x"], [], result_format=result_format)
            expected = (
                [["x", "x"]] if result_format == "csv" else {"columns": ["x", "x"], "rows": []}
            )
            self.assertEqual(expected, self.read(descriptor, result_format))
            self.assertEqual(0, descriptor["row_count"])

    def test_failed_stream_or_unsupported_value_leaves_no_partial_file(self) -> None:
        def broken():
            yield ["first"]
            raise RuntimeError("stream failed")

        for result_format in ("json_matrix", "csv", "toon"):
            with self.subTest(result_format=result_format):
                with self.assertRaisesRegex(RuntimeError, "stream failed"):
                    write_result_file(self.root, ["x"], broken(), result_format=result_format)
                with self.assertRaisesRegex(ValueError, "unsupported query result value"):
                    write_result_file(self.root, ["x"], [[object()]], result_format=result_format)
                with self.assertRaisesRegex(ValueError, "row width"):
                    write_result_file(self.root, ["x"], [["a", "b"]], result_format=result_format)
                directory = self.root / ".caprmedio_tmp/workbench/query_results"
                self.assertEqual([], list(directory.iterdir()))

    def test_symlinked_destination_components_do_not_write_outside_project(self) -> None:
        for relative in (
            ".caprmedio_tmp",
            ".caprmedio_tmp/workbench",
            ".caprmedio_tmp/workbench/query_results",
        ):
            with self.subTest(component=relative), tempfile.TemporaryDirectory() as directory:
                root = Path(directory).resolve()
                outside = root / "outside"
                outside.mkdir()
                target = root / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.symlink_to(outside, target_is_directory=True)
                with self.assertRaises((OSError, RuntimeError)):
                    write_result_file(root, ["x"], [[1]])
                self.assertEqual([], list(outside.iterdir()))

    def test_existing_result_filename_is_not_followed_or_overwritten(self) -> None:
        directory = self.root / ".caprmedio_tmp/workbench/query_results"
        directory.mkdir(parents=True)
        outside = self.root / "outside.txt"
        outside.write_text("keep", encoding="utf-8")
        (directory / "test-identifier.json").symlink_to(outside)
        with patch(
            "APP_WORKBENCH.FEATURE_WORKBENCH_BACKEND.result_files.uuid.uuid7",
            return_value="test-identifier",
        ):
            with self.assertRaises(FileExistsError):
                write_result_file(self.root, ["x"], [[1]])
        self.assertEqual("keep", outside.read_text(encoding="utf-8"))
        self.assertTrue((directory / "test-identifier.json").is_symlink())

    def test_invalid_metadata_fails_before_creating_any_directory(self) -> None:
        for kwargs in ({"result_format": "bad"}, {"offset": -1}, {"offset": True}, {"has_more": 1}):
            with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                write_result_file(self.root, ["x"], [], **kwargs)
        self.assertFalse((self.root / ".caprmedio_tmp").exists())

    def test_relative_root_never_falls_back_to_the_current_directory(self) -> None:
        with self.assertRaisesRegex(ValueError, "absolute selected path"):
            write_result_file(".", ["x"], [[1]])


if __name__ == "__main__":
    unittest.main()
