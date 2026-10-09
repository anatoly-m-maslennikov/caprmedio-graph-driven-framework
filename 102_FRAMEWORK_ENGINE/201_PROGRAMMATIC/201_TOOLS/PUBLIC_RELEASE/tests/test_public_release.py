"""E2E contract coverage for the native public-release Workflow binding."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from hashlib import sha256
from pathlib import Path
from types import SimpleNamespace
from unittest import mock


TOOLS = Path(__file__).resolve().parents[2]
PUBLIC_RELEASE = TOOLS / "PUBLIC_RELEASE"
RELEASE_VERSION = TOOLS / "RELEASE_VERSION"
for path in (str(TOOLS), str(PUBLIC_RELEASE), str(RELEASE_VERSION)):
    if path not in sys.path:
        sys.path.insert(0, path)

from release_full_gate import FullGateEvidence  # noqa: E402
from work_journal import canonical_json_digest  # noqa: E402
from public_release import (  # noqa: E402
    CommitPushResult,
    FinalizationResult,
    FullGateBinding,
    GateResult,
    PRDiscovery,
    PRUpsertResult,
    PrepareResult,
    PublicReleaseError,
    PullRequest,
    SourceProof,
    ToolCallEvidence,
    VerifiedPushReceipt,
    describe,
    run,
)


def digest(value: object) -> str:
    return canonical_json_digest(value)


class MockBindings:
    def __init__(self, root: Path, *, existing: bool = False) -> None:
        self.root = root
        self.existing = existing
        self.calls: list[str] = []
        self.owner = "anatoly-m-maslennikov"
        self.repository = "caprmedio-graph-driven-framework"
        self.initial_sha = "a" * 64
        self.final_sha = "b" * 64
        self.interrupt_push = False
        self.bad_gate = False
        self.bad_version = False
        self.bad_source = False
        self.duplicate = False
        self.push_owner = self.owner

    def call(self, name: str, *, effect: bool = False, report: bool = False,
             outcome: str = "completed") -> ToolCallEvidence:
        self.calls.append(name)
        return ToolCallEvidence(
            f"inputs/{name}.json", f"results/{name}.json",
            (f"effects/{name}.json",) if effect else (),
            (f"reports/{name}.json",) if report else (), outcome,
        )

    def url_for(self, number: int = 42) -> str:
        return f"https://github.com/{self.owner}/{self.repository}/pull/{number}"

    def pr(self, *, number: int = 42) -> PullRequest:
        return PullRequest(self.url_for(number), number, "amm/dev", "main")

    @staticmethod
    def file_hash(text: str) -> str:
        return sha256(text.encode("utf-8")).hexdigest()

    def source(self, candidate: str, pr: PullRequest | None = None) -> SourceProof:
        summary = "Public release contract and workflow."
        readme = "# CAPRMEDIO\n\nPublic release materials.\n"
        body = "# Public release\n\n## What's new\n\n- Public workflow binding.\n\n## What's fixed\n\n- Bound remote receipts.\n"
        if self.bad_source:
            body = "# Public release\n\n## What's new\n\n- Public workflow binding.\n\n## What's fixed\n"
        history = f"- {summary}"
        if pr is not None:
            history += f" [PR #{pr.number}]({pr.url})"
        (self.root / "README.md").write_text(readme, encoding="utf-8")
        docs = self.root / "docs"
        docs.mkdir(exist_ok=True)
        (docs / "public-pr.md").write_text(body, encoding="utf-8")
        (self.root / "VERSION_HISTORY.md").write_text(history + "\n", encoding="utf-8")
        version_toml = (self.root / "version.toml").read_text(encoding="utf-8")
        return SourceProof(candidate, "0.4.1", self.file_hash(version_toml),
                           "README.md", self.file_hash(readme), "docs/public-pr.md", self.file_hash(body),
                           "VERSION_HISTORY.md", self.file_hash(history + "\n"), summary,
                           pr.url if pr else None, pr.number if pr else None)

    def discover_matching_pr(self, parameters):
        matches = (self.pr(), self.pr(number=43)) if self.duplicate else ((self.pr(),) if self.existing else ())
        return PRDiscovery(self.call("discover", report=True), matches)

    def prepare_public_materials(self, parameters, pr_url):
        return PrepareResult(
            self.call("prepare", effect=True),
            self.source(self.initial_sha, self.pr() if pr_url else None),
        )

    def run_full_gate(self, parameters, source, phase):
        sha = "c" * 64 if self.bad_gate else source.candidate_snapshot_manifest_sha256
        evidence = FullGateEvidence(sha, "sha256:" + "1" * 64, "2" * 64, "3" * 64,
                                    "4" * 64, "5" * 64, "6" * 64, "passed", "passed",
                                    ".caprmedio_runtime/release_full_gate/test", "7" * 64, 9,
                                    "0.4.2" if self.bad_version else "0.4.1", source.version_toml_sha256)
        candidate = SimpleNamespace(manifest=SimpleNamespace(sha256=sha, framework_version="0.4.1", version_toml_sha256=source.version_toml_sha256))
        return GateResult(self.call(f"gate-{phase}", report=True),
                          FullGateBinding(candidate, object(), object(), object(), object(), object(), evidence, object()))

    def commit_and_push(self, parameters, source, phase):
        outcome = "interrupted_pending" if self.interrupt_push and phase == "initial" else "completed"
        commit = "a1b2c3d4"
        return CommitPushResult(self.call(f"push-{phase}", effect=True, outcome=outcome), commit,
                                VerifiedPushReceipt(self.push_owner, self.repository, "amm/dev", commit,
                                                    f"receipts/push-{phase}.json"))

    def upsert_main_pr(self, parameters, source, known_url, phase):
        return PRUpsertResult(self.call(f"pr-{phase}", effect=True), self.pr())

    def finalize_history_link(self, parameters, source, pull_request):
        if self.existing:
            return FinalizationResult(self.call("finalize", report=True, outcome="no_op"), source, False)
        return FinalizationResult(
            self.call("finalize", effect=True),
            self.source(self.final_sha, pull_request),
            True,
        )


class PublicReleaseTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.root = Path(self.directory.name)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\nruntime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        (self.root / "version.toml").write_text("[framework]\nversion = \"0.4.1\"\n", encoding="utf-8")
        self.bindings = MockBindings(self.root)
        self.reopen = mock.patch("public_release._reopen_full_gate_binding", return_value=self.root)
        self.reopen_verify = self.reopen.start()
        self.addCleanup(self.reopen.stop)

    def tearDown(self) -> None:
        self.directory.cleanup()

    def definitions(self) -> list[dict[str, object]]:
        rows: list[dict[str, object]] = [
            {"requested_run_id": "workflow", "kind": "workflow", "definition": self.definition("CA-O-188", "workflow.md", "0")}
        ]
        for number in (189, 191, 193, 195, 197):
            rows.extend([
                {"requested_run_id": f"step-{number}", "kind": "step", "definition": self.definition(f"CA-O-{number}", f"{number}.md", "1"), "parent_requested_run_id": "workflow"},
                {"requested_run_id": f"action-{number + 1}", "kind": "action", "definition": self.definition(f"CA-O-{number + 1}", f"{number + 1}.md", "2"), "parent_requested_run_id": f"step-{number}"},
            ])
        return rows

    @staticmethod
    def definition(atom_id: str, path: str, char: str) -> dict[str, object]:
        return {"atom_id": atom_id, "version": 1, "path": f"operations/{path}", "digest": char * 64}

    def request(self) -> dict[str, object]:
        parameters = {
            "release": {"selected_version": "0.4.1", "release_branch": "amm/dev", "target_branch": "main", "remote": {"scope": "personal", "name": "githuba", "owner": "anatoly-m-maslennikov", "repository": "caprmedio-graph-driven-framework"}},
            "source": {"candidate_snapshot_manifest_sha256": "a" * 64, "readme_ref": "README.md", "pr_body_ref": "docs/public-pr.md", "version_history_ref": "VERSION_HISTORY.md", "version_history_summary": "Public release contract and workflow."},
            "recovery": {"prior_push": "not_started", "prior_pr": "not_started"},
        }
        frontier = ["README.md", "VERSION_HISTORY.md", "docs/public-pr.md"]
        effects = [{"type": "git_push", "target": "amm/dev"}, {"type": "pull_request_upsert", "target": "main"}]
        manifest = {"manifest_ref": "selected/public-release.manifest.json", "manifest_digest": "d" * 64}
        return {
            "request_id": "public-release-1", "operation_route": "public.release", "parameters": parameters,
            "parameters_digest": digest(parameters), "target_frontier": frontier, "target_frontier_digest": digest(frontier),
            "effects": effects, "effects_digest": digest(effects), "definition_manifest": manifest,
            "source_freshness": {"selected_source_registry_ref": "selected/registry.json", "selected_source_registry_version": 1, "selected_source_registry_digest": "e" * 64, "selected_binding_ref": "selected/public-release.json", "selected_binding_digest": "f" * 64},
            "initiative": {"initiative_id": "CA-P-1869", "instruction_summary": "Operator invokes the bounded public release", "initiative_ref": "03_plan/CA-P-1869.md"},
            "requested_runs": self.definitions(),
        }

    @staticmethod
    def observer(request):
        return {"selected": request["operation_route"] == "public.release", "current": True, "observed": {
            "selected_source_registry_ref": "selected/registry.json", "selected_source_registry_version": 1,
            "selected_source_registry_digest": "e" * 64, "selected_binding_ref": "selected/public-release.json",
            "selected_binding_digest": "f" * 64, "definition_manifest": request["definition_manifest"],
        }}

    def authorization(self, preview, request):
        return {"authorization_ref": "authorizations/public-release.json", "authorization_freshness": {"state": "current", "digest": "9" * 64}, "request_id": request["request_id"], "operation_route": request["operation_route"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "parameters_digest": request["parameters_digest"], "target_frontier_digest": request["target_frontier_digest"], "effects_digest": request["effects_digest"], "definition_manifest": request["definition_manifest"], "source_freshness": request["source_freshness"]}

    def execute(self, request=None):
        request = self.request() if request is None else request
        preview = run(self.root, request, bindings=self.bindings, source_observer=self.observer)
        return run(self.root, {**request, "mode": "execute", "proposal_receipt": preview["proposal_receipt"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "assigned_action_id": "CA-O-198", "operator_authorization": self.authorization(preview, request)}, bindings=self.bindings, source_observer=self.observer)

    def test_successful_new_pr_finalizes_actual_history_link_then_regates(self) -> None:
        result = self.execute()
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual("completed", result["terminal_runs"][0]["outcome"])
        self.assertEqual("CA-O-188", result["workflow"])
        self.assertEqual(11, len(result["run_ids"]))
        self.assertEqual(9, len(result["tool_calls"]))
        self.assertIn("gate-history_link_final", self.bindings.calls)
        self.assertIn("push-history_link_final", self.bindings.calls)
        self.assertIn("pr-history_link_final", self.bindings.calls)
        journal = next((self.root / ".caprmedio_caprmedio/_journal").glob("*.ndjson"))
        events = [json.loads(line) for line in journal.read_text(encoding="utf-8").splitlines()]
        self.assertTrue(all(event["schema_version"] == 5 for event in events))
        self.assertEqual({"workflow", "step", "action"}, {event["run"]["kind"] for event in events})
        self.assertFalse(any(event["run"]["kind"] == "tool" for event in events))

    def test_existing_pr_is_discovered_before_freeze_and_does_not_rewrite_history(self) -> None:
        self.bindings = MockBindings(self.root, existing=True)
        result = self.execute()
        self.assertEqual("terminal", result["disposition"])
        self.assertLess(self.bindings.calls.index("discover"), self.bindings.calls.index("gate-initial"))
        self.assertNotIn("gate-history_link_final", self.bindings.calls)
        self.assertNotIn("push-history_link_final", self.bindings.calls)

    def test_all_input_failures_stop_before_remote_binding(self) -> None:
        cases = []
        unsafe = self.request(); unsafe["parameters"] = {**unsafe["parameters"], "release": {**unsafe["parameters"]["release"], "target_branch": "release"}}; unsafe["parameters_digest"] = digest(unsafe["parameters"]); cases.append(unsafe)
        stale = self.request(); stale["parameters"] = {**stale["parameters"], "recovery": {"prior_push": "unknown", "prior_pr": "not_started"}}; stale["parameters_digest"] = digest(stale["parameters"]); cases.append(stale)
        malformed = self.request(); malformed["parameters"] = {"release": {}, "source": {}, "recovery": {}}; malformed["parameters_digest"] = digest(malformed["parameters"]); cases.append(malformed)
        missing_run = self.request(); missing_run["requested_runs"] = missing_run["requested_runs"][:-1]; cases.append(missing_run)
        for request in cases:
            with self.subTest(request=request["request_id"]), self.assertRaises(PublicReleaseError):
                run(self.root, request, bindings=self.bindings, source_observer=self.observer)
        self.assertEqual([], self.bindings.calls)

    def test_stale_typed_full_gate_and_duplicate_pr_stop_before_push(self) -> None:
        self.bindings.bad_gate = True
        result = self.execute()
        self.assertEqual("terminal", result["disposition"])
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("push-initial", self.bindings.calls)
        self.bindings = MockBindings(self.root); self.bindings.duplicate = True
        duplicate_request = self.request()
        duplicate_request["request_id"] = "public-release-duplicate"
        result = self.execute(duplicate_request)
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("prepare", self.bindings.calls)

    def test_interrupted_push_has_truthful_terminal_runs_and_no_pr_replay(self) -> None:
        self.bindings.interrupt_push = True
        result = self.execute()
        self.assertEqual("started", result["disposition"])
        self.assertIn("interrupted_pending", {row["outcome"] for row in result["terminal_runs"]})
        self.assertEqual("inspect-or-recover-only", result["retry_disposition"])
        self.assertNotIn("pr-initial", self.bindings.calls)

    def test_execute_requires_authorization_and_selected_source_currentness(self) -> None:
        request = self.request()
        preview = run(self.root, request, bindings=self.bindings, source_observer=self.observer)
        with self.assertRaises(PublicReleaseError):
            run(self.root, {**request, "mode": "execute", "proposal_receipt": preview["proposal_receipt"], "proposal_receipt_digest": preview["proposal_receipt_digest"], "assigned_action_id": "CA-O-198", "operator_authorization": {}}, bindings=self.bindings, source_observer=self.observer)
        blocked = run(self.root, request, bindings=self.bindings, source_observer=lambda _: {"selected": True, "current": False, "observed": {"reason": "source changed"}})
        self.assertEqual("blocked", blocked["disposition"])

    def test_foreign_or_number_mismatched_pr_is_rejected_before_prepare(self) -> None:
        self.bindings = MockBindings(self.root, existing=True)
        self.bindings.owner = "foreign-owner"
        result = self.execute()
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("prepare", self.bindings.calls)

        self.bindings = MockBindings(self.root, existing=True)
        self.bindings.pr = lambda: PullRequest(self.bindings.url_for(42), 43, "amm/dev", "main")
        request = self.request()
        request["request_id"] = "public-release-number-mismatch"
        result = self.execute(request)
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("prepare", self.bindings.calls)

    def test_source_gate_version_and_push_negative_goldens_stop_before_pr_replay(self) -> None:
        self.bindings.bad_source = True
        result = self.execute()
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("gate-initial", self.bindings.calls)

        self.bindings = MockBindings(self.root)
        self.bindings.bad_version = True
        request = self.request(); request["request_id"] = "public-release-version-changed"
        result = self.execute(request)
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("push-initial", self.bindings.calls)

        self.bindings = MockBindings(self.root)
        self.bindings.push_owner = "foreign-owner"
        request = self.request(); request["request_id"] = "public-release-push-receipt"
        result = self.execute(request)
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("pr-initial", self.bindings.calls)

    def test_reopen_failure_and_describe_are_explicitly_non_executable(self) -> None:
        self.reopen_verify.side_effect = RuntimeError("aggregate receipt changed")
        result = self.execute()
        self.assertIn("failed", {row["outcome"] for row in result["terminal_runs"]})
        self.assertNotIn("push-initial", self.bindings.calls)
        descriptor = describe()
        self.assertIn("prototype", descriptor["admission"])
        self.assertTrue(all(item.startswith("planned only:") for item in descriptor["effects"]))


if __name__ == "__main__":
    unittest.main()
