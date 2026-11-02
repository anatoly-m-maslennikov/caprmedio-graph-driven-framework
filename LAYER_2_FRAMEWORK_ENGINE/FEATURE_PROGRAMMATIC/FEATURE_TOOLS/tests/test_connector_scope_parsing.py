from __future__ import annotations

import copy
from pathlib import Path
from types import SimpleNamespace
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_scope_parsing import (
    ScopeDataError, parse_scope_declarations, query_declarations, read_declaration, validate_scope_request,
)


def rows():
    def row(name, parent="PROJECT", kind="Unordered"):
        value = {"scope_unit_name": name, "parent": parent, "scope_unit_id": "SU-" + name,
                 "scope_unit_type": kind, "label": "FEATURE", "local_order": None,
                 "authority_path": Path("derived") / name, "delivery_path": Path("delivery") / name}
        if kind == "Ordered":
            value["local_order"] = 1
        return value
    return [row("ALPHA"), row("BETA"), row("CHILD", "ALPHA", "Ordered")]


def declarations(source_rows):
    return SimpleNamespace(
        root={"scope_unit_name": "demo", "scope_unit_type": "Unordered", "label": None,
              "local_order": None, "authority_path": Path(".caprmedio_demo"), "delivery_path": Path(".")},
        units=tuple(source_rows),
    )


def filters(identity="demo", self=True, descendants=True, predicates=None, fields=None):
    return {"frontier": {"identity": identity, "include_self": self, "include_descendants": descendants},
            "predicates": [] if predicates is None else predicates,
            "result_fields": ["scope_unit_name", "parent", "local_order"] if fields is None else fields}


class ScopeParsingTests(unittest.TestCase):
    def setUp(self):
        self.source_rows = rows()
        self.declarations = parse_scope_declarations(declarations(self.source_rows))

    def test_complete_read_projects_direct_declaration_facts_only(self):
        self.assertEqual(read_declaration(self.declarations, "demo")["declaration"],
                         {"scope_unit_name": "demo", "scope_unit_type": "Unordered"})
        actual = read_declaration(self.declarations, "CHILD")["declaration"]
        self.assertEqual(actual["scope_unit_id"], "SU-CHILD")
        self.assertEqual(actual["label"], "FEATURE")
        self.assertEqual(actual["local_order"], 1)
        self.assertNotIn("authority_path", actual)
        self.assertNotIn("delivery_path", actual)

    def test_derived_declaration_structure_normalizes_the_source_label(self):
        source = SimpleNamespace(as_structure=lambda: {"scope_units": [
            {"scope_unit_name": "demo", "parent": "PROJECT", "scope_unit_id": None,
             "scope_unit_label": None, "scope_unit_type": "Unordered",
             "authority_path": ".caprmedio_demo", "delivery_path": "."},
            {"scope_unit_name": "ALPHA", "parent": "demo", "scope_unit_id": "SU-ALPHA",
             "scope_unit_label": "FEATURE", "scope_unit_type": "Unordered",
             "authority_path": ".caprmedio_demo/SU-ALPHA_FEATURE_ALPHA", "delivery_path": "FEATURE_ALPHA"},
        ]})
        actual = parse_scope_declarations(source)
        self.assertEqual(read_declaration(actual, "ALPHA")["declaration"], {
            "scope_unit_name": "ALPHA", "scope_unit_id": "SU-ALPHA", "scope_unit_type": "Unordered",
            "label": "FEATURE", "parent": "PROJECT",
        })

    def test_exact_frontiers_and_empty_matching(self):
        full = query_declarations(self.declarations, filters())
        self.assertEqual([row["identity"] for row in full["matches"]], ["ALPHA", "BETA", "CHILD", "demo"])
        self.assertEqual(full["matches"][0]["facts"]["parent"], "PROJECT")
        for own, descendants, names in [(True, False, ["ALPHA"]), (False, True, ["CHILD"]),
                                         (True, True, ["ALPHA", "CHILD"])]:
            actual = query_declarations(self.declarations, filters("ALPHA", own, descendants))
            self.assertEqual([row["identity"] for row in actual["matches"]], names)
        empty = query_declarations(self.declarations, filters(predicates=[
            {"field": "scope_unit_name", "match": "exact", "value": "MISSING"}]))
        self.assertEqual(empty["matches"], [])
        self.assertTrue(empty["coverage"]["complete"])

    def test_literal_case_sensitive_conjunctive_filters(self):
        for mode, value in [("exact", "ALPHA"), ("prefix", "AL"), ("suffix", "PHA"), ("contains", "LP")]:
            actual = query_declarations(self.declarations, filters(predicates=[
                {"field": "scope_unit_name", "match": mode, "value": value},
                {"field": "parent", "match": "exact", "value": "PROJECT"}]))
            self.assertEqual([row["identity"] for row in actual["matches"]], ["ALPHA"])
        self.assertEqual(query_declarations(self.declarations, filters(predicates=[
            {"field": "scope_unit_name", "match": "prefix", "value": "al"}]))["matches"], [])
        actual = query_declarations(self.declarations, filters(predicates=[
            {"field": "scope_unit_type", "match": "exact", "value": "Ordered"}], fields=["local_order"]))
        self.assertEqual(actual["matches"], [{"identity": "CHILD", "facts": {"local_order": 1}}])

    def test_declaration_identity_and_graph_refusals(self):
        duplicate = rows(); duplicate.append(copy.deepcopy(duplicate[0]))
        colliding = rows(); colliding[0]["scope_unit_name"] = "demo"
        missing = rows(); missing[2]["parent"] = "MISSING"
        cycle = rows(); cycle[0]["parent"] = "CHILD"
        unordered = rows(); unordered[0]["local_order"] = 1
        for source in (duplicate, colliding, missing, cycle, unordered):
            with self.subTest(source=source), self.assertRaises(ScopeDataError) as caught:
                parse_scope_declarations(declarations(source))
            self.assertEqual(caught.exception.code, "schema_invalid")

    def test_input_and_missing_target_refusals(self):
        valid = {"operation": "query", "query": {"filters": filters()}}
        validate_scope_request(valid)
        for change in [{"frontier": None}, {"result_fields": ["parent", "parent"]},
                       {"result_fields": ["authority_path"]},
                       {"predicates": [{"field": "parent", "match": "contains", "value": "demo"}]},
                       {"predicates": [{"field": "parent", "match": "exact", "value": "PROJECT"}]},
                       {"frontier": {"identity": "source/ALPHA", "include_self": True, "include_descendants": False}},
                       {"frontier": {"identity": "demo", "include_self": False, "include_descendants": False}}]:
            with self.assertRaises(ScopeDataError) as caught:
                validate_scope_request({"operation": "query", "query": {"filters": {**filters(), **change}}})
            self.assertEqual(caught.exception.code, "input_invalid")
        for operation in [lambda: read_declaration(self.declarations, "old"),
                          lambda: query_declarations(self.declarations, filters("unknown"))]:
            with self.assertRaises(ScopeDataError) as caught:
                operation()
            self.assertEqual(caught.exception.code, "target_not_found")


if __name__ == "__main__":
    unittest.main()
