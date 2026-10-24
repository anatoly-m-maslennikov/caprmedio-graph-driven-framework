"""Subject Update assessment and selected-child forwarding contract tests.

The native publisher and source observation are seam doubles here; the separate
GoldenProject suite exercises their real authority and effect gates.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
from types import ModuleType
import unittest
from unittest.mock import Mock, patch


APP = Path(__file__).resolve().parents[1]
REPOSITORY = APP.parents[3]
TOOLS = APP.parents[1] / "201_TOOLS"
TEST_TEMP_ROOT = REPOSITORY / ".caprmedio_tmp" / "tests" / Path(__file__).stem
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import lifecycle_intents  # noqa: E402
from selected_execution import SelectedExecution, SelectedExecutionError  # noqa: E402


class _ChildSession:
    def __init__(self, order: list[str]) -> None:
        self.actual: dict[str, dict[str, str]] = {}
        self.order = order

    def start_run(self, requested_id: str) -> dict[str, str]:
        self.order.append("start")
        record = {"run_id": f"actual::{requested_id}"}
        self.actual[requested_id] = record
        return dict(record)

    def finish_run(self, run_id: str, **result: object) -> dict[str, object]:
        return {"run_id": run_id, "disposition": "terminal", **result}

    def note_effects(self, run_id: str, **result: object) -> None:
        self.observed_effects = {"run_id": run_id, **result}


class SubjectUpdateDispatchTests(unittest.TestCase):
    def setUp(self) -> None:
        TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.target = {
            "atom_id": "CA-R-100", "path": ".caprmedio_caprmedio/FIXTURE/04_requirement/CA-R-100--target.md",
            "filename": "CA-R-100--target.md", "version": 2, "digest": "a" * 64,
            "lifecycle": "active", "status": "Active", "updated_at": "2026-10-12 00:00:00 +0000",
            "content_role": "Requirement", "type": "General",
        }
        self.parameters = {
            "target": self.target,
            "subject_patches": [{"field": "governs", "before": "Old", "after": "New"}],
            "subject_intent_sha256": "b" * 64,
            "subject_profile": "legacy",
            "semantic_assessment_report": {"path": "report.md", "digest": "c" * 64},
        }
        self.evidence = {"admitted_change_class": "semantic_revision", "comparison": {"report": "verified"}}

    def test_assessment_binds_the_original_subject_request(self) -> None:
        seal = lifecycle_intents.update_assessment_seal(self.parameters, self.evidence)
        serialized = json.dumps(self.parameters, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        self.assertEqual(hashlib.sha256(serialized.encode("utf-8")).hexdigest(), seal["request_digest"])
        lifecycle_intents._validate_update_assessment(self.parameters, seal, self.evidence)
        for field in ("target", "subject_patches", "subject_intent_sha256", "subject_profile", "semantic_assessment_report"):
            with self.subTest(field=field):
                changed = copy.deepcopy(self.parameters)
                changed[field] = "different"
                with self.assertRaises(lifecycle_intents.LifecycleError) as caught:
                    lifecycle_intents._validate_update_assessment(changed, seal, self.evidence)
                self.assertEqual("reassessment-required", caught.exception.code)

    def test_subject_assessment_requires_the_intent_hash(self) -> None:
        incomplete = {key: value for key, value in self.parameters.items() if key != "subject_intent_sha256"}
        with self.assertRaises(lifecycle_intents.LifecycleError) as caught:
            lifecycle_intents.update_assessment_seal(incomplete)
        self.assertEqual("update-parameters-invalid", caught.exception.code)

    def _dispatch(self, *, retained_child: bool = False,
                  native_outcome: str = "failed", log_failure: bool = False,
                  metadata_unavailable: bool = False) -> tuple[dict[str, object], Mock, _ChildSession, dict[str, object], list[str]]:
        selected = SelectedExecution(self.root)
        order: list[str] = []
        session = _ChildSession(order)
        requested_child = "requested-child"
        if retained_child:
            session.actual[requested_child] = {"run_id": "existing-actual-child"}
        prior = {"state": "observed", "before_result": {"state": "present", "path": self.target["path"], "sha256": "a" * 64}}
        assessment = lifecycle_intents.update_assessment_seal(self.parameters, self.evidence)
        saved: list[dict[str, object]] = []

        def publish(_root: Path, parameters: dict[str, object], **call: object) -> dict[str, object]:
            self.assertEqual(self.parameters, parameters)
            if not call["execute"]:
                return {"operation": "update", "outcome": "preview", "observed": self.target}
            order.append("effect")
            return {"operation": "update", "outcome": native_outcome, "observed": self.target, "effects": []}

        def save(payload: dict[str, object]) -> str:
            saved.append(payload)
            return "native-result.json"

        native = ModuleType("atom_subject_apply")
        publisher = Mock(side_effect=publish)
        native.subject_update_action = publisher
        context = {
            "route": "update_atom", "parameters": self.parameters, "session": session,
            "lifecycle_requested_run_id": requested_child,
            "lifecycle_action_binding": {"atom_id": "CA-O-030"},
            "lifecycle_result_writer": save, "action_binding": {"atom_id": "CA-O-128"},
            "action_run_id": "actual-outer-action", "execution_request_id": "request",
            "lifecycle_prior_results": [{
                "step_definition_id": "CA-O-145", "action_definition_id": "CA-O-067",
                "result": "identity-preserving", "native_result": {"assessment": assessment},
                "completed_receipt": {"disposition": "terminal", "outcome": "completed"},
            }],
        }
        with (
            patch.dict(sys.modules, {"atom_subject_apply": native}),
            patch(
                "selected_lifecycle_handler.bound_action_structural_scope",
                return_value="FIXTURE",
            ),
            patch(
                "selected_lifecycle_observation.bound_action_structural_scope",
                return_value="FIXTURE",
            ),
            patch(
                "selected_lifecycle_handler.result_facts",
                return_value=({"path": self.target["path"], "sha256": "a" * 64}, b"before"),
            ),
            patch(
                "selected_lifecycle_result.result_facts",
                return_value=({"path": self.target["path"], "sha256": "a" * 64}, b"before"),
            ),
            patch(
                "selected_lifecycle_result.journal_context",
                return_value=("operator", "2026-10-12", "UTC", "2026-10-12T00:00:00+00:00"),
                side_effect=(
                    SelectedExecutionError("Journal metadata unavailable")
                    if metadata_unavailable
                    else None
                ),
            ),
            patch("selected_lifecycle_journal.prepare_lifecycle_journal", side_effect=AssertionError("Journal admission called")),
            patch("selected_lifecycle_journal.admit_lifecycle_prior", side_effect=AssertionError("Journal admission called")),
            patch("selected_lifecycle_journal.record_lifecycle_change", side_effect=OSError("full") if log_failure else None),
        ):
            result = selected.handlers["CA-O-128"](context)
        return result, publisher, session, prior, order

    def test_subject_handler_forwards_actual_child_and_verified_source_observation(self) -> None:
        result, publisher, session, prior, order = self._dispatch()
        self.assertEqual("failed", result["result"])
        self.assertEqual(["start", "effect"], order)
        self.assertEqual(2, publisher.call_count)
        preview_call, effect_call = publisher.call_args_list
        self.assertIsNone(preview_call.kwargs["session"])
        self.assertIs(effect_call.kwargs["session"], session)
        self.assertEqual("actual::requested-child", effect_call.kwargs["action_run_id"])
        self.assertEqual(effect_call.kwargs["prior"], prior)
        self.assertEqual(lifecycle_intents.update_assessment_seal(self.parameters, self.evidence), effect_call.kwargs["assessment"])

    def test_no_journal_admission_is_needed_for_actual_child(self) -> None:
        result, publisher, session, _prior, order = self._dispatch()
        self.assertEqual("failed", result["result"])
        self.assertEqual(["start", "effect"], order)
        self.assertEqual(1, len(session.actual))
        self.assertEqual(2, publisher.call_count)

    def test_logging_failure_keeps_the_actual_source_outcome(self) -> None:
        result, publisher, _session, _prior, order = self._dispatch(native_outcome="applied", log_failure=True)
        self.assertEqual("applied", result["result"])
        self.assertEqual("completed", result["terminal_outcome"])
        self.assertEqual("OSError", result["recording_error"])
        self.assertEqual(["start", "effect"], order)
        self.assertEqual(2, publisher.call_count)

    def test_unavailable_recording_metadata_keeps_the_actual_source_outcome(self) -> None:
        result, publisher, _session, _prior, order = self._dispatch(
            native_outcome="applied", metadata_unavailable=True
        )
        self.assertEqual("applied", result["result"])
        self.assertEqual("completed", result["terminal_outcome"])
        self.assertEqual("SelectedExecutionError", result["recording_error"])
        self.assertEqual(["start", "effect"], order)
        self.assertEqual(1, sum(bool(call.kwargs["execute"]) for call in publisher.call_args_list))

    def test_retained_child_never_reinvokes_native_subject_update(self) -> None:
        result, publisher, _session, _prior, order = self._dispatch(retained_child=True)
        self.assertEqual("lifecycle-recovery-required", result["result"])
        self.assertEqual([], order)
        publisher.assert_not_called()


if __name__ == "__main__":
    unittest.main()
