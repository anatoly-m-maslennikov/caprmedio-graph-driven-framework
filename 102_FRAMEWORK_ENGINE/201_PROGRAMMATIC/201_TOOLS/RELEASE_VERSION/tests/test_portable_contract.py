"""Synthetic physical evidence for the sealed portable package contract."""

from __future__ import annotations

import hashlib
import json
import shutil
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
from release_compilation import build_preflight_validated_candidate, compile_sealed_methodology_export  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, bind_sealed_methodology_export  # noqa: E402
from release_portable_contract import (  # noqa: E402
    build_sealed_portable_compilation,
    collect_portable_source_snapshot,
    revalidate_portable_source_snapshot,
    revalidate_sealed_portable_compilation,
    seal_portable_source_snapshot,
)
from release_portable_package import prepare_portable_release_package  # noqa: E402
from source_catalog_admission import build_source_admission_receipt, read_source_admission_receipt  # noqa: E402


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _tree_digest(root: Path) -> str:
    rows = [
        {
            "path": path.relative_to(root).as_posix(),
            "sha256": _sha256(path.read_bytes()),
            "mode": path.stat().st_mode & 0o777,
        }
        for path in sorted(root.rglob("*"))
        if path.is_file()
    ]
    return _sha256(json.dumps(rows, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))


def carrier(atom_id: str, *, content_role: str | None = None) -> bytes:
    role = f"content_role: {content_role}\n" if content_role is not None else ""
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "status: Active\n"
        f"{role}"
        "version: 1\n"
        "updated_at: 2026-10-09 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode("utf-8")


