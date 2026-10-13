from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_scope_parsing import (
    ScopeDataError, parse_scope_sources, query_declarations, read_declaration, validate_scope_request,
)


def serialize_project_structure(rows):
    return "schema_version = 1\n" + "".join(
        "\n[[scope_units]]\n" + "".join(f"{key} = {json.dumps(value)}\n" for key, value in row.items())
        for row in rows)


def rows():
    def row(name, parent="PROJECT", level=1, kind="Unordered"):
        value = {"scope_unit_name": name, "parent": parent, "scope_unit_type": kind,
                 "scope_unit_label": "FEATURE", "structural_level": level,
                 "navigational_order_number": level, "authority_path": "unmaterialized/" + name + "/",
                 "delivery_path": "implementation/" + name, "authority_mode": "casual"}
        if kind == "Ordered":
            value["local_order"] = 1
        return value
    return [row("ALPHA"), row("BETA"), row("CHILD", "ALPHA", 2, "Ordered")]


SETTINGS = '[project]\nname = "demo"\nkey = "demo"\nobsolete_names = ["old"]\n'


def filters(identity="demo", self=True, descendants=True, predicates=None, fields=None):
    return {"frontier": {"identity": identity, "include_self": self, "include_descendants": descendants},
            "predicates": [] if predicates is None else predicates,
            "result_fields": ["scope_unit_name", "parent", "local_order"] if fields is None else fields}


class ScopeParsingTests(unittest.TestCase):
    def setUp(self):
        self.source_rows = rows()
        self.declarations = parse_scope_sources(SETTINGS, serialize_project_structure(self.source_rows))

    def test_complete_read_preserves_values_and_absence(self):
        self.assertEqual(read_declaration(self.declarations, "demo")["declaration"],
                         {"name": "demo", "key": "demo", "obsolete_names": ["old"]})
        for row in self.source_rows:
            self.assertEqual(read_declaration(self.declarations, row["scope_unit_name"])["declaration"], row)
        self.assertNotIn("local_order", read_declaration(self.declarations, "ALPHA")["declaration"])
        self.assertNotIn("version", read_declaration(self.declarations, "CHILD")["declaration"])

    def test_exact_frontiers_and_empty_matching(self):
        full = query_declarations(self.declarations, filters())
        self.assertEqual([row["identity"] for row in full["matches"]], ["ALPHA", "BETA", "CHILD", "demo"])
        self.assertEqual(full["matches"][0]["facts"]["parent"], "demo")
        self.assertNotIn("authority_path", full["matches"][0]["facts"])
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
                {"field": "parent", "match": "exact", "value": "demo"}]))
            self.assertEqual([row["identity"] for row in actual["matches"]], ["ALPHA"])
        self.assertEqual(query_declarations(self.declarations, filters(predicates=[
            {"field": "scope_unit_name", "match": "prefix", "value": "al"}]))["matches"], [])
        actual = query_declarations(self.declarations, filters(predicates=[
            {"field": "scope_unit_type", "match": "exact", "value": "Ordered"}], fields=["local_order"]))
        self.assertEqual(actual["matches"], [{"identity": "CHILD", "facts": {"local_order": 1}}])

    def test_schema_identity_and_graph_refusals(self):
        cases = []
        duplicate = rows(); duplicate.append(copy.deepcopy(duplicate[0])); cases.append((duplicate, "target_ambiguous"))
        colliding = rows(); colliding[0]["scope_unit_name"] = "demo"; cases.append((colliding, "target_ambiguous"))
        missing = rows(); missing[2]["parent"] = "MISSING"; cases.append((missing, "schema_invalid"))
        cycle = rows(); cycle[0]["parent"] = "CHILD"; cases.append((cycle, "schema_invalid"))
        unordered = rows(); unordered[0]["local_order"] = 1; cases.append((unordered, "schema_invalid"))
        escaping = rows(); escaping[0]["authority_path"] = "../outside"; cases.append((escaping, "schema_invalid"))
        for source, code in cases:
            with self.subTest(code=code, source=source):
                with self.assertRaises(ScopeDataError) as caught:
                    parse_scope_sources(SETTINGS, serialize_project_structure(source))
                self.assertEqual(caught.exception.code, code)
        for source in ['schema_version = 1\n', 'schema_version = 2\nscope_units = []\n',
                       'schema_version = 1\nscope_units = []\nextra = true\n',
                       serialize_project_structure(rows()) + 'node_id = "invented"\n']:
            with self.assertRaises(ScopeDataError):
                parse_scope_sources(SETTINGS, source)

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
