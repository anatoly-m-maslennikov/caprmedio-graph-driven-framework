"""Regression checks for source and contract binding at Integrated handoff."""

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

from selected_integrated_action import (  # noqa: E402
    IntegratedActionInputError,
    IntegratedActionPending,
    invoke_integrated_action,
    submit_integrated_action,
)
from selected_integrated_action_contract import prompt_spec  # noqa: E402
from selected_integrated_action_outcome import (  # noqa: E402
    binding_digest,
    validate_outcome,
)
from selected_integrated_action_test_support import materialize_bound_inputs  # noqa: E402
from selected_implementation_packet import implementation_packet  # noqa: E402
from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402


CURRENT_STEP = "CA-O-231"
CURRENT_ACTION = "CA-O-017"


def current_packet(fixture: CurrentSharedContextFixture) -> dict[str, object]:
    parameters = fixture.native_implementation_parameters()
    return {
        **copy.deepcopy(parameters["base_packet"]),
        **copy.deepcopy(parameters["step_packets"][CURRENT_STEP]),
    }


class _Provider:
    def __init__(self) -> None:
        self.calls = 0
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
        return {
            **agent(self.prompt, packet),
            "step": CURRENT_STEP,
            "action": CURRENT_ACTION,
            "context": "Integrated",
            "source_bindings": packet.get("source_bindings", []),
            "retained_state": packet.get("retained_state", {}),
        }


class SelectedIntegratedActionSecurityTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()
        temporary = tempfile.TemporaryDirectory(
            dir=APP.parents[3] / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(temporary.cleanup)
        self.root, self.profile, self.trusted_methods = materialize_bound_inputs(
            self.fixture, Path(temporary.name)
        )

    def _capture(self, provider: _Provider) -> IntegratedActionPending:
        with self.assertRaises(IntegratedActionPending) as raised:
            packet = current_packet(self.fixture)
            invoke_integrated_action(
                provider,
                packet,
                step_id=CURRENT_STEP,
                action_id=CURRENT_ACTION,
                context="Integrated",
                selected_project_root=self.root,
                workflow_definition=self.profile["workflow"],
                step_definition=self.profile["steps"][CURRENT_STEP]["step"],
                action_definition=self.profile["steps"][CURRENT_STEP]["action"],
                trusted_workflow_binding=self.profile,
                trusted_method_projection=self.trusted_methods,
            )
        return raised.exception

    def _response(self) -> dict[str, object]:
        return {
            "result": "evaluation_ready",
            "outputs": {"fixture": True},
            "evidence": ["fixture-evidence"],
            "blockers": [],
        }

    def test_submission_requires_complete_source_definitions(self) -> None:
        provider = _Provider()
        pending = self._capture(provider)
        pending.capture["definitions"] = {}

        with self.assertRaises(IntegratedActionInputError):
            submit_integrated_action(provider, pending.capture, self._response())
        self.assertEqual(1, provider.calls)

    def test_submission_rejects_definitions_for_a_different_step_and_action(self) -> None:
        packet = current_packet(self.fixture)
        provider = _Provider()
        row = self.profile["steps"]["CA-O-232"]
        with self.assertRaises(IntegratedActionInputError):
            invoke_integrated_action(
                provider,
                packet,
                step_id=CURRENT_STEP,
                action_id=CURRENT_ACTION,
                context="Integrated",
                selected_project_root=self.root,
                workflow_definition=self.profile["workflow"],
                step_definition=row["step"],
                action_definition=row["action"],
                trusted_workflow_binding=self.profile,
                trusted_method_projection=self.trusted_methods,
            )
        self.assertEqual(0, provider.calls)

    def test_submission_recomputes_the_current_result_contract(self) -> None:
        for field in ("allowed_results", "output_schema"):
            provider = _Provider()
            pending = self._capture(provider)
            if field == "allowed_results":
                pending.capture[field] = [*pending.capture[field], "invented"]
            else:
                pending.capture[field]["properties"]["result"]["enum"].append("invented")

            with self.assertRaises(ValueError):
                submit_integrated_action(provider, pending.capture, self._response())
            self.assertEqual(1, provider.calls)

    def test_review_evidence_may_be_a_reference_but_requires_fresh_bindings(self) -> None:
        parameters = self.fixture.native_implementation_parameters()
        packet = implementation_packet(parameters, "CA-O-094", [])
        record = {
            "candidate": packet["candidate"],
            "result": "preliminary_clear",
        }
        packet["retained_state"]["preliminary_review"] = record
        passed = {
            "result": "passed",
            "outputs": {"checks": True},
            "evidence": ["test://fixture/current"],
            "blockers": [],
        }
        with self.assertRaises(ValueError):
            validate_outcome(packet, passed)

        record["binding_digest"] = binding_digest(packet)
        validate_outcome(packet, passed)

        packet["phase"] = "final"
        with self.assertRaises(ValueError):
            validate_outcome(packet, passed)


if __name__ == "__main__":
    unittest.main()
