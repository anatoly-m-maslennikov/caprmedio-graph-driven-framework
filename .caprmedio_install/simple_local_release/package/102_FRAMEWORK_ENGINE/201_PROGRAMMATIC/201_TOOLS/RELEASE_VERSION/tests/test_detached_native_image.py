"""Detached native Image artifact-reader coverage.

These fixtures write mock execution receipts only.  They do not run Docker,
establish a production image proof, or claim a release gate has passed.
"""

from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for _path in (RELEASE_ROOT, TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_image import (  # noqa: E402
    CANDIDATE_LABEL,
    CONTEXT_LABEL,
    IMAGE_ROOT,
    PortableImageBuildEvidence,
    PortableImageVerificationEvidence,
    _portable_context,
    _tree,
    read_detached_image_execution_artifacts,
)
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_candidate import (  # noqa: E402
    read_retained_candidate_identity,
    retain_retained_candidate_identity,
)
from release_suite import PortableSuiteGateEvidence  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES  # noqa: E402


_UNIT_MODULE = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_detached_native_image_unit.py"


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    path.chmod(mode)


def _test_members() -> dict[str, bytes]:
    paths = (*CANDIDATE_E2E_MODULES, _UNIT_MODULE)
    return {
        path: f"def test_{Path(path).stem}():\n    assert True\n".encode("utf-8")
        for path in paths
    }


def _seal(attempt: Path, evidence):
    payload = canonical_json(asdict(evidence))
    _write(attempt / "receipt.json", payload)
    return replace(evidence, receipt_sha256=_digest(payload))


class DetachedNativeImageReaderTests(unittest.TestCase):
    def _suite_receipt(self, fixture: PortablePackageFixture, retained) -> PortableSuiteGateEvidence:
        attempt = (
            fixture.root / ".caprmedio_runtime/release_suite"
            / fixture.candidate.manifest.sha256 / "attempt-mock-native"
        )
        stdout, stderr, coverage = b"MOCK DATA ONLY suite\n", b"", b"<testsuite tests='1'/>\n"
        _write(attempt / "stdout.bin", stdout)
        _write(attempt / "stderr.bin", stderr)
        _write(attempt / "coverage.xml", coverage)
        environment = fixture.candidate.manifest.full_suite_environment
        evidence = PortableSuiteGateEvidence(
            input_schema="portable-1",
            candidate_snapshot_manifest_sha256=fixture.candidate.manifest.sha256,
            candidate_run_id=retained.view.candidate_run_id,
            input_manifest_sha256=retained.view.input_manifest_sha256,
            source_catalog_sha256=retained.view.source_catalog_sha256,
            framework_version=retained.view.framework_version,
            version_toml_sha256=retained.view.version_toml_sha256,
            outcome="passed",
            reason="MOCK DATA ONLY detached image predecessor",
            runner=environment.runner,
            command=tuple(environment.command),
            working_directory=environment.working_directory,
            exit_code=0,
            executed_tests=1,
            coverage=("mock",),
            evidence_root=attempt.relative_to(fixture.root).as_posix(),
            stdout_sha256=_digest(stdout),
            stderr_sha256=_digest(stderr),
            report_sha256=_digest(coverage),
            executing_selector_sha256="a" * 64,
            executing_release_package_sha256="b" * 64,
            executing_skill_sha256="c" * 64,
            receipt_sha256=None,
            elapsed_seconds=0.0,
            control_context_digest="d" * 64,
            phase_map_sha256=retained.view.phase_map.sha256,
        )
        return _seal(attempt, evidence)

    def _image_receipts(self, fixture: PortablePackageFixture, retained, suite: PortableSuiteGateEvidence):
        root = fixture.root
        candidate = fixture.candidate
        image_id = "sha256:" + "a" * 64
        build_attempt = root / IMAGE_ROOT / candidate.manifest.sha256 / "build" / "attempt-mock-native"
        build_attempt.mkdir(parents=True)
        context, package_manifest = _portable_context(root, candidate, retained.view, build_attempt)
        context_sha256 = _tree(context)
        labels = {
            CANDIDATE_LABEL: candidate.manifest.sha256,
            CONTEXT_LABEL: context_sha256,
        }
        inspected = canonical_json([{"Config": {"Labels": labels}}])
        build_argv = [
            "docker", "build", "--iidfile", str(build_attempt / "image.id"),
            "--label", f"{CANDIDATE_LABEL}={candidate.manifest.sha256}",
            "--label", f"{CONTEXT_LABEL}={context_sha256}",
            "--file", str(context / "Dockerfile"), str(context),
        ]
        build_commands = canonical_json([
            {"argv": build_argv, "exit_code": 0, "timed_out": False,
             "stdout_sha256": _digest(b""), "stderr_sha256": _digest(b"")},
            {"argv": ["docker", "image", "inspect", image_id], "exit_code": 0, "timed_out": False,
             "stdout_sha256": _digest(inspected), "stderr_sha256": _digest(b"")},
        ])
        _write(build_attempt / "commands.json", build_commands)
        _write(build_attempt / "command-0.stdout", b"")
        _write(build_attempt / "command-0.stderr", b"")
        _write(build_attempt / "command-1.stdout", inspected)
        _write(build_attempt / "command-1.stderr", b"")
        common = {
            "package_schema": "portable-1",
            "package_manifest_sha256": package_manifest,
            "source_catalog_sha256": retained.view.source_catalog_sha256,
            "candidate_run_id": retained.view.candidate_run_id,
            "input_manifest_sha256": retained.view.input_manifest_sha256,
            "framework_version": retained.view.framework_version,
            "version_toml_sha256": retained.view.version_toml_sha256,
            "package_evidence_sha256": retained.receipt_sha256,
            "package_evidence_relpath": retained.receipt_path.relative_to(root).as_posix(),
        }
        build = _seal(build_attempt, PortableImageBuildEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
            outcome="built",
            reason="MOCK DATA ONLY physical build receipt",
            candidate_image_digest=image_id,
            context_root=context.relative_to(root).as_posix(),
            context_sha256=context_sha256,
            suite_receipt_sha256=suite.receipt_sha256,
            evidence_root=build_attempt.relative_to(root).as_posix(),
            commands_sha256=_digest(build_commands),
            execution_kind="docker-subprocess",
            **common,
        ))

        verify_attempt = root / IMAGE_ROOT / candidate.manifest.sha256 / "verify" / "attempt-mock-native"
        verify_attempt.mkdir(parents=True)
        report = canonical_json({
            "schema": "caprmedio.release_version.portable_image_canary.v1",
            "candidate_snapshot_manifest_sha256": candidate.manifest.sha256,
            "package_schema": retained.view.package_schema,
            "package_manifest_sha256": retained.view.actual_package_manifest_sha256,
            "source_catalog_sha256": retained.view.source_catalog_sha256,
            "candidate_run_id": retained.view.candidate_run_id,
            "input_manifest_sha256": retained.view.input_manifest_sha256,
            "framework_version": retained.view.framework_version,
            "version_toml_sha256": retained.view.version_toml_sha256,
            "verified_files": len(retained.view.member_inventory),
            "mcp_tools": ["get_mcp_reload_status"],
        })
        run_argv = [
            "docker", "run", "--rm", "--network=none", "--read-only", "--cap-drop=ALL",
            "--security-opt=no-new-privileges", "--pids-limit=128", "--tmpfs", "/tmp:rw,nosuid,nodev,size=128m",
            "--entrypoint", "python", image_id, "/opt/caprmedio-release-canary.py",
        ]
        verification_commands = canonical_json([
            {"argv": ["docker", "image", "inspect", image_id], "exit_code": 0, "timed_out": False,
             "stdout_sha256": _digest(inspected), "stderr_sha256": _digest(b"")},
            {"argv": run_argv, "exit_code": 0, "timed_out": False,
             "stdout_sha256": _digest(report), "stderr_sha256": _digest(b"")},
        ])
        _write(verify_attempt / "commands.json", verification_commands)
        _write(verify_attempt / "command-0.stdout", inspected)
        _write(verify_attempt / "command-0.stderr", b"")
        _write(verify_attempt / "command-1.stdout", report)
        _write(verify_attempt / "command-1.stderr", b"")
        verification = _seal(verify_attempt, PortableImageVerificationEvidence(
            candidate_snapshot_manifest_sha256=candidate.manifest.sha256,
            outcome="verified",
            reason="MOCK DATA ONLY physical verification receipt",
            candidate_image_digest=image_id,
            build_receipt_sha256=build.receipt_sha256,
            evidence_root=verify_attempt.relative_to(root).as_posix(),
            commands_sha256=_digest(verification_commands),
            execution_kind="docker-subprocess",
            **common,
        ))
        return build, verification

    def _archive(self):
        fixture = PortablePackageFixture(extra_engine_members=_test_members())
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        retained = retain_retained_candidate_identity(fixture.candidate, fixture.sealed, prepared)
        suite = self._suite_receipt(fixture, retained.package_evidence)
        build, verification = self._image_receipts(fixture, retained.package_evidence, suite)
        archive = Path(tempfile.mkdtemp(prefix="caprmedio-detached-image-")).resolve(strict=True) / "archive"
        shutil.copytree(fixture.root, archive)
        identity = read_retained_candidate_identity(
            archive / retained.descriptor_path.relative_to(fixture.root),
            expected_sha256=retained.descriptor_sha256,
            package_root=archive / retained.package_evidence.view.package_root.relative_to(fixture.root),
            sidecar_path=archive / retained.package_evidence.receipt_path.relative_to(fixture.root),
            expected_sidecar_sha256=retained.package_evidence.receipt_sha256,
        )
        # Managed macOS can refuse to rename compiler-read fixture roots.  A
        # post-archive source mutation establishes the same detached-reader
        # boundary without trying to clean up or move that retained fixture.
        fixture.atom_one.write_bytes(fixture.atom_one.read_bytes() + b"\nmutated after original image receipt\n")
        atom = archive / "99_source_drift" / "atom.md"
        _write(atom, b"source checkout no longer has authoritative bytes\n")
        return archive, identity, suite, build, verification

    def test_reopens_relocated_original_image_artifacts_without_live_checkout(self) -> None:
        archive, identity, suite, build, verification = self._archive()

        observed = read_detached_image_execution_artifacts(archive, identity, suite, build, verification)

        self.assertEqual(archive / verification.evidence_root, observed)
        self.assertTrue(identity.descriptor_path.is_relative_to(archive))

    def test_refuses_tampered_verification_receipt_context_member_and_suite_predecessor(self) -> None:
        variants = ("receipt", "context", "member", "predecessor")
        for variant in variants:
            with self.subTest(variant=variant):
                archive, identity, suite, build, verification = self._archive()
                if variant == "receipt":
                    (archive / verification.evidence_root / "receipt.json").write_bytes(b"tampered")
                elif variant == "context":
                    (archive / build.context_root / "canary.json").write_bytes(b"{}")
                elif variant == "member":
                    member = identity.package_evidence.view.member_inventory[0]
                    (archive / build.context_root / "PACKAGE" / member.path).write_bytes(b"tampered")
                else:
                    (archive / suite.evidence_root / "receipt.json").write_bytes(b"tampered")
                with self.assertRaises(ReleaseContractError) as raised:
                    read_detached_image_execution_artifacts(archive, identity, suite, build, verification)
                self.assertEqual("release-image-detached-suite-untrusted" if variant == "predecessor" else
                                 ("release-image-evidence-untrusted" if variant == "receipt" else "release-image-context-stale"),
                                 getattr(raised.exception, "code", None))

    def test_refuses_caller_forged_typed_candidate_and_image_facts(self) -> None:
        archive, identity, suite, build, verification = self._archive()

        with self.assertRaises(ReleaseContractError) as candidate:
            read_detached_image_execution_artifacts(
                archive, replace(identity, descriptor_sha256="0" * 64), suite, build, verification,
            )
        self.assertEqual("release-image-detached-candidate-untrusted", getattr(candidate.exception, "code", None))

        with self.assertRaises(ReleaseContractError) as package:
            read_detached_image_execution_artifacts(
                archive, replace(identity, package_evidence=object()), suite, build, verification,
            )
        self.assertEqual("release-image-detached-candidate-untrusted", getattr(package.exception, "code", None))

        with self.assertRaises(ReleaseContractError) as image:
            read_detached_image_execution_artifacts(
                archive, identity, suite, build,
                replace(verification, candidate_snapshot_manifest_sha256="0" * 64),
            )
        self.assertEqual("release-image-evidence-untrusted", getattr(image.exception, "code", None))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
