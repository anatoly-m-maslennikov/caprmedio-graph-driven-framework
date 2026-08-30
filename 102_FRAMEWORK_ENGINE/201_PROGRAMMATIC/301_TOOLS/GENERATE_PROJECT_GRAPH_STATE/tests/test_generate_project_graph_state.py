"""Focused acceptance tests for typed Project Scope Unit graph discovery."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("generate_project_graph_state", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
generate_project_graph_state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = generate_project_graph_state
SPEC.loader.exec_module(generate_project_graph_state)


class GenerateProjectGraphStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir(parents=True)
        self.modes = {"default": "casual"}

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def mkdir(self, relative: str) -> Path:
        path = self.control / relative
        path.mkdir(parents=True)
        return path

    def test_live_topology_has_exactly_the_current_typed_scope_units(self) -> None:
        rows = generate_project_graph_state.scope_units(
            generate_project_graph_state.CONTROL,
            generate_project_graph_state.ROOT,
            generate_project_graph_state.configuration()["authority_modes"],
        )
        parent_by_node = {row["node_id"]: row["structural_parent"] for row in rows}
        levels_by_node = {row["node_id"]: row["structural_level"] for row in rows}
        navigational_orders_by_node = {
            row["node_id"]: row["navigational_order_number"] for row in rows
        }
        self.assertEqual(
            [
                "101_LAYER_1_FRAMEWORK_METHODOLOGY",
                "102_LAYER_2_FRAMEWORK_ENGINE",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/302_FEATURE_APPS",
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/303_FEATURE_MCP",
                "102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC",
                "102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS",
                "103_LAYER_3_OPERATOR_DOCUMENTATION",
                "104_LAYER_4_CORE_EXTENSIONS",
                "105_LAYER_5_RELEASES",
                "110_FEATURE_COMMUNITY_EXTENSIONS",
                "110_FEATURE_FIELD",
            ],
            [row["node_id"] for row in rows],
        )
        self.assertEqual("caprmedio", parent_by_node["102_LAYER_2_FRAMEWORK_ENGINE"])
        self.assertEqual(
            "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC",
            parent_by_node["102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS"],
        )
        self.assertEqual(
            "102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC",
            parent_by_node["102_LAYER_2_FRAMEWORK_ENGINE/202_FEATURE_AGENTIC/301_FEATURE_SKILLS"],
        )
        self.assertEqual(1, levels_by_node["101_LAYER_1_FRAMEWORK_METHODOLOGY"])
        self.assertEqual(2, levels_by_node["102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC"])
        self.assertEqual(
            3,
            levels_by_node[
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS"
            ],
        )
        self.assertEqual(10, navigational_orders_by_node["110_FEATURE_COMMUNITY_EXTENSIONS"])
        self.assertEqual(
            1,
            navigational_orders_by_node[
                "102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS"
            ],
        )
        self.assertNotIn("CA-Epic", "\n".join(row["node_id"] for row in rows))

    def test_nearest_typed_scope_unit_is_parent_even_across_an_epic_directory(self) -> None:
        self.mkdir("101_LAYER_1_ROOT")
        self.mkdir(
            "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD"
        )
        self.mkdir("101_LAYER_1_ROOT/archive/301_FEATURE_RETIRED")
        self.mkdir("jobs_archive/CA-J-100")

        rows = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        parent_by_node = {row["node_id"]: row["structural_parent"] for row in rows}

        self.assertEqual(
            [
                "101_LAYER_1_ROOT",
                "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD",
            ],
            [row["node_id"] for row in rows],
        )
        self.assertEqual(
            "101_LAYER_1_ROOT",
            parent_by_node[
                "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD"
            ],
        )
        self.assertTrue(
            generate_project_graph_state.EPIC_DIRECTORY.fullmatch(
                "02-CA-Epic-004-ROOT-separate-epic-carrier"
            )
        )

    def test_directory_grammar_requires_layer_order_and_forbids_feature_order(self) -> None:
        layer = generate_project_graph_state.parse_scope_unit_name("101_LAYER_3_FRAMEWORK")
        feature = generate_project_graph_state.parse_scope_unit_name("201_FEATURE_PROGRAMMATIC")
        self.assertEqual("101", layer["numeric_prefix"])
        self.assertEqual(3, layer["local_order"])
        self.assertEqual("Layer", layer["scope_unit_type"])
        self.assertIsNone(feature["local_order"])
        self.assertEqual("Feature", feature["scope_unit_type"])
        with self.assertRaisesRegex(SystemExit, "Local Order"):
            generate_project_graph_state.parse_scope_unit_name("201_FEATURE_1_PROGRAMMATIC")
        with self.assertRaisesRegex(SystemExit, "Local Order"):
            generate_project_graph_state.parse_scope_unit_name("101_LAYER_FRAMEWORK")

    def test_dynamic_prefix_width_validates_ancestry_and_emits_navigational_order(self) -> None:
        self.assertEqual(
            7,
            generate_project_graph_state.navigational_order_number(
                "12007", structural_level=12, structural_level_width=2
            ),
        )
        with self.assertRaisesRegex(SystemExit, "Structural Level"):
            generate_project_graph_state.navigational_order_number(
                "110", structural_level=2, structural_level_width=1
            )
        with self.assertRaisesRegex(SystemExit, "Navigational Order Number"):
            generate_project_graph_state.navigational_order_number(
                "100", structural_level=1, structural_level_width=1
            )

    def test_current_configuration_binding_and_projection_keep_project_identity_lowercase(self) -> None:
        config = generate_project_graph_state.configuration()
        config_sha = generate_project_graph_state.sha(generate_project_graph_state.CONFIG)
        binding = generate_project_graph_state.configuration_binding(config_sha)
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.scope_units(
            generate_project_graph_state.CONTROL,
            generate_project_graph_state.ROOT,
            modes,
        )
        payload = generate_project_graph_state.project_scope_unit_graph(
            binding["updated_at"], config, config_sha, binding, rows, []
        )

        self.assertEqual("resolved", binding["status"])
        self.assertEqual("4", binding["revision"])
        self.assertEqual("caprmedio", config["project"]["key"])
        self.assertIn('key = "caprmedio"', payload)
        self.assertIn('name = "caprmedio"', payload)
        self.assertIn(
            'carrier = ".caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/caprmedio_framework_settings.toml"',
            payload,
        )
        self.assertNotIn("002_FRAMEWORK_ENGINE", payload)

    def test_identical_scope_frontier_serializes_identically(self) -> None:
        self.mkdir("101_LAYER_1_ROOT")
        self.mkdir("101_LAYER_1_ROOT/201_FEATURE_CHILD")

        first = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        second = generate_project_graph_state.scope_units(self.control, self.root, self.modes)

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
