import importlib.util
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import yaml

PATH = Path(__file__).with_name("generate_subject_projections.py")
spec = importlib.util.spec_from_file_location("subject_projection_generator", PATH)
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)
from scope_declaration_parse import ScopeDeclarationError


def doc(number=20, form="Primary Entities Tree", scope="Project//caprmedio"):
    return {"projection_id": f"CA-PROJ-{number:03d}", "form": form, "scope_unit": scope,
            "path": f"out/CA-PROJ-{number:03d}-view.md"}


def write_projection(root, document, *, selection="Current first", atoms=None):
    path = root / document["path"]
    path.parent.mkdir(exist_ok=True)
    metadata = {"projection_id": document["projection_id"], "form": document["form"],
                "scope_unit": document["scope_unit"],
                "source": {"named_selection": f"Named Selection//{selection}",
                           "atoms": ["CA-R-2640@1"] if atoms is None else atoms}}
    path.write_text("---\n" + yaml.safe_dump(metadata) + "---\n")
    return path


class ProjectionIdentityTests(unittest.TestCase):
    def test_current_root_resolves_and_project_is_a_scope_unit(self):
        reference, _ = generator.project_root_binding()
        self.assertEqual(reference, "Project//caprmedio")
        declaration = next((generator.ROOT / ".caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement").glob("CA-R-2524-*.md"))
        self.assertIn("Project ((NARROWER_THAN)) Scope Unit", declaration.read_text())

    def test_distinct_forms(self):
        names = [name for _, name, _ in generator.VIEWS]
        self.assertEqual(len(names), 7)
        self.assertEqual(len(set(names)), 7)
        self.assertEqual(len({(name, "Project//caprmedio") for name in names}), 7)

    def test_selection_is_validated_but_not_identity(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(generator, "ROOT", root), patch.object(generator, "OUTPUT", root / "out"):
                document = doc()
                path = write_projection(root, document, selection="changed")
                self.assertEqual(generator.output_predecessors([document])[path], path.read_bytes())
                write_projection(root, document, atoms=["CA-R-2640"])
                with self.assertRaisesRegex(ValueError, "source selection"):
                    generator.output_predecessors([document])

    def test_reject_duplicate_identity_and_registry_collision(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(generator, "ROOT", root), patch.object(generator, "OUTPUT", root / "out"):
                (root / "out").mkdir()
                with self.assertRaisesRegex(ValueError, "one-to-one"):
                    generator.output_predecessors([doc(), doc(21)])
                write_projection(root, doc(99))
                with self.assertRaisesRegex(ValueError, "another ID"):
                    generator.output_predecessors([doc()])

    def test_reject_old_carrier_and_symlink(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(generator, "ROOT", root), patch.object(generator, "OUTPUT", root / "out"):
                out = root / "out"
                out.mkdir()
                old = out / "CA-PROJ-020-old.md"
                old.write_text("---\nprojection_id: CA-PROJ-020\nform: Map\n---\n")
                with self.assertRaisesRegex(ValueError, "different carrier"):
                    generator.output_predecessors([doc()])
                old.unlink()
                (out / "CA-PROJ-020-view.md").symlink_to(root / "missing")
                with self.assertRaisesRegex(ValueError, "Unsafe"):
                    generator.output_predecessors([doc()])

    def test_staged_filenames_use_verified_root_name_with_exact_case(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            packet = root / "packet"
            packet.mkdir()
            frontier = root / "frontier.json"
            frontier.write_text('{"operations": []}')
            with (patch.object(generator, "ROOT", root), patch.object(generator, "OUTPUT", root / "out"),
                  patch.object(generator, "PACKET", packet), patch.object(generator, "FRONTIER", frontier),
                  patch.object(generator, "project_root_binding", return_value=("Project//MixedCase", "digest")),
                  patch.object(generator, "read_sources", return_value=[]),
                  patch.object(generator, "select_model_subjects", return_value=([], [])),
                  patch.object(generator, "build_subject_projection_data", return_value={"entities": [], "coverage": {}}),
                  patch.object(generator, "build_subject_audits", return_value={}),
                  patch.object(generator, "render_primary_projection", return_value="# View\nBody"),
                  patch.object(generator, "render_subject_audit", return_value="# View\nBody"),
                  patch.object(generator, "current_timestamp", return_value="2026-11-04"),
                  patch.object(generator.sys, "argv", ["generator"])):
                generator.main()
            staged = list((packet / "staged").glob("*.md"))
            self.assertEqual(len(staged), 7)
            self.assertTrue(all(path.name.startswith(f"CA-PROJ-0{number}-MixedCase--")
                                for number, path in zip(range(20, 27), sorted(staged))))
            self.assertTrue(all(yaml.safe_load(path.read_text().split("---", 2)[1])["scope_unit"]
                                == "Project//MixedCase" for path in staged))

    def test_unadopted_declarations_block_publication(self):
        with tempfile.TemporaryDirectory() as temp:
            with patch.object(generator, "ROOT", Path(temp)):
                with self.assertRaisesRegex(ValueError, "Form Declaration unavailable"):
                    generator.check_model_authority([doc()])

    def test_frozen_profile_collision_and_incomplete_profile(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with patch.object(generator, "ROOT", root), patch.object(generator, "OUTPUT", root / "out"):
                frozen = write_projection(root, doc(14))
                with self.assertRaisesRegex(ValueError, "another ID"):
                    generator.output_predecessors([doc()])
                frozen.write_text("---\nprojection_id: CA-PROJ-014\nform: Map\n---\n")
                self.assertIsNone(generator.output_predecessors([doc()])[root / doc()["path"]])

    def test_actual_resolver_rejects_missing_and_duplicate_root(self):
        source = next((generator.ROOT / ".caprmedio_caprmedio").glob("CA-R-2640-*.md")).read_text()
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            control = root / ".caprmedio_caprmedio"
            control.mkdir()
            with patch.object(generator, "ROOT", root):
                with self.assertRaises(ScopeDeclarationError):
                    generator.project_root_binding()
                (control / "CA-R-2640-first.md").write_text(source)
                (control / "CA-R-2640-second.md").write_text(source)
                with self.assertRaises(ScopeDeclarationError):
                    generator.project_root_binding()

    def test_missing_or_ambiguous_root_fails_closed(self):
        with patch.object(generator, "read_scope_unit_declarations", side_effect=ValueError("missing or ambiguous root")):
            with self.assertRaisesRegex(ValueError, "missing or ambiguous"):
                generator.project_root_binding()
        result = SimpleNamespace(root=SimpleNamespace(is_root=False, name="caprmedio"), by_name={}, digest="x")
        with patch.object(generator, "read_scope_unit_declarations", return_value=result):
            with self.assertRaisesRegex(ValueError, "unresolved"):
                generator.project_root_binding()


if __name__ == "__main__":
    unittest.main()
