"""Plain Journal append acceptance; fixtures never touch the live Project."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
for directory in (TOOLS, TOOLS / "APPEND_CHANGE_RECORDS"):
    sys.path.insert(0, str(directory))

import append_change_records as appender  # noqa: E402
import work_journal  # noqa: E402

TEST_TEMP_ROOT = TOOLS.parents[2] / ".caprmedio_tmp/tests/test_append_change_records"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)


class AppendChangeRecordsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT)
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n'
        )
        self.run_git("init", "-q")
        self.run_git("config", "user.name", "Test User")
        self.run_git("config", "user.email", "test@example.invalid")
        self.run_git("add", ".caprmedio_caprmedio/caprmedio_project_settings.toml")
        self.run_git("commit", "-qm", "initial")
        self.artifact = self.root / "artifact.md"
        self.artifact.write_text("Unchanged source\n")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_git(self, *args: str) -> str:
        return subprocess.run(
            [
                "git",
                "-c",
                "maintenance.auto=false",
                "-c",
                "gc.auto=0",
                "-C",
                str(self.root),
                *args,
            ],
            check=True,
            capture_output=True,
            text=True,
            timeout=10,
        ).stdout.strip()

    def context(self, *, action="UPDATE", local_date="2026-08-20", records=None) -> dict:
        return {
            "author": "test-user",
            "local_date": local_date,
            "timezone": "Asia/Tbilisi",
            "predictions": {
                "journal_records": records
                if records is not None
                else [
                    {
                        "event_id": "event-one",
                        "action_id": "action-one",
                        "event_digest": "caller-data",
                        "action_type": action,
                        "path": "../observed-path",
                        "custom": "observed value",
                    }
                ]
            },
        }

    def events(self) -> list:
        return work_journal.read_records(self.root)

    def test_dry_run_is_mutation_free(self) -> None:
        before = {
            p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()
        }
        context = self.context()
        with patch.object(appender, "append_sealed_events", side_effect=AssertionError("append")):
            result = appender.run(self.root, {"context": context}, apply=False)
        self.assertEqual(
            context["predictions"]["journal_records"],
            result["result"]["planned_effects"]["journal_records"],
        )
        self.assertEqual([], result["result"]["receipts"])
        self.assertEqual(
            before,
            {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()},
        )

    def test_repeated_and_conflicting_ids_append_again(self) -> None:
        context = self.context()
        first = appender.run(self.root, {"context": context}, apply=True)
        second = appender.run(self.root, {"context": context}, apply=True)
        different = self.context(records=[{"event_id": "event-one", "custom": "different"}])
        appender.run(self.root, {"context": different}, apply=True)
        self.assertEqual(
            [*context["predictions"]["journal_records"]] * 2
            + different["predictions"]["journal_records"],
            self.events(),
        )
        self.assertEqual(1, first["result"]["receipts"][0]["line"])
        self.assertEqual(2, second["result"]["receipts"][0]["line"])
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_no_schema_digest_history_or_git_checks(self) -> None:
        context = self.context(
            records=[{}, {"event_digest": "wrong", "previous_result_event": "unknown"}, 7, None]
        )
        context.update(schema_version="anything", context_id="wrong", validation=False)
        unrelated = self.root / "unrelated"
        unrelated.write_text("staged data")
        self.run_git("add", "unrelated")
        index = (self.root / ".git/index").read_bytes()
        before = self.artifact.read_bytes()
        appender.run(self.root, {"context": context}, apply=True)
        self.assertEqual(context["predictions"]["journal_records"], self.events())
        self.assertEqual(index, (self.root / ".git/index").read_bytes())
        self.assertEqual(before, self.artifact.read_bytes())

    def test_existing_unreadable_row_does_not_gate_append(self) -> None:
        path = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson"
        path.parent.mkdir()
        before = b"not JSON\n"
        path.write_bytes(before)
        result = appender.run(self.root, {"context": self.context()}, apply=True)
        self.assertEqual(2, result["result"]["receipts"][0]["line"])
        self.assertTrue(path.read_bytes().startswith(before))

    def test_no_git_repository_is_required(self) -> None:
        with tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT) as temporary:
            root = Path(temporary)
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_bytes(
                (self.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").read_bytes()
            )
            appender.run(root, self.context(), apply=True)
            self.assertEqual(
                self.context()["predictions"]["journal_records"], work_journal.read_records(root)
            )

    def test_one_thousand_rows_then_rollover_preserves_first_part(self) -> None:
        context = self.context(records=[{"number": n} for n in range(1000)])
        appender.run(self.root, context, apply=True)
        first = self.root / ".caprmedio_caprmedio/_journal/test-user-2026-08-20-part-1.ndjson"
        before = first.read_bytes()
        result = appender.run(self.root, self.context(records=[{"number": 1000}]), apply=True)
        self.assertEqual(before, first.read_bytes())
        self.assertEqual(1, result["result"]["receipts"][0]["line"])
        self.assertTrue(result["result"]["receipts"][0]["carrier"].endswith("-part-2.ndjson"))
        self.assertEqual([{"number": n} for n in range(1001)], self.events())

    def test_cli_keeps_existing_context_and_apply_interface(self) -> None:
        command = [
            sys.executable,
            "-B",
            str(TOOLS / "APPEND_CHANGE_RECORDS/append_change_records.py"),
            "--repository",
            str(self.root),
            "run",
            "--input",
            "-",
            "--apply",
        ]
        result = subprocess.run(
            command,
            input=json.dumps({"context": self.context()}),
            text=True,
            capture_output=True,
            timeout=10,
            check=True,
        )
        self.assertTrue(json.loads(result.stdout)["ok"])
        self.assertEqual(self.context()["predictions"]["journal_records"], self.events())


if __name__ == "__main__":
    unittest.main()
