"""Current Relation Definition Type registers one specific optional fenced String."""

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

sys.path[:0] = [str(Path(__file__).resolve().parents[2]), str(Path(__file__).resolve().parents[1])]
from validate_atoms_workers.authority import AuthorityContext, Obligation  # noqa: E402
from validate_atoms_workers.check_sections import _body  # noqa: E402
from validate_atoms_workers.check_support import Check  # noqa: E402
from test_current_type_admission import source_row  # noqa: E402
from test_rmed_sibling_layout import current_source, MINIMAL, rows as common_sources  # noqa: E402
from test_schema_extended import run  # noqa: E402


def relation_source():
    row = json.loads((Path(__file__).parent / "fixtures/current_relation_type_authority.json").read_text())
    assert hashlib.sha256(row["text"].encode()).hexdigest() == row["sha256"]
    return source_row(row["text"], row["source_path"])


def checked(body, metadata=None, sources=None):
    metadata = {"content_role": "Requirement", "type": "Relation Definition"} if metadata is None else metadata
    sources = [current_source(), relation_source()] if sources is None else sources
    context = AuthorityContext([row["binding"] for row in sources], 0, 0, 0, [], (), {}, False)
    check = Check(Obligation("body.sections", [], True, "body contract"), context, {"sources": sources})
    _body(metadata, body, check)
    return check


NOTATION = "\n## Notation for subject\n\n```text\n.\n```\n"


class RelationNotationLayoutTests(unittest.TestCase):
    def test_registered_relation_property_allows_one_fenced_string_without_changing_common_skeleton(self):
        for body in (MINIMAL, MINIMAL + NOTATION,
                     MINIMAL + "\n## Semantics\n\nMeaning.\n" + NOTATION + "\n## Details\n\nSupport.\n",
                     MINIMAL + NOTATION.replace("\n.\n", "\n\n")):
            with self.subTest(body=body):
                check = checked(body)
                self.assertEqual(check.findings + check.gaps, [])
                self.assertIn("CA-R-2228", [row["atom_id"] for row in check.obligation.authority])
        for metadata in ({"content_role": "Requirement", "type": "Entity Definition"},
                         {"content_role": "Method", "type": "Implementation Method"}):
            self.assertTrue(checked(MINIMAL + NOTATION, metadata).findings)

    def test_type_registration_does_not_admit_other_or_malformed_properties(self):
        for value in (NOTATION + NOTATION, NOTATION.replace("```text", "plain"),
                      NOTATION.replace("\n```\n", "\n"), NOTATION + "\n```text\nSecond\n```\n",
                      NOTATION.replace("## Notation", "### Notation"),
                      NOTATION.replace("## Notation for subject", "## Unregistered")):
            with self.subTest(value=value):
                self.assertTrue(checked(MINIMAL + value).findings)

    def test_unknown_missing_duplicate_or_stale_type_authority_is_a_gap(self):
        changed = copy.deepcopy(relation_source())
        changed["text"] = changed["text"].replace("zero or one string value", "zero or two string values")
        changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode()).hexdigest()
        stale = copy.deepcopy(relation_source())
        stale["text"] += "\nChanged bytes.\n"
        for sources in ([current_source()], [current_source(), changed], [current_source(), stale],
                        [current_source(), relation_source(), relation_source()]):
            self.assertTrue(checked(MINIMAL + NOTATION, sources=sources).gaps)

    def test_same_reviewed_type_claim_is_recognized_after_a_version_advance(self):
        source = relation_source()
        old = source["metadata"]["version"]
        revised = source_row(source["text"].replace(f"version: {old}", f"version: {old + 1}", 1),
                             source["binding"]["path"])
        result = checked(MINIMAL + NOTATION, sources=[current_source(), revised])
        self.assertEqual(result.findings + result.gaps, [])

    def test_reviewed_formal_claim_notation_recode_preserves_registration(self):
        source = relation_source()
        old = "Atom/Content Role: Requirement/Type: Relation Definition.Content.notation_for_subject"
        new = "Atom/(.Content Role: Requirement)/(.Type: Relation Definition).Content.notation_for_subject"
        self.assertEqual(source["text"].count(old), 1)
        revised = source_row(source["text"].replace(old, new), source["binding"]["path"])
        for row in (source, revised):
            with self.subTest(sha256=row["binding"]["sha256"]):
                result = checked(MINIMAL + NOTATION, sources=[current_source(), row])
                self.assertEqual(result.findings + result.gaps, [])
                self.assertIn(row["binding"], result.obligation.authority)
        changed = source_row(revised["text"].replace("zero or one string value", "zero or two string values"),
                             revised["binding"]["path"])
        self.assertTrue(checked(MINIMAL + NOTATION, sources=[current_source(), changed]).gaps)

    def test_related_schema_checks_use_the_same_type_property_registration(self):
        sources = [*common_sources(), relation_source()]
        metadata = {"content_role": "Requirement", "type": "Relation Definition"}
        result = run("body.additional_properties", metadata, MINIMAL + NOTATION, source_rows=sources)
        self.assertEqual(result.findings + result.gaps, [])
        result = run("property.single_location", {**metadata, "notation_for_subject": "."},
                     MINIMAL + NOTATION, source_rows=sources)
        self.assertIn("notation_for_subject", [row["property"] for row in result.findings])


if __name__ == "__main__":
    unittest.main()
