"""D539 publication safety for the pure graph builder.

The builder can publish a Projection but cannot record the Run terminal fact.
Its only outward completion is therefore awaiting terminal recording; the
shared executor owns the later terminal Journal entry.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
SCRIPT = Path(__file__).resolve().parents[1] / "generate_entity_graph.py"
SPEC = importlib.util.spec_from_file_location("graph_publication_safety", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)


def current_requirement(atom_id: str, *, governs: str = "Entity") -> str:
    return (
        "---\n"
        f"atom_id: {atom_id}\ncontent_role: Requirement\ntype: Definition\n"
        "current_scope_unit: TOOLS\nclaim_target_scope_unit: TOOLS\nstatus: Active\n"
        "version: 1\nupdated_at: '2026-10-09 00:00:00 +0000'\nsubjects:\n"
        f"  governs: {json.dumps(governs)}\n  depends_on: []\nrelations:\n  relates_to: []\n---\n"
        f"# {atom_id}\n\n## Summary\n\nFixture.\n\n## Claim\n\nthe Term {governs} **means** a fixture Entity.\n"
    )


class GraphPublicationSafetyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.selected = self.root / "selected"
        self.selected.mkdir(parents=True)
        (self.root / ".git").mkdir()
        self.control_root = ".caprmedio_publication_safety"
        self.projection_root = f"{self.control_root}/_projection"
        settings = self.root / self.control_root / "caprmedio_project_settings.toml"
        settings.parent.mkdir(parents=True)
        settings.write_text(
            "[paths]\n" f'control_root = "{self.control_root}"\n' f'projection_root = "{self.projection_root}"\n',
            encoding="utf-8", newline="\n")
        (self.selected / "CA-R-1872.md").write_text(current_requirement("CA-R-1872"), encoding="utf-8", newline="\n")
        self.destination = f"{self.projection_root}/entities-1872.json"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    @property
    def output(self) -> Path:
        return self.root / self.destination

    @staticmethod
    def execution_authorization() -> dict[str, object]:
        """Synthetic frozen Run Support packet, not a live authorization receipt."""

        return {
            "authorization_ref": "authorization:publication-safety-fixture",
            "authorization_freshness": {"state": "current", "digest": "a" * 64},
            "request_id": "request:publication-safety-fixture",
            "operation_route": "build_entities_graph",
            "proposal_receipt_digest": "b" * 64,
            "parameters_digest": "c" * 64,
            "target_frontier_digest": "d" * 64,
            "effects_digest": "e" * 64,
            "definition_manifest": {"manifest_ref": "manifest:publication-safety-fixture", "manifest_digest": "f" * 64},
            "source_freshness": {"selected_binding_digest": "0" * 64},
        }

    def request(self, *, execution_authorization: dict[str, object] | None | object = ..., **overrides: object) -> dict[str, object]:
        start = {"event_id": "publication-safety-start", "action_id": "CA-O-134", "event_digest": "0" * 64,
                 "carrier": f"{self.control_root}/_journal/events.ndjson", "line": 1,
                 "previous_carrier_digest": "0" * 64, "appended_carrier_digest": "1" * 64}
        authorization = self.execution_authorization() if execution_authorization is ... else execution_authorization
        context = graph.actual_run_recording_context(
            "workflow-1872", "step-1872", "action-1872", start,
            execution_authorization=authorization,
        )
        result: dict[str, object] = {
            "graph_kind": "entities", "source_frontier": graph.source_frontier_for(self.root, self.selected),
            # An explicitly empty selection is a sealed, provider-complete
            # empty graph; the source frontier itself remains nonempty.
            "selection": {"atom_ids": []}, "representation_configuration": {"format": "canonical-json"},
            "output_destination": self.destination, "capability_permission_evidence": {"authorized": True},
            "run_recording_context": context,
        }
        result.update(overrides)
        return result

    def write_existing(self, content: bytes = b'{"unrelated":"old projection"}\n') -> bytes:
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.output.write_bytes(content)
        return content

    def assert_awaiting_terminal(self, result: dict[str, object]) -> None:
        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual({"state": "awaiting_terminal_recording"}, result["completion"])
        self.assertEqual(["publication-safety-start"], result["run_receipt_refs"])
        self.assertNotIn("terminal_receipt_ref", result["completion"])

    def evidence(self, content: bytes | None) -> dict[str, str] | None:
        return None if content is None else {
            "carrier_path": self.destination,
            "carrier_sha256": hashlib.sha256(content).hexdigest(),
        }

    def assert_preserved(self, result: dict[str, object], before: bytes) -> None:
        self.assertEqual(before, self.output.read_bytes())
        self.assertEqual(
            {"state": "unchanged", "paths": [], "before": self.evidence(before), "after": self.evidence(before)},
            result["output_effects"],
        )

    def test_start_proves_only_start_even_after_projection_publication(self) -> None:
        result = graph.build_graph(self.root, self.request())
        self.assert_awaiting_terminal(result)
        output = self.output.read_bytes()
        self.assertEqual(
            {"state": "created", "paths": [self.destination], "before": None, "after": self.evidence(output)},
            result["output_effects"],
        )

    def test_actual_start_without_execution_authorization_is_blocked_without_effect(self) -> None:
        result = graph.build_graph(self.root, self.request(execution_authorization=None))
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual("actual-permission-unavailable", result["diagnostics"][-1]["code"])
        self.assertEqual({"state": "none", "paths": [], "before": None, "after": None}, result["output_effects"])
        self.assertFalse(self.output.exists())

    def test_missing_destination_is_nonpersisting_construction_not_a_destination_error(self) -> None:
        request = self.request()
        request.pop("output_destination")
        result = graph.build_graph(self.root, request)
        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual({"state": "construction_only"}, result["completion"])
        self.assertEqual({"state": "none", "paths": [], "before": None, "after": None}, result["output_effects"])
        self.assertFalse(self.output.exists())

    def test_unproven_existing_bytes_are_preserved_with_exact_effect_hashes(self) -> None:
        before = self.write_existing()
        result = graph.build_graph(self.root, self.request())
        self.assertEqual("blocked", result["outcome"])
        self.assertEqual("existing-projection-evidence-required", result["diagnostics"][-1]["code"])
        self.assert_preserved(result, before)

    def test_matching_current_digest_replaces_and_remains_awaiting_terminal_recording(self) -> None:
        before = self.write_existing()
        result = graph.build_graph(self.root, self.request(
            existing_projection_evidence={"sha256": hashlib.sha256(before).hexdigest()}))
        self.assert_awaiting_terminal(result)
        output = self.output.read_bytes()
        self.assertEqual(
            {"state": "replaced", "paths": [self.destination], "before": self.evidence(before), "after": self.evidence(output)},
            result["output_effects"],
        )

    def test_identical_current_projection_is_nonpersisting_but_still_awaits_terminal_recording(self) -> None:
        first = graph.build_graph(self.root, self.request())
        self.assert_awaiting_terminal(first)
        before = self.output.read_bytes()
        second = graph.build_graph(self.root, self.request(
            existing_projection_evidence={"sha256": hashlib.sha256(before).hexdigest()}))
        self.assert_awaiting_terminal(second)
        self.assert_preserved(second, before)

    def test_source_drift_and_write_failure_preserve_existing_hashes(self) -> None:
        before = self.write_existing()
        request = self.request(existing_projection_evidence={"sha256": hashlib.sha256(before).hexdigest()})
        original = graph.source_frontier_for
        calls = 0
        def drift(repository: Path, selected_folder: Path) -> dict[str, object]:
            nonlocal calls
            calls += 1
            value = original(repository, selected_folder)
            if calls == 3:
                value = copy.deepcopy(value)
                value["source_frontier_sha256"] = "d" * 64
            return value
        with patch.object(graph, "source_frontier_for", side_effect=drift):
            stale = graph.build_graph(self.root, request)
        self.assertEqual("stale", stale["outcome"])
        self.assertEqual("source-frontier-changed-before-publication", stale["diagnostics"][-1]["code"])
        self.assert_preserved(stale, before)
        with patch.object(graph, "atomic_write", side_effect=OSError("simulated disk failure")):
            failed = graph.build_graph(self.root, request)
        self.assertEqual("failed", failed["outcome"])
        self.assertEqual("projection-publication-failed", failed["diagnostics"][-1]["code"])
        self.assert_preserved(failed, before)

    def test_symlink_destination_and_caller_source_or_receipt_fields_are_rejected(self) -> None:
        outside = self.root.parent / "outside.json"
        outside.write_bytes(b"outside")
        self.output.parent.mkdir(parents=True, exist_ok=True)
        self.output.symlink_to(outside)
        request = self.request()
        request["source_fact_context"] = {"caller": "forged"}
        request["terminal_receipt_refs"] = ["caller-forged"]
        result = graph.build_graph(self.root, request)
        self.assertEqual("failed", result["outcome"])
        self.assertIn(result["diagnostics"][0]["code"], {"request-schema-invalid", "output-destination-symlink"})
        self.assertEqual(b"outside", outside.read_bytes())
        self.assertEqual({"state": "none", "paths": [], "before": None, "after": None}, result["output_effects"])


if __name__ == "__main__":
    unittest.main()
