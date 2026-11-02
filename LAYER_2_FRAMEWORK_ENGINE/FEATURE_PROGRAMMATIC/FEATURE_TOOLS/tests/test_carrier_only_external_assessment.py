"""Verified lossless reference recoding keeps its R1432 class through O145/O128."""

import copy
import hashlib
import json
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE.parent), str(HERE), str(HERE.parents[1] / "FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR")]
import lifecycle_intents as lifecycle  # noqa: E402
import test_selected_atom_lifecycle as fixtures  # noqa: E402
from selected_update_assessment import assess_update_identity  # noqa: E402


CAPTURED = HERE / "fixtures/carrier_only_recoding.json"


class CarrierOnlyExternalAssessmentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SelectedAtomLifecycleTest("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.captured = json.loads(CAPTURED.read_text())
        # Keep this classifier test bound to the actual reviewed Current
        # policies, independent of later repository source promotion.
        for key, old_path in zip(("r1432", "r1464"), self.fixture.semantic_assessment_authorities[1:]):
            value = self.captured["policies"][key]
            self.assertEqual(value["sha256"], hashlib.sha256(value["text"].encode()).hexdigest())
            old_path.write_text(value["text"])

    def package(self, target, proposal):
        report = self.fixture._semantic_assessment_report(proposal, change_class="carrier_only", target_descriptor=target)
        evidence = lifecycle._assessment_json((self.root / report["path"]).read_text())
        evidence["declaredDelta"] = "Verified lossless Entity-name/reference recoding; governed Claim, applicability, acceptance, Summary and Role remain unchanged."
        path = self.root / ".caprmedio_tmp/carrier-only-assessment.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps({"assessments": [evidence]}))
        return {"path": path.relative_to(self.root).as_posix(), "digest": hashlib.sha256(path.read_bytes()).hexdigest()}

    def fixture_parameters(self):
        path = self.fixture.target
        path.write_text(path.read_text().replace("Fixture claim.", "Use `Atom/Content Role: Requirement` as the same Entity reference."))
        atom = fixtures.atom_from_path(self.root, path)
        proposal = {"frontmatter": atom.frontmatter,
                    "content": atom.content.replace("Atom/Content Role: Requirement", "Atom/(.Content Role: Requirement)")}
        target = lifecycle.carrier_descriptor(self.root, atom)
        return {"target": target, "proposed": proposal, "change_class": "carrier_only",
                "semantic_assessment_report": self.package(target, proposal)}

    def seal(self, parameters):
        result = assess_update_identity(lifecycle, {"project_root": self.root, "parameters": parameters})
        self.assertEqual("identity-preserving", result["result"])
        self.assertEqual("carrier_only", result["native_result"]["assessment"]["admitted_change_class"])
        return result["native_result"]["assessment"]

    def test_actual_reviewed_notation_proposal_has_carrier_only_assessment_and_exact_seal(self):
        path = self.root / self.captured["target"]["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self.captured["target_raw"])
        self.assertEqual(self.captured["target"]["digest"], hashlib.sha256(path.read_bytes()).hexdigest())
        target = lifecycle.carrier_descriptor(self.root, str(path))
        proposal = self.captured["proposed"]
        parameters = {"target": target, "proposed": proposal, "change_class": "carrier_only",
                      "semantic_assessment_report": self.package(target, proposal)}
        before = path.read_bytes()
        assessment = self.seal(parameters)
        result = lifecycle.update_atom_action(self.root, parameters, assessment=assessment)
        self.assertEqual("preview", result["outcome"])
        self.assertEqual("carrier_only", result["assessment_evidence"]["admitted_change_class"])
        self.assertEqual(before, path.read_bytes())

    def test_bound_carrier_only_recode_preserves_identity_version_time_and_history_rules(self):
        parameters = self.fixture_parameters()
        before = self.fixture.target.read_bytes()
        assessment = self.seal(parameters)
        result = lifecycle.update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
        self.assertEqual("applied", result["outcome"])
        self.assertEqual(parameters["target"]["atom_id"], result["observed"]["atom_id"])
        self.assertEqual(parameters["target"]["version"] + 1, result["observed"]["version"])
        self.assertNotEqual(parameters["target"]["updated_at"], result["observed"]["updated_at"])
        self.assertEqual(before, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())

    def test_changed_body_without_verified_evidence_remains_unresolved(self):
        parameters = self.fixture_parameters()
        parameters.pop("semantic_assessment_report")
        before = self.fixture.target.read_bytes()
        result = lifecycle.update_atom_action(self.root, parameters, execute=True, authorized=True)
        self.assertEqual("unresolved", result["outcome"])
        self.assertEqual(before, self.fixture.target.read_bytes())

    def test_authority_and_proposal_drift_are_refused_after_assessment(self):
        for kind in ("authority", "proposal"):
            with self.subTest(kind=kind):
                parameters = self.fixture_parameters()
                assessment = self.seal(parameters)
                before = self.fixture.target.read_bytes()
                if kind == "authority":
                    path = self.fixture.semantic_assessment_authorities[1]
                    path.write_text(path.read_text() + "\nStale evidence.\n")
                else:
                    parameters = copy.deepcopy(parameters)
                    parameters["proposed"]["content"] += "\nUnassessed change.\n"
                result = lifecycle.update_atom_action(self.root, parameters, execute=True, authorized=True, assessment=assessment)
                self.assertEqual("unresolved", result["outcome"])
                self.assertEqual(before, self.fixture.target.read_bytes())

    def test_evidence_never_grants_effect_permission_and_recovery_class_guard_remains(self):
        parameters = self.fixture_parameters()
        assessment = self.seal(parameters)
        before = self.fixture.target.read_bytes()
        with self.assertRaisesRegex(lifecycle.LifecycleError, "authorization-required"):
            lifecycle.update_atom_action(self.root, parameters, execute=True, authorized=False, assessment=assessment)
        with self.assertRaisesRegex(lifecycle.LifecycleError, "recovery must be carrier_only"):
            lifecycle._admit_assessment_class("equivalent_refinement", carrier_recovery=True)
        with self.assertRaisesRegex(lifecycle.LifecycleError, "not admitted"):
            lifecycle._admit_assessment_class("unreviewed", carrier_recovery=False)
        self.assertEqual(before, self.fixture.target.read_bytes())


if __name__ == "__main__":
    unittest.main()
