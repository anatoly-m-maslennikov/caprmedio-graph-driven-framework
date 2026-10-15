"""Contract and mock-evidence tests; these do not simulate LLM judgment."""
import copy
import json
import re
import sys
import unittest
from pathlib import Path

import yaml

from test_split_evaluation import context, contract, gap, merge_evaluations, part

HERE = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[6]
CHECKS = {"properties", "scope", "claim", "details", "cce", "summary"}
EVALUATORS = {"evaluate_cce", "evaluate_properties", "evaluate_coherence"}
SECTIONS = [
    "1) Role & Mission", "2) Operating Principles (guarantee first-try success)",
    "3) Inputs & Interpretation", "4) Task-Type Playbooks (select matching TASK_TYPE)",
    "5) Formatting & Output Contract", "6) Web, Data, and Citations",
    "7) Error Handling & Edge Cases", "8) Final Validation Checklist (silent)",
    "9) Answer Template (the assistant will follow for final outputs)",
]


def validate_evidence(evaluation):
    """Exercise production admission, not a second test-only implementation."""
    contract.summarize_evaluations([evaluation], context=context())
    return evaluation["result"]


def passing_evidence():
    return merge_evaluations([part(group) for group in contract.GROUPS])


class PromptContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prompts = {p.stem.removesuffix(".prompt"): p.read_text() for p in HERE.glob("*.prompt.md")}
        cls.nodes = {name for name in cls.prompts if name.startswith("CA-O-")}

    def test_step_prompts_have_unique_action_bindings(self):
        self.assertEqual(set(self.prompts), self.nodes | {"evaluate_atom"} | EVALUATORS)
        actions = set()
        for step in self.nodes:
            binding = re.search(r"Step: (CA-O-\d+) \| Action: (CA-O-\d+) \| Context: (\w+)", self.prompts[step])
            self.assertIsNotNone(binding)
            self.assertEqual(binding[1], step)
            actions.add(binding[2])
        self.assertEqual(len(actions), len(self.nodes))

    def test_short_prompts_and_required_sections(self):
        for name, prompt in self.prompts.items():
            with self.subTest(prompt=name):
                self.assertTrue(prompt.startswith("# System Prompt\n"))
                if name in self.nodes:
                    self.assertNotRegex(prompt, r"(?m)^###")
                    self.assertLessEqual(len(prompt.split()), 160)
                else:
                    self.assertEqual(re.findall(r"^### (.+)$", prompt, re.M), SECTIONS)
                self.assertLessEqual(len(prompt.split()), 1800 if name == 'evaluate_coherence' else 1500 if name in EVALUATORS else 550 if name == "evaluate_atom" else 300)
                if name in self.nodes:
                    self.assertIn("Read", prompt)
                    self.assertIn("source", prompt.casefold())
                elif name == "evaluate_atom":
                    self.assertIn("pinned authority and input packet", prompt)
                    self.assertIn("README contract", prompt)
                else:
                    self.assertIn("inline", prompt)
                self.assertNotRegex(prompt, r"\b(?:TODO|TBD)\b")

    def test_evaluation_prompts_cover_runtime_checklist(self):
        sys.path.insert(0, str(HERE))
        from evaluation_contract import LOCAL_GROUPS as GROUPS
        prompt_checks = {check for checks in GROUPS.values() for check in checks}
        self.assertEqual(prompt_checks, CHECKS)
        for group, checks in GROUPS.items():
            for check in checks:
                self.assertIn(check, self.prompts["evaluate_" + group])

    def test_properties_prompt_preserves_optional_specialized_type_boundary(self):
        prompt = self.prompts["evaluate_properties"]
        row = next(line for line in prompt.splitlines() if line.startswith("| `type` |"))
        self.assertIn("ordinary R/M/D omit it unless a specialized Type applies", row)
        self.assertIn("one admitted String", row)
        self.assertIn("never a role-echo placeholder", row)
        self.assertIn("Evaluation retains its applicable Type requirement", row)
        for authority in ("CA-R-1700", "CA-D-276", "CA-D-283"):
            self.assertIn(authority, prompt)

    def test_freshness_permission_and_repair_guards(self):
        evaluation = self.prompts["evaluate_atom"]
        for phrase in ("before and after", "Below-threshold", "do not edit", "incomplete", "prerequisite"):
            self.assertIn(phrase.casefold(), evaluation.casefold())
        repair = " ".join(self.prompts["CA-O-110"].split())
        for phrase in ("Summary change requires replacement authority", "Formatting-only",
                       "governing checks to force a pass", "missing permission", "fixed_not_rechecked"):
            self.assertIn(phrase, repair)

    def test_properties_prompt_excludes_filename_location_checks(self):
        prompt = self.prompts["evaluate_properties"]
        for phrase in ("No filename/location conformance", "do not infer Properties from filenames or folders", "body layout"):
            self.assertIn(phrase, prompt)

    def test_prompts_do_not_embed_runtime_parameter_constants(self):
        for prompt in self.prompts.values():
            self.assertNotRegex(prompt, r"\b30 (?:Atoms|atoms|candidates)\b")
            self.assertNotIn("10 minutes", prompt)
            self.assertNotRegex(prompt, r"\b(?:10|90)%")

    def test_prompts_retain_context_isolation(self):
        self.assertIn("Context: Integrated", self.prompts["CA-O-108"])
        for step in ("CA-O-109", "CA-O-110"):
            self.assertIn("Context: Isolated", self.prompts[step])

    def test_carrier_role_profile_prompt_guards(self):
        self.assertIn("Entity model", self.prompts["evaluate_cce"])
        self.assertIn("meaning **and** value", self.prompts["evaluate_cce"])
        self.assertIn("Carrier definitions", self.prompts["evaluate_cce"])
        self.assertIn("semantic Content Role reclassification is excluded", self.prompts["evaluate_cce"])
        self.assertIn("reclassify Content Roles", self.prompts["evaluate_coherence"])

    def test_mock_corpus_is_separate_from_expected_judgments(self):
        cases = json.loads((HERE / "tests/fixtures/cases.json").read_text())
        self.assertGreaterEqual(len(cases), 8)
        ids = set()
        for case in cases:
            raw = (HERE / "tests/fixtures" / case["file"]).read_text()
            meta = yaml.safe_load(raw.split("---", 2)[1])
            self.assertNotIn(meta["atom_id"], ids)
            ids.add(meta["atom_id"])
            self.assertNotIn("required_failed_checks", raw)
            legacy_checks = {check for group in contract.GROUPS.values() for check in group}
            self.assertTrue(set(case["required_failed_checks"]).issubset(legacy_checks))
        self.assertTrue(any(not c["required_failed_checks"] for c in cases))

    def test_golden_carriers_reach_real_body_checker(self):
        tool_tests = ROOT / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/VALIDATE_ATOMS/tests"
        sys.path.insert(0, str(tool_tests))
        from test_authority_checks import run_check, outcome
        for case in json.loads((HERE / "tests/fixtures/cases.json").read_text()):
            text = (HERE / "tests/fixtures" / case["file"]).read_text()
            meta = yaml.safe_load(text.split("---", 2)[1])
            checked = run_check(["CA-D-479"], meta, text.split("---", 2)[2])
            self.assertEqual(outcome(checked, "body.sections")["outcome"], case["body_check"])

    def test_evidence_cannot_hide_missing_failed_or_blocked_checks(self):
        good = passing_evidence()
        self.assertEqual(validate_evidence(good), "passed")
        for mutation in ("missing", "duplicate", "no_evidence", "failed", "blocked", "unknown"):
            bad = copy.deepcopy(good)
            if mutation == "missing":
                bad["checks"].pop()
            elif mutation == "duplicate":
                bad["checks"][0]["id"] = bad["checks"][1]["id"]
            elif mutation == "no_evidence":
                bad["checks"][0]["evidence"] = []
            else:
                bad["checks"][0]["status"] = mutation
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                validate_evidence(bad)

    def test_failed_result_retains_blockers(self):
        parts = [part(group) for group in contract.GROUPS]
        parts[0]["checks"][0].update(status="failed", findings=[{
            "kind": "violation", "location": "Claim", "excerpt": "must", "reason": "not bold",
            "proposed_fix": "Render **must**", "confidence": 1.0}])
        parts[0]["result"] = "failed"
        parts[1]["checks"][0]["status"] = "blocked"
        parts[1].update(result="blocked", coverage_gaps=[gap("properties", "Missing authority")])
        evidence = merge_evaluations(parts)
        self.assertEqual(validate_evidence(evidence), "failed")
        evidence["coverage_gaps"] = []
        with self.assertRaises(ValueError):
            validate_evidence(evidence)


if __name__ == "__main__":
    unittest.main()
