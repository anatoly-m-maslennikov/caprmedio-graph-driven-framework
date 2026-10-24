"""Frozen functional journeys for the current Integrated Action frontier."""

from __future__ import annotations

import copy
from collections.abc import Mapping
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_integrated_action import (  # noqa: E402
    IntegratedActionPending,
    current_integrated_action_provider,
    invoke_integrated_action,
    submit_integrated_action,
)
from selected_integrated_action_contract import prompt_spec  # noqa: E402
from selected_integrated_action_outcome import binding_digest  # noqa: E402
from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402
from selected_integrated_action_test_support import materialize_bound_inputs  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402


CURRENT_STEP = "CA-O-231"
CURRENT_ACTION = "CA-O-017"


def current_packet(fixture: CurrentSharedContextFixture) -> dict[str, object]:
    parameters = fixture.native_implementation_parameters()
    return {
        **copy.deepcopy(parameters["base_packet"]),
        **copy.deepcopy(parameters["step_packets"][CURRENT_STEP]),
    }


class SelectedIntegratedActionFrontierTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()

    def test_current_frozen_frontier_uses_each_source_prompt_without_cli(self) -> None:
        parameters = self.fixture.native_implementation_parameters()
        calls: list[tuple[str, Mapping[str, object]]] = []
        for step_id, action_id in ACTIONS.items():
            packet = {
                **copy.deepcopy(parameters["base_packet"]),
                **copy.deepcopy(parameters["step_packets"][step_id]),
            }
            if step_id == "CA-O-230":
                packet["review_phase"] = "preliminary"
            if step_id == "CA-O-094":
                packet["retained_state"]["preliminary_review"] = {
                    "candidate": packet["candidate"],
                    "result": "preliminary_clear",
                    "binding_digest": binding_digest(packet),
                }
            spec = prompt_spec(step_id, action_id)
            result = next(label for label in spec["allowed_results"] if label != "blocked")
            response: dict[str, object] = {
                "result": result,
                "outputs": {"fixture": step_id},
                "evidence": [{"kind": "frozen-fixture", "step": step_id}],
                "blockers": [],
            }

            def agent(prompt: str, callback_packet: Mapping[str, object]) -> Mapping[str, object]:
                calls.append((prompt, callback_packet))
                return response

            returned = current_integrated_action_provider(
                packet,
                agent=agent,
                selected_project_root=Path("fixture-project"),
            )
            self.assertEqual(spec["prompt"], calls[-1][0])
            self.assertEqual(packet, calls[-1][1])
            self.assertEqual(step_id, returned["step"])
            self.assertEqual(action_id, returned["action"])
            self.assertEqual(packet["source_bindings"], returned["source_bindings"])
            self.assertEqual(packet["retained_state"], returned["retained_state"])

        self.assertEqual(len(ACTIONS), len(calls))

    def test_bound_o231_capture_and_submission_uses_frozen_sources(self) -> None:
        temporary = tempfile.TemporaryDirectory(
            dir=APP.parents[3] / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(temporary.cleanup)
        root, profile, trusted_methods = materialize_bound_inputs(
            self.fixture, Path(temporary.name)
        )
        packet = current_packet(self.fixture)
        packet.pop("plan_item")
        row = profile["steps"][CURRENT_STEP]
        with self.assertRaises(IntegratedActionPending) as raised:
            invoke_integrated_action(
                current_integrated_action_provider,
                packet,
                step_id=CURRENT_STEP,
                action_id=CURRENT_ACTION,
                context="Integrated",
                selected_project_root=root,
                workflow_definition=profile["workflow"],
                step_definition=row["step"],
                action_definition=row["action"],
                trusted_workflow_binding=profile,
                trusted_method_projection=trusted_methods,
            )
        capture = raised.exception.capture
        self.assertEqual(prompt_spec(CURRENT_STEP, CURRENT_ACTION)["prompt"], capture["prompt"])
        self.assertEqual(trusted_methods, capture["definitions"]["trusted_method_projection"])
        submitted = {
            "result": "evaluation_ready",
            "outputs": {"plan_item": "fixture-plan"},
            "evidence": [{"kind": "frozen-fixture", "status": "observed"}],
            "blockers": [],
        }
        result = submit_integrated_action(
            current_integrated_action_provider,
            capture,
            submitted,
        )
        self.assertEqual(submitted["outputs"], result["outputs"])
        self.assertEqual(submitted["evidence"], result["evidence"])
        self.assertEqual(packet["source_bindings"], result["source_bindings"])
        self.assertEqual(packet["retained_state"], result["retained_state"])


if __name__ == "__main__":
    unittest.main()
