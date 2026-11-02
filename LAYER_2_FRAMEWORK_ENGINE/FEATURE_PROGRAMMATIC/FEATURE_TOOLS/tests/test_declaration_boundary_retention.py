"""Retained declaration evidence survives elapsed budgets, never source drift."""

import copy
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from GENERATE_PROJECT_GRAPH_STATE import generate_project_graph_state as graph
from project_selection import ProjectSelectionError, resolve_project
from scope_declaration_test_support import write_scope_unit_declarations


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
        self.declarations = write_scope_unit_declarations(
            self.root,
            ({
                "scope_unit_name": "PARENT",
                "parent": "PROJECT",
                "scope_unit_type": "Unordered",
                "scope_unit_label": "FEATURE",
            },),
            control_root=self.control,
        )

    def foreign_marker(self):
        foreign = self.declarations["PARENT"]["delivery_path"]
        foreign.mkdir(parents=True, exist_ok=True)
        (foreign / "caprmedio_project_settings.toml").write_text(
            '[project]\nname="caprmedio"\n[paths]\ncontrol_root=".caprmedio_empty"\n'
        )

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
        self.assertEqual(copied._declaration_digest, rows._declaration_digest)
        declaration = self.declarations["PARENT"]["declaration_path"]
        declaration.write_text(declaration.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with patch.multiple(graph, ROOT=self.root, CONTROL=self.control):
            with self.assertRaises(SystemExit):
                graph.bind_scope_unit_structure(copied)


if __name__ == "__main__":
    unittest.main()
