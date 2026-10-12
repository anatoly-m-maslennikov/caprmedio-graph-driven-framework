"""Read-only preparation checks; fixtures establish no live release receipt."""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
for path in (RELEASE_ROOT, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import release_version as native  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import CANONICAL_SOURCE_RELATIVE, tree_sha256  # noqa: E402
from release_suite import SUPPORTED_RUNNER, SUITE_DRIVER_COMMAND, SUITE_DRIVER_WORKING_DIRECTORY  # noqa: E402
import test_methodology_export_handoff as export_fixture  # noqa: E402


class ReleasePreparationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = export_fixture.MethodologyExportHandoffTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.structure = self.fixture.write(".caprmedio_caprmedio/project_structure.toml", (
            '[[scope_units]]\nscope_unit_name = "FRAMEWORK_METHODOLOGY"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY"\n'
            '[[scope_units]]\nscope_unit_name = "METHODOLOGY_SOURCES"\n'
            'parent = "FRAMEWORK_METHODOLOGY"\n'
            f'authority_path = "{CANONICAL_SOURCE_RELATIVE}"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/sources"\n'
            '[[scope_units]]\nscope_unit_name = "APPLICABLE_METHODOLOGY"\n'
            'parent = "FRAMEWORK_METHODOLOGY"\n'
            'delivery_path = "101_FRAMEWORK_METHODOLOGY/applicable_methodology"\n'
        ).encode())
        self.settings = self.fixture.write(
            ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml", b""
        )
        self.fixture.write("101_FRAMEWORK_METHODOLOGY/prior.md", b"prior product\n")
        self.fixture.write(".agents/skills/ca/SKILL.md", b"prior skill\n")
        self.minimal = {"operation": "apply", "project_root": str(self.root)}

    def snapshot(self) -> dict[str, tuple[bytes, int]]:
        return {
            path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mode & 0o777)
            for path in self.root.rglob("*") if path.is_file()
        }

    def test_minimal_request_seals_actual_authority_without_writes_or_fake_receipts(self) -> None:
        before = self.snapshot()
        prepared = native.prepare_release_request(self.root, self.minimal)
        parsed = native.ReleaseVersionRequest.model_validate(prepared)
        manifest = parsed.candidate_snapshot_manifest
        self.assertEqual((parsed.operation, manifest.executing_release, manifest.framework_version), ("apply", "N", "N+1"))
        self.assertEqual(parsed.run_receipt_refs, [])
        self.assertEqual(manifest.canonical_source_snapshot_digest, tree_sha256(self.root, self.fixture.source))
        methodology = {row.source_path: (row.source_sha256, row.source_mode)
                       for row in manifest.source_inventory_rows if row.resource == "METHODOLOGY"}
        observed_sources = {
            path.relative_to(self.root).as_posix(): (hashlib.sha256(path.read_bytes()).hexdigest(), path.stat().st_mode & 0o777)
            for path in self.fixture.source.rglob("*") if path.is_file()
        }
        self.assertEqual(methodology, observed_sources)
        self.assertIn(self.fixture.atom.relative_to(self.root).as_posix(), methodology)
        self.assertEqual(manifest.full_suite_environment.model_dump(mode="json"), {
            "runner": SUPPORTED_RUNNER, "command": list(SUITE_DRIVER_COMMAND),
            "working_directory": SUITE_DRIVER_WORKING_DIRECTORY,
        })
        self.assertEqual(manifest.candidate_image.candidate_image_reference,
                         f"caprmedio-release:n-1-{manifest.canonical_source_snapshot_digest[:16]}")
        for path, observed in ((self.structure, manifest.project_structure_digest),
                               (self.settings, manifest.framework_settings_digest),
                               (self.root / "version.toml", manifest.version_toml_sha256)):
            self.assertEqual(observed, hashlib.sha256(path.read_bytes()).hexdigest())
        self.assertTrue(manifest.expected_derived_source_copy_sha256)
        self.assertTrue(manifest.expected_compiled_output_sha256)
        self.assertEqual(native.validate_prepared_release_request(self.root, prepared), parsed)
        self.assertEqual(self.snapshot(), before)
        self.assertFalse((self.root / ".caprmedio_tmp").exists())
        self.assertFalse((self.root / "101_FRAMEWORK_METHODOLOGY/sources").exists())
        self.assertFalse((self.root / "101_FRAMEWORK_METHODOLOGY/applicable_methodology").exists())
        result = native.release_version(parsed)
        self.assertEqual(result.outcome, "blocked")
        self.assertEqual((result.attempted_effects, result.gate_evidence_refs, result.image_refs, result.run_receipt_refs), ([], [], [], []))

    def test_prepared_request_rejects_live_source_version_structure_and_settings_drift(self) -> None:
        prepared = native.prepare_release_request(self.root, self.minimal)
        for path, changed in ((self.fixture.atom, export_fixture.carrier("CA-R-001") + b"changed\n"),
                              (self.root / "version.toml", b'[framework]\nversion = "N+2"\n'),
                              (self.structure, self.structure.read_bytes() + b"# changed structure\n"),
                              (self.settings, b"# changed settings\n")):
            with self.subTest(path=path.relative_to(self.root).as_posix()):
                original = path.read_bytes()
                path.write_bytes(changed)
                before = self.snapshot()
                with self.assertRaises(ReleaseContractError):
                    native.validate_prepared_release_request(self.root, prepared)
                self.assertEqual(self.snapshot(), before)
                path.write_bytes(original)

    def test_minimal_request_refuses_authority_overrides_and_wrong_candidate_version(self) -> None:
        before = self.snapshot()
        for extra in ({"candidate_version": "N+2"}, {"source_root": "other"},
                      {"expected_source_frontier_digest": "a" * 64},
                      {"run_receipt_refs": ["made-up-receipt"]},
                      {"full_suite_environment": {"command": ["true"]}},
                      {"candidate_image_reference": "caller:override"}):
            with self.subTest(extra=extra), self.assertRaises(ReleaseContractError):
                native.prepare_release_request(self.root, {**self.minimal, **extra})
        self.assertEqual(self.snapshot(), before)

    def test_prepared_request_rejects_project_root_substitution(self) -> None:
        prepared = native.prepare_release_request(self.root, self.minimal)
        prepared["project_root"] = str(self.root.parent)
        with self.assertRaises(ReleaseContractError):
            native.validate_prepared_release_request(self.root, prepared)

    def test_preparation_and_revalidation_pass_actual_selected_native_proof_to_builders(self) -> None:
        # A wiring test only: the sentinel is never admitted as an installation
        # or Full Gate fact. The manifest came from the real read-only fixture.
        prepared = native.prepare_release_request(self.root, self.minimal)
        manifest = native.ReleaseVersionRequest.model_validate(prepared).candidate_snapshot_manifest
        proof = object()
        with patch("release_promotion.bind_selected_native_n_from_checkpoint", return_value=proof) as bind, \
             patch("release_compilation.build_preflight_validated_candidate",
                   return_value=(object(), SimpleNamespace(manifest=manifest))) as build:
            self.assertEqual(native.prepare_release_request(self.root, self.minimal), prepared)
        bind.assert_called_once_with(self.root)
        self.assertIs(build.call_args.kwargs["native_installed_n"], proof)
        with patch("release_promotion.bind_selected_native_n_from_checkpoint", return_value=proof) as bind, \
             patch("release_version._locally_observed_candidate") as revalidate:
            parsed = native.validate_prepared_release_request(self.root, prepared)
        bind.assert_called_once_with(self.root)
        revalidate.assert_called_once_with(parsed, native_installed_n=proof)


if __name__ == "__main__":
    unittest.main()
