"""Deterministic acceptance tests for COMMIT_CHANGE_SET Evaluations E179, E196-E204, and E211-E213."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "commit_change_set.py"
SPEC = importlib.util.spec_from_file_location("commit_change_set", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
commit_change_set = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = commit_change_set
SPEC.loader.exec_module(commit_change_set)

class CommitChangeSetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / ".caprmedio").mkdir()
        (self.root / ".caprmedio/caprmedio_project_settings.toml").write_text(
            "[artifact_timestamps]\ntimezone = \"Asia/Tbilisi\"\n\n[paths]\njournal_root = \".caprmedio/work_journal\"\nruntime_root = \".caprmedio_runtime\"\n",
            encoding="utf-8",
        )
        self.git("init", "-q")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "CAPRMEDIO Test")
        self.git("config", "github.username", "anatoly-m-maslennikov")
        self.write_atom(".caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md", version=1, relations={})
        self.write_atom(
            ".caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md",
            version=1,
            relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]},
            body="first",
        )
        self.git("add", ".")
        self.git("commit", "-qm", "fixture")
        self.subject = ".caprmedio/04_requirement/CA-R-002-REQUIREMENT--subject.md"
        self.write_atom(self.subject, version=2, relations={"child_of": ["CA-R-001-REQUIREMENT--parent"]}, body="second")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def git(self, *arguments: str) -> str:
        return subprocess.run(["git", "-C", str(self.root), *arguments], check=True, capture_output=True, text=True).stdout

    def write_atom(self, path: str, *, version: int, relations: dict[str, list[str]], body: str = "Body") -> None:
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        relation_lines = "relations:\n" + "".join(
            f"  {kind}:\n" + "".join(f"    - {item}\n" for item in values) for kind, values in relations.items()
        )
        target.write_text(f"---\nversion: {version}\n{relation_lines}---\n# {target.stem}\n\n{body}\n", encoding="utf-8")

    def trigger(self) -> dict[str, object]:
        git_directory = (self.root / self.git("rev-parse", "--git-dir").strip()).resolve()
        repository_identity = hashlib.sha256(
            json.dumps(
                {"repository_root": self.root.resolve().as_posix(), "git_directory": git_directory.as_posix()},
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        adapter_id = "codex-test"
        source_event_id = "source-event-1"
        trigger_id = hashlib.sha256(
            json.dumps(
                {
                    "schema_version": 1,
                    "adapter_id": adapter_id,
                    "source_event_id": source_event_id,
                    "repository_id": repository_identity,
                },
                sort_keys=True,
                separators=(",", ":"),
            ).encode("utf-8")
        ).hexdigest()
        return {
            "schema_version": 1,
            "trigger_id": trigger_id,
            "adapter": {"id": adapter_id},
            "source_event_id": source_event_id,
            "repository": {"root": str(self.root), "identity": repository_identity},
            "observed_at": "2026-08-20T20:21:22Z",
            "before_path": self.subject,
            "after_path": self.subject,
            "llm_session": {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        }

    def snapshot(self) -> dict[str, object]:
        def files(path: Path) -> dict[str, str]:
            if not path.exists():
                return {}
            return {
                item.relative_to(self.root).as_posix(): hashlib.sha256(item.read_bytes()).hexdigest()
                for item in sorted(path.rglob("*"))
                if item.is_file()
            }

        return {
            "status": self.git("status", "--porcelain=v1"),
            "index": (self.root / ".git/index").read_bytes(),
            "head": self.git("rev-parse", "HEAD").strip(),
            "runtime": files(self.root / ".caprmedio_runtime"),
            "journal": files(self.root / ".caprmedio/work_journal"),
        }

    def append_only(self) -> tuple[dict[str, object], dict[str, object]]:
        context = commit_change_set.gather_context(self.root, self.trigger())
        appender = commit_change_set._import_appender()
        envelope = appender.run(self.root, {"context": context}, apply=True, wait_seconds=0)
        self.assertTrue(envelope["ok"])
        return context, envelope["result"]

    def stage_appended(self) -> dict[str, object]:
        context, appended = self.append_only()
        events = context["predictions"]["journal_records"]
        commit_change_set._stage_subject(self.root, context)
        commit_change_set._stage_receipt_sidecars(self.root, events, appended["receipts"])
        return context

    def test_e179_dry_run_is_fully_mutation_free(self) -> None:
        before = self.snapshot()
        result = commit_change_set.run(self.root, {"trigger": self.trigger()}, apply=False, wait_seconds=0)
        self.assertEqual(before, self.snapshot())
        self.assertEqual("UPDATE", result["change_set"]["action_type"])
        self.assertTrue(result["journal_records"])
        self.assertTrue(result["git_message"])
        self.assertEqual("available", result["lease"]["status"])

    def test_e199_commits_subject_and_only_receipt_bound_sidecars(self) -> None:
        result = commit_change_set.run(self.root, {"trigger": self.trigger()}, apply=True, wait_seconds=0)
        changed = set(self.git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines())
        self.assertIn(self.subject, changed)
        self.assertEqual(2, len(changed), changed)
        journal = next(path for path in changed if path.endswith(".ndjson"))
        records = [json.loads(line) for line in (self.root / journal).read_text(encoding="utf-8").splitlines()]
        self.assertEqual([receipt["event_id"] for receipt in result["receipts"]], [record["event_id"] for record in records])
        self.assertEqual(len(result["receipts"]), len(result["pipeline_correlations"]))
        self.assertEqual("released", result["lease"]["status"])
        self.assertFalse((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").exists())

    def test_e196_rejects_missing_receipts_without_runtime_mutation(self) -> None:
        context = commit_change_set.gather_context(self.root, self.trigger())
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "receipt") as captured:
            commit_change_set.run(self.root, {"context": context, "receipts": [], "lease": {}}, apply=True, wait_seconds=0)
        self.assertEqual("receipt-set-incomplete", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_e203_preserves_unrelated_staged_change_after_append(self) -> None:
        context, appended = self.append_only()
        unrelated = self.root / "unrelated.txt"
        unrelated.write_text("unrelated\n", encoding="utf-8")
        self.git("add", "unrelated.txt")
        with self.assertRaisesRegex(commit_change_set.ToolError, "staged") as captured:
            commit_change_set.run(
                self.root,
                {"context": context, "receipts": appended["receipts"], "lease": appended["lease"]},
                apply=True,
                wait_seconds=0,
            )
        self.assertEqual("unrelated-staged-change", captured.exception.code)
        self.assertTrue((self.root / ".caprmedio_runtime/state/append_change_records/blocked" / f"{context['action_id']}.json").is_file())
        self.assertEqual("unrelated.txt\0", self.git("diff", "--cached", "--name-only", "-z"))

    def test_e202_preserves_blocked_action_when_git_base_becomes_stale_after_append(self) -> None:
        context, appended = self.append_only()
        (self.root / "other.txt").write_text("independent commit\n", encoding="utf-8")
        self.git("add", "other.txt")
        self.git("commit", "-qm", "independent")
        with self.assertRaisesRegex(commit_change_set.ToolError, "Git base") as captured:
            commit_change_set.run(
                self.root,
                {"context": context, "receipts": appended["receipts"], "lease": appended["lease"]},
                apply=True,
                wait_seconds=0,
            )
        self.assertEqual("stale-context", captured.exception.code)
        blocked = self.root / ".caprmedio_runtime/state/append_change_records/blocked" / f"{context['action_id']}.json"
        self.assertTrue(blocked.is_file())
        self.assertTrue((self.root / ".caprmedio_runtime/state/commit_change_set/lease.json").is_file())

    def test_e204_records_proven_corrupted_context_after_append(self) -> None:
        context, appended = self.append_only()
        corrupted = dict(context)
        corrupted.pop("result")
        with self.assertRaisesRegex(commit_change_set.ToolError, "result"):
            commit_change_set.run(
                self.root,
                {"context": corrupted, "receipts": appended["receipts"], "lease": appended["lease"]},
                apply=True,
                wait_seconds=0,
            )
        blocked = self.root / ".caprmedio_runtime/state/append_change_records/blocked" / f"{context['action_id']}.json"
        self.assertTrue(blocked.is_file())
        payload = json.loads(blocked.read_text(encoding="utf-8"))
        self.assertEqual("invalid-context", payload["reason"])
        self.assertEqual([receipt["event_id"] for receipt in appended["receipts"]], [row["event_id"] for row in payload["receipt_refs"]])

    def test_allows_exact_already_staged_subject(self) -> None:
        self.git("add", self.subject)
        context = commit_change_set.gather_context(self.root, self.trigger())
        appender = commit_change_set._import_appender()
        appended = appender.run(self.root, {"context": context}, apply=True, wait_seconds=0)["result"]
        result = commit_change_set.run(
            self.root,
            {"context": context, "receipts": appended["receipts"], "lease": appended["lease"]},
            apply=True,
            wait_seconds=0,
        )
        self.assertEqual("released", result["lease"]["status"])
        self.assertEqual([], self.git("diff", "--cached", "--name-only").splitlines())

    def test_e211_pre_commit_rejects_atom_without_journal(self) -> None:
        self.git("add", self.subject)
        before = self.snapshot()
        with self.assertRaisesRegex(commit_change_set.ToolError, "Journal") as captured:
            commit_change_set.evaluate_pre_commit(self.root)
        self.assertEqual("governed-journal-missing", captured.exception.code)
        self.assertEqual(before, self.snapshot())

    def test_e211_pre_commit_accepts_exact_subject_and_sidecars_read_only(self) -> None:
        self.stage_appended()
        before = self.snapshot()
        result = commit_change_set.evaluate_pre_commit(self.root)
        self.assertTrue(result["governed"])
        self.assertEqual([self.subject], result["subject_paths"])
        self.assertEqual(before, self.snapshot())

    def test_e212_commit_message_requires_exact_projection(self) -> None:
        context = self.stage_appended()
        message_path = self.root / ".git" / "COMMIT_EDITMSG"
        expected = context["predictions"]["git_message"]
        message_path.write_text(expected + "\n", encoding="utf-8")
        before = message_path.read_bytes()
        result = commit_change_set.evaluate_commit_message(self.root, message_path)
        self.assertTrue(result["message_valid"])
        self.assertEqual(before, message_path.read_bytes())

        message_path.write_text(expected + "\nextra body\n", encoding="utf-8")
        changed = message_path.read_bytes()
        with self.assertRaisesRegex(commit_change_set.ToolError, "message") as captured:
            commit_change_set.evaluate_commit_message(self.root, message_path)
        self.assertEqual("commit-message-mismatch", captured.exception.code)
        self.assertEqual(changed, message_path.read_bytes())

    def test_e213_post_commit_observes_once_without_governed_mutation(self) -> None:
        commit_change_set.run(self.root, {"trigger": self.trigger()}, apply=True, wait_seconds=0)
        head = self.git("rev-parse", "HEAD").strip()
        journal_before = {
            path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
            for path in (self.root / ".caprmedio/work_journal").glob("*.ndjson")
        }

        first = commit_change_set.observe_post_commit(self.root)
        second = commit_change_set.observe_post_commit(self.root)

        self.assertTrue(first["valid"])
        self.assertTrue(first["governed"])
        self.assertTrue(first["observation_appended"])
        self.assertFalse(second["observation_appended"])
        log = self.root / first["observation"]
        self.assertEqual(1, len(log.read_text(encoding="utf-8").splitlines()))
        self.assertEqual(head, self.git("rev-parse", "HEAD").strip())
        self.assertEqual(
            journal_before,
            {
                path.relative_to(self.root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in (self.root / ".caprmedio/work_journal").glob("*.ndjson")
            },
        )


if __name__ == "__main__":
    unittest.main()
