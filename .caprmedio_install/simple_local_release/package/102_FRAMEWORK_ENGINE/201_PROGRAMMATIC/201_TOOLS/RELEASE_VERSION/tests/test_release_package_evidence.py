"""Physical, read-only coverage for the package-evidence adapter."""

from __future__ import annotations

from dataclasses import replace
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_package import (  # noqa: E402
    read_retained_native_package_evidence,
    retain_native_package_evidence,
)
from framework_package import assemble_framework_package  # noqa: E402
from release_handoff import (  # noqa: E402
    CompilerSuccessEvidence,
    build_validated_candidate,
    seal_candidate_compilation,
    validate_source_copy,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff_fixture import COMPILER, MATERIALIZED, ReleaseFixture, digest  # noqa: E402
from release_package_evidence import (  # noqa: E402
    PackageEvidenceError,
    bind_package_evidence,
    verify_bound_package_evidence,
)
from release_packaging import _complete_rows, _copy_release, _render_manifest  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES  # noqa: E402


UNIT_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_package_evidence_unit.py"
_ROLE_BY_RESOURCE = {
    "FRAMEWORK_ENGINE": "engine",
    "SKILL": "skill",
    "DEPENDENCY": "dependency",
    "PACKAGE_CONTROL": "version",
    "CATALOG": "catalog",
    "SOURCE_ADMISSION": "source-admission",
    "DEFAULT": "default",
    "METHODOLOGY": "methodology",
    "METHODOLOGY_SUPPORT": "methodology-support",
    "BINDING_PROJECTION": "binding-projection",
}


def _test_member(name: str) -> bytes:
    return f"def test_{name.replace('/', '_').replace('.', '_')}():\n    assert True\n".encode("utf-8")


def _fixture() -> PortablePackageFixture:
    members = {path: _test_member(path) for path in (*CANDIDATE_E2E_MODULES, UNIT_MODULE)}
    return PortablePackageFixture(extra_engine_members=members)


class _BindingPortablePackageFixture(PortablePackageFixture):
    """A physical candidate source with one exporter-frozen Delivery binding."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        self.binding_source = self.write(
            ".caprmedio_caprmedio/07_delivery/CA-D-901--binding.md",
            b"---\natom_id: CA-D-901\nstatus: Active\ncontent_role: Delivery\n"
            b"version: 1\nupdated_at: 2026-10-10 00:00:00 +0000\nrelations: {}\n---\n"
            b"# CA-D-901\n\n```toml\n[tool_binding]\n"
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n```\n',
        )


def _binding_fixture() -> _BindingPortablePackageFixture:
    members = {path: _test_member(path) for path in (*CANDIDATE_E2E_MODULES, UNIT_MODULE)}
    return _BindingPortablePackageFixture(extra_engine_members=members)


def _legacy_fixture(root: Path):
    fixture = ReleaseFixture(root)
    for path in (*CANDIDATE_E2E_MODULES, UNIT_MODULE):
        fixture.write(path, _test_member(path))
    candidate = build_validated_candidate(fixture.root, fixture.intent)
    fixture.deliver_copy()
    source_copy = validate_source_copy(candidate)
    fixture.materialize_bytes(candidate.manifest.sha256)
    evidence = CompilerSuccessEvidence(
        candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
        outcome="completed",
        compiler_entrypoint={"path": COMPILER, "sha256": digest((fixture.root / COMPILER).read_bytes())},
        compiler_frontier_digest=candidate.manifest.source_frontier_digest,
        child_materialization_root=f"{MATERIALIZED}/{candidate.manifest.sha256}",
        actual_compiled_output_sha256=candidate.manifest.expected_compiled_output_sha256,
    )
    return fixture, candidate, seal_candidate_compilation(source_copy, evidence)


def _member_inventory(rows) -> tuple[tuple[str, str, int, str], ...]:
    return tuple(sorted(
        (row.destination_path, row.sha256, row.mode, _ROLE_BY_RESOURCE[row.resource])
        for row in rows
    ))


class PackageEvidenceAdapterTests(unittest.TestCase):
    def test_legacy_view_reopens_actual_schema_two_package(self) -> None:
        fixture, candidate, compilation = _legacy_fixture(Path(tempfile.mkdtemp(prefix="package-evidence-legacy-")))
        candidate_sha256, rows, _selector_before = _complete_rows(fixture.root, compilation)
        release_root = fixture.root / ".caprmedio_runtime/framework/releases" / candidate_sha256
        release_root.mkdir(parents=True)
        manifest = _render_manifest(
            candidate_sha256,
            rows,
            framework_version=compilation.framework_version,
            version_toml_sha256=compilation.version_toml_sha256,
        )
        _copy_release(
            fixture.root,
            release_root,
            rows,
            manifest,
            framework_version=compilation.framework_version,
            version_toml_sha256=compilation.version_toml_sha256,
        )

        view = bind_package_evidence(candidate, compilation)

        self.assertEqual("legacy-2", view.package_schema)
        self.assertEqual(candidate.manifest.sha256, view.candidate_snapshot_manifest_sha256)
        self.assertEqual(release_root, view.package_root)
        self.assertEqual(tuple(sorted(CANDIDATE_E2E_MODULES)), view.phase_map.candidate_e2e_paths)
        self.assertEqual((UNIT_MODULE,), view.phase_map.unit_paths)
        self.assertEqual(_member_inventory(compilation.package_rows), tuple(
            (member.path, member.sha256, member.mode, member.role) for member in view.member_inventory
        ))

    def test_portable_view_reopens_physical_package_and_exact_phase_partition(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)

        view = bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=prepared)

        self.assertEqual("portable-1", view.package_schema)
        self.assertEqual(fixture.candidate.manifest.sha256, view.candidate_snapshot_manifest_sha256)
        self.assertEqual(prepared.package_manifest_sha256, view.actual_package_manifest_sha256)
        self.assertEqual(fixture.sealed.source_catalog_sha256, view.source_catalog_sha256)
        self.assertEqual(fixture.run_id, view.candidate_run_id)
        self.assertEqual(fixture.sealed.input_manifest_sha256, view.input_manifest_sha256)
        self.assertEqual(prepared.package.root, view.package_root)
        self.assertEqual("N+1", view.framework_version)
        self.assertEqual(fixture.sealed.version_toml_sha256, view.version_toml_sha256)
        self.assertEqual(_member_inventory(fixture.sealed.portable_package_rows), tuple(
            (member.path, member.sha256, member.mode, member.role) for member in view.member_inventory
        ))
        self.assertEqual(tuple(sorted(CANDIDATE_E2E_MODULES)), view.phase_map.candidate_e2e_paths)
        self.assertEqual((UNIT_MODULE,), view.phase_map.unit_paths)
        self.assertEqual(
            {UNIT_MODULE, *CANDIDATE_E2E_MODULES},
            {path for path, _digest, _phase in view.phase_map.rows},
        )
        self.assertFalse(hasattr(view, "passed"))
        self.assertFalse(hasattr(view, "outcome"))

    def test_portable_binding_frontier_reopens_in_view_and_retained_proof(self) -> None:
        fixture = _binding_fixture()
        self.addCleanup(fixture.cleanup)
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)

        view = bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=prepared)
        self.assertTrue(fixture.source_snapshot.binding_atoms)
        self.assertEqual(fixture.source_snapshot.binding_atoms, fixture.sealed.binding_atoms)
        self.assertTrue(prepared.package.binding_atoms)
        self.assertEqual(
            tuple(atom.record() for atom in fixture.sealed.binding_atoms),
            tuple(atom.record() for atom in prepared.package.binding_atoms),
        )
        expected_projection_paths = {
            f"methodology/bindings/{atom.source_path}"
            for atom in fixture.sealed.binding_atoms
        }
        binding_members = tuple(member for member in view.member_inventory if member.role == "binding-projection")
        self.assertEqual(expected_projection_paths, {member.path for member in binding_members})
        self.assertEqual(
            tuple(sorted(CANDIDATE_E2E_MODULES)),
            view.phase_map.candidate_e2e_paths,
        )
        self.assertNotIn(
            fixture.sealed.binding_atoms[0].source_path,
            {path for path, _digest, _phase in view.phase_map.rows},
        )

        retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
        reopened = read_retained_native_package_evidence(
            retained.view.package_root,
            retained.receipt_path,
            expected_sha256=retained.receipt_sha256,
        )
        self.assertEqual(view, retained.view)
        self.assertEqual(retained, reopened)
        self.assertEqual(binding_members, tuple(member for member in reopened.view.member_inventory if member.role == "binding-projection"))

    def test_supplied_view_is_rebound_before_acceptance(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        view = bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=prepared)

        self.assertEqual(
            view,
            verify_bound_package_evidence(fixture.candidate, fixture.sealed, view, prepared_package=prepared),
        )
        for forged in (
            replace(view, actual_package_manifest_sha256="0" * 64),
            replace(view, member_inventory=()),
        ):
            with self.subTest(forged=forged), self.assertRaises(PackageEvidenceError) as raised:
                verify_bound_package_evidence(fixture.candidate, fixture.sealed, forged, prepared_package=prepared)
            self.assertEqual("package-evidence-view-mismatch", raised.exception.code)
        with self.assertRaises(PackageEvidenceError) as raw:
            verify_bound_package_evidence(fixture.candidate, fixture.sealed, object(), prepared_package=prepared)  # type: ignore[arg-type]
        self.assertEqual("package-evidence-view-untrusted", raw.exception.code)

    def test_raw_rebound_and_missing_portable_receipts_refuse(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        for compilation, receipt, expected in (
            ({"portable_package_rows": []}, None, "package-evidence-compilation-untrusted"),
            (fixture.sealed, None, "package-evidence-portable-package-required"),
            (fixture.sealed, replace(prepared, candidate_run_id="different-run"), "package-evidence-portable-receipt-mismatch"),
        ):
            with self.subTest(expected=expected), self.assertRaises(PackageEvidenceError) as raised:
                bind_package_evidence(fixture.candidate, compilation, prepared_package=receipt)  # type: ignore[arg-type]
            self.assertEqual(expected, raised.exception.code)

        other = _fixture()
        with self.assertRaises(PackageEvidenceError) as rebound:
            bind_package_evidence(other.candidate, fixture.sealed, prepared_package=prepared)
        self.assertEqual("package-evidence-candidate-mismatch", rebound.exception.code)

    def test_portable_source_or_package_drift_refuses_reopen(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        (fixture.root / "defaults/runtime-config.toml").write_bytes(b"[runtime]\nprofile = 'drifted'\n")

        with self.assertRaises(ReleaseContractError) as source_drift:
            bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=prepared)
        self.assertIn(getattr(source_drift.exception, "code", ""), {"portable-contract-stale", "release-currentness-stale"})

        package_fixture = _fixture()
        package_prepared = prepare_portable_release_package(package_fixture.root, package_fixture.sealed)
        (package_prepared.package.root / "defaults/runtime-config.toml").write_bytes(b"[runtime]\nprofile = 'drifted'\n")
        with self.assertRaises(PackageEvidenceError) as package_drift:
            bind_package_evidence(package_fixture.candidate, package_fixture.sealed, prepared_package=package_prepared)
        self.assertIn(
            package_drift.exception.code,
            {"package-member-digest-mismatch", "package-file-digest-mismatch", "package-evidence-portable-package-stale"},
        )

    def test_portable_receipt_cannot_rebind_a_different_valid_package_inventory(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        assembly = Path(tempfile.mkdtemp(prefix="package-evidence-forged-", dir=fixture.root / ".caprmedio_tmp"))
        shutil.copytree(prepared.package.root, assembly, dirs_exist_ok=True)
        (assembly / "manifest.toml").unlink()
        (assembly / "defaults/runtime.toml").write_bytes(b"[runtime]\nprofile = 'forged'\n")
        forged_package = assemble_framework_package(assembly, prepared.package.root.parent)
        forged = replace(prepared, package=forged_package)

        with self.assertRaises(PackageEvidenceError) as raised:
            bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=forged)
        self.assertEqual("package-evidence-portable-inventory-mismatch", raised.exception.code)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
