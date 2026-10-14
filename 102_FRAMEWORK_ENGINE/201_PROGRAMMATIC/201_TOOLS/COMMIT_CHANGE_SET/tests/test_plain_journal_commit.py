"""Actual fixture commits need source intent, never Journal permission."""

import unittest
from unittest import mock

from commit_change_set_fixture import CommitChangeSetTests, commit_change_set as tool


class PlainJournalCommitTests(unittest.TestCase):
    def setUp(self):
        self.case = CommitChangeSetTests()
        self.case.setUp()
        self.addCleanup(self.case.tearDown)
        self.root = self.case.root

    def context(self):
        return tool.gather_context(self.root, self.case.trigger())

    def assert_refused(self, context, code):
        before = self.case.snapshot()
        with self.assertRaises(tool.ToolError) as raised:
            tool.run(self.root, {"context": context}, apply=True)
        self.assertEqual(raised.exception.code, code)
        self.assertEqual(self.case.snapshot(), before)

    def test_context_commit_has_no_journal_receipt_or_lease(self):
        context = self.context()
        before = self.case.git("rev-parse", "HEAD").strip()
        with mock.patch.object(tool, "_import_appender", side_effect=AssertionError):
            result = tool.run(self.root, {"context": context}, apply=True)
        self.assertNotEqual(result["commit"], before)
        self.assertEqual(self.case.git("rev-parse", "HEAD^").strip(), before)
        self.assertEqual(
            self.case.git("show", "--format=", "--name-only", "HEAD").strip(), self.case.subject
        )
        self.assertEqual(
            self.case.git("show", "-s", "--format=%B", "HEAD").strip(), result["git_message"]
        )
        self.assertFalse((self.root / ".caprmedio_caprmedio/_journal").exists())

    def test_malformed_prior_journal_is_not_commit_permission(self):
        journal = self.root / ".caprmedio_caprmedio/_journal/history.ndjson"
        journal.parent.mkdir()
        journal.write_bytes(b'not json\n{"event_id":"reused"}\n')
        context = self.context()
        tool.run(self.root, {"context": context, "receipts": [], "lease": {}}, apply=True)
        self.assertEqual(journal.read_bytes(), b'not json\n{"event_id":"reused"}\n')

    def test_trigger_logging_failure_does_not_undo_or_block_commit(self):
        with mock.patch.object(tool, "_import_appender", side_effect=OSError("log unavailable")):
            result = tool.run(self.root, {"trigger": self.case.trigger()}, apply=True)
        self.assertEqual(result["commit"], self.case.git("rev-parse", "HEAD").strip())
        self.assertEqual(result["diagnostics"][0]["code"], "journal-append-failed")

    def test_dry_run_has_no_effect(self):
        before = self.case.snapshot()
        tool.run(self.root, {"trigger": self.case.trigger()}, apply=False)
        self.assertEqual(self.case.snapshot(), before)

    def test_context_without_predicted_journal_rows_commits(self):
        context = self.context()
        context["predictions"] = {}
        result = tool.run(self.root, {"context": context}, apply=True)
        self.assertEqual(result["commit"], self.case.git("rev-parse", "HEAD").strip())

    def test_optional_claimed_prior_does_not_control_actual_commit_message(self):
        context = self.context()
        context["previous_result"] = {"path": "not-an-actual-before-state"}
        context["previous_result_event"] = "unobserved-journal-link"
        result = tool.run(self.root, {"context": context}, apply=True)
        self.assertEqual(result["git_message"], result["context"]["predictions"]["git_message"])

    def test_trigger_appends_actual_change_after_commit_only(self):
        result = tool.run(self.root, {"trigger": self.case.trigger()}, apply=True)
        self.assertNotIn("diagnostics", result)
        self.assertEqual(len(result["receipts"]), 1)
        journal = self.root / result["receipts"][0]["carrier"]
        self.assertEqual(len(journal.read_bytes().splitlines()), 1)
        self.assertEqual(
            self.case.git("show", "--format=", "--name-only", "HEAD").strip(),
            self.case.subject,
        )

    def test_post_commit_observes_without_prior_journal_or_dedup(self):
        tool.run(self.root, {"context": self.context()}, apply=True)
        first = tool.observe_post_commit(self.root)
        second = tool.observe_post_commit(self.root)
        self.assertTrue(first["valid"] and second["valid"])
        log = self.root / first["observation"]
        self.assertEqual(len(log.read_bytes().splitlines()), 2)

    def test_stale_git_base_refused(self):
        context = self.context()
        self.case.git("commit", "--allow-empty", "-qm", "other commit")
        self.assert_refused(context, "stale-context")

    def test_stale_source_bytes_refused(self):
        context = self.context()
        with (self.root / self.case.subject).open("ab") as stream:
            stream.write(b"changed\n")
        self.assert_refused(context, "stale-context")

    def test_unrelated_staged_path_refused(self):
        context = self.context()
        (self.root / "unrelated.txt").write_text("unrelated\n")
        self.case.git("add", "unrelated.txt")
        self.assert_refused(context, "unrelated-staged-change")

    def test_stale_relation_refused(self):
        context = self.context()
        parent = self.root / ".caprmedio_caprmedio/04_requirement/CA-R-001-REQUIREMENT--parent.md"
        with parent.open("ab") as stream:
            stream.write(b"changed\n")
        self.assert_refused(context, "stale-context")

    def test_tampered_context_refused(self):
        context = self.context()
        context["result"]["sha256"] = "0" * 64
        self.assert_refused(context, "context_identity_mismatch")

    def test_hook_needs_no_journal_and_accepts_actual_message(self):
        self.case.git("add", self.case.subject)
        self.assertTrue(tool.evaluate_pre_commit(self.root)["governed"])
        message = self.root / ".git/message"
        message.write_text("actual change\n")
        self.assertTrue(tool.evaluate_commit_message(self.root, message)["message_valid"])

    def test_hook_preserves_whitespace_refusal(self):
        with (self.root / self.case.subject).open("ab") as stream:
            stream.write(b"bad trailing whitespace \n")
        self.case.git("add", self.case.subject)
        with self.assertRaises(tool.ToolError) as raised:
            tool.evaluate_pre_commit(self.root)
        self.assertEqual(raised.exception.code, "staged-content-invalid")

    def test_hook_preserves_forbidden_path_refusal(self):
        runtime = self.root / ".caprmedio_runtime/unsafe.txt"
        runtime.parent.mkdir()
        runtime.write_text("local only\n")
        self.case.git("add", "-f", str(runtime))
        with self.assertRaises(tool.ToolError) as raised:
            tool.evaluate_pre_commit(self.root)
        self.assertEqual(raised.exception.code, "local-machine-path-staged")

    def test_commit_verifies_tree_and_message(self):
        context = self.context()
        result = tool.run(self.root, {"context": context}, apply=True)
        arguments = dict(
            parent=context["git_base"]["commit"],
            message=result["git_message"],
            expected_paths={self.case.subject},
            expected_tree=self.case.git("rev-parse", "HEAD^{tree}").strip(),
        )
        for field, value in (
            ("message", "wrong"),
            ("expected_paths", set()),
            ("expected_tree", "0" * 40),
            ("parent", "0" * 40),
        ):
            with self.subTest(field=field), self.assertRaises(tool.ToolError):
                tool._verify_commit(self.root, **{**arguments, field: value})


if __name__ == "__main__":
    unittest.main()
