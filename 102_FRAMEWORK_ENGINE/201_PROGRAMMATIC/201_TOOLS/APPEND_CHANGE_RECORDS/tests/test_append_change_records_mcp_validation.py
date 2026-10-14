"""Project-bound MCP append checks using the actual Journal writer."""

import copy
import unittest

from pydantic import ValidationError

from append_mcp_test_support import AppendMcpFixture, appender, native_tests, work_journal


class AppendMcpValidationTest(AppendMcpFixture, unittest.TestCase):
    def test_actual_stored_event_identity_collision_refuses_without_rewriting_history(self) -> None:
        context = self._context(replacement=True)
        original = context["predictions"]["journal_records"][0]
        conflicting = copy.deepcopy(original)
        conflicting["successor_atom_ids"] = ["CA-D-633"]
        conflicting = work_journal.with_event_digest(conflicting)
        work_journal.append_sealed_events(
            self.root,
            [conflicting],
            author=context["author"],
            local_date=context["local_date"],
            timezone=context["timezone"],
        )
        with self.assertRaises(work_journal.WorkJournalError) as refused:
            self._apply(context)
        self.assertEqual("identity-collision", refused.exception.code)
        self.assertEqual([conflicting], self._events())

    def test_foreign_project_context_is_refused_before_any_append(self) -> None:
        foreign = native_tests.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        foreign.setUp()
        self.addCleanup(foreign.tearDown)
        context = foreign.context()
        with self.assertRaises(appender.ToolError) as refused:
            self._apply(context)
        self.assertEqual("descriptor-root-mismatch", refused.exception.code)
        self.assertEqual([], self._events())
        self.assertFalse((foreign.root / ".caprmedio_caprmedio/_journal").exists())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_closed_request_and_strict_apply_reject_before_writes(self) -> None:
        for request in (
            {},
            {"context": self._context(), "root": str(self.root)},
            {"context": self._context(), "wait_seconds": 0},
            {"context": self._context(), "event": {}},
            *({"context": self._context(), "apply": value} for value in (1, 0, "true", None)),
        ):
            with self.subTest(request=request):
                with self.assertRaises(ValidationError):
                    appender.AppendChangeRecordsRequest.model_validate(request)
        self.assertEqual([], self._events())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())

    def test_event_digest_tamper_refuses_without_pending_or_append(self) -> None:
        context = self._context(replacement=True)
        context["predictions"]["journal_records"][0]["successor_atom_ids"] = ["CA-D-633"]
        with self.assertRaises(work_journal.WorkJournalError) as refused:
            self._apply(context)
        self.assertEqual("event-digest-mismatch", refused.exception.code)
        self.assertEqual([], self._events())
        self.assertFalse((self.root / ".caprmedio_runtime").exists())


if __name__ == "__main__":
    unittest.main()
