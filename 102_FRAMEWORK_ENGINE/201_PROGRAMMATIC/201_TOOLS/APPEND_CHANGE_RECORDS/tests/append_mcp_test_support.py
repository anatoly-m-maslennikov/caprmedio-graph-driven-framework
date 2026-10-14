"""Shared composition fixture; this module contains no collected TestCase."""

from __future__ import annotations

import copy
import json
from pathlib import Path
import sys

TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))
import test_append_change_records as native_tests  # noqa: E402
import append_change_records as appender  # noqa: E402
import work_journal  # noqa: E402


class AppendMcpFixture:
    def setUp(self) -> None:
        self.fixture = native_tests.AppendChangeRecordsTest("test_dry_run_is_mutation_free")
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root.resolve()
        self.adapter = appender.create_adapter(self.root)

    def _context(
        self, *, action_id: str = "observed-action-one", replacement: bool = False
    ) -> dict:
        context = self.fixture.context(action="MOVE+UPDATE" if replacement else "ADD")
        context["action_id"] = action_id
        event = context["predictions"]["journal_records"][0]
        event["action_id"] = action_id
        if replacement:
            context["previous_result_event"] = event["previous_result_event"]
            event.update(
                predecessor_atom_id="CA-D-562", successor_atom_ids=["CA-D-634", "CA-D-635"]
            )
        event["event_id"] = appender._expected_event_id(event)
        context["predictions"]["journal_records"] = [work_journal.with_event_digest(event)]
        context["context_id"] = appender._expected_context_id(context)
        return context

    def _events(self) -> list[dict]:
        journal = self.root / ".caprmedio_caprmedio/_journal"
        return [
            json.loads(line)
            for path in sorted(journal.glob("*.ndjson"))
            for line in path.read_text().splitlines()
        ]

    def _apply(self, context: dict) -> dict:
        return self.adapter.invoke({"context": context, "apply": True})

    def _recovery_context(self) -> dict:
        context = self._context(replacement=True)
        result = copy.deepcopy(context["result"])
        evidence = {
            "git": {"base_commit": context["git_base"]["commit"]},
            "carrier": {"path": result["path"], "sha256": result["sha256"]},
        }
        recovered = {
            key: context[key]
            for key in (
                "schema_version",
                "action_id",
                "author",
                "occurred_at",
                "llm_session",
                "structural_scope",
            )
        }
        recovered.update(
            event="recovered",
            kind="governed_project_state",
            subject_kind="file",
            result=result,
            recovery_evidence=evidence,
        )
        recovered["event_id"] = appender._expected_event_id(recovered)
        recovered = work_journal.with_event_digest(recovered)
        completed = context["predictions"]["journal_records"][0]
        completed["previous_result_event"] = recovered["event_id"]
        completed["event_id"] = appender._expected_event_id(completed)
        context["predictions"]["journal_records"] = [
            recovered,
            work_journal.with_event_digest(completed),
        ]
        context["previous_result_event"] = recovered["event_id"]
        context["recovery"] = {
            "event_id": recovered["event_id"],
            "result": result,
            "evidence": evidence,
            "evidence_digest": work_journal.canonical_json_digest(evidence),
            "contradictions": [],
        }
        context["context_id"] = appender._expected_context_id(context)
        return context
