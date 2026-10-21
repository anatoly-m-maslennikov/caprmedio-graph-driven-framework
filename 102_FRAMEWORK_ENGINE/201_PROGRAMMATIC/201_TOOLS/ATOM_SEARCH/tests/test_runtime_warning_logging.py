"""Focused checks for AtomSearch technical warnings on the Docker stderr stream."""

from __future__ import annotations

import io
import json
import os
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
for directory in (TOOLS, TOOLS / "ATOM_SEARCH", TOOLS / "ATOM_SEARCH/tests"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import atom_search as provider  # noqa: E402
from technical_diagnostics import TechnicalDiagnosticLogger, _runtime_version, make_technical_logger  # noqa: E402
import test_subject_lookup_provider as provider_fixtures  # noqa: E402


class _FailingStream:
    def write(self, _value: str) -> int:
        raise OSError("diagnostic sink unavailable")

    def flush(self) -> None:
        raise OSError("diagnostic sink unavailable")


class RuntimeWarningLoggingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = provider_fixtures.SubjectLookupProviderTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.sources = self.fixture.fixture
        self.settings = self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        self.settings.write_text(
            'schema_version = "2.0"\n'
            '[project]\nname = "lookup"\n'
            '[artifacts.identity]\nproject_prefix = "TEST"\n'
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n',
            encoding="utf-8",
        )
        self.request = self.fixture.request

    def _invalid(self) -> Path:
        path = self.sources.role / "CA-R-3-CORE-REQUIREMENT--invalid.md"
        path.write_text("---\natom_id: [invalid\n---\n", encoding="utf-8")
        return path

    def test_invalid_atom_warning_is_one_line_structured_stderr_with_project_prefix(self) -> None:
        invalid = self._invalid()
        stream = io.StringIO()
        with patch.dict(os.environ, {"CAPRMEDIO_RUNTIME_NAMESPACE": ""}):
            result = provider.create_adapter(self.root, diagnostic_stream=stream).invoke(self.request)
        record = json.loads(stream.getvalue())

        self.assertEqual([], result.errors)
        self.assertFalse(result.data.complete)
        warning = next(item for item in result.data.warnings if item.path == invalid.relative_to(self.root).as_posix())
        self.assertEqual("schema_invalid", warning.code)
        self.assertEqual("WARNING", record["severity"])
        self.assertEqual("atom_schema_invalid", record["event"])
        self.assertEqual("ATOM_SEARCH", record["component"])
        self.assertEqual("host", record["environment"])
        self.assertEqual(_runtime_version(), record["version"])
        self.assertEqual("TEST", record["project_prefix"])
        self.assertEqual("schema_invalid", record["code"])
        self.assertEqual(warning.path, record["relative_path"])
        self.assertNotIn(str(self.root), stream.getvalue())
        self.assertNotIn("_journal", stream.getvalue())

    def test_second_project_prefix_is_exact_in_explicit_docker_environment(self) -> None:
        self.settings.write_text(self.settings.read_text(encoding="utf-8").replace("TEST", "SECOND"),
                                 encoding="utf-8")
        self._invalid()
        stream = io.StringIO()
        result = provider.create_adapter(self.root, diagnostic_stream=stream,
                                         diagnostic_environment="docker").invoke(self.request)
        record = json.loads(stream.getvalue())

        self.assertEqual([], result.errors)
        self.assertFalse(result.data.complete)
        self.assertEqual("SECOND", record["project_prefix"])
        self.assertEqual("docker", record["environment"])

    def test_diagnostic_sink_failure_is_returned_without_losing_valid_matches(self) -> None:
        self._invalid()
        result = provider.create_adapter(self.root, diagnostic_stream=_FailingStream()).invoke(self.request)

        self.assertEqual([], result.errors)
        self.assertEqual("CA-R-1", result.data.matches[0].atom_id)
        self.assertFalse(result.data.complete)
        self.assertIn("schema_invalid", {warning.code for warning in result.data.warnings})
        failure = next(warning for warning in result.data.warnings
                        if warning.code == "diagnostic_logging_failed")
        self.assertIn("diagnostic sink unavailable", failure.reason)
        self.assertIn("technical diagnostic emission failed", failure.reason)

    def test_logger_redacts_secret_and_bounds_reason(self) -> None:
        stream = io.StringIO()
        logger = TechnicalDiagnosticLogger("TEST", self.root, "test-version", stream, "host")
        self.assertIsNone(logger.emit(
            code="schema_invalid", relative_path="atoms/bad.md",
            reason="token=super-secret " + ("x" * 2_000),
        ))
        line = stream.getvalue()
        self.assertLessEqual(len(line.encode("utf-8")), 4_096)
        self.assertNotIn("super-secret", line)
        self.assertIn("<redacted>", line)

    def test_logger_preserves_long_uppercase_unicode_prefix_exactly(self) -> None:
        stream = io.StringIO()
        prefix = "Ä" * 300
        logger, error = make_technical_logger(
            {"artifacts": {"identity": {"project_prefix": prefix}}}, self.root,
            stream=stream, environment="host")
        self.assertIsNone(error)
        self.assertIsNotNone(logger)
        self.assertIsNone(logger.emit(code="schema_invalid", relative_path="atoms/bad.md", reason="safe"))
        self.assertEqual(prefix, json.loads(stream.getvalue())["project_prefix"])

    def test_logger_reports_oversize_prefix_without_writing(self) -> None:
        stream = io.StringIO()
        prefix = "Ä" * 3_000
        logger, error = make_technical_logger(
            {"artifacts": {"identity": {"project_prefix": prefix}}}, self.root,
            stream=stream, environment="host")
        self.assertIsNone(error)
        self.assertIsNotNone(logger)
        failure = logger.emit(code="schema_invalid", relative_path="atoms/bad.md", reason="safe")

        self.assertIsNotNone(failure)
        self.assertIn("bounded output size", failure)
        self.assertEqual("", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
