"""A bounded reference lookup does not migrate unrelated legacy carriers."""

from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_atoms_workers.proposed_references import ProposedReferenceError, inventory_proposed_references


class UnrelatedLegacyReferenceLookupTests(unittest.TestCase):
    def setUp(self):
        scratch = Path(__file__).resolve().parents[5] / ".caprmedio_tmp"
        scratch.mkdir(exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(prefix="legacy-reference-", dir=scratch)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.structure = {"scope_units": [{"scope_unit_name": "TEST", "authority_path": "authority"}]}
        self.target = self.write("04_requirement/current.md", self.yaml("CA-R-1174"))

    def write(self, relative, text):
        path = self.root / "authority" / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    @staticmethod
    def yaml(identity, status="Active"):
        return (f"---\natom_id: {identity}\ncontent_role: Requirement\n"
                f"current_scope_unit: TEST\nstatus: {status}\nversion: 1\n---\n# Claim\n")

    @staticmethod
    def legacy(identity="CAPRMEDIO-CONC-076--old-runtime", key="semantic_id"):
        return f'+++\n{key} = "{identity}"\ncontent_role = "observation"\nstatus = "accepted"\n+++\n# Legacy\n'

    def lookup(self, ids=("CA-R-1174",)):
        return inventory_proposed_references(
            self.root, self.structure, ids,
            admitted_role_folders={"Requirement": "04_requirement", "Concern": "01_concern"},
            admitted_status_folders={"Requirement": {"Active": "", "Archived": "archived"},
                                     "Concern": {"Active": "", "Archived": "archived"}},
        )

    def test_unrelated_legacy_concern_does_not_block_requirement_lookup(self):
        legacy = self.write("01_concern/CAPRMEDIO-CONC-076--old-runtime.md", self.legacy())
        original = legacy.read_bytes()
        result = self.lookup()
        self.assertEqual(["CA-R-1174"], [row.atom_id for row in result.direct_targets])
        result.assert_current()
        self.assertEqual(original, legacy.read_bytes())

    def test_explicit_legacy_target_is_still_rejected(self):
        self.write("01_concern/legacy.md", self.legacy())
        with self.assertRaises(ProposedReferenceError):
            self.lookup(("CAPRMEDIO-CONC-076--old-runtime",))

    def test_legacy_cannot_hide_requested_id_or_duplicate(self):
        for key in ("atom_id", "semantic_id"):
            with self.subTest(key=key):
                self.write("01_concern/legacy.md", self.legacy("CA-R-1174", key))
                with self.assertRaises(ProposedReferenceError):
                    self.lookup()

    def test_filename_hint_does_not_silently_hide_requested_legacy(self):
        self.write("01_concern/CA-R-1174--legacy.md", self.legacy())
        with self.assertRaises(ProposedReferenceError):
            self.lookup()

    def test_malformed_or_identityless_legacy_remains_unresolved(self):
        for raw in ('+++\nsemantic_id = [\n+++\n', '+++\nstatus = "accepted"\n+++\n'):
            with self.subTest(raw=raw):
                self.write("01_concern/legacy.md", raw)
                with self.assertRaises(ProposedReferenceError):
                    self.lookup()

    def test_legacy_container_is_not_skipped(self):
        legacy = self.write("01_concern/legacy.md", self.legacy())
        legacy.with_suffix("").mkdir()
        with self.assertRaises(ProposedReferenceError):
            self.lookup()

    def test_current_yaml_duplicate_and_inactive_targets_remain_rejected(self):
        duplicate = self.write("04_requirement/other-name.md", self.yaml("CA-R-1174"))
        with self.assertRaisesRegex(ProposedReferenceError, "ambiguous"):
            self.lookup()
        duplicate.unlink()
        self.target.write_text(self.yaml("CA-R-1174", "Archived"))
        with self.assertRaises(ProposedReferenceError):
            self.lookup()

    def test_legacy_changes_are_still_in_currentness_evidence(self):
        legacy = self.write("01_concern/legacy.md", self.legacy())
        result = self.lookup()
        legacy.write_text(self.legacy() + "changed\n")
        with self.assertRaisesRegex(ProposedReferenceError, "changed"):
            result.assert_current()

    def test_discovered_plan_prerequisite_rechecks_legacy_identity_and_filename(self):
        def plan(identity, blocks):
            return (f"---\natom_id: {identity}\ncontent_role: Plan\ntype: Plan\n"
                    "current_scope_unit: TEST\nstatus: Active\nversion: 1\n"
                    f"relations:\n  blocks: {blocks}\n---\n# Plan\n")

        self.write("03_plan/first.md", plan("CA-P-FIRST", "[CA-P-SECOND]"))
        self.write("03_plan/second.md", plan("CA-P-SECOND", "[]"))

        def lookup():
            return inventory_proposed_references(
                self.root, self.structure, ["CA-P-FIRST"],
                admitted_role_folders={"Plan": "03_plan", "Concern": "01_concern"},
                admitted_status_folders={"Plan": {"Active": ""}, "Concern": {"Active": ""}},
                admitted_plan_status_folders={"Active": ""},
                candidate_metadata={"atom_id": "CA-P-NEW", "content_role": "Plan", "type": "Plan",
                                    "status": "Active", "relations": {"blocks": ["CA-P-FIRST"]}},
            )

        result = lookup()
        self.assertEqual(["CA-P-SECOND"], [row.atom_id for row in result.plan_prerequisite_closure])
        result.assert_current()
        for filename, identity in (("legacy.md", "CA-P-SECOND"),
                                   ("CA-P-SECOND--legacy.md", "unrelated-legacy")):
            with self.subTest(filename=filename):
                legacy = self.write("01_concern/" + filename, self.legacy(identity))
                with self.assertRaises(ProposedReferenceError):
                    lookup()
                legacy.unlink()

    def test_discovered_plan_ancestor_rechecks_legacy_identity(self):
        def plan(identity, parent):
            return (f"---\natom_id: {identity}\ncontent_role: Plan\ntype: Plan\n"
                    "current_scope_unit: TEST\nstatus: Active\nversion: 1\n"
                    f"relations:\n  is_decomposition_of: {parent}\n---\n# Plan\n")

        self.write("03_plan/second.md", plan("CA-P-SECOND", "[]"))
        self.write("03_plan/second/first.md", plan("CA-P-FIRST", "[CA-P-SECOND]"))

        def lookup():
            return inventory_proposed_references(
                self.root, self.structure, ["CA-P-FIRST"],
                admitted_role_folders={"Plan": "03_plan", "Concern": "01_concern"},
                admitted_status_folders={"Plan": {"Active": ""}, "Concern": {"Active": ""}},
                admitted_plan_status_folders={"Active": ""},
                candidate_path="authority/03_plan/second/first/new.md",
                candidate_metadata={"atom_id": "CA-P-NEW", "content_role": "Plan", "type": "Plan",
                                    "status": "Active", "relations": {"is_decomposition_of": ["CA-P-FIRST"]}},
            )

        result = lookup()
        self.assertEqual(["CA-P-FIRST", "CA-P-SECOND"], [row.atom_id for row in result.plan_parent_closure])
        self.assertTrue({"CA-P-FIRST", "CA-P-SECOND"} <= result._evidence.requested)
        self.write("01_concern/legacy.md", self.legacy("CA-P-SECOND"))
        with self.assertRaises(ProposedReferenceError):
            lookup()


if __name__ == "__main__":
    unittest.main()
