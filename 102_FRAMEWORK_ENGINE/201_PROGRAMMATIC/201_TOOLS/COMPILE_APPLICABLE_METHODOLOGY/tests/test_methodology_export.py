from __future__ import annotations

import hashlib
import importlib.util
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOL = Path(__file__).resolve().parents[1] / "methodology_export.py"
SPEC = importlib.util.spec_from_file_location("methodology_export", TOOL)
assert SPEC and SPEC.loader
exporter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = exporter
SPEC.loader.exec_module(exporter)


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def carrier(atom_id: str, *, status: str = "Active", version: int = 1, body: str = "claim") -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        f"status: {status}\n"
        f"version: {version}\n"
        "updated_at: 2026-10-09 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n{body}\n"
    ).encode("utf-8")


class FakeDirEntry:
    def __init__(self, name: str, *, directory: bool = False) -> None:
        self.name = name
        self.directory = directory

    def is_symlink(self) -> bool:
        return False

    def is_dir(self, *, follow_symlinks: bool = True) -> bool:
        return self.directory

    def is_file(self, *, follow_symlinks: bool = True) -> bool:
        return not self.directory


class FakeScandir:
    def __init__(self, entries: list[FakeDirEntry]) -> None:
        self.entries = entries

    def __enter__(self) -> list[FakeDirEntry]:
        return self.entries

    def __exit__(self, *unused: object) -> None:
        return None


