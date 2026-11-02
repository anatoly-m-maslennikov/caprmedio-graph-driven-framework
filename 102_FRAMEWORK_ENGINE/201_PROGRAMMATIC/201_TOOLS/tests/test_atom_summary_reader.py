"""Summary comparison follows real headings without changing candidate schema admission."""

from pathlib import Path
import sys
import unittest
from dataclasses import replace
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

import atom_operations as operations  # noqa: E402
from lifecycle_intents import LifecycleError, _source_summary, _summary  # noqa: E402


class AtomSummaryReaderTests(unittest.TestCase):
    @staticmethod
    def _plan_source(content):
        return operations.Atom(Path("/unused/plan.md"), "plan.md", "plan.md", "CA-P-2694",
            "active", "03_plan", "content_role: Plan\ntype: Plan\nstatus: Active", content)

    def test_rmed_h2_and_legacy_h1_have_the_same_summary_value(self):
        for role in ("Requirement", "Method", "Evaluation", "Delivery"):
            for heading in ("# Summary", "## Summary"):
                with self.subTest(role=role, heading=heading):
                    body = heading + "\n\nThe preserved Summary.\n\n## Claim\n\nClaim text.\n"
                    self.assertEqual("The preserved Summary.", operations._draft_summary(body, content_role=role))
                    self.assertEqual("The preserved Summary.", _summary(body, content_role=role))

    def test_existing_h1_rmed_summary_can_be_compared_to_current_h2_draft(self):
        canonical = operations.Atom(Path("/unused/current.md"), "current.md", "current.md", "CA-R-123",
            "active", "04_requirement", "content_role: Requirement\ntype: Rule\nstatus: Active",
            "# Summary\n\nSame immutable value.\n\n## Claim\n\nClaim.\n")
        draft = replace(canonical, atom_id=None, lifecycle="draft",
            frontmatter=canonical.frontmatter.replace("Active", "Draft"),
            content=canonical.content.replace("# Summary", "## Summary", 1))
        self.assertFalse(operations._existing_draft_preserves_canonical(draft, canonical))

    def test_other_roles_keep_h1_summary_layout(self):
        for role in ("Concern", "Analysis", "Plan", "Operations"):
            with self.subTest(role=role):
                self.assertEqual("Same value", _summary("# Summary\n\nSame value\n\n## Details\n", content_role=role))
                with self.assertRaises(LifecycleError):
                    _summary("## Summary\n\nSame value\n\n## Details\n", content_role=role)

    def test_identified_plan_source_accepts_legacy_h1_and_h2_summary(self):
        for heading in ("# Summary", "## Summary"):
            with self.subTest(heading=heading):
                source = self._plan_source(heading + "\n\nSame source value.\n\n## Objective\n\nObjective.\n")
                self.assertEqual("Same source value.", _source_summary(source))

    def test_identified_plan_source_rejects_duplicate_misplaced_and_fenced_summary(self):
        for content in (
            "# Summary\n\nFirst.\n\n## Summary\n\nSecond.\n",
            "# Objective\n\nBefore.\n\n## Summary\n\nMisplaced.\n",
            "```markdown\n## Summary\n\nFenced fake.\n```\n\n# Objective\n\nNo real Summary.\n",
        ):
            with self.subTest(content=content):
                with self.assertRaises(LifecycleError):
                    _source_summary(self._plan_source(content))

    def test_h2_canonical_plan_and_h1_draft_bind_only_when_summary_matches(self):
        canonical = self._plan_source("## Summary\n\nSame value.\n\n## Objective\n\nObjective.\n")
        draft = replace(canonical, atom_id=None, lifecycle="draft",
            content="# Summary\n\nSame value.\n\n## Objective\n\nObjective.\n")
        marker = operations.DraftMarker("CA-P-2694@38-draft", "CA-P-2694", 38)
        binding_patches = (
            patch.object(operations, "_bind_existing_draft_marker", return_value=(marker, 38)),
            patch.object(operations, "_require_exact_current_canonical"),
            patch.object(operations, "atom_version", return_value=37),
        )
        with binding_patches[0], binding_patches[1], binding_patches[2]:
            binding = operations.bind_existing_draft_promotion(Path("/unused"), draft, canonical, proposed_version=38)
        self.assertFalse(binding.no_op)

        changed = replace(draft, content=draft.content.replace("Same value.", "Changed value."))
        with patch.object(operations, "_bind_existing_draft_marker", return_value=(marker, 38)), \
                patch.object(operations, "_require_exact_current_canonical"), \
                patch.object(operations, "atom_version", return_value=37):
            with self.assertRaises(operations.ToolError) as error:
                operations.bind_existing_draft_promotion(Path("/unused"), changed, canonical, proposed_version=38)
        self.assertEqual("summary-changed", error.exception.code)

    def test_real_outline_rejects_missing_empty_duplicate_and_misplaced_summary(self):
        for body in (
            "```markdown\n## Summary\n\nFenced fake\n```\n",
            "## Summary\n\n## Claim\n\nNot a Summary value.\n",
            "## Summary\n\n### Child\n\nNot a direct Summary value.\n",
            "## Claim\n\nBefore.\n\n## Summary\n\nValue\n",
            "# Summary\n\nFirst.\n\n## Summary\n\nSecond.\n",
            "## Summary\n\nFirst.\n\n## Summary\n\nSecond.\n",
            "## Summary\n\nFirst.\n\n### SUMMARY\n\nSecond.\n",
        ):
            with self.subTest(body=body):
                with self.assertRaises(LifecycleError):
                    _summary(body, content_role="Requirement")

    def test_fenced_heading_is_content_and_complete_summary_value_is_preserved(self):
        value = "First line.\nSecond line.\n\n```markdown\n## Claim\n```"
        body = "## Summary\n\n" + value + "\n\n## Claim\n\nActual claim.\n"
        self.assertEqual(value, _summary(body, content_role="Requirement"))


if __name__ == "__main__":
    unittest.main()
