"""Refusal checks for retained Integrated pending dispatches."""

from __future__ import annotations

import copy

from selected_evidence_io import atomic_write, run_directory
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_dispatch import _frontier, dispatch_integrated
from selected_integrated_dispatch_capture import CAPTURE_NAME, load_capture
from selected_integrated_dispatch_profile import profile_from_frozen
from selected_integrated_frontier import IntegratedFrontierStore
from selected_integrated_frontier_records import digest
from selected_integrated_dispatch_test_support import (
    IntegratedDispatchTestCase,
    PendingProvider,
)


class SelectedIntegratedDispatchGuardTests(IntegratedDispatchTestCase):
    def test_forged_graph_refusal_precedes_provider(self) -> None:
        frozen, tracker = self.frozen("integrated-forged-graph")
        provider = PendingProvider()
        expected = copy.deepcopy(frozen["graph"])
        forged = copy.deepcopy(frozen)
        forged["graph"]["steps"][0]["on_result"] = [{"result": "forged", "terminal": "completed"}]

        def canonical_graph(_root: object, candidate: object) -> object:
            if candidate != frozen:
                raise SelectedExecutionError(
                    "selected Workflow graph changed after queue admission"
                )
            return expected

        self.revalidate_mock.side_effect = canonical_graph
        with self.assertRaisesRegex(SelectedExecutionError, "graph changed"):
            dispatch_integrated(
                self.root,
                forged,
                tracker=tracker,
                trusted_method_projection=self.fixture.support_inventory["method_projection"],
                action=provider,
            )
        self.assertEqual(0, provider.calls)

    def test_reentry_checks_currentness_before_republishing_prompt(self) -> None:
        frozen, tracker = self.frozen("integrated-currentness")
        provider = PendingProvider()
        methods = self.fixture.support_inventory["method_projection"]
        dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_method_projection=methods, action=provider
        )
        tracker.source_observer = lambda _request: {
            "selected": True,
            "current": False,
            "observed": {},
        }
        with self.assertRaisesRegex(SelectedExecutionError, "currentness"):
            dispatch_integrated(
                self.root,
                frozen,
                tracker=tracker,
                trusted_method_projection=methods,
                action=provider,
            )
        self.assertEqual(1, provider.calls)

    def test_continuation_is_bound_to_the_actual_action_visit(self) -> None:
        frozen, tracker = self.frozen("integrated-repeat")
        provider = PendingProvider()
        methods = self.fixture.support_inventory["method_projection"]
        pending = dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_method_projection=methods, action=provider
        )
        capture = pending["capture"]
        profile = profile_from_frozen(self.root, frozen)
        revisited = copy.deepcopy(capture)
        revisited["run_binding"]["action_run_id"] = "actual-action-revisit"
        first = _frontier(self.root, "integrated-repeat", frozen, profile, capture)
        second = _frontier(self.root, "integrated-repeat", frozen, profile, revisited)
        self.assertNotEqual(first["continuation_id"], second["continuation_id"])

    def test_stale_prompt_refuses_before_pending_republish(self) -> None:
        run_id = "integrated-stale-prompt"
        frozen, tracker = self.frozen(run_id)
        provider = PendingProvider()
        methods = self.fixture.support_inventory["method_projection"]
        dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_method_projection=methods, action=provider
        )
        with IntegratedFrontierStore(self.root, run_id) as store:
            frontier = store.load()["frontier"]
            self.assertIsInstance(frontier, dict)
            capture = load_capture(self.root, run_id, frontier)
            capture["prompt"] = "stale prompt"
            value = {
                "frontier_digest": digest(frontier),
                "capture": capture,
                "capture_digest": digest(capture),
            }
            continuation = frontier["continuation_id"]
            path = run_directory(self.root, run_id) / (
                f"{CAPTURE_NAME.removesuffix('.json')}-{continuation}.json"
            )
            atomic_write(path, value)
        with self.assertRaisesRegex(SelectedExecutionError, "prompt is stale"):
            dispatch_integrated(
                self.root,
                frozen,
                tracker=tracker,
                trusted_method_projection=methods,
                action=provider,
            )
        self.assertEqual(1, provider.calls)
