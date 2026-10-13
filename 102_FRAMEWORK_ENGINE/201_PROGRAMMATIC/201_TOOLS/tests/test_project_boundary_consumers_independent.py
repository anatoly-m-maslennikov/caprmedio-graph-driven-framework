"""Actual boundary consumers in isolated fixtures; no public/runtime activation."""

from pathlib import Path
import copy
import sys
import tomllib
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "VALIDATE_ATOMS/tests")]
sys.path.insert(0, str(TOOLS / "WORKFLOW_OPERATIONS/PROJECT_STRUCTURE/tests"))

import test_project_authority_boundary_independent as boundaries
import test_proposed_carrier_admission_regressions as carriers
import test_connector_independent_contract as contract_fixtures
import test_connector_scope_parsing as scope_inputs
import test_project_structure as structure_fixtures
from connector_bindings import ConnectorBindings, capture_source
from connector_scope_parsing import validate_scope_request
from connector_scope_reading import execute_scope_request
from GENERATE_PROJECT_GRAPH_STATE import generate_project_graph_state as graph
from WORKFLOW_OPERATIONS.PROJECT_STRUCTURE import project_structure as structure
from project_selection import ProjectSelectionError, bind_selection, resolve_project
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier as admission


class StructureAndGraphBoundaryIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = boundaries.DeclarationBoundaryHelperIndependentTests()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        control = self.fixture.root / ".caprmedio_caprmedio"
        self.fixture.control.rename(control)
        self.fixture.control = control
        self.fixture.structure = control / boundaries.selection.STRUCTURE_FILENAME
        self.fixture.marker(control, name="shared-name")
        marker = self.fixture.control / boundaries.selection.SETTINGS_FILENAME
        marker.write_text(marker.read_text().replace('[project]\n', '[project]\nkey = "fixture"\nrepository_slug = "fixture"\n')
                          + '\n[authority_modes]\ndefault = "casual"\n[artifacts.identity]\nproject_prefix = "CA"\n')

    def test_real_structure_normalization_and_graph_delivery_binding_reject_both_foreign_fields(self):
        for field in ("authority_path", "delivery_path"):
            with self.subTest(field=field):
                self.fixture.declare(field, "vendor/.caprmedio_other/new")
                row = tomllib.loads(self.fixture.structure.read_text())["scope_units"][0]
                marker = self.fixture.root / "vendor/.caprmedio_other/caprmedio_project_settings.toml"
                if marker.exists():
                    marker.unlink()
                self.assertEqual(structure._normalise_declaration(row, self.fixture.root), row)
                self.assertIn(row["authority_path"], graph._delivery_bindings(self.fixture.control, self.fixture.root)[0])
                self.fixture.marker(marker.parent, name="shared-name")
                before = self.fixture.snapshot()
                with self.subTest(consumer="Structure"):
                    with self.assertRaises((structure.StructuralConflict, ProjectSelectionError)):
                        structure._normalise_declaration(row, self.fixture.root)
                with self.subTest(consumer="Graph"):
                    with self.assertRaises((SystemExit, ProjectSelectionError)):
                        graph._delivery_bindings(self.fixture.control, self.fixture.root)
                self.assertEqual(self.fixture.snapshot(), before)

    def test_graph_rows_retain_original_marker_pins_through_deepcopy_and_binding(self):
        self.fixture.declare("delivery_path", "vendor/.caprmedio_empty/new")
        rows = graph.scope_units(self.fixture.control, self.fixture.root, {"default": "casual"})
        retained = copy.deepcopy(rows)
        original_pins = dict(rows._boundary_proof.marker_pins)
        settings = self.fixture.control / boundaries.selection.SETTINGS_FILENAME
        settings.write_bytes(settings.read_bytes() + b"\n# externally changed Settings\n")
        before = self.fixture.snapshot()
        with patch.multiple(graph, ROOT=self.fixture.root, CONTROL=self.fixture.control):
            with self.assertRaises(SystemExit):
                graph.bind_scope_unit_structure(retained)
        self.assertEqual(dict(retained._boundary_proof.marker_pins), original_pins)
        self.assertEqual(self.fixture.snapshot(), before)


class StructureCandidateBoundaryIndependentTests(unittest.TestCase):
    def test_reconstructed_handlers_cannot_capture_a_proof_in_late_phases(self):
        fixture = structure_fixtures.ProjectStructureActions()
        self.addCleanup(fixture.doCleanups)
        fixture.setUp()
        marker = fixture.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        context = {
            "workflow_run_id": "independent-reconstruction", "workflow_definition_id": "CA-O-015",
            "route": "create_scope_unit", "sealed_outer_admission": True,
            "parameters": fixture.parameters("Create", declaration=structure_fixtures.declaration("CHILD", parent="PARENT", level=2)),
        }
        handlers = structure_fixtures.project_structure.queue_action_handlers(fixture.root)
        self.assertEqual(handlers["CA-O-012"](context)["result"], "prepared")
        for drift in (False, True):
            with self.subTest(drift=drift):
                if drift:
                    marker.write_bytes(marker.read_bytes() + b"\n# external Settings drift\n")
                before = carriers.snapshot(fixture.root)
                reconstructed = structure_fixtures.project_structure.queue_action_handlers(fixture.root)
                for action in ("CA-O-005", "CA-O-013", "CA-O-014"):
                    with self.subTest(action=action):
                        result = reconstructed[action](context)
                        self.assertEqual(result["result"], "conflict")
                        self.assertEqual(result["effect_refs"], [])
                self.assertEqual(carriers.snapshot(fixture.root), before)

    def test_prepared_candidate_does_not_reseal_settings_drift_before_check(self):
        fixture = structure_fixtures.ProjectStructureActions()
        self.addCleanup(fixture.doCleanups)
        fixture.setUp()
        marker = fixture.root / ".caprmedio_caprmedio/caprmedio_project_settings.toml"
        context = {
            "workflow_run_id": "independent-boundary", "workflow_definition_id": "CA-O-015",
            "route": "create_scope_unit",
            "parameters": fixture.parameters("Create", declaration=structure_fixtures.declaration("CHILD", parent="PARENT", level=2)),
        }
        handlers = structure_fixtures.project_structure.queue_action_handlers(fixture.root)
        self.assertEqual(handlers["CA-O-012"](context)["result"], "prepared")
        marker.write_bytes(marker.read_bytes() + b"\n# external Settings drift\n")
        before = carriers.snapshot(fixture.root)
        result = handlers["CA-O-005"](context)
        self.assertEqual(result["result"], "conflict")
        self.assertEqual(result["effect_refs"], [])
        self.assertEqual(carriers.snapshot(fixture.root), before)


class CompleteCarrierBoundaryIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = carriers.ProposedCarrierAdmissionRegressions()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()

    def test_selected_absence_is_not_resealed_before_context_or_complete_carrier_validation(self):
        for field in ("authority_path", "delivery_path"):
            with self.subTest(field=field):
                root = self.fixture.root / field
                selected = self.fixture.project(root=root)
                original = selected.structure_path.read_text()
                other = "delivery_path" if field == "authority_path" else "authority_path"
                selected.structure_path.write_text(original + (
                    '\n[[scope_units]]\nscope_unit_name = "EXTRA"\nparent = "PROJECT"\n'
                    'scope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\n'
                    'structural_level = 1\nnavigational_order_number = 1\n'
                    f'{field} = "vendor/.caprmedio_other/new"\n{other} = "ordinary/extra"\n'
                ))
                selected = resolve_project(root, selected.control_relative)
                with bind_selection(selected):
                    context = admission.source_context_from_project(root)
                    result = admission.validate_proposed_carrier(
                        self.fixture.metadata(), carriers.PLAN_BODY, context, Path("03_plan/plan.md"),
                    )
                    self.assertEqual((result["findings"], result["gaps"]), ([], []))
                    foreign = root / "vendor/.caprmedio_other"
                    foreign.mkdir(parents=True)
                    (foreign / boundaries.selection.SETTINGS_FILENAME).write_text(
                        '[project]\nname = "amber"\n[paths]\ncontrol_root = ".caprmedio_other"\n'
                    )
                    before = carriers.snapshot(root)
                    with self.subTest(consumer="Source context"):
                        with self.assertRaises((admission.ProposedCarrierError, ProjectSelectionError)):
                            admission.source_context_from_project(root)
                    with self.subTest(consumer="Complete carrier"):
                        with self.assertRaises((admission.ProposedCarrierError, ProjectSelectionError)):
                            admission.validate_proposed_carrier(
                                self.fixture.metadata(), carriers.PLAN_BODY, context, Path("03_plan/plan.md"),
                            )
                    self.assertEqual(carriers.snapshot(root), before)


class ScopeReaderBoundaryIndependentTests(unittest.TestCase):
    """Real selected admission and Scope reader, inside the existing isolated fixture."""

    def setUp(self):
        self.contract = contract_fixtures.IndependentConnectorContractTests()
        self.addCleanup(self.contract.doCleanups)
        self.fixture, self.request, self.original_bindings, self.settings, self.structure = self.contract.scope_fixture()

    def bindings(self, validator=validate_scope_request):
        sources = tuple(capture_source(self.fixture.root, path.relative_to(self.fixture.root))
                        for path in (self.settings, self.structure))
        return ConnectorBindings(
            self.original_bindings._admission, supported_operations={"read"}, supported_kinds={"Scope Unit"},
            validate_payload=validator, resolve_sources=lambda _: sources,
            authority_sources=self.fixture.authorities,
        )

    def run_request(self, bindings):
        return execute_scope_request(self.request, bindings=bindings, project_name="demo", source_view="current")

    def test_scope_reader_refuses_both_foreign_fields_without_effects(self):
        for field in ("authority_path", "delivery_path"):
            with self.subTest(field=field):
                values = scope_inputs.rows()
                values[0][field] = "vendor/.caprmedio_other/new"
                self.structure.write_text(scope_inputs.serialize_project_structure(values))
                bindings = self.bindings()
                marker = self.fixture.root / "vendor/.caprmedio_other/caprmedio_project_settings.toml"
                if marker.exists():
                    marker.unlink()
                self.assertEqual(self.run_request(bindings)["errors"], [])
                marker.parent.mkdir(parents=True, exist_ok=True)
                marker.write_text('[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_other"\n')
                before = self.contract.snapshot(self.fixture.root)
                result = self.run_request(bindings)
                self.assertTrue(result["errors"])
                self.assertEqual(result["effects"], [])
                self.assertEqual(self.contract.snapshot(self.fixture.root), before)

    def test_scope_reader_rechecks_absence_after_bound_permission_revalidation(self):
        values = scope_inputs.rows()
        values[0]["delivery_path"] = "vendor/.caprmedio_other/new"
        self.structure.write_text(scope_inputs.serialize_project_structure(values))
        calls = 0

        def introduce_marker(value):
            nonlocal calls
            validate_scope_request(value)
            calls += 1
            if calls == 2:
                marker = self.fixture.root / "vendor/.caprmedio_other/caprmedio_project_settings.toml"
                marker.parent.mkdir(parents=True)
                marker.write_text('[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_other"\n')

        result = self.run_request(self.bindings(introduce_marker))
        self.assertGreaterEqual(calls, 2)
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"], [])
        self.assertIsNone(result["data"])


if __name__ == "__main__":
    unittest.main()
