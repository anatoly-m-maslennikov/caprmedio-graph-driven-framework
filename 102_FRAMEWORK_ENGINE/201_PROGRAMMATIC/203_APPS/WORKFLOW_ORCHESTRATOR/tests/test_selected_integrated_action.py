"""Frozen functional contracts for the current Integrated Action handoff loop."""

from __future__ import annotations

import copy
from collections.abc import Callable, Mapping
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402
from selected_integrated_action import (  # noqa: E402
    IntegratedActionPending,
    invoke_integrated_action,
    submit_integrated_action,
)
from selected_integrated_action_contract import prompt_spec  # noqa: E402
from selected_integrated_action_outcome import binding_digest  # noqa: E402
from selected_integrated_action_test_support import materialize_bound_inputs  # noqa: E402


CURRENT_STEP = "CA-O-231"
CURRENT_ACTION = "CA-O-017"
CURRENT_RESULTS = (
    "evaluation_ready",
    "requirement_ready",
    "evaluation_runnable",
    "review_ready",
    "complete",
    "blocked",
)
CURRENT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "result": {"type": "string", "enum": list(CURRENT_RESULTS)},
        "outputs": {"type": "object"},
        "evidence": {"type": "array"},
        "blockers": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["blockers", "evidence", "outputs", "result"],
}


def current_packet(fixture: CurrentSharedContextFixture) -> dict[str, object]:
    parameters = fixture.native_implementation_parameters()
    base = copy.deepcopy(parameters["base_packet"])
    step = copy.deepcopy(parameters["step_packets"][CURRENT_STEP])
    return {**base, **step}


class _ActionProvider:
    def __init__(self, *, context: str = "Integrated") -> None:
        self.context = context
        self.calls = 0
        self.cli_calls = 0
        self.prompt = prompt_spec(CURRENT_STEP, CURRENT_ACTION)["prompt"]

    def __call__(
        self,
        packet: Mapping[str, object],
        *,
        agent: Callable[[str, Mapping[str, object]], Mapping[str, object]],
        selected_project_root: Path,
        trusted_execution_authorization: Mapping[str, object] | None = None,
    ) -> dict[str, object]:
        del selected_project_root, trusted_execution_authorization
        self.calls += 1
        response = agent(self.prompt, packet)
        return {
            **response,
            "step": CURRENT_STEP,
            "action": CURRENT_ACTION,
            "context": self.context,
            "source_bindings": packet.get("source_bindings", []),
            "retained_state": packet.get("retained_state", {}),
        }


class SelectedIntegratedActionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()
        self.packet = current_packet(self.fixture)
        temporary = tempfile.TemporaryDirectory(
            dir=APP.parents[3] / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(temporary.cleanup)
        self.root, self.profile, self.trusted_methods = materialize_bound_inputs(
            self.fixture, Path(temporary.name)
        )

    def _invoke(self, action: _ActionProvider) -> IntegratedActionPending:
        with self.assertRaises(IntegratedActionPending) as raised:
            invoke_integrated_action(
                action,
                self.packet,
                step_id=CURRENT_STEP,
                action_id=CURRENT_ACTION,
                context="Integrated",
                selected_project_root=self.root,
                allowed_results=CURRENT_RESULTS,
                output_schema=CURRENT_SCHEMA,
                workflow_definition=self.profile["workflow"],
                step_definition=self.profile["steps"][CURRENT_STEP]["step"],
                action_definition=self.profile["steps"][CURRENT_STEP]["action"],
                trusted_workflow_binding=self.profile,
                trusted_method_projection=self.trusted_methods,
            )
        return raised.exception

    def test_current_o231_captures_exact_prompt_and_packet_without_cli_or_completion(self) -> None:
        action = _ActionProvider()
        pending = self._invoke(action)
        capture = pending.capture

        self.assertEqual("Integrated", capture["context"])
        self.assertEqual(CURRENT_STEP, capture["step_id"])
        self.assertEqual(CURRENT_ACTION, capture["action_id"])
        self.assertEqual(action.prompt, capture["prompt"])
        self.assertEqual(self.packet, capture["packet"])
        self.assertEqual(list(CURRENT_RESULTS), capture["allowed_results"])
        self.assertEqual(CURRENT_SCHEMA, capture["output_schema"])
        self.assertEqual(self.packet["source_bindings"], capture["packet"]["source_bindings"])
        self.assertEqual(1, action.calls)
        self.assertEqual(0, action.cli_calls)
        self.assertNotIn("completed", capture)

    def test_valid_submission_reuses_action_callback_and_preserves_result_contract(self) -> None:
        action = _ActionProvider()
        pending = self._invoke(action)
        submitted = {
            "result": "evaluation_ready",
            "outputs": {"plan_item": "fixture-plan", "tool_output": {"ok": True}},
            "evidence": [{"kind": "baseline", "status": "observed"}],
            "blockers": [],
        }

        result = submit_integrated_action(
            action,
            pending.capture,
            submitted,
            selected_project_root=self.root,
        )

        self.assertEqual("evaluation_ready", result["result"])
        self.assertEqual(submitted["outputs"], result["outputs"])
        self.assertEqual(submitted["evidence"], result["evidence"])
        self.assertEqual([], result["blockers"])
        self.assertEqual(self.packet["source_bindings"], result["source_bindings"])
        self.assertEqual(self.packet["candidate"], result["candidate"])
        self.assertEqual(binding_digest(self.packet), result["binding_digest"])
        self.assertEqual(2, action.calls)
        self.assertEqual(0, action.cli_calls)

    def test_invalid_submitted_result_remains_pending(self) -> None:
        action = _ActionProvider()
        pending = self._invoke(action)
        invalid = {
            "result": "not-a-current-result",
            "outputs": {},
            "evidence": [],
            "blockers": [],
        }

        with self.assertRaises(IntegratedActionPending) as raised:
            submit_integrated_action(action, pending.capture, invalid)

        self.assertEqual("invalid_submitted_response", raised.exception.capture["reason"])
        self.assertEqual(pending.capture["prompt"], raised.exception.capture["prompt"])
        self.assertEqual(1, action.calls)

    def test_explicit_isolated_context_is_not_intercepted(self) -> None:
        action = _ActionProvider(context="Isolated")
        with self.assertRaises(ValueError):
            invoke_integrated_action(
                action,
                self.packet,
                step_id="CA-O-232",
                action_id="CA-O-018",
                context="Isolated",
                selected_project_root=self.root,
                allowed_results=("prepared", "blocked"),
                output_schema=CURRENT_SCHEMA,
                workflow_definition=self.profile["workflow"],
                step_definition=self.profile["steps"]["CA-O-232"]["step"],
                action_definition=self.profile["steps"]["CA-O-232"]["action"],
                trusted_workflow_binding=self.profile,
                trusted_method_projection=self.trusted_methods,
            )
        self.assertEqual(0, action.calls)
        self.assertEqual(0, action.cli_calls)
