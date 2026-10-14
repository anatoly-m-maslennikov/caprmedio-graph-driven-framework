"""Native W11/W12 graph corpus proof in disposable Project authority."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
ROOT = APP.parents[3]
GRAPH_ROOT = APP.parents[1] / "201_TOOLS" / "GENERATE_ENTITY_GRAPH"
if str(GRAPH_ROOT) not in sys.path:
    sys.path.insert(0, str(GRAPH_ROOT))
if str(Path(__file__).resolve().parent) not in sys.path:
    sys.path.insert(0, str(Path(__file__).resolve().parent))

import generate_entity_graph  # noqa: E402
from selected_workflows_docker_fixture import FixtureLease, GoldenCase, GoldenProject  # noqa: E402


class SelectedGraphGoldenInputsTest(unittest.TestCase):
    """W11/W12 invoke their actual Action adapters, not fixture markers."""

    def _fixture(self, case_id: str, route: str) -> tuple[FixtureLease, GoldenProject]:
        parent = ROOT / ".caprmedio_tmp" / "tests" / "selected-graph-golden-inputs"
        parent.mkdir(parents=True, exist_ok=True)
        root = Path(tempfile.mkdtemp(dir=parent))
        fixture = GoldenProject(ROOT, root, GoldenCase(case_id, route))
        fixture.prepare()
        return FixtureLease(root), fixture

    @staticmethod
    def _native_graph_request(fixture: GoldenProject) -> dict[str, object]:
        """Direct Tool proof needs the same non-caller recording capability.

        Selected execution binds this from actual Run state, not a Journal
        receipt; this native fixture uses the same structural constructor.
        """

        request = fixture.native_parameters()
        route = next(row for row in fixture.manifest["routes"] if row["route"] == fixture.case.route)
        action = route["ordered_actions"][0]
        request["run_recording_context"] = generate_entity_graph.actual_run_recording_context(
            "golden-workflow", "golden-step", "golden-action",
            {
                "run_id": "golden-action", "kind": "action", "parent_run_id": "golden-step",
                "definition": {"atom_id": action["atom_id"], "version": action["version"]},
            },
        )
        return request

    def test_w11_w12_reject_malformed_or_stale_source_inputs_without_effects(self) -> None:
        for case_id, route, adapter in (
            ("W11", "build_entities_graph", generate_entity_graph.construct_entities_graph_projection),
            ("W12", "build_terms_graph", generate_entity_graph.construct_terms_graph_projection),
        ):
            with self.subTest(case=case_id, condition="malformed"):
                lease, fixture = self._fixture(case_id, route)
                try:
                    malformed = self._native_graph_request(fixture)
                    malformed["selection"] = {"atom_ids": "CA-R-201"}
                    result = adapter(fixture.root, malformed)
                    self.assertEqual("failed", result["outcome"], result)
                    self.assertEqual([], result["output_effects"]["paths"])
                finally:
                    lease.cleanup()
            with self.subTest(case=case_id, condition="stale"):
                lease, fixture = self._fixture(case_id, route)
                try:
                    request = self._native_graph_request(fixture)
                    source = fixture.graph_source_dir / "CA-R-201.md"
                    source.write_text(source.read_text(encoding="utf-8") + "\nChanged after frontier.\n", encoding="utf-8")
                    result = adapter(fixture.root, request)
                    self.assertEqual("stale", result["outcome"], result)
                    self.assertEqual([], result["output_effects"]["paths"])
                finally:
                    lease.cleanup()


if __name__ == "__main__":
    unittest.main()