class MethodologyExportTest(unittest.TestCase):
    def setUp(self) -> None:
        temporary = Path.cwd() / ".caprmedio_tmp/methodology-export-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.control = self.root / ".control"
        self.source = self.control / "101_CAPRMEDIO_FRAMEWORK/001_METHODOLOGY_SOURCES"
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in exporter.compiler.ROLE_BY_DIRECTORY:
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir(parents=True)
        self.write("001_CORE_META_MODEL/caprmedio_framework_default_settings.toml", b"")
        (self.root / exporter.compiler.SETTINGS_PATH).parent.mkdir(parents=True, exist_ok=True)
        (self.root / exporter.compiler.SETTINGS_PATH).write_text('[paths]\ncontrol_root = ".control"\n', encoding="utf-8")
        (self.control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f"authority_path = {json.dumps(self.source.relative_to(self.root).as_posix())}\n"
            'delivery_path = ".control/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"\n',
            encoding="utf-8",
        )
        self.write_instance(b"")
        self.write("003_PROJECT_CONFIGURATION/catalog/available.json", b'{"schema":"catalog.v1"}\n')
        self.write("003_PROJECT_CONFIGURATION/support/schema.json", b'{"type":"object"}\n')
        self.candidate = self.root / ".caprmedio_tmp/release_candidates/candidate-1"
        self.manifest_path = self.root / "frozen-methodology-manifest.json"

    def write(self, relative: str, data: bytes) -> Path:
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def write_instance(self, data: bytes) -> Path:
        path = self.control / exporter.compiler.INSTANCE_SETTINGS_RELATIVE
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def pin(self, relative: str) -> dict[str, str]:
        return {"path": relative, "sha256": digest((self.source / relative).read_bytes())}

    def supports(self) -> list[dict[str, str]]:
        return [
            self.pin("001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"),
            self.pin("003_PROJECT_CONFIGURATION/catalog/available.json"),
            self.pin("003_PROJECT_CONFIGURATION/support/schema.json"),
        ]

    def freeze(self, selected: list[dict[str, object]]) -> dict[str, object]:
        manifest = exporter.freeze_methodology_manifest(
            source_root=self.source,
            selected_atoms=selected,
            support_inventory=self.supports(),
            catalog_pins=[self.pin("003_PROJECT_CONFIGURATION/catalog/available.json")],
            project_root=self.root,
        )
        self.manifest_path.write_bytes(exporter.frozen_manifest_bytes(manifest))
        return manifest

    def export(self) -> exporter.MethodologyExport:
        return exporter.export_selected_methodology(
            source_root=self.source,
            frozen_manifest_path=self.manifest_path,
            release_candidate_root=self.candidate,
            project_root=self.root,
        )

    def output_files(self) -> dict[str, bytes]:
        root = self.candidate / "methodology"
        return {} if not root.exists() else {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in sorted(root.rglob("*")) if path.is_file()
        }

    def test_exports_only_frozen_selected_active_atoms_and_explicit_support(self) -> None:
        selected = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION/04_requirement/CA-R-002--inactive.md", carrier("CA-R-002", status="Inactive"))
        (self.source / "001_CORE_META_MODEL/.DS_Store").write_bytes(b"finder")
        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])

        result = self.export()
        output = self.output_files()

        self.assertEqual(selected.read_bytes(), output["001_CORE_META_MODEL/04_requirement/CA-R-001--active.md"])
        self.assertNotIn("003_PROJECT_CONFIGURATION/04_requirement/CA-R-002--inactive.md", output)
        self.assertNotIn("001_CORE_META_MODEL/.DS_Store", output)
        self.assertEqual(frozen["sha256"], result.frozen_manifest_sha256)
        self.assertEqual(1, result.atom_count)
        self.assertEqual(3, result.support_count)
        self.assertIn("methodology-export-inventory.json", output)
        self.assertTrue((self.candidate / "methodology-export-seal.json").is_file())
        self.assertFalse((self.candidate / "methodology-export-unsealed.json").exists())
        self.assertEqual(result.inventory, exporter.read_sealed_export(release_candidate_root=self.candidate).inventory)
        self.assertFalse((self.root / "methodology").exists())

    def test_export_requires_a_physical_canonical_frozen_manifest(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()
        self.assertEqual("frozen-manifest-missing", raised.exception.code)
        self.assertEqual({}, self.output_files())

        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.manifest_path.write_text("{}", encoding="utf-8")
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()
        self.assertEqual("frozen-manifest-invalid", raised.exception.code)
        self.assertEqual({}, self.output_files())

    def test_complete_active_frontier_is_bound_and_source_change_rejects_before_effect(self) -> None:
        source = self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        source.write_bytes(carrier("CA-R-001", body="changed"))

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()

        self.assertEqual("frozen-frontier-stale", raised.exception.code)
        self.assertTrue(frozen["active_frontier"])
        self.assertEqual({}, self.output_files())

    def test_configured_extension_revision_is_frozen_and_unselected_revision_is_excluded(self) -> None:
        self.write_instance(b'[extensions.demo]\nenabled = true\nrevision = "v2"\n')
        self.write("002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/CA-R-010--v1.md", carrier("CA-R-010"))
        v2 = self.write("002_INSTALLED_EXTENSIONS/demo/v2/04_requirement/CA-R-010--v2.md", carrier("CA-R-010", version=2))
        self.freeze([{"atom_id": "CA-R-010", "version": 2}])

        self.export()

        self.assertEqual(v2.read_bytes(), self.output_files()["002_INSTALLED_EXTENSIONS/demo/v2/04_requirement/CA-R-010--v2.md"])
        self.assertNotIn("002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/CA-R-010--v1.md", self.output_files())

    def test_unavailable_configured_extension_revision_refuses_before_freeze_or_export(self) -> None:
        self.write_instance(b'[extensions.demo]\nenabled = true\nrevision = "v2"\n')
        self.write("002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/CA-R-010--v1.md", carrier("CA-R-010"))

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.freeze([{"atom_id": "CA-R-010", "version": 1}])

        self.assertEqual("activated-extension-revision-missing", raised.exception.code)
        self.assertEqual({}, self.output_files())

    def test_project_binding_reopens_canonical_instance_and_refuses_wrong_root(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.assertEqual(
            frozen["project_binding"],
            exporter.reopen_project_export_binding(self.root, self.source),
        )
        self.write_instance(b"[instance]\nchanged = true\n")

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()
        self.assertEqual("frozen-manifest-project-binding-stale", raised.exception.code)

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter.freeze_methodology_manifest(
                source_root=self.source,
                selected_atoms=[{"atom_id": "CA-R-001", "version": 1}],
                support_inventory=self.supports(),
                catalog_pins=[self.pin("003_PROJECT_CONFIGURATION/catalog/available.json")],
                project_root=self.root / "wrong-project",
            )
        self.assertEqual("project-root-invalid", raised.exception.code)

    def test_project_binding_refuses_control_root_drift(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        replacement_control = self.root / ".replacement-control"
        replacement_control.mkdir()
        (replacement_control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f"authority_path = {json.dumps(self.source.relative_to(self.root).as_posix())}\n"
            'delivery_path = ".replacement-control/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"\n',
            encoding="utf-8",
        )
        (self.root / exporter.compiler.SETTINGS_PATH).write_text(
            '[paths]\ncontrol_root = ".replacement-control"\n', encoding="utf-8"
        )

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()

        self.assertEqual("frozen-manifest-project-binding-stale", raised.exception.code)

    def test_detached_export_refuses_extension_or_project_configuration_atoms(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.write("003_PROJECT_CONFIGURATION/04_requirement/CA-R-002--project.md", carrier("CA-R-002"))

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter.freeze_methodology_manifest(
                source_root=self.source,
                selected_atoms=[{"atom_id": "CA-R-001", "version": 1}],
                support_inventory=self.supports(),
                catalog_pins=[self.pin("003_PROJECT_CONFIGURATION/catalog/available.json")],
            )

        self.assertEqual("project-binding-required", raised.exception.code)

    def test_legacy_frozen_manifest_cannot_create_a_fresh_candidate(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        legacy = dict(frozen)
        legacy.pop("project_binding")
        legacy["schema"] = exporter.LEGACY_FROZEN_SCHEMA
        legacy["sha256"] = exporter._checksum(legacy)
        self.manifest_path.write_bytes(exporter.frozen_manifest_bytes(legacy))

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter.export_selected_methodology(
                source_root=self.source,
                frozen_manifest_path=self.manifest_path,
                release_candidate_root=self.candidate,
            )

        self.assertEqual("frozen-manifest-legacy-read-only", raised.exception.code)
        self.assertFalse(self.candidate.exists())

    def test_historical_sealed_v1_export_remains_readable(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.export()
        inventory_path = self.candidate / "methodology" / exporter.INVENTORY_NAME
        inventory = json.loads(inventory_path.read_text(encoding="utf-8"))
        legacy = dict(inventory["frozen_manifest"])
        legacy.pop("project_binding")
        legacy["schema"] = exporter.LEGACY_FROZEN_SCHEMA
        legacy["sha256"] = exporter._checksum(legacy)
        inventory["frozen_manifest"] = legacy
        inventory["frozen_manifest_sha256"] = legacy["sha256"]
        unsigned = dict(inventory)
        unsigned.pop("inventory_sha256")
        inventory["inventory_sha256"] = exporter._digest(exporter._json(unsigned))
        inventory_path.write_bytes(exporter._json(inventory) + b"\n")
        seal_path = self.candidate / exporter.SEAL_NAME
        seal = json.loads(seal_path.read_text(encoding="utf-8"))
        seal["frozen_manifest_sha256"] = legacy["sha256"]
        seal["inventory_sha256"] = inventory["inventory_sha256"]
        seal["output_tree_sha256"] = exporter._tree(self.candidate / "methodology")
        seal["sha256"] = exporter._checksum(seal)
        seal_path.write_bytes(exporter._json(seal) + b"\n")

        retained = exporter.read_sealed_export(release_candidate_root=self.candidate)

        self.assertEqual(legacy["sha256"], retained.frozen_manifest_sha256)

    def test_stale_catalog_and_unsafe_support_refuse_before_effect(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        (self.source / "003_PROJECT_CONFIGURATION/catalog/available.json").write_bytes(b'{"schema":"catalog.v2"}\n')
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()
        self.assertEqual("frozen-frontier-stale", raised.exception.code)
        self.assertEqual({}, self.output_files())

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter.freeze_methodology_manifest(
                source_root=self.source,
                selected_atoms=[{"atom_id": "CA-R-001", "version": 1}],
                support_inventory=[{"path": "../outside", "sha256": "0" * 64}],
                catalog_pins=[],
            )
        self.assertEqual("export-path-unsafe", raised.exception.code)

    def test_writer_lock_refuses_concurrent_writer_and_reader(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.candidate.mkdir(parents=True)
        (self.candidate / ".methodology-export.lock").write_text("other writer", encoding="utf-8")

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()
        self.assertEqual("export-run-locked", raised.exception.code)
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter.read_sealed_export(release_candidate_root=self.candidate)
        self.assertEqual("export-run-locked", raised.exception.code)
        self.assertEqual({}, self.output_files())

    def test_fault_leaves_explicit_unsealed_state_and_rejected_partial_cannot_resume(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        with patch.object(exporter, "_replace", side_effect=exporter.MethodologyExportError("injected", "fault")):
            with self.assertRaises(exporter.MethodologyExportError) as raised:
                self.export()
        self.assertEqual("injected", raised.exception.code)
        self.assertTrue((self.candidate / "methodology-export-unsealed.json").is_file())
        self.assertFalse((self.candidate / "methodology-export-seal.json").exists())
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            exporter.read_sealed_export(release_candidate_root=self.candidate)
        self.assertEqual("export-unsealed", raised.exception.code)
        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()
        self.assertEqual("export-unsealed", raised.exception.code)

    def test_same_run_refuses_different_sealed_manifest(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        first = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.export()
        self.write("003_PROJECT_CONFIGURATION/04_requirement/CA-R-002--active.md", carrier("CA-R-002"))
        second = self.freeze([{"atom_id": "CA-R-001", "version": 1}, {"atom_id": "CA-R-002", "version": 1}])

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()

        self.assertEqual("export-run-already-sealed", raised.exception.code)
        self.assertNotEqual(first["sha256"], second["sha256"])
        self.assertEqual(1, exporter.read_sealed_export(release_candidate_root=self.candidate).atom_count)

    def test_protected_env_metadata_refuses_before_payload_or_compiler_discovery(self) -> None:
        for name, directory in ((".env", False), (".env.local", False), ("config.env", False), (".env-private", True)):
            with self.subTest(name=name, directory=directory), \
                    patch.object(exporter.os, "scandir", return_value=FakeScandir([FakeDirEntry(name, directory=directory)])), \
                    patch.object(exporter.compiler, "discover_candidates") as discover, \
                    patch.object(Path, "read_bytes", autospec=True) as read_bytes:
                with self.assertRaises(exporter.MethodologyExportError) as raised:
                    exporter.freeze_methodology_manifest(
                        source_root=self.source,
                        selected_atoms=[{"atom_id": "CA-R-001", "version": 1}],
                        support_inventory=[],
                        catalog_pins=[],
                    )
                self.assertEqual("protected-source-path", raised.exception.code)
                discover.assert_not_called()
                read_bytes.assert_not_called()
        self.assertEqual({}, self.output_files())

    def test_protected_env_descendant_and_ancestor_refuse_using_metadata_only(self) -> None:
        nested = self.source / "safe-directory"

        def scandir(path: Path | str) -> FakeScandir:
            return FakeScandir(
                [FakeDirEntry("safe-directory", directory=True)]
                if Path(path) == self.source else [FakeDirEntry("config.env")]
            )

        with patch.object(exporter.os, "scandir", side_effect=scandir), \
                patch.object(exporter.compiler, "discover_candidates") as discover, \
                patch.object(Path, "read_bytes", autospec=True) as read_bytes:
            with self.assertRaises(exporter.MethodologyExportError) as raised:
                exporter.freeze_methodology_manifest(
                    source_root=self.source,
                    selected_atoms=[{"atom_id": "CA-R-001", "version": 1}],
                    support_inventory=[],
                    catalog_pins=[],
                )
            self.assertEqual("protected-source-path", raised.exception.code)
            discover.assert_not_called()
            read_bytes.assert_not_called()

        with patch.object(Path, "read_bytes", autospec=True) as read_bytes:
            with self.assertRaises(exporter.MethodologyExportError) as raised:
                exporter._guard_source_metadata(Path("/private/tmp/.env-ancestor/methodology-sources"))
            self.assertEqual("protected-source-path", raised.exception.code)
            read_bytes.assert_not_called()
        self.assertFalse(nested.exists())
        self.assertEqual({}, self.output_files())


if __name__ == "__main__":
    unittest.main()
