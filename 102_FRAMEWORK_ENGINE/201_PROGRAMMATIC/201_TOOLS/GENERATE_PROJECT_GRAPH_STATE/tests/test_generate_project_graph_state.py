"""Focused acceptance tests for typed Project Scope Unit graph discovery."""

from __future__ import annotations

import copy
import importlib.util
import json
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
import tomllib


SCRIPT = Path(__file__).resolve().parents[1] / "generate_project_graph_state.py"
SPEC = importlib.util.spec_from_file_location("generate_project_graph_state", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
generate_project_graph_state = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = generate_project_graph_state
SPEC.loader.exec_module(generate_project_graph_state)


class GenerateProjectGraphStateTests(unittest.TestCase):
    def test_persistent_carriers_use_the_project_single_roots(self) -> None:
        projection_root = generate_project_graph_state.CONTROL / "_projection"
        self.assertEqual(projection_root, generate_project_graph_state.OUTPUT.parent)
        self.assertEqual(projection_root, generate_project_graph_state.SOURCE_MAP.parent)
        self.assertEqual(
            generate_project_graph_state.CONTROL / "_journal",
            generate_project_graph_state.JOURNAL,
        )

    def test_methodology_sources_are_independent_from_instance_settings(self) -> None:
        expected = (
            generate_project_graph_state.CONTROL
            / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources"
        )
        self.assertEqual(expected, generate_project_graph_state.METHODOLOGY_SOURCES)
        self.assertNotEqual(generate_project_graph_state.CONFIG.parent.parent,
                            generate_project_graph_state.METHODOLOGY_SOURCES)

    def test_quoted_source_timestamps_use_the_existing_supported_formats(self) -> None:
        for value in ('"2026-09-06 12:00:00 +0400"', "'2026-09-06 12:00:00'", "2026-09-06 12:00:00 +0400"):
            self.assertEqual("2026-09-06 12:00:00", generate_project_graph_state.normalise_timestamp(value))
        self.assertEqual("", generate_project_graph_state.normalise_timestamp('"invalid"'))

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.control = self.root / ".caprmedio_caprmedio"
        self.root.mkdir(parents=True)
        self.control.mkdir()
        # Project-graph output writes must resolve this fixture itself, rather
        # than a checkout enclosing the test temporary directory.
        self.modes = {"default": "casual"}
        self.project_settings = self.root / generate_project_graph_state.SETTINGS_PATH
        self.project_settings.write_text(
            "[project]\nkey = 'fixture_project'\nname = 'fixture_project'\nrepository_slug = 'test'\n"
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\n"
            "[artifacts.identity]\nproject_prefix = 'TEST'\n", encoding="utf-8",
        )
        self.framework_settings = self.control / "000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"
        self.framework_settings.parent.mkdir()
        self.framework_settings.write_text(
            "[authority_modes]\ndefault = 'casual'\ngovernance = 'strict'\n"
            "metamodel = 'strict'\nproject = 'strict'\nsemantics = 'strict'\n", encoding="utf-8",
        )
        self.methodology_sources = (
            self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/"
            "000_APPLICABLE_MTHD_sources"
        )
        for index, (scope, atom_id) in enumerate((
            ("001_CORE_META_MODEL", "CA-R-101"),
            ("002_INSTALLED_EXTENSIONS", "CA-M-102"),
            ("003_PROJECT_CONFIGURATION", "CA-D-103"),
        ), 1):
            source = self.methodology_sources / scope / f"{atom_id}--fixture.md"
            source.parent.mkdir(parents=True, exist_ok=True)
            source.write_text(
                f"---\natom_id: {atom_id}\nversion: {index}\nupdated_at: 2026-10-01 00:00:0{index}\n---\n",
                encoding="utf-8",
            )
        self.fixture_generator = self.root / generate_project_graph_state.CANONICAL_GENERATOR_CARRIER
        self.fixture_generator.parent.mkdir(parents=True, exist_ok=True)
        self.fixture_generator.write_bytes(generate_project_graph_state.CANONICAL_GENERATOR.read_bytes())
        self._fixture_patch = mock.patch.multiple(
            generate_project_graph_state,
            ROOT=self.root,
            CONTROL=self.control,
            CONFIG=self.framework_settings,
            JOURNAL=self.control / "_journal",
            OUTPUT=self.control / "_projection/project_scope_unit_graph.projection.toml",
            SOURCE_MAP=self.control / "_projection/project_scope_unit_graph_sources.projection.toml",
            SCRIPT=self.fixture_generator,
            CANONICAL_GENERATOR=self.fixture_generator,
            METHODOLOGY_SOURCES=self.methodology_sources,
            METHODOLOGY_SOURCE_SCOPE_UNITS=(
                ("CORE_META_MODEL", self.methodology_sources / "001_CORE_META_MODEL"),
                ("INSTALLED_EXTENSIONS", self.methodology_sources / "002_INSTALLED_EXTENSIONS"),
                ("PROJECT_CONFIGURATION", self.methodology_sources / "003_PROJECT_CONFIGURATION"),
            ),
        )
        self._fixture_patch.start()
        self.addCleanup(self._fixture_patch.stop)

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def mkdir(self, relative: str) -> Path:
        path = self.control / relative
        path.mkdir(parents=True)
        return path

    def fixture_scope_units(self) -> list[dict[str, object]]:
        self.mkdir("101_LAYER_1_FRAMEWORK")
        self.mkdir("101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC")
        self.mkdir("101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS")
        self.mkdir("102_LAYER_2_OPERATIONS")
        self.declarations = [
            {"scope_unit_name": name, "parent": parent, "scope_unit_type": kind,
             "scope_unit_label": label, "structural_level": level,
             "navigational_order_number": navigation, "authority_path": f".caprmedio_caprmedio/{authority}",
             "delivery_path": delivery, **({"local_order": order} if order is not None else {})}
            for name, parent, kind, label, level, navigation, order, authority, delivery in (
                ("FRAMEWORK", "PROJECT", "Ordered", "LAYER", 1, 1, 1,
                 "101_LAYER_1_FRAMEWORK", "101_FRAMEWORK"),
                ("PROGRAMMATIC", "FRAMEWORK", "Unordered", "FEATURE", 2, 1, None,
                 "101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC", "101_FRAMEWORK/201_PROGRAMMATIC"),
                ("TOOLS", "PROGRAMMATIC", "Unordered", "FEATURE", 3, 1, None,
                 "101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS", "101_FRAMEWORK/201_PROGRAMMATIC/301_TOOLS"),
                ("OPERATIONS", "PROJECT", "Ordered", "LAYER", 1, 2, 2,
                 "102_LAYER_2_OPERATIONS", "102_OPERATIONS"),
            )
        ]
        self.write_structure(self.declarations)
        return generate_project_graph_state.scope_units(self.control, self.root, self.modes)

    def write_structure(self, declarations: list[dict[str, object]], *, schema_version: object = 1) -> None:
        lines = [f"schema_version = {json.dumps(schema_version)}"]
        for declaration in declarations:
            lines += ["", "[[scope_units]]"]
            lines += [f"{field} = {json.dumps(value)}" for field, value in declaration.items()]
        (self.control / "project_structure.toml").write_text("\n".join(lines) + "\n", encoding="utf-8")

    def test_delivery_paths_use_explicit_bindings_without_materializing_folders(self) -> None:
        self.fixture_scope_units()
        self.mkdir("101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/302_FEATURE_PROJECT_TOOLS")
        self.declarations[2]["delivery_path"] = "native/kept-tools"
        self.declarations.append(
            {"scope_unit_name": "PROJECT_TOOLS", "parent": "PROGRAMMATIC",
             "scope_unit_type": "Unordered", "scope_unit_label": "FEATURE",
             "structural_level": 3, "navigational_order_number": 2,
             "authority_path": ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/302_FEATURE_PROJECT_TOOLS",
             "delivery_path": "PROJECT_TOOLS"}
        )
        self.write_structure(self.declarations)
        before = (self.control / "project_structure.toml").read_bytes()
        rows = generate_project_graph_state.bind_scope_unit_structure(
            generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        )
        deliveries = {row["scope_unit_name"]: row["delivery_path"] for row in rows}
        self.assertEqual("native/kept-tools", deliveries["TOOLS"])
        self.assertEqual("PROJECT_TOOLS", deliveries["PROJECT_TOOLS"])
        self.assertEqual("101_FRAMEWORK", deliveries["FRAMEWORK"])
        self.assertEqual("102_OPERATIONS", deliveries["OPERATIONS"])
        self.assertFalse((self.root / "native").exists())
        self.assertFalse((self.root / "PROJECT_TOOLS").exists())
        self.assertEqual(before, (self.control / "project_structure.toml").read_bytes())
        self.assertFalse(generate_project_graph_state.OUTPUT.exists())
        self.assertFalse(generate_project_graph_state.SOURCE_MAP.exists())

    def test_missing_duplicate_mismatched_and_unsafe_structure_bindings_refuse_without_rows_changed(self) -> None:
        rows = self.fixture_scope_units()
        originals = copy.deepcopy(rows)
        cases = []
        cases.append(self.declarations[:2] + self.declarations[3:])
        cases.append(self.declarations + [self.declarations[2]])
        duplicate_authority = copy.deepcopy(self.declarations)
        duplicate_authority.append({**self.declarations[2], "scope_unit_name": "OTHER"})
        cases.append(duplicate_authority)
        mismatch = copy.deepcopy(self.declarations)
        mismatch[2]["scope_unit_name"] = "OTHER"
        cases.append(mismatch)
        for field in ("authority_path", "delivery_path"):
            for value in (".", "", 1, True, "../outside", "/outside", "native/../outside", "native//tools", "native/tools//", "native/./tools", "C:/outside", "native\\tools"):
                invalid = copy.deepcopy(self.declarations)
                invalid[2][field] = value
                cases.append(invalid)
        for field, value in (("scope_unit_type", True), ("scope_unit_type", ["Unordered"]), ("structural_level", 0),
                             ("parent", ""), ("navigational_order_number", True)):
            invalid = copy.deepcopy(self.declarations)
            invalid[2][field] = value
            cases.append(invalid)
        for declarations in cases:
            with self.subTest(declarations=declarations):
                self.write_structure(declarations)
                with self.assertRaises(SystemExit):
                    generate_project_graph_state.bind_scope_unit_structure(rows)
                self.assertEqual(originals, rows)
                self.assertFalse(generate_project_graph_state.OUTPUT.exists())
                self.assertFalse(generate_project_graph_state.SOURCE_MAP.exists())

    def test_terminal_slash_alias_preserves_delivery_and_rejects_duplicate_authority(self) -> None:
        rows = self.fixture_scope_units()
        declaration = self.declarations[2]
        declaration["authority_path"] += "/"
        declaration["delivery_path"] += "/"
        self.write_structure(self.declarations)
        source = self.control / "project_structure.toml"
        before = source.read_bytes()
        rows = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        bound = generate_project_graph_state.bind_scope_unit_structure(rows)
        tools = next(row for row in bound if row["scope_unit_name"] == "TOOLS")
        self.assertEqual("101_FRAMEWORK/201_PROGRAMMATIC/301_TOOLS/", tools["delivery_path"])
        self.assertEqual(before, source.read_bytes())
        original_rows = copy.deepcopy(rows)
        duplicate = {**declaration, "scope_unit_name": "OTHER",
                     "authority_path": declaration["authority_path"].removesuffix("/")}
        self.write_structure([*self.declarations, duplicate])
        before = source.read_bytes()
        with self.assertRaisesRegex(SystemExit, "duplicate Project Structure authority binding"):
            generate_project_graph_state.bind_scope_unit_structure(rows)
        self.assertEqual(original_rows, rows)
        self.assertEqual(before, source.read_bytes())
        self.assertFalse(generate_project_graph_state.OUTPUT.exists())
        self.assertFalse(generate_project_graph_state.SOURCE_MAP.exists())

    def test_changed_structure_cannot_repin_old_semantic_scope_rows(self) -> None:
        rows = self.fixture_scope_units()
        before = copy.deepcopy(rows)
        self.declarations[2]["navigational_order_number"] = 7
        self.write_structure(self.declarations)
        with self.assertRaisesRegex(SystemExit, "changed after Scope rows"):
            generate_project_graph_state.bind_scope_unit_structure(rows)
        self.assertEqual(before, rows)
        self.assertFalse(generate_project_graph_state.OUTPUT.exists())
        self.assertFalse(generate_project_graph_state.SOURCE_MAP.exists())

    def test_directory_observations_do_not_redeclare_folders_and_semantics_bind_toml(self) -> None:
        rows = self.fixture_scope_units()
        self.mkdir("101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/201_FEATURE_OTHER")
        self.declarations[2]["authority_path"] = ".caprmedio_caprmedio/untyped-tools"
        self.declarations[2]["authority_mode"] = "strict"
        self.write_structure(self.declarations)
        source = self.control / "project_structure.toml"
        before = source.read_bytes()
        rows = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        observations = generate_project_graph_state.directory_observations(self.control, self.root, rows)
        by_path = {item["authority_path"]: item for item in observations}
        self.assertNotIn("OTHER", {row["scope_unit_name"] for row in rows})
        self.assertEqual("undeclared", by_path[".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/201_FEATURE_OTHER"]["kind"])
        self.assertFalse(by_path[".caprmedio_caprmedio/untyped-tools"]["authority_materialized"])
        self.assertEqual("declared", by_path[".caprmedio_caprmedio/untyped-tools"]["kind"])
        config = generate_project_graph_state.configuration()
        bindings = generate_project_graph_state.settings_bindings()
        atoms = generate_project_graph_state.active_source_atoms()
        graph = generate_project_graph_state.project_scope_unit_graph("2026-10-01 00:00:00", config, bindings, rows, atoms, observations=observations)
        sources = generate_project_graph_state.project_scope_unit_graph_sources("2026-10-01 00:00:00", bindings, rows, atoms, observations=observations)
        document = tomllib.loads(sources)
        by_field = {item["output_path"]: item for item in document["bindings"]}
        for row in rows:
            prefix = "scope_units." + str(row["node_id"]) + "."
            for field in ("scope_unit_name", "scope_unit_type", "scope_unit_label", "parent", "structural_parent",
                          "structural_level", "navigational_order_number", "authority_path", "delivery_path", "child_composition"):
                self.assertEqual("project_structure", by_field[prefix + field]["source_kind"])
                self.assertEqual(generate_project_graph_state.sha(source), by_field[prefix + field]["source_sha256"])
            mode_kind = "project_structure" if row["scope_unit_name"] == "TOOLS" else "framework_settings"
            self.assertEqual(mode_kind, by_field[prefix + "authority_mode"]["source_kind"])
            self.assertEqual("directory_observation", by_field[prefix + "authority_materialized"]["source_kind"])
        encoded_observations = [
            {key: value for key, value in item.items() if value is not None} for item in observations
        ]
        self.assertEqual(encoded_observations, tomllib.loads(graph)["directory_observations"])
        self.assertEqual(graph, generate_project_graph_state.project_scope_unit_graph("2026-10-01 00:00:00", config, bindings, rows, atoms, observations=observations))
        self.assertEqual(before, source.read_bytes())
        self.assertFalse(generate_project_graph_state.OUTPUT.exists())
        self.assertFalse(generate_project_graph_state.SOURCE_MAP.exists())

    def test_declared_folder_beneath_an_ordinary_file_refuses(self) -> None:
        rows = self.fixture_scope_units()
        original_rows = copy.deepcopy(rows)
        (self.root / "file-parent").write_text("ordinary file", encoding="utf-8")
        for field in ("authority_path", "delivery_path"):
            with self.subTest(field=field):
                declarations = copy.deepcopy(self.declarations)
                declarations[2][field] = "file-parent/tools"
                self.write_structure(declarations)
                with self.assertRaisesRegex(SystemExit, "not a directory"):
                    generate_project_graph_state.bind_scope_unit_structure(rows)
                self.assertEqual(original_rows, rows)
                self.assertFalse(generate_project_graph_state.OUTPUT.exists())
                self.assertFalse(generate_project_graph_state.SOURCE_MAP.exists())

    def test_structure_source_and_binding_symlinks_and_invalid_schema_refuse(self) -> None:
        rows = self.fixture_scope_units()
        for version in (2, True, "1"):
            with self.subTest(schema_version=version):
                self.write_structure(self.declarations, schema_version=version)
                with self.assertRaisesRegex(SystemExit, "schema"):
                    generate_project_graph_state.bind_scope_unit_structure(rows)
        self.write_structure(self.declarations)
        source = self.control / "project_structure.toml"
        original = source.read_bytes()
        for payload in ("not TOML", "schema_version = 1\n", source.read_text() + "\nunknown = 1\n"):
            source.write_text(payload, encoding="utf-8")
            with self.assertRaises(SystemExit):
                generate_project_graph_state.bind_scope_unit_structure(rows)
        source.write_bytes(original)
        saved = self.root / "saved.toml"
        source.rename(saved)
        source.symlink_to(saved)
        with self.assertRaisesRegex(SystemExit, "missing or invalid"):
            generate_project_graph_state.bind_scope_unit_structure(rows)
        source.unlink()
        saved.rename(source)
        (self.root / "native").symlink_to(self.control, target_is_directory=True)
        self.declarations[2]["delivery_path"] = "native/tools"
        self.write_structure(self.declarations)
        with self.assertRaisesRegex(SystemExit, "unsafe"):
            generate_project_graph_state.bind_scope_unit_structure(rows)
        source.unlink()
        with self.assertRaisesRegex(SystemExit, "missing or invalid"):
            generate_project_graph_state.bind_scope_unit_structure(rows)

    def test_fixture_topology_derives_typed_scope_unit_structure(self) -> None:
        rows = self.fixture_scope_units()
        parent_by_node = {row["node_id"]: row["structural_parent"] for row in rows}
        levels_by_node = {row["node_id"]: row["structural_level"] for row in rows}
        navigational_orders_by_node = {
            row["node_id"]: row["navigational_order_number"] for row in rows
        }
        self.assertEqual(
            [
                "101_LAYER_1_FRAMEWORK",
                "101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC",
                "101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS",
                "102_LAYER_2_OPERATIONS",
            ],
            [row["node_id"] for row in rows],
        )
        self.assertEqual("fixture_project", parent_by_node["101_LAYER_1_FRAMEWORK"])
        self.assertEqual(
            "101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC",
            parent_by_node["101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS"],
        )
        self.assertEqual(1, levels_by_node["101_LAYER_1_FRAMEWORK"])
        self.assertEqual(2, levels_by_node["101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC"])
        self.assertEqual(
            3,
            levels_by_node["101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS"],
        )
        self.assertEqual(2, navigational_orders_by_node["102_LAYER_2_OPERATIONS"])
        self.assertEqual(
            1,
            navigational_orders_by_node["101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/301_FEATURE_TOOLS"],
        )
        self.assertNotIn("CA-Epic", "\n".join(row["node_id"] for row in rows))
        required_fields = {
            "scope_unit_name",
            "project_boundary_position",
            "scope_unit_type",
            "scope_unit_label",
            "child_composition",
            "structural_level",
            "local_order",
            "navigational_order_number",
            "parent",
            "authority_path",
        }
        self.assertTrue(all(required_fields <= set(row) for row in rows))
        self.assertTrue(all(row["project_boundary_position"] == "PROJECT" for row in rows))
        self.assertEqual("Ordered", rows[0]["scope_unit_type"])
        self.assertEqual("LAYER", rows[0]["scope_unit_label"])
        self.assertEqual("UNORDERED", rows[0]["child_composition"])
        self.assertEqual("NONE", rows[2]["child_composition"])

    def test_declared_scope_unit_parent_is_preserved_across_an_epic_directory(self) -> None:
        self.mkdir("101_LAYER_1_ROOT")
        self.mkdir(
            "101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD"
        )
        self.mkdir("101_LAYER_1_ROOT/archive/301_FEATURE_RETIRED")
        self.mkdir("jobs_archive/CA-J-100")
        self.write_structure([
            {"scope_unit_name": "ROOT", "parent": "PROJECT", "scope_unit_type": "Ordered",
             "scope_unit_label": "LAYER", "structural_level": 1, "local_order": 1,
             "navigational_order_number": 1, "authority_path": ".caprmedio_caprmedio/101_LAYER_1_ROOT",
             "delivery_path": "root"},
            {"scope_unit_name": "CHILD", "parent": "ROOT", "scope_unit_type": "Unordered",
             "scope_unit_label": "FEATURE", "structural_level": 2, "navigational_order_number": 1,
             "authority_path": ".caprmedio_caprmedio/101_LAYER_1_ROOT/03_plan/02-CA-Epic-004-ROOT-separate-epic-carrier/201_FEATURE_CHILD",
             "delivery_path": "root/child"},
        ])

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

    def test_declarations_override_legacy_prefix_and_include_untyped_and_missing_authority(self) -> None:
        self.fixture_scope_units()
        self.mkdir("101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS")
        self.mkdir("untyped-scope")
        self.declarations[2]["authority_path"] = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS"
        self.declarations[2]["navigational_order_number"] = 7
        for name, authority in (("UNTYPED", "untyped-scope"), ("ABSENT", "not-materialized")):
            self.declarations.append(
                {"scope_unit_name": name, "parent": "PROGRAMMATIC", "scope_unit_type": "Unordered",
                 "scope_unit_label": "CUSTOM", "structural_level": 3, "navigational_order_number": 8,
                 "authority_path": ".caprmedio_caprmedio/" + authority, "delivery_path": "native/" + name}
            )
        self.write_structure(self.declarations)
        source = self.control / "project_structure.toml"
        before = source.read_bytes()
        rows = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        by_name = {row["scope_unit_name"]: row for row in rows}
        self.assertEqual(6, len(rows))
        self.assertEqual(3, by_name["TOOLS"]["structural_level"])
        self.assertEqual(7, by_name["TOOLS"]["navigational_order_number"])
        self.assertEqual("101_LAYER_1_FRAMEWORK/201_FEATURE_PROGRAMMATIC", by_name["TOOLS"]["parent"])
        self.assertEqual("untyped-scope", by_name["UNTYPED"]["node_id"])
        self.assertTrue(by_name["UNTYPED"]["authority_materialized"])
        self.assertFalse(by_name["ABSENT"]["authority_materialized"])
        self.assertEqual("CUSTOM", by_name["ABSENT"]["scope_unit_label"])
        self.assertEqual(before, source.read_bytes())
        self.assertFalse((self.control / "not-materialized").exists())
        self.assertFalse(generate_project_graph_state.OUTPUT.exists())

    def test_directory_grammar_requires_layer_order_and_forbids_feature_order(self) -> None:
        layer = generate_project_graph_state.parse_scope_unit_name("101_LAYER_3_FRAMEWORK")
        feature = generate_project_graph_state.parse_scope_unit_name("201_FEATURE_PROGRAMMATIC")
        self.assertEqual("101", layer["numeric_prefix"])
        self.assertEqual(3, layer["local_order"])
        self.assertEqual("Ordered", layer["scope_unit_type"])
        self.assertEqual("LAYER", layer["scope_unit_label"])
        self.assertIsNone(feature["local_order"])
        self.assertEqual("Unordered", feature["scope_unit_type"])
        self.assertEqual("FEATURE", feature["scope_unit_label"])
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
        bindings = generate_project_graph_state.settings_bindings()
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.bind_scope_unit_structure(
            self.fixture_scope_units()
        )
        source_atoms = generate_project_graph_state.active_source_atoms()
        payload = generate_project_graph_state.project_scope_unit_graph(
            generate_project_graph_state.source_updated_at(bindings, source_atoms), config, bindings, rows, source_atoms
        )

        self.assertEqual(
            ".caprmedio_caprmedio/caprmedio_project_settings.toml",
            bindings["project_settings"]["carrier"],
        )
        self.assertEqual("TEST", config["artifacts"]["identity"]["project_prefix"])
        self.assertEqual("fixture_project", config["project"]["key"])
        self.assertIn('key = "fixture_project"', payload)
        self.assertIn('name = "fixture_project"', payload)
        self.assertIn(
            'carrier = ".caprmedio_caprmedio/000_CAPRMEDIO_framework/caprmedio_framework_settings.toml"',
            payload,
        )
        self.assertNotIn("002_FRAMEWORK_ENGINE", payload)


    def test_identity_and_structural_project_parent_come_only_from_project_settings(self) -> None:
        self.fixture_scope_units()
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ):
            config = generate_project_graph_state.configuration()
            rows = generate_project_graph_state.scope_units(self.control, self.root, config["authority_modes"])
        self.assertEqual("fixture_project", config["project"]["name"])
        self.assertEqual("TEST", config["artifacts"]["identity"]["project_prefix"])
        self.assertEqual("fixture_project", rows[0]["parent"])
        self.assertEqual("fixture_project", rows[0]["structural_parent"])

    def test_missing_or_invalid_project_settings_never_falls_back_to_framework_settings(self) -> None:
        self.framework_settings.write_text(
            self.framework_settings.read_text() + "\n[project]\nkey='caprmedio'\nname='caprmedio'\nrepository_slug='test'\n"
            "[artifacts.identity]\nproject_prefix='CA'\n", encoding="utf-8",
        )
        self.project_settings.unlink()
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ):
            with self.assertRaisesRegex(SystemExit, "Project Settings"):
                generate_project_graph_state.configuration()
            for payload in ("not valid TOML", "project='bad'", "[project]\nname='caprmedio'\n"):
                with self.subTest(payload=payload):
                    self.project_settings.write_text(payload)
                    with self.assertRaisesRegex(SystemExit, "Project Settings"):
                        generate_project_graph_state.configuration()

    def test_duplicate_project_identity_in_framework_settings_is_rejected(self) -> None:
        original = self.framework_settings.read_text()
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ):
            for addition in ("\n[project]\nname='other'\n", "\n[artifacts.identity]\nproject_prefix='OTHER'\n"):
                with self.subTest(addition=addition):
                    self.framework_settings.write_text(original + addition)
                    with self.assertRaisesRegex(SystemExit, "belongs only in Project Settings"):
                        generate_project_graph_state.configuration()

    def test_log_rows_bind_settings_separately_and_detect_drift_or_ambiguity(self) -> None:
        journal = self.control / "work_journal"
        journal.mkdir()
        records = [
            {
                "schema_version": 3,
                "kind": "governed_project_change", "event": "completed", "subject_kind": "file",
                "occurred_at": "2026-09-11 00:00:00 +0400", "event_id": path.stem,
                "action_id": "settings-fixture", "author": "fixture-author",
                "llm_session": {"app": "codex", "uuid": "fixture-session"},
                "structural_scope": "fixture_project", "action_type": "ADD", "sources": [],
                "result": {"state": "present", "filename": path.name,
                           "path": path.relative_to(self.root).as_posix(),
                           "sha256": generate_project_graph_state.sha(path), "version": 1},
            }
            for path in (self.project_settings, self.framework_settings)
        ]
        receipt = journal / "settings.ndjson"
        receipt.write_text("\n".join(json.dumps(record) for record in records) + "\n")
        with mock.patch.object(generate_project_graph_state, "ROOT", self.root), mock.patch.object(
            generate_project_graph_state, "CONFIG", self.framework_settings
        ), mock.patch.object(generate_project_graph_state, "JOURNAL", journal):
            bindings = generate_project_graph_state.settings_bindings()
            self.assertTrue(all(item["status"] == "resolved" for item in bindings.values()))
            self.assertNotEqual(bindings["project_settings"]["carrier"], bindings["framework_settings"]["carrier"])
            self.assertTrue(all("atom_id" not in item for item in bindings.values()))
            original = self.project_settings.read_text()
            self.project_settings.write_text(original + "\n# drift\n")
            bindings = generate_project_graph_state.settings_bindings()
            self.assertEqual("unresolved", bindings["project_settings"]["status"])
            self.assertEqual("resolved", bindings["framework_settings"]["status"])
            self.project_settings.write_text(original)
            receipt.write_text(receipt.read_text() + json.dumps(records[0]) + "\n")
            self.assertEqual("ambiguous", generate_project_graph_state.settings_bindings()["project_settings"]["status"])

    def test_active_methodology_source_frontier_covers_every_emitted_scope_unit_field(self) -> None:
        config = generate_project_graph_state.configuration()
        bindings = generate_project_graph_state.settings_bindings()
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.bind_scope_unit_structure(
            self.fixture_scope_units()
        )
        source_atoms = generate_project_graph_state.active_source_atoms()
        payload = generate_project_graph_state.project_scope_unit_graph_sources(
            generate_project_graph_state.source_updated_at(bindings, source_atoms),
            bindings,
            rows,
            source_atoms,
        )
        document = tomllib.loads(payload)
        bindings = document["bindings"]
        projection = document["projection"]
        by_field = {item["output_path"]: item for item in bindings}
        for field in ("project.key", "project.name", "project.repository_slug", "project.obsolete_names", "artifacts.identity.project_prefix"):
            self.assertEqual("project_settings", by_field[field]["source_kind"])
            self.assertEqual(generate_project_graph_state.SETTINGS_PATH.as_posix(), by_field[field]["source_carrier"])
        self.assertEqual("framework_settings", by_field["authority_modes"]["source_kind"])

        self.assertEqual(
            "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py",
            projection["canonical_generator"],
        )
        self.assertEqual(
            generate_project_graph_state.sha(generate_project_graph_state.CANONICAL_GENERATOR),
            projection["canonical_generator_sha256"],
        )
        self.assertTrue(projection["executed_generator"])
        self.assertTrue(projection["executed_generator_sha256"])
        self.assertEqual(4, len(rows))
        self.assertGreater(len(source_atoms), 0)
        self.assertEqual(
            {atom["atom_id"] for atom in source_atoms},
            {
                binding["output_path"].removeprefix("methodology_source_atoms.")
                for binding in bindings
                if binding["source_kind"] == "methodology_source_atom"
            },
        )
        for row in rows:
            prefix = "scope_units." + str(row["node_id"]) + "."
            output_paths = {item["output_path"] for item in bindings if item["output_path"].startswith(prefix)}
            for field in (
                "scope_unit_name",
                "project_boundary_position",
                "scope_unit_type",
                "scope_unit_label",
                "child_composition",
                "structural_level",
                "navigational_order_number",
                "parent",
                "authority_path",
                "delivery_path",
            ):
                self.assertIn(prefix + field, output_paths)
            self.assertIn(prefix + "delivery_path", output_paths)
            structure_bindings = [
                item
                for item in bindings
                if item["output_path"] == prefix + "delivery_path"
            ]
            self.assertEqual(1, len(structure_bindings))
            self.assertEqual("project_structure", structure_bindings[0]["source_kind"])
            self.assertEqual(".caprmedio_caprmedio/project_structure.toml", structure_bindings[0]["source_carrier"])
            self.assertEqual(generate_project_graph_state.sha(self.control / "project_structure.toml"), structure_bindings[0]["source_sha256"])
            self.assertEqual("sha256:" + structure_bindings[0]["source_sha256"], structure_bindings[0]["source_revision"])

    def test_main_generates_with_unknown_or_ambiguous_optional_history(self) -> None:
        self.fixture_scope_units()
        journal = generate_project_graph_state.JOURNAL
        row = {"result": {"path": self.project_settings.relative_to(self.root).as_posix(),
                          "sha256": generate_project_graph_state.sha(self.project_settings)}}
        for history in ("missing", "ambiguous", "invalid_encoding", "unavailable"):
            with self.subTest(history=history):
                if history == "ambiguous":
                    journal.mkdir()
                    (journal / "settings.ndjson").write_text((json.dumps(row) + "\n") * 2)
                elif history == "invalid_encoding":
                    (journal / "settings.ndjson").write_bytes(b"\xff\n")
                with mock.patch.object(generate_project_graph_state, "parse_args",
                                       return_value=mock.Mock(describe=False, apply=True)), \
                        mock.patch.object(generate_project_graph_state, "installed_generator"), \
                        mock.patch.object(generate_project_graph_state, "write_output") as write, \
                        mock.patch("builtins.print"):
                    if history == "unavailable":
                        with mock.patch.object(generate_project_graph_state, "journal_records",
                                               side_effect=PermissionError("unavailable")):
                            generate_project_graph_state.main()
                    else:
                        generate_project_graph_state.main()
                self.assertEqual(2, write.call_count)
                graph = tomllib.loads(write.call_args_list[0].args[1])
                self.assertEqual("unknown", graph["projection"]["currentness"])
                self.assertEqual("fixture_project", graph["project"]["name"])
                for kind, carrier in (("project_settings", self.project_settings),
                                      ("framework_settings", self.framework_settings)):
                    binding = graph["settings"][kind]
                    self.assertEqual("ambiguous" if history == "ambiguous" and kind == "project_settings"
                                     else "unresolved", binding["status"])
                    self.assertEqual("unknown", binding["revision"])
                    self.assertEqual(carrier.stem, binding["identifier"])
                    self.assertEqual(carrier.relative_to(self.root).as_posix(), binding["carrier"])
                    self.assertEqual(generate_project_graph_state.sha(carrier), binding["sha256"])

    def test_canonical_projection_bytes_do_not_depend_on_executed_generator_carrier(self) -> None:
        config = generate_project_graph_state.configuration()
        bindings = generate_project_graph_state.settings_bindings()
        modes = config["authority_modes"]
        assert isinstance(modes, dict)
        rows = generate_project_graph_state.bind_scope_unit_structure(
            self.fixture_scope_units()
        )
        source_atoms = generate_project_graph_state.active_source_atoms()
        # The sealed Unit workspace deliberately has no live installed-tools
        # selector.  Materialize the smallest schema-valid installed package
        # in this already gitless disposable Project, then reopen it through
        # the verified reader rather than depending on host runtime state.
        import framework_installation

        tools_runtime = self.root / ".caprmedio_runtime" / "tools"
        tools = tools_runtime / "releases" / "pending" / "TOOLS"
        installed = tools / "GENERATE_PROJECT_GRAPH_STATE" / "generate_project_graph_state.py"
        installed.parent.mkdir(parents=True)
        installed.write_bytes(generate_project_graph_state.CANONICAL_GENERATOR.read_bytes())
        installed.chmod(generate_project_graph_state.CANONICAL_GENERATOR.stat().st_mode & 0o777)
        for relative in (
            "INSTALL_TOOLS/install_tools.py",
            "COMMIT_TRIGGER/commit_trigger.py",
            "START_BACKGROUND_SERVICES/start_background_services.py",
        ):
            carrier = tools / relative
            carrier.parent.mkdir(parents=True, exist_ok=True)
            carrier.write_text("# sealed fixture carrier\n", encoding="utf-8")
        row = {
            "path": "TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py",
            "sha256": generate_project_graph_state.sha(installed),
            "mode": installed.stat().st_mode & 0o777,
        }
        release = framework_installation.digest(
            {
                "schema_version": framework_installation.SCHEMA_VERSION,
                "package": framework_installation.PACKAGE,
                "files": [row],
            }
        )
        release_root = tools_runtime / "releases" / release
        release_root.mkdir()
        tools.rename(release_root / "TOOLS")
        (tools_runtime / "current.toml").write_text(
            framework_installation._render_current_manifest(release), encoding="utf-8"
        )
        (release_root / "manifest.toml").write_text(
            framework_installation._render_release_manifest(release, [row]), encoding="utf-8"
        )
        with mock.patch(
            "framework_installation.resolve_repository",
            return_value=self.root,
        ):
            installation = generate_project_graph_state.installation_status(self.root)
        self.assertTrue(installation["verified"])
        installed = self.root / str(installation["package_root"]) / "GENERATE_PROJECT_GRAPH_STATE" / "generate_project_graph_state.py"
        self.assertTrue(installed.is_file())
        source_payload = generate_project_graph_state.project_scope_unit_graph(
            generate_project_graph_state.source_updated_at(bindings, source_atoms),
            config,
            bindings,
            rows,
            source_atoms,
            generate_project_graph_state.CANONICAL_GENERATOR,
        )
        installed_payload = generate_project_graph_state.project_scope_unit_graph(
            generate_project_graph_state.source_updated_at(bindings, source_atoms),
            config,
            bindings,
            rows,
            source_atoms,
            installed,
        )
        self.assertEqual(
            generate_project_graph_state.canonical_projection_bytes(source_payload),
            generate_project_graph_state.canonical_projection_bytes(installed_payload),
        )
        self.assertIn(
            'canonical_generator = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py"',
            installed_payload,
        )
        self.assertIn(
            f'executed_generator = "{generate_project_graph_state.project_relative(installed)}"',
            installed_payload,
        )

    def test_identical_scope_frontier_serializes_identically(self) -> None:
        self.fixture_scope_units()

        first = generate_project_graph_state.scope_units(self.control, self.root, self.modes)
        second = generate_project_graph_state.scope_units(self.control, self.root, self.modes)

        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
