"""D597 retained schema-1 native package sidecar tests."""

from __future__ import annotations

import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = RELEASE_ROOT.parent
TEST_ROOT = Path(__file__).resolve().parent
for candidate in (TOOLS_ROOT, RELEASE_ROOT, TEST_ROOT):
    if str(candidate) not in sys.path:
        sys.path.insert(0, str(candidate))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_package_evidence import verify_bound_package_evidence  # noqa: E402
from release_portable_package import prepare_portable_release_package  # noqa: E402
from release_retained_package import (  # noqa: E402
    RetainedNativePackageError,
    read_retained_native_package_evidence,
    retain_native_package_evidence,
)
from release_test_phases import derive_test_phase_map_from_rows  # noqa: E402


def _test_members() -> dict[str, bytes]:
    root = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests"
    return {
        f"{root}/test_docker_e2e.py": b"def test_docker_e2e():\n    assert True\n",
        f"{root}/test_selected_query_mcp_e2e.py": b"def test_selected_query_mcp_e2e():\n    assert True\n",
        f"{root}/test_selected_workflows_docker_e2e.py": b"def test_selected_workflows_docker_e2e():\n    assert True\n",
        "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_retained_unit.py": b"def test_retained_unit():\n    assert True\n",
    }


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")


class RetainedNativePackageTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture(extra_engine_members=_test_members())
        self.prepared = prepare_portable_release_package(self.fixture.root, self.fixture.sealed)

    def _retained(self):
        return retain_native_package_evidence(self.fixture.candidate, self.fixture.sealed, self.prepared)

    def _detached_copy(self, retained):
        root = Path(tempfile.mkdtemp(prefix="caprmedio-retained-native-")).resolve(strict=True)
        package = root / self.prepared.package_manifest_sha256
        sidecar = root / "package_evidence" / retained.receipt_path.name
        shutil.copytree(self.prepared.package.root, package)
        sidecar.parent.mkdir()
        shutil.copyfile(retained.receipt_path, sidecar)
        return root, package, sidecar

    def _write_sidecar_variant(self, root: Path, document: dict[str, object]) -> Path:
        payload = _canonical(document)
        path = root / "package_evidence" / f"{hashlib.sha256(payload).hexdigest()}.json"
        path.write_bytes(payload)
        return path

    def test_retain_and_detached_reader_survive_current_checkout_changes(self) -> None:
        retained = self._retained()
        _root, package, sidecar = self._detached_copy(retained)

        selector = self.fixture.root / ".caprmedio_runtime/framework/current.toml"
        selector.write_bytes(b'release = "changed"\n')
        source = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        source.write_bytes(source.read_bytes() + b"changed\n")

        reopened = read_retained_native_package_evidence(
            package,
            sidecar,
            expected_sha256=retained.receipt_sha256,
        )
        self.assertEqual(reopened.receipt_sha256, retained.receipt_sha256)
        self.assertEqual(reopened.receipt_path, sidecar)
        self.assertEqual(reopened.view.actual_package_manifest_sha256, retained.view.actual_package_manifest_sha256)
        self.assertEqual(reopened.view.member_inventory, retained.view.member_inventory)
        self.assertEqual(reopened.view.phase_map, retained.view.phase_map)
        self.assertEqual(reopened.view.package_root, package)
        self.assertNotEqual(reopened.view.package_root, retained.view.package_root)

    def test_reader_refuses_tampered_digest_sidecar_projection_and_package_members(self) -> None:
        retained = self._retained()
        root, package, sidecar = self._detached_copy(retained)
        document = json.loads(sidecar.read_text(encoding="utf-8"))

        with self.assertRaises(RetainedNativePackageError) as digest:
            read_retained_native_package_evidence(package, sidecar, expected_sha256="0" * 64)
        self.assertEqual(digest.exception.code, "retained-package-sidecar-digest-mismatch")

        extra = dict(document)
        extra["unexpected"] = True
        with self.assertRaises(RetainedNativePackageError) as invalid:
            read_retained_native_package_evidence(package, self._write_sidecar_variant(root, extra))
        self.assertEqual(invalid.exception.code, "retained-package-sidecar-invalid")

        missing = dict(document)
        missing.pop("test_bindings")
        with self.assertRaises(RetainedNativePackageError) as absent:
            read_retained_native_package_evidence(package, self._write_sidecar_variant(root, missing))
        self.assertEqual(absent.exception.code, "retained-package-sidecar-invalid")

        altered_binding = json.loads(json.dumps(document))
        altered_binding["test_bindings"][0]["package_path"] = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        with self.assertRaises(RetainedNativePackageError) as mapping:
            read_retained_native_package_evidence(package, self._write_sidecar_variant(root, altered_binding))
        self.assertEqual(mapping.exception.code, "retained-package-test-projection-mismatch")

        origin_swapped = json.loads(json.dumps(document))
        left, right = origin_swapped["test_bindings"][:2]
        left["package_path"], right["package_path"] = right["package_path"], left["package_path"]
        left["sha256"], right["sha256"] = right["sha256"], left["sha256"]
        origin_swapped["phase_map_sha256"] = derive_test_phase_map_from_rows(
            tuple({"source_path": binding["source_path"], "sha256": binding["sha256"]}
                  for binding in origin_swapped["test_bindings"])
        ).sha256
        with self.assertRaises(RetainedNativePackageError) as origin:
            read_retained_native_package_evidence(package, self._write_sidecar_variant(root, origin_swapped))
        self.assertEqual(origin.exception.code, "retained-package-test-origin-mismatch")

        extra_member = package / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_extra.py"
        extra_member.write_bytes(b"def test_extra():\n    assert True\n")
        with self.assertRaises(RetainedNativePackageError) as package_extra:
            read_retained_native_package_evidence(package, sidecar)
        self.assertEqual(package_extra.exception.code, "package-extra-member")

        _missing_root, missing_package, missing_sidecar = self._detached_copy(retained)
        (missing_package / "defaults/runtime.toml").unlink()
        with self.assertRaises(RetainedNativePackageError) as package_missing:
            read_retained_native_package_evidence(missing_package, missing_sidecar)
        self.assertEqual(package_missing.exception.code, "package-member-missing")

    def test_reader_refuses_secret_or_aliased_sidecar_before_metadata_or_bytes(self) -> None:
        retained = self._retained()
        root, package, sidecar = self._detached_copy(retained)
        protected = sidecar.parent / ".env.never-read"
        with (
            mock.patch("release_retained_package.os.lstat", side_effect=AssertionError("unexpected metadata access")),
            mock.patch.object(Path, "read_bytes", side_effect=AssertionError("unexpected byte access")),
            self.assertRaises(RetainedNativePackageError) as secret,
        ):
            read_retained_native_package_evidence(package, protected)
        self.assertEqual(secret.exception.code, "release-inventory-secret-refused")

        alias = root / "sidecar-alias"
        alias.symlink_to(root, target_is_directory=True)
        aliased = alias / "package_evidence" / sidecar.name
        with mock.patch.object(Path, "read_bytes", side_effect=AssertionError("unexpected byte access")), self.assertRaises(
            RetainedNativePackageError
        ) as symlink:
            read_retained_native_package_evidence(package, aliased)
        self.assertEqual(symlink.exception.code, "retained-package-sidecar-path-invalid")

    def test_writer_requires_current_live_candidate_evidence_before_sidecar_effect(self) -> None:
        source = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        source.write_bytes(source.read_bytes() + b"changed\n")

        with self.assertRaises(RetainedNativePackageError) as stale:
            self._retained()
        self.assertEqual(stale.exception.code, "release-currentness-stale")
        candidate_root = self.fixture.root / ".caprmedio_tmp/release_candidates" / self.fixture.run_id
        self.assertFalse((candidate_root / "package_evidence").exists())

    def test_writer_revalidates_again_immediately_before_publication(self) -> None:
        source = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        calls = 0

        def stale_after_first_check(*args, **kwargs):
            nonlocal calls
            calls += 1
            result = verify_bound_package_evidence(*args, **kwargs)
            if calls == 1:
                source.write_bytes(source.read_bytes() + b"changed-after-first-check\n")
            return result

        with mock.patch("release_retained_package.verify_bound_package_evidence", side_effect=stale_after_first_check):
            with self.assertRaises(RetainedNativePackageError) as stale:
                self._retained()
        self.assertEqual(stale.exception.code, "release-currentness-stale")
        self.assertEqual(calls, 2)
        candidate_root = self.fixture.root / ".caprmedio_tmp/release_candidates" / self.fixture.run_id
        self.assertFalse((candidate_root / "package_evidence").exists())

    def test_writer_is_content_addressed_and_idempotently_reopens_exact_bytes(self) -> None:
        first = self._retained()
        second = self._retained()

        self.assertEqual(first, second)
        self.assertEqual(first.receipt_path.name, f"{first.receipt_sha256}.json")
        payload = first.receipt_path.read_bytes()
        self.assertEqual(first.receipt_sha256, hashlib.sha256(payload).hexdigest())
        document = json.loads(payload.decode("utf-8"))
        self.assertEqual(set(document), {
            "schema_version", "package_schema", "candidate_snapshot_manifest_sha256",
            "package_manifest_sha256", "source_catalog_sha256", "candidate_run_id",
            "input_manifest_sha256", "framework_version", "version_toml_sha256",
            "member_inventory", "test_bindings", "phase_map_sha256",
        })
        self.assertEqual(
            [binding["source_path"] for binding in document["test_bindings"]],
            sorted(binding["source_path"] for binding in document["test_bindings"]),
        )
        self.assertEqual(document["phase_map_sha256"], first.view.phase_map.sha256)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
