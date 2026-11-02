from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prepare_current_notation_adoption import convert_subject as _convert_subject, prepare_manifest


def convert_subject(value):
    return _convert_subject(value, property_owners={"Atom": frozenset({"Content Role", "Type"})})


class CurrentNotationPreparationTests(unittest.TestCase):
    def test_containment_count_stays_on_written_source_and_reverse_absent(self):
        converted = convert_subject("Workflow >{1+} Step >{0+} Sub-step")
        self.assertEqual(converted["state"], "safe")
        self.assertEqual(converted["after"], "Workflow {1+}<+ Step {0+}<+ Sub-step")
        self.assertEqual(converted["containment_tokens"], 2)

    def test_property_qualification_keeps_complete_bearer_and_relation_direction(self):
        converted = convert_subject("Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step")
        self.assertEqual(converted["after"], "Atom/(.Content Role:Operations)/(.Type:Workflow) {1+}<+ Atom/(.Content Role:Operations)/(.Type:Step)")
        self.assertEqual(converted["property_qualifiers"], 4)
        self.assertEqual(convert_subject(converted["after"])["state"], "unchanged")

    def test_bare_property_access_requires_the_same_explicit_atom_owner(self):
        self.assertEqual(convert_subject("Atom/Content Role:Operations/Type")["after"], "Atom/(.Content Role:Operations).Type")
        converted = convert_subject("Atom/Content Role")
        self.assertEqual(converted["after"], "Atom.Content Role")
        self.assertEqual(converted["property_accesses"], 1)
        self.assertEqual(converted["property_qualifiers"], 0)
        self.assertEqual(_convert_subject("Atom/Type:Workflow")["state"], "unresolved-qualifier")

    def test_non_atom_property_scope_is_exact_and_does_not_create_content_role(self):
        owners = {"Entity/Object/Continuant/Projection": frozenset({"Type"}),
                  "Entity/Object/Continuant/Structural Unit/Scope Unit": frozenset({"Type"})}
        for owner in owners:
            result = _convert_subject(owner + "/Type:Catalog", property_owners=owners)
            self.assertEqual(result["after"], owner + "/(.Type:Catalog)")
            self.assertEqual(_convert_subject(owner + "/Content Role:Method", property_owners=owners)["state"], "unresolved-qualifier")
        self.assertEqual(_convert_subject("Actor/Type:Operator", property_owners=owners)["state"], "unresolved-qualifier")

    def test_existing_directional_counts_formats_and_escapes_are_unchanged(self):
        for value in ("Part {1}+>{2..4} Whole", "Entity.Property[Text]{2}", r"Literal\>Name.Child", "Entity >| Classification", 'atom(content_role="Plan>Exact").Status'):
            with self.subTest(value=value):
                self.assertEqual(convert_subject(value)["state"], "unchanged")
                self.assertEqual(convert_subject(value)["after"], value)

    def test_uncertain_qualifier_and_bad_operator_are_review_only(self):
        for value in ("Widget/Status:Active", "Widget/Type:Value", "Widget/Content Role:Operations"):
            self.assertEqual(convert_subject(value)["state"], "unresolved-qualifier")
        for value in ("Whole -> Part", "Whole >{4..2} Part", "Whole >(Part", "Whole ((R>)) Part"):
            with self.subTest(value=value):
                self.assertEqual(convert_subject(value)["state"], "review-needed")

    def test_same_authority_ids_with_unreviewed_bytes_cannot_enable_property_rewrites(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as scratch:
            root = Path(scratch).resolve()
            directory = root / ".caprmedio_caprmedio" / "current"
            directory.mkdir(parents=True)
            for identity, version, subject in (("CA-R-1284", 23, "Entity"), ("CA-R-2397", 1, "Entity/Object/Continuant/Projection.Type"), ("CA-R-1", 1, "Entity/Object/Continuant/Projection/Type:Catalog")):
                (directory / (identity + ".md")).write_text(f"---\natom_id: {identity}\nversion: {version}\nstatus: Active\nsubjects:\n  governs: {subject}\n  depends_on: []\n---\n## Claim\nUnreviewed authority text.\n")
            frontier = root / "frontier.json"
            frontier.write_text(json.dumps({"roots": ["current"]}))
            manifest = prepare_manifest(root, frontier)
            self.assertEqual(manifest["checked_property_authorities"], [])
            self.assertEqual(manifest["subject_patch_payload"], [])
            self.assertEqual(manifest["subjects"][0]["state"], "unresolved-qualifier")

    def test_manifest_is_sha_pinned_dry_run_and_uses_whole_scalar_patch_contract(self):
        with tempfile.TemporaryDirectory(ignore_cleanup_errors=True) as scratch:
            root = Path(scratch).resolve()
            directory = root / ".caprmedio_caprmedio" / "current"
            directory.mkdir(parents=True)
            source = directory / "CA-R-1.md"
            raw = b'---\natom_id: CA-R-1\nversion: 3\nstatus: Active\nsubjects:\n  governs: Whole >{1+} Part\n  depends_on: []\n---\n## Claim\n\nExample Whole > Part.\n'
            source.write_bytes(raw)
            for number, status in enumerate(("Backlog", "Done", "Canceled"), 2):
                (directory / f"CA-R-{number}.md").write_bytes(raw.replace(b"CA-R-1", f"CA-R-{number}".encode()).replace(b"status: Active", f"status: {status}".encode()))
            (directory / "CA-R-5.md").write_bytes(raw.replace(b"CA-R-1", b"CA-R-5").replace(b"status: Active", b"status: active").replace(b"governs: Whole >{1+} Part", b"governs: {kind: Atom}"))
            ignored = directory / "draft" / "CA-R-2.md"
            ignored.parent.mkdir()
            ignored.write_bytes(raw)
            frontier = root / "frontier.json"
            frontier.write_text(json.dumps({"roots": ["current"]}))
            manifest = prepare_manifest(root, frontier)
            self.assertEqual(source.read_bytes(), raw)
            self.assertEqual(manifest["coverage"]["current_carriers"], 5)
            item = manifest["subject_patch_payload"][0]
            self.assertEqual(item["expected"]["sha256"], hashlib.sha256(raw).hexdigest())
            self.assertEqual(item["subject_patches"], [{"field": "governs", "old": "Whole >{1+} Part", "new": "Whole {1+}<+ Part"}])
            self.assertEqual(len(manifest["body_candidates"]), 5)
            self.assertTrue(manifest["preview_blockers"])


if __name__ == "__main__":
    unittest.main()
