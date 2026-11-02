"""Completion checks for the declaration-source graph serialization boundary."""

from __future__ import annotations

import copy
import sys
import unittest

import tomllib

from test_declaration_graph_independent import DeclarationGraphIndependentTests, graph


class DeclarationTaskCompletionIndependentTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = DeclarationGraphIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def test_graph_and_source_serializers_are_deterministic_and_read_only(self) -> None:
        rows = self.fixture.rows()
        observations = graph.directory_observations(self.fixture.control, self.fixture.root, rows)
        before = {
            path.relative_to(self.fixture.root): path.read_bytes()
            for path in self.fixture.root.rglob("*") if path.is_file()
        }
        first = (
            graph.project_scope_unit_graph("2026-11-02 00:00:00", graph.configuration(), self.fixture.bindings(), rows, [],
                                           observations=observations),
            graph.project_scope_unit_graph_sources("2026-11-02 00:00:00", self.fixture.bindings(), rows, [],
                                                   observations=observations),
        )
        second_rows = self.fixture.rows()
        second = (
            graph.project_scope_unit_graph("2026-11-02 00:00:00", graph.configuration(), self.fixture.bindings(), second_rows, [],
                                           observations=graph.directory_observations(self.fixture.control, self.fixture.root, second_rows)),
            graph.project_scope_unit_graph_sources("2026-11-02 00:00:00", self.fixture.bindings(), second_rows, [],
                                                   observations=graph.directory_observations(self.fixture.control, self.fixture.root, second_rows)),
        )
        self.assertEqual(first, second)
        bindings = tomllib.loads(first[1])["bindings"]
        self.assertTrue(any(row["source_kind"] == "scope_unit_declaration" for row in bindings))
        self.assertEqual(before, {
            path.relative_to(self.fixture.root): path.read_bytes()
            for path in self.fixture.root.rglob("*") if path.is_file()
        })
        self.assertFalse(graph.OUTPUT.exists())
        self.assertFalse(graph.SOURCE_MAP.exists())

    def test_row_mutation_cannot_replace_captured_declaration_source(self) -> None:
        rows = self.fixture.rows()
        changed = copy.deepcopy(rows)
        changed[0]["scope_unit_name"] = "FORGED"
        with self.assertRaises(SystemExit):
            graph.project_scope_unit_graph_sources("2026-11-02 00:00:00", self.fixture.bindings(), changed, [])


if __name__ == "__main__":
    unittest.main()
