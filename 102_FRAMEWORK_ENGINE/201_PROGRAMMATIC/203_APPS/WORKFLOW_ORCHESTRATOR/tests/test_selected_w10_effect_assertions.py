"""W10 logical references must resolve to real, approved rollback effects."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
import unittest


TESTS = Path(__file__).resolve().parent
APP = TESTS.parent
ROOT = APP.parents[3]
for location in (TESTS, APP, APP.parents[1] / "201_TOOLS", APP.parents[1] / "204_MCP"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import test_selected_workflows_docker_e2e as docker_evidence  # noqa: E402
import selected_workflows_docker_fixture as corpus  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402
from selected_routes import SelectedRouteAdapter  # noqa: E402


class SelectedW10EffectAssertions(unittest.TestCase):
    def setUp(self) -> None:
        parent = ROOT / ".caprmedio_tmp/tests/selected-w10-effect-assertions"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.fixture = corpus.GoldenProject(
            ROOT, self.root, corpus.GoldenCase("W10", "revert_changes")
        )
        self.fixture.prepare()
        self.evidence = docker_evidence.SelectedWorkflowsDockerEndToEnd("runTest")
        self.request_id = "w10-real-host-effect-assertions"
        preview = SelectedRouteAdapter(self.root).invoke(
            self.fixture.case.route, self.fixture.request(request_id=self.request_id)
        )
        self.assertEqual("preview", preview["disposition"], preview)
        execution = self.fixture.request(
            request_id=self.request_id,
            mode="execute",
            receipt=preview["proposal_receipt"],
            receipt_digest=preview["proposal_receipt_digest"],
        )
        runner = SelectedExecution(self.root)
        frozen = runner.freeze(
            {"operation": "enqueue_selected", "run_id": self.request_id, "execution": execution}
        )
        self.selected = SelectedNativeProviders(self.root).execution(frozen).dispatch(frozen)
        self.assertEqual("terminal", self.selected["disposition"], self.selected)
        self.graph = self.evidence._graph_result(self.root, self.request_id)
        self.native = self.evidence._w10_native_result(self.root, self.request_id, self.graph)
        self.references = self.graph["step_results"][0]["effect_refs"]

    def test_actual_host_effect_and_terminal_references_need_no_placeholder_files(self) -> None:
        rows = self.evidence._assert_graph_path_and_native_results(
            self.root, self.fixture, self.request_id, self.graph
        )
        self.evidence._assert_shared_run_journal(
            self.root,
            self.request_id,
            self.evidence._route_binding(self.fixture),
            self.selected,
            self.graph,
        )
        self.assertTrue(rows[0]["effect_refs"])
        self.assertFalse((self.root / self.references[0]).exists())
        self.assertEqual(
            "schema_version = 1\n",
            (self.root / ".caprmedio_caprmedio/rollback-structure.toml").read_text(),
        )

    def test_wrong_logical_effect_reference_is_rejected(self) -> None:
        with self.assertRaises(AssertionError):
            self.evidence._assert_w10_effect_refs(
                self.root, self.request_id, self.native, ["wrong/effect"]
            )

    def test_wrong_restored_hash_is_rejected(self) -> None:
        native = copy.deepcopy(self.native)
        native["effect_account"]["effects"][0]["receipt"]["native_result"]["restored"][0][
            "after_sha256"
        ] = "0" * 64
        with self.assertRaises(AssertionError):
            self.evidence._assert_w10_effect_refs(
                self.root, self.request_id, native, self.references
            )

    def test_actual_restored_member_drift_is_rejected(self) -> None:
        restored = self.root / ".caprmedio_caprmedio/rollback-structure.toml"
        restored.write_text("changed after reversal\n", encoding="utf-8")
        with self.assertRaises(AssertionError):
            self.evidence._assert_w10_effect_refs(
                self.root, self.request_id, self.native, self.references
            )


if __name__ == "__main__":
    unittest.main()
