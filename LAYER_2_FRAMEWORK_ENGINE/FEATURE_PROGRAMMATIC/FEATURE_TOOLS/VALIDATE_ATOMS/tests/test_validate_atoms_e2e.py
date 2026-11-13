"""Integrity checks for the historical, source-authored golden corpus."""

from __future__ import annotations

import hashlib
from pathlib import Path
import unittest

from golden_fixtures import (
    fixture_path,
    read_json,
)
from golden_support import assert_report_contract

HERE = Path(__file__).resolve().parent
MANIFEST = read_json(HERE / "cases.json")


class GoldenCorpus(unittest.TestCase):
    maxDiff = 12000

    def test_manifest_and_expected_reports(self) -> None:
        self.assertEqual(set(MANIFEST), {"schema_version", "cases"})
        self.assertEqual(MANIFEST["schema_version"], 1)
        self.assertTrue(MANIFEST["cases"])
        ids: set[str] = set()
        for case in MANIFEST["cases"]:
            with self.subTest(case=case["case_id"]):
                self.assertEqual(
                    set(case),
                    {
                        "case_id",
                        "request",
                        "fixture_paths",
                        "authority",
                        "check_codes",
                        "expected_report",
                        "expected_exit_code",
                    },
                )
                self.assertNotIn(case["case_id"], ids)
                ids.add(case["case_id"])
                self.assertTrue(case["authority"])
                self.assertTrue(case["fixture_paths"])
                self.assertTrue(case["check_codes"])
                fixture_path(case["request"]).read_bytes()
                for path in case["fixture_paths"]:
                    self.assertTrue(fixture_path(path).exists(), path)
                expected = read_json(fixture_path(case["expected_report"]))
                assert_report_contract(self, expected)
                self.assertEqual(
                    case["expected_exit_code"],
                    {"valid": 0, "invalid": 1, "incomplete": 2, "error": 3}[expected["result"]],
                )

    def test_authority_copies_are_exact(self) -> None:
        for item in read_json(HERE / "source_bindings.json"):
            with self.subTest(authority=item["atom_id"]):
                actual = hashlib.sha256(fixture_path(item["fixture_path"]).read_bytes()).hexdigest()
                self.assertEqual(
                    actual, item["sha256"], "fixture bytes diverged from reviewed source binding"
                )


if __name__ == "__main__":
    unittest.main()
