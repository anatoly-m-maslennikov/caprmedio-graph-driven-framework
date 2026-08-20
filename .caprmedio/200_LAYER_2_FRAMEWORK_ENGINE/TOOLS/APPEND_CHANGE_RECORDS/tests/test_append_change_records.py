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


TOOLS = Path(__file__).resolve().parents[2]
APPENDER = TOOLS / "APPEND_CHANGE_RECORDS"
CONTEXT_TOOL = TOOLS / "COMMIT_CONTEXT"
for _parent in Path(__file__).resolve().parents:
    if _parent.name == ".caprmedio":
        sys.pycache_prefix = str(_parent.parent / ".caprmedio_runtime" / "cache" / "python")
        break
for path in (str(APPENDER), str(TOOLS)):
    if path not in sys.path:
        sys.path.insert(0, path)

from append_change_records import (  # noqa: E402
    ToolError,
    _expected_context_id,
    _expected_event_id,
    release_verified_lease,
    run,
)
from work_journal import (  # noqa: E402
    append_sealed_events,
    canonical_json_digest,
    with_event_digest,
)
sys.path.insert(0, str(CONTEXT_TOOL))
from commit_context_logic import gather_context  # noqa: E402


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

    def repository_identity(self) -> str:
        git_directory = Path(self.run_git("rev-parse", "--git-dir"))
        if not git_directory.is_absolute():
            git_directory = self.root / git_directory
        return canonical_json_digest(
            {"repository_root": self.root.resolve().as_posix(), "git_directory": git_directory.resolve().as_posix()}
        )

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
        event = {
            "schema_version": 2,
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
        if action != "ADD":
            event["previous_result_event"] = "prior-event"
        event["event_id"] = _expected_event_id(event)
        event = with_event_digest(event)
        context: dict[str, object] = {
            "schema_version": 2,
            "action_id": "action-001",
            "trigger": {
                "repository": {"root": str(self.root), "identity": self.repository_identity()},
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
        context["context_id"] = _expected_context_id(context)
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
        self.assertEqual(first["result"]["receipts"], second["result"]["receipts"])
        self.assertFalse((self.root / ".caprmedio/work_journal/test-user-2026-08-21-part-1.ndjson").exists())
        correlations = self.root / ".caprmedio_runtime/state/commit_trigger/pipeline_correlations.ndjson"
        registered = [json.loads(line) for line in correlations.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["registered"], [record["event"] for record in registered])
        self.assertEqual(first["result"]["receipts"][0]["appended_carrier_digest"], registered[0]["transition"]["appended_carrier_digest"])
        release_verified_lease(self.root, first["result"]["lease"])
        retired = [json.loads(line) for line in correlations.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["registered", "retired"], [record["event"] for record in retired])

    def test_rejects_stale_context_before_append(self) -> None:
        context = self.context()
        context["git_base"] = {"commit": "0" * 40, "tree": "0" * 40}
        with self.assertRaisesRegex(ToolError, "context_id"):
            run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertFalse((self.root / ".caprmedio/work_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").exists())

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

    def test_appends_recovery_then_change_from_exact_sealed_evidence(self) -> None:
        context = self.context(action="UPDATE")
        result = copy.deepcopy(context["result"])
        assert isinstance(result, dict)
        evidence = {
            "git": {"base_commit": context["git_base"]["commit"], "path": result["path"], "sha256": result["sha256"]},
            "carrier": {"identity": "CA-R-001", "filename": result["filename"], "version": result["version"], "sha256": result["sha256"]},
        }
        recovered = {
            "schema_version": 2,
            "action_id": "action-001",
            "event": "recovered",
            "kind": "governed_file_state",
            "author": "test-user",
            "occurred_at": "2026-08-20T23:59:59+04:00",
            "llm_session": {"app": "codex", "uuid": "session-001"},
            "structural_scope": "PROJECT",
            "result": result,
            "recovery_evidence": evidence,
        }
        recovered["event_id"] = _expected_event_id(recovered)
        recovered = with_event_digest(recovered)
        completed = context["predictions"]["journal_records"][0]
        assert isinstance(completed, dict)
        completed = copy.deepcopy(completed)
        completed["previous_result_event"] = recovered["event_id"]
        completed["event_id"] = _expected_event_id(completed)
        completed = with_event_digest(completed)
        context["previous_result_event"] = recovered["event_id"]
        context["recovery"] = {
            "event_id": recovered["event_id"],
            "result": result,
            "evidence": evidence,
            "evidence_digest": canonical_json_digest(evidence),
            "contradictions": [],
        }
        context["predictions"]["journal_records"] = [recovered, completed]
        context["context_id"] = _expected_context_id(context)
        output = run(self.root, {"context": context}, apply=True, wait_seconds=0)
        journal = self.root / ".caprmedio/work_journal/test-user-2026-08-20-part-1.ndjson"
        records = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertEqual(["recovered", "completed"], [record["event"] for record in records])
        self.assertEqual(recovered["event_id"], records[-1]["previous_result_event"])
        release_verified_lease(self.root, output["result"]["lease"])

    def test_consumes_the_actual_commit_context_schema(self) -> None:
        parent = self.root / ".caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        parent.parent.mkdir(parents=True, exist_ok=True)
        parent.write_text("---\nversion: 1\nrelations: {}\n---\n# Parent\n\nBody\n", encoding="utf-8")
        subject = self.root / ".caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        subject.write_text(
            "---\nversion: 1\nrelations:\n  child_of:\n    - CA-R-001-REQUIREMENT--parent\n---\n# Subject\n\nBody\n",
            encoding="utf-8",
        )
        self.run_git("config", "github.username", "test-user")
        repository_id = self.repository_identity()
        adapter_id = "test"
        source_event_id = "source-event"
        trigger = {
            "schema_version": 1,
            "trigger_id": canonical_json_digest(
                {
                    "schema_version": 1,
                    "adapter_id": adapter_id,
                    "source_event_id": source_event_id,
                    "repository_id": repository_id,
                }
            ),
            "adapter": {"id": adapter_id},
            "source_event_id": source_event_id,
            "repository": {"root": str(self.root.resolve()), "identity": repository_id},
            "observed_at": "2026-08-20T23:59:59+04:00",
            "before_path": None,
            "after_path": subject.relative_to(self.root).as_posix(),
            "llm_session": {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        }
        context = gather_context(self.root, trigger)
        output = run(self.root, {"context": context}, apply=False, wait_seconds=0)
        self.assertTrue(output["ok"])
        self.assertEqual("dry-run", output["mode"])


if __name__ == "__main__":
    unittest.main()
