"""D597@4 retained candidate descriptor boundary tests."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from unittest import mock


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
TEST_ROOT = Path(__file__).resolve().parent
for _path in (TOOLS_ROOT, RELEASE_ROOT, TEST_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_contract import candidate_snapshot_manifest_sha256, canonical_json  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_candidate import (  # noqa: E402
    RetainedCandidateError,
    encode_retained_candidate_descriptor,
    read_retained_candidate_identity,
    reopen_retained_candidate_identity,
    retain_retained_candidate_identity,
)
from release_retained_package import (  # noqa: E402
    read_retained_native_package_evidence,
    retain_native_package_evidence,
)
from release_test_phases import CANDIDATE_E2E_MODULES  # noqa: E402


def _test_members() -> dict[str, bytes]:
    members = {
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_retained_candidate_unit.py": (
            b"def test_retained_candidate_unit():\n    assert True\n"
        ),
    }
    members.update({
        path: f"def test_{Path(path).stem}():\n    assert True\n".encode()
        for path in CANDIDATE_E2E_MODULES
    })
    return members


class RetainedCandidateDescriptorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture(extra_engine_members=_test_members())
        self.prepared = prepare_portable_release_package(self.fixture.root, self.fixture.sealed)
        self.retained = retain_native_package_evidence(self.fixture.candidate, self.fixture.sealed, self.prepared)

    def _detached(self) -> tuple[Path, Path, Path, object]:
        root = Path(tempfile.mkdtemp(prefix="caprmedio-retained-candidate-")).resolve(strict=True)
        package = root / self.prepared.package_manifest_sha256
        sidecar = root / "package_evidence" / self.retained.receipt_path.name
        descriptor = root / "candidate-snapshot.json"
        shutil.copytree(self.prepared.package.root, package)
        sidecar.parent.mkdir()
        shutil.copyfile(self.retained.receipt_path, sidecar)
        descriptor.write_bytes(encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
        reopened = read_retained_native_package_evidence(
            package,
            sidecar,
            expected_sha256=self.retained.receipt_sha256,
        )
        return descriptor, package, sidecar, reopened

    def _read(self, descriptor: Path, package: Path, sidecar: Path, *, expected: str | None = None, sidecar_expected: str | None = None):
        return read_retained_candidate_identity(
            descriptor,
            expected_sha256=hashlib.sha256(descriptor.read_bytes()).hexdigest() if expected is None else expected,
            package_root=package,
            sidecar_path=sidecar,
            expected_sidecar_sha256=(hashlib.sha256(sidecar.read_bytes()).hexdigest()
                                     if sidecar_expected is None else sidecar_expected),
        )

    def test_canonical_round_trip_keeps_raw_and_self_excluding_identities_distinct(self) -> None:
        descriptor, package, sidecar, _reopened = self._detached()
        raw = descriptor.read_bytes()
        identity = self._read(descriptor, package, sidecar)

        self.assertEqual(raw, encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
        self.assertEqual(identity.descriptor, self.fixture.candidate.manifest)
        self.assertEqual(identity.descriptor_sha256, hashlib.sha256(raw).hexdigest())
        self.assertEqual(identity.candidate_snapshot_manifest_sha256, self.fixture.candidate.manifest.sha256)
        self.assertNotEqual(identity.descriptor_sha256, identity.candidate_snapshot_manifest_sha256)
        self.assertEqual(identity.framework_version, self.retained.view.framework_version)
        self.assertEqual(identity.version_toml_sha256, self.retained.view.version_toml_sha256)

    def test_reopen_identity_rejects_forged_transport_fields(self) -> None:
        descriptor, package, sidecar, _reopened = self._detached()
        identity = self._read(descriptor, package, sidecar)

        self.assertEqual(identity, reopen_retained_candidate_identity(identity))
        with self.assertRaises(RetainedCandidateError) as digest:
            reopen_retained_candidate_identity(replace(identity, descriptor_sha256="0" * 64))
        self.assertEqual("retained-candidate-descriptor-digest-mismatch", digest.exception.code)

        with self.assertRaises(RetainedCandidateError) as nested:
            reopen_retained_candidate_identity(replace(identity, package_evidence=object()))
        self.assertEqual("retained-candidate-identity-untrusted", nested.exception.code)

    def test_reader_refuses_duplicate_unknown_noncanonical_malformed_and_image_input_drift(self) -> None:
        descriptor, package, sidecar, _reopened = self._detached()

        variants = {
            "duplicate": b'{"schema":"one","schema":"two"}',
            "noncanonical": descriptor.read_bytes() + b"\n",
            "malformed": b"{",
        }
        for name, raw in variants.items():
            with self.subTest(name=name):
                descriptor.write_bytes(raw)
                with self.assertRaises(RetainedCandidateError) as raised:
                    self._read(descriptor, package, sidecar)
                self.assertIn(raised.exception.code, {
                    "retained-candidate-descriptor-invalid",
                    "retained-candidate-descriptor-noncanonical",
                })

        unknown = json.loads(encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
        unknown["unexpected"] = True
        descriptor.write_bytes(canonical_json(unknown))
        with self.assertRaises(RetainedCandidateError) as raised:
            self._read(descriptor, package, sidecar)
        self.assertEqual("retained-candidate-descriptor-invalid", raised.exception.code)

        image_drift = json.loads(encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
        image = next(row for row in image_drift["source_inventory_rows"] if row["resource"] == "IMAGE_INPUT")
        image["source_sha256"] = "0" * 64
        image_drift["sha256"] = candidate_snapshot_manifest_sha256(image_drift)
        descriptor.write_bytes(canonical_json(image_drift))
        with self.assertRaises(RetainedCandidateError) as raised:
            self._read(descriptor, package, sidecar)
        self.assertEqual("retained-candidate-package-mismatch", raised.exception.code)

        reordered = json.loads(encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
        reordered["source_inventory_rows"].reverse()
        reordered["sha256"] = candidate_snapshot_manifest_sha256(reordered)
        descriptor.write_bytes(canonical_json(reordered))
        with self.assertRaises(RetainedCandidateError) as raised:
            self._read(descriptor, package, sidecar)
        self.assertEqual("retained-candidate-descriptor-noncanonical", raised.exception.code)

        descriptor.write_bytes(b"x" * (8 * 1024 * 1024 + 1))
        with self.assertRaises(RetainedCandidateError) as raised:
            self._read(descriptor, package, sidecar)
        self.assertEqual("retained-candidate-descriptor-oversized", raised.exception.code)

    def test_reader_reopens_physical_sidecar_and_refuses_missing_or_mismatched_sidecar(self) -> None:
        descriptor, package, sidecar, reopened = self._detached()
        identity = self._read(descriptor, package, sidecar)
        self.assertEqual(identity.package_evidence, reopened)

        with self.assertRaises(RetainedCandidateError) as missing:
            self._read(
                descriptor,
                package,
                sidecar.parent / "missing.json",
                sidecar_expected=self.retained.receipt_sha256,
            )
        self.assertEqual("retained-package-sidecar-unavailable", missing.exception.code)

        with self.assertRaises(RetainedCandidateError) as mismatch:
            self._read(descriptor, package, sidecar, sidecar_expected="0" * 64)
        self.assertEqual("retained-package-sidecar-digest-mismatch", mismatch.exception.code)

    def test_reader_refuses_secret_and_symlink_descriptor_paths_before_byte_reads(self) -> None:
        descriptor, package, sidecar, _reopened = self._detached()
        secret = descriptor.parent / ".env-candidate-snapshot.json"
        with (
            mock.patch("release_retained_candidate.os.lstat", side_effect=AssertionError("unexpected metadata access")),
            mock.patch.object(Path, "read_bytes", side_effect=AssertionError("unexpected byte access")),
            self.assertRaises(RetainedCandidateError) as raised,
        ):
            self._read(
                secret,
                package,
                sidecar,
                expected="0" * 64,
                sidecar_expected=self.retained.receipt_sha256,
            )
        self.assertEqual("release-inventory-secret-refused", raised.exception.code)

        descriptor.rename(descriptor.parent / "descriptor-real.json")
        descriptor.symlink_to(descriptor.parent / "descriptor-real.json")
        with self.assertRaises(RetainedCandidateError) as raised:
            self._read(descriptor, package, sidecar)
        self.assertEqual("retained-candidate-descriptor-path-invalid", raised.exception.code)

    def test_reader_refuses_descriptor_replacement_and_growth_after_open(self) -> None:
        descriptor, package, sidecar, _reopened = self._detached()
        expected = hashlib.sha256(descriptor.read_bytes()).hexdigest()
        native_read = os.read
        replaced = False

        def replace_after_open(descriptor_fd: int, count: int) -> bytes:
            nonlocal replaced
            payload = native_read(descriptor_fd, count)
            if not replaced:
                replaced = True
                replacement = descriptor.parent / "replacement.json"
                replacement.write_bytes(encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
                replacement.replace(descriptor)
            return payload

        with mock.patch("release_retained_candidate.os.read", side_effect=replace_after_open):
            with self.assertRaises(RetainedCandidateError) as raised:
                self._read(
                    descriptor,
                    package,
                    sidecar,
                    expected=expected,
                    sidecar_expected=self.retained.receipt_sha256,
                )
        self.assertEqual("retained-candidate-descriptor-path-invalid", raised.exception.code)

        descriptor.write_bytes(encode_retained_candidate_descriptor(self.fixture.candidate.manifest))
        expected = hashlib.sha256(descriptor.read_bytes()).hexdigest()
        grew = False

        def grow_after_open(descriptor_fd: int, count: int) -> bytes:
            nonlocal grew
            if not grew:
                grew = True
                with descriptor.open("ab") as stream:
                    stream.write(b"x" * (8 * 1024 * 1024))
            return native_read(descriptor_fd, count)

        with mock.patch("release_retained_candidate.os.read", side_effect=grow_after_open):
            with self.assertRaises(RetainedCandidateError) as raised:
                self._read(
                    descriptor,
                    package,
                    sidecar,
                    expected=expected,
                    sidecar_expected=self.retained.receipt_sha256,
                )
        self.assertEqual("retained-candidate-descriptor-oversized", raised.exception.code)

    def test_explicit_retention_and_detached_read_need_no_source_checkout(self) -> None:
        identity = retain_retained_candidate_identity(self.fixture.candidate, self.fixture.sealed, self.prepared)
        self.assertEqual(identity.descriptor_path.name, "candidate-snapshot.json")

        descriptor, package, sidecar, _reopened = self._detached()
        self.assertNotEqual(descriptor.parent, self.fixture.root)
        source = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        source.unlink()
        self.assertFalse(source.exists())
        detached = self._read(descriptor, package, sidecar)
        self.assertEqual(detached.descriptor_sha256, hashlib.sha256(descriptor.read_bytes()).hexdigest())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
