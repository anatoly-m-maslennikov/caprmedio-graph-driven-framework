"""Concrete installed-N transport codec; disposable physical O200 fixture."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
for folder in (RELEASE_ROOT, RELEASE_ROOT.parent, RELEASE_ROOT.parent / "tests", Path(__file__).resolve().parent):
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))

import framework_package  # noqa: E402
import test_installed_mcp_binding as package_fixture  # noqa: E402
import test_native_selected_installation as installed_fixture  # noqa: E402
import portable_package_fixture as portable_fixture  # noqa: E402
from release_checkpoint import (  # noqa: E402
    _load_native_compilation,
    _load_native_document,
    _load_native_n,
    _load_native_snapshot,
    _native_compilation_value,
    _native_document_value,
    _native_n_value,
    _native_snapshot_value,
)
from release_contract import ReleaseContractError  # noqa: E402
from release_handoff import bind_native_installed_n, NativeInstalledNBinding  # noqa: E402
from installed_mcp_binding import TargetProjectContext as InstalledMcpTargetProjectContext  # noqa: E402
from release_portable_contract import seal_portable_source_snapshot  # noqa: E402


class _BindingFrontierFixture(portable_fixture.PortablePackageFixture):
    """Current physical package fixture with one frozen Delivery binding."""

    def __init__(self) -> None:
        super().__init__(admit=False)
        self.admission = self.admit_sources()
        self.sealed = seal_portable_source_snapshot(self.source_snapshot)

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        self.binding_source = self.write(
            ".caprmedio_caprmedio/07_delivery/CA-D-901--binding.md",
            b"---\natom_id: CA-D-901\nstatus: Active\ncontent_role: Delivery\n"
            b"version: 1\nupdated_at: 2026-10-10 00:00:00 +0000\nrelations: {}\n---\n"
            b"# CA-D-901\n\n```toml\n[tool_binding]\n"
            b'entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"\n```\n',
        )


class PortableBindingFrontierCheckpointTests(unittest.TestCase):
    def _fixture(self) -> _BindingFrontierFixture:
        fixture = _BindingFrontierFixture()
        self.addCleanup(fixture.cleanup)
        self.assertTrue(fixture.source_snapshot.binding_atoms)
        self.assertTrue(fixture.sealed.binding_atoms)
        return fixture

    def test_roundtrips_actual_nonempty_frozen_binding_frontier(self) -> None:
        fixture = self._fixture()
        snapshot = fixture.source_snapshot
        compilation = fixture.sealed

        restored_snapshot = _load_native_snapshot(
            _native_snapshot_value(snapshot), snapshot.candidate, snapshot.private_compilation,
        )
        restored_compilation = _load_native_compilation(
            _native_compilation_value(compilation), restored_snapshot,
        )

        self.assertEqual(restored_snapshot, snapshot)
        self.assertEqual(restored_compilation, compilation)
        self.assertEqual(
            tuple(atom.record() for atom in restored_compilation.binding_atoms),
            tuple(atom.record() for atom in compilation.binding_atoms),
        )

    def test_refuses_missing_or_tampered_nonempty_binding_frontier(self) -> None:
        fixture = self._fixture()
        snapshot = fixture.source_snapshot
        compilation = fixture.sealed

        missing_snapshot = copy.deepcopy(_native_snapshot_value(snapshot))
        del missing_snapshot["binding_atoms"]
        with self.assertRaises(ReleaseContractError) as missing:
            _load_native_snapshot(missing_snapshot, snapshot.candidate, snapshot.private_compilation)
        self.assertEqual("release-checkpoint-binding-mismatch", missing.exception.code)

        tampered_snapshot = copy.deepcopy(_native_snapshot_value(snapshot))
        tampered_snapshot["binding_atoms"][0]["sha256"] = "0" * 64
        with self.assertRaises(ReleaseContractError) as tampered:
            _load_native_snapshot(tampered_snapshot, snapshot.candidate, snapshot.private_compilation)
        self.assertEqual("release-checkpoint-binding-mismatch", tampered.exception.code)

        missing_compilation = copy.deepcopy(_native_compilation_value(compilation))
        del missing_compilation["binding_atoms"]
        with self.assertRaises(ReleaseContractError) as missing_compiled:
            _load_native_compilation(missing_compilation, snapshot)
        self.assertEqual("release-checkpoint-binding-mismatch", missing_compiled.exception.code)

    def test_legacy_empty_frontier_is_accepted_only_without_binding_projection_rows(self) -> None:
        fixture = portable_fixture.PortablePackageFixture()
        self.addCleanup(fixture.cleanup)
        snapshot = fixture.source_snapshot
        compilation = fixture.sealed
        self.assertEqual((), snapshot.binding_atoms)
        self.assertEqual((), compilation.binding_atoms)
        self.assertFalse(any(row.resource == "BINDING_PROJECTION" for row in snapshot.portable_package_rows))
        self.assertFalse(any(row.resource == "BINDING_PROJECTION" for row in compilation.portable_package_rows))

        legacy_snapshot = _native_snapshot_value(snapshot)
        del legacy_snapshot["binding_atoms"]
        restored_snapshot = _load_native_snapshot(
            legacy_snapshot, snapshot.candidate, snapshot.private_compilation,
        )
        legacy_compilation = _native_compilation_value(compilation)
        del legacy_compilation["binding_atoms"]
        restored_compilation = _load_native_compilation(legacy_compilation, restored_snapshot)

        self.assertEqual(restored_snapshot, snapshot)
        self.assertEqual(restored_compilation, compilation)


class SelectedNativeBindingCodecTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        installed_fixture.NativeSelectedInstallationTests.setUpClass()
        cls.installed = installed_fixture.NativeSelectedInstallationTests("runTest")
        cls.installed.setUp()
        cls.root = str(cls.installed.target)
        cls.binding = bind_native_installed_n(
            cls.installed.target, cls.installed.package, cls.installed.packet,
            target_context_sha256=cls.installed.context.sha256,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        if hasattr(cls, "installed"):
            cls.installed.doCleanups()

    def test_current_binding_roundtrip_reopens_original_packet_and_final_native_generation(self) -> None:
        restored = _load_native_n(_native_n_value(self.binding, self.root), self.root)
        self.assertIs(type(restored), NativeInstalledNBinding)
        self.assertIs(type(restored.selected.binding.target_context), InstalledMcpTargetProjectContext)
        self.assertEqual(restored, self.binding)

    def test_historical_binding_is_documentary_and_reopens_private_retained_package_not_deleted_n(self) -> None:
        actual = framework_package.verify_framework_package
        calls = []

        def observe(path):
            calls.append(Path(path))
            return actual(path)

        with patch.object(framework_package, "verify_framework_package", side_effect=observe):
            restored = _load_native_n(_native_n_value(self.binding, self.root), self.root, historical=True)
        self.assertEqual(restored, self.binding)
        self.assertIn(self.binding.full_gate_packet.retained_candidate.package_evidence.view.package_root, calls)
        self.assertNotIn(self.binding.verified_package.root, calls)

    def test_closed_documentary_codec_roundtrips_an_actual_nonempty_verified_package_frontier(self) -> None:
        package_case = package_fixture.InstalledMcpBindingTests("runTest")
        package_case.setUp()
        self.addCleanup(package_case.doCleanups)
        verified = package_case._package(binding_count=2)

        self.assertEqual(("CA-D-901", "CA-D-902"), tuple(atom.atom_id for atom in verified.binding_atoms))
        documentary = _native_document_value(verified, str(package_case.root))
        restored = _load_native_document(documentary, str(package_case.root))

        self.assertIs(type(restored), framework_package.VerifiedFrameworkPackage)
        self.assertEqual(restored, verified)
        self.assertEqual(
            tuple(atom.record() for atom in restored.binding_atoms),
            tuple(atom.record() for atom in verified.binding_atoms),
        )

    def test_unrecognized_context_tag_and_packet_tamper_refuse(self) -> None:
        value = copy.deepcopy(_native_n_value(self.binding, self.root))
        context = value["selected"]["value"]["binding"]["value"]["target_context"]
        self.assertEqual(context["type"], "InstalledMcpTargetProjectContext")
        context["type"] = "RunExecutionSession"
        with self.assertRaises(ReleaseContractError):
            _load_native_n(value, self.root)
        value = copy.deepcopy(_native_n_value(self.binding, self.root))
        value["packet"]["descriptor_sha256"] = "f" * 64
        with self.assertRaises(ReleaseContractError):
            _load_native_n(value, self.root)


if __name__ == "__main__":
    unittest.main()
