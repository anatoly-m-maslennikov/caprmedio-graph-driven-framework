"""Read-only Journal snapshots bind exactly one supplied Project root."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(TOOLS), str(TOOLS / "FIND_AND_FETCH_JOURNAL_EVENTS")]

from find_and_fetch_journal_events import JournalQueryError, capture_snapshot, query  # noqa: E402
import find_and_fetch_journal_events as journal_query  # noqa: E402
from project_selection import bind_selection, resolve_project  # noqa: E402


DEFAULTS_RELATIVE = Path("core/caprmedio_framework_default_settings.toml")
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
        (control / "project_structure.toml").write_text(
            'schema_version = 1\n[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\n'
            f'authority_path = "{control.name}/core"\ndelivery_path = "{control.name}/core"\n',
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
        self._project(root, "ancestor")
        control = root / ".caprmedio_ancestor"
        (control / DEFAULTS_RELATIVE).unlink()
        (control / "core").rmdir()
        (control / "core").symlink_to(self.beta / ".caprmedio_beta/core", target_is_directory=True)
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(root)

    def test_dangling_instance_settings_symlink_is_not_treated_as_absent(self) -> None:
        instance = self.alpha / (
            ".caprmedio_alpha/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        )
        instance.parent.mkdir(parents=True, exist_ok=True)
        instance.symlink_to(self.beta / "missing-settings.toml")
        with self.assertRaisesRegex(JournalQueryError, "instance-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_unsafe_instance_parent_is_not_treated_as_optional_absence(self) -> None:
        parent = self.alpha / ".caprmedio_alpha/000_CAPRMEDIO_framework"
        parent.symlink_to(self.beta / "missing-instance-folder", target_is_directory=True)
        with self.assertRaisesRegex(JournalQueryError, "instance-settings-unavailable"):
            capture_snapshot(self.alpha)
        parent.unlink()
        parent.write_text("not a directory")
        with self.assertRaisesRegex(JournalQueryError, "instance-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_declared_defaults_and_partial_instance_overrides_are_project_local(self) -> None:
        beta_defaults = self.beta / ".caprmedio_beta" / DEFAULTS_RELATIVE
        beta_defaults.write_text(DEFAULTS.replace("max_page_size = 2", "max_page_size = 3"))
        before = {path: path.read_bytes() for path in self.repository.rglob("*") if path.is_file()}
        alpha = capture_snapshot(self.alpha)
        beta = capture_snapshot(self.beta)
        self.assertEqual(2, query(alpha, {})["limits"]["max_page_size"]["configured"])
        self.assertEqual(3, query(beta, {})["limits"]["max_page_size"]["configured"])
        self.assertEqual(before, {path: path.read_bytes() for path in self.repository.rglob("*") if path.is_file()})
        instance = self.alpha / ".caprmedio_alpha/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        instance.parent.mkdir(parents=True)
        instance.write_text("[query]\nmax_page_size = 1\n")
        snapshot = capture_snapshot(self.alpha)
        evidence = query(snapshot, {})["limits"]
        self.assertEqual(1, evidence["max_page_size"]["configured"])
        self.assertEqual("instance", evidence["max_page_size"]["source"])
        self.assertEqual("default", evidence["max_request_bytes"]["source"])
        native = capture_snapshot(self.alpha, instance_settings={"query": {"max_page_size": 2}})
        self.assertEqual(2, query(native, {})["limits"]["max_page_size"]["configured"])
        explicit = capture_snapshot(self.alpha, limits={"max_page_size": 3})
        self.assertEqual(3, query(explicit, {})["limits"]["max_page_size"]["configured"])
        self.assertEqual(4, query(explicit, {"limits": {"max_page_size": 4}})["limits"]["max_page_size"]["configured"])

    def test_missing_duplicate_and_unsafe_core_declarations_refuse(self) -> None:
        structure = self.alpha / ".caprmedio_alpha/project_structure.toml"
        original = structure.read_text()
        row = original.split("[[scope_units]]", 1)[1]
        variants = ["schema_version = 1\n", original + "\n[[scope_units]]" + row,
                    original.replace(".caprmedio_alpha/core", "../beta/.caprmedio_beta/core"),
                    original.replace(".caprmedio_alpha/core", "/outside/core"),
                    original.replace('authority_path = ".caprmedio_alpha/core"\n', "")]
        for invalid in variants:
            with self.subTest(structure=invalid):
                structure.write_text(invalid)
                with self.assertRaises(JournalQueryError):
                    capture_snapshot(self.alpha)
        structure.write_text(original)
        self.assertEqual(["same-event-id"], capture_snapshot(self.alpha)["event_ids"])

    def test_missing_or_malformed_defaults_do_not_use_an_installed_fallback(self) -> None:
        defaults = self.alpha / ".caprmedio_alpha" / DEFAULTS_RELATIVE
        defaults.unlink()
        old = self.alpha / ".caprmedio_alpha/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/caprmedio_framework_default_settings.toml"
        old.parent.mkdir(parents=True)
        old.write_text(DEFAULTS)
        with self.assertRaisesRegex(JournalQueryError, "default-settings-unavailable"):
            capture_snapshot(self.alpha)
        defaults.write_text("[query\n")
        with self.assertRaisesRegex(JournalQueryError, "default-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_invalid_present_instance_values_refuse_without_default_fallback(self) -> None:
        instance = self.alpha / ".caprmedio_alpha/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        instance.parent.mkdir(parents=True)
        for value in ("true", "0", "-1"):
            with self.subTest(value=value):
                instance.write_text(f"[query]\nmax_page_size = {value}\n")
                with self.assertRaises(JournalQueryError) as refused:
                    capture_snapshot(self.alpha)
                self.assertEqual("invalid-limit", refused.exception.code)
        instance.write_text("[query\n")
        with self.assertRaisesRegex(JournalQueryError, "instance-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_foreign_bound_project_and_stale_structure_are_refused(self) -> None:
        selected = resolve_project(self.alpha)
        with bind_selection(selected):
            with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
                capture_snapshot(self.beta)
            structure = self.alpha / ".caprmedio_alpha/project_structure.toml"
            structure.write_text(structure.read_text() + "\n# changed selection\n")
            with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
                capture_snapshot(self.alpha)

    def test_declared_core_cannot_cross_another_project_boundary(self) -> None:
        self._project(self.alpha / "nested", "nested")
        structure = self.alpha / ".caprmedio_alpha/project_structure.toml"
        structure.write_text(structure.read_text().replace(".caprmedio_alpha/core", "nested/.caprmedio_nested/core"))
        with self.assertRaisesRegex(JournalQueryError, "project-settings-unavailable"):
            capture_snapshot(self.alpha)

    def test_structure_drift_during_settings_reads_is_refused(self) -> None:
        structure = self.alpha / ".caprmedio_alpha/project_structure.toml"
        read_toml = journal_query._read_toml

        def changed(path, code, reader):
            value = read_toml(path, code, reader)
            structure.write_text(structure.read_text() + "\n# concurrent declaration edit\n")
            return value

        with patch.object(journal_query, "_read_toml", side_effect=changed):
            with self.assertRaisesRegex(JournalQueryError, "query-settings-changed"):
                capture_snapshot(self.alpha)

    def test_core_defaults_can_use_the_declared_project_source_location(self) -> None:
        source = self.alpha / "declared-methodology"
        source.mkdir()
        (source / "caprmedio_framework_default_settings.toml").write_text(
            DEFAULTS.replace("max_page_size = 2", "max_page_size = 4"))
        structure = self.alpha / ".caprmedio_alpha/project_structure.toml"
        structure.write_text(structure.read_text().replace(".caprmedio_alpha/core", "declared-methodology"))
        self.assertEqual(4, query(capture_snapshot(self.alpha), {})["limits"]["max_page_size"]["configured"])


if __name__ == "__main__":
    unittest.main()
