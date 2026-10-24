"""Trust-boundary checks for the current Integrated Action bridge."""

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
    IntegratedActionInputError,
    current_integrated_action_provider,
    invoke_integrated_action,
)
from selected_integrated_action_outcome import (  # noqa: E402
    binding_digest,
    validate_outcome,
)
from selected_implementation_packet import implementation_packet  # noqa: E402
from selected_integrated_action_test_support import materialize_bound_inputs  # noqa: E402
from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402


CURRENT_STEP = "CA-O-231"
CURRENT_ACTION = "CA-O-017"


def current_packet(fixture: CurrentSharedContextFixture) -> dict[str, object]:
    parameters = fixture.native_implementation_parameters()
    return {
        **copy.deepcopy(parameters["base_packet"]),
        **copy.deepcopy(parameters["step_packets"][CURRENT_STEP]),
    }


class SelectedIntegratedActionBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()

    def test_source_bound_bridge_refuses_missing_authority_before_callback(self) -> None:
        packet = current_packet(self.fixture)
        called = False

        def provider(*args: object, **kwargs: object) -> Mapping[str, object]:
            nonlocal called
            called = True
            return {}

        with self.assertRaises(IntegratedActionInputError):
            invoke_integrated_action(
                provider,
                packet,
                step_id=CURRENT_STEP,
                action_id=CURRENT_ACTION,
                context="Integrated",
                selected_project_root=Path("fixture-project"),
            )
        self.assertFalse(called)

    def test_source_bound_bridge_refuses_packet_marker_drift(self) -> None:
        temporary = tempfile.TemporaryDirectory(
            dir=APP.parents[3] / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(temporary.cleanup)
        root, profile, trusted_methods = materialize_bound_inputs(
            self.fixture, Path(temporary.name)
        )
        packet = current_packet(self.fixture)
        packet["step_marker"] = "CA-O-232"
        row = profile["steps"][CURRENT_STEP]
        with self.assertRaises(ValueError):
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

    def test_review_postconditions_reject_phase_and_candidate_drift(self) -> None:
        parameters = self.fixture.native_implementation_parameters()
        review_packet = {
            **copy.deepcopy(parameters["base_packet"]),
            **copy.deepcopy(parameters["step_packets"]["CA-O-230"]),
            "review_phase": "final",
        }
        review = {
            "result": "preliminary_clear",
            "outputs": {"review": True},
            "evidence": [{"candidate": review_packet["candidate"]}],
            "blockers": [],
        }
        with self.assertRaises(ValueError):
            validate_outcome(review_packet, review)

        check_packet = {
            **copy.deepcopy(parameters["base_packet"]),
            **copy.deepcopy(parameters["step_packets"]["CA-O-094"]),
        }
        check_packet["retained_state"]["preliminary_review"] = {
            "candidate": "stale-candidate",
            "result": "preliminary_clear",
            "binding_digest": binding_digest(check_packet),
        }
        passed = {
            "result": "passed",
            "outputs": {"checks": True},
            "evidence": [{"candidate": check_packet["candidate"]}],
            "blockers": [],
        }
        with self.assertRaises(ValueError):
            validate_outcome(check_packet, passed)

    def test_retry_budget_counts_real_packet_rounds(self) -> None:
        parameters = self.fixture.native_implementation_parameters()
        permitted = {
            "step_definition_id": "CA-O-096",
            "action_definition_id": "CA-O-024",
            "result": "retry_permitted",
            "outputs": {},
            "evidence": [],
            "blockers": [],
        }
        o096_packet = implementation_packet(parameters, "CA-O-096", [permitted])
        validate_outcome(o096_packet, permitted)

        repaired_result = {
            "step_definition_id": "CA-O-099",
            "action_definition_id": "CA-O-021",
            "result": "repaired",
            "outputs": {"changed": True},
            "evidence": [{"kind": "fixture"}],
            "blockers": [],
        }
        last_round_packet = implementation_packet(parameters, "CA-O-099", [permitted])
        self.assertEqual(
            last_round_packet["retry"]["consumed"],
            last_round_packet["retry"]["effective_limit"],
        )
        validate_outcome(last_round_packet, repaired_result)

        exhausted_packet = implementation_packet(
            parameters, "CA-O-096", [permitted, repaired_result]
        )
        with self.assertRaises(ValueError):
            validate_outcome(exhausted_packet, permitted)

        blocked = {
            "result": "retry_blocked",
            "outputs": {},
            "evidence": [],
            "blockers": ["retry budget exhausted"],
        }
        validate_outcome(exhausted_packet, blocked)

        beyond_budget_packet = implementation_packet(
            parameters,
            "CA-O-099",
            [permitted, repaired_result, permitted],
        )
        self.assertGreater(
            beyond_budget_packet["retry"]["consumed"],
            beyond_budget_packet["retry"]["effective_limit"],
        )
        with self.assertRaises(ValueError):
            validate_outcome(beyond_budget_packet, repaired_result)


if __name__ == "__main__":
    unittest.main()
