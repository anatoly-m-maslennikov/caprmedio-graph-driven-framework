"""Independent Settings-bound declaration checks; not public activation evidence."""

import os
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest

TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

import project_selection as selection


class DeclarationBoundaryHelperIndependentTests(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/project-boundary-independent"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=scratch, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.control = self.root / ".caprmedio_owner"
        self.control.mkdir()
        self.marker(self.control, name="shared-name")
        self.structure = self.control / selection.STRUCTURE_FILENAME
        self.declare()

    def marker(self, control, *, name="other", declared=None, raw=None):
        control.mkdir(parents=True, exist_ok=True)
        path = control / selection.SETTINGS_FILENAME
        path.write_text(raw if raw is not None else (
            f'[project]\nname = "{name}"\n[paths]\ncontrol_root = "{declared or control.name}"\n'
        ), encoding="utf-8")
        return path

    def declare(self, field="authority_path", value=".caprmedio_owner/unit"):
        paths = {"authority_path": ".caprmedio_owner/unit", "delivery_path": "delivery/unit"}
        paths[field] = value
        self.structure.write_text(
            'schema_version = 1\n[[scope_units]]\nscope_unit_name = "UNIT"\n'
            'parent = "PROJECT"\nscope_unit_type = "Unordered"\nscope_unit_label = "FEATURE"\n'
            'structural_level = 1\nnavigational_order_number = 1\n'
            + "".join(f'{key} = "{item}"\n' for key, item in paths.items()), encoding="utf-8",
        )

    def select(self):
        rows = tomllib.loads(self.structure.read_text())["scope_units"]
        return selection._declaration_boundary_proof(self.root, self.control.name, rows)

    def snapshot(self):
        return {path.relative_to(self.root).as_posix(): (path.read_bytes(), path.stat().st_mtime_ns)
                for path in self.root.rglob("*") if path.is_file() and not path.is_symlink()}

    def test_foreign_control_and_descendant_refuse_both_fields_even_same_name_without_structure(self):
        foreign = self.root / "vendor/.caprmedio_foreign"
        self.marker(foreign, name="shared-name")
        self.assertFalse((foreign / selection.STRUCTURE_FILENAME).exists())
        for field in ("authority_path", "delivery_path"):
            for tail in ("", "/unmaterialized/child"):
                with self.subTest(field=field, tail=tail):
                    self.declare(field, "vendor/.caprmedio_foreign" + tail)
                    before = self.snapshot()
                    with self.assertRaises(selection.ProjectSelectionError):
                        self.select()
                    self.assertEqual(self.snapshot(), before)

    def test_owning_paths_empty_lookalikes_and_absent_ordinary_paths_remain_valid(self):
        (self.root / "vendor/.caprmedio_empty").mkdir(parents=True)
        for field in ("authority_path", "delivery_path"):
            for value in (".caprmedio_owner", ".caprmedio_owner/new/unit", "vendor/.caprmedio_empty/new",
                          "missing/ordinary/unit", "vendor/.caprmedio_absent/new"):
                with self.subTest(field=field, value=value):
                    self.declare(field, value)
                    before = self.snapshot()
                    observed = self.select()
                    self.assertIsNotNone(observed)
                    self.assertEqual(self.snapshot(), before)

    def test_malformed_or_conflicting_settings_marker_is_not_an_empty_lookalike(self):
        foreign = self.root / "vendor/.caprmedio_foreign"
        for raw in ("[project\n", '[project]\nname=""\n[paths]\ncontrol_root=".caprmedio_foreign"\n',
                    '[project]\nname="other"\n[paths]\ncontrol_root=".caprmedio_wrong"\n'):
            self.marker(foreign, raw=raw)
            for field in ("authority_path", "delivery_path"):
                with self.subTest(field=field, raw=raw):
                    self.declare(field, "vendor/.caprmedio_foreign/unit")
                    with self.assertRaises(selection.ProjectSelectionError):
                        self.select()

    def test_symlinked_settings_or_control_path_refuses(self):
        foreign = self.root / "vendor/.caprmedio_foreign"
        marker = self.marker(foreign)
        raw = marker.read_bytes()
        marker.unlink()
        marker.symlink_to(self.control / selection.SETTINGS_FILENAME)
        for field in ("authority_path", "delivery_path"):
            self.declare(field, "vendor/.caprmedio_foreign/unit")
            with self.subTest(field=field), self.assertRaises(selection.ProjectSelectionError):
                self.select()
        marker.unlink()
        marker.write_bytes(raw)
        alias = self.root / "vendor/.caprmedio_alias"
        alias.symlink_to(foreign, target_is_directory=True)
        for field in ("authority_path", "delivery_path"):
            self.declare(field, "vendor/.caprmedio_alias/unit")
            with self.subTest(field=field), self.assertRaises(selection.ProjectSelectionError):
                self.select()

    def test_actual_unreadable_settings_marker_refuses(self):
        marker = self.marker(self.root / "vendor/.caprmedio_foreign")
        mode = marker.stat().st_mode
        marker.chmod(0)
        try:
            if os.access(marker, os.R_OK):
                self.skipTest("Host privileges bypass file mode; not evidence of unreadability refusal")
            for field in ("authority_path", "delivery_path"):
                self.declare(field, "vendor/.caprmedio_foreign/unit")
                with self.subTest(field=field), self.assertRaises(selection.ProjectSelectionError):
                    self.select()
        finally:
            marker.chmod(mode)


class DeclarationBoundaryProofCurrentnessIndependentTests(unittest.TestCase):
    # Currentness tests use the same real proof API, not mocked filesystem admission.
    setUp = DeclarationBoundaryHelperIndependentTests.setUp
    marker = DeclarationBoundaryHelperIndependentTests.marker
    declare = DeclarationBoundaryHelperIndependentTests.declare
    select = DeclarationBoundaryHelperIndependentTests.select

    def test_absent_marker_introduction_refuses_without_resealing(self):
        self.declare("delivery_path", "vendor/.caprmedio_empty/new")
        proof = self.select()
        absent = "vendor/.caprmedio_empty/" + selection.SETTINGS_FILENAME
        self.assertIsNone(proof.marker_pins[absent])
        original_pins = dict(proof.marker_pins)
        self.marker(self.root / "vendor/.caprmedio_empty")
        for _ in range(2):
            with self.assertRaises(selection.ProjectSelectionError):
                proof.revalidate()
        self.assertEqual(dict(proof.marker_pins), original_pins)

    def test_own_settings_change_or_removal_refuses_retained_proof(self):
        path = self.control / selection.SETTINGS_FILENAME
        original = path.read_bytes()
        for raw in (original.replace(b"shared-name", b"renamed"), None):
            proof = self.select()
            original_pins = dict(proof.marker_pins)
            if raw is None:
                path.unlink()
            else:
                path.write_bytes(raw)
            try:
                with self.subTest(missing=raw is None), self.assertRaises(selection.ProjectSelectionError):
                    proof.revalidate()
                self.assertEqual(dict(proof.marker_pins), original_pins)
            finally:
                path.write_bytes(original)

    def test_ordinary_directory_materialization_is_not_a_new_project_marker(self):
        self.declare("delivery_path", "ordinary/not-yet-materialized")
        proof = self.select()
        (self.root / "ordinary/not-yet-materialized").mkdir(parents=True)
        self.assertIsNone(proof.revalidate())
        with self.assertRaises(TypeError):
            proof.marker_pins["invented"] = None

    def test_elapsed_capture_reader_budget_does_not_expire_unchanged_marker_proof(self):
        self.declare("delivery_path", "vendor/.caprmedio_empty/new")
        reader = selection.ReadContext(roots=[str(self.root)], limits=dict(selection.CEILINGS))
        proof = selection._declaration_boundary_proof(
            self.root, self.control.name, tomllib.loads(self.structure.read_text())["scope_units"], reader=reader,
        )
        original_pins = dict(proof.marker_pins)
        # Exercise the budget mechanism without a minute-long sleep; Settings reads remain real.
        reader.started -= reader.limits["timeout_seconds"] + 1
        self.assertIsNone(proof.revalidate())
        self.assertEqual(dict(proof.marker_pins), original_pins)
        self.marker(self.root / "vendor/.caprmedio_empty")
        with self.assertRaises(selection.ProjectSelectionError):
            proof.revalidate()
        self.assertEqual(dict(proof.marker_pins), original_pins)


class ProjectSelectionBoundaryIndependentTests(DeclarationBoundaryHelperIndependentTests):
    """Actual Selection caller coverage; acceptance awaits P2322 wiring."""

    def select(self):
        return selection.resolve_project(self.root, self.control.name)

    def test_selection_retains_first_absence_proof_across_revalidation(self):
        self.declare("delivery_path", "vendor/.caprmedio_empty/new")
        selected = self.select()
        original_pins = dict(selected._boundary_proof.marker_pins)
        self.assertIsNone(selected._revalidate_boundary())
        self.marker(self.root / "vendor/.caprmedio_empty", name="shared-name")
        for _ in range(2):
            with self.assertRaises(selection.ProjectSelectionError):
                selected._revalidate_boundary()
        self.assertEqual(dict(selected._boundary_proof.marker_pins), original_pins)


if __name__ == "__main__":
    unittest.main()
