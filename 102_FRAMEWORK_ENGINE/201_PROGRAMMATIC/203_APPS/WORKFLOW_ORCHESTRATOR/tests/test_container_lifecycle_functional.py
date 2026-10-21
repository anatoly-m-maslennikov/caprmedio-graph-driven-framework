"""Native functional acceptance for source-sealed container lifecycle Runs.

Each case uses only the checked-in frozen source closure and a disposable
Project.  The coordinator is admitted through shared preview support; member
Runs are then dispatched through the native provider boundary.
"""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import re
import sys
import unittest


APP = Path(__file__).resolve().parents[1]
PROGRAMMATIC = APP.parents[1]
TOOLS = PROGRAMMATIC / "201_TOOLS"
MCP = PROGRAMMATIC / "204_MCP"
for location in (APP / "tests", APP, TOOLS, MCP):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from container_lifecycle_composition import ContainerLifecycleCompositionError  # noqa: E402
from container_lifecycle_fixture import ContainerLifecycleFixture  # noqa: E402
from selected_execution import SelectedExecution, build_requested_runs  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402
from selected_routes import _QueueBackedSelectedSupport  # noqa: E402
from workflow_run_support import _canonical_digest  # noqa: E402


def _plan_bytes(atom_id: str, *, status: str = "Active", parent: str | None = None) -> bytes:
    return ContainerLifecycleFixture.plan_carrier_bytes(atom_id, status=status, parent=parent)


def _write_plan(path: Path, atom_id: str, *, status: str = "Active", parent: str | None = None) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(_plan_bytes(atom_id, status=status, parent=parent))
    return path


def _metadata(path: Path) -> tuple[str, int]:
    text = path.read_text(encoding="utf-8")
    status = re.search(r"(?m)^status:\s*([^\n#]+)", text)
    version = re.search(r"(?m)^version:\s*([0-9]+)", text)
    if status is None or version is None:
        raise AssertionError(f"carrier metadata is incomplete: {path}")
    return status.group(1).strip(), int(version.group(1))


def _journal_events(root: Path, request_id: str | None = None) -> list[dict[str, object]]:
    journal = root / ".caprmedio_caprmedio" / "_journal"
    events = [
        json.loads(line)
        for path in sorted(journal.rglob("*.ndjson"))
        for line in path.read_text(encoding="utf-8").splitlines()
        if line
    ]
    if request_id is None:
        return events
    return [event for event in events if event.get("llm_session", {}).get("uuid") == request_id]


def _authority_snapshot(root: Path) -> dict[str, bytes]:
    base = root / ".caprmedio_caprmedio" / "fixture"
    return {
        path.relative_to(root).as_posix(): path.read_bytes()
        for path in sorted(base.rglob("*"))
        if path.is_file()
    }


