"""Stable Atom ID lookup is confined to one selected Project's authority."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))

from current_atom_locator import CurrentAtomLocator, CurrentAtomLocatorError, locate_current_atom  # noqa: E402


class CurrentAtomLocatorTests(unittest.TestCase):
    def setUp(self):
        scratch = REPOSITORY / ".caprmedio_tmp/tests/current-atom-locator"
        scratch.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.control = self.root / ".caprmedio_control"
        self.scope = self.control / "scope"
        self.scope.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "fixture"\n[paths]\ncontrol_root = ".caprmedio_control"\n', encoding="utf-8")
        (self.control / "project_structure.toml").write_text(
            'schema_version = 1\n[[scope_units]]\nscope_unit_name = "UNIT"\n'
            'authority_path = ".caprmedio_control/scope"\n'
            'delivery_path = ".caprmedio_control/delivery"\n', encoding="utf-8")
        self.atom_id = "CA-R-101"
        self.hint = "old/path/CA-R-101--old-name.md"

    def atom(self, path, atom_id=None, *, status="Active", role="Requirement"):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f'---\natom_id: {atom_id or self.atom_id}\nstatus: {status}\n'
            f'content_role: {role}\n---\nbody\n', encoding="utf-8")
        return path

    def locate(self):
        return locate_current_atom(self.root, self.atom_id, self.hint)

    def test_missing_hint_follows_identity_after_move(self):
        moved = self.atom(self.scope / "04_requirement" / "feature" / "CA-R-101--new-name.md")
        self.assertEqual(moved.relative_to(self.root).as_posix(), self.locate())

    def test_duplicate_current_identity_refuses(self):
        self.atom(self.scope / "04_requirement" / "a" / "CA-R-101--one.md")
        self.atom(self.scope / "04_requirement" / "b" / "CA-R-101--two.md")
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            self.locate()
        self.assertEqual("atom-identity-duplicate", caught.exception.code)

    def test_unique_current_claim_preserves_quoted_legacy_id_and_refuses_duplicate(self):
        legacy_id = "CAPRMEDIO-R-793"
        first = self.atom(
            self.scope / "04_requirement" / "feature" / f"{legacy_id}--current.md", legacy_id
        )
        first.write_text(
            first.read_text(encoding="utf-8").replace(
                f"atom_id: {legacy_id}", f'atom_id: "{legacy_id}"'
            ),
            encoding="utf-8",
        )
        locator = CurrentAtomLocator(self.root)
        locator.assert_unique_current_claim(legacy_id, first)

        duplicate = self.atom(
            self.scope / "04_requirement" / "another" / f"{legacy_id}--duplicate.md", legacy_id
        )
        duplicate.write_text(
            duplicate.read_text(encoding="utf-8").replace(
                f"atom_id: {legacy_id}", f'atom_id: "{legacy_id}"'
            ),
            encoding="utf-8",
        )
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            CurrentAtomLocator(self.root).assert_unique_current_claim(legacy_id, first)
        self.assertEqual("atom-identity-duplicate", caught.exception.code)

    def test_unique_current_claim_ignores_unregistered_000_and_projection_copies(self):
        current = self.atom(self.scope / "04_requirement" / "CA-R-101--current.md")
        self.atom(self.control / "000" / "04_requirement" / "CA-R-101--unregistered.md")
        projection = self.atom(
            self.scope / "04_requirement" / "_projection" / "CA-R-101--projection.md"
        )
        projection.write_text(
            projection.read_text(encoding="utf-8").replace(
                "status: Active", "status: Active\nartifact_form: Projection"
            ),
            encoding="utf-8",
        )

        CurrentAtomLocator(self.root).assert_unique_current_claim(self.atom_id, current)

    def test_unique_current_claim_requires_exact_expected_path(self):
        self.atom(self.scope / "04_requirement" / "CA-R-101--current.md")
        locator = CurrentAtomLocator(self.root)
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locator.assert_unique_current_claim(
                self.atom_id, self.scope / "04_requirement" / "CA-R-101--other.md"
            )
        self.assertEqual("atom-identity-path-mismatch", caught.exception.code)

    def test_selected_metadata_with_competing_filename_identity_refuses(self):
        self.atom(self.scope / "04_requirement" / "CA-C-1--misnamed.md", self.atom_id)
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            self.locate()
        self.assertEqual("atom-identity-source-ambiguous", caught.exception.code)

    def test_draft_and_archived_only_claims_are_not_current(self):
        self.atom(self.scope / "04_requirement" / "draft" / "CA-R-101--draft.md", status="Draft")
        self.atom(self.scope / "04_requirement" / "archived" / "CA-R-101--old.md", status="Archived")
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            self.locate()
        self.assertEqual("atom-identity-not-found", caught.exception.code)

    def test_existing_symlink_hint_fails_closed(self):
        target = self.atom(self.root / "outside.md")
        hint = self.root / self.hint
        hint.parent.mkdir(parents=True)
        hint.symlink_to(target)
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locate_current_atom(self.root, self.atom_id, self.hint)
        self.assertEqual("atom-path-unavailable", caught.exception.code)

    def test_missing_hint_through_symlink_parent_does_not_trigger_fallback(self):
        alias = self.root / "alias"
        alias.symlink_to(self.scope, target_is_directory=True)
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locate_current_atom(self.root, self.atom_id, "alias/missing/CA-R-101--old.md")
        self.assertEqual("atom-path-unavailable", caught.exception.code)

    def test_foreign_hint_is_rejected(self):
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locate_current_atom(self.root, self.atom_id, self.root.parent / "foreign.md")
        self.assertEqual("atom-path-outside-project", caught.exception.code)

    def test_unrelated_malformed_concern_does_not_block_lookup(self):
        self.atom(self.scope / "04_requirement" / "feature" / "CA-R-101--current.md")
        malformed = self.scope / "01_concern" / "CA-C-999--unrelated.md"
        malformed.parent.mkdir(parents=True)
        malformed.write_text("---\natom_id: CA-C-999\nbroken: [\n---\n", encoding="utf-8")
        self.assertEqual(".caprmedio_control/scope/04_requirement/feature/CA-R-101--current.md", self.locate())

    def test_identity_family_limits_reads_to_its_registered_role_folder(self):
        moved = self.atom(self.scope / "09_operations" / "CA-O-101--current.md", "CA-O-101", role="Operations")
        unrelated = self.scope / "01_concern" / "CA-C-900--unrelated.md"
        unrelated.parent.mkdir(parents=True)
        unrelated.write_text("not an Atom\n", encoding="utf-8")
        from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
        from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS
        original_read = ReadContext.read
        reads = []

        def read(reader, path, **kwargs):
            if kwargs.get("remember", True):
                reads.append(path)
            return original_read(reader, path, **kwargs)

        with patch.object(ReadContext, "read", read):
            result = locate_current_atom(self.root, "CA-O-101", self.hint,
                                         reader=ReadContext(roots=[str(self.root)], limits=dict(CEILINGS)))
        self.assertEqual(moved.relative_to(self.root).as_posix(), result)
        self.assertNotIn(unrelated, reads)

    def test_registered_delivery_and_projection_copies_are_not_current_sources(self):
        real = self.atom(self.scope / "09_operations" / "CA-O-101--current.md", "CA-O-101", role="Operations")
        self.atom(self.scope / "09_operations" / "delivery" / "CA-O-101--delivered.md",
                  "CA-O-101", role="Operations")
        projection = self.scope / "09_operations" / "projection-copy.md"
        projection.write_text(
            "---\natom_id: CA-O-101\nstatus: Active\ncontent_role: Operations\n"
            "artifact_form: Projection\n---\n", encoding="utf-8")
        structure = self.control / "project_structure.toml"
        structure.write_text(structure.read_text().replace(
            'delivery_path = ".caprmedio_control/delivery"',
            'delivery_path = ".caprmedio_control/scope/09_operations/delivery"'), encoding="utf-8")
        self.assertEqual(real.relative_to(self.root).as_posix(),
                         locate_current_atom(self.root, "CA-O-101", self.hint))

    def test_one_admission_reuses_one_role_index_for_42_missing_hints(self):
        locator = CurrentAtomLocator(self.root)
        sources = []
        for index in range(42):
            atom_id = f"CA-O-{100 + index}"
            sources.append(self.atom(self.scope / "09_operations" / f"{atom_id}--current.md", atom_id,
                                     role="Operations"))
        for index in range(42):
            atom_id = f"CA-O-{100 + index}"
            self.assertTrue(locator.locate(atom_id, f"missing/{atom_id}.md").endswith(f"{atom_id}--current.md"))
        self.assertEqual(1, len(locator._records))
        self.assertEqual(1, len(locator.reader.inventories))
        self.assertEqual(42, len(locator.reader.fingerprints))
        locator.revalidate()

    def test_final_revalidation_rejects_changed_or_new_current_sources(self):
        moved = self.atom(self.scope / "09_operations" / "CA-O-101--current.md", "CA-O-101", role="Operations")
        locator = CurrentAtomLocator(self.root)
        locator.locate("CA-O-101", "missing/CA-O-101.md")
        moved.write_text(moved.read_text() + "changed\n", encoding="utf-8")
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locator.revalidate()
        self.assertEqual("atom-identity-source-changed", caught.exception.code)

        locator = CurrentAtomLocator(self.root)
        locator.locate("CA-O-101", "missing/CA-O-101.md")
        self.atom(self.scope / "09_operations" / "CA-O-101--duplicate.md", "CA-O-101", role="Operations")
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locator.revalidate()
        self.assertEqual("atom-identity-source-changed", caught.exception.code)

    def test_repeated_revalidation_detects_changes_after_an_earlier_check(self):
        self.atom(self.scope / "09_operations" / "CA-O-101--current.md", "CA-O-101", role="Operations")
        locator = CurrentAtomLocator(self.root)
        locator.locate("CA-O-101", "missing/CA-O-101.md")
        locator.revalidate()
        self.atom(self.scope / "09_operations" / "CA-O-101--duplicate.md", "CA-O-101", role="Operations")
        with self.assertRaises(CurrentAtomLocatorError) as caught:
            locator.revalidate()
        self.assertEqual("atom-identity-source-changed", caught.exception.code)

    def test_registered_root_scans_only_role_folders_and_reads_nested_scope_once(self):
        parent_role = self.control / "04_requirement"
        moved = self.atom(parent_role / "nested" / "04_requirement" / "CA-R-101--current.md")
        self.atom(self.control / "000_legacy" / "04_requirement" / "CA-R-101--legacy.md")
        self.atom(parent_role / ".caprmedio_foreign" / "04_requirement" / "CA-R-101--foreign.md")
        (self.control / "project_structure.toml").write_text(
            'schema_version = 1\n'
            '[[scope_units]]\nscope_unit_name = "ROOT"\n'
            'authority_path = ".caprmedio_control"\ndelivery_path = ".caprmedio_control/delivery"\n'
            '[[scope_units]]\nscope_unit_name = "NESTED"\n'
            'authority_path = ".caprmedio_control/04_requirement/nested"\n'
            'delivery_path = ".caprmedio_control/delivery/nested"\n', encoding="utf-8")
        from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
        from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS
        original_read = ReadContext.read
        reads = []

        def read(reader, path, **kwargs):
            if kwargs.get("remember", True):
                reads.append(path)
            return original_read(reader, path, **kwargs)

        with patch.object(ReadContext, "read", read):
            result = locate_current_atom(self.root, self.atom_id, self.hint,
                                         reader=ReadContext(roots=[str(self.root)], limits=dict(CEILINGS)))
        self.assertEqual(moved.relative_to(self.root).as_posix(), result)
        self.assertEqual(1, reads.count(moved))


if __name__ == "__main__":
    unittest.main()
