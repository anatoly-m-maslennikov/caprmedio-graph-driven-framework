"""Isolated tests for the concrete public-release Git/GitHub binding seam."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from hashlib import sha256
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
PUBLIC_RELEASE = TOOLS / "PUBLIC_RELEASE"
for path in (str(TOOLS), str(PUBLIC_RELEASE)):
    if path not in sys.path:
        sys.path.insert(0, path)

from native_bindings import NativeCommandEvidence, NativePublicReleaseBindings, NativePublicReleaseError  # noqa: E402
from public_release import GateResult, PullRequest, PublicReleaseError, PublicReleaseInterrupted, ToolCallEvidence  # noqa: E402


OWNER = "anatoly-m-maslennikov"
REPOSITORY = "caprmedio-graph-driven-framework"
INITIAL = "a" * 64
FINAL = "b" * 64


class FakeRunner:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.calls: list[tuple[str, ...]] = []
        self.responses: dict[tuple[str, ...], list[subprocess.CompletedProcess[str]]] = {}

    def add(self, argv: tuple[str, ...], stdout: str = "") -> None:
        self.responses.setdefault(argv, []).append(subprocess.CompletedProcess(argv, 0, stdout, ""))

    def __call__(self, argv, **_kwargs):
        command = tuple(argv)
        self.calls.append(command)
        queue = self.responses.get(command)
        if not queue:
            return subprocess.CompletedProcess(command, 1, "", "fixture missing command")
        return queue.pop(0)


class Recorder:
    def __init__(self) -> None:
        self.rows: list[NativeCommandEvidence] = []

    def __call__(self, item: NativeCommandEvidence) -> ToolCallEvidence:
        self.rows.append(item)
        prefix = f"evidence/{item.operation.replace(':', '-')}.json"
        return ToolCallEvidence(
            f"inputs/{item.operation}.json", prefix,
            (f"effects/{item.operation}.json",) if item.effect else (),
            (prefix,),
        )


class NativePublicReleaseBindingsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.temp.name).resolve()
        (self.root / ".git").mkdir()
        (self.root / "README.md").write_text("# CAPRMEDIO\n\nPublic release.\n", encoding="utf-8")
        docs = self.root / "docs"
        docs.mkdir()
        (docs / "public-pr.md").write_text(
            "# Public release\n\n## What's new\n\n- Native binding.\n\n## What's fixed\n\n- Exact evidence.\n",
            encoding="utf-8",
        )
        (self.root / "VERSION_HISTORY.md").write_text("- Public native binding.\n", encoding="utf-8")
        (self.root / "version.toml").write_text("[framework]\nversion = \"0.4.1\"\n", encoding="utf-8")
        self.runner = FakeRunner(self.root)
        self.recorder = Recorder()
        self.candidates: dict[str, str] = {"after_history_finalization": INITIAL}
        self.admissions: list[str] = []
        self._bind_commands()
        self.bindings = NativePublicReleaseBindings(
            self.root,
            effect_admitter=self.admit,
            candidate_observer=self.candidate,
            evidence_recorder=self.recorder,
            command_runner=self.runner,
        )

    def tearDown(self) -> None:
        self.temp.cleanup()

    def parameters(self) -> dict[str, object]:
        return {
            "release": {
                "selected_version": "0.4.1", "release_branch": "amm/dev", "target_branch": "main",
                "remote": {"scope": "personal", "name": "githuba", "owner": OWNER, "repository": REPOSITORY},
            },
            "source": {
                "candidate_snapshot_manifest_sha256": INITIAL, "readme_ref": "README.md",
                "pr_body_ref": "docs/public-pr.md", "version_history_ref": "VERSION_HISTORY.md",
                "version_history_summary": "Public native binding.",
            },
            "recovery": {"prior_push": "not_started", "prior_pr": "not_started"},
        }

    def admit(self, operation, _parameters, _source) -> None:
        self.admissions.append(operation)

    def candidate(self, _parameters, phase) -> str:
        return self.candidates.get(phase, INITIAL)

    def _bind_commands(self) -> None:
        root = str(self.root)
        for _ in range(20):
            self.runner.add(("git", "-C", root, "rev-parse", "--show-toplevel"), root + "\n")
            self.runner.add(("git", "-C", root, "branch", "--show-current"), "amm/dev\n")
            self.runner.add(("git", "-C", root, "remote", "get-url", "githuba"), f"git@githuba:{OWNER}/{REPOSITORY}.git\n")

    def _list(self, rows: list[dict[str, object]]) -> None:
        self.runner.add(
            ("gh", "pr", "list", "--repo", f"{OWNER}/{REPOSITORY}", "--state", "open", "--head", "amm/dev",
             "--base", "main", "--json", "number,url,headRefName,baseRefName,state"),
            json.dumps(rows),
        )

    @staticmethod
    def pr(number: int = 42) -> dict[str, object]:
        return {"number": number, "url": f"https://github.com/{OWNER}/{REPOSITORY}/pull/{number}",
                "headRefName": "amm/dev", "baseRefName": "main", "state": "OPEN"}

    def prepare(self):
        return self.bindings.prepare_public_materials(self.parameters(), None)

    def queue_push_through_commit(self):
        prepared = self.prepare()
        root = str(self.root)
        allowed = ("README.md", "docs/public-pr.md", "VERSION_HISTORY.md")
        self.runner.add(("git", "-C", root, "diff", "--cached", "--name-only"))
        self.runner.add(("git", "-C", root, "status", "--porcelain=v1", "--untracked-files=all"), " M README.md\n M docs/public-pr.md\n")
        self.runner.add(("git", "-C", root, "add", "--", *allowed))
        self.runner.add(("git", "-C", root, "diff", "--cached", "--name-only"), "README.md\ndocs/public-pr.md\n")
        self.runner.add(("git", "-C", root, "commit", "-m", "docs: prepare public release 0.4.1"))
        commit = "c" * 40
        self.runner.add(("git", "-C", root, "rev-parse", "HEAD"), commit + "\n")
        push = ("git", "-C", root, "push", "githuba", "HEAD:refs/heads/amm/dev")
        self.runner.add(push)
        return prepared, commit, push

    def test_discovery_binds_selected_project_remote_and_exact_branch(self) -> None:
        self._list([self.pr()])
        result = self.bindings.discover_matching_pr(self.parameters())
        self.assertEqual((PullRequest(f"https://github.com/{OWNER}/{REPOSITORY}/pull/42", 42, "amm/dev", "main"),), result.matches)
        self.assertEqual("discover_matching_pr", self.recorder.rows[-1].operation)
        self.assertTrue(all(isinstance(part, str) for command in self.recorder.rows[-1].commands for part in command))
        self.assertFalse(self.admissions)

    def test_remote_requires_canonical_github_or_personal_ssh_identity(self) -> None:
        allowed = (
            f"git@githuba:{OWNER}/{REPOSITORY}.git",
            f"git@github.com:{OWNER}/{REPOSITORY}.git",
            f"https://github.com/{OWNER}/{REPOSITORY}.git",
            f"ssh://git@github.com/{OWNER}/{REPOSITORY}.git",
            f"ssh://git@githuba/{OWNER}/{REPOSITORY}.git",
        )
        for url in allowed:
            with self.subTest(url=url):
                NativePublicReleaseBindings._assert_remote_target(url, OWNER, REPOSITORY)
        denied = (
            f"https://attacker.invalid/{OWNER}/{REPOSITORY}.git",
            f"https://token@github.com/{OWNER}/{REPOSITORY}.git",
            f"https://github.com:443/{OWNER}/{REPOSITORY}.git",
            f"ssh://git@attacker.invalid/{OWNER}/{REPOSITORY}.git",
            f"ssh://other@github.com/{OWNER}/{REPOSITORY}.git",
            f"ssh://git@github.com:22/{OWNER}/{REPOSITORY}.git",
        )
        for url in denied:
            with self.subTest(url=url), self.assertRaisesRegex(NativePublicReleaseError, "unsafe-remote"):
                NativePublicReleaseBindings._assert_remote_target(url, OWNER, REPOSITORY)

    def test_prepare_reopens_full_pr_body_and_exact_document_bytes(self) -> None:
        prepared = self.prepare()
        self.assertEqual(INITIAL, prepared.source.candidate_snapshot_manifest_sha256)
        self.assertEqual(sha256((self.root / "docs/public-pr.md").read_bytes()).hexdigest(), prepared.source.pr_body_sha256)
        (self.root / "README.md").write_text("changed\n", encoding="utf-8")
        with self.assertRaisesRegex(NativePublicReleaseError, "source-proof-stale"):
            self.bindings.commit_and_push(self.parameters(), prepared.source, "initial")
        self.assertNotIn("commit_and_push:initial", self.admissions)

    def test_generated_document_capture_derives_its_summary_and_pr_link_from_current_bytes(self) -> None:
        (self.root / "VERSION_HISTORY.md").write_text(
            "# Version History\n\n## 0.4.1\n- Generated new material.\n- Generated fixed material.\n",
            encoding="utf-8",
        )
        self.bindings.begin_generated_public_materials(self.parameters())
        generated = self.bindings.capture_generated_public_materials(self.parameters())

        self.assertEqual("Generated new material.; Generated fixed material.", generated.source.version_history_summary)
        self.assertIsNone(generated.source.version_history_pr_url)
        self.assertIn("prepare_generated_public_materials", self.admissions)

        pull_request = PullRequest(
            f"https://github.com/{OWNER}/{REPOSITORY}/pull/42", 42, "amm/dev", "main",
        )
        self.bindings.begin_generated_history_link(self.parameters(), generated.source)
        (self.root / "VERSION_HISTORY.md").write_text(
            "# Version History\n\n## 0.4.1 [PR](https://github.com/"
            f"{OWNER}/{REPOSITORY}/pull/42)\n- Generated new material.\n- Generated fixed material.\n",
            encoding="utf-8",
        )
        linked = self.bindings.capture_generated_public_materials(self.parameters(), pull_request)

        self.assertEqual(pull_request.url, linked.source.version_history_pr_url)
        self.assertEqual(generated.source.version_history_summary, linked.source.version_history_summary)
        self.assertIn("prepare_generated_history_link", self.admissions)

    def test_push_refuses_before_git_add_when_admission_rejects(self) -> None:
        prepared = self.prepare()

        def reject(_operation, _parameters, _source):
            raise RuntimeError("revoked")

        self.bindings._effect_admitter = reject
        with self.assertRaisesRegex(NativePublicReleaseError, "native-admission-unproven"):
            self.bindings.commit_and_push(self.parameters(), prepared.source, "initial")
        self.assertFalse(any("add" in command for command in self.runner.calls))

    def test_push_stages_only_public_files_and_verifies_remote_head(self) -> None:
        prepared, commit, _push = self.queue_push_through_commit()
        root = str(self.root)
        self.runner.add(("git", "-C", root, "ls-remote", "--heads", "githuba", "refs/heads/amm/dev"), f"{commit}\trefs/heads/amm/dev\n")
        result = self.bindings.commit_and_push(self.parameters(), prepared.source, "initial")
        self.assertEqual(commit, result.commit_sha)
        self.assertEqual("effects/commit_and_push:initial.json", result.call.effect_refs[0])
        self.assertIn("commit_and_push:initial", self.admissions)

    def test_push_verification_failure_after_success_is_interrupted(self) -> None:
        prepared, _commit, push = self.queue_push_through_commit()
        with self.assertRaises(PublicReleaseInterrupted):
            self.bindings.commit_and_push(self.parameters(), prepared.source, "initial")
        self.assertEqual(1, self.runner.calls.count(push))

    def test_upsert_rejects_incomplete_pr_body_before_gh_effect(self) -> None:
        (self.root / "docs/public-pr.md").write_text("## What's new\n\n- only.\n", encoding="utf-8")
        with self.assertRaisesRegex(PublicReleaseError, "source-proof-invalid"):
            self.prepare()
        self.assertFalse(any(command[:3] == ("gh", "pr", "create") for command in self.runner.calls))

    def test_upsert_uses_body_file_and_observes_created_pr(self) -> None:
        prepared = self.prepare()
        self._list([])
        create = ("gh", "pr", "create", "--repo", f"{OWNER}/{REPOSITORY}", "--head", "amm/dev", "--base", "main",
                  "--title", "CAPRMEDIO 0.4.1 public release", "--body-file", "docs/public-pr.md")
        self.runner.add(create, "https://github.com/example/ignored/pull/1\n")
        self._list([self.pr()])
        result = self.bindings.upsert_main_pr(self.parameters(), prepared.source, None, "initial")
        self.assertEqual(42, result.pull_request.number)
        self.assertIn("upsert_main_pr:initial", self.admissions)
        self.assertIn(create, self.runner.calls)

    def test_unknown_create_outcome_is_interrupted_not_replayed(self) -> None:
        prepared = self.prepare()
        self._list([])
        create = ("gh", "pr", "create", "--repo", f"{OWNER}/{REPOSITORY}", "--head", "amm/dev", "--base", "main",
                  "--title", "CAPRMEDIO 0.4.1 public release", "--body-file", "docs/public-pr.md")
        self.runner.responses[create] = [subprocess.CompletedProcess(create, 1, "", "network")]
        with self.assertRaises(PublicReleaseInterrupted):
            self.bindings.upsert_main_pr(self.parameters(), prepared.source, None, "initial")
        self.assertEqual(1, self.runner.calls.count(create))

    def test_create_success_with_failed_rediscovery_is_interrupted(self) -> None:
        prepared = self.prepare()
        self._list([])
        create = ("gh", "pr", "create", "--repo", f"{OWNER}/{REPOSITORY}", "--head", "amm/dev", "--base", "main",
                  "--title", "CAPRMEDIO 0.4.1 public release", "--body-file", "docs/public-pr.md")
        self.runner.add(create, "https://github.com/example/ignored/pull/1\n")
        with self.assertRaises(PublicReleaseInterrupted):
            self.bindings.upsert_main_pr(self.parameters(), prepared.source, None, "initial")
        self.assertEqual(1, self.runner.calls.count(create))

    def test_edit_success_with_failed_reopen_is_interrupted(self) -> None:
        prepared = self.prepare()
        self._list([self.pr()])
        edit = ("gh", "pr", "edit", "42", "--repo", f"{OWNER}/{REPOSITORY}",
                "--title", "CAPRMEDIO 0.4.1 public release", "--body-file", "docs/public-pr.md")
        self.runner.add(edit)
        with self.assertRaises(PublicReleaseInterrupted):
            self.bindings.upsert_main_pr(self.parameters(), prepared.source, None, "initial")
        self.assertEqual(1, self.runner.calls.count(edit))

    def test_effect_evidence_failure_after_create_is_interrupted(self) -> None:
        prepared = self.prepare()
        self._list([])
        create = ("gh", "pr", "create", "--repo", f"{OWNER}/{REPOSITORY}", "--head", "amm/dev", "--base", "main",
                  "--title", "CAPRMEDIO 0.4.1 public release", "--body-file", "docs/public-pr.md")
        self.runner.add(create, "https://github.com/example/ignored/pull/1\n")
        self._list([self.pr()])

        def unavailable(_evidence):
            raise OSError("journal unavailable")

        self.bindings._evidence_recorder = unavailable
        with self.assertRaises(PublicReleaseInterrupted):
            self.bindings.upsert_main_pr(self.parameters(), prepared.source, None, "initial")
        self.assertEqual(1, self.runner.calls.count(create))

    def test_history_finalization_keeps_candidate_and_proves_actual_link(self) -> None:
        prepared = self.prepare()
        pr = PullRequest(f"https://github.com/{OWNER}/{REPOSITORY}/pull/42", 42, "amm/dev", "main")
        with self.assertRaisesRegex(NativePublicReleaseError, "history-finalizer-required"):
            self.bindings.finalize_history_link(self.parameters(), prepared.source, pr)
        self.assertEqual("- Public native binding.\n", (self.root / "VERSION_HISTORY.md").read_text(encoding="utf-8"))

        def finalize(_parameters, _source, _pr, line):
            (self.root / "VERSION_HISTORY.md").write_text(line + "\n", encoding="utf-8")
            return INITIAL

        self.bindings._history_link_finalizer = finalize
        result = self.bindings.finalize_history_link(self.parameters(), prepared.source, pr)
        self.assertTrue(result.changed)
        self.assertEqual(INITIAL, result.source.candidate_snapshot_manifest_sha256)
        self.assertEqual(prepared.source.readme_sha256, result.source.readme_sha256)
        self.assertEqual(prepared.source.pr_body_sha256, result.source.pr_body_sha256)
        self.assertNotEqual(prepared.source.version_history_sha256, result.source.version_history_sha256)
        self.assertNotEqual(prepared.source.public_document_closure_sha256, result.source.public_document_closure_sha256)
        self.assertIn(pr.url, (self.root / "VERSION_HISTORY.md").read_text(encoding="utf-8"))

    def test_history_fake_changed_candidate_is_interrupted_even_when_observer_agrees(self) -> None:
        prepared = self.prepare()
        pr = PullRequest(f"https://github.com/{OWNER}/{REPOSITORY}/pull/42", 42, "amm/dev", "main")

        def finalize(_parameters, _source, _pr, line):
            (self.root / "VERSION_HISTORY.md").write_text(line + "\n", encoding="utf-8")
            return FINAL

        self.bindings._history_link_finalizer = finalize
        self.candidates["after_history_finalization"] = FINAL
        with self.assertRaises(PublicReleaseInterrupted) as rejected:
            self.bindings.finalize_history_link(self.parameters(), prepared.source, pr)
        self.assertEqual("new-local-cycle-required", rejected.exception.__cause__.code)
        self.assertIn(pr.url, (self.root / "VERSION_HISTORY.md").read_text(encoding="utf-8"))

    def test_history_callback_cannot_change_readme_bytes(self) -> None:
        prepared = self.prepare()
        pr = PullRequest(f"https://github.com/{OWNER}/{REPOSITORY}/pull/42", 42, "amm/dev", "main")

        def finalize(_parameters, _source, _pr, line):
            (self.root / "VERSION_HISTORY.md").write_text(line + "\n", encoding="utf-8")
            (self.root / "README.md").write_text("# Changed README\n", encoding="utf-8")
            return INITIAL

        self.bindings._history_link_finalizer = finalize
        with self.assertRaises(PublicReleaseInterrupted) as rejected:
            self.bindings.finalize_history_link(self.parameters(), prepared.source, pr)
        self.assertEqual("history-link-invalid", rejected.exception.__cause__.code)
        self.assertFalse(any(row.operation == "finalize_history_link" for row in self.recorder.rows))

    def test_full_gate_requires_real_callback_and_admission(self) -> None:
        prepared = self.prepare()
        with self.assertRaisesRegex(NativePublicReleaseError, "full-gate-binding-required"):
            self.bindings.run_full_gate(self.parameters(), prepared.source, "initial")
        self.assertIn("run_full_gate:initial", self.admissions)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
