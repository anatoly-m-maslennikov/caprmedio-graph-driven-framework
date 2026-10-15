"""Historical Active bytes are not current sources; current duplicates still fail."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_graph_fact_context as fixture_support  # noqa: E402

graph_builder = fixture_support.graph_builder
graph_fact_context = fixture_support.graph_fact_context


class ActiveSourceHistoryExclusionTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture_support.GraphFactContextTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)

    def test_exact_active_predecessor_is_excluded_in_both_history_directory_names(self):
        original = self.fixture.source.read_bytes()
        self.assertIn(b"status: Active\n", original)
        for name in ("archive", "archived"):
            folder = self.fixture.selected / name
            folder.mkdir()
            (folder / "CA-R-001@1.md").write_bytes(original)
        carriers, diagnostics = graph_builder.discover_atoms(
            self.fixture.repository, self.fixture.selected
        )
        self.assertEqual([], diagnostics)
        self.assertEqual(["CA-R-001"], [carrier.atom_id for carrier in carriers])
        frontier = graph_builder.source_frontier_for(self.fixture.repository, self.fixture.selected)
        self.assertEqual(1, len(frontier["carriers"]))
        self.assertEqual(original, self.fixture.source.read_bytes())

    def test_genuine_current_duplicate_remains_refused(self):
        duplicate = self.fixture.selected / "CA-R-001-copy.md"
        duplicate.write_bytes(self.fixture.source.read_bytes())
        carriers, diagnostics = graph_builder.discover_atoms(
            self.fixture.repository, self.fixture.selected
        )
        self.assertEqual([], diagnostics)
        self.assertEqual(2, len(carriers))
        with self.assertRaises(graph_fact_context.FactContextError) as failure:
            graph_fact_context._pool(self.fixture.repository, carriers)
        self.assertEqual("context-carrier-duplicate", failure.exception.code)


if __name__ == "__main__":
    unittest.main()
