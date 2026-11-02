"""The observed Current D479 Claim selects RMED siblings; frozen authority stays historical."""

import copy
import hashlib
import json
from pathlib import Path
import unittest
import sys

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from test_schema_extended import run, sources
from test_authority_checks import source as historical_source
from validate_atoms_workers.authority import resolve_context
from validate_atoms_workers.checks import validate_carrier


CAPTURED = Path(__file__).resolve().parents[2] / "tests/fixtures/rmed_current_layout.json"


def current_source():
    row = json.loads(CAPTURED.read_text(encoding="utf-8"))["layout_authority"]
    text = row["text"]
    if hashlib.sha256(text.encode()).hexdigest() != row["sha256"]:
        raise AssertionError("captured Current body-layout authority bytes drifted")
    metadata = yaml.safe_load(text.split("---", 2)[1])
    return {"binding": {"atom_id": "CA-D-479", "version": metadata["version"],
                        "path": row["source_path"], "sha256": row["sha256"]},
            "text": text, "metadata": metadata}


def rows():
    return [row for row in sources() if row["binding"]["atom_id"] != "CA-D-479"] + [current_source()]


def check_body(body, role="Requirement", authority=None):
    selected = [current_source()] if authority is None else authority
    result = validate_carrier({"content_role": role}, body, resolve_context(selected), {"sources": selected})
    outcome = next(row for row in result["outcomes"] if row["code"] == "body.sections")
    return outcome["outcome"], result


MINIMAL = "## Summary\n\nPreserved Summary.\n\n## Claim\n\nRequired prose.\n"


class RmedSiblingLayoutTests(unittest.TestCase):
    def test_current_rmed_required_and_optional_siblings(self):
        full = MINIMAL.replace("## Claim", "## Claim scope\n\nSelected context.\n\n## Claim")
        full += "\n## Semantics\n\nMeaning.\n\n## Details\n\nSupporting detail.\n"
        for role in ("Requirement", "Method", "Evaluation", "Delivery"):
            for body in (MINIMAL, full):
                with self.subTest(role=role, body=body):
                    self.assertEqual("passed", check_body(body, role)[0])
                    additional = run("body.additional_properties", {"content_role": role}, body, source_rows=rows())
                    self.assertEqual([], additional.findings)
                    self.assertEqual([], additional.gaps)

    def test_legacy_read_compatibility_does_not_admit_h1_current_candidate(self):
        self.assertEqual("failed", check_body(MINIMAL.replace("## Summary", "# Summary"))[0])
        old = "# Summary\n\nPreserved Summary.\n\n## Scope\n\nScope.\n\n## Claim\n\nProse.\n\n## Details\n"
        historical = historical_source("CA-D-479")
        self.assertEqual("passed", check_body(old, authority=[historical])[0])
        self.assertEqual("failed", check_body(MINIMAL, authority=[historical])[0])

    def test_non_rmed_h1_layout_is_unchanged(self):
        from test_current_body import body
        for role in ("Concern", "Analysis", "Plan", "Operations"):
            with self.subTest(role=role):
                self.assertEqual("passed", check_body(body(role), role)[0])

    def test_formal_child_is_optional_requirement_only_and_does_not_supply_prose(self):
        formal = "\n### Formal claim\n\n```text\nX/(.Property:Value)\n```\n"
        self.assertEqual("passed", check_body(MINIMAL + formal)[0])
        self.assertEqual("passed", check_body(MINIMAL + formal.replace("\n```\n", "\n````\n"))[0])
        self.assertEqual("failed", check_body(MINIMAL.replace("Required prose.", "") + formal)[0])
        for role in ("Method", "Evaluation", "Delivery"):
            self.assertEqual("failed", check_body(MINIMAL + formal, role)[0])
        for malformed in (formal.replace("### Formal", "## Formal"),
                          formal.replace("```text", "not fenced"),
                          formal.replace("X/(.Property:Value)", ""),
                          formal + formal):
            self.assertEqual("failed", check_body(MINIMAL + malformed)[0])

    def test_duplicate_reordered_nested_fenced_and_empty_properties_fail(self):
        for body in (MINIMAL + "\n## Claim\n\nAgain.\n",
                     MINIMAL + "\n## Claim scope\n\nToo late.\n",
                     MINIMAL.replace("Required prose.", "```text\nOnly code\n```"),
                     MINIMAL.replace("Required prose.", "### Supporting\n\nOnly child text."),
                     MINIMAL.replace("## Summary", "```md\n## Summary\n```\n## Unregistered"),
                     MINIMAL.replace("Preserved Summary.", ""),
                     MINIMAL + "\n## Details\n",
                     MINIMAL + "\n## Details\n\n### Same key\nA\n### Same key!\nB\n"):
            with self.subTest(body=body):
                self.assertEqual("failed", check_body(body)[0])
        fenced = MINIMAL.replace("Required prose.", "Required prose.\n```md\n## Claim\n## Summary\n```")
        self.assertEqual("passed", check_body(fenced)[0])

    def test_current_optional_body_properties_cannot_be_duplicated_in_frontmatter(self):
        checked = run("property.single_location", {"content_role": "Requirement", "claim_scope": "duplicate",
                      "semantics": "duplicate", "formal_claim": "duplicate"}, MINIMAL, source_rows=rows())
        self.assertEqual({"claim_scope", "semantics", "formal_claim"},
                         {row["property"] for row in checked.findings})

    def test_layout_is_bound_to_reviewed_claim_not_frozen_metadata_version(self):
        changed = copy.deepcopy(current_source())
        version = changed["metadata"]["version"]
        changed["text"] = changed["text"].replace(f"version: {version}", f"version: {version + 1}", 1)
        changed["metadata"]["version"] = changed["binding"]["version"] = version + 1
        changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode()).hexdigest()
        self.assertEqual("passed", check_body(MINIMAL, authority=[changed])[0])

    def test_unknown_or_ambiguous_authority_does_not_fall_back(self):
        changed = copy.deepcopy(current_source())
        changed["text"] = changed["text"].replace("The prose is mandatory", "Different unreviewed rule: prose is mandatory")
        changed["binding"]["sha256"] = hashlib.sha256(changed["text"].encode()).hexdigest()
        self.assertEqual("not_checked", check_body(MINIMAL, authority=[changed])[0])
        self.assertEqual("not_checked", check_body(MINIMAL, authority=[current_source(), current_source()])[0])


if __name__ == "__main__":
    unittest.main()
