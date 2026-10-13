"""Independent P2304 expectations from R1070/M149/E295, using isolated sources."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest
from unittest import mock


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("p2304_independent_graph", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)
GENERATOR_SOURCE = SCRIPT.read_bytes()
SCRATCH = Path.cwd() / ".caprmedio_tmp" / "tests" / "p2304-independent"


class DeclarationGraphIndependentTests(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=SCRATCH)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        self.settings = self.root / graph.SETTINGS_PATH
        self.settings.write_text("[project]\nkey='independent'\nname='independent'\nrepository_slug='independent'\n"
                                 "[paths]\ncontrol_root='.caprmedio_caprmedio'\n"
                                 "[artifacts.identity]\nproject_prefix='TEST'\n", encoding="utf-8")
        self.framework = self.control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        self.framework.parent.mkdir()
        self.framework.write_text("[authority_modes]\ndefault='casual'\ngovernance='strict'\nmetamodel='strict'\n"
                                  "project='strict'\nsemantics='strict'\n", encoding="utf-8")
        self.structure = self.control / "project_structure.toml"
        self.declarations = [
            self.declaration("ROOT", "PROJECT", 1, 1, "101_LAYER_1_ROOT", kind="Ordered", order=1),
            self.declaration("PRIMARY", "ROOT", 2, 1, "101_LAYER_1_ROOT/201_FEATURE_PRIMARY"),
            self.declaration("SECONDARY", "ROOT", 2, 2, "101_LAYER_1_ROOT/202_FEATURE_SECONDARY"),
            self.declaration("LEGACY", "SECONDARY", 3, 7, "101_LAYER_1_ROOT/201_FEATURE_PRIMARY/201_FEATURE_LEGACY"),
            self.declaration("UNNUMBERED", "PRIMARY", 3, 8, "101_LAYER_1_ROOT/201_FEATURE_PRIMARY/unnumbered"),
            self.declaration("ABSENT", "PRIMARY", 3, 9, "101_LAYER_1_ROOT/201_FEATURE_PRIMARY/not-created"),
        ]
        for row in self.declarations[:-1]:
            (self.root / row["authority_path"]).mkdir(parents=True, exist_ok=True)
        (self.control / "101_LAYER_1_ROOT/201_FEATURE_PRIMARY/303_FEATURE_INTRUDER").mkdir()
        self.write_structure()
        self.generator = self.root / graph.CANONICAL_GENERATOR_CARRIER
        self.generator.parent.mkdir(parents=True)
        self.generator.write_bytes(GENERATOR_SOURCE)
        patch = mock.patch.multiple(graph, ROOT=self.root, CONTROL=self.control, CONFIG=self.framework,
                                    OUTPUT=self.control / "_projection/graph.toml",
                                    SOURCE_MAP=self.control / "_projection/sources.toml",
                                    JOURNAL=self.control / "_journal", SCRIPT=self.generator,
                                    CANONICAL_GENERATOR=self.generator)
        patch.start()
        self.addCleanup(patch.stop)
        self.source_before = {path: path.read_bytes() for path in (self.settings, self.framework, self.structure, self.generator)}

    def declaration(self, name, parent, level, navigation, path, *, kind="Unordered", order=None):
        row = {"scope_unit_name": name, "parent": parent, "scope_unit_type": kind,
               "scope_unit_label": "LAYER" if kind == "Ordered" else "FEATURE",
               "structural_level": level, "navigational_order_number": navigation,
               "authority_path": ".caprmedio_caprmedio/" + path,
               "delivery_path": "separate-implementation/" + name.lower()}
        if order is not None:
            row["local_order"] = order
        return row

    def write_structure(self):
        lines = ["schema_version = 1"]
        for row in self.declarations:
            lines.extend(["", "[[scope_units]]", *[f"{key} = {json.dumps(value)}" for key, value in row.items()]])
        self.structure.write_text("\n".join(lines) + "\n", encoding="utf-8")

    def rows(self):
        return graph.bind_scope_unit_structure(graph.scope_units(self.control, self.root, {"default": "casual"}))

    def assert_sources_unchanged(self):
        for path, raw in self.source_before.items():
            self.assertEqual(path.read_bytes(), raw, path)
        self.assertFalse(graph.OUTPUT.exists())
        self.assertFalse(graph.SOURCE_MAP.exists())

    def bindings(self):
        result = {}
        for kind, path in (("project_settings", self.settings), ("framework_settings", self.framework)):
            result[kind] = {"status": "resolved", "carrier": path.relative_to(self.root).as_posix(),
                            "identifier": "independent-fixture", "revision": "1", "updated_at": "2026-10-13 00:00:00",
                            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                            "journal_carrier": "fixture", "journal_line": "1", "journal_event_id": "fixture"}
        return result

    def test_complete_declarations_override_prefix_folder_parent_and_navigation(self):
        rows = self.rows()
        by_name = {row["scope_unit_name"]: row for row in rows}
        self.assertEqual(set(by_name), {row["scope_unit_name"] for row in self.declarations})
        legacy = by_name["LEGACY"]
        self.assertEqual(legacy["structural_level"], 3)
        self.assertEqual(legacy["navigational_order_number"], 7)
        self.assertEqual(legacy["parent"], by_name["SECONDARY"]["node_id"])
        self.assertEqual(legacy["structural_parent"], by_name["SECONDARY"]["node_id"])
        self.assertEqual(legacy["node_id"], "101_LAYER_1_ROOT/201_FEATURE_PRIMARY/201_FEATURE_LEGACY")
        self.assertTrue(by_name["UNNUMBERED"]["authority_materialized"])
        self.assertFalse(by_name["ABSENT"]["authority_materialized"])
        self.assertEqual(by_name["PRIMARY"]["child_composition"], "UNORDERED")
        self.assertEqual(by_name["SECONDARY"]["child_composition"], "UNORDERED")
        self.assert_sources_unchanged()

    def test_all_semantic_fields_bind_exact_structure_bytes(self):
        rows = self.rows()
        document = tomllib.loads(graph.project_scope_unit_graph_sources(
            "2026-10-13 00:00:00", self.bindings(), rows, []))
        by_field = {item["output_path"]: item for item in document["bindings"]}
        digest = hashlib.sha256(self.source_before[self.structure]).hexdigest()
        for row in rows:
            for field in ("scope_unit_name", "scope_unit_type", "scope_unit_label", "structural_level",
                          "navigational_order_number", "parent", "structural_parent", "child_composition",
                          "authority_path", "delivery_path"):
                binding = by_field["scope_units." + row["node_id"] + "." + field]
                self.assertEqual(binding["source_kind"], "project_structure", (row["scope_unit_name"], field))
                self.assertEqual(binding["source_carrier"], ".caprmedio_caprmedio/project_structure.toml")
                self.assertEqual(binding["source_sha256"], digest)
                self.assertEqual(binding["source_revision"], "sha256:" + digest)
        self.assert_sources_unchanged()

    def test_changed_structure_cannot_rebind_old_semantic_rows_to_new_source_pin(self):
        rows = graph.scope_units(self.control, self.root, {"default": "casual"})
        original_rows = copy.deepcopy(rows)
        self.declarations[3]["navigational_order_number"] = 9
        self.write_structure()
        changed_source = self.structure.read_bytes()
        with self.assertRaises(SystemExit):
            graph.bind_scope_unit_structure(rows)
        self.assertEqual(rows, original_rows)
        self.assertEqual(self.structure.read_bytes(), changed_source)
        self.assertFalse(graph.OUTPUT.exists())
        self.assertFalse(graph.SOURCE_MAP.exists())

    def test_projection_determinism_and_no_authority_or_output_writes(self):
        config = graph.configuration()
        bindings = self.bindings()
        first_rows, second_rows = self.rows(), self.rows()
        self.assertEqual(first_rows, second_rows)
        first_observations = graph.directory_observations(self.control, self.root, first_rows)
        second_observations = graph.directory_observations(self.control, self.root, second_rows)
        self.assertEqual(first_observations, second_observations)
        first = graph.project_scope_unit_graph("2026-10-13 00:00:00", config, bindings, first_rows, [],
                                               observations=first_observations)
        second = graph.project_scope_unit_graph("2026-10-13 00:00:00", config, bindings, second_rows, [],
                                                observations=second_observations)
        self.assertEqual(first, second)
        self.assertEqual(graph.project_scope_unit_graph_sources("2026-10-13 00:00:00", bindings, first_rows, [],
                                                                observations=first_observations),
                         graph.project_scope_unit_graph_sources("2026-10-13 00:00:00", bindings, second_rows, [],
                                                                observations=second_observations))
        self.assert_sources_unchanged()

    def test_undeclared_and_mismatched_folders_are_observations_only(self):
        rows = self.rows()
        expected_rows = copy.deepcopy(rows)
        observations = graph.directory_observations(self.control, self.root, rows)
        by_path = {item["authority_path"]: item for item in observations}
        legacy = by_path[self.declarations[3]["authority_path"]]
        self.assertEqual(legacy["kind"], "declared")
        self.assertEqual(legacy["observed_numeric_prefix"], "201")
        self.assertIn("parent", legacy["mismatches"])
        self.assertIn("navigational_order_number", legacy["mismatches"])
        self.assertEqual(legacy["observed_parent"], "101_LAYER_1_ROOT/201_FEATURE_PRIMARY")
        absent = by_path[self.declarations[5]["authority_path"]]
        self.assertEqual(absent["kind"], "declared")
        self.assertFalse(absent["authority_materialized"])
        self.assertTrue(by_path[self.declarations[4]["authority_path"]]["authority_materialized"])
        intruder_path = ".caprmedio_caprmedio/101_LAYER_1_ROOT/201_FEATURE_PRIMARY/303_FEATURE_INTRUDER"
        intruder = by_path[intruder_path]
        self.assertEqual(intruder["kind"], "undeclared")
        self.assertNotIn("INTRUDER", {row["scope_unit_name"] for row in rows})
        self.assertEqual(rows, expected_rows)
        document = tomllib.loads(graph.project_scope_unit_graph(
            "2026-10-13 00:00:00", graph.configuration(), self.bindings(), rows, [], observations=observations))
        self.assertEqual(document["directory_observations"],
                         [{key: value for key, value in item.items() if value is not None} for item in observations])
        self.assertEqual({row["scope_unit_name"] for row in document["scope_units"]},
                         {row["scope_unit_name"] for row in self.declarations})
        self.assert_sources_unchanged()

    def test_invalid_authority_refuses_and_does_not_fall_back_to_observed_folders(self):
        original = copy.deepcopy(self.declarations)
        for mutation in (lambda rows: rows[3].update(parent="UNDECLARED"),
                         lambda rows: rows[3].update(structural_level=2),
                         lambda rows: rows.append(copy.deepcopy(rows[3]))):
            self.declarations = copy.deepcopy(original)
            mutation(self.declarations)
            self.write_structure()
            before = self.structure.read_bytes()
            with self.assertRaises(SystemExit):
                self.rows()
            self.assertEqual(self.structure.read_bytes(), before)
            self.assertFalse(graph.OUTPUT.exists())
            self.assertFalse(graph.SOURCE_MAP.exists())

    def test_invalid_toml_and_unsafe_authority_path_refuse_without_writes(self):
        for invalid in (b"not TOML", b"schema_version = 1\n"):
            self.structure.write_bytes(invalid)
            with self.subTest(invalid=invalid), self.assertRaises(SystemExit):
                self.rows()
            self.assertEqual(self.structure.read_bytes(), invalid)
        self.declarations[3]["authority_path"] = "../outside-project"
        self.write_structure()
        before = self.structure.read_bytes()
        with self.assertRaises(SystemExit):
            self.rows()
        self.assertEqual(self.structure.read_bytes(), before)
        self.assertFalse(graph.OUTPUT.exists())
        self.assertFalse(graph.SOURCE_MAP.exists())


if __name__ == "__main__":
    unittest.main()
