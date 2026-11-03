from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
if str(TOOLS) not in sys.path:
    sys.path.insert(0, str(TOOLS))

from scope_declaration_render import render_scope_declaration
from scope_declaration_test_support import write_scope_unit_declarations
from scope_unit_declarations import read_scope_unit_declarations


class ScopeDeclarationRenderTest(unittest.TestCase):
    def test_renderer_namespaces_metadata_but_keeps_claims_local(self) -> None:
        rendered = render_scope_declaration(
            name="CHILD", project_name="caprmedio", atom_id="CA-R-1", updated_at="now",
            scope_id="SU-1", parent="PROJECT",
        )

        self.assertIn('active: "CAPRMEDIO_STRUCTURE <+ Scope Unit//CHILD"', rendered)
        self.assertIn("passive: []", rendered)
        self.assertNotIn("CAPRMEDIO", rendered.split("## Claim", 1)[1])

    def test_renderer_keeps_other_projects_on_bare_metadata_subjects(self) -> None:
        rendered = render_scope_declaration(
            name="CHILD", project_name="demo", atom_id="CA-R-1", updated_at="now",
            scope_id="SU-1", parent="PROJECT",
        )

        self.assertIn('active: "Scope Unit//CHILD"', rendered)
        self.assertNotIn("CAPRMEDIO", rendered)

    def test_renderer_uses_only_the_conditional_order_number(self) -> None:
        rendered = render_scope_declaration(
            name='CHILD"X', project_name="demo", atom_id="CA-R-1", updated_at="now",
            scope_id="SU-1", label="FEATURE", ordered=True, order_number=True, parent="PROJECT",
        )
        self.assertIn('Scope Unit//CHILD"X.ID == "SU-1"', rendered)
        self.assertIn("order.ordered == true", rendered)
        self.assertNotIn("order.number", rendered)
        self.assertIn("((IS_CONTAINED_BY)) Project//demo", rendered)

    def test_materializer_places_root_and_child_at_parent_authority(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            (control / "caprmedio_project_settings.toml").write_text("[project]\nname = \"demo\"\n", encoding="utf-8")
            rows = write_scope_unit_declarations(root, ({
                "scope_unit_name": "CHILD", "parent": "PROJECT", "scope_unit_type": "Ordered",
                "scope_unit_label": "FEATURE", "local_order": 2,
            },))
            self.assertTrue(rows["demo"]["declaration_path"].is_file())
            self.assertTrue(rows["CHILD"]["declaration_path"].is_file())
            self.assertEqual(rows["demo"]["declaration_path"].parent, control)
            self.assertEqual(rows["CHILD"]["declaration_path"].parent, control / "04_requirement")
            self.assertIn("TEST-SU-1_FEATURE_2_CHILD", str(rows["CHILD"]["authority_path"]))
            self.assertNotIn("TEST-SU-1", str(rows["CHILD"]["delivery_path"]))
            self.assertEqual(set(read_scope_unit_declarations(root, control.name).by_name), {"demo", "CHILD"})


if __name__ == "__main__":
    unittest.main()
