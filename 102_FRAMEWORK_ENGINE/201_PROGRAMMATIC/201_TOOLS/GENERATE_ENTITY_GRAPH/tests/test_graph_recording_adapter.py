"""Queue-adapter boundary tests for selected graph recording capabilities."""

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
SCRIPT = Path(__file__).resolve().parents[1] / "generate_entity_graph.py"
SPEC = importlib.util.spec_from_file_location("graph_recording_adapter", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)


class GraphRecordingAdapterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.repository = Path(self.temporary.name) / "repository"
        self.repository.mkdir()
        self.handlers = graph.queue_action_handlers(self.repository)
        self.recording = graph.actual_run_recording_context(
            "workflow-run",
            "step-run",
            "action-run",
            {
                "event_id": "event-start",
                "action_id": "CA-O-134",
                "event_digest": "0" * 64,
                "carrier": ".caprmedio/_journal/events.ndjson",
                "line": 1,
                "previous_carrier_digest": "0" * 64,
                "appended_carrier_digest": "1" * 64,
            },
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @staticmethod
    def built_result() -> dict[str, object]:
        return {
            "outcome": "built",
            "output_effects": {"state": "published", "paths": ["projection/entities_graph.json"]},
        }

    def test_nested_graph_request_preserves_outer_actual_recording_capability(self) -> None:
        context = {
            "parameters": {
                "run_recording_context": self.recording,
                "graph_request": {
                    "graph_kind": "entities",
                    "selection": {"atom_ids": ["CA-R-001"]},
                },
            },
        }

        with patch.object(graph, "build_graph", return_value=self.built_result()) as build:
            output = self.handlers["CA-O-134"](context)

        self.assertEqual("built", output["result"])
        self.assertEqual(["projection/entities_graph.json"], output["effect_refs"])
        request = build.call_args.args[1]
        self.assertEqual("entities", request["graph_kind"])
        self.assertIs(self.recording, request["run_recording_context"])
        self.assertEqual({"atom_ids": ["CA-R-001"]}, request["selection"])

    def test_flat_graph_request_preserves_actual_recording_capability(self) -> None:
        context = {
            "parameters": {
                "graph_kind": "entities",
                "selection": {"atom_ids": ["CA-R-002"]},
                "run_recording_context": self.recording,
            },
        }

        with patch.object(graph, "build_graph", return_value=self.built_result()) as build:
            self.handlers["CA-O-134"](context)

        request = build.call_args.args[1]
        self.assertIs(self.recording, request["run_recording_context"])
        self.assertEqual({"atom_ids": ["CA-R-002"]}, request["selection"])

    def test_nested_caller_forgery_cannot_replace_outer_recording_capability(self) -> None:
        forged = {"state": "confirmed", "receipt_refs": ["caller-supplied"]}
        context = {
            "parameters": {
                "run_recording_context": self.recording,
                "graph_request": {"graph_kind": "entities", "run_recording_context": forged},
            },
        }

        with patch.object(graph, "build_graph", return_value=self.built_result()) as build:
            self.handlers["CA-O-134"](context)

        self.assertIs(self.recording, build.call_args.args[1]["run_recording_context"])

    def test_nested_typed_context_without_outer_executor_context_is_not_forwarded(self) -> None:
        context = {"parameters": {"graph_request": {
            "graph_kind": "entities", "run_recording_context": self.recording,
        }}}
        with patch.object(graph, "build_graph", return_value=self.built_result()) as build:
            self.handlers["CA-O-134"](context)
        self.assertNotIn("run_recording_context", build.call_args.args[1])

    def test_direct_or_unminted_recording_instance_is_not_an_actual_capability(self) -> None:
        with self.assertRaises(graph.EntityGraphError):
            graph.ActualRunRecordingContext("workflow", "step", "action", {})
        unminted = object.__new__(graph.ActualRunRecordingContext)
        result = graph.build_graph(self.repository, {
            "graph_kind": "entities", "source_frontier": {}, "selection": {"atom_ids": []},
            "representation_configuration": {"format": "canonical-json"},
            "capability_permission_evidence": {"authorized": True}, "run_recording_context": unminted,
        })
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("recording-context-untrusted", result["diagnostics"][0]["code"])
        self.assertEqual("none", result["output_effects"]["state"])

    def test_malformed_nested_graph_request_is_blocked_without_effect_or_build(self) -> None:
        context = {"parameters": {"run_recording_context": self.recording, "graph_request": ["not", "an", "object"]}}

        with patch.object(graph, "build_graph") as build:
            output = self.handlers["CA-O-134"](context)

        self.assertEqual("blocked", output["result"])
        self.assertEqual([], output["effect_refs"])
        self.assertEqual("queue-parameters-invalid", output["graph_result"]["diagnostics"][0]["code"])
        build.assert_not_called()

    def test_missing_or_forged_recording_context_fails_native_build_without_effects(self) -> None:
        for supplied in (None, {"event_id": "caller-forged"}):
            with self.subTest(supplied=supplied):
                output = self.handlers["CA-O-134"]({
                    "parameters": {
                        "graph_kind": "entities",
                        "source_frontier": {},
                        "selection": {},
                        "representation_configuration": {},
                        "capability_permission_evidence": {"authorized": True},
                        "run_recording_context": supplied,
                    },
                })

                self.assertEqual("failed", output["result"])
                self.assertEqual([], output["effect_refs"])
                self.assertEqual("recording-context-untrusted", output["graph_result"]["diagnostics"][0]["code"])


if __name__ == "__main__":
    unittest.main()
