"""Current O016 dispatch ownership checks before legacy dispatch can begin."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path
import sys
from typing import Any
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

import selected_dispatch  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_execution_contracts import SelectedExecutionError  # noqa: E402


def _frozen(*, version: int = 18, entry_step: str = "CA-O-231") -> dict[str, Any]:
    return {
        "request": {
            "run_id": "current-integrated",
            "execution": {
                "operation_route": "run_implementation_workflow",
                "mode": "execute",
                "parameters": {"base_packet": {}, "step_packets": {}},
            },
        },
        "graph": {
            "route": "run_implementation_workflow",
            "entry_step": entry_step,
            "workflow": {"atom_id": "CA-O-016", "version": version},
        },
    }


class SelectedDispatchCurrentIntegratedTests(unittest.TestCase):
    def test_owner_recognition_ignores_invalid_current_packet_until_integrated_admission(
        self,
    ) -> None:
        self.assertTrue(selected_dispatch._is_current_integrated(_frozen()))
        self.assertTrue(selected_dispatch._is_current_integrated(_frozen(version=20)))
        self.assertFalse(selected_dispatch._is_current_integrated(_frozen(version=17)))
        self.assertFalse(selected_dispatch._is_current_integrated(_frozen(version=19)))
        self.assertTrue(selected_dispatch._is_current_integrated(_frozen(entry_step="CA-O-091")))

    def test_selected_execution_facade_routes_v20_to_integrated_before_legacy(self) -> None:
        expected = {"disposition": "started", "status": "pending_action"}
        execution = object.__new__(SelectedExecution)
        execution.root = Path("/selected-project")
        execution.handlers = {}
        with (
            patch.object(selected_dispatch, "dispatch_current_integrated", return_value=expected) as direct,
            patch.object(selected_dispatch, "dispatch_admitted_with_failure_boundary") as legacy,
        ):
            result = execution.dispatch(_frozen(version=20))

        self.assertEqual(expected, result)
        direct.assert_called_once()
        legacy.assert_not_called()

    def test_wrong_current_entry_is_refused_before_integrated_or_legacy_dispatch(self) -> None:
        with self.assertRaisesRegex(SelectedExecutionError, "enter at CA-O-231"):
            selected_dispatch.dispatch_current_integrated(
                Path("/selected-project"), {}, _frozen(entry_step="CA-O-091")
            )

    def test_current_malformed_packet_cannot_fall_through_to_legacy_dispatch(self) -> None:
        expected = {"disposition": "blocked", "outcome": "blocked"}
        with (
            patch.object(
                selected_dispatch, "dispatch_current_integrated", return_value=expected
            ) as direct,
            patch.object(selected_dispatch, "dispatch_admitted_with_failure_boundary") as legacy,
        ):
            result = selected_dispatch.dispatch(Path("/selected-project"), {}, _frozen())

        self.assertEqual(expected, result)
        direct.assert_called_once()
        legacy.assert_not_called()

    def test_common_admission_precedes_trusted_method_load(self) -> None:
        events: list[str] = []
        frozen = _frozen()
        tracker = object()
        expected = {"status": "pending_action"}

        def admit(received_tracker: object, execution: object) -> None:
            self.assertIs(tracker, received_tracker)
            self.assertEqual(frozen["request"]["execution"], execution)
            events.append("validate")

        def methods(_root: Path, _frozen: Mapping[str, Any]) -> tuple[object, ...]:
            events.append("methods")
            return ()

        with (
            patch("selected_run_session.shared_tracker", return_value=tracker),
            patch("selected_integrated_dispatch_admission.validate", side_effect=admit),
            patch("shared_context_validation_loader.load_frozen_methods", side_effect=methods),
            patch(
                "selected_integrated_dispatch.dispatch_integrated", return_value=expected
            ) as dispatch,
        ):
            result = selected_dispatch.dispatch_current_integrated(
                Path("/selected-project"), {}, frozen
            )

        self.assertEqual(expected, result)
        self.assertEqual(["validate", "methods"], events)
        dispatch.assert_called_once_with(
            Path("/selected-project"), frozen, tracker=tracker, trusted_methods=()
        )


if __name__ == "__main__":
    unittest.main()
