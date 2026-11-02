"""Focused runtime checks for declaration-derived Project graph state."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


TESTS = Path(__file__).resolve().parent
if str(TESTS) not in sys.path:
    sys.path.insert(0, str(TESTS))

from test_declaration_graph_independent import DeclarationGraphIndependentTests, graph


class GenerateProjectGraphStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = DeclarationGraphIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_persistent_carriers_remain_under_the_single_control_root(self) -> None:
        self.assertEqual(self.fixture.control / "_projection", graph.OUTPUT.parent)
        self.assertEqual(self.fixture.control / "_projection", graph.SOURCE_MAP.parent)
        self.assertEqual(self.fixture.control / "_journal", graph.JOURNAL)

    def test_current_declaration_rows_keep_order_only_for_ordered_units(self) -> None:
        rows = {row["scope_unit_name"]: row for row in self.fixture.rows()}
        self.assertEqual(1, rows["FRAMEWORK"]["local_order"])
        self.assertIsNone(rows["PROGRAMMATIC"]["local_order"])
        self.assertIsNone(rows["TOOLS"]["local_order"])
        scope_id = rows["FRAMEWORK"]["scope_unit_id"]
        self.assertTrue(rows["FRAMEWORK"]["authority_path"].split("/")[-1].startswith(scope_id))
        self.assertFalse(rows["TOOLS"]["delivery_path"].split("/")[-1].startswith(rows["TOOLS"]["scope_unit_id"]))

    def test_unmaterialized_declared_scope_does_not_create_a_folder(self) -> None:
        rows = self.fixture.rows()
        tools = next(row for row in rows if row["scope_unit_name"] == "TOOLS")
        authority = self.fixture.root / tools["authority_path"]
        self.assertFalse(authority.is_dir())
        observations = graph.directory_observations(self.fixture.control, self.fixture.root, rows)
        observed = next(item for item in observations if item["authority_path"] == tools["authority_path"])
        self.assertEqual("declared", observed["kind"])
        self.assertFalse(observed["authority_materialized"])


if __name__ == "__main__":
    unittest.main()
