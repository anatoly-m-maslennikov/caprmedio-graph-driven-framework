"""Actual shared-Run proofs for the two admitted native query Action adapters."""
from __future__ import annotations

import hashlib
import importlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
REPOSITORY = APP.parents[3]
TEST_TEMP_ROOT = REPOSITORY / ".caprmedio_tmp/tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution import SelectedExecution, SelectedExecutionError, build_requested_runs, canonical_json  # noqa: E402
from workflow_run_support import RunTracker  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


class SelectedQueryExecutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / ".git").mkdir()
        self.control = self.root / ".caprmedio_caprmedio"
        self.journal = self.control / "_journal"
        self.journal.mkdir(parents=True)
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[project]\nname = "caprmedio"\n[paths]\ncontrol_root = ".caprmedio_caprmedio"\njournal_root = ".caprmedio_caprmedio/_journal"\nruntime_root = ".caprmedio_runtime"\n',
            encoding="utf-8",
        )
        (self.control / "project_structure.toml").write_text(
            'schema_version = 1\n[[scope_units]]\nscope_unit_name = "CORE_META_MODEL"\nauthority_path = ".caprmedio_caprmedio/core"\ndelivery_path = ".caprmedio_caprmedio/output"\n',
            encoding="utf-8",
        )
        defaults = self.control / "core"
        defaults.mkdir(parents=True)
        (defaults / "caprmedio_framework_default_settings.toml").write_text(
            "[query]\nmax_request_bytes = 4096\nmax_grammar_depth = 16\n"
            "max_filter_tokens = 128\nmax_in_members = 16\nmax_selected_fields = 8\n"
            "max_page_size = 2\nmax_snapshot_members = 256\nmax_file_bytes = 131072\n"
            "max_total_read_bytes = 2097152\ntimeout_seconds = 10\nmax_findings = 8\n",
            encoding="utf-8",
        )
        fixture = GoldenProject(REPOSITORY, self.root, GoldenCase("W15", "find_and_fetch_journal_events"))
        self.manifest = fixture._copy_reviewed_manifest()

    def _execution(self, route: str, parameters: dict[str, object], run_id: str) -> tuple[SelectedExecution, dict[str, object]]:
        manifest = self.manifest
        manifest_ref = ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json"
        definition_ref = next(row["workflow"]["source_path"] for row in manifest["routes"] if row["route"] == route)
        execution: dict[str, object] = {
            "mode": "execute", "request_id": f"request-{run_id}", "operation_route": route,
            "parameters": parameters, "parameters_digest": digest(parameters),
            "target_frontier": [definition_ref], "target_frontier_digest": digest([definition_ref]),
            "effects": [], "effects_digest": digest([]),
            "definition_manifest": {"manifest_ref": manifest_ref, "manifest_digest": manifest["canonical_manifest_sha256"]},
            "source_freshness": manifest["source_freshness"],
            "initiative": {"initiative_id": f"initiative-{run_id}", "instruction_summary": "query fixture", "initiative_ref": definition_ref},
        }
        selected = SelectedExecution(self.root)
        graph = selected._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, run_id)

        def observe(request: dict[str, object]) -> dict[str, object]:
            return {"selected": request.get("operation_route") == route, "current": True,
                    "observed": {"manifest_ref": manifest_ref, "manifest_digest": manifest["canonical_manifest_sha256"]}}

        preview = RunTracker(self.root, source_observer=observe, executor=lambda _request, _session: None).run_selected_operation({**execution, "mode": "preview"})
        execution.update({
            "proposal_receipt": preview["proposal_receipt"],
            "proposal_receipt_digest": preview["proposal_receipt_digest"],
            "assigned_action_id": f"assignment-{run_id}",
            "operator_authorization": {
                "authorization_ref": f"authorizations/{run_id}.json",
                "authorization_freshness": {"state": "current", "digest": "c" * 64},
                "request_id": execution["request_id"], "operation_route": route,
                "proposal_receipt_digest": preview["proposal_receipt_digest"],
                "parameters_digest": execution["parameters_digest"],
                "target_frontier_digest": execution["target_frontier_digest"],
                "effects_digest": execution["effects_digest"],
                "definition_manifest": execution["definition_manifest"],
                "source_freshness": execution["source_freshness"],
            },
        })
        frozen = selected.freeze({"operation": "enqueue_selected", "run_id": run_id, "execution": execution})
        return selected, frozen

    def _progress(self, frozen: dict[str, object]) -> dict[str, object]:
        run_id = frozen["request"]["run_id"]
        action_id = f"{run_id}:step:1:action:1"
        return json.loads((self.root / ".caprmedio_install/workflow_orchestrator/runs" / run_id / f"{action_id}.json").read_text())

    def _events(self) -> list[dict[str, object]]:
        return [
            json.loads(line)
            for path in self.journal.glob("*.ndjson")
            for line in path.read_text(encoding="utf-8").splitlines()
        ]

    def test_journal_query_captures_before_shared_lineage_and_excludes_later_events(self) -> None:
        source = self.journal / "source.ndjson"
        source.write_bytes(b'{"event_id":"E-before","value":1}\n')
        selected, frozen = self._execution("find_and_fetch_journal_events", {"query_request": {"limit": 1}}, "journal-query")
        import query_actions

        original = query_actions.journal_query_action

        def append_after_capture(context):
            source.write_bytes(source.read_bytes() + b'{"event_id":"E-later","value":2}\n')
            return original(context)

        with patch.object(query_actions, "journal_query_action", append_after_capture):
            selected.handlers["CA-O-162"] = append_after_capture
            result = selected.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(3, len(result["run_ids"]))
        progress = self._progress(frozen)
        native = progress["native_result"]
        self.assertEqual(["E-before"], native["results"])
        self.assertEqual(["E-before"], native["snapshot"]["event_ids"])
        self.assertNotIn("E-later", json.dumps(native))
        starts = [event for event in self._events() if event.get("event") == "started"]
        self.assertEqual({"journal-query", "journal-query:step:1", "journal-query:step:1:action:1"}, {event["run"]["run_id"] for event in starts})
        action_start = next(event for event in starts if event["run"]["run_id"].endswith("action:1"))
        self.assertEqual("journal-query:step:1", action_start["run"]["parent_run_id"])

    def test_journal_diagnostic_records_real_failed_lineage_without_source_mutation(self) -> None:
        source = self.journal / "source.ndjson"
        before = b'{"event_id":"E-before","value":1}\n'
        source.write_bytes(before)
        selected, frozen = self._execution(
            "find_and_fetch_journal_events", {"query_request": {"filter": '"event:/value" = __import__("os")'}}, "journal-invalid",
        )
        result = selected.dispatch(frozen)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(before, source.read_bytes())
        progress = self._progress(frozen)
        self.assertEqual("invalid", progress["native_result"]["status"])
        self.assertEqual("failed", next(row for row in result["terminal_runs"] if row["run_id"].endswith("action:1"))["outcome"])

    def test_journal_continuation_reuses_only_the_opaque_retained_handle(self) -> None:
        (self.journal / "source.ndjson").write_bytes(b'{"event_id":"E-1"}\n{"event_id":"E-2"}\n')
        selected, first = self._execution("find_and_fetch_journal_events", {"query_request": {"limit": 1}}, "journal-page-one")
        self.assertEqual("terminal", selected.dispatch(first)["disposition"])
        native = self._progress(first)["native_result"]
        selected, second = self._execution(
            "find_and_fetch_journal_events",
            {"query_request": {"snapshot": native["snapshot"], "cursor": native["next_cursor"], "limit": 1}},
            "journal-page-two",
        )
        self.assertEqual("terminal", selected.dispatch(second)["disposition"])
        self.assertEqual(["E-2"], self._progress(second)["native_result"]["results"])
        tampered = dict(native["snapshot"])
        tampered["event_ids"] = ["INJECTED"]
        selected, rejected = self._execution(
            "find_and_fetch_journal_events",
            {"query_request": {"snapshot": tampered, "cursor": native["next_cursor"], "limit": 1}},
            "journal-tampered",
        )
        self.assertEqual("terminal", selected.dispatch(rejected)["disposition"])
        self.assertEqual("invalid", self._progress(rejected)["native_result"]["status"])
        module = importlib.import_module("FIND_AND_FETCH_JOURNAL_EVENTS.find_and_fetch_journal_events")
        importlib.reload(module)
        selected, unknown = self._execution(
            "find_and_fetch_journal_events",
            {"query_request": {"snapshot": native["snapshot"], "cursor": native["next_cursor"], "limit": 1}},
            "journal-restart",
        )
        self.assertEqual("terminal", selected.dispatch(unknown)["disposition"])
        self.assertEqual("unknown-snapshot", self._progress(unknown)["native_result"]["findings"][0]["code"])

    def test_artifact_query_uses_the_native_tool_result(self) -> None:
        artifact = self.root / "artifact.md"
        artifact.write_text("---\nartifact_id: A-1\ntitle: Example\nstate: open\n---\n# Body\n", encoding="utf-8")
        before = artifact.read_bytes()
        selected, frozen = self._execution(
            "find_and_fetch_artifacts", {"query_request": {"filter": '"fm:/state" = "open"', "select": ["fm:/title"]}}, "artifact-query",
        )
        self.assertEqual("terminal", selected.dispatch(frozen)["disposition"])
        native = self._progress(frozen)["native_result"]
        self.assertEqual([{"artifact_id": "A-1", "fm:/title": "Example"}], native["results"])
        self.assertIn("snapshot", native)
        self.assertEqual({"complete": True, "incomplete": False, "findings": []}, native["diagnostics"])
        self.assertEqual(before, artifact.read_bytes())

    def test_denied_query_shape_creates_no_run_or_event(self) -> None:
        with self.assertRaisesRegex(SelectedExecutionError, "query request is not admitted"):
            self._execution(
                "find_and_fetch_journal_events",
                {"query_request": {"mutation": "delete"}},
                "journal-denied",
            )
        self.assertEqual([], self._events())


if __name__ == "__main__":
    unittest.main()
