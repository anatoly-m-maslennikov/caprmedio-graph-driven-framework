"""Currentness and idempotency guards for the Integrated resume coordinator."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
for location in (APP, Path(__file__).resolve().parent):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution_contracts import SelectedExecutionError  # noqa: E402
from selected_integrated_dispatch import dispatch_integrated  # noqa: E402
from selected_integrated_frontier import IntegratedFrontierError  # noqa: E402
from selected_integrated_resume import resume_integrated  # noqa: E402
from test_selected_integrated_resume import (  # noqa: E402
    CountingProvider,
    IntegratedResumeFixture,
)


class SelectedIntegratedResumeGuardTests(IntegratedResumeFixture):
    def test_method_drift_refuses_before_the_submitted_provider_runs(self) -> None:
        frozen, tracker, methods = self._journey("integrated-resume-drift")
        provider = CountingProvider()
        pending = dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_methods=methods, action=provider
        )
        changed = copy.deepcopy(methods)
        changed[0]["content"] += "\nchanged"

        with self.assertRaises(SelectedExecutionError):
            resume_integrated(
                self.root,
                frozen,
                self._submission(pending, self._response("evaluation_ready", {"plan_item": {}})),
                tracker=tracker,
                trusted_methods=changed,
                action=provider,
            )

        self.assertEqual(1, provider.calls)

    def test_conflicting_repeat_submission_is_refused_without_provider_replay(self) -> None:
        frozen, tracker, methods = self._journey("integrated-resume-conflict")
        provider = CountingProvider()
        pending = dispatch_integrated(
            self.root, frozen, tracker=tracker, trusted_methods=methods, action=provider
        )
        plan = {"plan_id": "one", "item_id": "one", "dod": ["one"], "estimated_minutes": 1}
        resume_integrated(
            self.root,
            frozen,
            self._submission(pending, self._response("evaluation_ready", {"plan_item": plan})),
            tracker=tracker,
            trusted_methods=methods,
            action=provider,
        )
        calls = provider.calls
        conflict = {"plan_id": "two", "item_id": "two", "dod": ["two"], "estimated_minutes": 1}

        with self.assertRaises(IntegratedFrontierError):
            resume_integrated(
                self.root,
                frozen,
                self._submission(
                    pending, self._response("evaluation_ready", {"plan_item": conflict})
                ),
                tracker=tracker,
                trusted_methods=methods,
                action=provider,
            )

        self.assertEqual(calls, provider.calls)


if __name__ == "__main__":
    unittest.main()
