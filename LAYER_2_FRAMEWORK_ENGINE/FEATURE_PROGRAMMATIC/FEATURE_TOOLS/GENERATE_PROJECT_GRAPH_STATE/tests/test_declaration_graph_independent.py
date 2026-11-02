"""Independent source-pinning checks for declaration-derived Scope Unit graphs."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import tomllib


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
TOOLS = SCRIPT.parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))
SPEC = importlib.util.spec_from_file_location("declaration_graph", SCRIPT)
assert SPEC and SPEC.loader
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)

from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402


class DeclarationGraphIndependentTests(unittest.TestCase):
    def setUp(self) -> None:
        scratch = Path.cwd() / ".caprmedio_tmp/tests/declaration-graph"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            "[project]\nkey='fixture'\nname='fixture'\nrepository_slug='fixture'\n"
            "[paths]\ncontrol_root='.caprmedio_caprmedio'\n"
            "[artifacts.identity]\nproject_prefix='TEST'\n", encoding="utf-8")
        self.framework = self.control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        self.framework.parent.mkdir()
        self.framework.write_text(
            "[authority_modes]\ndefault='casual'\ngovernance='strict'\nmetamodel='strict'\nproject='strict'\nsemantics='strict'\n",
            encoding="utf-8")
        self.generator = self.root / graph.CANONICAL_GENERATOR_CARRIER
        self.generator.parent.mkdir(parents=True)
        self.generator.write_bytes(SCRIPT.read_bytes())
        self.patch = mock.patch.multiple(
            graph, ROOT=self.root, CONTROL=self.control, CONFIG=self.framework,
            OUTPUT=self.control / "_projection/graph.toml", SOURCE_MAP=self.control / "_projection/sources.toml",
            JOURNAL=self.control / "_journal", SCRIPT=self.generator, CANONICAL_GENERATOR=self.generator,
        )
        self.patch.start()
        self.addCleanup(self.patch.stop)
        self.declared = write_scope_unit_declarations(self.root, (
            {"scope_unit_name": "FRAMEWORK", "parent": "PROJECT", "scope_unit_type": "Ordered",
             "scope_unit_label": "LAYER", "local_order": 1},
            {"scope_unit_name": "PROGRAMMATIC", "parent": "FRAMEWORK", "scope_unit_type": "Unordered",
             "scope_unit_label": "FEATURE"},
            {"scope_unit_name": "TOOLS", "parent": "PROGRAMMATIC", "scope_unit_type": "Unordered",
             "scope_unit_label": "FEATURE"},
        ))
        root_declaration = Path(self.declared["fixture"]["declaration_path"])
        if root_declaration.parent != self.control:
            root_declaration = root_declaration.replace(self.control / root_declaration.name)
            self.declared["fixture"]["declaration_path"] = root_declaration

    def rows(self):
        return graph.scope_units(self.control, self.root, {"default": "casual"})

    def bindings(self):
        return {
            kind: {"status": "resolved", "carrier": path.relative_to(self.root).as_posix(),
                   "identifier": "fixture", "revision": "1", "updated_at": "2026-11-02 00:00:00",
                   "sha256": graph.sha(path), "journal_carrier": "fixture", "journal_line": "1",
                   "journal_event_id": "fixture"}
            for kind, path in (("project_settings", self.control / "caprmedio_project_settings.toml"),
                               ("framework_settings", self.framework))
        }

    def test_rows_are_derived_from_declarations_not_folder_topology(self) -> None:
        rows = self.rows()
        by_name = {row["scope_unit_name"]: row for row in rows}
        self.assertEqual({"FRAMEWORK", "PROGRAMMATIC", "TOOLS"}, set(by_name))
        self.assertEqual(by_name["FRAMEWORK"]["parent"], "fixture")
        self.assertEqual(by_name["TOOLS"]["parent"], by_name["PROGRAMMATIC"]["node_id"])
        self.assertTrue(by_name["FRAMEWORK"]["scope_unit_id"])
        self.assertNotIn("structural_level", by_name["TOOLS"])
        self.assertNotIn("navigational_order_number", by_name["TOOLS"])

    def test_semantic_fields_pin_the_current_declaration_atom(self) -> None:
        rows = self.rows()
        sources = tomllib.loads(graph.project_scope_unit_graph_sources("2026-11-02 00:00:00", self.bindings(), rows, []))
        by_output = {row["output_path"]: row for row in sources["bindings"]}
        for row in rows:
            source = row["declaration_source_pin"]
            for field in ("scope_unit_name", "scope_unit_id", "scope_unit_type", "scope_unit_label",
                          "parent", "authority_path", "delivery_path"):
                binding = by_output["scope_units." + row["node_id"] + "." + field]
                self.assertEqual("scope_unit_declaration", binding["source_kind"])
                self.assertEqual(source["atom_id"] + "@" + str(source["version"]), binding["source_revision"])
                self.assertEqual(source["sha256"], binding["source_sha256"])

    def test_directory_candidates_are_only_observations(self) -> None:
        rows = self.rows()
        intruder = self.control / "CA-SU-999_FEATURE_INTRUDER"
        intruder.mkdir()
        observations = graph.directory_observations(self.control, self.root, rows)
        observed = {item["authority_path"]: item for item in observations}
        self.assertEqual("undeclared", observed[intruder.relative_to(self.root).as_posix()]["kind"])
        self.assertNotIn("INTRUDER", {row["scope_unit_name"] for row in rows})

    def test_changed_declaration_refuses_old_rows(self) -> None:
        rows = self.rows()
        source = Path(self.declared["TOOLS"]["declaration_path"])
        source.write_bytes(source.read_bytes() + b"\n# changed\n")
        with self.assertRaises(SystemExit):
            graph.project_scope_unit_graph_sources("2026-11-02 00:00:00", self.bindings(), rows, [])


if __name__ == "__main__":
    unittest.main()
