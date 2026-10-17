"""Status inheritance uses actual base values and retains both source bindings."""
from pathlib import Path
import json
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import authoritative_status_models as models  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS  # noqa: E402


class StatusInheritanceTests(unittest.TestCase):
    def setUp(self):
        scratch = TOOLS.parents[2] / ".caprmedio_tmp/tests/status-inheritance"
        scratch.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name).resolve()
        self.sources = self.root / ".caprmedio_caprmedio" / models._SOURCE_TAIL
        self.sources.mkdir(parents=True)

    def source(self, number, subject, claim, status="Active"):
        path = self.sources / f"CA-R-{number}.md"
        path.write_text(
            f"---\natom_id: CA-R-{number}\ncontent_role: Requirement\n"
            f"version: 1\nstatus: {status}\nsubjects:\n  governs: {json.dumps(subject)}\n"
            f"---\n## Claim\n\n{claim}\n", encoding="utf-8",
        )
        return path

    def base(self, prefix="", values="Draft, Active, Archived"):
        return self.source(900, prefix + "Atom.Status", f"Atom.Status **must** admit ({values}).")

    def role(self, role="Plan", additions="(Backlog, Done, Canceled)", prefix=""):
        return self.source(901, prefix + f"Atom/Content Role: {role}.Status",
                           f"the Core {role} Status model **must** inherit the allowed values "
                           f"of Atom.Status and add {additions}.")

    def test_accepted_single_and_list_additions_short_and_full_subjects(self):
        for prefix in ("", "Entity/Continuant/Object/"):
            for role, additions, extra in (
                ("Plan", "(Backlog, Done, Canceled)", ["Backlog", "Done", "Canceled"]),
                ("Analysis", "Done", ["Done"]),
                ("Concern", "(Resolved, Canceled)", ["Resolved", "Canceled"]),
            ):
                with self.subTest(prefix=prefix, role=role):
                    self.base(prefix)
                    self.role(role, additions, prefix)
                    reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
                    index = models.capture_status_models(self.root, reader)
                    direct = models.resolve_status_model(self.root, {"content_role": role}, extra[0])
                    self.assertEqual(direct, models.resolve_status_model(
                        self.root, {"content_role": role}, extra[0], _index=index))
                    self.assertEqual(["Draft", "Active", "Archived", *extra], direct["statuses"])
                    self.assertEqual(["CA-R-900", "CA-R-901"],
                                     [row["atom_id"] for row in direct["model_sources"]])
                    models.revalidate_status_models(index, reader)

    def test_base_is_read_not_hardcoded_and_duplicates_are_not_repeated(self):
        self.base(values="Draft, Active, Archived, Additional")
        self.role(additions="(Active, Done)")
        result = models.resolve_status_model(self.root, {"content_role": "Plan"}, "Additional")
        self.assertEqual(["Draft", "Active", "Archived", "Additional", "Done"], result["statuses"])

    def test_missing_duplicate_inactive_and_wrong_subject_base_refuse(self):
        self.role()
        with self.assertRaises(models.StatusModelError):
            models.resolve_status_model(self.root, {"content_role": "Plan"}, "Active")
        self.base()
        self.source(902, "Atom.Status", "Atom.Status **must** admit (Draft, Active, Archived).")
        with self.assertRaisesRegex(models.StatusModelError, "one current"):
            models.resolve_status_model(self.root, {"content_role": "Plan"}, "Active")
        for subject, status in (("Atom.Status", "Archived"), ("Scope Unit.Status", "Active")):
            self.source(902, subject, "Atom.Status **must** admit (Draft, Active, Archived).", status)
            with self.assertRaises(models.StatusModelError):
                models.resolve_status_model(self.root, {"content_role": "Plan"}, "Active")

    def test_existing_specific_exact_model_keeps_precedence_and_does_not_leak(self):
        self.base()
        self.role()
        self.source(902, "Atom/Content Role: Plan/Type: Epic.Status",
                    "the Core Plan Status **must** be exactly (Active, Paused).")
        specific = models.resolve_status_model(self.root, {"content_role": "Plan", "type": "Epic"}, "Paused")
        self.assertEqual(["Active", "Paused"], specific["statuses"])
        self.assertEqual(["CA-R-902"], [row["atom_id"] for row in specific["model_sources"]])
        generic = models.resolve_status_model(self.root, {"content_role": "Plan", "type": "Other"}, "Backlog")
        self.assertIn("Draft", generic["statuses"])
        with self.assertRaises(models.StatusModelError):
            models.resolve_status_model(self.root, {"content_role": "Plans"}, "Active")

    def test_base_changes_invalidate_index_and_supplied_models(self):
        base = self.base()
        self.role()
        reader = ReadContext(roots=[str(self.root)], limits=dict(CEILINGS))
        index = models.capture_status_models(self.root, reader)
        before = models.resolve_status_model(self.root, {"content_role": "Plan"}, "Active", _index=index)
        base.write_text(base.read_text().replace("version: 1", "version: 2"), encoding="utf-8")
        with self.assertRaises(models.StatusModelError):
            models.revalidate_status_models(index, reader)
        with self.assertRaises(models.StatusModelError):
            models.resolve_status_model(self.root, {"content_role": "Plan"}, "Active", supplied_model=before)


if __name__ == "__main__":
    unittest.main()
