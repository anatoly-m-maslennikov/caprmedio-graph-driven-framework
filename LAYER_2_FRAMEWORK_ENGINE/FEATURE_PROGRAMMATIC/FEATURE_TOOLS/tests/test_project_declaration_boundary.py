"""Author controls for private, observed declaration boundary evidence."""

from __future__ import annotations

import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from project_selection import ProjectSelectionError, _declaration_boundary_proof
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


class DeclarationBoundaryAuthorTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.control = ".caprmedio_own"
        self.settings = self.marker(self.control)

    def marker(self, relative, name="own", declared=None):
        path = self.root / relative / "caprmedio_project_settings.toml"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f'[project]\nname="{name}"\n[paths]\ncontrol_root="{declared or path.parent.name}"\n')
        return path

    def proof(self, authority="authority", delivery="delivery", **kwargs):
        return _declaration_boundary_proof(self.root, self.control,
            [{"authority_path": authority, "delivery_path": delivery}], **kwargs)

    def test_owning_absent_and_lookalike_paths_are_effect_free(self):
        (self.root / ".caprmedio_lookalike").mkdir()
        before = self.settings.read_bytes()
        proof = self.proof(f"{self.control}/units", ".caprmedio_lookalike/delivery")
        self.assertEqual(proof.marker_pins[f"{self.control}/caprmedio_project_settings.toml"],
                         hashlib.sha256(before).hexdigest())
        self.assertIsNone(proof.marker_pins[".caprmedio_lookalike/caprmedio_project_settings.toml"])
        proof.revalidate()
        self.assertEqual(self.settings.read_bytes(), before)
        with self.assertRaises(TypeError):
            proof.marker_pins["changed"] = None

    def test_foreign_same_name_control_and_descendants_refuse_both_fields(self):
        self.marker("vendor/.caprmedio_foreign")
        for field in ("authority", "delivery"):
            for path in ("vendor/.caprmedio_foreign", "vendor/.caprmedio_foreign/unit"):
                with self.subTest(field=field, path=path), self.assertRaisesRegex(ProjectSelectionError, "another Project"):
                    self.proof(**{field: path})

    def test_foreign_project_directory_does_not_forbid_ordinary_sibling_delivery(self):
        self.marker("vendor/.caprmedio_foreign", name="other")
        self.proof("vendor/source", "vendor/delivery").revalidate()

    def test_malformed_and_contradictory_markers_refuse(self):
        path = self.marker("vendor/.caprmedio_foreign")
        for raw in (b"[project\n", b'[project]\nname=""\n[paths]\ncontrol_root=".caprmedio_foreign"\n',
                    b'[project]\nname="other"\n[paths]\ncontrol_root=".caprmedio_different"\n'):
            path.write_bytes(raw)
            with self.subTest(raw=raw), self.assertRaises(ProjectSelectionError):
                self.proof("vendor/.caprmedio_foreign/unit")

    def test_marker_and_path_symlinks_refuse(self):
        directory = self.root / "vendor/.caprmedio_foreign"
        directory.mkdir(parents=True)
        link = directory / "caprmedio_project_settings.toml"
        link.symlink_to(self.settings)
        with self.assertRaises(ProjectSelectionError):
            self.proof("vendor/.caprmedio_foreign")
        link.unlink()
        shortcut = self.root / "shortcut"
        shortcut.symlink_to(self.settings.parent, target_is_directory=True)
        with self.assertRaises(ProjectSelectionError):
            self.proof("shortcut/unit")

    def test_absent_marker_introduction_is_stale_without_resealing(self):
        proof = self.proof("vendor/.caprmedio_lookalike/unit")
        before = dict(proof.marker_pins)
        self.marker("vendor/.caprmedio_lookalike", name="foreign")
        with self.assertRaisesRegex(ProjectSelectionError, "changed"):
            proof.revalidate()
        self.assertEqual(dict(proof.marker_pins), before)

    def test_own_settings_change_and_removal_are_stale(self):
        proof = self.proof()
        original = self.settings.read_bytes()
        self.settings.write_bytes(original + b"\n# changed\n")
        with self.assertRaisesRegex(ProjectSelectionError, "changed"):
            proof.revalidate()
        self.settings.write_bytes(original)
        proof.revalidate()
        self.settings.unlink()
        with self.assertRaisesRegex(ProjectSelectionError, "disappeared"):
            proof.revalidate()

    def test_ordinary_materialization_does_not_change_marker_absence(self):
        proof = self.proof("missing/ordinary", "missing/delivery")
        (self.root / "missing/ordinary").mkdir(parents=True)
        (self.root / "missing/delivery").mkdir()
        proof.revalidate()

    def test_invalid_paths_and_non_directory_paths_refuse(self):
        file_path = self.root / "ordinary-file"
        file_path.write_bytes(b"not a directory")
        for path in ("../outside", "/absolute", "a/../b", "a\\b", ".", "ordinary-file"):
            with self.subTest(path=path), self.assertRaises(ProjectSelectionError):
                self.proof(path)

    def test_provided_reader_does_not_replace_a_previous_source_pin(self):
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        reader.read(self.settings)
        original = reader.fingerprints[str(self.settings)]
        self.settings.write_bytes(self.settings.read_bytes() + b"\n# drift\n")
        with self.assertRaisesRegex(ProjectSelectionError, "changed"):
            self.proof(reader=reader)
        self.assertEqual(reader.fingerprints[str(self.settings)], original)


if __name__ == "__main__":
    unittest.main()
