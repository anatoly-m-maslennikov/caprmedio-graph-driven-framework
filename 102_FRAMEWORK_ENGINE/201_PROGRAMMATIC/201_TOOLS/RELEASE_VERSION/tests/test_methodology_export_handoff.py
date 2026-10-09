"""Private exporter-to-compiler bindings with disposable Methodology sources."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
EXPORT_ROOT = RELEASE_ROOT.parents[0] / "COMPILE_APPLICABLE_METHODOLOGY"
for path in (RELEASE_ROOT, EXPORT_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import methodology_export as exporter  # noqa: E402
from release_compilation import (  # noqa: E402
    PRIVATE_COMPILED_MANIFEST_NAME,
    build_preflight_validated_candidate,
    compile_sealed_methodology_export,
    read_sealed_private_methodology_compilation,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, bind_sealed_methodology_export  # noqa: E402


def carrier(atom_id: str) -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "status: Active\n"
        "version: 1\n"
        "updated_at: 2026-10-09 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode("utf-8")


class MethodologyExportHandoffTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve(strict=True)
        self.source = self.root / CANONICAL_SOURCE_RELATIVE
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir(parents=True)
        self.write(".caprmedio_caprmedio/project_structure.toml", (
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f'authority_path = "{CANONICAL_SOURCE_RELATIVE}"\n'
        ).encode())
        self.write(".caprmedio_caprmedio/caprmedio_project_settings.toml", b'[paths]\ncontrol_root = ".caprmedio_caprmedio"\n')
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml", b"")
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml", b"")
        self.atom = self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        self.write(".caprmedio_runtime/framework/current.toml", b'release = "N"\n')
        self.write("version.toml", b'[framework]\nversion = "N+1"\n')
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n", 0o755)
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"mcp\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md", b"prompt\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", b"# ca\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", b"name: ca\n")
        self.write("pyproject.toml", b"[project]\nname = 'fixture'\n")
        self.write("uv.lock", b"version = 1\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile", b"FROM scratch\nCOPY pyproject.toml uv.lock ./\n")
        self.write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            (EXPORT_ROOT / "compile_applicable_methodology.py").read_bytes(),
            0o755,
        )
        self.candidate_root = self.root / ".caprmedio_tmp/release_candidates/run-001"

    def write(self, relative: str, data: bytes, mode: int = 0o644) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        path.chmod(mode)
        return path

    def candidate(self):
        return build_preflight_validated_candidate(
            self.root,
            candidate_release="N+1",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+1",
        )[1]

    def export(self) -> None:
        manifest = exporter.freeze_methodology_manifest(
            source_root=self.source,
            selected_atoms=[{"atom_id": "CA-R-001", "version": 1}],
            support_inventory=[],
            catalog_pins=[],
        )
        frozen = self.write("freeze/manifest.json", exporter.frozen_manifest_bytes(manifest))
        exporter.export_selected_methodology(
            source_root=self.source,
            frozen_manifest_path=frozen,
            release_candidate_root=self.candidate_root,
        )

    def test_sealed_export_binds_candidate_and_private_compiled_manifest(self) -> None:
        self.export()
        candidate = self.candidate()
        bound = bind_sealed_methodology_export(candidate, self.candidate_root)
        compiled = compile_sealed_methodology_export(bound)
        manifest_path = self.root / compiled.compiled_root / PRIVATE_COMPILED_MANIFEST_NAME
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        self.assertEqual(bound.candidate.manifest.sha256, candidate.manifest.sha256)
        self.assertEqual(manifest["frozen_manifest_sha256"], bound.frozen_manifest_sha256)
        self.assertEqual(manifest["export_inventory_sha256"], bound.export_inventory_sha256)
        self.assertEqual(manifest["export_seal_sha256"], bound.export_seal_sha256)
        self.assertEqual(manifest["sha256"], compiled.compiled_manifest_sha256)
        self.assertTrue((self.root / compiled.compiled_root / "04_requirement" / self.atom.name).is_file())
        self.assertFalse((self.root / "methodology").exists())
        self.assertFalse((self.root / ".caprmedio_caprmedio/_projection").exists())
        projected = self.root / compiled.compiled_root / "04_requirement" / self.atom.name
        projected.write_bytes(projected.read_bytes() + b"tampered\n")
        with self.assertRaises(ReleaseContractError) as raised:
            read_sealed_private_methodology_compilation(bound)
        self.assertEqual(raised.exception.code, "release-private-compiled-invalid")

    def test_unsealed_or_tampered_export_cannot_be_bound_or_compiled(self) -> None:
        self.export()
        candidate = self.candidate()
        exported_atom = self.candidate_root / "methodology" / self.atom.relative_to(self.source)
        exported_atom.write_bytes(exported_atom.read_bytes() + b"tampered\n")
        with self.assertRaises(ReleaseContractError) as raised:
            bind_sealed_methodology_export(candidate, self.candidate_root)
        self.assertEqual(raised.exception.code, "export-seal-invalid")
        self.assertFalse((self.candidate_root / "compiled").exists())

    def test_candidate_source_change_refuses_even_when_old_export_seal_remains(self) -> None:
        self.export()
        candidate = self.candidate()
        self.atom.write_bytes(self.atom.read_bytes() + b"changed\n")
        with self.assertRaises(ReleaseContractError) as raised:
            bind_sealed_methodology_export(candidate, self.candidate_root)
        self.assertEqual(raised.exception.code, "release-currentness-stale")
        self.assertFalse((self.candidate_root / "compiled").exists())


if __name__ == "__main__":
    unittest.main()