class ContainerLifecycleFunctionalTests(unittest.TestCase):
    """Exercise the full preview -> freeze -> native dispatch boundary."""

    def fixture(self) -> ContainerLifecycleFixture:
        fixture = ContainerLifecycleFixture()
        try:
            fixture.prepare()
        except BaseException:
            fixture.close()
            raise
        self.addCleanup(fixture.close)
        return fixture

    def request(
        self, fixture: ContainerLifecycleFixture, run_id: str, status: str,
        *, target: Path | None = None,
    ) -> tuple[SelectedExecution, dict[str, object]]:
        parameters = fixture.status_parameters(target=target)
        parameters["status"] = status
        manifest = {
            "manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
            "manifest_digest": fixture.manifest["canonical_manifest_sha256"],
        }
        frontier = [parameters["target"]["path"]]
        effects = [{"type": "change_atom_status", "target": frontier[0], "status": status}]
        preview_request: dict[str, object] = {
            "mode": "preview",
            "operation_route": "change_atom_status",
            "request_id": f"{run_id}-request",
            "parameters": parameters,
            "parameters_digest": _canonical_digest(parameters),
            "target_frontier": frontier,
            "target_frontier_digest": _canonical_digest(frontier),
            "effects": effects,
            "effects_digest": _canonical_digest(effects),
            "definition_manifest": manifest,
            "source_freshness": dict(fixture.manifest["source_freshness"]),
            "initiative": {
                "initiative_id": f"functional-{run_id}",
                "instruction_summary": "Native container lifecycle functional acceptance",
                "initiative_ref": "fixture/container-lifecycle-input.json",
            },
        }
        support = _QueueBackedSelectedSupport(fixture.root, None)
        preview = support._tracker().run_selected_operation(preview_request)
        self.assertEqual("preview", preview.get("disposition"), preview)
        observed = preview["proposal_receipt"]["source_freshness"]["observed"]
        self.assertIn("container_lifecycle", observed)

        selected = SelectedExecution(fixture.root)
        graph = selected._validate_graph({**preview_request, "mode": "execute"})
        requested_runs = build_requested_runs(graph, run_id)
        execution = {
            **preview_request,
            "mode": "execute",
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": "CA-O-029",
            "requested_runs": requested_runs,
        }
        execution["operator_authorization"] = {
            "authorization_ref": "fixture/operator-authorization.json",
            "authorization_freshness": {"state": "current", "digest": "a" * 64},
            "request_id": execution["request_id"],
            "operation_route": execution["operation_route"],
            "proposal_receipt_digest": execution["proposal_receipt_digest"],
            "parameters_digest": execution["parameters_digest"],
            "target_frontier_digest": execution["target_frontier_digest"],
            "effects_digest": execution["effects_digest"],
            "definition_manifest": execution["definition_manifest"],
            "source_freshness": execution["source_freshness"],
        }
        frozen = selected.freeze({"operation": "enqueue_selected", "run_id": run_id, "execution": execution})
        self.assertEqual(
            observed["container_lifecycle"],
            frozen["request"]["execution"]["proposal_receipt"]["source_freshness"]["observed"]["container_lifecycle"],
        )
        return selected, frozen

    def dispatch(self, fixture: ContainerLifecycleFixture, run_id: str) -> dict[str, object]:
        return SelectedNativeProviders(fixture.root).dispatch(run_id)

    def assert_real_member_runs(
        self, fixture: ContainerLifecycleFixture, result: dict[str, object], coordinator_id: str,
    ) -> None:
        members = result.get("members")
        self.assertIsInstance(members, list)
        self.assertNotIn("terminal_runs", result)
        self.assertFalse(result.get("original_requested_root_run_started"))
        self.assertNotEqual(coordinator_id, result.get("parent_run_id"))
        actual_ids: list[str] = []
        for member in members:
            self.assertIsInstance(member, dict)
            actual = member.get("actual_run_id")
            requested = member.get("requested_run_id")
            self.assertIsInstance(actual, str)
            self.assertIsInstance(requested, str)
            self.assertEqual(actual, requested)
            self.assertNotEqual(actual, coordinator_id)
            actual_ids.append(actual)
            workflow_events = [
                event for event in _journal_events(fixture.root, f"{requested}-request")
                if event.get("run", {}).get("kind") == "workflow"
            ]
            self.assertEqual({actual}, {event["run"]["run_id"] for event in workflow_events})
        self.assertEqual(result.get("parent_run_id"), actual_ids[-1])
        self.assertEqual(actual_ids, [member.get("actual_run_id") for member in members])
        self.assertEqual([], _journal_events(fixture.root, f"{coordinator_id}-request"))

    def test_archive_is_deepest_first_flat_and_preserves_exact_history(self) -> None:
        fixture = self.fixture()
        grandchild = _write_plan(
            fixture.child_plan.with_suffix("") / "done" / "03-CA-P-703-TASK--grandchild.md",
            "CA-P-703", status="Done", parent="CA-P-702",
        )
        original = {path: path.read_bytes() for path in (fixture.parent_plan, fixture.child_plan, grandchild)}
        _selected, frozen = self.request(fixture, "functional-archive", "Archived")
        result = self.dispatch(fixture, "functional-archive")

        self.assertEqual("container-lifecycle/v1", result["schema"])
        self.assertEqual("completed", result["outcome"])
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(["CA-P-703", "CA-P-702", "CA-P-701"], [row["atom_id"] for row in result["members"]])
        self.assertEqual(["Archived"] * 3, [row["requested_status"] for row in result["members"]])
        self.assertEqual(3, len(result["completed"]))
        self.assertIsNone(result["failed"])
        self.assert_real_member_runs(fixture, result, "functional-archive")

        archive = fixture.parent_plan.parent / "archived"
        for source, raw in original.items():
            history = archive / f"{source.stem}@1.md"
            current = archive / f"{source.stem}@2.md"
            self.assertEqual(raw, history.read_bytes(), source)
            self.assertEqual(("Archived", 2), _metadata(current))
            self.assertFalse(source.exists(), source)
            self.assertTrue(current.parent == archive)

    def test_done_cancels_active_descendants_and_keeps_done_noop(self) -> None:
        fixture = self.fixture()
        active = _write_plan(
            fixture.parent_plan.with_suffix("") / "03-CA-P-703-TASK--active.md",
            "CA-P-703", parent="CA-P-701",
        )
        done = _write_plan(
            fixture.parent_plan.with_suffix("") / "done" / "04-CA-P-704-TASK--done.md",
            "CA-P-704", status="Done", parent="CA-P-701",
        )
        original_active = {
            fixture.child_plan: fixture.child_plan.read_bytes(),
            active: active.read_bytes(),
        }
        original_done = done.read_bytes()
        _selected, frozen = self.request(fixture, "functional-done", "Done")
        result = self.dispatch(fixture, "functional-done")

        self.assertEqual("completed", result["outcome"])
        self.assertEqual(["CA-P-702", "CA-P-703", "CA-P-704", "CA-P-701"], [row["atom_id"] for row in result["members"]])
        self.assertEqual(["Canceled", "Canceled", "Done", "Done"], [row["requested_status"] for row in result["members"]])
        self.assertEqual([], next(row for row in result["members"] if row["atom_id"] == "CA-P-704")["effect_refs"])
        self.assert_real_member_runs(fixture, result, "functional-done")

        plan_root = fixture.parent_plan.parent
        done_child = plan_root / "done" / fixture.parent_plan.stem / "done" / done.name
        self.assertEqual(original_done, done_child.read_bytes())
        self.assertEqual(("Done", 1), _metadata(done_child))
        self.assertFalse((plan_root / "archived" / f"{done.stem}@1.md").exists())
        for source, raw in original_active.items():
            canceled = plan_root / "done" / fixture.parent_plan.stem / "canceled" / source.name
            self.assertEqual(("Canceled", 2), _metadata(canceled))
            self.assertFalse(source.exists())
            self.assertEqual(raw, (plan_root / "archived" / f"{source.stem}@1.md").read_bytes())
        parent_done = plan_root / "done" / fixture.parent_plan.name
        self.assertEqual(("Done", 2), _metadata(parent_done))
        self.assertTrue((plan_root / "archived" / f"{fixture.parent_plan.stem}@1.md").is_file())

    def test_root_auth_tamper_stops_before_member_dispatch(self) -> None:
        fixture = self.fixture()
        selected, frozen = self.request(fixture, "functional-auth", "Archived")
        tampered = deepcopy(frozen)
        tampered["request"]["execution"]["operator_authorization"]["request_id"] = "forged-request"
        selected._write(selected.run_directory("functional-auth") / "selected_request.json", tampered)
        before = _authority_snapshot(fixture.root)

        with self.assertRaisesRegex((ValueError, ContainerLifecycleCompositionError), "authorization|operator"):
            self.dispatch(fixture, "functional-auth")
        self.assertEqual(before, _authority_snapshot(fixture.root))
        self.assertEqual([], _journal_events(fixture.root))

    def test_source_mutation_after_freeze_stops_before_any_member_effect(self) -> None:
        fixture = self.fixture()
        _selected, frozen = self.request(fixture, "functional-stale", "Archived")
        fixture.child_plan.write_bytes(fixture.child_plan.read_bytes() + b"\n<!-- stale fixture -->\n")
        before = _authority_snapshot(fixture.root)

        try:
            result = self.dispatch(fixture, "functional-stale")
        except ContainerLifecycleCompositionError:
            result = None
        if result is not None:
            self.assertIn(result.get("outcome"), {"blocked", "interrupted_pending"})
            self.assertEqual([], result.get("completed", []))
            self.assertEqual([], result.get("effect_refs", []))
        self.assertEqual(before, _authority_snapshot(fixture.root))
        self.assertEqual([], _journal_events(fixture.root))

    def test_duplicate_dispatch_reuses_accepted_aggregate_without_replay(self) -> None:
        fixture = self.fixture()
        _selected, frozen = self.request(fixture, "functional-duplicate", "Archived")
        first = self.dispatch(fixture, "functional-duplicate")
        self.assertEqual("completed", first["outcome"])
        authority = _authority_snapshot(fixture.root)
        events = _journal_events(fixture.root)

        second = self.dispatch(fixture, "functional-duplicate")
        self.assertEqual(first, second)
        self.assertEqual(authority, _authority_snapshot(fixture.root))
        self.assertEqual(events, _journal_events(fixture.root))


if __name__ == "__main__":
    unittest.main()
