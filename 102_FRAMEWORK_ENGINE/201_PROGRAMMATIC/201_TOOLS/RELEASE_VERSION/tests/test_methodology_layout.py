from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import methodology_layout


class LayoutTests(unittest.TestCase):
    def test_current_registry_supplies_all_release_places(self):
        with tempfile.TemporaryDirectory(dir="/private/tmp", ignore_cleanup_errors=True) as directory:
            root = Path(directory)
            control = Path(".caprmedio_demo")
            (root / control).mkdir()
            registry = root / control / "project_structure.toml"
            registry.write_text('''[[scope_units]]
scope_unit_name = "FRAMEWORK_METHODOLOGY"
delivery_path = "101_FRAMEWORK_METHODOLOGY"
[[scope_units]]
scope_unit_name = "METHODOLOGY_SOURCES"
parent = "FRAMEWORK_METHODOLOGY"
authority_path = ".caprmedio_demo/authoring/sources"
delivery_path = "101_FRAMEWORK_METHODOLOGY/sources"
[[scope_units]]
scope_unit_name = "APPLICABLE_METHODOLOGY"
parent = "FRAMEWORK_METHODOLOGY"
delivery_path = "101_FRAMEWORK_METHODOLOGY/applicable_methodology"
''')
            with patch.object(methodology_layout, "configured_control_root", return_value=control):
                layout = methodology_layout.resolve_methodology_layout(root)
            self.assertEqual(".caprmedio_demo/authoring/sources", layout.source_root)
            self.assertEqual("101_FRAMEWORK_METHODOLOGY/sources", layout.source_copy_root)
            self.assertEqual(".caprmedio_demo/000_CAPRMEDIO_framework", layout.installed_root)
            self.assertEqual(64, len(layout.structure_sha256))


if __name__ == "__main__":
    unittest.main()
