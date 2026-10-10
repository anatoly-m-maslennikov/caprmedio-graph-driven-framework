"""Physical immutable-package input checks for the fresh public Unit adapter."""

from __future__ import annotations

import hashlib
import inspect
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
if str(RELEASE_ROOT) not in sys.path:
    sys.path.insert(0, str(RELEASE_ROOT))

from release_contract import canonical_json  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_package_evidence import PackageEvidenceView, PackageMemberEvidence  # noqa: E402
from release_suite import MODULE_RULES_RELATIVE  # noqa: E402
from release_suite_execution import installed_public_n_suite_executor  # noqa: E402
from release_test_phases import CANDIDATE_E2E_MODULES, derive_test_phase_map_from_rows  # noqa: E402
from release_public_suite import (  # noqa: E402
    PublicSuiteInputError, _package_rows, execute_public_release_suite,
)
import release_public_suite as public_suite  # noqa: E402


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


class DetachedPublicPackageRowsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.root = Path(tempfile.mkdtemp(prefix="public-suite-package-"))
        self.addCleanup(lambda: None)
        self.members: list[PackageMemberEvidence] = []
        self._write(MODULE_RULES_RELATIVE, canonical_json({"schema_version": 1, "module_probes": []}), "engine")
        self.test_paths = (
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_public_unit.py",
            *CANDIDATE_E2E_MODULES,
        )
        for path in self.test_paths:
            self._write(path, f"def test_{Path(path).stem}():\n    pass\n".encode(), "engine")
        self._write("METHODOLOGY/compiled/compiled.json", b"{}\n", "methodology")
        self._write("SKILLS/ca/SKILL.md", b"# ca\n", "skill")
        self._write("SKILLS/ca/agents/openai.yaml", b"name: ca\n", "skill")
        self.phase_map = derive_test_phase_map_from_rows(
            SimpleNamespace(source_path=member.path, sha256=member.sha256)
            for member in self.members
        )

    def _write(self, relative: str, payload: bytes, role: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
        path.chmod(0o644)
        self.members.append(PackageMemberEvidence(relative, _sha256(payload), 0o644, role))

    def _view(self, members=None):
        return PackageEvidenceView(
            package_schema="portable-1",
            candidate_snapshot_manifest_sha256="a" * 64,
            actual_package_manifest_sha256="b" * 64,
            source_catalog_sha256="c" * 64,
            candidate_run_id="public-fixture",
            input_manifest_sha256="d" * 64,
            framework_version="N+1",
            version_toml_sha256="e" * 64,
            package_root=self.root,
            member_inventory=tuple(members if members is not None else self.members),
            phase_map=self.phase_map,
        )

    def test_reopens_complete_immutable_package_rows_without_project_checkout_sources(self) -> None:
        rows, compiled_root = _package_rows(object(), self.root, self._view())

        self.assertEqual(compiled_root, "METHODOLOGY/compiled")
        self.assertEqual({row.source_path for row in rows}, {member.path for member in self.members})
        destinations = {row.source_path: row.destination_path for row in rows}
        self.assertEqual(
            destinations["102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_public_unit.py"],
            "FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tests/test_public_unit.py",
        )
        self.assertEqual(destinations["METHODOLOGY/compiled/compiled.json"], "METHODOLOGY/compiled/compiled.json")
        self.assertEqual(destinations["SKILLS/ca/SKILL.md"], "SKILLS/ca/SKILL.md")

    def test_refuses_missing_compiled_package_member_before_an_executor_can_be_constructed(self) -> None:
        members = [member for member in self.members if not member.path.startswith("METHODOLOGY/compiled/")]

        with self.assertRaises(PublicSuiteInputError) as raised:
            _package_rows(object(), self.root, self._view(members))

        self.assertEqual(raised.exception.code, "public-suite-package-invalid")

    def test_refuses_member_byte_drift(self) -> None:
        member = next(member for member in self.members if member.path == MODULE_RULES_RELATIVE)
        (self.root / member.path).write_bytes(b"changed\n")

        with self.assertRaises(PublicSuiteInputError) as raised:
            _package_rows(object(), self.root, self._view())

        self.assertEqual(raised.exception.code, "public-suite-package-stale")

    def test_refuses_symlinked_immutable_package_member(self) -> None:
        member = next(member for member in self.members if member.path == MODULE_RULES_RELATIVE)
        path = self.root / member.path
        path.unlink()
        path.symlink_to(self.root / "SKILLS" / "ca" / "SKILL.md")

        with self.assertRaises(PublicSuiteInputError) as raised:
            _package_rows(object(), self.root, self._view())

        self.assertEqual(raised.exception.code, "public-suite-package-stale")

    def test_public_producer_exposes_only_the_typed_docker_boundary(self) -> None:
        self.assertEqual(
            ("inputs", "docker"),
            tuple(inspect.signature(execute_public_release_suite).parameters),
        )

    def test_public_executor_refuses_traversing_compiled_root_before_native_or_docker_reopen(self) -> None:
        with self.assertRaises(ReleaseContractError) as raised:
            installed_public_n_suite_executor(
                "a" * 64, object(), project_root=str(self.root),
                compiled_root="../untrusted", docker=object(),
            )

        self.assertEqual("release-suite-executor-handoff-untrusted", raised.exception.code)

    def test_refuses_symlinked_public_attempt_parent_before_docker_boundary(self) -> None:
        external = Path(tempfile.mkdtemp(prefix="public-suite-external-"))
        candidate = "a" * 64
        runtime = self.root / ".caprmedio_runtime"
        runtime.mkdir()
        (runtime / "release_suite").symlink_to(external, target_is_directory=True)
        detached = SimpleNamespace(
            project_root=self.root,
            candidate_snapshot_manifest_sha256=candidate,
            current_native_n=object(),
            compiled_root="METHODOLOGY/compiled",
        )

        with (
            patch.object(public_suite, "reopen_public_retained_suite_inputs", return_value=detached),
            patch.object(public_suite, "installed_public_n_suite_executor") as executor,
            patch.object(public_suite, "_native_state") as native_state,
            self.assertRaises(ReleaseContractError) as raised,
        ):
            execute_public_release_suite(object(), docker=object())

        self.assertEqual("release-suite-path-unsafe", raised.exception.code)
        executor.assert_not_called()
        native_state.assert_not_called()
        self.assertFalse((external / candidate).exists())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
