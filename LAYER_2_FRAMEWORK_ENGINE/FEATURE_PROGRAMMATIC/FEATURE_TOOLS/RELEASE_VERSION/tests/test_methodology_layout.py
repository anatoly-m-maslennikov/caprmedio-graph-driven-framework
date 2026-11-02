from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from scope_declaration_test_support import write_scope_unit_declarations  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import methodology_layout  # noqa: E402


class LayoutTests(unittest.TestCase):
    def _project(self):
        root = Path(tempfile.mkdtemp(prefix="release-methodology-layout-", dir=tempfile.gettempdir()))
        control = root / ".caprmedio_demo"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "demo"\n[paths]\ncontrol_root = ".caprmedio_demo"\n', encoding="utf-8",
        )
        rows = (
            {"scope_unit_name": "FRAMEWORK_METHODOLOGY", "scope_unit_type": "Unordered"},
            {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "FRAMEWORK_METHODOLOGY", "scope_unit_type": "Unordered"},
            {"scope_unit_name": "APPLICABLE_METHODOLOGY", "parent": "FRAMEWORK_METHODOLOGY", "scope_unit_type": "Unordered"},
        )
        return root, write_scope_unit_declarations(root, rows, control_root=control)

    def test_current_declarations_supply_all_release_places(self):
        root, rows = self._project()
        layout = methodology_layout.resolve_methodology_layout(root)
        self.assertEqual(rows["METHODOLOGY_SOURCES"]["authority_path"].relative_to(root).as_posix(), layout.source_root)
        self.assertEqual("FRAMEWORK_METHODOLOGY", layout.product_root)
        self.assertEqual("FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES", layout.source_copy_root)
        self.assertEqual("FRAMEWORK_METHODOLOGY/APPLICABLE_METHODOLOGY", layout.applicable_root)
        self.assertEqual(".caprmedio_demo", layout.control_root)
        self.assertEqual(".caprmedio_demo/000_CAPRMEDIO_framework", layout.installed_root)
        self.assertEqual(64, len(layout.declaration_sha256))

    def test_symlinked_source_ancestor_is_refused(self):
        root, rows = self._project()
        target = root / "alias-target"
        target.mkdir()
        source = rows["METHODOLOGY_SOURCES"]["authority_path"]
        source.parent.mkdir(parents=True, exist_ok=True)
        source.symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "unsafe"):
            methodology_layout.resolve_methodology_layout(root)


if __name__ == "__main__":
    unittest.main()
