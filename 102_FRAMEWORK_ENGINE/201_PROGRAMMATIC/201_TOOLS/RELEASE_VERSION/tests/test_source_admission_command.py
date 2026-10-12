"""Actual direct O199 host-command coverage without a selected-run shim."""

from __future__ import annotations

import json
import shutil
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


RELEASE_ROOT = Path(__file__).resolve().parents[1]
TEST_ROOT = Path(__file__).resolve().parent
TOOLS_ROOT = RELEASE_ROOT.parent
for _path in (RELEASE_ROOT, TEST_ROOT, TOOLS_ROOT):
    if str(_path) not in sys.path:
        sys.path.insert(0, str(_path))

from direct_action_session import SOURCE_ADMISSION_ATOM_RELATIVE  # noqa: E402
from portable_package_fixture import PortablePackageFixture  # noqa: E402
from source_admission_command import (  # noqa: E402
    COMMAND_DIRECTORY,
    SourceAdmissionCommandError,
    build_source_admission_command_receipt,
    read_source_admission_command_receipt,
    run_source_admission_command,
)
import source_admission_command as command_module  # noqa: E402


def _repository_root() -> Path:
    for candidate in RELEASE_ROOT.parents:
        if (candidate / SOURCE_ADMISSION_ATOM_RELATIVE).is_file():
            return candidate
    raise RuntimeError("repository root is unavailable")


REPOSITORY_ROOT = _repository_root()


class _DirectSourceFixture(PortablePackageFixture):
    """Seeds actual O199/Operator carriers before candidate sealing."""

    def _seed_project(self, extra_engine_members: dict[str, bytes]) -> None:
        super()._seed_project(extra_engine_members)
        (self.root / ".git").mkdir()
        self.write(
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            b"[paths]\ncontrol_root = '.caprmedio_caprmedio'\njournal_root = '.caprmedio_caprmedio/_journal'\nruntime_root = '.caprmedio_runtime'\n",
        )
        self.write(
            ".caprmedio_caprmedio/operators_registry.toml",
            b'[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\njournal_author = "fixture-operator"\n',
        )
        target = self.root / SOURCE_ADMISSION_ATOM_RELATIVE
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPOSITORY_ROOT / SOURCE_ADMISSION_ATOM_RELATIVE, target)


class SourceAdmissionCommandTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = _DirectSourceFixture(admit=False)
        self.addCleanup(self.fixture.cleanup)

    def _run(self):
        return run_source_admission_command(
            self.fixture.candidate,
            self.fixture.private_compilation,
            candidate_run_id=self.fixture.run_id,
            operator="Fixture Operator",
            command_id="fixture-o199-command",
            operators_registry_ref=".caprmedio_caprmedio/operators_registry.toml",
        )

    def _events(self) -> list[dict[str, object]]:
        journal = self.fixture.root / ".caprmedio_caprmedio/_journal"
        return [json.loads(line) for path in sorted(journal.glob("*.ndjson")) for line in path.read_text(encoding="utf-8").splitlines()]

    def test_real_direct_start_command_receipt_and_catalog_are_bound(self) -> None:
        result = self._run()

        self.assertTrue(result.command_receipt_path.is_file())
        self.assertEqual(self.fixture.root / COMMAND_DIRECTORY / f"{result.command_receipt.sha256}.json", result.command_receipt_path)
        self.assertEqual(result.admission.snapshot_sha256, result.command_receipt.snapshot_sha256)
        self.assertEqual(result.action_start["run_id"], result.command_receipt.action_run_id)
        self.assertEqual(result.action_start["event_id"], result.command_receipt.action_start_event_id)
        self.assertEqual("Fixture Operator", result.command_receipt.operator)
        self.assertEqual("fixture-operator", result.command_receipt.journal_author)
        self.assertEqual("completed", result.terminal["outcome"])
        events = self._events()
        self.assertEqual(["started", "completed"], [event["event"] for event in events])
        self.assertEqual(["CA-O-199", "CA-O-199"], [event["action_id"] for event in events])
        self.assertEqual(["fixture-operator", "fixture-operator"], [event["author"] for event in events])
        self.assertTrue(result.admission.catalog_path.is_file())
        self.assertTrue(result.admission.receipt_path.is_file())

    def test_closed_command_receipt_refuses_digest_schema_and_source_rewrites(self) -> None:
        result = self._run()
        payload = result.command_receipt_path.read_bytes()
        with self.assertRaises(SourceAdmissionCommandError) as digest:
            read_source_admission_command_receipt(payload, expected_sha256="0" * 64)
        self.assertEqual("source-admission-command-receipt-digest-mismatch", digest.exception.code)
        forged = json.loads(payload)
        forged["permission"] = True
        with self.assertRaises(SourceAdmissionCommandError) as schema:
            read_source_admission_command_receipt(json.dumps(forged, sort_keys=True, separators=(",", ":")).encode())
        self.assertEqual("source-admission-command-receipt-invalid", schema.exception.code)
        source = self.fixture.root / SOURCE_ADMISSION_ATOM_RELATIVE
        source.write_bytes(source.read_bytes() + b"changed\n")
        with self.assertRaises(Exception):
            self._run()
        self.assertEqual(payload, result.command_receipt_path.read_bytes())

    def test_unmapped_operator_refuses_before_start_or_publication(self) -> None:
        registry = self.fixture.root / ".caprmedio_caprmedio/operators_registry.toml"
        registry.write_text('[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\n', encoding="utf-8")
        with self.assertRaises(SourceAdmissionCommandError) as refused:
            self._run()
        self.assertEqual("source-admission-command-operator-invalid", refused.exception.code)
        self.assertFalse((self.fixture.root / "catalog.toml").exists())
        self.assertFalse((self.fixture.root / COMMAND_DIRECTORY).exists())
        self.assertEqual([], self._events())

    def test_source_snapshot_drift_refuses_before_start_or_publication(self) -> None:
        tool = self.fixture.root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/tool.py"
        tool.write_bytes(tool.read_bytes() + b"changed\n")
        with self.assertRaises(Exception) as refused:
            self._run()
        self.assertEqual("release-currentness-stale", getattr(refused.exception, "code", None))
        self.assertFalse((self.fixture.root / "catalog.toml").exists())
        self.assertFalse((self.fixture.root / COMMAND_DIRECTORY).exists())
        self.assertEqual([], self._events())

    def test_registry_drift_after_real_start_refuses_before_catalog(self) -> None:
        registry = self.fixture.root / ".caprmedio_caprmedio/operators_registry.toml"
        original_publish = command_module._publish_exact

        def mutate_registry(directory: Path, filename: str, payload: bytes) -> Path:
            published = original_publish(directory, filename, payload)
            registry.write_text(
                '[[operators]]\nname = "Fixture Operator"\nrole = "project owner"\njournal_author = "other-operator"\n',
                encoding="utf-8",
            )
            return published

        with patch.object(command_module, "_publish_exact", side_effect=mutate_registry):
            with self.assertRaises(Exception) as refused:
                self._run()
        self.assertEqual("source-admission-invocation-rejected", getattr(refused.exception, "code", None))
        self.assertFalse((self.fixture.root / "catalog.toml").exists())
        self.assertFalse((self.fixture.root / "admissions").exists())
        self.assertTrue(list((self.fixture.root / COMMAND_DIRECTORY).glob("*.json")))
        self.assertEqual(["started"], [event["event"] for event in self._events()])

    def test_receipt_builder_requires_exact_closed_o199_shape(self) -> None:
        with self.assertRaises(SourceAdmissionCommandError):
            build_source_admission_command_receipt(
                command_id="bad command",
                operator="Fixture Operator",
                journal_author="fixture-operator",
                action_run_id="run",
                action_start_event_id="start",
                snapshot_sha256="a" * 64,
                action_source={"atom_id": "CA-O-198", "version": 1, "path": "actions/o199.md", "sha256": "b" * 64},
                operators_registry_sha256="c" * 64,
            )


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
