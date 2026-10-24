"""Focused checks for partial results from generic Atom text search."""

from __future__ import annotations

import argparse
import io
import json
import sys
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
for directory in (TOOLS, TOOLS / "ATOM_SEARCH", TOOLS / "ATOM_SEARCH/tests"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import atom_operations as operations  # noqa: E402
import test_subject_lookup as fixtures  # noqa: E402
from technical_diagnostics import TechnicalDiagnosticLogger  # noqa: E402


class GenericAtomScanWarningsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = fixtures.SubjectLookupTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.role = self.fixture.role
        self.under = self.role.relative_to(self.root).as_posix()

    def _args(self, **overrides: object) -> argparse.Namespace:
        values = dict(
            under=self.under, lifecycle="active", atom=None, query=None, limit=None, view="metadata"
        )
        values.update(overrides)
        return argparse.Namespace(**values)

    def _invalid(self, atom_id: str = "CA-R-3") -> Path:
        path = self.role / f"{atom_id}-CORE-REQUIREMENT--invalid.md"
        path.write_text("---\natom_id: [invalid\n---\n", encoding="utf-8")
        return path

    def _logger(self) -> TechnicalDiagnosticLogger:
        return TechnicalDiagnosticLogger("CA", self.root, "test", io.StringIO(), "host")

    def test_valid_match_survives_malformed_carrier_with_cli_result_error(self) -> None:
        invalid = self._invalid()
        sink = io.StringIO()
        logger_instance = TechnicalDiagnosticLogger("CA", self.root, "test", sink, "host")
        with patch.object(operations, "_cli_logger", return_value=logger_instance) as logger:
            result = operations.run_search(self.root, self._args(query=["CA-R-1"]))

        logger.assert_called_once()
        self.assertEqual(1, result["count"])
        self.assertEqual("CA-R-1", result["atoms"][0]["metadata"]["atom_id"])
        self.assertFalse(result["complete"])
        self.assertEqual(["schema_invalid"], [error["code"] for error in result["errors"]])
        self.assertEqual(invalid.relative_to(self.root).as_posix(), result["warnings"][0]["path"])
        record = json.loads(sink.getvalue())
        self.assertEqual(invalid.relative_to(self.root).as_posix(), record["relative_path"])
        self.assertTrue(record["reason"])

    def test_all_invalid_carriers_are_incomplete_and_attributable(self) -> None:
        first = self.role / "CA-R-1-CORE-REQUIREMENT--fixture.md"
        second = self.role / "CA-R-2-CORE-REQUIREMENT--fixture.md"
        for path in (first, second):
            path.write_text("---\natom_id: [invalid\n---\n", encoding="utf-8")

        with patch.object(operations, "_cli_logger", return_value=self._logger()) as logger:
            result = operations.run_search(self.root, self._args())

        self.assertEqual(2, logger.call_count)
        self.assertEqual({"count", "atoms", "complete", "warnings", "errors"}, set(result))
        self.assertEqual([], result["atoms"])
        self.assertFalse(result["complete"])
        self.assertEqual(["schema_invalid"], [error["code"] for error in result["errors"]])
        self.assertEqual(
            {path.relative_to(self.root).as_posix() for path in (first, second)},
            {warning["path"] for warning in result["warnings"]},
        )

    def test_default_scan_and_mutation_refusal_remain_unchanged(self) -> None:
        invalid = self._invalid()
        with patch.object(operations, "_cli_logger") as logger:
            atoms = operations.scan_atoms(self.root, under=self.under, lifecycle="active")
        logger.assert_not_called()
        self.assertEqual({"CA-R-1", "CA-R-2"}, {atom.atom_id for atom in atoms})

        payload = self.root / "update.json"
        payload.write_text(
            json.dumps({"atoms": [{"selector": invalid.name, "content": "changed"}]}),
            encoding="utf-8",
        )
        before = {
            path.relative_to(self.root).as_posix(): path.read_bytes()
            for path in self.root.rglob("*")
            if path.is_file()
        }
        with self.assertRaises(operations.ToolError) as raised:
            operations.run_update(
                self.root, argparse.Namespace(input=str(payload), apply=True, stage_preview=False)
            )
        self.assertEqual("atom-not-found", raised.exception.code)
        self.assertEqual(
            before,
            {
                path.relative_to(self.root).as_posix(): path.read_bytes()
                for path in self.root.rglob("*")
                if path.is_file()
            },
        )

    def test_logger_failure_is_visible_without_outer_cli_duplicate(self) -> None:
        self._invalid()
        with patch.object(operations, "_cli_logger", return_value=None) as logger:
            result = operations.run_search(self.root, self._args())

        logger.assert_called_once()
        logging_warnings = [
            warning
            for warning in result["warnings"]
            if warning["code"] == "diagnostic_logging_failed"
        ]
        self.assertEqual(1, len(logging_warnings))
        self.assertIn("technical diagnostic emission failed", logging_warnings[0]["reason"])

    def test_cli_envelope_keeps_partial_result_and_response_error(self) -> None:
        self._invalid()
        argv = [
            "atom-search",
            "--repository",
            str(self.root),
            "run",
            "--under",
            self.under,
            "--query",
            "CA-R-1",
        ]
        stdout, stderr = io.StringIO(), io.StringIO()
        with (
            patch.object(operations, "_cli_logger", return_value=self._logger()),
            patch.object(sys, "argv", argv),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            code = operations.cli("ATOM_SEARCH")

        envelope = json.loads(stdout.getvalue())
        self.assertEqual(0, code)
        self.assertTrue(envelope["ok"])
        self.assertFalse(envelope["result"]["complete"])
        self.assertEqual(
            ["schema_invalid"], [error["code"] for error in envelope["result"]["errors"]]
        )
        self.assertEqual("", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
