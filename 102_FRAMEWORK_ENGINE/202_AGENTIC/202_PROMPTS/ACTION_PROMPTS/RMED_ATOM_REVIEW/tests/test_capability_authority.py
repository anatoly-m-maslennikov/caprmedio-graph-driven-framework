"""Prompt/authority regressions; not a substitute for agentic semantic evaluation."""
from pathlib import Path
import unittest

HERE = Path(__file__).resolve().parents[1]


def text(name):
    return " ".join((HERE / name).read_text().split())


class CapabilityAuthority(unittest.TestCase):
    def test_gather_check_and_fix_all_receive_authority(self):
        for name in ("CA-O-108.prompt.md", "CA-O-109.prompt.md",
                     "CA-O-110.prompt.md", "evaluate_coherence.prompt.md",
                     "repair/propose_repair.prompt.md"):
            with self.subTest(name=name):
                self.assertIn("CA-R-1799", text(name))

    def test_checker_preserves_approved_automation_and_mandatory_safeguards(self):
        check = text("evaluate_coherence.prompt.md")
        for boundary in ("explicit prior authorization", "Workflow or automation",
                         "gates and safeguards", "remain mandatory",
                         "missing repeated approval wording alone is not a violation",
                         "Unresolved intent is a coverage gap"):
            self.assertIn(boundary, check)

    def test_checker_has_positive_and_negative_examples(self):
        check = text("evaluate_coherence.prompt.md")
        self.assertIn("provide a rebuild capability", check)
        self.assertIn("during an authorized rebuild, validate the output", check)
        self.assertIn("rebuild even without Operator authorization", check)
        self.assertIn('unspecified "the Projection"', check)
        self.assertIn("not an invented target", check)

    def test_fixer_needs_known_intent_and_permission_for_semantic_change(self):
        check = text("CA-O-110.prompt.md")
        for boundary in ("known capability/target", "authorized meaning change",
                         "Preserve safeguards and authorized-run obligations",
                         "never mechanically weaken", "Retirement needs explicit authority"):
            self.assertIn(boundary, check)
        repair = text("repair/propose_repair.prompt.md")
        for boundary in ("semantic change is authorized", "Unknown intent blocks repair",
                         "Never mechanically replace", "invent a Projection",
                         "Retirement requires explicit authority"):
            self.assertIn(boundary, repair)

    def test_scope_check_fix_and_no_recheck_remain(self):
        self.assertIn("no seventh check or review stage", text("README.md"))
        self.assertIn("does not recheck saved output", text("CA-O-110.prompt.md"))
        self.assertIn("every required check before this Atom's fix phase",
                      text("CA-O-109.prompt.md"))


if __name__ == "__main__":
    unittest.main()
