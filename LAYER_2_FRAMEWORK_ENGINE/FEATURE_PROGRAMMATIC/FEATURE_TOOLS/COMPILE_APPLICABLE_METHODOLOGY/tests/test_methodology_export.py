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


def carrier(atom_id: str, *, status: str = "Active", version: int = 1, content_role: str | None = None, body: str = "claim") -> bytes:
    lines = (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
    )
    if content_role is not None:
        lines += f"content_role: {content_role}\n"
    lines += (
        f"status: {status}\n"
        f"version: {version}\n"
        "updated_at: 2026-10-09 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n{body}\n"
    )
    return lines.encode("utf-8")


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
        from scope_declaration_test_support import write_scope_unit_declarations

        temporary = Path.cwd() / ".caprmedio_tmp/methodology-export-tests"
        temporary.mkdir(parents=True, exist_ok=True)
        self.root = Path(tempfile.mkdtemp(prefix="case-", dir=temporary))
        self.addCleanup(shutil.rmtree, self.root, True)
        self.control = self.root / ".caprmedio_caprmedio"
        settings = self.control / "caprmedio_project_settings.toml"
        settings.parent.mkdir(parents=True, exist_ok=True)
        settings.write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        self.declarations = write_scope_unit_declarations(
            self.root,
            (
                {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "PROJECT", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "CORE_META_MODEL", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "INSTALLED_EXTENSIONS", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "PROJECT_CONFIGURATION", "parent": "METHODOLOGY_SOURCES", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "FRAMEWORK_ENGINE", "parent": "PROJECT", "scope_unit_type": "Unordered"},
                {"scope_unit_name": "PROJECT_TOOLS", "parent": "PROJECT", "scope_unit_type": "Unordered"},
            ),
        )
        self.source = Path(self.declarations["METHODOLOGY_SOURCES"]["authority_path"])
        self.layers = {
            name: Path(self.declarations[name]["authority_path"])
            for name, _, _ in exporter.compiler.LAYERS
        }
        self.logical_layers = dict(zip(
            ("001_CORE_META_MODEL", "002_INSTALLED_EXTENSIONS", "003_PROJECT_CONFIGURATION"),
            ("CORE_META_MODEL", "INSTALLED_EXTENSIONS", "PROJECT_CONFIGURATION"),
            strict=True,
        ))
        self.logical_layers.update({name: name for name, _, _ in exporter.compiler.LAYERS})
        self.engine_source = Path(self.declarations["FRAMEWORK_ENGINE"]["authority_path"])
        self.engine_delivery = Path(self.declarations["FRAMEWORK_ENGINE"]["delivery_path"])
        self.project_tools_source = Path(self.declarations["PROJECT_TOOLS"]["authority_path"])
        self.project_tools_delivery = Path(self.declarations["PROJECT_TOOLS"]["delivery_path"])
        self.engine_source.mkdir(parents=True, exist_ok=True)
        for layer in ("CORE_META_MODEL", "PROJECT_CONFIGURATION"):
            for role in exporter.compiler.ROLE_BY_DIRECTORY:
                (self.layers[layer] / role).mkdir(parents=True, exist_ok=True)
        self.layers["INSTALLED_EXTENSIONS"].mkdir(parents=True)
        self.write("CORE_META_MODEL/caprmedio_framework_default_settings.toml", b"")
        self.write_instance(b"")
        self.write("PROJECT_CONFIGURATION/catalog/available.json", b'{"schema":"catalog.v1"}\n')
        self.write("PROJECT_CONFIGURATION/support/schema.json", b'{"type":"object"}\n')
        self.candidate = self.root / ".caprmedio_tmp/release_candidates/candidate-1"
        self.manifest_path = self.root / "frozen-methodology-manifest.json"

    def write(self, relative: str, data: bytes) -> Path:
        path = self.source_path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def source_relative(self, relative: str) -> str:
        path = Path(relative)
        layer = self.logical_layers.get(path.parts[0]) if path.parts else None
        if layer is None:
            return path.as_posix()
        return (self.layers[layer].relative_to(self.source) / Path(*path.parts[1:])).as_posix()

    def source_path(self, relative: str) -> Path:
        return self.source / self.source_relative(relative)

    def write_instance(self, data: bytes) -> Path:
        path = self.control / exporter.compiler.INSTANCE_SETTINGS_RELATIVE
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def write_engine_delivery(self, relative: str, data: bytes) -> Path:
        path = self.engine_source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def write_control_delivery(self, relative: str, data: bytes) -> Path:
        path = self.control / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        return path

    def engine_entrypoint(self, relative: str) -> str:
        return (self.engine_delivery / relative).relative_to(self.root).as_posix()

    def pin(self, relative: str) -> dict[str, str]:
        path = self.source_relative(relative)
        return {"path": path, "sha256": digest((self.source / path).read_bytes())}

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
        self.source_path("001_CORE_META_MODEL/.DS_Store").write_bytes(b"finder")
        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])

        result = self.export()
        output = self.output_files()

        self.assertEqual(selected.read_bytes(), output[self.source_relative("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md")])
        self.assertNotIn(self.source_relative("003_PROJECT_CONFIGURATION/04_requirement/CA-R-002--inactive.md"), output)
        self.assertNotIn(self.source_relative("001_CORE_META_MODEL/.DS_Store"), output)
        self.assertEqual(frozen["sha256"], result.frozen_manifest_sha256)
        self.assertEqual(1, result.atom_count)
        self.assertEqual(3, result.support_count)
        self.assertIn("methodology-export-inventory.json", output)
        self.assertTrue((self.candidate / "methodology-export-seal.json").is_file())
        self.assertFalse((self.candidate / "methodology-export-unsealed.json").exists())
        self.assertEqual(result.inventory, exporter.read_sealed_export(release_candidate_root=self.candidate).inventory)
        self.assertFalse((self.root / "methodology").exists())

    def test_nested_source_and_delivery_binding_keep_exact_bytes_through_sealed_export(self) -> None:
        nested = (
            b"---\nidentity:\n  atom_id: CA-R-001\ncontext:\n  role: Requirement\n  form: Rule\n"
            b"state:\n  status: Active\n  version: 1\nrelations: {}\n---\n# Claim\n\nNested source.\n"
        )
        selected_path = "001_CORE_META_MODEL/04_requirement/CA-R-001--nested.md"
        selected = self.write(selected_path, nested)
        entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/DEMO_TOOL/demo_tool.py")
        member = self.root / entrypoint
        member.parent.mkdir(parents=True, exist_ok=True)
        member.write_bytes(b"VALUE = 1\n")
        binding_bytes = (
            "---\nidentity:\n  atom_id: CA-D-001\ncontext:\n  role: Delivery\n  form: Tool\n"
            "state:\n  status: Active\n  version: 3\nrelations: {}\n---\n"
            f'## Binding\n\n```toml\n[tool_binding]\nentrypoint = "{entrypoint}"\n```\n'
        ).encode()
        binding_source = self.write_engine_delivery("07_delivery/CA-D-001--nested.md", binding_bytes)
        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.assertEqual(["CA-D-001"], [row["atom_id"] for row in frozen["binding_atoms"]])
        result = self.export()
        self.assertEqual(nested, self.output_files()[self.source_relative(selected_path)])
        binding = frozen["binding_atoms"][0]
        projected = result.output_root / result.inventory["bindings"][0]["destination_path"]
        exporter.validate_binding_projection_source_preservation(
            binding_bytes, projected.read_bytes(), exporter.BindingAtom(**binding),
        )
        self.assertEqual(nested, selected.read_bytes())
        self.assertEqual(binding_bytes, binding_source.read_bytes())
        self.assertEqual(result.inventory, exporter.read_sealed_export(release_candidate_root=self.candidate).inventory)

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

    def test_frozen_binding_frontier_discovers_two_active_deliveries_outside_methodology_and_projects_them(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        first_entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/DEMO_TOOL/demo_tool.py")
        second_entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/OTHER_TOOL/other_tool.py")
        for entrypoint, contents in ((first_entrypoint, b"def main():\n    return None\n"), (second_entrypoint, b"VALUE = 2\n")):
            engine_member = self.root / entrypoint
            engine_member.parent.mkdir(parents=True, exist_ok=True)
            engine_member.write_bytes(contents)
        first_source = self.write_engine_delivery(
            "CA-SU-16_FEATURE_TOOLS/DEMO_TOOL/07_delivery/CA-D-001--tool.md",
            carrier(
                "CA-D-001",
                content_role="Delivery",
                body=(
                    "binding\n\n```toml\n[tool_binding]\n"
                    'name = "DEMO_TOOL"\n'
                    f'entrypoint = "{first_entrypoint}"\n'
                    "```\n"
                ),
            ),
        )
        second_source = self.write_control_delivery(
            "003_PROJECT_CONFIGURATION/CA-SU-16_FEATURE_TOOLS/OTHER_TOOL/CA-D-002--tool.md",
            carrier(
                "CA-D-002",
                content_role="Delivery",
                body=f"binding\n\n```toml\n[tool_binding]\nentrypoint = \"{second_entrypoint}\"\n```\n",
            ),
        )
        self.write_engine_delivery(
            "CA-SU-16_FEATURE_TOOLS/OTHER_TOOL/archive/CA-D-999--ignored.md",
            carrier("CA-D-999", content_role="Delivery", body=f"```toml\n[tool_binding]\nentrypoint = \"{first_entrypoint}\"\n```\n"),
        )

        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        result = self.export()

        expected_first = first_source.relative_to(self.root).as_posix()
        expected_second = second_source.relative_to(self.root).as_posix()
        expected_bindings = sorted(
            [
                {"atom_id": "CA-D-001", "source_path": expected_first, "version": 1, "sha256": digest(first_source.read_bytes())},
                {"atom_id": "CA-D-002", "source_path": expected_second, "version": 1, "sha256": digest(second_source.read_bytes())},
            ],
            key=lambda item: str(item["source_path"]),
        )
        self.assertEqual(
            expected_bindings,
            frozen["binding_atoms"],
        )
        row = next(item for item in result.inventory["bindings"] if item["source_path"] == expected_first)
        self.assertEqual(f"bindings/{expected_first}", row["destination_path"])
        projected = result.output_root / row["destination_path"]
        binding = exporter.BindingAtom(expected_first, "CA-D-001", 1, digest(first_source.read_bytes()))
        exporter.validate_binding_projection_source_preservation(first_source.read_bytes(), projected.read_bytes(), binding)
        self.assertEqual(result.inventory, exporter.read_sealed_export(release_candidate_root=self.candidate).inventory)

    def test_mixed_framework_and_registered_project_tools_exports_only_framework_binding(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        project_authority = self.project_tools_source
        project_authority.mkdir(parents=True)
        engine_entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/DEMO_TOOL/demo_tool.py")
        project_entrypoint = (self.project_tools_delivery / "PUBLIC_RELEASE/public_release.py").relative_to(self.root).as_posix()
        for entrypoint in (engine_entrypoint, project_entrypoint):
            member = self.root / entrypoint
            member.parent.mkdir(parents=True, exist_ok=True)
            member.write_bytes(b"VALUE = 1\n")
        engine_source = self.write_engine_delivery("CA-SU-16_FEATURE_TOOLS/07_delivery/CA-D-001--tool.md",
            carrier("CA-D-001", content_role="Delivery", body=f'```toml\n[tool_binding]\nentrypoint = "{engine_entrypoint}"\n```\n'))
        self.write_control_delivery(
            (project_authority.relative_to(self.control) / "07_delivery/CA-D-002--project-tool.md").as_posix(),
            carrier("CA-D-002", content_role="Delivery", body=f'```toml\n[tool_binding]\nentrypoint = "{project_entrypoint}"\n```\n'))

        frozen = self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        result = self.export()

        self.assertEqual(["CA-D-001"], [row["atom_id"] for row in frozen["binding_atoms"]])
        self.assertEqual([engine_source.relative_to(self.root).as_posix()],
                         [row["source_path"] for row in result.inventory["bindings"]])
        self.assertEqual(result.inventory, exporter.read_sealed_export(release_candidate_root=self.candidate).inventory)

    def test_unregistered_project_tools_entrypoint_remains_invalid_framework_binding(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.write_engine_delivery("CA-SU-16_FEATURE_TOOLS/07_delivery/CA-D-001--tool.md",
            carrier("CA-D-001", content_role="Delivery", body='```toml\n[tool_binding]\nentrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/unknown.py"\n```\n'))

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.freeze([{"atom_id": "CA-R-001", "version": 1}])

        self.assertEqual("binding-entrypoint-invalid", raised.exception.code)

    def test_frozen_binding_frontier_refuses_framework_engine_inventory_drift_before_export(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/DRIFT_TOOL/drift_tool.py")
        engine_member = self.root / entrypoint
        engine_member.parent.mkdir(parents=True)
        engine_member.write_bytes(b"VALUE = 1\n")
        self.write_engine_delivery(
            "CA-SU-16_FEATURE_TOOLS/DRIFT_TOOL/07_delivery/CA-D-002--tool.md",
            carrier(
                "CA-D-002",
                content_role="Delivery",
                body=f"binding\n\n```toml\n[tool_binding]\nentrypoint = \"{entrypoint}\"\n```\n",
            ),
        )
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        engine_member.write_bytes(b"VALUE = 2\n")

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()

        self.assertEqual("framework-engine-inventory-stale", raised.exception.code)
        self.assertEqual({}, self.output_files())

    def test_frozen_binding_frontier_refuses_an_added_active_control_binding_before_export(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        first_entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIRST_TOOL/first.py")
        second_entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/SECOND_TOOL/second.py")
        for entrypoint in (first_entrypoint, second_entrypoint):
            member = self.root / entrypoint
            member.parent.mkdir(parents=True, exist_ok=True)
            member.write_bytes(b"VALUE = 1\n")
        self.write_engine_delivery(
            "CA-SU-16_FEATURE_TOOLS/FIRST_TOOL/07_delivery/CA-D-010--first.md",
            carrier("CA-D-010", content_role="Delivery", body=f"```toml\n[tool_binding]\nentrypoint = \"{first_entrypoint}\"\n```\n"),
        )
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        self.write_engine_delivery(
            "CA-SU-16_FEATURE_TOOLS/SECOND_TOOL/07_delivery/CA-D-011--second.md",
            carrier("CA-D-011", content_role="Delivery", body=f"```toml\n[tool_binding]\nentrypoint = \"{second_entrypoint}\"\n```\n"),
        )

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.export()

        self.assertEqual("binding-frontier-stale", raised.exception.code)
        self.assertEqual({}, self.output_files())

    def test_binding_frontier_requires_an_explicit_atom_id_in_control_metadata(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        entrypoint = self.engine_entrypoint("FEATURE_PROGRAMMATIC/FEATURE_TOOLS/NO_ID_TOOL/no_id.py")
        member = self.root / entrypoint
        member.parent.mkdir(parents=True, exist_ok=True)
        member.write_bytes(b"VALUE = 1\n")
        source = carrier("CA-D-012", content_role="Delivery", body=f"```toml\n[tool_binding]\nentrypoint = \"{entrypoint}\"\n```\n")
        self.write_control_delivery(
            "003_PROJECT_CONFIGURATION/CA-SU-16_FEATURE_TOOLS/NO_ID_TOOL/CA-D-012--tool.md",
            source.replace(b"atom_id: CA-D-012\n", b""),
        )

        with self.assertRaises(exporter.MethodologyExportError) as raised:
            self.freeze([{"atom_id": "CA-R-001", "version": 1}])

        self.assertEqual("binding-source-identity-invalid", raised.exception.code)

    def test_declared_control_frontier_contains_required_tool_bindings_without_using_methodology_source_layout(self) -> None:
        expected = {}
        for atom_id, relative, tool_relative in (
            ("CA-D-013", "CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/FIXTURE_TOOL/07_delivery/CA-D-013--fixture.md",
             "FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIXTURE_TOOL/fixture.py"),
            ("CA-D-014", "CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/07_delivery/CA-D-014--fixture.md",
             "FEATURE_PROGRAMMATIC/FEATURE_MCP/fixture.py"),
        ):
            entrypoint = self.engine_entrypoint(tool_relative)
            raw = carrier(atom_id, content_role="Delivery",
                          body=f"```toml\n[tool_binding]\nentrypoint = \"{entrypoint}\"\n```\n")
            source = self.write_engine_delivery(relative, raw)
            expected[atom_id] = (source.relative_to(self.root).as_posix(), digest(raw))
            target = self.root / entrypoint
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"VALUE = 1\n")
        self.write_engine_delivery(
            "CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery/CA-D-015--non-binding-fixture.md",
            carrier("CA-D-015", content_role="Delivery"),
        )
        binding = exporter.reopen_project_export_binding(self.root, self.source)

        frontier = exporter._binding_frontier(binding)

        by_id = {item.atom_id: item for item in frontier}
        self.assertTrue(set(expected).issubset(by_id))
        self.assertNotIn("CA-D-015", by_id)
        for atom_id, (source_path, sha256) in expected.items():
            self.assertEqual(source_path, by_id[atom_id].source_path)
            self.assertEqual(sha256, by_id[atom_id].sha256)
            self.assertEqual(1, by_id[atom_id].version)

    def test_configured_extension_revision_is_frozen_and_unselected_revision_is_excluded(self) -> None:
        self.write_instance(b'[extensions.demo]\nenabled = true\nrevision = "v2"\n')
        self.write("002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/CA-R-010--v1.md", carrier("CA-R-010"))
        v2 = self.write("002_INSTALLED_EXTENSIONS/demo/v2/04_requirement/CA-R-010--v2.md", carrier("CA-R-010", version=2))
        self.freeze([{"atom_id": "CA-R-010", "version": 2}])

        self.export()

        self.assertEqual(v2.read_bytes(), self.output_files()[self.source_relative("002_INSTALLED_EXTENSIONS/demo/v2/04_requirement/CA-R-010--v2.md")])
        self.assertNotIn(self.source_relative("002_INSTALLED_EXTENSIONS/demo/v1/04_requirement/CA-R-010--v1.md"), self.output_files())

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

    def test_project_binding_refuses_declaration_frontier_drift(self) -> None:
        self.write("001_CORE_META_MODEL/04_requirement/CA-R-001--active.md", carrier("CA-R-001"))
        self.freeze([{"atom_id": "CA-R-001", "version": 1}])
        declaration = Path(self.declarations["METHODOLOGY_SOURCES"]["declaration_path"])
        declaration.write_text(declaration.read_text(encoding="utf-8").replace("2026-11-02", "2026-11-03"), encoding="utf-8")

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
        legacy.pop("binding_atoms")
        legacy.pop("framework_engine_inventory_sha256")
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
        legacy.pop("binding_atoms")
        legacy.pop("framework_engine_inventory_sha256")
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
        self.source_path("003_PROJECT_CONFIGURATION/catalog/available.json").write_bytes(b'{"schema":"catalog.v2"}\n')
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
                project_root=self.root,
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
