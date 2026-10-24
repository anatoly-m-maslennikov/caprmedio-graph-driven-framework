# implementation of:
# Evaluation: CA-E-652
"""Direct-Method source coverage for the source-bound Integrated bridge."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
from typing import Any
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_execution_contracts import SelectedExecutionError  # noqa: E402
from selected_integrated_action import (  # noqa: E402
    IntegratedActionInputError,
    IntegratedActionPending,
    current_integrated_action_provider,
    invoke_integrated_action,
    submit_integrated_action,
)
from selected_integrated_dispatch import dispatch_integrated  # noqa: E402
from selected_integrated_dispatch_test_support import (  # noqa: E402
    IntegratedDispatchTestCase,
    PendingProvider,
)
from shared_context_direct_fixture import DirectSharedContextFixture  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402


STEP_ID = "CA-O-231"
ACTION_ID = "CA-O-017"


def _profile(fixture: DirectSharedContextFixture) -> dict[str, Any]:
    pins = {pin["atom_id"]: dict(pin) for pin in fixture.source_pins()}
    return {
        "workflow": pins["CA-O-016"],
        "entry_step": STEP_ID,
        "steps": {
            step: {"step": pins[step], "action": pins[action]} for step, action in ACTIONS.items()
        },
    }


class SelectedIntegratedDirectBridgeTests(IntegratedDispatchTestCase):
    fixture_loader = DirectSharedContextFixture

    def _trusted_methods(self) -> list[dict[str, Any]]:
        return [dict(row) for row in self.fixture.trusted_methods]

    def test_direct_capture_persists_methods_and_rejects_reentry_drift(self) -> None:
        frozen, tracker = self.frozen("integrated-direct")
        methods = self._trusted_methods()
        provider = PendingProvider()
        pending = dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_methods=methods, action=provider
        )
        capture = pending["capture"]
        self.assertEqual(methods, capture["definitions"]["trusted_methods"])
        self.assertIsNone(capture["definitions"]["trusted_method_projection"])
        self.assertEqual(
            {"workflow_run_id", "step_run_id", "action_run_id"},
            set(pending) & {"workflow_run_id", "step_run_id", "action_run_id"},
        )
        resumed = dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_methods=methods, action=provider
        )
        self.assertEqual(pending["continuation_id"], resumed["continuation_id"])

        changed = copy.deepcopy(methods)
        changed[0]["sha256"] = "0" * 64
        with self.assertRaises(SelectedExecutionError):
            dispatch_integrated(
                self.root, frozen, tracker=tracker, trusted_methods=changed, action=provider
            )
        self.assertEqual(1, provider.calls)

    def test_dispatch_rejects_a_trusted_direct_subset_of_the_frozen_inventory(self) -> None:
        frozen, tracker = self.frozen("integrated-direct-subset")
        request = frozen["request"]
        assert isinstance(request, dict)
        execution = request["execution"]
        assert isinstance(execution, dict)
        parameters = execution["parameters"]
        assert isinstance(parameters, dict)
        base = parameters["base_packet"]
        steps = parameters["step_packets"]
        assert isinstance(base, dict) and isinstance(steps, dict)
        packet = copy.deepcopy({**base, **steps[STEP_ID]})
        packet.pop("plan_item")
        methods = self._trusted_methods()[:-1]
        packet["methods"] = methods
        profile = _profile(self.fixture)
        row = profile["steps"][STEP_ID]
        with self.assertRaises(IntegratedActionPending):
            invoke_integrated_action(
                current_integrated_action_provider,
                packet,
                step_id=STEP_ID,
                action_id=ACTION_ID,
                context="Integrated",
                selected_project_root=self.root,
                workflow_definition=profile["workflow"],
                step_definition=row["step"],
                action_definition=row["action"],
                trusted_workflow_binding=profile,
                trusted_methods=methods,
            )
        provider = PendingProvider()
        with patch("selected_action_context.implementation_packet") as build_packet:
            with self.assertRaises(SelectedExecutionError):
                dispatch_integrated(
                    self.root, frozen, tracker=tracker, trusted_methods=methods, action=provider
                )
        build_packet.assert_not_called()
        self.assertEqual(0, provider.calls)

    def test_direct_submission_revalidates_full_packet_methods(self) -> None:
        fixture = DirectSharedContextFixture.load()
        temporary = tempfile.TemporaryDirectory(dir=APP.parents[3] / ".caprmedio_tmp")
        self.addCleanup(temporary.cleanup)
        root = fixture.materialize(Path(temporary.name) / "project")
        profile = _profile(fixture)
        parameters = fixture.native_implementation_parameters()
        packet = {
            **copy.deepcopy(parameters["base_packet"]),
            **copy.deepcopy(parameters["step_packets"][STEP_ID]),
        }
        packet.pop("plan_item")
        row = profile["steps"][STEP_ID]
        methods = [dict(source) for source in fixture.trusted_methods]
        with self.assertRaises(IntegratedActionPending) as raised:
            invoke_integrated_action(
                current_integrated_action_provider,
                packet,
                step_id=STEP_ID,
                action_id=ACTION_ID,
                context="Integrated",
                selected_project_root=root,
                workflow_definition=profile["workflow"],
                step_definition=row["step"],
                action_definition=row["action"],
                trusted_workflow_binding=profile,
                trusted_methods=methods,
            )
        capture = raised.exception.capture
        self.assertEqual(methods, capture["definitions"]["trusted_methods"])
        capture["packet"]["methods"][0]["content"] += "\nchanged"
        response = {
            "result": "evaluation_ready",
            "outputs": {"plan_item": "fixture-plan"},
            "evidence": [{"kind": "direct-fixture"}],
            "blockers": [],
        }
        with self.assertRaises(IntegratedActionInputError):
            submit_integrated_action(current_integrated_action_provider, capture, response)
