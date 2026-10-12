"""Current-layout consumer checks without Docker or publication effects."""

from __future__ import annotations

import sys
import hashlib
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace

RELEASE_ROOT = Path(__file__).resolve().parents[1]
for path in (RELEASE_ROOT.parent, RELEASE_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from release_contract import ReleaseContractError
from release_e2e_gate import _freeze_release_e2e_settings, _reopen_retained_release_e2e_settings
from release_image import CANARY, PORTABLE_CANARY, _known_canary
from release_handoff import PackageRow
from release_package_evidence import PackageMemberEvidence, _portable_phase_rows
from release_packaging import ReleasePackagingError, _destination_for
from release_retained_package import _normalized_source_path, _parse_test_bindings
from release_suite_inputs import _portable_origin


class MethodologyLayoutConsumerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.source_root = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES"
        self.export_root = ".caprmedio_tmp/release_candidates/run/export/sources"
        self.source = f"{self.export_root}/001_CORE_META_MODEL/tests/test_unit.py"
        self.origin = f"{self.source_root}/001_CORE_META_MODEL/tests/test_unit.py"
        self.compilation = SimpleNamespace(
            candidate=SimpleNamespace(manifest=SimpleNamespace(canonical_source_snapshot_ref=self.source_root)),
            private_compilation=SimpleNamespace(methodology_export=SimpleNamespace(source_export_root=self.export_root)),
            portable_package_rows=(SimpleNamespace(resource="METHODOLOGY", source_path=self.source, sha256="a" * 64),),
        )

    def test_all_portable_origins_use_sealed_snapshot_ref(self) -> None:
        self.assertEqual(_portable_origin(self.compilation, self.source, "METHODOLOGY"), self.origin)
        self.assertEqual(_normalized_source_path(self.compilation, resource="METHODOLOGY", source_path=self.source), self.origin)
        self.assertEqual(_portable_phase_rows(self.compilation)[0].source_path, self.origin)

    def test_origin_outside_sealed_private_export_is_refused(self) -> None:
        for reader in (
            lambda: _portable_origin(self.compilation, "elsewhere/test_unit.py", "METHODOLOGY"),
            lambda: _normalized_source_path(self.compilation, resource="METHODOLOGY", source_path="elsewhere/test_unit.py"),
        ):
            with self.assertRaises(ReleaseContractError):
                reader()

    def test_package_destination_uses_sealed_private_materialization(self) -> None:
        compiled = ".caprmedio_tmp/release_candidates/run/compiled"
        row = PackageRow(resource="METHODOLOGY", source_path=f"{compiled}/unit.md",
                         destination_path="METHODOLOGY/compiled/unit.md", sha256="a" * 64, mode=0o644)
        _destination_for(row, self.source_root, compiled)
        with self.assertRaises(ReleasePackagingError):
            _destination_for(row, self.source_root, "101_FRAMEWORK_METHODOLOGY/applicable_methodology")

    def test_detached_source_prefix_is_retained_not_current_registry(self) -> None:
        package = "methodology/active/001_CORE_META_MODEL/tests/test_unit.py"
        members = (PackageMemberEvidence(package, "a" * 64, 0o644, "methodology"),)
        raw = [{"source_path": self.origin, "package_path": package, "sha256": "a" * 64, "phase": "unit"}]
        self.assertEqual(_parse_test_bindings(raw, members)[0].source_path, self.origin)
        raw[0]["source_path"] = f"{self.source_root}/001_CORE_META_MODEL/tests/test_other.py"
        with self.assertRaises(ReleaseContractError):
            _parse_test_bindings(raw, members)

    def test_detached_methodology_prefixes_must_be_consistent(self) -> None:
        members = tuple(PackageMemberEvidence(f"methodology/active/tests/{name}", "a" * 64, 0o644, "methodology")
                        for name in ("test_a.py", "test_b.py"))
        raw = [{"source_path": f"{prefix}/tests/{name}", "package_path": f"methodology/active/tests/{name}",
                "sha256": "a" * 64, "phase": "unit"}
               for prefix, name in ((self.source_root, "test_a.py"), ("another/source", "test_b.py"))]
        with self.assertRaises(ReleaseContractError):
            _parse_test_bindings(raw, members)

    def test_e2e_settings_snapshot_retains_actual_source_refs(self) -> None:
        raw = b"[release_e2e]\ninspect_timeout_seconds=1\nharness_timeout_seconds=1\ncleanup_timeout_seconds=1\nmax_stdout_bytes=1024\nmax_stderr_bytes=1024\nmax_junit_bytes=1024\n"
        frozen = _freeze_release_e2e_settings(raw, b"[release_e2e]\n",
            default_settings_relative=f"{self.source_root}/defaults.toml",
            instance_settings_relative="control/000framework/caprmedio_framework_settings.toml")
        self.assertIn(self.source_root.encode(), frozen.snapshot)
        self.assertIn(b"control/000framework/caprmedio_framework_settings.toml", frozen.snapshot)

    def test_detached_e2e_settings_reopen_without_current_authoring_registry(self) -> None:
        root = Path(tempfile.mkdtemp(prefix="release-layout-retained-settings-"))
        attempt = root / ".caprmedio_runtime/release_e2e/attempt-original"
        attempt.mkdir(parents=True)
        default = b"[release_e2e]\ninspect_timeout_seconds=1\nharness_timeout_seconds=1\ncleanup_timeout_seconds=1\nmax_stdout_bytes=1024\nmax_stderr_bytes=1024\nmax_junit_bytes=1024\n"
        instance = b"[release_e2e]\n"
        frozen = _freeze_release_e2e_settings(default, instance,
            default_settings_relative=f"{self.source_root}/defaults.toml",
            instance_settings_relative="control/000framework/caprmedio_framework_settings.toml")
        for name, payload in (("release-e2e-limits.json", frozen.snapshot),
                              ("release-e2e-default-settings.toml", default),
                              ("release-e2e-instance-settings.toml", instance)):
            (attempt / name).write_bytes(payload)
        relative = attempt.relative_to(root).as_posix()
        evidence = SimpleNamespace(evidence_root=relative, settings_snapshot_path=f"{relative}/release-e2e-limits.json",
                                   settings_snapshot_sha256=hashlib.sha256(frozen.snapshot).hexdigest())
        self.assertEqual(_reopen_retained_release_e2e_settings(root, evidence), frozen.limits)
        (attempt / "release-e2e-default-settings.toml").write_bytes(default + b"changed=true\n")
        with self.assertRaises(ReleaseContractError):
            _reopen_retained_release_e2e_settings(root, evidence)

    def test_current_canaries_have_explicit_isolated_source_not_installed_source(self) -> None:
        for canary in (CANARY, PORTABLE_CANARY):
            self.assertIn(".caprmedio_caprmedio/methodology_sources", canary)
            self.assertNotIn("000_APPLICABLE_MTHD_sources", canary)
            self.assertTrue(_known_canary(canary.encode()))


if __name__ == "__main__":
    unittest.main()
