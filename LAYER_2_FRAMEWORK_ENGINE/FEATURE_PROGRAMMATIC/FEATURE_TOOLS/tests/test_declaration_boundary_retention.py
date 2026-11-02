"""Retained declaration evidence survives elapsed budgets, never source drift."""

from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

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


if __name__ == "__main__":
    unittest.main()
