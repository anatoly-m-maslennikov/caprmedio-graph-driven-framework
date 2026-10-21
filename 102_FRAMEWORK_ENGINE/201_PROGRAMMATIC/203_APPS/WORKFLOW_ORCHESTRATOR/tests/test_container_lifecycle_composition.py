"""Focused synthetic checks for sealed container lifecycle composition."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from container_lifecycle_composition import (  # noqa: E402
    ContainerLifecycleCompositionError,
    _digest,
    coordinate_container_lifecycle,
)
from workflow_run_support import _canonical_digest, _proposal, _validate_common  # noqa: E402


def _admission(atom_id: str, path: str, digest: str, requested: str = "Archived") -> dict[str, object]:
    prior = {"atom_id": atom_id, "path": path, "version": 1, "digest": digest,
             "content_role": "Plan", "type": "Plan", "status": "Active"}
    return {"operation": "change_status", "prior": prior, "requested_status": requested,
            "current_status": "Active", "status_model": {"statuses": ["Active", requested]},
            "archive": requested == "Archived"}


def _fixture(*, count: int = 1) -> tuple[dict[str, object], dict[str, object]]:
    parent = _admission("CA-P-ROOT", "root.md", "a" * 64)
    descendants: list[dict[str, object]] = []
    for index in range(count):
        atom_id = f"CA-P-CHILD-{index}"
        digest = chr(ord("b") + index) * 64
        admission = _admission(atom_id, f"child-{index}.md", digest)
        descendants.append({
            "target": {"atom_id": atom_id, "path": f"child-{index}.md", "version": 1,
                       "sha256": digest, "content_role": "Plan", "atom_type": "Plan",
                       "status": "Active", "parent_atom_id": "CA-P-ROOT"},
            "status": "Archived", "admission": admission,
        })
    seal = {"parent": parent, "descendants": descendants}
    parameters = {"target": parent["prior"], "status": "Archived"}
    source = {"selected_source_registry_ref": "registry.json", "selected_source_registry_version": 1,
              "selected_source_registry_digest": "c" * 64, "selected_binding_ref": "binding.json",
              "selected_binding_digest": "d" * 64}
    execution: dict[str, object] = {
        "mode": "execute", "operation_route": "change_atom_status", "request_id": "coord-request",
        "parameters": parameters, "parameters_digest": _digest(parameters), "target_frontier": ["root.md"],
        "target_frontier_digest": _digest(["root.md"]), "effects": [{"type": "carrier"}],
        "effects_digest": _digest([{"type": "carrier"}]),
        "definition_manifest": {"manifest_ref": "manifest.json", "manifest_digest": "e" * 64},
        "source_freshness": source,
        "initiative": {"initiative_id": "initiative", "instruction_summary": "summary", "initiative_ref": "input.md"},
        "assigned_action_id": "CA-O-030", "operator_authorization": {
            "authorization_ref": "auth.json", "authorization_freshness": {"state": "current", "digest": "f" * 64},
        },
        "requested_runs": [
            {"requested_run_id": "coord", "kind": "workflow", "definition": {"atom_id": "W", "version": 1, "path": "workflow.md", "digest": "1" * 64}},
            {"requested_run_id": "coord:step", "kind": "step", "definition": {"atom_id": "S", "version": 1, "path": "step.md", "digest": "2" * 64}, "parent_requested_run_id": "coord"},
            {"requested_run_id": "coord:action", "kind": "action", "definition": {"atom_id": "A", "version": 1, "path": "action.md", "digest": "3" * 64}, "parent_requested_run_id": "coord:step"},
        ],
    }
    graph = {
        "route": "change_atom_status",
        "workflow": {"atom_id": "CA-O-127", "version": 1, "path": "workflow.md", "sha256": "1" * 64},
        "steps": [{"atom_id": "S", "version": 1, "path": "step.md", "sha256": "2" * 64,
                   "actions": [{"atom_id": "A", "version": 1, "path": "action.md", "sha256": "3" * 64}]}],
    }
    preview = {key: value for key, value in execution.items() if key not in {
        "proposal_receipt", "proposal_receipt_digest", "assigned_action_id",
        "operator_authorization", "requested_runs",
    }}
    preview["mode"] = "preview"
    execution["proposal_receipt"] = _proposal(preview, {"selected": True, "current": True,
        "observed": {"manifest_ref": "manifest.json", "manifest_digest": "e" * 64,
                     "lifecycle_admission": parent, "container_lifecycle": seal}})
    execution["proposal_receipt_digest"] = _canonical_digest(execution["proposal_receipt"])
    execution["operator_authorization"].update({
        "request_id": execution["request_id"], "operation_route": execution["operation_route"],
        "proposal_receipt_digest": execution["proposal_receipt_digest"],
        "parameters_digest": execution["parameters_digest"],
        "target_frontier_digest": execution["target_frontier_digest"],
        "effects_digest": execution["effects_digest"], "definition_manifest": execution["definition_manifest"],
        "source_freshness": execution["source_freshness"],
    })
    return {"request": {"run_id": "coord", "execution": execution}, "graph": graph,
            "lifecycle_admission": parent}, seal


class FakeTracker:
    def __init__(self, selected: "FakeSelected") -> None:
        self.selected = selected

    def _observe(self, request: dict[str, object]) -> dict[str, object]:
        target = request["parameters"]["target"]
        admission = self.selected.admissions[target["atom_id"]]
        return {"selected": True, "current": True, "observed": {
            "manifest_ref": "manifest.json", "manifest_digest": "e" * 64,
            "lifecycle_admission": admission,
        }}

    def run_selected_operation(self, request: dict[str, object]) -> dict[str, object]:
        parsed = _validate_common(request)
        proposal = _proposal(parsed, self._observe(parsed))
        return {"disposition": "preview", "proposal_receipt": proposal,
                "proposal_receipt_digest": _canonical_digest(proposal)}

    @staticmethod
    def _validate_execute(request: dict[str, object], proposal: dict[str, object], digest: str) -> None:
        if request["proposal_receipt"] != proposal or request["proposal_receipt_digest"] != digest:
            raise AssertionError("execute binding differs from preview")


class FakeSelected:
    def __init__(self, root: Path, seal: dict[str, object], outcomes: list[str] | None = None,
                 *, effects_on_failure: bool = False) -> None:
        self.root = root
        self.seal = seal
        self.admissions = {seal["parent"]["prior"]["atom_id"]: seal["parent"]}
        self.admissions.update({row["target"]["atom_id"]: row["admission"] for row in seal["descendants"]})
        self.outcomes = outcomes or []
        self.effects_on_failure = effects_on_failure
        self.frozen: list[dict[str, object]] = []
        self.dispatched: list[str] = []

    def run_directory(self, run_id: str) -> Path:
        return self.root / "runs" / run_id

    def _read(self, path: Path) -> dict[str, object]:
        return json.loads(path.read_text(encoding="utf-8"))

    @staticmethod
    def _write(path: Path, value: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")

    def persist_root(self, frozen: dict[str, object]) -> None:
        self._write(self.run_directory("coord") / "selected_request.json", frozen)

    def _revalidate(self, frozen: dict[str, object]) -> dict[str, str]:
        return frozen["graph"]

    def _validate_lifecycle_admission(self, graph: object, execution: object, *, expected_admission: object) -> object:
        return expected_admission

    def _shared_tracker(self, frozen: dict[str, object]) -> FakeTracker:
        return FakeTracker(self)

    def freeze(self, request: dict[str, object]) -> dict[str, object]:
        self.frozen.append(deepcopy(request))
        frozen = {"request": request, "graph": request.get("graph", {"route": "change_atom_status"}),
                  "lifecycle_admission": request["execution"]["proposal_receipt"]["source_freshness"]["observed"]["lifecycle_admission"]}
        self._write(self.run_directory(request["run_id"]) / "selected_request.json", frozen)
        return frozen

    def dispatch(self, frozen: dict[str, object]) -> dict[str, object]:
        run_id = frozen["request"]["run_id"]
        self.dispatched.append(run_id)
        outcome = self.outcomes[len(self.dispatched) - 1] if len(self.dispatched) <= len(self.outcomes) else "completed"
        effect_refs = [f"effect/{run_id}"] if outcome == "completed" or self.effects_on_failure else []
        return {"run_ids": [run_id], "terminal_runs": [{"run_id": run_id, "disposition": "terminal", "outcome": outcome,
                                    "effect_refs": effect_refs}]}


class ContainerLifecycleCompositionTests(unittest.TestCase):
    def test_descendant_first_ordinary_runs_and_marked_aggregate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            frozen, seal = _fixture(count=2)
            original = deepcopy(frozen)
            selected = FakeSelected(Path(directory), seal)
            selected.persist_root(frozen)
            with patch("container_lifecycle_composition._seal_contained_status_changes", return_value=seal):
                result = coordinate_container_lifecycle(selected, frozen)
            self.assertEqual({"result": result}, selected._read(selected.run_directory("coord") / "accepted.json"))
            self.assertEqual(["CA-P-CHILD-0", "CA-P-CHILD-1", "CA-P-ROOT"], [row["atom_id"] for row in result["members"]])
            self.assertEqual(result["completed"], selected.dispatched)
            self.assertEqual(result["parent_run_id"], result["members"][-1]["actual_run_id"])
            self.assertEqual("container-lifecycle/v1", result["schema"])
            self.assertFalse(result["original_requested_root_run_started"])
            self.assertNotIn("terminal_runs", result)
            self.assertNotIn("rootworkflow_run_id", result)
            self.assertEqual(original, frozen)
            self.assertNotIn("coord", selected.dispatched)
            self.assertTrue(all(row["actual_run_id"] == row["requested_run_id"] for row in result["members"]))
            for request in selected.frozen:
                self.assertNotIn("container_lifecycle", request["execution"]["proposal_receipt"]["source_freshness"]["observed"])
                self.assertEqual([request["execution"]["parameters"]["target"]["path"]], request["execution"]["target_frontier"])

    def test_stops_on_failure_and_retains_untouched_frontier(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            frozen, seal = _fixture(count=2)
            selected = FakeSelected(Path(directory), seal, outcomes=["completed", "failed"], effects_on_failure=True)
            selected.persist_root(frozen)
            with patch("container_lifecycle_composition._seal_contained_status_changes", return_value=seal):
                result = coordinate_container_lifecycle(selected, frozen)
            self.assertEqual("partial", result["outcome"])
            self.assertEqual("terminal", result["disposition"])
            self.assertEqual(result["failed"]["requested_run_id"], selected.dispatched[-1])
            self.assertTrue(result["failed"]["actual_run_id"])
            self.assertEqual([result["members"][-1]["requested_run_id"]], result["untouched"])
            self.assertEqual(2, len(selected.dispatched))
            progress = selected._read(selected.run_directory("coord") / "container_lifecycle_progress.json")
            self.assertEqual("dispatching", progress["state"])

    def test_retained_dispatching_frontier_never_replays(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            frozen, seal = _fixture()
            selected = FakeSelected(Path(directory), seal)
            selected.persist_root(frozen)
            member_request = {"run_id": "member", "execution": {}}
            selected._write(selected.run_directory("member") / "selected_request.json", member_request)
            retained = {"schema": "container-lifecycle/v1", "coordinator_id": "coord", "parent_run_id": None,
                        "original_requested_root_run_started": False, "members": [], "completed": [], "failed": None,
                        "untouched": ["member"], "effect_refs": [], "outcome": "interrupted_pending", "disposition": "started"}
            selected._write(selected.run_directory("coord") / "container_lifecycle_progress.json",
                            {"state": "dispatching", "root_frozen_digest": _digest(frozen),
                             "member_request_digest": _digest(member_request), "aggregate": retained, "current": "member"})
            result = coordinate_container_lifecycle(selected, frozen)
            self.assertEqual(retained, result)
            self.assertEqual([], selected.dispatched)

    def test_changed_seal_refuses_before_freezing_any_member(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            frozen, seal = _fixture()
            changed = deepcopy(seal)
            changed["descendants"][0]["status"] = "Done"
            selected = FakeSelected(Path(directory), seal)
            selected.persist_root(frozen)
            with patch("container_lifecycle_composition._seal_contained_status_changes", return_value=changed):
                with self.assertRaises(ContainerLifecycleCompositionError):
                    coordinate_container_lifecycle(selected, frozen)
            self.assertEqual([], selected.frozen)
            self.assertEqual([], selected.dispatched)

    def test_new_descendant_after_first_effect_stops_before_parent(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            frozen, seal = _fixture()
            injected = deepcopy(seal)
            injected["descendants"].append({
                "target": {"atom_id": "CA-P-INJECTED", "path": "injected.md", "version": 1,
                           "sha256": "9" * 64, "content_role": "Plan", "atom_type": "Plan",
                           "status": "Active", "parent_atom_id": "CA-P-ROOT"},
                "status": "Archived", "admission": _admission("CA-P-INJECTED", "injected.md", "9" * 64),
            })
            selected = FakeSelected(Path(directory), seal)
            selected.persist_root(frozen)
            with patch("container_lifecycle_composition._seal_contained_status_changes",
                       side_effect=[seal, seal, injected]):
                result = coordinate_container_lifecycle(selected, frozen)
            self.assertEqual([result["members"][0]["requested_run_id"]], selected.dispatched)
            self.assertEqual("completed", result["members"][0]["outcome"])
            self.assertEqual("blocked", result["members"][1]["outcome"])
            self.assertIsNone(result["members"][1].get("actual_run_id"))
            self.assertEqual("partial", result["outcome"])
            self.assertEqual("terminal", result["disposition"])


if __name__ == "__main__":
    unittest.main()
