"""Synthetic status observations for the technical container coordinator."""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest import mock


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

import backend  # noqa: E402


RUN_ID = "container-status-run"
CHILD_ID = f"{RUN_ID}:member:child"
PARENT_ID = f"{RUN_ID}:member:parent"
ACTUAL_CHILD_ID = f"{RUN_ID}:actual:child"
ACTUAL_PARENT_ID = f"{RUN_ID}:actual:parent"


def _marker() -> dict[str, object]:
    return {"coordinator_id": RUN_ID, "sealed": True}


def _frozen(*, container: bool) -> dict[str, object]:
    observed: dict[str, object] = {"lifecycle_admission": {}}
    if container:
        observed["container_lifecycle"] = _marker()
    return {
        "request": {
            "run_id": RUN_ID,
            "execution": {
                "proposal_receipt": {"source_freshness": {"observed": observed}},
                "requested_runs": [{"requested_run_id": RUN_ID, "kind": "workflow"}],
            },
        },
        "graph": {"workflow": {"atom_id": "CA-O-127"}, "route": "change_atom_status"},
    }


def _aggregate(*, outcome: str = "completed", disposition: str = "terminal") -> dict[str, object]:
    child_actual_id = ACTUAL_CHILD_ID if outcome in {"completed", "partial"} else None
    parent_actual_id = ACTUAL_PARENT_ID if outcome == "completed" else None
    members = [
        {"atom_id": "CA-P-CHILD", "requested_run_id": CHILD_ID, "actual_run_id": child_actual_id,
         "outcome": "completed" if child_actual_id else ("failed" if outcome == "failed" else "interrupted_pending"),
         "effect_refs": []},
        {"atom_id": "CA-PARENT", "requested_run_id": PARENT_ID, "actual_run_id": parent_actual_id,
         "outcome": "completed" if parent_actual_id else "untouched", "effect_refs": []},
    ]
    return {
        "schema": "container-lifecycle/v1",
        "coordinator_id": RUN_ID,
        "parent_requested_run_id": PARENT_ID,
        "parent_run_id": parent_actual_id,
        "original_requested_root_run_started": False,
        "members": members,
        "completed": [ACTUAL_CHILD_ID, ACTUAL_PARENT_ID] if outcome == "completed" else
        [ACTUAL_CHILD_ID] if outcome == "partial" else [],
        "failed": {"atom_id": "CA-P-CHILD", "requested_run_id": CHILD_ID, "outcome": "failed"}
        if outcome in {"failed", "pending"} else None,
        "untouched": [PARENT_ID] if outcome in {"partial", "pending", "failed"} else [],
        "effect_refs": [".caprmedio_caprmedio/fixture/parent.md"],
        "outcome": outcome,
        "disposition": disposition,
    }


