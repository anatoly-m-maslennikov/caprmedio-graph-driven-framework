# CA-E-799@3
# CA-E-800@3
"""Small invariant gates for resource-soak metric helpers."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).parent))

from workbench_soak_metrics import CgroupSnapshot, assert_inventory, plateau


class SoakMetricTests(unittest.TestCase):
    def test_plateau_rejects_growth(self) -> None:
        with self.assertRaisesRegex(AssertionError, "plateau"):
            plateau([CgroupSnapshot(1, 10, 10, 0), CgroupSnapshot(2, 21, 21, 0)], 10)

    def test_falling_memory_does_not_count_as_growth(self) -> None:
        result = plateau([CgroupSnapshot(1, 100, 100, 0), CgroupSnapshot(2, 10, 100, 0)], 10)
        self.assertEqual(0, result["growth_bytes"])
        self.assertEqual(90, result["spread_bytes"])

    def test_inventory_rejects_orphan_table_and_empty_relation_key(self) -> None:
        inventory = {"result_tables": ["query_current", "query_orphan"], "result_ids": ["current"],
                     "pinned_result_ids": [], "open_view_result_ids": [], "source_cache": {},
                     "relation_state": {"empty_outgoing_keys": ["Atom:CA-R-1"]}}
        with self.assertRaisesRegex(AssertionError, "result tables"):
            assert_inventory(inventory)
        inventory["result_tables"] = ["query_current"]
        with self.assertRaisesRegex(AssertionError, "empty outgoing"):
            assert_inventory(inventory)


if __name__ == "__main__":
    unittest.main()
