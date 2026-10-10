"""Read-only Journal snapshots bind exactly one supplied Project root."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(TOOLS), str(TOOLS / "FIND_AND_FETCH_JOURNAL_EVENTS")]

from find_and_fetch_journal_events import JournalQueryError, capture_snapshot, query  # noqa: E402


DEFAULTS_RELATIVE = Path(
    "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/"
    "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
)
DEFAULTS = (
    "[query]\nmax_request_bytes = 4096\nmax_grammar_depth = 16\n"
    "max_filter_tokens = 128\nmax_in_members = 16\nmax_selected_fields = 8\n"
    "max_page_size = 2\nmax_snapshot_members = 8\nmax_file_bytes = 4096\n"
    "max_total_read_bytes = 16384\ntimeout_seconds = 10\nmax_findings = 8\n"
)


class JournalQueryProjectIsolationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name).resolve()
        self.alpha = self.repository / "alpha"
        self.beta = self.repository / "beta"
        self.alpha_carrier = self._project(self.alpha, "alpha")
        self.beta_carrier = self._project(self.beta, "beta")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _project(self, root: Path, name: str) -> Path:
        control = root / f".caprmedio_{name}"
        journal = control / "_journal"
        journal.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            f'[project]\nname = "{name}"\n[paths]\ncontrol_root = "{control.name}"\n',
            encoding="utf-8",
        )
        defaults = control / DEFAULTS_RELATIVE
        defaults.parent.mkdir(parents=True)
        defaults.write_text(DEFAULTS, encoding="utf-8")
        carrier = journal / "events.ndjson"
        carrier.write_text(
            json.dumps({"event_id": "same-event-id", "project": name}) + "\n", encoding="utf-8",
        )
        return carrier

    def test_sibling_non_git_projects_have_separate_snapshots_and_query_results(self) -> None:
        alpha = capture_snapshot(self.alpha)
        beta = capture_snapshot(self.beta)
        self.assertFalse((self.alpha / ".git").exists())
        self.assertFalse((self.beta / ".git").exists())
        self.assertEqual(".caprmedio_alpha/_journal", alpha["source_root"])
        self.assertEqual(".caprmedio_beta/_journal", beta["source_root"])
        self.assertNotEqual(alpha["id"], beta["id"])
        self.assertEqual(["same-event-id"], alpha["event_ids"])
        self.assertEqual(["same-event-id"], beta["event_ids"])
        before = (self.alpha_carrier.read_bytes(), self.beta_carrier.read_bytes())
        for snapshot, expected in ((alpha, "alpha"), (beta, "beta")):
            fetched = query(snapshot, {"mode": "fields", "select": ["event:/project"]})
            self.assertEqual("complete", fetched["status"])
            self.assertEqual([{"event_id": "same-event-id", "event:/project": expected}], fetched["results"])
            foreign = "beta" if expected == "alpha" else "alpha"
            self.assertEqual([], query(snapshot, {"filter": f'"event:/project" = "{foreign}"'})["results"])
        self.assertEqual(before, (self.alpha_carrier.read_bytes(), self.beta_carrier.read_bytes()))
        self.assertFalse((self.repository / ".caprmedio_runtime").exists())
        self.assertFalse((self.alpha / ".caprmedio_runtime").exists())
        self.assertFalse((self.beta / ".caprmedio_runtime").exists())

    def test_other_project_changes_do_not_change_selected_snapshot(self) -> None:
        alpha = capture_snapshot(self.alpha)
        beta = capture_snapshot(self.beta)
        self.beta_carrier.write_text('{"event_id":"changed-event-id"}\n', encoding="utf-8")
        self.assertEqual(["same-event-id"], query(alpha, {})["results"])
        self.assertEqual("blocked", query(beta, {})["status"])

    def test_unconfigured_child_does_not_use_parent_repository_control(self) -> None:
        self._project(self.repository, "caprmedio")
        root = self.repository / "unconfigured"
        root.mkdir()
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(root)

    def test_ambiguous_and_contradictory_controls_are_refused(self) -> None:
        self._project(self.alpha, "extra")
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(self.alpha)
        settings = self.beta / ".caprmedio_beta/caprmedio_project_settings.toml"
        settings.write_text('[paths]\ncontrol_root = ".caprmedio_alpha"\n', encoding="utf-8")
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(self.beta)

    def test_control_and_settings_aliases_cannot_read_sibling_project(self) -> None:
        alias_root = self.repository / "alias"
        alias_root.mkdir()
        (alias_root / ".caprmedio_beta").symlink_to(self.beta / ".caprmedio_beta", target_is_directory=True)
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(alias_root)
        settings = self.alpha / ".caprmedio_alpha/caprmedio_project_settings.toml"
        settings.unlink()
        settings.symlink_to(self.beta / ".caprmedio_beta/caprmedio_project_settings.toml")
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_query_defaults_symlink_is_not_followed_to_another_project(self) -> None:
        defaults = self.alpha / ".caprmedio_alpha" / DEFAULTS_RELATIVE
        defaults.unlink()
        defaults.symlink_to(self.beta / ".caprmedio_beta" / DEFAULTS_RELATIVE)
        with self.assertRaisesRegex(JournalQueryError, "default-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_aliased_defaults_ancestor_is_not_followed(self) -> None:
        root = self.repository / "ancestor-alias"
        control = root / ".caprmedio_ancestor"
        control.mkdir(parents=True)
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_ancestor"\n', encoding="utf-8",
        )
        (control / "000_CAPRMEDIO_framework").symlink_to(
            self.beta / ".caprmedio_beta/000_CAPRMEDIO_framework", target_is_directory=True,
        )
        with self.assertRaisesRegex(JournalQueryError, "default-settings-unavailable"):
            capture_snapshot(root)

    def test_dangling_instance_settings_symlink_is_not_treated_as_absent(self) -> None:
        instance = self.alpha / (
            ".caprmedio_alpha/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        )
        instance.parent.mkdir(parents=True, exist_ok=True)
        instance.symlink_to(self.beta / "missing-settings.toml")
        with self.assertRaisesRegex(JournalQueryError, "instance-settings-unavailable"):
            capture_snapshot(self.alpha)


if __name__ == "__main__":
    unittest.main()
