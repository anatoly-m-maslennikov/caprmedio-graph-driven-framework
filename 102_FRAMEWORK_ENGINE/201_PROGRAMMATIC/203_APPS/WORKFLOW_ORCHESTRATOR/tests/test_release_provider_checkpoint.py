"""Cached source effects require actual Run state and their saved progress."""

from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    sys.path.insert(0, str(location))

from selected_native_providers import SelectedNativeProviders  # noqa: E402


class ReleaseProviderCheckpointTests(unittest.TestCase):
    def setUp(self):
        self.result = SimpleNamespace(
            outcome="completed", effect_evidence_refs=("evidence/actual.json",)
        )
        self.run = SimpleNamespace(
            results={0: self.result}, contexts={0: SimpleNamespace(action_run_id="actual-action")}
        )
        self.terminal = {
            "disposition": "terminal",
            "outcome": "completed",
            "run_id": "actual-action",
            "result_ref": "runs/action.json",
            "effect_refs": ["evidence/actual.json"],
        }
        self.session = SimpleNamespace(terminal={"requested-action": self.terminal})
        self.progress = {
            "action_run_id": "actual-action",
            "result": "phase-completed",
            "effect_refs": ["evidence/actual.json"],
        }

    def proven(self, recordings=None, allowed=frozenset({"completed"})):
        return SelectedNativeProviders._restored_completed_result_is_proven(
            self.session,
            index=0,
            run=self.run,
            shared_recordings=recordings or {},
            requested_action="requested-action",
            action_run_id="actual-action",
            expected_result="phase-completed",
            progress_reader=lambda requested: self.progress,
            allowed_private_outcomes=allowed,
        )

    def test_cached_actual_result_needs_no_journal_receipt(self):
        self.assertTrue(self.proven())
        self.assertTrue(self.proven({0: {"arbitrary": "historical log metadata"}}))

    def test_wrong_or_unfinished_actual_action_cannot_reuse_cached_effects(self):
        for field, value in (
            ("disposition", "interrupted"),
            ("outcome", "failed"),
            ("run_id", "different-action"),
            ("result_ref", ""),
            ("effect_refs", []),
        ):
            with self.subTest(field=field):
                previous = self.terminal[field]
                self.terminal[field] = value
                self.assertFalse(self.proven())
                self.terminal[field] = previous

    def test_wrong_saved_source_progress_cannot_reuse_cached_effects(self):
        for field, value in (
            ("action_run_id", "different-action"),
            ("result", "different-result"),
            ("effect_refs", []),
        ):
            with self.subTest(field=field):
                previous = self.progress[field]
                self.progress[field] = value
                self.assertFalse(self.proven())
                self.progress[field] = previous

    def test_missing_typed_result_or_native_context_blocks_reuse(self):
        self.run.results = {}
        self.assertFalse(self.proven())
        self.run.results = {0: self.result}
        self.run.contexts = {}
        self.assertFalse(self.proven())

    def test_retained_native_pending_label_requires_explicit_source_disposition(self):
        self.result.outcome = "pending"
        self.assertFalse(self.proven())
        self.assertTrue(self.proven(allowed=frozenset({"pending"})))

    def test_already_started_action_without_private_result_is_never_replayed(self):
        self.assertTrue(
            SelectedNativeProviders._restored_action_without_typed_result_is_blocked(
                {"restored_action": True},
                cached_result=False,
            )
        )
        self.assertFalse(
            SelectedNativeProviders._restored_action_without_typed_result_is_blocked(
                {"restored_action": True},
                cached_result=True,
            )
        )


if __name__ == "__main__":
    unittest.main()
