"""Bounded documentary recovery of real Session recording failures.

These tests reopen actual canonical starts and immutable pending Events; they
do not claim a package pass, authorize effects, or replay an interrupted Run.
"""

from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

RELEASE_ROOT = Path(__file__).resolve().parents[1]
for directory in (RELEASE_ROOT, RELEASE_ROOT.parent, Path(__file__).resolve().parent):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import test_selected_installation_command as command_fixture  # noqa: E402
import work_journal  # noqa: E402
from release_checkpoint import _native_partial_publication_hint, _reopen_native_partial_frontier_start  # noqa: E402
from release_contract import ReleaseContractError  # noqa: E402
from release_actions import SelectedReleaseActionContext  # noqa: E402
from workflow_run_support import RunExecutionSession  # noqa: E402


class SelectedNativePartialFrontierTests(unittest.TestCase):
    def setUp(self):
        self.fixture = command_fixture.SelectedInstallationCommandTests("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.command()
        self.fixture.query_defaults()

    def pending(self, outcome):
        with patch.object(work_journal, "append_sealed_events", side_effect=OSError("actual fixture append interruption")):
            result = self.fixture.session.finish_run(
                "actual-action", outcome=outcome, result_ref="results/exact-partial.json",
                effect_refs=[".caprmedio_runtime/installation/lock.toml"],
            )
        self.assertEqual(result["disposition"], "recording_pending")
        return {"event_id": self.fixture.session.pending[-1], "event_outcome": outcome}

    def assert_read_only_reopen(self, pending):
        path = work_journal._pending_path(self.fixture.root, pending["event_id"])
        before = path.read_bytes()
        journal = {item: item.read_bytes() for item in (self.fixture.root / work_journal.configured_journal_root(self.fixture.root)).iterdir() if item.is_file()}
        self.assertIsNone(_reopen_native_partial_frontier_start(str(self.fixture.root), self.fixture.context, pending))
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual({item: item.read_bytes() for item in journal}, journal)
        return path

    def test_uncertain_effect_pending_recording_preserves_exact_actual_event(self):
        pending = self.pending("partial")
        self.assert_read_only_reopen(pending)
        changed = dict(pending, event_outcome="completed")
        with self.assertRaises(ReleaseContractError):
            _reopen_native_partial_frontier_start(str(self.fixture.root), self.fixture.context, changed)

    def test_interrupted_pending_recording_restores_documentary_start_not_permission(self):
        pending = self.pending("interrupted_pending")
        self.assert_read_only_reopen(pending)
        self.assertFalse(self.fixture.session.interrupted)
        self.assertIn(pending["event_id"], self.fixture.session.pending)

    def test_changed_canonical_source_refuses_partial_documentary_frontier(self):
        pending = self.pending("partial")
        path = self.fixture.root / self.fixture.source["path"]
        path.write_bytes(path.read_bytes() + b"\n# changed after start\n")
        with self.assertRaises(ReleaseContractError):
            _reopen_native_partial_frontier_start(str(self.fixture.root), self.fixture.context, pending)

    def test_same_byte_source_alias_cannot_replace_canonical_started_binding(self):
        pending = self.pending("partial")
        source = self.fixture.root / self.fixture.source["path"]
        physical = self.fixture.root / "physical-action-source.md"
        physical.write_bytes(source.read_bytes())
        source.unlink()
        source.symlink_to(physical)
        with self.assertRaises(ReleaseContractError):
            _reopen_native_partial_frontier_start(str(self.fixture.root), self.fixture.context, pending)

    def test_retirement_pending_recording_requires_its_own_actual_o179_chain(self):
        request = copy.deepcopy(self.fixture.session.request)
        request["request_id"] = "retirement-documentary-fixture"
        request["operator_authorization"]["request_id"] = request["request_id"]
        source = self.fixture.root / "operations/CA-O-179.md"
        source.write_bytes(b"---\natom_id: CA-O-179\nversion: 3\n---\nretirement fixture source\n")
        request["requested_runs"][1]["definition"] = {
            "atom_id": "CA-O-179", "version": 3, "path": "operations/CA-O-179.md",
            "digest": hashlib.sha256(source.read_bytes()).hexdigest(),
        }
        session = RunExecutionSession(self.fixture.tracker, request)
        session.start_run("wf", run_id="retirement-workflow")
        session.start_run("step", run_id="retirement-step")
        session.start_run("action", run_id="retirement-action")
        context = SelectedReleaseActionContext(
            str(self.fixture.root), "retirement-workflow", "retirement-step", "retirement-action",
            "retirement-workflow", "retirement-step", "CA-O-179", "CA-O-169",
            self.fixture.run.frozen_parameters_sha256, workflow_version=9,
        )
        with patch.object(work_journal, "append_sealed_events", side_effect=OSError("actual fixture append interruption")):
            session.finish_run("retirement-action", outcome="partial", result_ref="results/retirement.json", effect_refs=[])
        pending = {"event_id": session.pending[-1], "event_outcome": "partial"}
        self.assertIsNone(_reopen_native_partial_frontier_start(str(self.fixture.root), context, pending))
        with self.assertRaises(ReleaseContractError):
            _reopen_native_partial_frontier_start(str(self.fixture.root), self.fixture.context, pending)

    def test_partial_decode_hint_is_narrow_and_cannot_turn_success_into_uncertainty(self):
        self.assertTrue(_native_partial_publication_hint({"in_progress": {}, "next_phase": 10, "stopped": False}))
        source = {"in_progress": None, "next_phase": 11, "stopped": True,
                  "results": [{"index": 10, "result": {"outcome": "effect_uncertain"}}]}
        self.assertTrue(_native_partial_publication_hint(source))
        changed = copy.deepcopy(source)
        changed["results"][0]["result"]["outcome"] = "completed"
        self.assertFalse(_native_partial_publication_hint(changed))
        changed = copy.deepcopy(source)
        changed["stopped"] = False
        self.assertFalse(_native_partial_publication_hint(changed))
        self.assertFalse(_native_partial_publication_hint({"in_progress": {}, "next_phase": 9, "stopped": False}))


if __name__ == "__main__":
    unittest.main()
