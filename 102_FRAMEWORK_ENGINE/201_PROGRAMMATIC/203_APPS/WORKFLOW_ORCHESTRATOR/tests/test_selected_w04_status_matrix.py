"""Complete W04 selected execution matrix; Docker retains transport representatives."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
from typing import Any
import unittest


TESTS = Path(__file__).resolve().parent
APP = TESTS.parent
PROGRAMMATIC = APP.parents[1]
for location in (TESTS, APP, PROGRAMMATIC / "201_TOOLS", PROGRAMMATIC / "204_MCP"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_selected_workflows_docker_e2e as docker_evidence  # noqa: E402
import selected_workflows_docker_fixture as corpus  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_routes import SelectedRouteAdapter  # noqa: E402


class SelectedW04StatusMatrixTests(unittest.TestCase):
    def setUp(self) -> None:
        # Composition reuses assertions, not the opt-in Docker TestCase collection.
        self.evidence = docker_evidence.SelectedWorkflowsDockerEndToEnd("runTest")

    def _fixture(self) -> tuple[corpus.FixtureLease, corpus.GoldenProject]:
        repository = APP.parents[3]
        parent = repository / ".caprmedio_tmp/tests/selected-w04-status-matrix"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        lease = corpus.FixtureLease(root)
        self.addCleanup(lease.cleanup)
        fixture = corpus.GoldenProject(
            repository, root, corpus.GoldenCase("W04", "change_atom_status")
        )
        fixture.prepare()
        return lease, fixture

    def _execute(
        self,
        fixture: corpus.GoldenProject,
        path: Path,
        status: str,
        request_id: str,
        *,
        expected_outcome: str = "completed",
    ) -> dict[str, Any]:
        root = fixture.root
        before = fixture.snapshot()
        records = self.evidence._recording_snapshot(root)
        preview = SelectedRouteAdapter(root).invoke(
            fixture.case.route,
            fixture.request_for_status(path, status, request_id=request_id),
        )
        self.assertEqual("preview", preview.get("disposition"), preview)
        self.assertEqual(before, fixture.snapshot(), "preview changed authority")
        self.assertEqual(records, self.evidence._recording_snapshot(root), "preview wrote records")
        execution = fixture.request_for_status(
            path,
            status,
            request_id=request_id,
            mode="execute",
            receipt=preview["proposal_receipt"],
            receipt_digest=preview["proposal_receipt_digest"],
        )
        runner = SelectedExecution(root)
        frozen = runner.freeze(
            {"operation": "enqueue_selected", "run_id": request_id, "execution": execution}
        )
        selected = runner.dispatch(frozen)
        self.assertEqual("terminal", selected.get("disposition"), selected)
        graph = self.evidence._graph_result(root, request_id)
        rows = self.evidence._assert_graph_path_and_native_results(
            root,
            fixture,
            request_id,
            graph,
            expected_outcome=expected_outcome,
        )
        self.evidence._assert_shared_run_journal(
            root,
            request_id,
            self.evidence._route_binding(fixture),
            selected,
            graph,
            expected_outcome=expected_outcome,
        )
        native = self.evidence._action_progress(root, request_id, rows[-1]["action_run_id"])[
            "native_result"
        ]
        if not isinstance(native, dict):
            self.fail(f"native Action result is not a mapping: {native}")
        return native

    def _assert_destination(
        self,
        fixture: corpus.GoldenProject,
        native: dict[str, Any],
        role: str,
        status: str,
        source_id: str,
        statuses: tuple[str, ...],
    ) -> Path:
        self.assertEqual("applied", native.get("outcome"), native)
        model = native["status_model"]
        self.assertEqual(list(statuses), model["statuses"], native)
        expected_source_ids = (
            ("CA-R-1947", "CA-R-1608") if role == "Concern"
            else ("CA-R-1947", "CA-R-1539") if role == "Plan"
            else (source_id,)
        )
        self.assertEqual(
            expected_source_ids,
            tuple(row["atom_id"] for row in model["model_sources"]),
            native,
        )
        pin = model["model_sources"][0]
        self.assertEqual(
            hashlib.sha256((fixture.root / pin["path"]).read_bytes()).hexdigest(), pin["sha256"]
        )
        observed: Path = fixture.root / native["observed"]["path"]
        self.assertTrue(observed.is_file(), native)
        self.assertEqual(status, native["observed"]["status"], native)
        if role == "Requirement" and status == "Draft":
            self.assertIsNone(native["observed"]["atom_id"], native)
            self.assertNotIn("atom_id:", observed.read_text(encoding="utf-8"), native)
            self.assertIn("history", native, native)
        return observed

    def _assert_noop(
        self, fixture: corpus.GoldenProject, path: Path, status: str, role: str
    ) -> None:
        before = fixture.snapshot()
        native = self._execute(
            fixture, path, status, f"p1616-{role.lower()}-noop", expected_outcome="no_op"
        )
        self.assertEqual("no-op", native.get("outcome"), native)
        self.assertTrue(
            all(effect.get("state") == "unchanged" for effect in native.get("effects", [])), native
        )
        self.assertEqual(before, fixture.snapshot(), "no-op changed authority/history")

    def _assert_refusal(self, fixture: corpus.GoldenProject, path: Path, role: str) -> None:
        before = fixture.snapshot()
        records = self.evidence._recording_snapshot(fixture.root)
        rejected = SelectedRouteAdapter(fixture.root).invoke(
            fixture.case.route,
            fixture.request_for_status(
                path, "NotAdmitted", request_id=f"p1616-{role.lower()}-rejected"
            ),
        )
        self.evidence._assert_status_admission_blocked(rejected)
        self.assertEqual(before, fixture.snapshot(), "rejected W04 request changed authority")
        self.assertEqual(
            records,
            self.evidence._recording_snapshot(fixture.root),
            "refusal wrote Journal or Run records",
        )

    def test_all_29_destinations_eight_noops_and_eight_refusals(self) -> None:
        applied = noops = refusals = 0
        for role, _letter, _folder, source_id, statuses in corpus.STATUS_DOMAINS:
            with self.subTest(role=role):
                lease, fixture = self._fixture()
                try:
                    for offset, status in enumerate(statuses):
                        current = next(
                            value
                            for value in statuses
                            if value != status and value.casefold() != "draft"
                        )
                        path = fixture.status_atom(role, current, number=8000 + offset)
                        native = self._execute(
                            fixture,
                            path,
                            status,
                            f"p1616-{role.lower()}-{status.casefold()}-change",
                        )
                        observed = self._assert_destination(
                            fixture, native, role, status, source_id, statuses
                        )
                        if role == "Requirement" and status == "Draft":
                            self._assert_noop(fixture, observed, "Draft", "requirement-draft")
                        applied += 1
                    self._assert_noop(fixture, observed, statuses[-1], role)
                    noops += 1
                    self._assert_refusal(fixture, observed, role)
                    refusals += 1
                finally:
                    lease.cleanup()
        self.assertEqual((29, 8, 8), (applied, noops, refusals))


if __name__ == "__main__":
    unittest.main()
