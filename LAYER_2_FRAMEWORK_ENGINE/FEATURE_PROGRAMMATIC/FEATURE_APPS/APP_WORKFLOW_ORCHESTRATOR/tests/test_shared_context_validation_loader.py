"""Focused tests for loading the frozen direct Method selection."""

from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
for location in (APP, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from shared_context_direct_fixture import DirectSharedContextFixture  # noqa: E402
from shared_context_validation_loader import (  # noqa: E402
    FrozenMethodLoaderError,
    load_frozen_methods,
)


class FrozenMethodLoaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = DirectSharedContextFixture.load()
        self.temporary = tempfile.TemporaryDirectory(
            dir=PROJECT_ROOT / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(self.temporary.cleanup)
        self.root = self.fixture.materialize(Path(self.temporary.name) / "project")
        self.rows = {row["atom_id"]: dict(row) for row in self.fixture.trusted_methods}

    def _frozen(self, *atom_ids: str) -> dict[str, object]:
        rows = [copy.deepcopy(self.rows[atom_id]) for atom_id in atom_ids]
        return {
            "request": {
                "operation": "enqueue_selected",
                "execution": {"parameters": {"base_packet": {"methods": rows}}},
            }
        }

    def test_original_frozen_selection_is_independent_of_provider_subset(self) -> None:
        frozen = self._frozen("CA-M-191", "CA-M-193", "CA-M-431")
        expected = load_frozen_methods(self.root, frozen)
        provider_step = {"methods": [copy.deepcopy(self.rows["CA-M-191"])]}
        provider_step["methods"].append(copy.deepcopy(self.rows["CA-M-431"]))
        self.assertEqual(expected, load_frozen_methods(self.root, frozen))
        self.assertEqual(3, len(expected))

    def test_changed_current_bytes_are_stale(self) -> None:
        frozen = self._frozen("CA-M-431")
        row = self.rows["CA-M-431"]
        target = self.root / str(row["path"])
        target.write_text(target.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        with self.assertRaises(FrozenMethodLoaderError) as raised:
            load_frozen_methods(self.root, frozen)
        self.assertEqual("stale_source", raised.exception.code)

    def test_oversized_current_source_does_not_call_path_read_bytes(self) -> None:
        frozen = self._frozen("CA-M-431")
        row = self.rows["CA-M-431"]
        target = self.root / str(row["path"])
        target.write_bytes(b"x" * (10 * 1024 * 1024))
        original_read_bytes = Path.read_bytes

        def guarded_read_bytes(path: Path) -> bytes:
            if path == target:
                raise AssertionError("source loader must use bounded_bytes")
            return original_read_bytes(path)

        with patch.object(Path, "read_bytes", new=guarded_read_bytes):
            with self.assertRaises(FrozenMethodLoaderError) as raised:
                load_frozen_methods(self.root, frozen)
        self.assertEqual("unresolved_method", raised.exception.code)

    def test_missing_declared_parent_is_explicit(self) -> None:
        with self.assertRaises(FrozenMethodLoaderError) as raised:
            load_frozen_methods(self.root, self._frozen("CA-M-430"))
        self.assertEqual("missing_parent", raised.exception.code)
        self.assertEqual(("CA-M-415",), raised.exception.needed_ids)
        self.assertEqual(["CA-M-415"], raised.exception.warning()["needed_ids"])

    def test_unresolved_declared_parent_is_not_silently_omitted(self) -> None:
        frozen = self._frozen("CA-M-430", "CA-M-415")
        parent = self.rows["CA-M-415"]
        target = self.root / str(parent["path"])
        target.write_text(
            target.read_text(encoding="utf-8").replace("status: Active", "status: Archived", 1),
            encoding="utf-8",
        )
        with self.assertRaises(FrozenMethodLoaderError) as raised:
            load_frozen_methods(self.root, frozen)
        self.assertEqual("unresolved_parent", raised.exception.code)

    def test_authored_parent_of_is_an_explicit_unsupported_condition(self) -> None:
        frozen = self._frozen("CA-M-431")
        row = frozen["request"]["execution"]["parameters"]["base_packet"]["methods"][0]
        assert isinstance(row, dict)
        target = self.root / str(row["path"])
        content = target.read_text(encoding="utf-8").replace(
            "relations:\n", "relations:\n  parent_of:\n    - CA-M-415\n", 1
        )
        target.write_text(content, encoding="utf-8")
        row["content"] = content
        row["sha256"] = hashlib.sha256(content.encode("utf-8")).hexdigest()
        with self.assertRaises(FrozenMethodLoaderError) as raised:
            load_frozen_methods(self.root, frozen)
        self.assertEqual("unsupported_condition", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
