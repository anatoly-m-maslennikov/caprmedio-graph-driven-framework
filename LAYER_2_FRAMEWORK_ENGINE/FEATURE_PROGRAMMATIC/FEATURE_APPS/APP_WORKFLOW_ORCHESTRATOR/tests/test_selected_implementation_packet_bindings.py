"""Regression checks for original bindings on observed O016 evidence."""

from __future__ import annotations

from collections.abc import Mapping
import copy
from pathlib import Path
import sys
from typing import Any, cast
import unittest


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_action_execution import retain_implementation_result  # noqa: E402
from selected_implementation_packet import implementation_packet  # noqa: E402
from selected_integrated_action_outcome import binding_digest  # noqa: E402


def _parameters() -> dict[str, Any]:
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
        },
        "step_packets": {
            "CA-O-231": {"context": "Integrated", "retained_state": {}},
            "CA-O-230": {"context": "Integrated", "retained_state": {}},
        },
    }


def _record(
    prior: list[dict[str, Any]],
    packet: Mapping[str, Any],
    step: str,
    action: str,
    result: str,
    outputs: Mapping[str, Any],
) -> None:
    retain_implementation_result(
        "CA-O-016",
        {"atom_id": step},
        {"atom_id": action},
        result,
        {
            "native_result": {
                "outputs": dict(outputs),
                "evidence": [{"kind": "fixture"}],
                "candidate": copy.deepcopy(packet["candidate"]),
                "binding_digest": binding_digest(packet),
            }
        },
        prior,
    )


class SelectedImplementationPacketBindingTests(unittest.TestCase):
    def test_drift_cannot_rebind_actual_prior_review_evidence(self) -> None:
        parameters = _parameters()
        original = cast(Mapping[str, Any], parameters["base_packet"])
        prior: list[dict[str, Any]] = []
        _record(
            prior,
            original,
            "CA-O-231",
            "CA-O-017",
            "review_ready",
            {"review_phase": "preliminary"},
        )
        _record(
            prior,
            original,
            "CA-O-230",
            "CA-O-225",
            "preliminary_clear",
            {"review": "clear"},
        )
        current = implementation_packet(parameters, "CA-O-230", prior)["retained_state"]
        self.assertEqual("preliminary_clear", current["preliminary_review"]["result"])
        for key, value in (
            ("candidate", {"id": "candidate-b"}),
            ("phase", "changed"),
            ("evaluations", [{"test": "changed"}]),
            ("method_projection", {"content": "changed", "sources": []}),
        ):
            changed = copy.deepcopy(parameters)
            cast(dict[str, Any], changed["base_packet"])[key] = value
            retained = implementation_packet(changed, "CA-O-230", prior)["retained_state"]
            self.assertNotIn("preliminary_review", retained)


if __name__ == "__main__":
    unittest.main()
