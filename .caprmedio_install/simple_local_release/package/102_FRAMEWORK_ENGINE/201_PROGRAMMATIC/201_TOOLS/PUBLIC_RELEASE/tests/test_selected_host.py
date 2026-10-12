"""Temporary real selected Session tests; no Git, fresh gate or live installation."""
from __future__ import annotations

from dataclasses import replace
import json
import hashlib
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

PUBLIC = Path(__file__).resolve().parents[1]
PROGRAMMATIC = PUBLIC.parents[1]
for path in (PUBLIC, PUBLIC.parent, PUBLIC / "tests", PROGRAMMATIC / "204_MCP",
             PROGRAMMATIC / "204_MCP/tests", PROGRAMMATIC / "203_APPS/WORKFLOW_ORCHESTRATOR",
             PROGRAMMATIC / "203_APPS/WORKFLOW_ORCHESTRATOR/tests"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

import selected_admission
import test_release_manifest_admission as manifest_fixture
import test_public_release as documentation_fixture
from selected_execution import SelectedExecution
from selected_routes import load_selected_manifest, selected_manifest_ref
from selected_host import SelectedPublicHostError, create_selected_public_bindings, _history_payload, _SelectedPublicHost
from native_bindings import NativeCommandEvidence
from public_release import FreshPublicNativeFullGateBinding, GateResult, PublicReleaseError, ToolCallEvidence, _gate, _parameters
from workflow_run_support import RunTracker


class SelectedPublicHostTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = manifest_fixture.ReleaseManifestAdmissionTest()
        cls.fixture.setUpClass()
        cls.fixture.setUp()
        # These are this test class's borrowed helper instances, not a global
        # tempfile override. Retain only their disposable directories; keep
        # all registered source-pin patch cleanup intact.
        retained_cleanups = []
        for entry in cls.fixture._cleanups:
            cleanup, _arguments, _keywords = entry
            temporary = getattr(cleanup, "__self__", None)
            if isinstance(temporary, tempfile.TemporaryDirectory):
                temporary._finalizer.detach()
            else:
                retained_cleanups.append(entry)
        cls.fixture._cleanups = retained_cleanups
        cls.addClassCleanup(cls.fixture.doCleanups)
        cls.fixture._copy_public_release_sources()
        admission = selected_admission.derive_public_release_source_admission(cls.fixture.root)
        cls.fixture.save(cls.fixture.public_successor(admission))
        cls.root = cls.fixture.root
        (cls.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\n'
            'journal_root = ".caprmedio_caprmedio/_journal"\nruntime_root = ".caprmedio_runtime"\n', encoding="utf-8")

    def setUp(self):
        self.documents = documentation_fixture.MockBindings(self.root)
        (self.root / "version.toml").write_text('[framework]\nversion = "0.4.1"\n', encoding="utf-8")
        self.documents.source(self.documents.initial_sha)

    def with_host(self, action_id, callback):
        helper = documentation_fixture.PublicReleaseTests("runTest")
        request = helper.request()
        workflow_id = "host-" + hashlib.sha256(self._testMethodName.encode()).hexdigest()[:16]
        request["request_id"] = workflow_id
        manifest = load_selected_manifest(self.root)
        request["definition_manifest"] = {"manifest_ref": selected_manifest_ref(self.root),
                                          "manifest_digest": manifest["canonical_manifest_sha256"]}
        request["source_freshness"] = manifest["source_freshness"]
        store = SelectedExecution(self.root)
        graph = store._validate_graph({**request, "mode": "execute"})
        request["requested_runs"] = store.build_requested_runs(graph, workflow_id)

        def observer(_request):
            current = load_selected_manifest(self.root)
            return {"selected": True, "current": current == manifest,
                    "observed": {"manifest_digest": current["canonical_manifest_sha256"]}}

        result = {}
        frozen = None

        def execute(_request, session):
            workflow = request["requested_runs"][0]
            action = next(row for row in request["requested_runs"] if row["definition"]["atom_id"] == action_id)
            session.start_run(workflow["requested_run_id"])
            session.start_run(action["parent_requested_run_id"])
            session.start_run(action["requested_run_id"])
            bindings = create_selected_public_bindings(self.root, frozen, session)
            result["value"] = callback(bindings, session)

        tracker = RunTracker(self.root, source_observer=observer, executor=execute)
        preview = tracker.run_selected_operation({**request, "mode": "preview"})
        execution = {**request, "mode": "execute", "proposal_receipt": preview["proposal_receipt"],
                     "proposal_receipt_digest": preview["proposal_receipt_digest"], "assigned_action_id": action_id,
                     "operator_authorization": helper.authorization(preview, request)}
        frozen = store.freeze({"operation": "enqueue_selected", "run_id": workflow_id, "execution": execution})
        receipt = tracker.run_selected_operation(execution)
        self.assertNotIn("execution_error", receipt)
        return result["value"]

    def test_actual_admitted_session_records_parented_immutable_native_observation(self):
        def check(bindings, session):
            evidence = NativeCommandEvidence("discover_matching_pr", (), {"matches": []}, False)
            call = bindings._evidence_recorder(evidence)
            self.assertEqual(call, bindings._evidence_recorder(evidence))
            document = json.loads((self.root / call.result_ref).read_bytes())
            action = next(run for run in session.actual.values() if run["kind"] == "action")
            self.assertEqual(action["run_id"], document["action_run_id"])
            self.assertEqual(action["parent_run_id"], document["parent_step_run_id"])
            self.assertEqual(0o600, (self.root / call.result_ref).stat().st_mode & 0o777)
            self.assertNotIn("tool", [run["kind"] for run in session.actual.values()])
            return call
        self.with_host("CA-O-190", check)

    def test_changed_physical_action_source_refuses_before_evidence_write(self):
        def check(bindings, session):
            action = next(run for run in session.actual.values() if run["kind"] == "action")
            source = self.root / action["definition"]["path"]
            original = source.read_bytes()
            source.write_bytes(original + b"\nchanged\n")
            try:
                with self.assertRaises((RuntimeError, ValueError)):
                    bindings._evidence_recorder(NativeCommandEvidence("discover_matching_pr", (), {"matches": []}, False))
            finally:
                source.write_bytes(original)
        self.with_host("CA-O-190", check)

    def test_arbitrary_command_or_secret_observation_refuses(self):
        def check(bindings, _session):
            for evidence in (
                NativeCommandEvidence("discover_matching_pr", (("sh", "-c", "other"),), {}, False),
                NativeCommandEvidence("discover_matching_pr", (), {"token": "not-for-storage"}, False),
            ):
                with self.assertRaises(SelectedPublicHostError):
                    bindings._evidence_recorder(evidence)
        self.with_host("CA-O-190", check)

    def test_candidate_observer_refuses_missing_actual_native_generation(self):
        def check(bindings, _session):
            with self.assertRaises(SelectedPublicHostError):
                bindings._candidate_observer(_parameters(bindings._effect_admitter.__self__.session.request["parameters"]),
                                             "prepare_public_materials")
        self.with_host("CA-O-192", check)

    def test_wrong_active_action_cannot_admit_git_effect(self):
        def check(bindings, session):
            with self.assertRaises(SelectedPublicHostError):
                bindings._effect_admitter("commit_and_push:initial", session.request["parameters"], None)
        self.with_host("CA-O-190", check)

    def test_substituted_source_ref_refuses_before_native_candidate_lookup(self):
        def check(bindings, session):
            source = self.documents.source(self.documents.initial_sha)
            with patch.object(bindings._effect_admitter.__self__, "native_n", side_effect=AssertionError("must refuse first")):
                with self.assertRaises(SelectedPublicHostError):
                    bindings._effect_admitter("commit_and_push:initial", session.request["parameters"],
                                             replace(source, readme_ref="other-readme.md"))
        self.with_host("CA-O-196", check)

    def test_exact_history_payload_preserves_unrelated_bytes_and_line_endings(self):
        original = b"# History\r\n- Public summary.\r\n- Older release.\n"
        line = "- Public summary. [PR #7](https://github.com/example/project/pull/7)"
        self.assertEqual(b"# History\r\n" + line.encode() + b"\r\n- Older release.\n",
                         _history_payload(original, "Public summary.", line))

    def test_history_payload_refuses_duplicate_or_substituted_summary(self):
        for original in (b"- Summary.\n- Summary.\n", b"- Different summary.\n"):
            with self.assertRaises(SelectedPublicHostError):
                _history_payload(original, "Summary.", "- Summary. [PR #7](https://github.com/example/project/pull/7)")


class SelectedPublicGateTransportTests(unittest.TestCase):
    def test_failed_or_interrupted_producer_without_bridge_returns_typed_gate_result(self):
        # Transport-only negative test: admission and the physical producer are
        # mocked, never replaced with a fabricated passing gate assertion.
        from release_public_producer import PublicNativeFullGateResult

        host = object.__new__(_SelectedPublicHost)
        host.root = Path("/unopened-transport-only-project")
        host.session = object()
        inputs, packet, source = object(), object(), object()
        call = ToolCallEvidence("state/observation.json", "state/observation.json", (),
                                ("state/observation.json",))
        for outcome in ("failed", "interrupted_pending"):
            with self.subTest(outcome=outcome):
                producer = PublicNativeFullGateResult(inputs, None, None, None, outcome,
                    "state/producer-result.json", "a" * 64, None, None)
                with patch.object(host, "admit") as admit, \
                        patch.object(host, "native_n", return_value=SimpleNamespace(full_gate_packet=packet)), \
                        patch.object(host, "record", return_value=call) as record, \
                        patch("release_public_gate.reopen_public_fresh_gate_inputs", return_value=inputs) as reopen, \
                        patch("release_public_producer.run_public_native_full_gate", return_value=producer):
                    result = host.gate({}, source, "initial")
                admit.assert_called_once_with("run_full_gate:initial", {}, source)
                reopen.assert_called_once_with(host.root, host.session, packet, source)
                self.assertIsInstance(result, GateResult)
                self.assertIsInstance(result.binding, FreshPublicNativeFullGateBinding)
                self.assertIs(result.binding.result, producer)
                self.assertFalse(producer.passed)
                self.assertEqual(("state/observation.json", "state/producer-result.json"), result.call.report_refs)
                self.assertEqual((), result.call.effect_refs)
                self.assertIsNone(record.call_args.args[0].observations["bridge_ref"])
                with self.assertRaises(PublicReleaseError) as refused:
                    _gate(result, "initial full gate", source, project_root=host.root, selected_version="0.4.1")
                self.assertEqual("full-gate-unproven", refused.exception.code)


if __name__ == "__main__":
    unittest.main()
