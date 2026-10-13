"""Focused coverage for the finite graph-authority refresh closure."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock, patch


TESTS = Path(__file__).resolve().parent
TOOL = TESTS.parent
PROJECT = TOOL.parents[3]
sys.path.insert(0, str(TOOL))
sys.path.insert(0, str(TOOL.parent))

from project_selection import bind_selection, resolve_project  # noqa: E402

from validate_atoms_workers.graph_authority_refresh import (  # noqa: E402
    APPROVED_GRAPH_AUTHORITY_IDS,
    _source_roots,
    refresh_entries,
    verify_entries,
)


GRAPH_AUTHORITY = TOOL / "validate_atoms_workers" / "graph_authority.json"


class GraphAuthorityRefreshTests(unittest.TestCase):
    @staticmethod
    def _entries() -> dict[str, object]:
        return {
            atom_id: {
                "version": 1,
                "sha256": "0" * 64,
                "source_path": "stale/" + atom_id + ".md",
            }
            for atom_id in APPROVED_GRAPH_AUTHORITY_IDS
        }

    def test_authority_roots_are_the_finite_authored_source_roots(self) -> None:
        selection = resolve_project(PROJECT)
        owner = next(row["authority_path"] for row in selection.structure["scope_units"]
                     if row["scope_unit_name"] == "CORE_META_MODEL")
        self.assertEqual(
            _source_roots(PROJECT),
            (PROJECT / owner / "04_requirement", PROJECT / owner / "07_delivery"),
        )

    def test_relocated_declared_owner_and_foreign_selection(self) -> None:
        temporary = PROJECT / ".caprmedio_tmp" / "tests" / "graph_authority_refresh"
        temporary.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary) as directory:
            root = Path(directory)
            control = root / ".caprmedio_example"
            owner = control / "declared_core"
            for role in ("04_requirement", "07_delivery"):
                (owner / role).mkdir(parents=True)
            (control / "caprmedio_project_settings.toml").write_text(
                '[project]\nname = "example"\n[paths]\ncontrol_root = ".caprmedio_example"\n'
            )
            structure = control / "project_structure.toml"
            declaration = (
                '[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\n'
                'authority_path = ".caprmedio_example/declared_core"\n'
                'delivery_path = ".caprmedio_example/declared_core"\n'
            )
            structure.write_text("schema_version = 1\n" + declaration)
            selection = resolve_project(root)
            with bind_selection(selection):
                self.assertEqual(_source_roots(root),
                                 (owner / "04_requirement", owner / "07_delivery"))
                with self.assertRaisesRegex(ValueError, "another root"):
                    _source_roots(PROJECT)
            structure.write_text("schema_version = 1\n")
            with self.assertRaisesRegex(ValueError, "owner is absent or ambiguous"):
                _source_roots(root)
            structure.write_text("schema_version = 1\n" + declaration * 2)
            with self.assertRaisesRegex(ValueError, "unique"):
                _source_roots(root)

    def test_shared_graph_and_registry_pins_are_the_same_canonical_tuples(self) -> None:
        graph_entries = json.loads(GRAPH_AUTHORITY.read_text(encoding="utf-8"))["sources"]
        registry_entries = json.loads(
            (TOOL / "validate_atoms_workers/registry.json").read_text(encoding="utf-8")
        )["sources"]
        for atom_id in ("CA-D-268", "CA-D-269", "CA-D-305", "CA-D-471", "CA-D-481", "CA-R-1539"):
            with self.subTest(atom_id=atom_id):
                self.assertEqual(
                    tuple(graph_entries[atom_id][field] for field in ("version", "sha256", "source_path")),
                    tuple(registry_entries[atom_id][field] for field in ("version", "sha256", "source_path")),
                )

    def test_committed_authority_is_the_exact_current_finite_closure(self) -> None:
        entries = json.loads(GRAPH_AUTHORITY.read_text(encoding="utf-8"))["sources"]
        before = copy.deepcopy(entries)

        self.assertEqual(refresh_entries(PROJECT, entries), entries)
        verify_entries(PROJECT, entries)
        self.assertEqual(
            {key: entries[key] for key in entries if key not in APPROVED_GRAPH_AUTHORITY_IDS},
            {key: before[key] for key in before if key not in APPROVED_GRAPH_AUTHORITY_IDS},
        )

    def test_stale_pin_is_refused(self) -> None:
        entries = json.loads(GRAPH_AUTHORITY.read_text(encoding="utf-8"))["sources"]
        entries = refresh_entries(PROJECT, entries)
        entries["CA-D-268"]["sha256"] = "0" * 64

        with self.assertRaisesRegex(ValueError, "graph authority source is stale: CA-D-268"):
            verify_entries(PROJECT, entries)

    def test_missing_active_source_is_refused(self) -> None:
        with patch(
            "validate_atoms_workers.graph_authority_refresh._source_roots", return_value=()
        ):
            with self.assertRaisesRegex(ValueError, "active source is absent: CA-D-268"):
                refresh_entries(PROJECT, self._entries())

    def test_ambiguous_active_source_is_refused(self) -> None:
        source_root = Mock()
        source_root.glob.return_value = [Path("first.md"), Path("second.md")]
        parsed = SimpleNamespace(
            metadata={"atom_id": "CA-D-268", "status": "Active", "version": 1}
        )
        with (
            patch(
                "validate_atoms_workers.graph_authority_refresh._source_roots",
                return_value=(source_root,),
            ),
            patch(
                "validate_atoms_workers.graph_authority_refresh.parse_carrier", return_value=parsed
            ),
            patch.object(Path, "is_symlink", return_value=False),
            patch.object(Path, "is_file", return_value=True),
            patch.object(Path, "read_bytes", return_value=b"fixture"),
        ):
            with self.assertRaisesRegex(ValueError, "active source is ambiguous: CA-D-268"):
                refresh_entries(PROJECT, self._entries())

    def test_projected_active_carrier_in_authoring_root_is_refused(self) -> None:
        source_root = Mock()
        source_root.glob.return_value = [Path("projected.md")]
        parsed = SimpleNamespace(metadata={
            "atom_id": "CA-D-268", "status": "Active", "version": 1,
            "projection": {"source_carrier_path": "original.md"},
        })
        with (
            patch("validate_atoms_workers.graph_authority_refresh._source_roots", return_value=(source_root,)),
            patch("validate_atoms_workers.graph_authority_refresh.parse_carrier", return_value=parsed),
            patch.object(Path, "is_symlink", return_value=False),
            patch.object(Path, "is_file", return_value=True),
            patch.object(Path, "read_bytes", return_value=b"fixture"),
        ):
            with self.assertRaisesRegex(ValueError, "graph authority source is projected: CA-D-268"):
                refresh_entries(PROJECT, self._entries())


if __name__ == "__main__":
    unittest.main()
