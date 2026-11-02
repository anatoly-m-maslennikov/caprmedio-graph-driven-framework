"""Focused coverage for the finite graph-authority refresh closure."""

from __future__ import annotations

from copy import deepcopy
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
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402

from validate_atoms_workers.graph_authority_refresh import (  # noqa: E402
    APPROVED_GRAPH_AUTHORITY_IDS,
    _active_source,
    _source_roots,
    refresh_entries,
    verify_entries,
)


class GraphAuthorityRefreshTests(unittest.TestCase):
    @staticmethod
    def _project(root: Path, rows: tuple[dict[str, str], ...]) -> dict[str, dict[str, object]]:
        control = root / ".caprmedio_example"
        control.mkdir(parents=True, exist_ok=True)
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "example"\n[paths]\ncontrol_root = ".caprmedio_example"\n'
        )
        return write_scope_unit_declarations(root, rows, control_root=control)

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

    def test_core_only_project_does_not_require_optional_configuration_owner(self) -> None:
        temporary = PROJECT / ".caprmedio_tmp" / "tests" / "graph_authority_refresh"
        temporary.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary) as directory:
            root = Path(directory)
            declared = self._project(root, (
                {"scope_unit_name": "CORE_META_MODEL", "scope_unit_label": "Layer"},
            ))
            owner = Path(declared["CORE_META_MODEL"]["authority_path"])
            for role in ("04_requirement", "07_delivery"):
                (owner / role).mkdir(parents=True)
            selection = resolve_project(root)
            with bind_selection(selection):
                self.assertEqual(
                    _source_roots(root),
                    (owner / "04_requirement", owner / "07_delivery"),
                )

    def test_relocated_declared_owner_and_foreign_selection(self) -> None:
        temporary = PROJECT / ".caprmedio_tmp" / "tests" / "graph_authority_refresh"
        temporary.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=temporary) as directory:
            root = Path(directory)
            declared = self._project(root, (
                {"scope_unit_name": "CORE_META_MODEL", "scope_unit_label": "Layer"},
                {"scope_unit_name": "PROJECT_CONFIGURATION", "scope_unit_label": "Layer"},
            ))
            owners = {name: Path(declared[name]["authority_path"])
                      for name in ("CORE_META_MODEL", "PROJECT_CONFIGURATION")}
            for owner in owners.values():
                for role in ("04_requirement", "07_delivery"):
                    (owner / role).mkdir(parents=True)
            selection = resolve_project(root)
            with bind_selection(selection):
                self.assertEqual(_source_roots(root),
                                 tuple(
                                     owner / role
                                     for owner in owners.values()
                                     for role in ("04_requirement", "07_delivery")
                                 ))
                with self.assertRaisesRegex(ValueError, "another root"):
                    _source_roots(PROJECT)

    def test_declared_project_configuration_fixture_is_selected(self) -> None:
        temporary = PROJECT / ".caprmedio_tmp" / "tests" / "graph_authority_refresh"
        temporary.mkdir(parents=True, exist_ok=True)
        fixture = TESTS / "fixtures" / "graph_authority" / "CA-D-305-project-configuration.md"
        with tempfile.TemporaryDirectory(dir=temporary) as directory:
            root = Path(directory)
            declared = self._project(root, (
                {"scope_unit_name": "CORE_META_MODEL", "scope_unit_label": "Layer"},
                {"scope_unit_name": "PROJECT_CONFIGURATION", "scope_unit_label": "Layer"},
            ))
            owners = {name: Path(declared[name]["authority_path"])
                      for name in ("CORE_META_MODEL", "PROJECT_CONFIGURATION")}
            for role in ("04_requirement", "07_delivery"):
                (owners["CORE_META_MODEL"] / role).mkdir(parents=True)
            (owners["PROJECT_CONFIGURATION"] / "07_delivery").mkdir(parents=True)
            source = owners["PROJECT_CONFIGURATION"] / "07_delivery" / (
                "CA-D-305-PROJECT_CONFIGURATION-CORE--carry-projected-atoms-without-new-identity.md"
            )
            source.write_bytes(fixture.read_bytes())
            selection = resolve_project(root)
            with bind_selection(selection):
                selected, metadata = _active_source(root, "CA-D-305")
            self.assertEqual(source, selected)
            self.assertEqual(16, metadata["version"])
            self.assertFalse((owners["PROJECT_CONFIGURATION"] / "04_requirement").exists())
            (owners["PROJECT_CONFIGURATION"] / "04_requirement").symlink_to(
                owners["CORE_META_MODEL"] / "04_requirement", target_is_directory=True
            )
            with self.assertRaisesRegex(ValueError, "Scope Unit Declaration source discovery is unavailable or unsafe"):
                _source_roots(root)

    def test_stale_pin_is_refused(self) -> None:
        root = Path("synthetic-project").resolve()
        entries = self._entries()
        with (
            patch(
                "validate_atoms_workers.graph_authority_refresh._active_source",
                side_effect=lambda _root, atom_id: (
                    root / "source" / f"{atom_id}.md", {"version": 2}
                ),
            ),
            patch.object(Path, "read_bytes", return_value=b"synthetic source"),
        ):
            entries = refresh_entries(root, entries)
            entries["CA-D-268"]["sha256"] = "0" * 64

            with self.assertRaisesRegex(ValueError, "graph authority source is stale: CA-D-268"):
                verify_entries(root, entries)

    def test_refresh_preserves_input_and_unapproved_entries(self) -> None:
        root = Path("synthetic-project").resolve()
        entries = {**self._entries(), "unapproved": {"sentinel": ["unchanged"]}}
        before = deepcopy(entries)
        with (
            patch(
                "validate_atoms_workers.graph_authority_refresh._active_source",
                return_value=(root / "source.md", {"version": 2}),
            ) as lookup,
            patch.object(Path, "read_bytes", return_value=b"synthetic source"),
        ):
            refreshed = refresh_entries(root, entries)
        self.assertEqual(before, entries)
        self.assertEqual(before.keys(), refreshed.keys())
        self.assertEqual(before["unapproved"], refreshed["unapproved"])
        self.assertEqual(
            APPROVED_GRAPH_AUTHORITY_IDS, {call.args[1] for call in lookup.call_args_list}
        )
        self.assertEqual(2, refreshed["CA-D-268"]["version"])

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
