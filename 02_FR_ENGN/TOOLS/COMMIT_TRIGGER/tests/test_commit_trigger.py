"""Deterministic acceptance tests for COMMIT_TRIGGER Evaluations E169, E186, E194."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import os
import stat
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "commit_trigger.py"
SPEC = importlib.util.spec_from_file_location("commit_trigger", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
commit_trigger = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = commit_trigger
SPEC.loader.exec_module(commit_trigger)


class CommitTriggerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repository = Path(self.temporary.name) / "repository"
        self.repository.mkdir()
        self._git("init", "-q")
        self._git("config", "user.name", "CAPRMEDIO Test")
        self._git("config", "user.email", "test@example.invalid")
        (self.repository / "README.md").write_text("fixture\n", encoding="utf-8")
        self._git("add", "README.md")
        self._git("commit", "-qm", "fixture")
        self.adapter = commit_trigger.AdapterSpec(
            "codex-file-events",
            "codex",
            "CODEX_THREAD_ID",
            "CODEX_SESSION_ID",
            True,
        )
        commit_trigger.adapter_operation(self.repository, "install", adapter=self.adapter, apply=True)
        self.environment = {"CODEX_THREAD_ID": "019f591f-04f6-70f2-8de7-828b7cccc69d"}

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _git(self, *arguments: str) -> str:
        completed = subprocess.run(
            ["git", "-C", str(self.repository), *arguments],
            check=True,
            capture_output=True,
            text=True,
        )
        return completed.stdout

    def _observation(self, **overrides: object) -> dict[str, object]:
        observation: dict[str, object] = {
            "adapter_id": self.adapter.adapter_id,
            "source_event_id": "host-event-001",
            "observed_at": "2026-08-20T20:21:22+00:00",
            "before_path": None,
            "after_path": ".caprmedio/04_requirement/CA-R-001.md",
        }
        observation.update(overrides)
        return observation

    def _snapshot(self) -> dict[str, object]:
        def files(root: Path) -> dict[str, str]:
            if not root.exists():
                return {}
            return {
                path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in sorted(root.rglob("*"))
                if path.is_file()
            }

        runtime = self.repository / ".caprmedio_runtime"
        journals = self.repository / ".caprmedio" / "work_journal"
        return {
            "status": self._git("status", "--porcelain=v1"),
            "index": (self.repository / ".git" / "index").read_bytes(),
            "head": self._git("rev-parse", "HEAD").strip(),
            "runtime": files(runtime),
            "journals": files(journals),
        }

    def test_e169_emit_one_stable_trigger_without_mutation(self) -> None:
        """Noisy delivery coalesces to one stable trigger and changes no state."""

        observation = self._observation()
        before = self._snapshot()
        triggers = commit_trigger.emit_from_registered_adapter(
            [observation, dict(observation), dict(observation)],
            repository=self.repository,
            adapter_id=self.adapter.adapter_id,
            environment=self.environment,
        )
        after = self._snapshot()

        self.assertEqual(len(triggers), 1)
        trigger = triggers[0]
        self.assertEqual(trigger["schema_version"], 1)
        self.assertEqual(trigger["adapter"], {"id": "codex-file-events"})
        self.assertEqual(trigger["source_event_id"], "host-event-001")
        self.assertEqual(trigger["observed_at"], "2026-08-20T20:21:22Z")
        self.assertEqual(trigger["before_path"], None)
        self.assertEqual(trigger["after_path"], ".caprmedio/04_requirement/CA-R-001.md")
        self.assertEqual(
            trigger["llm_session"],
            {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        )
        self.assertNotIn("occurred_at", trigger["llm_session"])
        self.assertEqual(before, after)

    def test_e186_adapter_lifecycle_preserves_existing_hook_bytes_and_behavior(self) -> None:
        """Registry-only lifecycle never changes an existing Git Hook carrier."""

        hook = self.repository / ".git" / "hooks" / "post-commit"
        sentinel = self.repository / "hook-sentinel.log"
        hook.write_text(f"#!/bin/sh\nprintf 'sentinel\\n' >> {sentinel}\n", encoding="utf-8")
        hook.chmod(0o751)
        original_bytes = hook.read_bytes()
        original_mode = stat.S_IMODE(hook.stat().st_mode)

        commit_trigger.adapter_operation(self.repository, "uninstall", adapter_id=self.adapter.adapter_id, apply=True)
        status_before = commit_trigger.adapter_operation(self.repository, "status")
        self.assertEqual(status_before["adapters"], [])
        self._run_hook(hook)

        commit_trigger.adapter_operation(self.repository, "install", adapter=self.adapter, apply=True)
        enabled = commit_trigger.emit_from_registered_adapter(
            [self._observation()], repository=self.repository, adapter_id=self.adapter.adapter_id, environment=self.environment
        )
        self._run_hook(hook)
        self.assertEqual(len(enabled), 1)

        commit_trigger.adapter_operation(self.repository, "disable", adapter_id=self.adapter.adapter_id, apply=True)
        disabled = commit_trigger.emit_from_registered_adapter(
            [self._observation()], repository=self.repository, adapter_id=self.adapter.adapter_id, environment=self.environment
        )
        self._run_hook(hook)
        self.assertEqual(disabled, [])

        commit_trigger.adapter_operation(self.repository, "uninstall", adapter_id=self.adapter.adapter_id, apply=True)
        uninstalled = commit_trigger.emit_from_registered_adapter(
            [self._observation()], repository=self.repository, adapter_id=self.adapter.adapter_id, environment=self.environment
        )
        self._run_hook(hook)
        self.assertEqual(uninstalled, [])
        self.assertEqual(hook.read_bytes(), original_bytes)
        self.assertEqual(stat.S_IMODE(hook.stat().st_mode), original_mode)
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "sentinel\nsentinel\nsentinel\nsentinel\n")
        self.assertFalse((self.repository / ".caprmedio_runtime" / "commit_trigger" / "backup").exists())

    def test_e194_suppress_correlated_journal_and_runtime_events(self) -> None:
        """Correlated pipeline side effects cannot recursively produce a trigger."""

        original = self._observation(source_event_id="subject-change")
        journal = self._observation(
            source_event_id="journal-write",
            before_path=None,
            after_path=".caprmedio/work_journal/alice-2026-08-20-part-1.ndjson",
            pipeline={"owned": True, "action_id": "action-001", "kind": "journal"},
        )
        runtime = self._observation(
            source_event_id="runtime-write",
            before_path=None,
            after_path=".caprmedio_runtime/commit_change_set/action-001.json",
            pipeline={"owned": True, "action_id": "action-001", "kind": "runtime-state"},
        )
        triggers = commit_trigger.emit_from_registered_adapter(
            [original, journal, runtime],
            repository=self.repository,
            adapter_id=self.adapter.adapter_id,
            environment=self.environment,
        )

        self.assertEqual([trigger["source_event_id"] for trigger in triggers], ["subject-change"])

    def test_native_codex_watch_detects_one_edit_and_suppresses_correlated_pipeline_write(self) -> None:
        """The non-invasive native adapter polls a source boundary without Hooks."""

        control_root = self.repository / ".caprmedio"
        control_root.mkdir()
        atom = control_root / "04_requirement" / "CA-R-001.md"

        def write_atom() -> None:
            time.sleep(0.04)
            atom.parent.mkdir(parents=True)
            atom.write_text("first revision\n", encoding="utf-8")

        writer = threading.Thread(target=write_atom)
        writer.start()
        batches = list(
            commit_trigger.watch_triggers(
                repository=self.repository,
                adapter=self.adapter,
                environment=self.environment,
                poll_interval=0.01,
                maximum_polls=12,
            )
        )
        writer.join()
        triggers = [trigger for batch in batches for trigger in batch]
        self.assertEqual(len(triggers), 1)
        self.assertEqual(triggers[0]["before_path"], None)
        self.assertEqual(triggers[0]["after_path"], ".caprmedio/04_requirement/CA-R-001.md")
        self.assertTrue(str(triggers[0]["source_event_id"]).startswith("watch-"))

        previous = commit_trigger.scan_governed_files(self.repository)
        journal = control_root / "work_journal" / "alice-2026-08-20-part-1.ndjson"
        journal.parent.mkdir()
        journal.write_text('{"event_id":"fixture"}\n', encoding="utf-8")
        current = commit_trigger.scan_governed_files(self.repository)
        observations = commit_trigger.detect_watch_observations(
            previous,
            current,
            adapter_id=self.adapter.adapter_id,
            repository=self.repository,
            observed_at="2026-08-20T20:21:22Z",
            correlations={
                ".caprmedio/work_journal/alice-2026-08-20-part-1.ndjson": commit_trigger.PipelineCorrelation(
                    "action-001", ".caprmedio/work_journal/alice-2026-08-20-part-1.ndjson", "journal"
                )
            },
        )
        self.assertEqual(len(observations), 1)
        self.assertEqual(observations[0]["pipeline"], {"owned": True, "action_id": "action-001", "kind": "journal"})
        self.assertEqual(
            commit_trigger.emit_triggers(
                observations,
                adapter=self.adapter,
                repository=self.repository,
                environment=self.environment,
            ),
            [],
        )

    def test_codex_host_resolution_prefers_thread_then_falls_back(self) -> None:
        self.assertEqual(
            commit_trigger.resolve_codex_session(
                environment={
                    "CODEX_THREAD_ID": "019f591f-04f6-70f2-8de7-828b7cccc69d",
                    "CODEX_SESSION_ID": "019f5920-04f6-70f2-8de7-828b7cccc69d",
                }
            ),
            {"app": "codex", "uuid": "019f591f-04f6-70f2-8de7-828b7cccc69d"},
        )
        self.assertEqual(
            commit_trigger.resolve_codex_session(environment={"CODEX_SESSION_ID": "019f5920-04f6-70f2-8de7-828b7cccc69d"}),
            {"app": "codex", "uuid": "019f5920-04f6-70f2-8de7-828b7cccc69d"},
        )

    def test_cli_exposes_machine_readable_contract_and_unchanged_handoff(self) -> None:
        observation_path = self.repository / "observation.json"
        observation_path.write_text(json.dumps(self._observation()), encoding="utf-8")
        completed = subprocess.run(
            [
                sys.executable,
                str(SCRIPT),
                "--repository",
                str(self.repository),
                "observe",
                "--adapter-id",
                self.adapter.adapter_id,
                "--input",
                str(observation_path),
            ],
            check=True,
            capture_output=True,
            text=True,
            env={**os.environ, **self.environment},
        )
        envelope = json.loads(completed.stdout)
        self.assertTrue(envelope["ok"])
        self.assertEqual(envelope["tool"], {"capability_id": "COMMIT_TRIGGER", "kind": "hook"})
        handoff = envelope["result"]["handoffs"][0]
        self.assertEqual(handoff["interface"], "COMMIT_CHANGE_SET")
        self.assertEqual(handoff["trigger"]["llm_session"]["app"], "codex")

    @staticmethod
    def _run_hook(hook: Path) -> None:
        subprocess.run([str(hook)], check=True, capture_output=True, text=True)


if __name__ == "__main__":
    unittest.main()
