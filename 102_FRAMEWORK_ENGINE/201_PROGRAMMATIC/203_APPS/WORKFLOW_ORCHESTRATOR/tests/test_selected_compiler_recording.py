"""Real shared-recording proof for the CA-O-011 compiler publication edge."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path.insert(0, str(APP))
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "COMPILE_APPLICABLE_METHODOLOGY"))

import compile_applicable_methodology as compiler  # noqa: E402
import work_journal  # noqa: E402
from selected_execution import SelectedExecution, build_requested_runs, canonical_json  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject  # noqa: E402


def digest(value: object) -> str:
    return hashlib.sha256(canonical_json(value)).hexdigest()


def carrier(atom_id: str, *, version: int = 1) -> bytes:
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        "cce_form: obligation\n"
        "status: Active\n"
        f"version: {version}\n"
        "updated_at: 2026-10-05 00:00:00 +0400\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\nclaim\n"
    ).encode()


class SelectedCompilerRecordingTest(unittest.TestCase):
    """Actual publication and Run outcomes remain separate from Journal I/O."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / ".git").mkdir()
        self.control = self.root / ".caprmedio_caprmedio"
        self.control.mkdir()
        (self.control / "caprmedio_project_settings.toml").write_text(
            '[paths]\ncontrol_root = ".caprmedio_caprmedio"\n', encoding="utf-8"
        )
        self.source = self.control / "000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources"
        for layer in ("001_CORE_META_MODEL", "003_PROJECT_CONFIGURATION"):
            for role in compiler.ROLE_BY_DIRECTORY:
                (self.source / layer / role).mkdir(parents=True, exist_ok=True)
        (self.source / "002_INSTALLED_EXTENSIONS").mkdir(parents=True)
        (self.control / "project_structure.toml").write_text(
            "[[scope_units]]\n"
            'scope_unit_name = "METHODOLOGY_SOURCES"\n'
            f"authority_path = {json.dumps(self.source.relative_to(self.root).as_posix())}\n",
            encoding="utf-8",
        )
        (self.source / "001_CORE_META_MODEL/caprmedio_framework_default_settings.toml").write_text("", encoding="utf-8")
        (self.source / "003_PROJECT_CONFIGURATION/caprmedio_framework_settings.toml").write_text("", encoding="utf-8")
        self.core = self.source / "001_CORE_META_MODEL/04_requirement/CA-R-001--core.md"
        self.core.write_bytes(carrier("CA-R-001"))
        self._write_manifest()

    def _write_manifest(self) -> None:
        fixture = GoldenProject(APP.parents[3], self.root, GoldenCase("W13", "build_applicable_methodology"))
        value = fixture._copy_reviewed_manifest()
        self.source_freshness = value["source_freshness"]
        self.manifest = self.control / "_projection/selected_workflow_bindings.json"

    def _compiler_parameters(self) -> dict[str, object]:
        places = compiler.methodology_paths(self.root)
        bindings = compiler.governed_bindings(self.root, places)
        assessed = compiler.run_request({
            "operation": "dry_run",
            "project_root": self.root.as_posix(),
            "governed_bindings": bindings,
        })
        self.assertEqual("assessed", assessed["outcome"])
        return {
            "operation": "apply",
            "project_root": self.root.as_posix(),
            "governed_bindings": bindings,
            "expected_source_frontier_digest": assessed["source_frontier_digest"],
        }

    def _request(self, run_id: str) -> tuple[SelectedExecution, dict[str, object]]:
        manifest = json.loads(self.manifest.read_text(encoding="utf-8"))
        parameters = self._compiler_parameters()
        manifest_ref = self.manifest.relative_to(self.root).as_posix()
        definition_manifest = {
            "manifest_ref": manifest_ref,
            "manifest_digest": manifest["canonical_manifest_sha256"],
        }
        target_frontier = [self.core.relative_to(self.root).as_posix()]
        effects = [{"type": "publish", "target": ".caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY"}]
        execution: dict[str, object] = {
            "mode": "execute",
            "request_id": f"request-{run_id}",
            "operation_route": "build_applicable_methodology",
            "parameters": parameters,
            "parameters_digest": digest(parameters),
            "target_frontier": target_frontier,
            "target_frontier_digest": digest(target_frontier),
            "effects": effects,
            "effects_digest": digest(effects),
            "definition_manifest": definition_manifest,
            "source_freshness": self.source_freshness,
            "initiative": {
                "initiative_id": "compiler-recording-fixture",
                "instruction_summary": "record publication through the actual selected Action Run",
                "initiative_ref": self.core.relative_to(self.root).as_posix(),
            },
        }
        runner = SelectedExecution(self.root)
        graph = runner._validate_graph(execution)
        execution["requested_runs"] = build_requested_runs(graph, run_id)
        proposal = {
            "request_id": execution["request_id"],
            "operation_route": execution["operation_route"],
            "initiative_ref": execution["initiative"]["initiative_ref"],
            "source_freshness": {
                "declared": self.source_freshness,
                "observed": {
                    "manifest_ref": manifest_ref,
                    "manifest_digest": manifest["canonical_manifest_sha256"],
                },
                "selected": True,
                "current": True,
            },
            "parameters_digest": execution["parameters_digest"],
            "target_frontier_digest": execution["target_frontier_digest"],
            "effects_digest": execution["effects_digest"],
            "definition_manifest": definition_manifest,
        }
        proposal_digest = digest(proposal)
        execution.update({
            "proposal_receipt": proposal,
            "proposal_receipt_digest": proposal_digest,
            "assigned_action_id": "compiler-recording-fixture",
            "operator_authorization": {
                "authorization_ref": "authorizations/compiler-recording.json",
                "authorization_freshness": {"state": "current", "digest": "c" * 64},
                "request_id": execution["request_id"],
                "operation_route": execution["operation_route"],
                "proposal_receipt_digest": proposal_digest,
                "parameters_digest": execution["parameters_digest"],
                "target_frontier_digest": execution["target_frontier_digest"],
                "effects_digest": execution["effects_digest"],
                "definition_manifest": definition_manifest,
                "source_freshness": self.source_freshness,
            },
        })
        return runner, {"operation": "enqueue_selected", "run_id": run_id, "execution": execution}

    def _projection_bytes(self) -> dict[str, bytes]:
        """Return generated members, excluding co-located authoritative sources."""
        output = self.root / compiler.methodology_paths(self.root).output
        return {
            path.relative_to(output).as_posix(): path.read_bytes()
            for _, role_directory in compiler.ROLES
            for path in sorted((output / role_directory).rglob("*"))
            if path.is_file()
        }

    def _journal_events(self) -> list[dict[str, object]]:
        journal_root = self.control / "_journal"
        return [
            json.loads(line)
            for path in journal_root.glob("*.ndjson")
            for line in path.read_text(encoding="utf-8").splitlines()
        ]

    def test_compiler_publication_retains_actual_action_outcome_and_output(self) -> None:
        runner, request = self._request("compiler-recorded")
        result = runner.dispatch(runner.freeze(request))

        self.assertEqual("terminal", result["disposition"])
        expected = {row["requested_run_id"]: row for row in request["execution"]["requested_runs"]}
        self.assertEqual({"completed"}, {row["outcome"] for row in result["terminal_runs"]})
        projection = self._projection_bytes()
        self.assertEqual({"04_requirement/CA-R-001--core.md"}, set(projection))
        graph_result = json.loads((runner.run_directory("compiler-recorded") / "graph_result.json").read_text(encoding="utf-8"))
        actual = {graph_result["workflow_run_id"]}
        for row in graph_result["step_results"]:
            actual.update((row["step_run_id"], row["action_run_id"]))
        self.assertEqual(actual, set(result["run_ids"]))
        self.assertLessEqual(actual, set(expected))
        self.assertEqual(
            "completed publication from the still-valid final frontier",
            graph_result["step_results"][-1]["result"],
        )
        action_progress = runner.run_directory("compiler-recorded") / f"{graph_result['step_results'][-1]['action_run_id']}.json"
        progress = json.loads(action_progress.read_text(encoding="utf-8"))
        native = progress["native_result"]
        self.assertEqual("completed publication from the still-valid final frontier", progress["result"])
        self.assertEqual("pending_recording", native["outcome"])
        self.assertEqual([], native["run_receipt_refs"])
        self.assertEqual(request["execution"]["parameters"]["expected_source_frontier_digest"], native["source_frontier_digest"])
        self.assertEqual("CA-R-001", native["source_frontier"][0]["source_atom_id"])
        self.assertIn(b"  source_atom_id: CA-R-001", projection["04_requirement/CA-R-001--core.md"])

        events = self._journal_events()
        completed = [
            event for event in events
            if event.get("kind") == "workflow_execution" and event.get("event") == "completed"
        ]
        self.assertEqual(actual, {event["run"]["run_id"] for event in completed})
        for event in completed:
            planned = expected[event["run"]["run_id"]]
            self.assertEqual(planned["definition"], event["run"]["definition"])
            self.assertEqual(planned.get("parent_requested_run_id"), event["run"].get("parent_run_id"))
        action_event = next(event for event in completed if event["run"]["run_id"] == graph_result["step_results"][-1]["action_run_id"])
        step_event = next(event for event in completed if event["run"]["run_id"] == graph_result["step_results"][-1]["step_run_id"])
        workflow_event = next(event for event in completed if event["run"]["kind"] == "workflow")
        self.assertEqual("completed", action_event["outcome"])
        self.assertEqual(step_event["run"]["run_id"], action_event["run"]["parent_run_id"])
        self.assertEqual(workflow_event["run"]["run_id"], step_event["run"]["parent_run_id"])
        self.assertEqual(native["publication"]["output_digest"], progress["compiler_publication_recording"]["output_digest"])
        self.assertEqual(native["source_frontier_digest"], progress["compiler_publication_recording"]["source_frontier_digest"])
        self.assertEqual(
            [row["output_path"] for row in native["publication"]["output_plan"]],
            progress["compiler_publication_recording"]["output_paths"],
        )
        self.assertEqual(progress["compiler_publication_recording"]["output_paths"], action_event["effect_refs"])

    def test_failed_action_recording_preserves_output_and_never_replays_publication(self) -> None:
        calls = 0
        original = compiler.ACTION_ADAPTERS["CA-O-009"]

        def counted(parameters: object) -> dict[str, object]:
            nonlocal calls
            calls += 1
            return dict(original(parameters))

        with patch.dict(compiler.ACTION_ADAPTERS, {"CA-O-009": counted}):
            runner, request = self._request("compiler-recording-pending")
            frozen = runner.freeze(request)
            append = work_journal.append_sealed_events

            def fail_action_terminal(*args: object, **kwargs: object) -> object:
                events = args[1]
                if (isinstance(events, list) and events and events[0].get("event") == "completed"
                        and events[0].get("run", {}).get("definition", {}).get("atom_id") == "CA-O-009"):
                    raise OSError("fixture action logging failure")
                return append(*args, **kwargs)

            with patch.object(work_journal, "append_sealed_events", side_effect=fail_action_terminal):
                pending = runner.dispatch(frozen)
            output_after_failure = self._projection_bytes()
            retry = runner.dispatch(frozen)

        self.assertEqual("terminal", pending["disposition"])
        self.assertIn("fixture action logging failure", pending["diagnostics"])
        self.assertEqual(pending, retry)
        self.assertEqual(1, calls)
        self.assertEqual(output_after_failure, self._projection_bytes())
        graph_result = json.loads((runner.run_directory("compiler-recording-pending") / "graph_result.json").read_text(encoding="utf-8"))
        action_id = graph_result["step_results"][-1]["action_run_id"]
        action_terminal = next(row for row in pending["terminal_runs"] if row["run_id"] == action_id)
        self.assertEqual("terminal", action_terminal["disposition"])
        self.assertEqual("completed", action_terminal["outcome"])
        self.assertEqual("fixture action logging failure", action_terminal["recording_error"])
        self.assertFalse(any(event.get("run", {}).get("run_id") == action_id and event.get("event") == "completed" for event in self._journal_events()))
        progress = json.loads((runner.run_directory("compiler-recording-pending") /
                               f"{action_id}.json").read_text(encoding="utf-8"))
        self.assertEqual("completed publication from the still-valid final frontier", progress["result"])
        self.assertEqual("pending_recording", progress["native_result"]["outcome"])


if __name__ == "__main__":
    unittest.main()
