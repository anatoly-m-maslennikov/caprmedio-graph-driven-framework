"""Project-local settings and persistent Journal isolation without Git."""

from __future__ import annotations

import datetime as dt
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

import work_journal  # noqa: E402


class WorkJournalProjectIsolationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.repository = Path(self.directory.name).resolve()
        self.alpha = self.repository / "alpha"
        self.beta = self.repository / "beta"
        self._project(self.alpha, "alpha", "UTC")
        self._project(self.beta, "beta", "Asia/Tbilisi")

    def tearDown(self) -> None:
        self.directory.cleanup()

    def _project(self, root: Path, name: str, timezone: str = "UTC") -> Path:
        control = root / f".caprmedio_{name}"
        control.mkdir(parents=True)
        settings = control / "caprmedio_project_settings.toml"
        settings.write_text(
            f'[project]\nname = "{name}"\n'
            f'[paths]\ncontrol_root = "{control.name}"\n'
            f'journal_root = "{control.name}/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n'
            f'[artifact_timestamps]\ntimezone = "{timezone}"\n',
            encoding="utf-8",
        )
        # A standalone Project can allocate owned atomic intermediates.
        (control / "project_structure.toml").write_text("schema_version = 1\n", encoding="utf-8")
        return settings

    def _event(self, project: str) -> dict[str, object]:
        definition = {
            "atom_id": "CA-O-200", "version": 1,
            "path": "operations/CA-O-200.md", "digest": "a" * 64,
        }
        return work_journal.with_event_digest({
            "schema_version": 5,
            "kind": "workflow_execution",
            "event_id": "same-event-id",
            "action_id": "same-action-id",
            "event": "completed",
            "author": "test-user",
            "occurred_at": "2026-10-10T12:00:00+00:00",
            "llm_session": {"app": "codex", "uuid": "same-session-id"},
            "structural_scope": "TOOLS",
            "initiative": {
                "initiative_id": "same-initiative-id",
                "instruction_summary": f"initialize {project}",
                "initiative_ref": "plan/initialization.md",
            },
            "run": {"run_id": "same-run-id", "kind": "action", "definition": definition},
            "definition_bindings": [{"kind": "action", **definition}],
            "input_ref": "inputs/initialize.json",
            "outcome": "completed",
            "result_ref": "results/initialize.json",
            "effect_refs": [f"{project}-result.md"],
            "report_ref": "reports/initialize.md",
            "redaction": {"redacted": False, "fields": []},
        })

    def test_sibling_projects_persist_same_event_identity_in_their_own_journals(self) -> None:
        for root, name in ((self.alpha, "alpha"), (self.beta, "beta")):
            self.assertFalse((root / ".git").exists())
            self.assertEqual(Path(f".caprmedio_{name}/_journal"), work_journal.configured_journal_root(root))
            self.assertEqual(Path(".caprmedio_runtime"), work_journal.configured_runtime_root(root))
            event = self._event(name)
            receipts = work_journal.append_sealed_events(
                root, [event], author="test-user", local_date="2026-10-10", timezone="UTC",
            )
            self.assertEqual(f".caprmedio_{name}/_journal/test-user-2026-10-10-part-1.ndjson", receipts[0]["carrier"])
            carrier = root / str(receipts[0]["carrier"])
            self.assertEqual([event], [json.loads(line) for line in carrier.read_text(encoding="utf-8").splitlines()])
            self.assertEqual(receipts, work_journal.append_sealed_events(
                root, [event], author="test-user", local_date="2026-10-10", timezone="UTC",
            ))
            self.assertTrue((root / ".caprmedio_runtime/state/work_journal").is_dir())
            self.assertFalse((root / ".caprmedio_caprmedio").exists())
        self.assertNotEqual(self._event("alpha")["event_digest"], self._event("beta")["event_digest"])
        self.assertFalse((self.repository / ".caprmedio_runtime").exists())

    def test_timestamp_reads_exact_project_settings(self) -> None:
        moment = dt.datetime(2026, 10, 10, 12, tzinfo=dt.UTC)
        with mock.patch.object(work_journal.dt, "datetime") as clock:
            clock.now.return_value = moment
            work_journal.current_timestamp(self.alpha)
            self.assertEqual(dt.UTC, clock.now.call_args.args[0])
            work_journal.current_timestamp(self.beta)
            self.assertEqual("Asia/Tbilisi", clock.now.call_args.args[0].key)

    def test_existing_canonical_project_remains_supported(self) -> None:
        root = self.repository / "canonical"
        settings = self._project(root, "caprmedio")
        self.assertEqual(settings, work_journal.resolve_settings_path(root))
        self.assertEqual(work_journal.SETTINGS_PATH.parent / "_journal", work_journal.configured_journal_root(root))

    def test_ambiguous_controls_refuse_implicit_selection(self) -> None:
        self._project(self.alpha, "extra")
        with self.assertRaisesRegex(RuntimeError, "ambiguous"):
            work_journal.resolve_settings_path(self.alpha)
        self.assertEqual(
            self.alpha / ".caprmedio_alpha/caprmedio_project_settings.toml",
            work_journal.resolve_settings_path(self.alpha, ".caprmedio_alpha"),
        )

    def test_declared_control_must_match_the_selected_settings_carrier(self) -> None:
        settings = self.alpha / ".caprmedio_alpha/caprmedio_project_settings.toml"
        settings.write_text('[paths]\ncontrol_root = ".caprmedio_beta"\n', encoding="utf-8")
        with self.assertRaisesRegex(RuntimeError, "exactly"):
            work_journal.resolve_settings_path(self.alpha)

    def test_control_symlink_is_rejected_even_if_target_is_another_project(self) -> None:
        root = self.repository / "alias"
        root.mkdir()
        (root / ".caprmedio_beta").symlink_to(self.beta / ".caprmedio_beta", target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            work_journal.configured_journal_root(root)
        with self.assertRaises(RuntimeError):
            work_journal.resolve_settings_path(root, ".caprmedio_beta")

    def test_settings_symlink_is_rejected(self) -> None:
        settings = self.alpha / ".caprmedio_alpha/caprmedio_project_settings.toml"
        settings.unlink()
        settings.symlink_to(self.beta / ".caprmedio_beta/caprmedio_project_settings.toml")
        with self.assertRaisesRegex(RuntimeError, "unsafe"):
            work_journal.resolve_settings_path(self.alpha)

    def test_supplied_root_symlink_and_parent_traversal_are_rejected(self) -> None:
        alias = self.repository / "alpha-alias"
        alias.symlink_to(self.alpha, target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            work_journal.resolve_settings_path(alias)
        with self.assertRaisesRegex(RuntimeError, "unsafe"):
            work_journal.resolve_settings_path(self.beta / ".." / "alpha")

    def test_configured_runtime_and_journal_cannot_escape_through_symlinks(self) -> None:
        (self.alpha / ".caprmedio_alpha/_journal").symlink_to(self.beta, target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            work_journal.configured_journal_root(self.alpha)
        (self.alpha / ".caprmedio_runtime").symlink_to(self.beta, target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, "symlink"):
            work_journal.configured_runtime_root(self.alpha)

    def test_unconfigured_child_never_uses_parent_repository_settings(self) -> None:
        self._project(self.repository, "caprmedio")
        child = self.repository / "unconfigured"
        child.mkdir()
        for reader in (work_journal.resolve_settings_path, work_journal.configured_journal_root,
                       work_journal.configured_runtime_root, work_journal.current_timestamp):
            with self.subTest(reader=reader.__name__), self.assertRaisesRegex(RuntimeError, "missing"):
                reader(child)
        self.assertFalse((child / ".caprmedio_runtime").exists())

    def test_nested_controls_and_unsafe_explicit_paths_do_not_select_a_project(self) -> None:
        root = self.repository / "nested"
        self._project(root / "nested", "hidden")
        with self.assertRaisesRegex(RuntimeError, "missing"):
            work_journal.resolve_settings_path(root)
        for value in ("../beta/.caprmedio_beta", ".caprmedio_alpha/extra", ".caprmedio_", "/.caprmedio_alpha"):
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                work_journal.resolve_settings_path(self.alpha, value)


if __name__ == "__main__":
    unittest.main()
