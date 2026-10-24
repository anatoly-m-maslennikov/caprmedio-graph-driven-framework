"""Frozen-fixture checks for initial Integrated graph dispatch."""

from __future__ import annotations

import copy

from selected_integrated_dispatch_test_support import (
    IntegratedDispatchTestCase,
    PendingProvider,
)
from selected_execution_contracts import SelectedExecutionError
from selected_integrated_dispatch import dispatch_integrated
from selected_integrated_session import restore_checkpoint


class SelectedIntegratedDispatchTests(IntegratedDispatchTestCase):
    def test_initial_pending_dispatch_retains_run_ids_and_does_not_replay(self) -> None:
        frozen, tracker = self.frozen("integrated-entry")
        provider = PendingProvider()
        result = dispatch_integrated(
            self.root,
            frozen,
            tracker=tracker,
            trusted_method_projection=self.fixture.support_inventory["method_projection"],
            action=provider,
        )
        repeated = dispatch_integrated(
            self.root,
            frozen,
            tracker=tracker,
            trusted_method_projection=self.fixture.support_inventory["method_projection"],
            action=provider,
        )
        self.assertEqual("started", result["disposition"])
        self.assertEqual("pending_action", result["status"])
        self.assertEqual(result, repeated)
        self.assertEqual(1, provider.calls)
        self.assertEqual("CA-O-231", result["capture"]["step_id"])
        restored = restore_checkpoint(self.root, frozen, tracker)
        self.assertEqual(3, len(restored.actual))
        self.assertFalse(restored.terminal)
        self.assertFalse(restored.interrupted)

    def test_reentry_revalidates_the_external_method_inventory(self) -> None:
        frozen, tracker = self.frozen("integrated-method-drift")
        provider = PendingProvider()
        methods = self.fixture.support_inventory["method_projection"]
        dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_method_projection=methods, action=provider
        )
        changed = copy.deepcopy(methods)
        changed["sources"][0]["sha256"] = "0" * 64
        with self.assertRaises(SelectedExecutionError):
            dispatch_integrated(
                self.root,
                frozen,
                tracker=tracker,
                trusted_method_projection=changed,
                action=provider,
            )
        self.assertEqual(1, provider.calls)

    def test_source_mismatch_refuses_before_the_provider(self) -> None:
        frozen, tracker = self.frozen("integrated-source-drift")
        provider = PendingProvider()
        step = next(row for row in self.fixture.source_pins() if row["atom_id"] == "CA-O-231")
        source = self.root / str(step["source_path"])
        source.write_text(source.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")
        with self.assertRaisesRegex(SelectedExecutionError, "changed"):
            dispatch_integrated(
                self.root,
                frozen,
                tracker=tracker,
                trusted_method_projection=self.fixture.support_inventory["method_projection"],
                action=provider,
            )
        self.assertEqual(0, provider.calls)
