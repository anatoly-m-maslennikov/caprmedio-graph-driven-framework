"""Synthetic retained-state transaction and installation-lock coverage."""
from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from installation_transaction import (  # noqa: E402
    InstallationTransactionError,
    installation_publication_lock,
    run_retained_legacy_migration,
)
import installation_state as state  # noqa: E402


def _digest(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


class InstallationTransactionTests(unittest.TestCase):
    def setUp(self) -> None:
        # Retained legacy fixtures must never be cleaned up by the test code.
        self.root = Path(tempfile.mkdtemp(dir="/private/tmp")) / "project-a"
        self.root.mkdir()
        self.context = _digest("project-a")
        self.command = _digest("command-a")
        self._legacy_fixture(self.root)

    @staticmethod
    def _legacy_fixture(root: Path) -> None:
        install = root / ".caprmedio_install"
        install.mkdir(exist_ok=True)
        (install / "current.toml").write_text('schema_version = 1\nrelease = "legacy"\n', encoding="utf-8")
        for name in ("project_mcp", "mcp_hot_reload", "workflow_orchestrator"):
            carrier = install / name / "state.txt"
            carrier.parent.mkdir(exist_ok=True)
            carrier.write_text(name, encoding="utf-8")

    def _lock(self, root: Path, context: str, owner: str):
        return installation_publication_lock(
            root,
            target_context_sha256=context,
            owner_run_id=owner,
            operation="installation",
            command_sha256=self.command,
            timeout_seconds=0,
        )

    def test_same_project_busy_but_cross_project_is_independent(self) -> None:
        with self._lock(self.root, self.context, "first") as first:
            with self.assertRaisesRegex(InstallationTransactionError, "installation-lock-busy"):
                with self._lock(self.root, self.context, "second"):
                    pass
            other = self.root.parent / "project-b"
            other.mkdir()
            other_context = _digest("project-b")
            with self._lock(other, other_context, "other") as second:
                second.revalidate()
                second.release("completed")
            first.release("completed")

    def test_success_switches_only_after_staged_and_verified_retention(self) -> None:
        result = run_retained_legacy_migration(
            self.root,
            migration_id="migration-ok",
            target_context_sha256=self.context,
            owner_run_id="run-ok",
            command_sha256=self.command,
            state_generation="generation-ok",
            process_observations=[],
        )
        self.assertEqual(("completed", "retained"), (result["status"], result["phase"]))
        self.assertTrue((self.root / ".caprmedio_runtime/installation/current.toml").is_file())
        self.assertTrue((self.root / ".caprmedio_install/workflow_orchestrator/state.txt").is_file())
        self.assertFalse((self.root / ".caprmedio_runtime/installation/lock.toml").exists())

    def test_injected_phase_failures_preserve_sources_and_report_actual_state(self) -> None:
        for phase in ("planned", "staged", "published", "switched", "retained"):
            with self.subTest(phase=phase):
                root = self.root.parent / f"failure-{phase}"
                root.mkdir()
                self._legacy_fixture(root)
                result = run_retained_legacy_migration(
                    root,
                    migration_id=f"migration-{phase}",
                    target_context_sha256=_digest(phase),
                    owner_run_id=f"run-{phase}",
                    command_sha256=self.command,
                    state_generation="generation-failure",
                    process_observations=[],
                    fail_after=phase,
                )
                self.assertIn(result["status"], {"partial", "recording-pending"})
                self.assertTrue((root / ".caprmedio_install/project_mcp/state.txt").is_file())
                if phase in {"switched", "retained"}:
                    self.assertTrue((root / ".caprmedio_runtime/installation/current.toml").is_file())
                else:
                    self.assertFalse((root / ".caprmedio_runtime/installation/current.toml").exists())

    def test_switch_receipt_failure_reports_selected_recording_pending_and_releases_lock(self) -> None:
        original_write = state._atomic_write

        def deny_switch_receipt(path, *args, **kwargs):
            if Path(path).name == "switch.toml":
                raise PermissionError("switch receipt denied")
            return original_write(path, *args, **kwargs)

        with patch.object(state, "_atomic_write", side_effect=deny_switch_receipt):
            result = run_retained_legacy_migration(
                self.root,
                migration_id="migration-receipt-denied",
                target_context_sha256=self.context,
                owner_run_id="run-receipt-denied",
                command_sha256=self.command,
                state_generation="generation-receipt-denied",
                process_observations=[],
            )
        self.assertEqual(("recording-pending", "switched"), (result["status"], result["phase"]))
        self.assertTrue(result["selector_changed"])
        self.assertEqual(
            (self.root / ".caprmedio_install/current.toml").read_bytes(),
            (self.root / ".caprmedio_runtime/installation/current.toml").read_bytes(),
        )
        self.assertTrue(
            (self.root / ".caprmedio_runtime/installation/migrations/migration-receipt-denied/history.toml").is_file()
        )
        self.assertFalse((self.root / ".caprmedio_runtime/installation/lock.toml").exists())


if __name__ == "__main__":
    unittest.main()
