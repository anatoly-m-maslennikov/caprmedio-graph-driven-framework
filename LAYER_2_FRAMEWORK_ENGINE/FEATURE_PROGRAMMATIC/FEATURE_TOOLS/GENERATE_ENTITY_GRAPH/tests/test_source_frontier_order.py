"""Producer and verifier share POSIX path ordering, not Path component ordering."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_graph_fact_context as fixture_support  # noqa: E402

graph = fixture_support.graph_builder
facts = fixture_support.graph_fact_context


class SourceFrontierOrderTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture_support.GraphFactContextTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        folder = self.fixture.selected / self.fixture.source.stem
        folder.mkdir()
        self.child = folder / "CA-R-002.md"
        self.child.write_text(fixture_support.current_atom("CA-R-002", "Child **means** a child."))

    def checked_frontier(self):
        carriers, diagnostics = graph.discover_atoms(self.fixture.repository, self.fixture.selected)
        self.assertEqual([], diagnostics)
        frontier = graph.source_frontier_for(self.fixture.repository, self.fixture.selected)
        pool = facts._pool(self.fixture.repository, carriers)
        selection = facts._selection({"atom_ids": [], "scope_unit_names": []}, set(pool))
        return carriers, frontier, pool, selection

    def test_nested_same_stem_parent_and_child_roundtrip_in_posix_order(self):
        carriers, frontier, pool, selection = self.checked_frontier()
        paths = [carrier.carrier_path for carrier in carriers]
        self.assertEqual(sorted(paths), paths)
        self.assertEqual(["CA-R-001", "CA-R-002"], [carrier.atom_id for carrier in carriers])
        self.assertEqual(
            frontier, facts._frontier(self.fixture.repository, frontier, pool, selection)
        )
        self.assertEqual(
            facts._digest([pool[carrier.atom_id][1] for carrier in carriers]),
            frontier["source_frontier_sha256"],
        )

    def test_actual_child_byte_drift_still_refuses_saved_frontier(self):
        _carriers, frontier, pool, selection = self.checked_frontier()
        self.child.write_bytes(self.child.read_bytes() + b"\nActual child changed.\n")
        with self.assertRaises(facts.FactContextError) as failure:
            facts._frontier(self.fixture.repository, frontier, pool, selection)
        self.assertEqual("context-source-stale", failure.exception.code)


if __name__ == "__main__":
    unittest.main()