class PortableContractTests(unittest.TestCase):
    def setUp(self) -> None:
        # Keep synthetic evidence inspectable on hosts that deny recursive
        # cleanup beneath an otherwise writable temporary directory.
        self.root = Path(tempfile.mkdtemp(dir="/private/tmp")).resolve()
        self.addCleanup(self._cleanup)
        self.source = self.root / CANONICAL_SOURCE_RELATIVE
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in ("04_requirement", "05_method", "06_evaluation", "07_delivery", "09_operations"):
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir(parents=True)
        self.write(".caprmedio_caprmedio/project_structure.toml", (
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f'authority_path = "{CANONICAL_SOURCE_RELATIVE}"\n'
            'delivery_path = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY"\n\n'
            "[[scope_units]]\n"
            'scope_unit_name = "FRAMEWORK_ENGINE"\n'
            'authority_path = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE"\n'
            'delivery_path = "102_FRAMEWORK_ENGINE"\n'
        ).encode())
        (self.root / ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE").mkdir()
        self.write(".caprmedio_caprmedio/caprmedio_project_settings.toml", b'[paths]\ncontrol_root = ".caprmedio_caprmedio"\n')
        self.instance_settings = self.write(
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml",
            b"",
        )
        self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml", b"")
        self.atom = self.write(f"{CANONICAL_SOURCE_RELATIVE}/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", carrier("CA-R-001"))
        self.support = self.write(f"{CANONICAL_SOURCE_RELATIVE}/003_PROJECT_CONFIGURATION/support.txt", b"declared support\n")
        self.write(".caprmedio_runtime/framework/current.toml", b'release = "N"\n')
        self.write("version.toml", b'[framework]\nversion = "N+1"\n')
        self.write("pyproject.toml", b"[project]\nname = 'portable-contract'\n")
        self.write("uv.lock", b"version = 1\n")
        self.write("defaults/runtime.toml", b"[runtime]\nname = 'portable'\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py", b"tool\n", 0o755)
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/app.py", b"app\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py", b"mcp\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/201_PROMPTS/prompt.md", b"prompt\n")
        self.skill = self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", b"# ca\n")
        self.write("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/agents/openai.yaml", b"name: ca\n")
        self.write("102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/Dockerfile", b"FROM scratch\nCOPY pyproject.toml uv.lock ./\n")
        self.write(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/COMPILE_APPLICABLE_METHODOLOGY/compile_applicable_methodology.py",
            (EXPORT_ROOT / "compile_applicable_methodology.py").read_bytes(),
            0o755,
        )
        self._write_catalog()
        self.run_root = self.root / ".caprmedio_tmp/release_candidates/portable-001"

    def _cleanup(self) -> None:
        try:
            shutil.rmtree(self.root)
        except OSError:
            pass

    def write(self, relative: str, payload: bytes, mode: int = 0o644) -> Path:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        path.chmod(mode)
        return path

    def _catalog_record(self, identity: str, kind: str, digest: str, path: str, receipt_sha256: str) -> list[str]:
        return [
            f"[source.{identity}]",
            f'kind = "{kind}"',
            f'revision = "{digest}"',
            f'sha256 = "{digest}"',
            f'admission_receipt_sha256 = "{receipt_sha256}"',
            'visibility = "public"',
            "selection_default = false",
            f'path = "{path}"',
            "",
        ]

    def _write_catalog(
        self,
        *,
        active_files: tuple[Path, ...] | None = None,
        binding_projection: tuple[Path, Path] | None = None,
        workspace: str = ".catalog",
    ) -> None:
        if active_files is None:
            active_files = (self.atom,)
        engine = _tree_digest(self.root / "102_FRAMEWORK_ENGINE")
        # Catalog digests use logical package-relative paths, not authoring
        # roots.  Build only those row shapes without copying any real source.
        active_root = self.root / f"{workspace}-active"
        active_root.mkdir()
        source_active_root = self.source / "001_CORE_META_MODEL"
        for active_file in active_files:
            active_copy = active_root / "001_CORE_META_MODEL" / active_file.relative_to(source_active_root)
            active_copy.parent.mkdir(parents=True, exist_ok=True)
            active_copy.write_bytes(active_file.read_bytes())
            active_copy.chmod(active_file.stat().st_mode & 0o777)
        active = _tree_digest(active_root / "001_CORE_META_MODEL")
        support_root = self.root / f"{workspace}-support"
        support_root.mkdir()
        copied = support_root / "003_PROJECT_CONFIGURATION/support.txt"
        copied.parent.mkdir(parents=True)
        copied.write_bytes(self.support.read_bytes())
        copied.chmod(self.support.stat().st_mode & 0o777)
        support = _tree_digest(support_root)
        descriptors: list[dict[str, object]] = [
            {
                "identity": "core-meta-model",
                "kind": "methodology",
                "revision": active,
                "sha256": active,
                "visibility": "public",
                "selection_default": False,
                "path": "methodology/active/001_CORE_META_MODEL",
            },
            {
                "identity": "local-core",
                "kind": "core",
                "revision": engine,
                "sha256": engine,
                "visibility": "public",
                "selection_default": False,
                "path": "102_FRAMEWORK_ENGINE",
            },
            {
                "identity": "methodology-support",
                "kind": "support",
                "revision": support,
                "sha256": support,
                "visibility": "public",
                "selection_default": False,
                "path": "methodology/support",
            },
        ]
        if binding_projection is not None:
            projection, relative = binding_projection
            binding_root = self.root / f"{workspace}-binding"
            binding_copy = binding_root / relative
            binding_copy.parent.mkdir(parents=True, exist_ok=True)
            binding_copy.write_bytes(projection.read_bytes())
            binding_copy.chmod(projection.stat().st_mode & 0o777)
            binding = _tree_digest(binding_root)
            descriptors.append({
                "identity": "delivery-bindings",
                "kind": "binding",
                "revision": binding,
                "sha256": binding,
                "visibility": "public",
                "selection_default": False,
                "path": "methodology/bindings",
            })
        receipt_bytes = build_source_admission_receipt(
            operator="fixture-operator",
            command_ref="fixture-command",
            action_run_id="fixture-action-run",
            sources=tuple(sorted(descriptors, key=lambda descriptor: str(descriptor["identity"]))),
        )
        receipt = read_source_admission_receipt(receipt_bytes)
        self.write(f"admissions/{receipt.sha256}.json", receipt_bytes)
        lines = ["schema_version = 1", ""]
        lines.extend(self._catalog_record("core-meta-model", "methodology", active, "methodology/active/001_CORE_META_MODEL", receipt.sha256))
        lines.extend(self._catalog_record("local-core", "core", engine, "102_FRAMEWORK_ENGINE", receipt.sha256))
        lines.extend(self._catalog_record("methodology-support", "support", support, "methodology/support", receipt.sha256))
        if binding_projection is not None:
            lines.extend(self._catalog_record("delivery-bindings", "binding", _tree_digest(self.root / f"{workspace}-binding"), "methodology/bindings", receipt.sha256))
        self.write("catalog.toml", ("\n".join(lines) + "\n").encode())

    def sealed(self, *, selected_atoms: list[dict[str, object]] | None = None):
        if selected_atoms is None:
            selected_atoms = [{"atom_id": "CA-R-001", "version": 1}]
        frozen = exporter.freeze_methodology_manifest(
            source_root=self.source,
            project_root=self.root,
            selected_atoms=selected_atoms,
            support_inventory=[{
                "path": "003_PROJECT_CONFIGURATION/support.txt",
                "sha256": _sha256(self.support.read_bytes()),
            }],
            catalog_pins=[],
        )
        frozen_path = self.write("freeze/manifest.json", exporter.frozen_manifest_bytes(frozen))
        exporter.export_selected_methodology(
            source_root=self.source,
            frozen_manifest_path=frozen_path,
            release_candidate_root=self.run_root,
            project_root=self.root,
        )
        candidate = build_preflight_validated_candidate(
            self.root,
            candidate_release="N+1",
            full_suite_environment={"runner": "fixture", "command": ["python", "-m", "unittest"], "working_directory": "."},
            candidate_image_reference="fixture:N+1",
        )[1]
        private = compile_sealed_methodology_export(bind_sealed_methodology_export(candidate, self.run_root))
        return candidate, private

    def test_builds_complete_physical_rows_and_revalidates_them(self) -> None:
        candidate, private = self.sealed()
        sealed = build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")
        rows = {row.destination_path: row for row in sealed.portable_package_rows}
        self.assertEqual(sealed.candidate_snapshot_manifest_sha256, candidate.manifest.sha256)
        self.assertEqual(sealed.framework_version, "N+1")
        self.assertEqual(sealed.version_toml_sha256, _sha256((self.root / "version.toml").read_bytes()))
        self.assertEqual(sealed.source_catalog_sha256, _sha256((self.root / "catalog.toml").read_bytes()))
        self.assertIn("102_FRAMEWORK_ENGINE/202_AGENTIC/205_SKILLS/ca/SKILL.md", rows)
        self.assertIn("SKILLS/ca/SKILL.md", rows)
        self.assertIn("methodology/active/001_CORE_META_MODEL/04_requirement/CA-R-001--core.md", rows)
        self.assertIn("methodology/support/003_PROJECT_CONFIGURATION/support.txt", rows)
        admissions = [row for row in rows.values() if row.resource == "SOURCE_ADMISSION"]
        self.assertEqual(len(admissions), 1)
        self.assertEqual(admissions[0].destination_path, admissions[0].source_path)
        self.assertEqual(admissions[0].destination_path, f"admissions/{admissions[0].sha256}.json")
        self.assertEqual(revalidate_sealed_portable_compilation(sealed), sealed)

    def test_collects_pre_catalog_source_snapshot_without_writing_or_reading_catalog(self) -> None:
        candidate, private = self.sealed()
        catalog = self.root / "catalog.toml"
        catalog.unlink()
        before = {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*")
            if path.is_file()
        }

        snapshot = collect_portable_source_snapshot(candidate, private, candidate_run_id="portable-001")

        after = {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after, before)
        self.assertNotIn("CATALOG", {row.resource for row in snapshot.portable_package_rows})
        self.assertNotIn("SOURCE_ADMISSION", {row.resource for row in snapshot.portable_package_rows})
        self.assertNotIn("catalog.toml", {row.destination_path for row in snapshot.portable_package_rows})
        self.assertEqual(revalidate_portable_source_snapshot(snapshot), snapshot)

    def test_collects_frozen_binding_projection_without_copying_live_delivery_authority(self) -> None:
        delivery_relative = ".caprmedio_caprmedio/07_delivery/CA-D-001--binding.md"
        delivery = self.write(
            delivery_relative,
            carrier("CA-D-001", content_role="Delivery")
            + b"\n```toml\n[tool_binding]\n"
            + b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n```\n',
        )
        candidate, private = self.sealed(selected_atoms=[
            {"atom_id": "CA-R-001", "version": 1},
        ])
        snapshot = collect_portable_source_snapshot(candidate, private, candidate_run_id="portable-001")

        self.assertEqual(1, len(snapshot.binding_atoms))
        binding = snapshot.binding_atoms[0]
        self.assertEqual("CA-D-001", binding.atom_id)
        self.assertEqual(1, binding.version)
        self.assertEqual(
            delivery_relative,
            binding.source_path,
        )
        self.assertEqual(_sha256(delivery.read_bytes()), binding.sha256)
        rows = [row for row in snapshot.portable_package_rows if row.resource == "BINDING_PROJECTION"]
        self.assertEqual(1, len(rows))
        self.assertEqual(
            f"methodology/bindings/{binding.source_path}",
            rows[0].destination_path,
        )
        self.assertNotEqual(binding.sha256, rows[0].sha256)
        self.assertEqual(revalidate_portable_source_snapshot(snapshot), snapshot)

    def test_seals_and_assembles_the_binding_projection_with_exact_source_pin(self) -> None:
        delivery = self.write(
            ".caprmedio_caprmedio/07_delivery/CA-D-001--binding.md",
            carrier("CA-D-001", content_role="Delivery")
            + b"\n```toml\n[tool_binding]\n"
            + b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n```\n',
        )
        candidate, private = self.sealed(selected_atoms=[
            {"atom_id": "CA-R-001", "version": 1},
        ])
        snapshot = collect_portable_source_snapshot(candidate, private, candidate_run_id="portable-001")
        projection = next(row for row in snapshot.portable_package_rows if row.resource == "BINDING_PROJECTION")
        self._write_catalog(
            active_files=(self.atom,),
            binding_projection=(
                self.root / projection.source_path,
                Path(projection.destination_path).relative_to("methodology/bindings"),
            ),
            workspace=".binding-catalog",
        )

        sealed = seal_portable_source_snapshot(snapshot)
        prepared = prepare_portable_release_package(self.root, sealed)

        self.assertEqual(tuple(atom.record() for atom in prepared.package.binding_atoms), tuple(atom.record() for atom in sealed.binding_atoms))
        package_projection = next(
            row for row in prepared.package.inventory
            if row.role == "binding-projection"
        )
        self.assertEqual(projection.destination_path, package_projection.path)
        self.assertEqual(
            (self.root / projection.source_path).read_bytes(),
            (prepared.private_package_root / projection.destination_path).read_bytes(),
        )
        self.assertNotEqual(delivery.read_bytes(), (prepared.private_package_root / projection.destination_path).read_bytes())

    def test_pre_catalog_source_snapshot_refuses_physical_drift(self) -> None:
        candidate, private = self.sealed()
        snapshot = collect_portable_source_snapshot(candidate, private, candidate_run_id="portable-001")
        defaults = self.root / "defaults/runtime.toml"
        defaults.write_bytes(defaults.read_bytes() + b"changed = true\n")

        with self.assertRaises(ReleaseContractError) as stale:
            revalidate_portable_source_snapshot(snapshot)
        self.assertEqual(stale.exception.code, "portable-source-snapshot-stale")

    def test_seals_the_exact_admitted_pre_catalog_snapshot(self) -> None:
        candidate, private = self.sealed()
        snapshot = collect_portable_source_snapshot(candidate, private, candidate_run_id="portable-001")

        sealed = seal_portable_source_snapshot(snapshot)
        compatibility = build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")

        self.assertEqual(sealed, compatibility)
        self.assertEqual(sealed.candidate_run_id, snapshot.candidate_run_id)
        self.assertEqual(sealed.candidate, snapshot.candidate)
        self.assertEqual(sealed.private_compilation, snapshot.private_compilation)
        self.assertEqual(revalidate_sealed_portable_compilation(sealed), sealed)

    def test_seal_refuses_bool_or_raw_snapshot_without_output_effects(self) -> None:
        candidate, private = self.sealed()
        before = {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*")
            if path.is_file()
        }

        for value in (False, {"candidate": candidate, "private": private}):
            with self.subTest(value=type(value).__name__):
                with self.assertRaises(ReleaseContractError) as invalid:
                    seal_portable_source_snapshot(value)  # type: ignore[arg-type]
                self.assertEqual(invalid.exception.code, "portable-source-snapshot-untrusted")

        after = {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after, before)

    def test_seal_refuses_source_drift_before_reading_catalog_or_writing(self) -> None:
        candidate, private = self.sealed()
        snapshot = collect_portable_source_snapshot(candidate, private, candidate_run_id="portable-001")
        defaults = self.root / "defaults/runtime.toml"
        defaults.write_bytes(defaults.read_bytes() + b"changed = true\n")
        catalog = self.root / "catalog.toml"
        catalog.write_bytes(b"not valid TOML either")
        before = {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*")
            if path.is_file()
        }

        with self.assertRaises(ReleaseContractError) as stale:
            seal_portable_source_snapshot(snapshot)
        self.assertEqual(stale.exception.code, "portable-source-snapshot-stale")

        after = {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*")
            if path.is_file()
        }
        self.assertEqual(after, before)

    def test_defaults_or_catalog_drift_refuse_reopen(self) -> None:
        candidate, private = self.sealed()
        sealed = build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")
        defaults = self.root / "defaults/runtime.toml"
        defaults.write_bytes(defaults.read_bytes() + b"changed = true\n")
        with self.assertRaises(ReleaseContractError) as stale:
            revalidate_sealed_portable_compilation(sealed)
        self.assertEqual(stale.exception.code, "portable-contract-stale")
        defaults.write_bytes(b"[runtime]\nname = 'portable'\n")
        (self.root / "catalog.toml").write_bytes(b"schema_version = 1\n")
        with self.assertRaises(ReleaseContractError) as catalog:
            build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")
        self.assertEqual(catalog.exception.code, "catalog-invalid")

    def test_portable_contract_reuses_scalar_catalog_descriptor_validation(self) -> None:
        candidate, private = self.sealed()
        catalog = self.root / "catalog.toml"
        original = catalog.read_bytes()
        for expected, replacement in (
            (b'kind = "core"', b'kind = ["core"]'),
            (b'visibility = "public"', b'visibility = ["public"]'),
        ):
            with self.subTest(replacement=replacement):
                catalog.write_bytes(original.replace(expected, replacement, 1))
                with self.assertRaises(ReleaseContractError) as raised:
                    build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")
                self.assertEqual(raised.exception.code, "catalog-invalid")
                catalog.write_bytes(original)

    def test_requires_physical_receipt_and_exact_catalog_descriptor_match(self) -> None:
        candidate, private = self.sealed()
        catalog = self.root / "catalog.toml"
        original = catalog.read_bytes()
        receipt = next((self.root / "admissions").glob("*.json"))
        receipt_bytes = receipt.read_bytes()
        receipt.unlink()
        with self.assertRaises(ReleaseContractError) as missing:
            build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")
        self.assertEqual(missing.exception.code, "portable-contract-admission-missing")

        receipt.write_bytes(receipt_bytes)
        catalog.write_bytes(original.replace(b'visibility = "public"', b'visibility = "private"', 1))
        with self.assertRaises(ReleaseContractError) as mismatch:
            build_sealed_portable_compilation(candidate, private, candidate_run_id="portable-001")
        self.assertEqual(mismatch.exception.code, "portable-contract-admission-mismatch")


if __name__ == "__main__":
    unittest.main()