class ContainerStatusTests(unittest.TestCase):
    def _status(
        self,
        result: dict[str, object] | None,
        *,
        container: bool = True,
        scheduler_status: str = "SUCCESS",
        accepted: bool = True,
    ) -> dict[str, object]:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selected_directory = root / "selected"
            selected_directory.mkdir()
            (selected_directory / "selected_request.json").touch()
            if accepted:
                (selected_directory / "accepted.json").touch()
            selected = mock.Mock()
            selected.root = root
            selected.run_directory.return_value = selected_directory
            reads = [_frozen(container=container)]
            if accepted:
                reads.append({"result": result})
            selected._read.side_effect = reads
            handle = mock.Mock()
            handle.get_status.return_value = types.SimpleNamespace(status=scheduler_status)
            transport = mock.Mock()
            transport.retrieve_workflow.return_value = handle
            with mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                    mock.patch.object(backend, "client", return_value=transport):
                observed = backend.status(root, {"operation": "status", "run_id": RUN_ID})
        return observed

    def test_completed_aggregate_exposes_actual_parent_and_technical_coordinator(self):
        observed = self._status(_aggregate())

        self.assertEqual("SUCCESS", observed["scheduler_status"])
        self.assertEqual(RUN_ID, observed["coordinator_id"])
        self.assertEqual("technical_coordinator", observed["identity_kind"])
        self.assertEqual(PARENT_ID, observed["parent_requested_run_id"])
        self.assertEqual(ACTUAL_PARENT_ID, observed["parent_run_id"])
        self.assertEqual([ACTUAL_CHILD_ID, ACTUAL_PARENT_ID], observed["completed"])
        self.assertEqual(ACTUAL_PARENT_ID, observed["members"][-1]["actual_run_id"])
        self.assertNotIn("member_run_ids", observed)
        self.assertEqual("completed", observed["outcome"])
        self.assertEqual("terminal", observed["disposition"])
        self.assertNotIn("workflow_run_id", observed)
        self.assertNotIn("workflow_id", observed)

    def test_partial_aggregate_preserves_failed_and_untouched_members(self):
        observed = self._status(_aggregate(outcome="partial"))

        self.assertEqual("partial", observed["outcome"])
        self.assertEqual([ACTUAL_CHILD_ID], observed["completed"])
        self.assertEqual(PARENT_ID, observed["parent_requested_run_id"])
        self.assertIsNone(observed["parent_run_id"])
        self.assertEqual([PARENT_ID], observed["untouched"])

    def test_failed_member_aggregate_preserves_nonterminal_failure(self):
        observed = self._status(_aggregate(outcome="failed", disposition="started"))

        self.assertEqual("failed", observed["outcome"])
        self.assertEqual("started", observed["disposition"])
        self.assertEqual(CHILD_ID, observed["failed"]["requested_run_id"])
        self.assertEqual(PARENT_ID, observed["parent_requested_run_id"])
        self.assertIsNone(observed["parent_run_id"])
        self.assertEqual([PARENT_ID], observed["untouched"])

    def test_pending_aggregate_cannot_claim_terminal_completion(self):
        observed = self._status(_aggregate(outcome="pending", disposition="started"))

        self.assertEqual("pending", observed["outcome"])
        self.assertEqual("started", observed["disposition"])
        self.assertEqual(PARENT_ID, observed["parent_requested_run_id"])
        self.assertIsNone(observed["parent_run_id"])
        self.assertNotIn("workflow_run_id", observed)

    def test_requested_ids_cannot_be_relabelled_as_completed_actual_runs(self):
        aggregate = _aggregate()
        aggregate["completed"] = [CHILD_ID, PARENT_ID]
        observed = self._status(aggregate)

        self.assertEqual("interrupted_pending", observed["outcome"])
        self.assertEqual("recording_pending", observed["disposition"])
        self.assertIn("actual Run identities", observed["reason"])

    def test_failed_member_must_be_a_mapping_not_a_run_id_list(self):
        aggregate = _aggregate(outcome="failed", disposition="started")
        aggregate["failed"] = [CHILD_ID]
        observed = self._status(aggregate)

        self.assertEqual("interrupted_pending", observed["outcome"])
        self.assertEqual("recording_pending", observed["disposition"])
        self.assertIn("mapping or null", observed["reason"])

    def test_member_actual_run_cannot_claim_the_technical_coordinator(self):
        aggregate = _aggregate()
        aggregate["members"][0]["actual_run_id"] = RUN_ID
        aggregate["completed"] = [RUN_ID, ACTUAL_PARENT_ID]
        observed = self._status(aggregate)

        self.assertEqual("interrupted_pending", observed["outcome"])
        self.assertEqual("recording_pending", observed["disposition"])
        self.assertIn("technical coordinator", observed["reason"])

    def test_malformed_aggregate_is_interrupted_not_success(self):
        aggregate = _aggregate()
        aggregate["coordinator_id"] = "different-root"
        observed = self._status(aggregate)

        self.assertEqual("interrupted_pending", observed["outcome"])
        self.assertEqual("recording_pending", observed["disposition"])
        self.assertIn("coordinator", observed["reason"])
        self.assertNotIn("workflow_run_id", observed)

    def test_dbos_success_without_aggregate_is_not_workflow_completion(self):
        observed = self._status(None, accepted=False)

        self.assertEqual("interrupted_pending", observed["outcome"])
        self.assertEqual("recording_pending", observed["disposition"])
        self.assertEqual(RUN_ID, observed["coordinator_id"])
        self.assertNotIn("workflow_run_id", observed)

    def test_ordinary_selected_status_keeps_workflow_identity_and_terminal_evidence(self):
        result = {
            "disposition": "terminal",
            "terminal_runs": [{"run_id": RUN_ID, "kind": "workflow",
                                "disposition": "terminal", "outcome": "completed"}],
        }
        observed = self._status(result, container=False)

        self.assertEqual(RUN_ID, observed["workflow_run_id"])
        self.assertEqual("CA-O-127", observed["workflow_id"])
        self.assertEqual("completed", observed["outcome"])
        self.assertNotIn("coordinator_id", observed)

    def test_direct_enqueue_requires_exact_container_seal(self):
        execution = {
            "operation_route": "change_atom_status",
            "parameters": {"target": {"atom_id": "CA-P-1"}, "status": "Archived"},
            "proposal_receipt": {"source_freshness": {
                "observed": {"container_lifecycle": _marker()},
            }},
        }
        with mock.patch(
                    "container_lifecycle_admission.seal_contained_status_changes",
                    return_value={"different": "seal"},
                ), \
                mock.patch(
                    "selected_execution.preflight_selected_lifecycle",
                    return_value={"operation": "change_status"},
                ):
            with self.assertRaises(RuntimeError):
                backend._verify_container_lifecycle_seal(Path(tempfile.gettempdir()), execution)

    def test_enqueue_selected_reports_coordinator_without_a_workflow_identity(self):
        execution = {
            "operation_route": "change_atom_status",
            "proposal_receipt": {"source_freshness": {
                "observed": {"container_lifecycle": _marker()},
            }},
        }
        frozen = _frozen(container=True)
        selected = mock.Mock()
        selected.freeze.return_value = frozen
        transport = mock.Mock()
        with mock.patch.object(backend, "SelectedExecution", return_value=selected), \
                mock.patch.object(backend, "client", return_value=transport), \
                mock.patch.object(backend, "_verify_container_lifecycle_seal"), \
                mock.patch.object(backend, "status", return_value={
                    "workflow_run_id": RUN_ID, "workflow_id": "CA-O-104",
                    "scheduler_status": "ENQUEUED",
                }):
            observed = backend.enqueue_selected(Path(tempfile.gettempdir()), {
                "operation": "enqueue_selected", "run_id": RUN_ID, "execution": execution,
            })

        self.assertEqual(RUN_ID, observed["coordinator_id"])
        self.assertEqual("technical_coordinator", observed["identity_kind"])
        self.assertNotIn("workflow_run_id", observed)
        self.assertNotIn("workflow_id", observed)
        transport.enqueue.assert_called_once()


if __name__ == "__main__":
    unittest.main()
