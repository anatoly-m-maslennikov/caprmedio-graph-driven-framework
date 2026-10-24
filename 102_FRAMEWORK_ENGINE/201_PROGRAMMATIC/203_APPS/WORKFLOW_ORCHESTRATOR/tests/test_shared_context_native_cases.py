"""Functional input cases for the current shared-context Workflow boundary."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
for location in (APP, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402


class SharedContextNativeCaseTests(unittest.TestCase):
    """Keep current packet gates explicit before native adapter execution exists."""

    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()

    def test_packet_keeps_full_m_projection_separate_from_selected_rde(self) -> None:
        packet = self.fixture.native_implementation_parameters()
        support = self.fixture.support_inventory
        required = {row["atom_id"]: row["version"] for row in support["required_authority"]}
        self.assertEqual({"CA-R-1843": 3, "CA-R-1845": 2, "CA-M-328": 2, "CA-D-544": 3}, required)
        self.assertEqual(39, len(packet["base_packet"]["method_projection"]["sources"]))
        self.assertEqual(15, len(packet["base_packet"]["evaluations"]))
        self.assertIn("not the full Project R/E/D universe", support["applicable_rde"]["selection"])
        self.assertEqual(
            self.fixture.method_projection_content(),
            packet["base_packet"]["method_projection"]["content"],
        )
        for section in ("requirements", "delivery", "evaluations"):
            for row in packet["base_packet"][section]:
                raw = self.fixture.support_source_bytes(row["atom_id"])
                self.assertEqual(raw.decode("utf-8"), row["content"])
                self.assertEqual(hashlib.sha256(raw).hexdigest(), row["sha256"])
        self.assertTrue(self.fixture.packet_bindings_are_current(packet))
        self.assertNotIn(
            "CA-M-328", {row["atom_id"] for row in packet["base_packet"]["source_bindings"]}
        )

    def test_stale_current_source_case_changes_an_exact_bound_pin(self) -> None:
        parent = PROJECT_ROOT / ".caprmedio_tmp" / "shared-context-stale-source"
        parent.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=parent) as raw:
            project = self.fixture.materialize(Path(raw) / "project")
            pin = next(row for row in self.fixture.source_pins() if row["atom_id"] == "CA-O-231")
            target = project / str(pin["source_path"])
            target.write_bytes(target.read_bytes() + b"\n# stale fixture mutation\n")
            self.assertNotEqual(str(pin["sha256"]), hashlib.sha256(target.read_bytes()).hexdigest())

        stale_packet = self.fixture.packet_variant(stale_atom="CA-O-231")
        self.assertFalse(self.fixture.packet_bindings_are_current(stale_packet))

    def test_review_case_requires_explicit_phase_and_preserves_read_only_contract(self) -> None:
        packet = self.fixture.packet_variant(review_phase="preliminary")
        self.assertEqual("preliminary", packet["base_packet"]["review_phase"])
        source = self.fixture.source_bytes("CA-O-230").decode("utf-8")
        self.assertIn("explicit review_phase preliminary or final", source)
        self.assertIn("Read-only review never edits code", source)

    def test_candidate_change_invalidates_retained_preclearance(self) -> None:
        packet = self.fixture.packet_variant(review_phase="preliminary")
        packet["base_packet"]["retained_state"]["preliminary_review"] = {
            "candidate": "fixture-candidate-v1",
            "result": "preliminary_clear",
        }
        changed = self.fixture.packet_variant(candidate="fixture-candidate-v2")
        self.assertNotEqual(
            packet["base_packet"]["retained_state"]["preliminary_review"]["candidate"],
            changed["base_packet"]["candidate"],
        )

    def test_retry_zero_and_exhausted_inputs_remain_distinct(self) -> None:
        zero = self.fixture.packet_variant(retry_limit=0)
        exhausted = self.fixture.packet_variant(retry_limit=1, retry_consumed=1)
        self.assertEqual(
            (0, 0),
            (
                zero["base_packet"]["retry"]["consumed"],
                zero["base_packet"]["retry"]["effective_limit"],
            ),
        )
        self.assertEqual(
            (1, 1),
            (
                exhausted["base_packet"]["retry"]["consumed"],
                exhausted["base_packet"]["retry"]["effective_limit"],
            ),
        )

    def test_completed_workflow_has_no_implicit_release_handoff(self) -> None:
        graph = self.fixture.graph()
        terminals = {
            row["to"] for row in graph["transitions"] if row["to"] in {"completed", "blocked"}
        }
        self.assertEqual({"completed", "blocked"}, terminals)
        self.assertTrue(self.fixture.manifest["expected_boundary"]["no_execution_proof"])
        source = self.fixture.source_bytes("CA-O-016").decode("utf-8")
        self.assertIn("Start release as a separately admitted Workflow Run", source)
        self.assertNotIn('"release"', {row["to"] for row in graph["transitions"]})


if __name__ == "__main__":
    unittest.main()
