"""Pure current-form golden checks for current Entity and Terms graph helpers.

These fixtures are not a live Run or a full E555/E556 publication proof.
"""

from __future__ import annotations

import hashlib
import sys
import tempfile
import unittest
from dataclasses import dataclass
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
GRAPH_ROOT = Path(__file__).resolve().parents[1]
if str(GRAPH_ROOT) not in sys.path:
    sys.path.insert(0, str(GRAPH_ROOT))

import definition_claims  # noqa: E402
import entity_projection  # noqa: E402
import owned_scope_selection  # noqa: E402
import term_hierarchy  # noqa: E402


@dataclass(frozen=True)
class Carrier:
    atom_id: str
    version: int
    content_role: str
    status: str
    carrier_path: str
    sha256: str
    body: str

    def evidence(self) -> dict[str, object]:
        return {"atom_id": self.atom_id, "atom_revision": self.version,
                "carrier_path": self.carrier_path, "carrier_sha256": self.sha256}


@dataclass(frozen=True)
class Subject:
    kind: str
    subject_path: str

    def evidence(self) -> dict[str, object]:
        return {"kind": self.kind, "subject_path": self.subject_path}


def current_body(claim: str, *, details: str = "Current explanatory detail.") -> str:
    return f"""# Summary

Current core fixture.

## Scope

Only the selected Scope Unit applies.

## Claim

{claim}

## Details

{details}
"""


def current_atom(atom_id: str, *, subject: str, scope: str = "Core", status: str = "Active", role: str = "Requirement") -> str:
    return (
        "---\n"
        f"atom_id: {atom_id}\nversion: 1\ncontent_role: {role}\nstatus: {status}\ncurrent_scope_unit: {scope}\n"
        "subjects:\n  governs:\n    continuant:\n"
        f"      - {subject}\n"
        "  depends_on:\n    continuant: []\n---\n\n"
        + current_body(f"the Term {subject} **means** a current core {subject}.")
    )


class CurrentCoreGraphGoldenTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "project"
        self.sources = self.root / "sources"
        self.sources.mkdir(parents=True)
        (self.root / ".git").mkdir()
        control = self.root / ".caprmedio_caprmedio"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[paths]\ncontrol_root = '.caprmedio_caprmedio'\nprojection_root = '.caprmedio_caprmedio/_projection'\n", encoding="utf-8")
        (control / "project_structure.toml").write_text(
            "[[scope_units]]\nscope_unit_name = 'Core'\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, name: str, content: str) -> Path:
        path = self.sources / name
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def test_recognizes_only_current_primary_claim_definition(self) -> None:
        carrier = Carrier(
            "CA-R-1872", 1, "Requirement", "Active", "sources/CA-R-1872.md", "a" * 64,
            current_body("the Term Carrier **means** a thing that bears content.",
                         details="the Term Ignored **means** Details are not a Claim.\n\n```\nthe Term Fenced **means** no fact.\n```"),
        )
        assessed = definition_claims.assess_definition(carrier, [Subject("GOVERNS", "Carrier")])
        self.assertEqual("recognized", assessed["state"])
        self.assertEqual("Carrier", assessed["term"])
        self.assertEqual("Carrier", assessed["subject_path"])
        self.assertEqual("Claim", assessed["contribution"]["section"])
        self.assertEqual("the Term Carrier **means** a thing that bears content.", assessed["contribution"]["text"])
        self.assertEqual([], assessed["diagnostics"])

    def test_definition_mismatch_is_an_honest_unsupported_current_fact(self) -> None:
        carrier = Carrier("CA-R-1873", 1, "Delivery", "Active", "sources/CA-R-1873.md", "b" * 64,
                          current_body("the Term File Carrier **means** a Carrier borne by a file."))
        assessed = definition_claims.assess_definition(carrier, [Subject("GOVERNS", "Carrier")])
        self.assertEqual("target_mismatch", assessed["state"])
        self.assertIn("definition-terminal-term-mismatch", {row["code"] for row in assessed["diagnostics"]})

    def test_hierarchy_recognition_never_asserts_native_admission(self) -> None:
        carrier = {"atom_id": "CA-D-1872", "atom_revision": 1, "carrier_path": "sources/CA-D-1872.md", "carrier_sha256": "c" * 64}
        recognized = term_hierarchy.assess_hierarchy_claim(
            carrier, {"governs": ["File Carrier"], "depends_on": ["Carrier"]},
            {"section": "Claim", "text": "the Term File Carrier NARROWER_THAN Carrier."},
        )
        self.assertEqual("recognized", recognized["state"])
        self.assertEqual(term_hierarchy.TERMS_NARROWER_THAN, recognized["facts"][0]["kind"])
        self.assertEqual("child_to_parent", recognized["facts"][0]["direction"])
        self.assertIn("native-admission-unassessed", {row["code"] for row in recognized["diagnostics"]})
        incomplete = term_hierarchy.analyze_hierarchy(["File Carrier"], recognized["facts"])
        self.assertEqual([], incomplete["edges"])
        self.assertEqual(["File Carrier"], [row["child"] for row in incomplete["external_references"]])
        self.assertEqual([], incomplete["roots"])
        self.assertIn("root-coverage-unresolved", {row["code"] for row in incomplete["diagnostics"]})

    def test_subkind_alias_and_subject_mismatch_cannot_create_hierarchy_edges(self) -> None:
        carrier = {"atom_id": "CA-R-1874", "atom_revision": 1, "carrier_path": "sources/CA-R-1874.md", "carrier_sha256": "d" * 64}
        alias = term_hierarchy.assess_hierarchy_claim(
            carrier, {"governs": ["File Carrier"], "depends_on": ["Carrier"]},
            {"section": "Claim", "text": "the Term File Carrier SUBKIND_OF Carrier."})
        mismatch = term_hierarchy.assess_hierarchy_claim(
            carrier, {"governs": ["Carrier"], "depends_on": ["File Carrier"]},
            {"section": "Claim", "text": "the Term File Carrier NARROWER_THAN Carrier."})
        self.assertEqual("not_relation", alias["state"])
        self.assertEqual([], alias["facts"])
        self.assertEqual("target_mismatch", mismatch["state"])
        self.assertEqual([], mismatch["facts"])
        self.assertIn("hierarchy-claim-subject-mismatch", {row["code"] for row in mismatch["diagnostics"]})

    def test_hierarchy_analysis_is_permutation_deterministic_when_native_terms_exist(self) -> None:
        facts = [
            {"kind": term_hierarchy.TERMS_NARROWER_THAN, "relation": term_hierarchy.TERMS_NARROWER_THAN,
             "child": "File Carrier", "parent": "Carrier", "direction": "child_to_parent", "source_evidence": {"carrier_path": "b.md"}},
            {"kind": term_hierarchy.TERMS_NARROWER_THAN, "relation": term_hierarchy.TERMS_NARROWER_THAN,
             "child": "Carrier", "parent": "Primary Entity", "direction": "child_to_parent", "source_evidence": {"carrier_path": "a.md"}},
        ]
        forward = term_hierarchy.analyze_hierarchy(["Primary Entity", "Carrier", "File Carrier"], facts)
        backward = term_hierarchy.analyze_hierarchy(["File Carrier", "Carrier", "Primary Entity"], list(reversed(facts)))
        self.assertEqual(forward, backward)
        self.assertEqual({"File Carrier": ["Carrier"], "Carrier": ["Primary Entity"], "Primary Entity": []}, forward["parents_by_term"])
        self.assertEqual(["Primary Entity"], forward["roots"])

    def test_entity_projection_keeps_metadata_and_incidence_source_owned(self) -> None:
        carrier = Carrier("CA-R-1875", 1, "Requirement", "Active", "sources/CA-R-1875.md", "e" * 64, "")
        projection = entity_projection.build_entity_projection(
            [carrier], [Subject("GOVERNS", "Carrier"), Subject("DEPENDS_ON", "Source Atom")],
            {"CA-R-1875": {"author": "Atom-owned", "isEntityProperty": True}}, [{"scope_unit_name": "Core"}])
        self.assertEqual([], projection["entities"])
        self.assertEqual([], projection["native_properties"])
        self.assertEqual([], projection["native_relations"])
        self.assertEqual(["DEPENDS_ON", "GOVERNS"], [row["relation"] for row in projection["atom_incidence"]])
        self.assertEqual("Carrier", projection["entity_candidates"][0]["candidate_identity"])
        self.assertEqual("unresolved", projection["entity_candidates"][0]["disposition"])
        self.assertEqual({"author": "Atom-owned", "isEntityProperty": True}, projection["source_atoms"][0]["metadata"])
        self.assertEqual({}, projection["source_fact_context_evidence"])
        self.assertEqual("unknown", projection["coverage"]["entity_admission"]["status"])
        self.assertEqual("not-covered", projection["coverage"]["native_relations"]["status"])

    def test_owned_scope_selection_uses_only_explicit_active_current_scope(self) -> None:
        self.write("CA-R-1872.md", current_atom("CA-R-1872", subject="Carrier"))
        self.write("CA-D-1872.md", current_atom("CA-D-1872", subject="File Carrier", role="Delivery"))
        other = self.write("CA-O-1872.md", current_atom("CA-O-1872", subject="Operations", scope="Other", role="Operations"))
        self.write("CA-R-inactive.md", current_atom("CA-R-inactive", subject="Retired", status="Inactive"))
        selection = owned_scope_selection.prepare_owned_scope_selection(self.root, self.sources, "Core")
        self.assertEqual("prepared", selection["outcome"])
        self.assertEqual(["CA-D-1872", "CA-R-1872"], selection["selection"]["atom_ids"])
        self.assertEqual(
            [{"atom_id": "CA-O-1872", "carrier_path": "sources/CA-O-1872.md",
              "carrier_sha256": hashlib.sha256(other.read_bytes()).hexdigest(), "current_scope_unit": "Other"}],
            selection["inventory"]["support_sources"])


if __name__ == "__main__":
    unittest.main()
