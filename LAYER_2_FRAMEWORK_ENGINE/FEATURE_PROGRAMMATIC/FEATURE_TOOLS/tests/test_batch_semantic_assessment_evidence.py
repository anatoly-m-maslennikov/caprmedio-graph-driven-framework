"""One completed review package can bind independent semantic Atom updates."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(Path(__file__).resolve().parent))

import test_selected_atom_lifecycle as fixtures  # noqa: E402
from lifecycle_intents import (  # noqa: E402
    LifecycleError, _assessment_json, carrier_descriptor, update_assessment_seal,
    update_atom_action,
)


class BatchSemanticAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SelectedAtomLifecycleTest(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        proposal = self.fixture._proposal(
            self.fixture.target, summary="Stable summary", body_suffix="\nClarified acceptance detail.\n"
        )
        self.report = self.fixture._semantic_assessment_report(proposal)
        self.evidence = _assessment_json((self.root / self.report["path"]).read_text())
        self.package = self.root / ".caprmedio_tmp/review.json"
        self.package.parent.mkdir(parents=True, exist_ok=True)
        self.parameters = {
            "target": carrier_descriptor(self.root, "CA-R-100"),
            "proposed": proposal,
            "change_class": "semantic_revision",
        }

    def pin(self):
        return {"path": self.package.relative_to(self.root).as_posix(),
                "digest": hashlib.sha256(self.package.read_bytes()).hexdigest()}

    def write_package(self, payload):
        self.package.write_text(json.dumps(payload), encoding="utf-8")
        self.parameters["semantic_assessment_report"] = self.pin()

    def preview(self):
        return update_atom_action(self.root, self.parameters, execute=False, authorized=True)

    def test_package_selects_exact_target_and_preserves_normal_assessment_seal(self):
        other = copy.deepcopy(self.evidence)
        other["target"]["atom_id"] = "CA-R-101"
        self.write_package({"assessments": [other, self.evidence]})
        preview = self.preview()
        self.assertEqual("preview", preview["outcome"])
        self.assertEqual(self.pin(), preview["assessment_evidence"]["comparison"]["report"])
        assessment = update_assessment_seal(self.parameters, preview["assessment_evidence"])
        before = self.fixture.target.read_bytes()
        result = update_atom_action(self.root, self.parameters, execute=True, authorized=True,
                                    assessment=assessment)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(self.parameters["target"]["version"] + 1, result["observed"]["version"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())

    def test_package_does_not_authorize_execution(self):
        self.write_package({"assessments": [self.evidence]})
        before = self.fixture.target.read_bytes()
        with self.assertRaisesRegex(LifecycleError, "authorization-required"):
            update_atom_action(self.root, self.parameters, execute=True, authorized=False)
        self.assertEqual(before, self.fixture.target.read_bytes())

    def test_existing_done_analysis_report_remains_supported(self):
        self.parameters["semantic_assessment_report"] = self.report
        result = self.preview()
        self.assertEqual("preview", result["outcome"])
        self.assertEqual("CA-A-400", result["assessment_evidence"]["comparison"]["report"]["atom_id"])

    def test_missing_duplicate_or_malformed_package_records_are_rejected(self):
        other = copy.deepcopy(self.evidence)
        other["target"]["atom_id"] = "CA-R-101"
        cases = [[], {}, {"assessments": []}, {"assessments": {}},
                 {"assessments": [other]}, {"assessments": [self.evidence, self.evidence]},
                 {"assessments": [self.evidence, None]},
                 {"assessments": [self.evidence, {"target": {}}]},
                 {"assessments": [self.evidence, {**other, "proposal": None}]},
                 {"assessments": [self.evidence, {**other, "authorityPins": {}}]},
                 {"assessments": [self.evidence, {**other, "lineageEvidencePins": []}]},
                 {"assessments": [self.evidence], "authorized": True}]
        before = self.fixture.target.read_bytes()
        for payload in cases:
            with self.subTest(payload=payload):
                self.write_package(payload)
                self.assertEqual("unresolved", self.preview()["outcome"])
                self.assertEqual(before, self.fixture.target.read_bytes())

    def test_duplicate_json_keys_and_invalid_json_are_rejected(self):
        for text in ('{"assessments": [], "assessments": []}', '{',
                     '{"assessments": [{"target": {}, "target": {}}]}'):
            with self.subTest(text=text):
                self.package.write_text(text, encoding="utf-8")
                self.parameters["semantic_assessment_report"] = self.pin()
                self.assertEqual("unresolved", self.preview()["outcome"])

    def test_target_proposal_authority_identity_and_lineage_checks_remain(self):
        cases = [("target", "digest", "0" * 64), ("target", "path", "wrong.md"),
                 ("proposal", "content_digest", "0" * 64),
                 ("authorityPins", "r1432", {"path": self.report["path"], "digest": self.report["digest"]})]
        for section, field, value in cases:
            with self.subTest(section=section, field=field):
                evidence = copy.deepcopy(self.evidence)
                evidence[section][field] = value
                self.write_package({"assessments": [evidence]})
                self.assertEqual("unresolved", self.preview()["outcome"])
        for field, value in (("lineageEvidencePins", []), ("primaryClaimIdentityPreserved", False),
                             ("declaredDelta", ""), ("admittedChangeClass", "carrier_only")):
            with self.subTest(field=field):
                self.write_package({"assessments": [{**self.evidence, field: value}]})
                self.assertEqual("unresolved", self.preview()["outcome"])

    def test_stale_package_and_lineage_are_rejected(self):
        self.write_package({"assessments": [self.evidence]})
        self.package.write_text(self.package.read_text() + "\n")
        self.assertEqual("unresolved", self.preview()["outcome"])
        evidence = copy.deepcopy(self.evidence)
        evidence["lineageEvidencePins"][0]["digest"] = "0" * 64
        self.write_package({"assessments": [evidence]})
        self.assertEqual("unresolved", self.preview()["outcome"])


if __name__ == "__main__":
    unittest.main()
