"""Retained declaration evidence survives elapsed budgets, never source drift."""

import copy
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from GENERATE_PROJECT_GRAPH_STATE import generate_project_graph_state as graph
from WORKFLOW_OPERATIONS.PROJECT_STRUCTURE import project_structure as structure
from project_selection import ProjectSelectionError, resolve_project


class DeclarationBoundaryRetentionTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp/tests/declaration-retention"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname="caprmedio"\nkey="test"\nrepository_slug="test"\n'
            '[paths]\ncontrol_root=".caprmedio_caprmedio"\n'
            '[artifacts.identity]\nproject_prefix="CA"\n[authority_modes]\ndefault="casual"\n'
        )
        self.source = self.control / "project_structure.toml"
        self.source.write_text(structure.serialize_project_structure([self.row("PARENT")]))

    def row(self, name, *, parent="PROJECT", level=1):
        return {"scope_unit_name": name, "parent": parent, "scope_unit_type": "Unordered",
                "scope_unit_label": "FEATURE", "structural_level": level,
                "navigational_order_number": 0, "authority_path": f".caprmedio_caprmedio/{name}",
                "delivery_path": "vendor/.caprmedio_empty/new"}

    def foreign_marker(self):
        foreign = self.root / "vendor/.caprmedio_empty"
        foreign.mkdir(parents=True, exist_ok=True)
        (foreign / "caprmedio_project_settings.toml").write_text(
            '[project]\nname="caprmedio"\n[paths]\ncontrol_root=".caprmedio_empty"\n'
        )

    def parameters(self):
        return {"operation": "Create", "expected_toml_revision": hashlib.sha256(self.source.read_bytes()).hexdigest(),
                "declaration": self.row("CHILD", parent="PARENT", level=2), "reference_frontier": [],
                "goal_coverage_disposition": {"state": "missing", "parent": "PARENT", "gap_ref": "GAP",
                                              "authorized_disposition": "report-only"},
                "preservation_disposition": {"preserved": []},
                "recovery_disposition": {"authorized": True, "boundary": "toml-and-listed-references"}}

    def test_selection_recheck_gets_fresh_budget_but_keeps_original_absence(self):
        selected = resolve_project(self.root)
        proof = selected._boundary_proof
        captured = dict(proof.marker_pins)
        proof._reader.started -= max(61, proof._reader.limits["timeout_seconds"] + 1)
        selected._revalidate_boundary()
        self.foreign_marker()
        with self.assertRaises(ProjectSelectionError):
            selected._revalidate_boundary()
        self.assertEqual(dict(proof.marker_pins), captured)

    def test_graph_copy_and_bind_recheck_original_absence(self):
        rows = graph.scope_units(self.control, self.root, {"default": "casual"})
        copied = copy.deepcopy(rows)
        self.assertIs(copied._boundary_proof, rows._boundary_proof)
        self.foreign_marker()
        with patch.multiple(graph, ROOT=self.root, CONTROL=self.control):
            with self.assertRaises(SystemExit):
                graph.bind_scope_unit_structure(copied)

    def test_queue_rechecks_first_proposal_before_later_phase_and_effect(self):
        handlers = structure.queue_action_handlers(self.root)
        context = {"workflow_run_id": "boundary-test", "workflow_definition_id": "CA-O-015",
                   "route": "create_scope_unit", "parameters": self.parameters(), "sealed_outer_admission": True}
        self.assertEqual(handlers["CA-O-012"](context)["result"], "prepared")
        before = self.source.read_bytes()
        self.foreign_marker()
        for action in ("CA-O-005", "CA-O-013", "CA-O-014"):
            self.assertEqual(handlers[action](copy.deepcopy(context))["result"], "conflict")
        self.assertEqual(self.source.read_bytes(), before)

    def test_post_declaration_boundary_change_reports_partial_not_completed(self):
        result = structure.apply_scope_unit_action(self.root, self.parameters(), after_declaration=self.foreign_marker)
        self.assertEqual(result["state"], "partial")
        self.assertEqual([effect["path"] for effect in result["actual_effects"]], [structure.STRUCTURE_RELATIVE_PATH])
        self.assertIn("Declaration boundary evidence changed", result["validation_errors"][0])

    def test_reconstructed_late_handlers_cannot_capture_replacement_proof(self):
        context = {"workflow_run_id": "lost-proof", "workflow_definition_id": "CA-O-015",
                   "route": "create_scope_unit", "parameters": self.parameters(), "sealed_outer_admission": True}
        self.assertEqual(structure.queue_action_handlers(self.root)["CA-O-012"](context)["result"], "prepared")
        handlers = structure.queue_action_handlers(self.root)
        before = self.source.read_bytes()
        for action in ("CA-O-005", "CA-O-013", "CA-O-014"):
            result = handlers[action](copy.deepcopy(context))
            self.assertEqual(result["result"], "conflict")
            self.assertIn("retained proposal", result["native_result"]["validation_errors"][0])
        self.assertEqual(self.source.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
