"""Selected fixture pins use exact inputs without catalog scans or fallback."""

from __future__ import annotations

import hashlib
import json
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

import test_selected_routes_mcp as fixture
from validate_atoms_workers.parsing import parse_carrier


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
                source = fixture.ROOT / pin["source_path"]
                raw = source.read_bytes()
                metadata = parse_carrier(raw, source).metadata
                self.assertEqual(metadata["atom_id"], pin["atom_id"])
                self.assertEqual(metadata["version"], pin["version"])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), pin["digest"])
                self.assertEqual(raw, (self.root / pin["source_path"]).read_bytes())

    def test_wrong_source_identity_status_and_version_fail_before_copy(self) -> None:
        manifest = json.loads(
            (fixture.ROOT / fixture.selected_manifest_ref(fixture.ROOT)).read_text()
        )
        identity = manifest["routes"][0]["workflow"]["atom_id"]
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
                self.assertEqual([], list(self.root.iterdir()))

    def test_missing_exact_source_is_not_found_through_another_path(self) -> None:
        manifest = json.loads(
            (fixture.ROOT / fixture.selected_manifest_ref(fixture.ROOT)).read_text()
        )
        source = fixture.ROOT / manifest["routes"][0]["workflow"]["source_path"]
        original = Path.read_bytes

        def missing(path: Path) -> bytes:
            if path == source:
                raise FileNotFoundError("exact fixture source is unavailable")
            return original(path)

        with patch.object(Path, "read_bytes", missing):
            with self.assertRaises(FileNotFoundError):
                fixture.copy_complete_selected_guard_fixture(self.root)
        self.assertEqual([], list(self.root.iterdir()))


if __name__ == "__main__":
    unittest.main()
