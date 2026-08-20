"""Deterministic acceptance tests for APPEND_CHANGE_RECORDS."""

from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[4]
TOOLS = REPOSITORY / "02_FR_ENGN" / "TOOLS"
APPENDER = TOOLS / "APPEND_CHANGE_RECORDS"
sys.pycache_prefix = str(REPOSITORY / ".caprmedio_runtime" / "cache" / "python")
for path in (str(APPENDER), str(TOOLS)):
    if path not in sys.path:
        sys.path.insert(0, path)

from append_change_records import (  # noqa: E402
    ToolError,
    release_verified_lease,
    run,
)
from work_journal import (  # noqa: E402
    append_sealed_events,
    canonical_json_digest,
    with_event_digest,
)


def sha(value: bytes | str) -> str:
    raw = value.encode("utf-8") if isinstance(value, str) else value
    return hashlib.sha256(raw).hexdigest()


class AppendChangeRecordsTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        control = self.root / ".caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\n"
            'journal_root = ".caprmedio/work_journal"\n'
            'runtime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        self.run_git("init", "-q")
        self.run_git("config", "user.name", "Test User")
        self.run_git("config", "user.email", "test@example.invalid")
        self.run_git("add", ".caprmedio/caprmedio_project_settings.toml")
        self.run_git("commit", "-qm", "initial")
        self.artifact = self.root / "artifact.md"
        self.artifact.write_text("# Artifact\n\nInitial governed content.\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def run_git(self, *arguments: str) -> str:
        completed = subprocess.run(
            ["git", "-C", str(self.root), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout.strip()

    def context(self, *, action: str = "ADD", local_date: str = "2026-08-20") -> dict[str, object]:
        git_base = {
            "commit": self.run_git("rev-parse", "HEAD"),
            "tree": self.run_git("rev-parse", "HEAD^{tree}"),
        }
        result = {
            "state": "present",
            "filename": self.artifact.name,
            "version": 1,
            "path": self.artifact.relative_to(self.root).as_posix(),
            "sha256": sha(self.artifact.read_bytes()),
        }
        source_frontier = {
            "identity": "CA-R-001",
            "state": "present",
            "filename": result["filename"],
            "version": result["version"],
            "path": result["path"],
            "sha256": result["sha256"],
        }
        event = with_event_digest(
            {
                "schema_version": 2,
                "event_id": "event-001",
                "action_id": "action-001",
                "event": "completed",
                "kind": "governed_file_change",
                "author": "test-user",
                "occurred_at": "2026-08-20T23:59:59+04:00",
                "llm_session": {"app": "codex", "uuid": "session-001"},
                "structural_scope": "PROJECT",
                "action_type": action,
                "sources": [],
                "result": result,
            }
        )
        if action != "ADD":
            event["previous_result_event"] = "prior-event"
            event = with_event_digest(event)
        context: dict[str, object] = {
            "schema_version": 2,
            "context_id": "context-001",
            "action_id": "action-001",
            "trigger": {
                "repository": {"root": str(self.root), "identity": sha(str(self.root))},
            },
            "subject": {"identity": "CA-R-001", "selected_state": "working"},
            "structural_scope": "PROJECT",
            "action_type": action,
            "sources": [],
            "relations": [],
            "result": result,
            "llm_session": {"app": "codex", "uuid": "session-001"},
            "author": "test-user",
            "occurred_at": "2026-08-20T23:59:59+04:00",
            "timezone": "Asia/Tbilisi",
            "local_date": local_date,
            "git_base": git_base,
            "frontier": {
                "source_sha256": canonical_json_digest(source_frontier),
                "relations_sha256": canonical_json_digest([]),
            },
            "snapshots": {"working": result},
            "validation": {"valid": True, "diagnostics": []},
            "predictions": {
                "journal_records": [event],
                "journal_partitions": [
                    {
                        "author": "test-user",
                        "local_date": local_date,
                        "part": 1,
                        "path": f".caprmedio/work_journal/test-user-{local_date}-part-1.ndjson",
                        "predicted_line": 1,
                    }
                ],
            },
        }
        return context

    def test_dry_run_is_mutation_free(self) -> None:
        result = run(self.root, {"context": self.context()}, apply=False, wait_seconds=0)
        self.assertTrue(result["ok"])
        self.assertEqual("dry-run", result["mode"])
        self.assertFalse((self.root / ".caprmedio/work_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_apply_is_idempotent_and_routes_by_sealed_date(self) -> None:
        payload = {"context": self.context()}
        first = run(self.root, payload, apply=True, wait_seconds=0)
        second = run(self.root, payload, apply=True, wait_seconds=0)
        path = self.root / ".caprmedio/work_journal/test-user-2026-08-20-part-1.ndjson"
        self.assertTrue(path.is_file())
        self.assertEqual(1, len(path.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(first["receipts"], second["receipts"])
        self.assertFalse((self.root / ".caprmedio/work_journal/test-user-2026-08-21-part-1.ndjson").exists())
        release_verified_lease(self.root, first["lease"])

    def test_rejects_stale_context_before_append(self) -> None:
        context = self.context()
        context["git_base"] = {"commit": "0" * 40, "tree": "0" * 40}
        with self.assertRaisesRegex(ToolError, "Git base commit"):
            run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio/work_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/commit_change_set/lease.json").exists())

    def test_rejects_existing_staged_change_before_append(self) -> None:
        unrelated = self.root / "unrelated.txt"
        unrelated.write_text("unrelated\n", encoding="utf-8")
        self.run_git("add", "unrelated.txt")
        with self.assertRaisesRegex(ToolError, "index contains a change outside the resolved subject identity"):
            run(self.root, {"context": self.context()}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio/work_journal").exists())

    def test_rejects_missing_result_before_append(self) -> None:
        context = self.context()
        context.pop("result")
        with self.assertRaisesRegex(ToolError, "result must be an object"):
            run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio/work_journal").exists())

    def test_rolls_to_second_part_after_one_hundred_records(self) -> None:
        event_template = self.context()["predictions"]["journal_records"][0]
        assert isinstance(event_template, dict)
        events: list[dict[str, object]] = []
        for number in range(101):
            event = copy.deepcopy(event_template)
            event["event_id"] = f"event-{number:03d}"
            event["action_id"] = "one-action"
            event = with_event_digest(event)
            events.append(event)
        receipts = append_sealed_events(
            self.root,
            events,
            author="test-user",
            local_date="2026-08-20",
            timezone="Asia/Tbilisi",
        )
        first = self.root / ".caprmedio/work_journal/test-user-2026-08-20-part-1.ndjson"
        second = self.root / ".caprmedio/work_journal/test-user-2026-08-20-part-2.ndjson"
        self.assertEqual(100, len(first.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(1, len(second.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(100, receipts[99]["line"])
        self.assertEqual(1, receipts[100]["line"])


if __name__ == "__main__":
    unittest.main()
