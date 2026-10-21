"""Focused public lookup checks for invalid per-Atom schema handling."""
from __future__ import annotations

import shutil
from pathlib import Path
import sys
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
for directory in (TOOLS, TOOLS / "ATOM_SEARCH", TOOLS / "ATOM_SEARCH/tests"):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import atom_search as provider  # noqa: E402
import test_subject_lookup_provider as provider_fixtures  # noqa: E402


class InvalidAtomSchemaWarningsTests(unittest.TestCase):
    """Invalid individual carriers are warnings; frontier failures remain errors."""

    EXPECTED_VALID_MATCHES = [
        ("CA-R-1", 1, "depends_on", "Core/Atom/child"),
        ("CA-R-1", 1, "governs", "Core/Atom"),
    ]

    def setUp(self) -> None:
        self.fixture = provider_fixtures.SubjectLookupProviderTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.adapter = self.fixture.adapter
        self.request = self.fixture.request
        self.sources = self.fixture.fixture

    def _invoke(self, request=None):
        before = self.fixture.ledger()
        result = self.adapter.invoke(self.request if request is None else request).model_dump(mode="json")
        self.assertEqual({"data", "current_state", "effects", "errors"}, set(result))
        self.assertEqual(before, self.fixture.ledger())
        self.assertFalse((self.root / ".caprmedio_tmp").exists())
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())
        return result

    def _warnings(self, result):
        data = result["data"]
        self.assertIsNotNone(data)
        warnings = data["warnings"]
        self.assertIsInstance(warnings, list)
        self.assertTrue(warnings)
        return warnings

    def _assert_valid_matches(self, result) -> None:
        self.assertEqual(
            self.EXPECTED_VALID_MATCHES,
            [(row["atom_id"], row["version"], row["field"], row["value"])
             for row in result["data"]["matches"]],
        )

    def _assert_warning_for(self, warnings, path: Path) -> None:
        relative = path.relative_to(self.root).as_posix()
        warning = next((item for item in warnings if item.get("path") == relative), None)
        self.assertIsNotNone(warning, warnings)
        self.assertNotIn(str(self.root), str(warning))
        reason = warning.get("reason")
        self.assertIsInstance(reason, str)
        self.assertTrue(reason)

    def _write_invalid(self, atom_id: str, *, matching: bool = False) -> Path:
        path = self.sources.role / f"{atom_id}-CORE-REQUIREMENT--invalid.md"
        if matching:
            path.write_text(
                "---\n"
                f"atom_id: {atom_id}\n"
                "version: 1\n"
                "status: Active\n"
                "content_role: Requirement\n"
                "current_scope_unit: CORE\n"
                "updated_at: now\n"
                "subjects:\n"
                "  governs: Core/Atom\n"
                "  depends_on: invalid\n"
                "---\nInvalid matching carrier\n",
                encoding="utf-8",
            )
        else:
            path.write_text("---\natom_id: [invalid\n---\nUnrelated malformed carrier\n", encoding="utf-8")
        return path

    def test_valid_match_survives_unrelated_invalid_carrier_as_warning(self) -> None:
        invalid = self._write_invalid("CA-R-3")

        result = self._invoke()

        self.assertEqual([], result["errors"])
        self.assertEqual([], result["effects"])
        self._assert_valid_matches(result)
        self.assertFalse(result["data"]["complete"])
        self._assert_warning_for(self._warnings(result), invalid)

    def test_valid_match_survives_matching_invalid_carrier_without_matching_it(self) -> None:
        invalid = self._write_invalid("CA-R-3", matching=True)

        result = self._invoke()

        self.assertEqual([], result["errors"])
        self.assertEqual([], result["effects"])
        self._assert_valid_matches(result)
        self.assertFalse(result["data"]["complete"])
        self._assert_warning_for(self._warnings(result), invalid)

    def test_all_invalid_carriers_return_empty_incomplete_data_with_warnings(self) -> None:
        invalid_one = self.sources.role / "CA-R-1-CORE-REQUIREMENT--fixture.md"
        invalid_two = self.sources.role / "CA-R-2-CORE-REQUIREMENT--fixture.md"
        invalid_one.write_text("---\natom_id: [invalid\n---\n", encoding="utf-8")
        invalid_two.write_text("---\natom_id: [invalid\n---\n", encoding="utf-8")

        result = self._invoke()

        self.assertEqual([], result["errors"])
        self.assertEqual([], result["effects"])
        self.assertEqual([], result["data"]["matches"])
        self.assertEqual([], result["current_state"])
        self.assertFalse(result["data"]["complete"])
        warnings = self._warnings(result)
        self._assert_warning_for(warnings, invalid_one)
        self._assert_warning_for(warnings, invalid_two)

    def test_duplicate_identity_remains_an_error_not_a_warning(self) -> None:
        duplicate = self.sources.role / "CA-R-1-CORE-REQUIREMENT--duplicate.md"
        shutil.copyfile(self.sources.role / "CA-R-1-CORE-REQUIREMENT--fixture.md", duplicate)

        result = self._invoke()

        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual("target_ambiguous", result["errors"][0]["code"])
        self.assertEqual([], result["effects"])

    def test_security_source_boundary_remains_an_error(self) -> None:
        linked = self.sources.role / "CA-R-3-CORE-REQUIREMENT--linked.md"
        linked.symlink_to(self.sources.role / "CA-R-1-CORE-REQUIREMENT--fixture.md")

        result = self._invoke()

        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertTrue(result["errors"])
        self.assertEqual([], result["effects"])

    def test_stale_contract_remains_an_error(self) -> None:
        source = self.root / provider.SOURCE_PINS[0]["path"]
        source.write_bytes(source.read_bytes().replace(b"CA-R-1936", b"CA-R-99999", 1))

        result = self._invoke()

        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual("stale_state", result["errors"][0]["code"])
        self.assertEqual([], result["effects"])

    def test_bounded_source_io_remains_an_error(self) -> None:
        with patch.object(
            provider,
            "run_subject_search",
            side_effect=provider.ToolError(
                "subject-source-verification-unavailable", "bounded source unavailable"
            ),
        ):
            result = self._invoke()

        self.assertIsNone(result["data"])
        self.assertIsNone(result["current_state"])
        self.assertEqual("backend_failure", result["errors"][0]["code"])
        self.assertEqual([], result["effects"])


if __name__ == "__main__":
    unittest.main()
