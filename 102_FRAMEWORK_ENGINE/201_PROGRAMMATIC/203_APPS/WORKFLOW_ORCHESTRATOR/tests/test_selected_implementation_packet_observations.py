"""Focused carry-forward checks for actual O016 Integrated observations."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
from typing import Mapping, cast
import unittest


APP = Path(__file__).resolve().parents[1]
for location in (APP, Path(__file__).resolve().parent):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_implementation_packet import implementation_packet  # noqa: E402
from selected_integrated_action_outcome import binding_digest  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402


def _parameters() -> dict[str, object]:
    packets = {step: {"context": "Integrated", "retained_state": {}} for step in ACTIONS}
    return {
        "base_packet": {
            "context": "Integrated",
            "candidate": {"id": "candidate-a"},
            "phase": "implementation",
            "requirements": [],
            "delivery": [],
            "evaluations": [],
            "method_projection": {"content": "", "sources": []},
            "retained_state": {},
            "retry": {"consumed": 0, "effective_limit": 1},
        },
        "step_packets": packets,
    }


def _result(
    step: str,
    action: str,
    result: str,
    outputs: dict[str, object],
    *,
    packet: Mapping[str, object],
) -> dict[str, object]:
    return {
        "step_definition_id": step,
        "action_definition_id": action,
        "result": result,
        "outputs": outputs,
        "evidence": [{"kind": "fixture"}],
        "retained_state": {"untrusted": True},
        "candidate": copy.deepcopy(packet["candidate"]),
        "binding_digest": binding_digest(packet),
    }


class SelectedImplementationPacketObservationTests(unittest.TestCase):
    def test_o231_plan_and_review_outputs_progress_without_unsealing_authority(self) -> None:
        parameters = _parameters()
        packet = cast(Mapping[str, object], parameters["base_packet"])
        plan = {
            "plan_id": "plan-a",
            "item_id": "item-a",
            "dod": ["verified"],
            "estimated_minutes": 1,
        }
        prior = [
            _result(
                "CA-O-231",
                "CA-O-017",
                "review_ready",
                {"plan_item": plan, "review_phase": "preliminary"},
                packet=packet,
            )
        ]

        packet = implementation_packet(parameters, "CA-O-230", prior)

        self.assertEqual(plan, packet["plan_item"])
        self.assertEqual("preliminary", packet["review_phase"])
        self.assertEqual({"id": "candidate-a"}, packet["candidate"])
        self.assertNotIn("untrusted", packet["retained_state"])

    def test_actual_review_and_final_check_evidence_are_bound_to_the_frozen_candidate(self) -> None:
        parameters = _parameters()
        packet = cast(Mapping[str, object], parameters["base_packet"])
        prior = [
            _result(
                "CA-O-231",
                "CA-O-017",
                "review_ready",
                {"review_phase": "preliminary"},
                packet=packet,
            ),
            _result(
                "CA-O-230", "CA-O-225", "preliminary_clear", {"review": "clear"}, packet=packet
            ),
            _result(
                "CA-O-231",
                "CA-O-017",
                "evaluation_runnable",
                {"review_phase": "final"},
                packet=packet,
            ),
            _result("CA-O-094", "CA-O-020", "passed", {"checks": ["ok"]}, packet=packet),
            _result("CA-O-230", "CA-O-225", "passed", {"review": "final"}, packet=packet),
        ]

        packet = implementation_packet(parameters, "CA-O-231", prior)

        state = packet["retained_state"]
        self.assertEqual("final", packet["review_phase"])
        self.assertEqual("preliminary_clear", state["preliminary_review"]["result"])
        self.assertEqual("passed", state["final_checks"]["result"])
        self.assertEqual("passed", state["final_review"]["result"])
        self.assertEqual({"id": "candidate-a"}, state["final_review"]["candidate"])


if __name__ == "__main__":
    unittest.main()
