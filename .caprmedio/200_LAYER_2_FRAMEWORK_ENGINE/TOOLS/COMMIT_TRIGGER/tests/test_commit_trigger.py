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

    def _write_atom(self, path: str, *, version: int, body: str) -> None:
        target = self.repository / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(
            f"---\nversion: {version}\nrelations:\n---\n# {target.stem}\n\n{body}\n",
            encoding="utf-8",
        )

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
            after_path=".caprmedio_runtime/state/commit_change_set/action-001.json",
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
        carrier = ".caprmedio/work_journal/alice-2026-08-20-part-1.ndjson"
        state = current[carrier]
        transition = {
            "event_id": "event-001",
            "event_digest": hashlib.sha256(b"event").hexdigest(),
            "carrier": carrier,
            "line": state.line_count,
            "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
            "appended_carrier_digest": state.sha256,
        }
        correlation_id = commit_trigger._sha256({"action_id": "action-001", "transition": transition})
        observations = commit_trigger.detect_watch_observations(
            previous,
            current,
            adapter_id=self.adapter.adapter_id,
            repository=self.repository,
            observed_at="2026-08-20T20:21:22Z",
            correlations={
                carrier: (
                    commit_trigger.PipelineCorrelation(
                        correlation_id=correlation_id,
                        action_id="action-001",
                        **transition,
                    ),
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

    def test_native_watch_pairs_move_and_update_by_stable_carrier_identity(self) -> None:
        control_root = self.repository / ".caprmedio"
        old = control_root / "04_requirement" / "CA-R-001-REQUIREMENT--old-summary.md"
        old.parent.mkdir(parents=True)
        old.write_text("---\nversion: 1\nrelations: {}\n---\n# Old\n", encoding="utf-8")
        previous = commit_trigger.scan_governed_files(self.repository)

        new = control_root / "100_LAYER_1_META" / "04_requirement" / "CA-R-001-REQUIREMENT--new-summary.md"
        new.parent.mkdir(parents=True)
        old.replace(new)
        new.write_text("---\nversion: 2\nrelations: {}\n---\n# New\n", encoding="utf-8")
        current = commit_trigger.scan_governed_files(self.repository)

        observations = commit_trigger.detect_watch_observations(
            previous,
            current,
            adapter_id=self.adapter.adapter_id,
            repository=self.repository,
            observed_at="2026-08-20T20:21:22Z",
        )
        affected = [
            observation
            for observation in observations
            if observation.get("before_path") == old.relative_to(self.repository).as_posix()
            or observation.get("after_path") == new.relative_to(self.repository).as_posix()
        ]
        self.assertEqual(len(affected), 1)
        self.assertEqual(affected[0]["before_path"], old.relative_to(self.repository).as_posix())
        self.assertEqual(affected[0]["after_path"], new.relative_to(self.repository).as_posix())

    def test_digest_bound_correlation_replay_and_retirement(self) -> None:
        carrier = ".caprmedio/work_journal/alice-2026-08-20-part-1.ndjson"
        transition = {
            "event_id": "event-001",
            "event_digest": hashlib.sha256(b"event").hexdigest(),
            "carrier": carrier,
            "line": 1,
            "previous_carrier_digest": hashlib.sha256(b"").hexdigest(),
            "appended_carrier_digest": hashlib.sha256(b"record\n").hexdigest(),
        }
        action_id = "action-001"
        correlation_id = commit_trigger._sha256({"action_id": action_id, "transition": transition})
        path = self.repository / ".caprmedio_runtime/state/commit_trigger/pipeline_correlations.ndjson"
        path.parent.mkdir(parents=True, exist_ok=True)
        registered = {
            "schema_version": 1,
            "event": "registered",
            "correlation_id": correlation_id,
            "action_id": action_id,
            "transition": transition,
        }
        path.write_text(json.dumps(registered, sort_keys=True) + "\n", encoding="utf-8")
        active = commit_trigger._read_pipeline_correlations(path)
        self.assertEqual([item.correlation_id for item in active[carrier]], [correlation_id])
        retired = {
            "schema_version": 1,
            "event": "retired",
            "correlation_id": correlation_id,
            "action_id": action_id,
        }
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(retired, sort_keys=True) + "\n")
        self.assertEqual(commit_trigger._read_pipeline_correlations(path), {})

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

    def test_runtime_install_is_content_addressed_and_self_contained(self) -> None:
        status = commit_trigger.install_runtime_package(self.repository, apply=True)

        self.assertTrue(status["installed"])
        self.assertTrue(status["verified"])
        release_root = self.repository / str(status["package_root"])
        self.assertTrue((release_root / "manifest.toml").is_file())
        self.assertEqual(8, status["file_count"])
        for relative in (
            "COMMIT_TRIGGER/commit_trigger.py",
            "COMMIT_CONTEXT/commit_context.py",
            "APPEND_CHANGE_RECORDS/append_change_records.py",
            "COMMIT_CHANGE_SET/commit_change_set.py",
        ):
            completed = subprocess.run(
                [sys.executable, "-I", "-B", str(release_root / relative), "--repository", str(self.repository), "describe"],
                check=True,
                capture_output=True,
                text=True,
                cwd=self.repository,
                env={"PATH": os.environ.get("PATH", "")},
            )
            self.assertTrue(json.loads(completed.stdout)["ok"], relative)

    def test_project_codex_hook_runs_installed_pipeline_and_commits_one_atom(self) -> None:
        (self.repository / ".gitignore").write_text("/.caprmedio_runtime/\n/.codex/hooks.json\n", encoding="utf-8")
        (self.repository / ".caprmedio").mkdir()
        (self.repository / ".caprmedio/caprmedio_project_settings.toml").write_text(
            "[artifact_timestamps]\ntimezone = \"Asia/Tbilisi\"\n\n"
            "[paths]\njournal_root = \".caprmedio/work_journal\"\n"
            "runtime_root = \".caprmedio_runtime\"\n",
            encoding="utf-8",
        )
        subject = ".caprmedio/04_requirement/CA-R-001-REQUIREMENT--subject.md"
        self._write_atom(subject, version=1, body="first")
        self._git("config", "github.username", "anatoly-m-maslennikov")
        self._git("add", ".gitignore", ".caprmedio")
        self._git("commit", "-qm", "governed fixture")

        installed = commit_trigger.install_runtime_package(self.repository, apply=True)
        entrypoint = self.repository / str(installed["entrypoint"])
        subprocess.run(
            [
                sys.executable,
                "-I",
                "-B",
                str(entrypoint),
                "--repository",
                str(self.repository),
                "adapter",
                "install",
                "--adapter-id",
                self.adapter.adapter_id,
                "--application",
                "codex",
                "--host-session-env",
                "CODEX_THREAD_ID",
                "--fallback-session-env",
                "CODEX_SESSION_ID",
                "--apply",
            ],
            check=True,
            capture_output=True,
            text=True,
            cwd=self.repository,
        )
        hook_config = self.repository / ".codex/hooks.json"
        self.assertTrue(hook_config.is_symlink())
        self.assertEqual(
            (self.repository / ".caprmedio_runtime/hooks/codex/hooks.json").resolve(),
            hook_config.resolve(),
        )
        payload = {
            "session_id": self.environment["CODEX_THREAD_ID"],
            "tool_use_id": "tool-use-001",
            "cwd": str(self.repository),
        }

        for phase in ("pre", "post"):
            if phase == "post":
                self._write_atom(subject, version=2, body="second")
            completed = subprocess.run(
                [
                    sys.executable,
                    "-I",
                    "-B",
                    str(entrypoint),
                    "--repository",
                    str(self.repository),
                    "codex-hook",
                    phase,
                    "--adapter-id",
                    self.adapter.adapter_id,
                ],
                input=json.dumps(payload),
                check=True,
                capture_output=True,
                text=True,
                cwd=self.repository,
            )
            envelope = json.loads(completed.stdout)
            self.assertTrue(envelope["ok"], completed.stdout)

        self.assertEqual("committed", envelope["result"]["effect"])
        self.assertEqual(1, envelope["result"]["commit_count"])
        changed = self._git("diff-tree", "--no-commit-id", "--name-only", "-r", "HEAD").splitlines()
        self.assertIn(subject, changed)
        journals = [path for path in changed if path.startswith(".caprmedio/work_journal/")]
        self.assertEqual(1, len(journals))
        record = json.loads((self.repository / journals[0]).read_text(encoding="utf-8").splitlines()[-1])
        self.assertEqual(
            {"app": "codex", "uuid": self.environment["CODEX_THREAD_ID"]},
            record["llm_session"],
        )
        self.assertEqual("", self._git("status", "--porcelain=v1"))

    @staticmethod
    def _run_hook(hook: Path) -> None:
        subprocess.run([str(hook)], check=True, capture_output=True, text=True)


if __name__ == "__main__":
    unittest.main()
