"""Detached D597 native E2E artifact-reader coverage.

The fixture writes receipt-shaped proof packets without running Docker or a
host harness.  The readers under test are real retained readers; no verifier
or package/selector binding is replaced by a mock.
"""

from __future__ import annotations

from dataclasses import asdict, replace
import hashlib
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for _path in (RELEASE_ROOT, TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

import release_e2e_gate as gate  # noqa: E402
from release_contract import ReleaseContractError, canonical_json  # noqa: E402
from release_handoff import CURRENT_SELECTOR_RELATIVE  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_candidate import (  # noqa: E402
    read_retained_candidate_identity,
    retain_retained_candidate_identity,
)
import test_detached_native_image as image_fixtures  # noqa: E402
from test_portable_release_e2e_gate import _write_retained_n  # noqa: E402
from portable_package_fixture import PortablePackageFixture  # noqa: E402


def _digest(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _write(path: Path, payload: bytes, mode: int = 0o644) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(payload)
    path.chmod(mode)


def _seal(attempt: Path, evidence):
    payload = canonical_json(asdict(evidence))
    _write(attempt / "receipt.json", payload)
    return replace(evidence, receipt_sha256=_digest(payload))


class DetachedNativeE2EReaderTests(unittest.TestCase):
    def _seed_e2e(self, root: Path, candidate, retained, suite, image):
        """Write a complete packet whose absolute paths are rooted at ``root``."""

        _write_retained_n(SimpleNamespace(root=root, candidate=candidate))
        grammar_raw = (RELEASE_ROOT / "release_e2e_bindings.json").read_bytes()
        _write(root / gate.GRAMMAR_RELATIVE, grammar_raw)
        grammar = gate._parse_grammar(grammar_raw)
        phase_map = retained.package_evidence.view.phase_map
        parent = root / gate.EVIDENCE_ROOT / retained.candidate_snapshot_manifest_sha256
        attempt = parent / "attempt-detached-native"
        reports = attempt / "scratch" / "reports"
        reports.mkdir(parents=True)
        evidence_root = attempt.relative_to(root).as_posix()
        default_settings = b"""[release_e2e]
inspect_timeout_seconds = 1.0
harness_timeout_seconds = 1.0
cleanup_timeout_seconds = 1.0
max_stdout_bytes = 1024
max_stderr_bytes = 1024
max_junit_bytes = 1024
"""
        frozen = gate._freeze_release_e2e_settings(default_settings, b"[release_e2e]\n")
        _write(attempt / "release-e2e-limits.json", frozen.snapshot)
        _write(attempt / "release-e2e-grammar.json", grammar_raw)
        _write(attempt / "release-e2e-default-settings.toml", default_settings)
        _write(attempt / "release-e2e-instance-settings.toml", b"[release_e2e]\n")
        state = gate._active_n_state(root, candidate)
        controller = root / gate.RUNTIME_ROOT / "releases" / candidate.authority.executing_release / gate._N_DRIVER_RELATIVE
        executable = Path(sys.executable).resolve()
        controller_sha256 = _digest(controller.read_bytes())
        executable_sha256 = _digest(executable.read_bytes())
        capability = gate.FrozenHostE2ECapability(
            *state,
            gate.ExecutableIdentity("n_host_controller", str(controller), controller_sha256),
            gate.ExecutableIdentity("python", str(executable), executable_sha256),
            gate.ExecutableIdentity("driver", str(controller), controller_sha256),
            gate.ExecutableIdentity("docker", str(executable), executable_sha256),
            str(executable.parent),
        )
        capability_payload = gate._host_identities_bytes(capability)
        _write(attempt / "host-identities.json", capability_payload)
        context, harnesses = gate._context_bytes_for_binding(
            root, attempt / "scratch", reports, retained.candidate_snapshot_manifest_sha256,
            image.candidate_image_digest, _digest(grammar_raw), phase_map.sha256, grammar,
        )
        _write(attempt / "scratch" / "context.json", context)
        _write(attempt / "inspect.stdout.bin", (image.candidate_image_digest + "\n").encode())
        _write(attempt / "inspect.stderr.bin", b"")
        source_sha256s = {
            path: digest for path, digest, phase in phase_map.rows if phase == "candidate_e2e"
        }
        junit = b"<testsuite tests='1' failures='0' errors='0' skipped='0'><testcase name='ok'/></testsuite>"
        receipts = []
        for index, (row, harness) in enumerate(zip(grammar["harnesses"], harnesses, strict=True)):
            pattern = Path(row["source_path"]).name
            stdout, stderr = f"MOCK DATA ONLY harness {index}\n".encode(), b""
            stdout_path = f"{evidence_root}/harness-{index}.stdout.bin"
            stderr_path = f"{evidence_root}/harness-{index}.stderr.bin"
            junit_path = f"{evidence_root}/harness-{index}.junit.xml"
            _write(attempt / f"harness-{index}.stdout.bin", stdout)
            _write(attempt / f"harness-{index}.stderr.bin", stderr)
            _write(attempt / f"harness-{index}.junit.xml", junit)
            receipts.append(gate.HarnessReceipt(
                row["source_path"], source_sha256s[row["source_path"]],
                (str(executable), str(controller), *row["argv"][2:7], str((reports / f"{pattern}.xml").resolve())),
                "2026-10-10T00:00:00.000000Z", "2026-10-10T00:00:01.000000Z", 0, False,
                stdout_path, _digest(stdout), stderr_path, _digest(stderr),
                junit_path, _digest(junit), 1, 1.0, "",
            ))
        evidence = gate.PortableCandidateE2EGateEvidence(
            candidate_snapshot_manifest_sha256=retained.candidate_snapshot_manifest_sha256,
            candidate_image_digest=image.candidate_image_digest,
            phase_map_sha256=phase_map.sha256,
            grammar_sha256=_digest(grammar_raw),
            outcome="passed",
            reason="MOCK DATA ONLY detached physical E2E receipt",
            harness_receipts=tuple(receipts),
            evidence_root=evidence_root,
            receipt_sha256=None,
            settings_snapshot_path=f"{evidence_root}/release-e2e-limits.json",
            settings_snapshot_sha256=frozen.sha256,
            host_capability_path=f"{evidence_root}/host-identities.json",
            host_capability_sha256=_digest(capability_payload),
            execution_kind="host-subprocess",
            package_schema="portable-1",
            package_manifest_sha256=retained.package_evidence.view.actual_package_manifest_sha256,
            package_evidence_sha256=retained.package_evidence.receipt_sha256,
            package_evidence_relpath=retained.package_evidence.receipt_path.relative_to(root).as_posix(),
            source_catalog_sha256=retained.package_evidence.view.source_catalog_sha256,
            candidate_run_id=retained.package_evidence.view.candidate_run_id,
            input_manifest_sha256=retained.package_evidence.view.input_manifest_sha256,
            framework_version=retained.framework_version,
            version_toml_sha256=retained.version_toml_sha256,
        )
        return _seal(attempt, evidence)

    def _archive(self):
        fixture = PortablePackageFixture(extra_engine_members=image_fixtures._test_members())
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        original = retain_retained_candidate_identity(fixture.candidate, fixture.sealed, prepared)
        archive = Path(tempfile.mkdtemp(prefix="caprmedio-detached-e2e-", dir="/private/tmp")).resolve(strict=True) / "archive"
        shutil.copytree(fixture.root, archive)
        retained = read_retained_candidate_identity(
            archive / original.descriptor_path.relative_to(fixture.root),
            expected_sha256=original.descriptor_sha256,
            package_root=archive / original.package_evidence.view.package_root.relative_to(fixture.root),
            sidecar_path=archive / original.package_evidence.receipt_path.relative_to(fixture.root),
            expected_sidecar_sha256=original.package_evidence.receipt_sha256,
        )
        archived_fixture = SimpleNamespace(root=archive, candidate=fixture.candidate)
        image_fixture = image_fixtures.DetachedNativeImageReaderTests(methodName="runTest")
        suite = image_fixture._suite_receipt(archived_fixture, retained.package_evidence)
        _write_retained_n(archived_fixture)
        state = gate._active_n_state(archive, fixture.candidate)
        suite = _seal(
            archive / suite.evidence_root,
            replace(
                suite,
                executing_selector_sha256=state[0],
                executing_release_package_sha256=state[1],
                executing_skill_sha256=state[2],
                receipt_sha256=None,
            ),
        )
        build, verification = image_fixture._image_receipts(archived_fixture, retained.package_evidence, suite)
        e2e = self._seed_e2e(archive, fixture.candidate, retained, suite, verification)

        # The original checkout can drift after evidence retention; detached
        # readers may not use it as either their root or their currentness proof.
        fixture.atom_one.write_bytes(fixture.atom_one.read_bytes() + b"\nsource changed after retained proof\n")
        (fixture.root / CURRENT_SELECTOR_RELATIVE).write_bytes(b'release = "N+1"\n')
        return archive, retained, suite, build, verification, e2e

    def _unchanged_original_packet_archive(self):
        """Copy a packet after it was recorded, without resealing any E2E bytes."""

        fixture = PortablePackageFixture(extra_engine_members=image_fixtures._test_members())
        prepared = prepare_portable_release_package(fixture.root, fixture.sealed)
        original = retain_retained_candidate_identity(fixture.candidate, fixture.sealed, prepared)
        source_fixture = SimpleNamespace(root=fixture.root, candidate=fixture.candidate)
        image_fixture = image_fixtures.DetachedNativeImageReaderTests(methodName="runTest")
        suite = image_fixture._suite_receipt(source_fixture, original.package_evidence)
        _write_retained_n(source_fixture)
        state = gate._active_n_state(fixture.root, fixture.candidate)
        suite = _seal(
            fixture.root / suite.evidence_root,
            replace(
                suite,
                executing_selector_sha256=state[0],
                executing_release_package_sha256=state[1],
                executing_skill_sha256=state[2],
                receipt_sha256=None,
            ),
        )
        build, verification = image_fixture._image_receipts(source_fixture, original.package_evidence, suite)
        e2e = self._seed_e2e(fixture.root, fixture.candidate, original, suite, verification)
        archive = Path(tempfile.mkdtemp(prefix="caprmedio-copied-e2e-", dir="/private/tmp")).resolve(strict=True) / "archive"
        shutil.copytree(fixture.root, archive)
        retained = read_retained_candidate_identity(
            archive / original.descriptor_path.relative_to(fixture.root),
            expected_sha256=original.descriptor_sha256,
            package_root=archive / original.package_evidence.view.package_root.relative_to(fixture.root),
            sidecar_path=archive / original.package_evidence.receipt_path.relative_to(fixture.root),
            expected_sidecar_sha256=original.package_evidence.receipt_sha256,
        )
        fixture.atom_one.write_bytes(fixture.atom_one.read_bytes() + b"\nsource changed after original packet copy\n")
        (fixture.root / CURRENT_SELECTOR_RELATIVE).write_bytes(b'release = "N+1"\n')
        return archive, retained, suite, build, verification, e2e

    def _read(self, archive, retained, suite, build, verification, e2e):
        return gate.read_detached_candidate_e2e_execution_artifacts(
            archive, retained, suite, verification, e2e, image_build=build,
        )

    def test_reopens_detached_packet_after_live_source_and_selector_drift(self) -> None:
        archive, retained, suite, build, verification, e2e = self._archive()

        self.assertEqual(archive, self._read(archive, retained, suite, build, verification, e2e))

    def test_reopens_unchanged_original_packet_after_archive_copy(self) -> None:
        archive, retained, suite, build, verification, e2e = self._unchanged_original_packet_archive()

        self.assertEqual(archive, self._read(archive, retained, suite, build, verification, e2e))

    def test_refuses_mismatched_predecessors_and_packet_tampering(self) -> None:
        variants = (
            "sidecar", "version", "image", "host-capability", "report", "grammar", "settings",
        )
        for variant in variants:
            with self.subTest(variant=variant):
                archive, retained, suite, build, verification, e2e = self._archive()
                if variant == "sidecar":
                    e2e = replace(e2e, package_evidence_sha256="0" * 64)
                elif variant == "version":
                    e2e = replace(e2e, framework_version="N-tampered")
                elif variant == "image":
                    e2e = replace(e2e, candidate_image_digest="sha256:" + "0" * 64)
                elif variant == "host-capability":
                    (archive / e2e.host_capability_path).write_bytes(b"tampered")
                elif variant == "report":
                    (archive / e2e.harness_receipts[0].junit_path).write_bytes(b"<testsuite/>")
                elif variant == "grammar":
                    (archive / e2e.evidence_root / "release-e2e-grammar.json").write_bytes(b"{}")
                else:
                    (archive / e2e.evidence_root / "release-e2e-default-settings.toml").write_bytes(b"[release_e2e]\nmax_stdout_bytes = 1\n")
                with self.assertRaises(ReleaseContractError):
                    self._read(archive, retained, suite, build, verification, e2e)

    def test_refuses_raw_identity_and_a_root_that_does_not_anchor_its_references(self) -> None:
        archive, retained, suite, build, verification, e2e = self._archive()

        with self.assertRaises(ReleaseContractError):
            self._read(archive, object(), suite, build, verification, e2e)  # type: ignore[arg-type]
        with self.assertRaises(ReleaseContractError):
            self._read(archive.parent, retained, suite, build, verification, e2e)

    def test_rejects_external_identity_paths_before_any_retained_reopen(self) -> None:
        archive, retained, suite, build, verification, e2e = self._archive()
        external = replace(retained, descriptor_path=archive.parent / "foreign" / "candidate-snapshot.json")

        # This is a fail-fast guard, not a substituted verifier: an external
        # path must be rejected by lexical root binding before any physical
        # retained-identity read could be attempted.
        with mock.patch.object(
            gate,
            "reopen_retained_candidate_identity",
            side_effect=AssertionError("external identity was reopened"),
        ):
            with self.assertRaises(ReleaseContractError) as raised:
                self._read(archive, external, suite, build, verification, e2e)
        self.assertEqual("release-e2e-retained-candidate-root-mismatch", raised.exception.code)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
