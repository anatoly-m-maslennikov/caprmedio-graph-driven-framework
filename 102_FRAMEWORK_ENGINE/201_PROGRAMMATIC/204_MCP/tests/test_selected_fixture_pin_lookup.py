"""Selected fixture pins use exact inputs without catalog scans or fallback."""

from __future__ import annotations

import hashlib
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

MCP_TESTS = Path(__file__).resolve().parent
VALIDATE_ATOMS = Path(__file__).resolve().parents[2] / "201_TOOLS" / "VALIDATE_ATOMS"
if str(MCP_TESTS) not in sys.path:
    sys.path.insert(0, str(MCP_TESTS))
if str(VALIDATE_ATOMS) not in sys.path:
    sys.path.insert(0, str(VALIDATE_ATOMS))

import test_selected_routes_mcp as fixture  # noqa: E402
from validate_atoms_workers.parsing import parse_carrier  # noqa: E402
from frozen_selected_workflows import frozen_manifest, frozen_source_bytes  # noqa: E402


class SelectedFixturePinLookupTests(unittest.TestCase):
    def setUp(self) -> None:
        temporary = tempfile.TemporaryDirectory(dir=fixture.TEST_TEMP_ROOT)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def test_exact_selected_sources_keep_identity_revision_and_hash_without_catalog(self) -> None:
        with patch(
            "capability_discovery.service.Service.catalog",
            side_effect=AssertionError("catalog scanned"),
        ):
            manifest = fixture.copy_complete_selected_guard_fixture(self.root)
        self.assertEqual(
            fixture.SELECTED_ROUTE_NAMES, tuple(row["route"] for row in manifest["routes"])
        )
        for route in manifest["routes"]:
            for pin in [
                *fixture.selected_routes._definition_sequence(route),
                *route["native_action_calls"],
            ]:
                raw = frozen_source_bytes(pin["source_path"], pin["digest"])
                metadata = parse_carrier(raw, Path(pin["source_path"])).metadata
                self.assertEqual(metadata["atom_id"], pin["atom_id"])
                self.assertEqual(metadata["version"], pin["version"])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), pin["digest"])
                self.assertEqual(raw, (self.root / pin["source_path"]).read_bytes())

    def test_wrong_source_identity_status_and_version_preserve_existing_fixture(self) -> None:
        manifest = frozen_manifest()
        identity = manifest["routes"][0]["workflow"]["atom_id"]
        fixture.frozen_project(self.root)
        before = {path.relative_to(self.root): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}
        for field, value in (
            ("atom_id", "CA-O-WRONG"),
            ("status", "Inactive"),
            ("version", 0),
            ("version", True),
        ):
            with self.subTest(field=field, value=value):
                metadata = {"atom_id": identity, "status": "Active", "version": 1, field: value}
                with patch(
                    "validate_atoms_workers.parsing.parse_carrier",
                    return_value=types.SimpleNamespace(metadata=metadata),
                ):
                    with self.assertRaises(AssertionError):
                        fixture.copy_complete_selected_guard_fixture(self.root)
                self.assertEqual(before, {path.relative_to(self.root): path.read_bytes()
                                          for path in self.root.rglob("*") if path.is_file()})

    def test_missing_exact_source_is_not_found_through_another_path(self) -> None:
        path = frozen_manifest()["routes"][0]["workflow"]["source_path"]
        original = frozen_source_bytes

        def missing(relative, expected_digest=None):
            if str(relative) == path:
                raise FileNotFoundError("exact fixture source is unavailable")
            return original(relative, expected_digest)

        with patch("frozen_selected_workflows.frozen_source_bytes", missing):
            with self.assertRaises(FileNotFoundError):
                fixture.copy_complete_selected_guard_fixture(self.root)


if __name__ == "__main__":
    unittest.main()
