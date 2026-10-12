"""Actual D600 control currentness, independent of any Full Gate assertion."""

from __future__ import annotations

from dataclasses import replace
from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
for path in (TOOLS, TOOLS / "tests"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import test_portable_runtime_materialization as fixtures
from framework_installation import (
    InstallationError,
    PortableInstallationRequest,
    _reopen_prospective_target_context,
    verify_prospective_portable_full_gate,
)
from framework_package import verify_current_package_selector
from target_methodology_selection import FRAMEWORK_INSTANCE_SETTINGS_RELATIVE
from installation_context import TargetProjectRequest


class ProspectiveContextCurrentnessTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.PortableRuntimeMaterializationTests("runTest")
        self.fixture.setUp()
        self.request = PortableInstallationRequest(
            target=TargetProjectRequest(
                target_root=self.fixture.target,
                control_child=self.fixture.control.name,
                mode=self.fixture.context.mode,
                target_project_identity=self.fixture.context.target_project_identity,
                settings_path=self.fixture.control / "caprmedio_project_settings.toml",
                project_structure_path=self.fixture.control / "project_structure.toml",
                operators_registry_path=self.fixture.control / "operators_registry.toml",
                repository_identity=self.fixture.context.repository_identity,
                root_locator=self.fixture.context.root_locator,
                package_root=self.fixture.package.root,
                package_evidence=self.fixture.package_evidence,
            ),
            retained_gate_receipt_path=self.fixture.target / "not-a-gate.json",
        )

    def read(self, context=None):
        return _reopen_prospective_target_context(
            self.request, self.fixture.context if context is None else context,
        )

    def test_current_full_context_reopens(self):
        self.assertEqual(self.fixture.context, self.read())

    def test_invalid_nested_target_has_stable_refusal(self):
        with self.assertRaises(InstallationError) as refused:
            _reopen_prospective_target_context(replace(self.request, target=None), self.fixture.context)
        self.assertEqual("portable-context-invalid", refused.exception.code)

    def test_first_preparation_rebinds_before_context_persistence(self):
        carrier = self.fixture.target / ".caprmedio_runtime/installation/contexts" / f"{self.fixture.context.sha256}.toml"
        carrier.rename(self.fixture.base / "retained-context.toml")
        selector = self.fixture.target / ".caprmedio_install/current.toml"
        selector.rename(self.fixture.base / "retained-selector.toml")
        self.assertEqual(self.fixture.context, self.read())

    def test_caller_built_selection_context_refused(self):
        self.assertGreater(len(self.fixture.context.methodology_source_identities), 1)
        forged = replace(self.fixture.context,
                         methodology_source_identities=self.fixture.context.methodology_source_identities[:-1])
        self.assertNotEqual(self.fixture.context.sha256, forged.sha256)
        with self.assertRaises(InstallationError):
            self.read(forged)

    def test_framework_settings_registry_and_other_control_drift_refused(self):
        for relative in (
            FRAMEWORK_INSTANCE_SETTINGS_RELATIVE,
            Path("operators_registry.toml"),
            Path("caprmedio_project_settings.toml"),
            Path("project_structure.toml"),
        ):
            path = self.fixture.control / relative
            payload = path.read_bytes()
            with self.subTest(control=relative):
                path.write_bytes(payload + b"\n# bound control changed\n")
                try:
                    with self.assertRaises(InstallationError):
                        self.read()
                finally:
                    path.write_bytes(payload)

    def test_missing_bound_framework_settings_refused(self):
        path = self.fixture.control / FRAMEWORK_INSTANCE_SETTINGS_RELATIVE
        moved = path.with_name("retained-settings.toml")
        path.rename(moved)
        with self.assertRaises(InstallationError):
            self.read()

    def verify(self, context):
        selector = verify_current_package_selector(
            (self.fixture.target / ".caprmedio_install/current.toml").read_bytes(),
            self.fixture.package,
        )
        return verify_prospective_portable_full_gate(
            self.request, package=self.fixture.package, target_context=context, selector=selector,
        )

    def test_public_gate_boundary_rejects_forged_context_before_gate(self):
        forged = replace(self.fixture.context,
                         methodology_source_identities=self.fixture.context.methodology_source_identities[:-1])
        with self.assertRaises(InstallationError) as refused:
            self.verify(forged)
        self.assertEqual("portable-context-stale", refused.exception.code)

    def test_current_controls_do_not_substitute_for_a_full_gate(self):
        with self.assertRaises(InstallationError) as refused:
            self.verify(self.fixture.context)
        self.assertEqual("portable-full-gate-invalid", refused.exception.code)


if __name__ == "__main__":
    unittest.main()
