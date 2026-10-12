"""Independent physical revalidation coverage for final selected-native reads."""

from __future__ import annotations

from dataclasses import replace
import hashlib
import shutil
import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
RELEASE_ROOT = TOOLS / "RELEASE_VERSION"
RELEASE_TEST_ROOT = RELEASE_ROOT / "tests"
for path in (TOOLS, Path(__file__).resolve().parent, RELEASE_ROOT, RELEASE_TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import test_native_selected_installation as native_fixture  # noqa: E402
from installed_mcp_binding import InstalledMcpBindingError, _context  # noqa: E402
from native_selected_installation import NativeSelectedInstallationError  # noqa: E402


class NativeFinalRevalidationTests(native_fixture.NativeSelectedInstallationTests):
    """Mutate one physical final carrier per fresh selected-native fixture."""

    def test_positive_final_reader_still_reopens_every_final_carrier(self) -> None:
        selected = self._read()
        self.assertEqual(self.package.manifest_digest, selected.package_manifest_sha256)
        self.assertEqual(self.context.sha256, selected.target_project_context_sha256)

    def test_refuses_missing_actual_direct_o200_start(self) -> None:
        journal_root = self.target / self.context.control_child_relpath / "_journal"
        journal = next(journal_root.glob("*.ndjson"))
        journal.write_bytes(b"")
        with self.assertRaises(NativeSelectedInstallationError) as refused:
            self._read()
        self.assertIn("installation-command", refused.exception.code)

    def test_refuses_tampered_final_wrapper_environment_or_manifest(self) -> None:
        final = self.target / ".caprmedio_runtime/installation/generations/1"
        for name in ("wrapper", "environment.toml", "stage-manifest.toml"):
            with self.subTest(carrier=name):
                payload = (final / name).read_bytes()
                (final / name).write_bytes(payload + b"# physical final carrier drift\n")
                with self.assertRaises(NativeSelectedInstallationError):
                    self._read()
                (final / name).write_bytes(payload)

    def test_refuses_current_settings_structure_or_registry_drift(self) -> None:
        control = self.target / self.context.control_child_relpath
        for name in (
            "caprmedio_project_settings.toml",
            "project_structure.toml",
            "operators_registry.toml",
        ):
            with self.subTest(carrier=name):
                path = control / name
                payload = path.read_bytes()
                path.write_bytes(payload + b"\n# physical D600 control drift\n")
                with self.assertRaises(NativeSelectedInstallationError):
                    self._read()
                path.write_bytes(payload)

    def test_d600_reader_refuses_the_bare_control_child(self) -> None:
        bare_control = self.target / ".caprmedio_"
        shutil.copytree(self.target / self.context.control_child_relpath, bare_control)
        forged = replace(self.context, control_child_relpath=bare_control.name)
        carrier = self.target / ".caprmedio_runtime/installation/contexts" / f"{forged.sha256}.toml"
        carrier.write_bytes(forged.with_digest_toml())
        self.assertEqual(hashlib.sha256(forged.toml_bytes()).hexdigest(), forged.sha256)
        with self.assertRaises(InstalledMcpBindingError):
            _context(self.target, forged.sha256)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
