"""Already sealed package controls are read-only Unit fixture inputs."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest


TEST_ROOT = Path(__file__).resolve().parent
for path in (TEST_ROOT.parent, TEST_ROOT):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from portable_package_fixture import PortablePackageFixture  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_suite import _bound_suite_inputs, _copy_workspace_file  # noqa: E402
from release_suite_inputs import collect_portable_suite_inputs  # noqa: E402
from test_portable_release_suite import _members  # noqa: E402


class ReleaseSuiteWorkspaceSupportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = PortablePackageFixture(extra_engine_members=_members())
        self.addCleanup(self.fixture.cleanup)
        assert self.fixture.sealed is not None
        self.sealed = self.fixture.sealed

    def test_copies_only_sealed_controls_without_adding_runner_claims(self) -> None:
        inputs = collect_portable_suite_inputs(self.fixture.candidate, self.sealed)
        runner_paths = {row.source_path for row in inputs.source_paths}
        controls = [row for row in inputs.workspace_paths if row.origin_kind == "workspace_support"]
        self.assertEqual(
            {row.source_path for row in controls},
            {"defaults/runtime-config.toml", "version.toml", "pyproject.toml", "uv.lock"},
        )
        self.assertTrue(runner_paths.isdisjoint(row.source_path for row in controls))
        self.assertTrue(set(inputs.phase_map.unit_paths).isdisjoint(row.source_path for row in controls))
        sealed_rows = {row.source_path: row for row in self.sealed.portable_package_rows}
        with tempfile.TemporaryDirectory(prefix="release-workspace-support-") as directory:
            workspace = Path(directory)
            for row in controls:
                sealed = sealed_rows[row.source_path]
                self.assertEqual((row.resource, row.sha256, row.mode), (sealed.resource, sealed.sha256, sealed.mode))
                _copy_workspace_file(self.fixture.root, workspace, row.source_path, row.sha256, row.mode)
                copied = workspace / row.source_path
                self.assertEqual(hashlib.sha256(copied.read_bytes()).hexdigest(), row.sha256)
                self.assertEqual(copied.stat().st_mode & 0o777, row.mode)
        bound = _bound_suite_inputs(self.fixture.candidate, self.sealed)
        self.assertEqual(bound.rows, inputs.source_paths)
        self.assertEqual(bound.workspace_rows, inputs.workspace_paths)
        self.assertEqual(bound.phase_map, inputs.phase_map)
        self.assertFalse(any(row.resource in {"CATALOG", "SOURCE_ADMISSION"} for row in bound.workspace_rows))

    def test_undeclared_live_default_is_not_included(self) -> None:
        self.fixture.write("defaults/unsealed.toml", b"unsealed = true\n")
        with self.assertRaises(ReleaseContractError):
            collect_portable_suite_inputs(self.fixture.candidate, self.sealed)

    def test_control_drift_and_symlink_are_refused(self) -> None:
        inputs = collect_portable_suite_inputs(self.fixture.candidate, self.sealed)
        version = next(row for row in inputs.workspace_paths if row.source_path == "version.toml")
        physical = self.fixture.root / version.source_path
        original = physical.read_bytes()
        physical.write_bytes(original + b"# drift\n")
        with tempfile.TemporaryDirectory(prefix="release-workspace-stale-") as directory:
            with self.assertRaises(ReleaseContractError) as raised:
                _copy_workspace_file(self.fixture.root, Path(directory), version.source_path, version.sha256, version.mode)
            self.assertEqual(raised.exception.code, "release-currentness-stale")
        physical.write_bytes(original)
        physical.unlink()
        physical.symlink_to(self.fixture.root / "pyproject.toml")
        with self.assertRaises(ReleaseContractError):
            collect_portable_suite_inputs(self.fixture.candidate, self.sealed)


if __name__ == "__main__":
    unittest.main()
