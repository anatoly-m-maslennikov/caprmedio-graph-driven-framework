# CA-E-796@1
"""Static contract checks for the short Implementation Workflow prompts."""

import re
import unittest
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]


class PromptContracts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prompts = {
            p.name.removesuffix(".prompt.md"): p.read_text(encoding="utf-8")
            for p in HERE.glob("*.prompt.md")
        }

    def test_prompt_bindings_have_step_action_and_context(self):
        for step, prompt in self.prompts.items():
            with self.subTest(step=step):
                binding = re.search(
                    r"^Step: (CA-O-\d+) \| Action: (CA-O-\d+) \| Context: (Integrated|Isolated)$",
                    prompt,
                    re.M,
                )
                self.assertIsNotNone(binding)
                self.assertEqual(binding[1], step)

    def test_prompt_result_labels_are_unique(self):
        for step, prompt in self.prompts.items():
            with self.subTest(step=step):
                actual = re.search(r"^Results: (.+)$", prompt, re.M)[1].split(" | ")
                self.assertEqual(len(actual), len(set(actual)))

    def test_prompts_are_short_and_grounded(self):
        for step, prompt in self.prompts.items():
            with self.subTest(step=step):
                self.assertTrue(prompt.startswith("# System Prompt\n"))
                self.assertLessEqual(len(prompt.split()), 160)
                self.assertIn("pinned authority and input packet", prompt)
                self.assertNotIn("methods_ready", prompt)
                self.assertNotRegex(prompt, r"\b(?:TODO|TBD)\b|\{\{")
                self.assertIn("permission", prompt)
                self.assertIn("Return", prompt)

    def test_testing_and_learning_boundaries(self):
        tests = self.prompts["CA-O-092"]
        self.assertIn("E2E tests first", tests)
        self.assertIn("golden corpus", tests)
        self.assertIn("Mock external boundaries, not the implementation", tests)
        self.assertIn("Do not create or promote M Atoms", self.prompts["CA-O-099"])
        self.assertIn("Method learning is separate", self.prompts["CA-O-091"])
        self.assertIn("initial failed Evaluation consumes zero retries", self.prompts["CA-O-096"])

    def test_preparation_packet_separates_what_how_and_checks(self):
        prompt = self.prompts["CA-O-091"]
        for fragment in (
            "R + D implementation targets",
            "E separately as checks",
            "all active Ms",
            "into one file",
            "full content and source bindings",
            "completeness and freshness",
            "does not establish applicability",
        ):
            self.assertIn(fragment, prompt)
        readme = (HERE / "README.md").read_text(encoding="utf-8")
        for fragment in (
            "**what to implement**",
            "**how to implement**",
            "**what to check**",
            "same verified file binding downstream",
        ):
            self.assertIn(fragment, readme)

    def test_prompt_runtime_contract_is_not_live_llm_proof(self):
        readme = (HERE / "README.md").read_text(encoding="utf-8")
        self.assertIn("Automatic Agent dispatch is retired.", readme)
