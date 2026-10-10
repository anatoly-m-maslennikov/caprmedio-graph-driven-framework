from pathlib import Path
import copy
import hashlib
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import methodology_layout


class LayoutTests(unittest.TestCase):
    @staticmethod
    def _rows():
        return [
            {"scope_unit_name": "FRAMEWORK_METHODOLOGY", "delivery_path": "101_FRAMEWORK_METHODOLOGY"},
            {"scope_unit_name": "METHODOLOGY_SOURCES", "parent": "FRAMEWORK_METHODOLOGY",
             "authority_path": ".caprmedio_demo/authoring/sources", "delivery_path": "101_FRAMEWORK_METHODOLOGY/sources"},
            {"scope_unit_name": "APPLICABLE_METHODOLOGY", "parent": "FRAMEWORK_METHODOLOGY",
             "delivery_path": "101_FRAMEWORK_METHODOLOGY/applicable_methodology"},
        ]

    @staticmethod
    def _project(rows):
        # Retain the disposable fixtures for terminal evidence; no cleanup
        # behavior substitutes for a resolver assertion.
        root = Path(tempfile.mkdtemp(prefix="release-methodology-layout-", dir="/private/tmp"))
        (root / ".caprmedio_caprmedio").mkdir()
        (root / ".caprmedio_caprmedio/caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_demo"\n', encoding="utf-8",
        )
        (root / ".caprmedio_demo").mkdir()
        registry = root / ".caprmedio_demo/project_structure.toml"
        registry.write_text("\n".join(
            "[[scope_units]]\n" + "\n".join(f'{key} = "{value}"' for key, value in row.items())
            for row in rows
        ) + "\n", encoding="utf-8")
        return root, registry

    def test_current_registry_supplies_all_release_places(self):
        root, registry = self._project(self._rows())
        layout = methodology_layout.resolve_methodology_layout(root)
        self.assertEqual(".caprmedio_demo/authoring/sources", layout.source_root)
        self.assertEqual("101_FRAMEWORK_METHODOLOGY", layout.product_root)
        self.assertEqual("101_FRAMEWORK_METHODOLOGY/sources", layout.source_copy_root)
        self.assertEqual("101_FRAMEWORK_METHODOLOGY/applicable_methodology", layout.applicable_root)
        self.assertEqual(".caprmedio_demo", layout.control_root)
        self.assertEqual(".caprmedio_demo/000_CAPRMEDIO_framework", layout.installed_root)
        self.assertEqual(hashlib.sha256(registry.read_bytes()).hexdigest(), layout.structure_sha256)

    def test_registered_source_inside_installed_folder_is_refused(self):
        rows = self._rows()
        rows[1]["authority_path"] = ".caprmedio_demo/000_CAPRMEDIO_framework/sources"
        root, _ = self._project(rows)
        with self.assertRaisesRegex(ValueError, "not installed Methodology"):
            methodology_layout.resolve_methodology_layout(root)

    def test_product_enclosing_authoring_source_is_refused(self):
        rows = self._rows()
        rows[0]["delivery_path"] = ".caprmedio_demo/authoring"
        rows[1]["delivery_path"] = ".caprmedio_demo/authoring/sources"
        rows[2]["delivery_path"] = ".caprmedio_demo/authoring/applicable_methodology"
        root, _ = self._project(rows)
        with self.assertRaisesRegex(ValueError, "must not enclose Project authority"):
            methodology_layout.resolve_methodology_layout(root)

    def test_each_missing_required_scope_row_is_refused(self):
        for index, row in enumerate(self._rows()):
            with self.subTest(scope=row["scope_unit_name"]):
                rows = self._rows()
                del rows[index]
                root, _ = self._project(rows)
                with self.assertRaisesRegex(ValueError, f'exactly one {row["scope_unit_name"]}'):
                    methodology_layout.resolve_methodology_layout(root)

    def test_each_duplicate_required_scope_row_is_refused(self):
        for row in self._rows():
            with self.subTest(scope=row["scope_unit_name"]):
                rows = self._rows() + [copy.deepcopy(row)]
                root, _ = self._project(rows)
                with self.assertRaisesRegex(ValueError, f'exactly one {row["scope_unit_name"]}'):
                    methodology_layout.resolve_methodology_layout(root)

    def test_mismatched_source_or_applicable_parent_is_refused(self):
        for index in (1, 2):
            with self.subTest(scope=self._rows()[index]["scope_unit_name"]):
                rows = self._rows()
                rows[index]["parent"] = "FRAMEWORK_ENGINE"
                root, _ = self._project(rows)
                with self.assertRaisesRegex(ValueError, "must belong to FRAMEWORK_METHODOLOGY"):
                    methodology_layout.resolve_methodology_layout(root)

    def test_symlinked_source_ancestor_is_refused(self):
        root, _ = self._project(self._rows())
        target = root / "alias-target"
        target.mkdir()
        (root / ".caprmedio_demo/authoring").symlink_to(target, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "must not traverse a symlink"):
            methodology_layout.resolve_methodology_layout(root)


if __name__ == "__main__":
    unittest.main()
