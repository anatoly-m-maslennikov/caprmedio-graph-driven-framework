"""Schema-1 image-context coverage with a real reopened portable package.

No test invokes Docker.  The package is assembled and reopened through the
production portable-package and package-evidence adapters before its private
image context is inspected.
"""

from __future__ import annotations

import hashlib
import json
import sys
import unittest
from dataclasses import replace
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_image import (  # noqa: E402
    PortableImageBuildEvidence,
    _portable_context,
    _read_portable_context_evidence,
    _tree,
    build_candidate_image,
)
from release_package_evidence import bind_package_evidence  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_package import retain_native_package_evidence  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402


UNIT_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_portable_image_unit.py"


def _test_member(name: str) -> bytes:
    return f"def test_{name.replace('/', '_').replace('.', '_')}():\n    assert True\n".encode("utf-8")


def _fixture() -> PortablePackageFixture:
    return PortablePackageFixture(
        extra_engine_members={path: _test_member(path) for path in (*CANDIDATE_E2E_MODULES, UNIT_MODULE)},
    )


class _NoDocker:
    def run(self, argv, *, cwd, timeout_seconds):  # pragma: no cover - must not be reached
        raise AssertionError(f"unexpected Docker invocation: {argv}")


class PortableReleaseImageTests(unittest.TestCase):
    def test_native_context_copies_the_complete_reopened_schema_one_package(self) -> None:
        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        view = bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=prepared)
        attempt = fixture.root / ".caprmedio_tmp/native-image-context"
        attempt.mkdir()

        context, manifest_digest = _portable_context(fixture.root, fixture.candidate, view, attempt)

        self.assertEqual("portable-1", view.package_schema)
        self.assertEqual(view.actual_package_manifest_sha256, manifest_digest)
        self.assertEqual(
            (prepared.package.root / "manifest.toml").read_bytes(),
            (context / "PACKAGE/manifest.toml").read_bytes(),
        )
        source_admissions = [member for member in view.member_inventory if member.role == "source-admission"]
        self.assertEqual(1, len(source_admissions))
        for member in view.member_inventory:
            copied = context / "PACKAGE" / member.path
            self.assertTrue(copied.is_file(), member.path)
            self.assertEqual(member.sha256, hashlib.sha256(copied.read_bytes()).hexdigest())
        self.assertTrue((context / "PACKAGE" / source_admissions[0].path).is_file())
        self.assertTrue((context / "102_FRAMEWORK_ENGINE").is_dir())
        spec = json.loads((context / "canary.json").read_bytes())
        self.assertEqual(view.actual_package_manifest_sha256, spec["package_manifest_sha256"])
        self.assertEqual(view.source_catalog_sha256, spec["source_catalog_sha256"])
        self.assertEqual(view.candidate_run_id, spec["candidate_run_id"])
        self.assertEqual(view.input_manifest_sha256, spec["input_manifest_sha256"])
        self.assertEqual(view.framework_version, spec["framework_version"])
        self.assertEqual(view.version_toml_sha256, spec["version_toml_sha256"])
        self.assertEqual(len(view.member_inventory), len(spec["package_rows"]))

    def test_native_build_requires_typed_prepared_package_before_any_docker_call(self) -> None:
        fixture = _fixture()

        with self.assertRaises(ReleaseContractError) as raised:
            build_candidate_image(
                fixture.candidate,
                fixture.sealed,
                object(),  # type: ignore[arg-type]
                executor=_NoDocker(),
            )

        self.assertEqual("release-image-portable-package-required", raised.exception.code)

    def test_retained_native_context_proof_survives_later_source_drift(self) -> None:
        """Historical image reads use only the copied package and sidecar.

        Changing the source invalidates the live binder, while the retained
        package context remains readable with its pre-Docker sidecar.  This is
        the selection-change boundary: no later artifact reader gets a fresh
        package view from current Project state.
        """

        fixture = _fixture()
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        retained = retain_native_package_evidence(fixture.candidate, fixture.sealed, prepared)
        attempt = fixture.root / ".caprmedio_runtime/release_image" / fixture.candidate.manifest.sha256 / "build" / "attempt-sidecar"
        attempt.mkdir(parents=True)
        context, package_manifest = _portable_context(fixture.root, fixture.candidate, retained.view, attempt)
        sidecar_relative = retained.receipt_path.relative_to(fixture.root).as_posix()
        build = PortableImageBuildEvidence(
            candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
            outcome="built",
            reason="fixture",
            candidate_image_digest="sha256:" + "c" * 64,
            context_root=context.relative_to(fixture.root).as_posix(),
            context_sha256=_tree(context),
            package_manifest_sha256=package_manifest,
            suite_receipt_sha256="d" * 64,
            evidence_root=attempt.relative_to(fixture.root).as_posix(),
            commands_sha256="e" * 64,
            execution_kind="test-double",
            source_catalog_sha256=retained.view.source_catalog_sha256,
            candidate_run_id=retained.view.candidate_run_id,
            input_manifest_sha256=retained.view.input_manifest_sha256,
            framework_version=retained.view.framework_version,
            version_toml_sha256=retained.view.version_toml_sha256,
            package_evidence_sha256=retained.receipt_sha256,
            package_evidence_relpath=sidecar_relative,
        )

        fixture.atom_one.write_bytes(fixture.atom_one.read_bytes() + b"\nchanged after image selection\n")
        (fixture.root / ".caprmedio_runtime/framework/current.toml").write_text('release = "other"\n')
        with self.assertRaises(ReleaseContractError):
            bind_package_evidence(fixture.candidate, fixture.sealed, prepared_package=prepared)

        reopened = _read_portable_context_evidence(fixture.root, build)

        self.assertEqual(retained.receipt_sha256, reopened.receipt_sha256)
        self.assertEqual(package_manifest, reopened.view.actual_package_manifest_sha256)
        self.assertEqual(retained.view.member_inventory, reopened.view.member_inventory)

        unsafe = fixture.root / "sidecar-link"
        unsafe.symlink_to(retained.receipt_path)
        with self.assertRaises(ReleaseContractError) as raised:
            _read_portable_context_evidence(
                fixture.root,
                replace(build, package_evidence_relpath="sidecar-link"),
            )
        self.assertEqual("release-image-package-evidence-path-invalid", raised.exception.code)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
