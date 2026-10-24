"""Definition-only checks; no native adapter, live Project, or MCP required."""

import json
from pathlib import Path
import re
import unittest


HERE = Path(__file__).resolve().parents[1]
EXPECTED = {
    "CA-O-231": "CA-O-017",
    "CA-O-232": "CA-O-018",
    "CA-O-233": "CA-O-019",
    "CA-O-094": "CA-O-020",
    "CA-O-234": "CA-O-089",
    "CA-O-096": "CA-O-024",
    "CA-O-099": "CA-O-021",
    "CA-O-230": "CA-O-225",
}


class SharedDefinitionContracts(unittest.TestCase):
    def test_exact_step_action_integrated_bindings(self):
        self.assertEqual(
            {p.stem.removesuffix(".prompt") for p in HERE.glob("*.prompt.md")}, set(EXPECTED)
        )
        for step, action in EXPECTED.items():
            with self.subTest(step=step):
                text = (HERE / f"{step}.prompt.md").read_text()
                self.assertIn(f"Step: {step} | Action: {action} | Context: Integrated", text)
                self.assertNotIn("Context: Isolated", text)
                self.assertIn("complete common input packet", text)
                self.assertIn("permission", text)

    def test_frontier_is_definition_only_not_runtime_admission(self):
        frontier = json.loads((HERE / "definition_frontier.projection.json").read_text())
        self.assertEqual(frontier["kind"], "definition_only_source_frontier")
        self.assertIs(frontier["runtime_admitted"], False)
        self.assertEqual(frontier["steps"], EXPECTED)
        sources = {row["atom_id"]: row for row in frontier["sources"]}
        self.assertEqual(len(sources), len(frontier["sources"]))
        for row in sources.values():
            self.assertGreater(row["version"], 0)
            self.assertRegex(row["sha256"], r"^[a-f0-9]{64}$")
            self.assertTrue(row["path"].startswith(".caprmedio_caprmedio/"))

    def test_shared_packet_keeps_authority_and_actual_evidence(self):
        readme = (HERE / "README.md").read_text()
        for name in (
            "selected_project",
            "plan",
            "requirements_and_delivery",
            "methods",
            "method_projection",
            "applicable_evaluations",
            "source_revisions",
            "candidate",
            "permissions",
            "retry",
            "evidence",
        ):
            self.assertIn(f"`{name}`", readme)
        self.assertIn("persistent Plan", readme)
        self.assertIn("Native realization is pending", readme)
        self.assertIn("not admitted", readme)

    def test_methods_use_source_rows_and_legacy_projection_is_optional(self):
        readme = (HERE / "README.md").read_text()
        self.assertIn("Method SourceRows", readme)
        self.assertIn("optional legacy", readme)
        self.assertIn("No paragraph compiler or", readme)
        self.assertIn("validated independently", readme)
        for step in EXPECTED:
            prompt = (HERE / f"{step}.prompt.md").read_text()
            self.assertIn("full current Method SourceRows", prompt)
            self.assertIn("optional legacy `method_projection` is not required", prompt)
            self.assertNotIn("full current M projection", prompt)

    def test_integrated_pending_handoff_returns_through_the_same_mcp_operation(self):
        readme = (HERE / "README.md").read_text()
        self.assertIn("pending handoff", readme)
        self.assertIn("same MCP operation", readme)
        self.assertIn("`submit_result`", readme)
        self.assertIn("does\nnot complete the Plan", readme)
        self.assertIn("independent `child_of`", readme)

    def test_review_requires_explicit_phase_and_never_accepts_preliminary(self):
        review = (HERE / "CA-O-230.prompt.md").read_text()
        self.assertIn("caller-supplied", review)
        self.assertIn("When omitted or invalid, return `unresolved`", review)
        self.assertIn("complete selected code/policy assessment", review)
        self.assertIn("no confirmed findings", review)
        self.assertIn("listing pending checks", review)
        self.assertIn("not `passed`", review)
        self.assertIn("Do not edit code", review)

    def test_result_sets_are_unique_and_review_is_phase_aware(self):
        for step in EXPECTED:
            text = (HERE / f"{step}.prompt.md").read_text()
            result = re.search(r"Results: ([\s\S]*?)\.", text)
            self.assertIsNotNone(result, step)
            labels = re.findall(r"`([a-z_]+)`", result[1])
            self.assertEqual(len(labels), len(set(labels)), step)
        review = (HERE / "CA-O-230.prompt.md").read_text()
        for label in ("preliminary_clear", "passed", "findings", "partial", "unresolved"):
            self.assertIn(f"`{label}`", review)

    def test_preparation_and_repair_keep_review_and_check_closure(self):
        prepare = (HERE / "CA-O-231.prompt.md").read_text()
        repair = (HERE / "CA-O-099.prompt.md").read_text()
        self.assertIn("`review_ready`", prepare)
        self.assertIn("R/M/D obligations", prepare)
        self.assertIn("same candidate", prepare)
        self.assertIn("mark affected previous review/check evidence", repair)
        self.assertIn("remaining budget", repair)

    def test_final_checks_require_current_preliminary_clearance(self):
        checks = (HERE / "CA-O-094.prompt.md").read_text()
        self.assertIn("For final checks require actual `preliminary_clear`", checks)
        self.assertIn("this exact", checks)
        self.assertIn("candidate and relevant source/test/input bindings", checks)
        self.assertIn("If it is missing or stale", checks)
        self.assertIn("return `blocked`, never `passed`", checks)
        self.assertIn("baseline checks", checks)
        self.assertIn("do not require preliminary clearance", checks)

    def test_summary_replacements_use_distinct_current_source_identities(self):
        frontier = json.loads((HERE / "definition_frontier.projection.json").read_text())
        ids = {row["atom_id"] for row in frontier["sources"]}
        self.assertTrue({"CA-O-231", "CA-O-232", "CA-O-233", "CA-O-234", "CA-E-652"} <= ids)
        self.assertFalse({"CA-O-091", "CA-O-092", "CA-O-093", "CA-O-095", "CA-E-519"} & ids)


if __name__ == "__main__":
    unittest.main()
