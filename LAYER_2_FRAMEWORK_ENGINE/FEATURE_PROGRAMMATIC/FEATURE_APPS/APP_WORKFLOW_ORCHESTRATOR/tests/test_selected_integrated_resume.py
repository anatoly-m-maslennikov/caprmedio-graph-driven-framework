"""Frozen O016@18 journeys for the bounded Integrated result coordinator."""

from __future__ import annotations

import copy
from collections.abc import Callable, Mapping
from pathlib import Path
import sys
from typing import Any, cast
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
for location in (APP, Path(__file__).resolve().parent):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution_run_plan import build_requested_runs  # noqa: E402
from selected_integrated_action_provider import current_integrated_action_provider  # noqa: E402
from selected_integrated_dispatch import dispatch_integrated  # noqa: E402
from selected_integrated_frontier_records import MAX_RECORD_BYTES, state_path  # noqa: E402
from selected_integrated_resume import resume_integrated  # noqa: E402
from selected_integrated_session import restore_checkpoint  # noqa: E402
from selected_integrated_dispatch_test_support import IntegratedDispatchTestCase  # noqa: E402
from shared_context_direct_fixture import DirectSharedContextFixture  # noqa: E402
from workflow_run_support import RunTracker, _canonical_digest, _proposal, _validate_common  # noqa: E402


class CountingProvider:
    def __init__(self) -> None:
        self.calls = 0

    def __call__(
        self,
        packet: Mapping[str, Any],
        *,
        agent: Callable[[str, Mapping[str, Any]], Mapping[str, Any]],
        selected_project_root: Path,
        trusted_execution_authorization: Mapping[str, Any] | None = None,
    ) -> dict[str, Any]:
        self.calls += 1
        return current_integrated_action_provider(
            packet,
            agent=agent,
            selected_project_root=selected_project_root,
            trusted_execution_authorization=trusted_execution_authorization,
        )


class IntegratedResumeFixture(IntegratedDispatchTestCase):
    fixture_loader = DirectSharedContextFixture

    def setUp(self) -> None:
        super().setUp()
        self.resume_revalidate = patch(
            "selected_integrated_resume.revalidate",
            side_effect=lambda _root, frozen: copy.deepcopy(frozen["graph"]),
        )
        self.resume_revalidate.start()
        self.addCleanup(self.resume_revalidate.stop)

    def _reseal(self, frozen: dict[str, Any], tracker: RunTracker) -> None:
        request = cast(dict[str, Any], frozen["request"])
        execution, graph = request["execution"], frozen["graph"]
        parameters = cast(dict[str, Any], execution["parameters"])
        execution["parameters_digest"] = _canonical_digest(parameters)
        execution["requested_runs"] = build_requested_runs(
            graph, request["run_id"], parameters["run_visit_limits"]
        )
        parsed = _validate_common(execution)
        proposal = _proposal(parsed, tracker._observe(parsed))
        execution["proposal_receipt"] = proposal
        execution["proposal_receipt_digest"] = _canonical_digest(proposal)
        execution["operator_authorization"] = {
            **execution["operator_authorization"],
            "parameters_digest": execution["parameters_digest"],
            "proposal_receipt_digest": execution["proposal_receipt_digest"],
        }

    def _journey(self, run_id: str) -> tuple[dict[str, Any], RunTracker, list[dict[str, Any]]]:
        frozen, tracker = self.frozen(run_id)
        request = cast(dict[str, Any], frozen["request"])
        execution = cast(dict[str, Any], request["execution"])
        graph = cast(dict[str, Any], frozen["graph"])
        steps = {row["atom_id"]: row for row in cast(list[dict[str, Any]], graph["steps"])}
        steps["CA-O-231"]["on_result"] = [
            {"result": "evaluation_ready", "next": "CA-O-232"},
            {"result": "evaluation_runnable", "next": "CA-O-094"},
        ]
        steps["CA-O-232"]["on_result"] = [{"result": "prepared", "next": "CA-O-231"}]
        execution["parameters"] = copy.deepcopy(execution["parameters"])
        base = cast(dict[str, Any], execution["parameters"])["base_packet"]
        workspace = self.root / "fixture" / "disposable-workspace"
        workspace.mkdir(parents=True)
        base["workspace"] = str(workspace)
        base["permissions"]["implementation_workspace"]["path"] = str(workspace)
        self._reseal(frozen, tracker)
        return frozen, tracker, [dict(row) for row in self.fixture.trusted_methods]

    @staticmethod
    def _submission(pending: Mapping[str, Any], response: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "continuation_id": pending["continuation_id"],
            "action_run_id": pending["action_run_id"],
            "result": dict(response),
        }

    @staticmethod
    def _response(result: str, outputs: Mapping[str, Any]) -> dict[str, Any]:
        return {
            "result": result,
            "outputs": dict(outputs),
            "evidence": [{"kind": "fixture"}],
            "blockers": [],
        }


class SelectedIntegratedResumeTests(IntegratedResumeFixture):
    def test_three_pending_publications_advance_plan_without_replay(self) -> None:
        frozen, tracker, methods = self._journey("integrated-resume")
        provider = CountingProvider()
        self.assertGreaterEqual(len(methods), 40)
        initial = dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_methods=methods, action=provider
        )
        plan = {
            "plan_id": "journey",
            "item_id": "prepare",
            "dod": ["tested"],
            "estimated_minutes": 1,
        }
        second = resume_integrated(
            self.root,
            frozen,
            self._submission(initial, self._response("evaluation_ready", {"plan_item": plan})),
            tracker=tracker,
            trusted_methods=methods,
            action=provider,
        )
        repeated = resume_integrated(
            self.root,
            frozen,
            self._submission(initial, self._response("evaluation_ready", {"plan_item": plan})),
            tracker=tracker,
            trusted_methods=methods,
            action=provider,
        )
        third = resume_integrated(
            self.root,
            frozen,
            self._submission(second, self._response("prepared", {"tests": ["ok"]})),
            tracker=tracker,
            trusted_methods=methods,
            action=provider,
        )
        fourth = resume_integrated(
            self.root,
            frozen,
            self._submission(third, self._response("evaluation_runnable", {"plan_item": plan})),
            tracker=tracker,
            trusted_methods=methods,
            action=provider,
        )

        self.assertEqual(second, repeated)
        self.assertEqual(
            ["CA-O-232", "CA-O-231", "CA-O-094"],
            [item["capture"]["step_id"] for item in (second, third, fourth)],
        )
        self.assertEqual(plan, second["capture"]["packet"]["plan_item"])
        self.assertEqual(7, provider.calls)
        self.assertLessEqual(
            state_path(self.root, "integrated-resume").stat().st_size, MAX_RECORD_BYTES
        )
        session = restore_checkpoint(self.root, frozen, tracker)
        self.assertNotIn("integrated-resume", session.terminal)
        self.assertFalse(session.interrupted)


if __name__ == "__main__":
    unittest.main()
