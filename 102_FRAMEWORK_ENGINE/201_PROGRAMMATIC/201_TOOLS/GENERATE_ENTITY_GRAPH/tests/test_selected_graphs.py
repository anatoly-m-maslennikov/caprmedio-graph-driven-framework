"""CA-E-555 through CA-E-558 functional tests for selected graph builds."""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


TEST_TEMP_ROOT = Path.cwd() / ".caprmedio_tmp" / "tests" / Path(__file__).stem
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
SCRIPT = Path(__file__).resolve().parents[1] / "generate_entity_graph.py"
SPEC = importlib.util.spec_from_file_location("selected_graphs_generator", SCRIPT)
assert SPEC is not None and SPEC.loader is not None
graph = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = graph
SPEC.loader.exec_module(graph)


def atom(
    atom_id: str,
    *,
    cce_form: str,
    governs: str,
    depends_on: tuple[str, ...] = (),
    claim: str = "claim.",
) -> str:
    dependencies = "".join(f"      - {json.dumps(value)}\n" for value in depends_on)
    if not dependencies:
        dependencies = "    continuant: []\n"
    else:
        dependencies = f"    continuant:\n{dependencies}"
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "cce_version: cce_1\n"
        f"cce_form: {cce_form}\n"
        "subjects:\n"
        "  governs:\n"
        "    continuant:\n"
        f"      - {json.dumps(governs)}\n"
        f"  depends_on:\n{dependencies}"
        "version: 1\n"
        "updated_at: 2026-10-04 00:00:00 +0000\n"
        "relations: {}\n"
        "---\n"
        f"# {atom_id}\n\n{claim}\n"
    )


def current_atom(
    atom_id: str,
    *,
    governs: str | tuple[str, ...],
    depends_on: tuple[str, ...] = (),
    status: str = "Active",
    claim: str = "Entity MEANS a canonical graph identity.",
) -> str:
    """A current source carrier: scalar/list Subjects and no retired CCE fields."""

    dependencies = ", ".join(json.dumps(value) for value in depends_on)
    return (
        "---\n"
        f"atom_id: {atom_id}\n"
        "content_role: Requirement\n"
        "current_scope_unit: TOOLS\n"
        "claim_target_scope_unit: TOOLS\n"
        f"status: {status}\n"
        "author: Test Author\n"
        "version: 1\n"
        "updated_at: \"2026-10-04 00:00:00 +0000\"\n"
        "subjects:\n"
        f"  governs: {json.dumps(governs)}\n"
        f"  depends_on: [{dependencies}]\n"
        "relations:\n"
        "  relates_to: []\n"
        "---\n"
        "# Summary\n\nA current test source.\n\n"
        "## Scope\n\nTOOLS.\n\n"
        f"## Claim\n\n{claim}\n\n"
        "## Details\n\nBounded test details.\n"
    )


class SelectedGraphTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.root = Path(self.temporary.name) / "repository"
        self.control_root = ".caprmedio_selected_graphs"
        self.projection_root = f"{self.control_root}/_projection"
        self.selected = self.root / "selected"
        self.selected.mkdir(parents=True)
        # Published graph projections use project_runtime.atomic_tempfile.
        (self.root / ".git").mkdir()
        settings = self.root / self.control_root / "caprmedio_project_settings.toml"
        settings.parent.mkdir(parents=True)
        settings.write_text(
            "[paths]\n"
            f'control_root = "{self.control_root}"\n'
            f'projection_root = "{self.projection_root}"\n',
            encoding="utf-8",
            newline="\n",
        )
        self.write(
            "CA-R-001.md",
            current_atom("CA-R-001", governs="Entity"),
        )
        self.write(
            "CA-R-002.md",
            current_atom("CA-R-002", governs="Property"),
        )
        self.write(
            "CA-R-003.md",
            current_atom(
                "CA-R-003", governs="Property",
                depends_on=("Entity",),
                claim="Property SUBKIND_OF Entity.",
            ),
        )
        self.write(
            "CA-R-004.md",
            current_atom("CA-R-004", governs="Entity/Property: Label"),
        )

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write(self, relative: str, content: str) -> Path:
        path = self.selected / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
        return path

    def test_declared_frontier_exclusions_are_not_unassessed_source_failures(self) -> None:
        self.write("README.md", "Selected source documentation.\n")
        self.write("CA-R-099.md", current_atom("CA-R-099", governs="Retired", status="Canceled"))
        result = graph.build_graph(self.root, self.request("terms"))
        self.assertEqual("incomplete", result["outcome"])
        codes = {row["code"] for row in result["diagnostics"]}
        self.assertIn("non-atom-markdown-skipped", codes)
        self.assertIn("inactive-status-skipped", codes)
        self.assertNotIn("source-selection-incomplete", codes)
        self.assertNotIn("Canceled", json.dumps(result["diagnostics"]))

    def request(self, graph_kind: str, **overrides: object) -> dict[str, object]:
        request: dict[str, object] = {
            "graph_kind": graph_kind,
            "source_frontier": graph.source_frontier_for(self.root, self.selected),
            "selection": {"atom_ids": ["CA-R-001", "CA-R-002", "CA-R-003", "CA-R-004"], "scope_unit_names": []},
            "representation_configuration": {"format": "canonical-json"},
            "capability_permission_evidence": {"authorized": True},
        }
        request.update(overrides)
        return request

    def authorized_start(self, graph_kind: str):
        action = "CA-O-134" if graph_kind == "entities" else "CA-O-137"
        route = "build_entities_graph" if graph_kind == "entities" else "build_terms_graph"
        return graph.actual_run_recording_context(
            "test-workflow-run", "test-step-run", "test-action-run",
            {"event_id": "test-action-start", "action_id": action, "event_digest": "0" * 64,
             "carrier": ".caprmedio_selected_graphs/_journal/events.ndjson", "line": 1,
             "previous_carrier_digest": "0" * 64, "appended_carrier_digest": "1" * 64},
            execution_authorization={
                "authorization_ref": "test-authorization", "authorization_freshness": {"state": "current", "digest": "0" * 64},
                "request_id": "test-request", "operation_route": route, "proposal_receipt_digest": "0" * 64,
                "parameters_digest": "0" * 64, "target_frontier_digest": "0" * 64, "effects_digest": "0" * 64,
                "definition_manifest": {}, "source_freshness": {},
            },
        )

    def test_caller_supplied_recording_claim_cannot_publish(self) -> None:
        result = graph.build_graph(
            self.root,
            self.request(
                "entities",
                run_recording_context={"state": "confirmed", "receipt_refs": ["forged-receipt"]},
            ),
        )

        self.assertEqual("failed", result["outcome"])
        self.assertEqual("recording-context-untrusted", result["diagnostics"][0]["code"])
        self.assertEqual([], result["output_effects"]["paths"])
        self.assertFalse((self.root / self.projection_root / "entities_graph.json").exists())

    def test_secret_shaped_property_is_rejected_without_value_disclosure(self) -> None:
        secret = "do-not-disclose-graph-secret"
        self.write(
            "CA-R-005.md",
            current_atom("CA-R-005", governs="Protected Entity").replace(
                "version: 1\n", f"api_key: {secret}\nversion: 1\n",
            ),
        )
        result = graph.build_graph(
            self.root,
            self.request(
                "entities",
                selection={"atom_ids": ["CA-R-001", "CA-R-002", "CA-R-003", "CA-R-004", "CA-R-005"]},
            ),
        )

        serialized = json.dumps(result, sort_keys=True)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("secret-shaped-property", result["diagnostics"][0]["code"])
        self.assertNotIn(secret, serialized)
        self.assertFalse((self.root / self.projection_root / "entities_graph.json").exists())

    def test_malformed_source_scalar_is_not_copied_into_error_details(self) -> None:
        request = self.request("entities")
        private_value = "private-credential-do-not-disclose"
        self.write("CA-R-001.md", current_atom("CA-R-001", governs="Entity").replace(
            "version: 1\n", f"version: {private_value}\n",
        ))
        result = graph.build_graph(self.root, request)
        self.assertEqual("failed", result["outcome"])
        self.assertEqual("atom-version-invalid", result["diagnostics"][0]["code"])
        self.assertNotIn(private_value, json.dumps(result))
        self.assertEqual("none", result["output_effects"]["state"])

    def test_partial_entities_and_terms_graphs_are_separate_and_traceable(self) -> None:
        entities = graph.build_graph(self.root, self.request("entities"))
        terms = graph.build_graph(self.root, self.request("terms"))

        self.assertEqual("incomplete", entities["outcome"])
        self.assertEqual("incomplete", terms["outcome"])
        self.assertIn("entities_graph", entities)
        self.assertNotIn("terms_graph", entities)
        self.assertIn("terms_graph", terms)
        self.assertNotIn("entities_graph", terms)
        self.assertTrue(entities["non_authoritative"])
        self.assertTrue(terms["non_authoritative"])

        self.assertEqual([], entities["entities_graph"]["entities"])
        self.assertEqual([], entities["entities_graph"]["native_relations"])
        source_atoms = entities["entities_graph"]["source_atoms"]
        self.assertEqual(["CA-R-001", "CA-R-002", "CA-R-003", "CA-R-004"], [row["source"]["atom_id"] for row in source_atoms])
        self.assertEqual("selected/CA-R-001.md", source_atoms[0]["source"]["carrier_path"])
        self.assertEqual([], terms["terms_graph"]["terms"])

        self.assertEqual(
            entities["source_frontier_evidence"]["source_frontier_sha256"],
            terms["source_frontier_evidence"]["source_frontier_sha256"],
        )
        self.assertEqual("unresolved", entities["quality_dispositions"]["coverage"])
        self.assertEqual({"state": "construction_only"}, entities["completion"])
        self.assertEqual({"state": "none", "paths": [], "before": None, "after": None}, entities["output_effects"])
        self.assertNotIn("settings_sha256", entities)

    def test_current_subject_schema_preserves_incidence_without_native_admission(self) -> None:
        self.write(
            "CA-R-101.md",
            current_atom("CA-R-101", governs="Entity", depends_on=("Property",)),
        )
        self.write(
            "CA-R-102.md",
            current_atom("CA-R-102", governs=("Property",)),
        )
        self.write(
            "CA-R-103.md",
            current_atom("CA-R-103", governs="Entity/Property: Label", depends_on=("Property",)),
        )
        selection = {"atom_ids": ["CA-R-101", "CA-R-102", "CA-R-103"], "scope_unit_names": []}
        entities = graph.build_graph(self.root, self.request("entities", selection=selection))
        terms = graph.build_graph(self.root, self.request("terms", selection=selection))

        self.assertEqual("incomplete", entities["outcome"])
        self.assertEqual("incomplete", terms["outcome"])
        self.assertEqual([], entities["entities_graph"]["entities"])
        self.assertEqual(
            ["CA-R-101", "CA-R-102", "CA-R-103"],
            [row["source"]["atom_id"] for row in entities["entities_graph"]["source_atoms"]],
        )
        self.assertEqual([], entities["entities_graph"]["native_properties"])
        self.assertEqual([], terms["terms_graph"]["terms"])

    def test_current_status_excludes_non_active_carriers_without_dropping_active_frontier(self) -> None:
        self.write("CA-R-110.md", current_atom("CA-R-110", governs="Active Entity"))
        self.write(
            "CA-R-111.md",
            current_atom("CA-R-111", governs="Retired Entity", status="Done"),
        )
        frontier = graph.source_frontier_for(self.root, self.selected)
        frontier_ids = [row["atom_id"] for row in frontier["carriers"]]
        self.assertIn("CA-R-110", frontier_ids)
        self.assertNotIn("CA-R-111", frontier_ids)
        self.assertEqual(
            "inactive-status-skipped",
            graph.discover_atoms(self.root, self.selected)[1][-1]["code"],
        )

    def test_whole_control_root_excludes_persisted_projection_and_journal_copies(self) -> None:
        live = self.root / self.control_root / "000_framework" / "CA-R-201.md"
        live.parent.mkdir(parents=True)
        live.write_text(
            current_atom("CA-R-201", governs="Projection/Journal: Ledger"),
            encoding="utf-8",
            newline="\n",
        )
        copied_projection = self.root / self.projection_root / "snapshot" / "CA-R-201.md"
        copied_projection.parent.mkdir(parents=True)
        copied_projection.write_bytes(live.read_bytes())
        journal_copy = self.root / self.control_root / "_journal" / "CA-R-202.md"
        journal_copy.parent.mkdir(parents=True)
        journal_copy.write_text(
            current_atom("CA-R-202", governs="Journal Copy"),
            encoding="utf-8",
            newline="\n",
        )

        control = self.root / self.control_root
        carriers, _ = graph.discover_atoms(self.root, control)
        frontier = graph.source_frontier_for(self.root, control)

        self.assertEqual(["CA-R-201"], [carrier.atom_id for carrier in carriers])
        self.assertEqual([f"{self.control_root}/000_framework/CA-R-201.md"], [carrier.carrier_path for carrier in carriers])
        self.assertEqual(["CA-R-201"], [row["atom_id"] for row in frontier["carriers"]])

    def test_queue_handlers_consume_frozen_parameters_without_owning_transitions(self) -> None:
        handlers = graph.queue_action_handlers(self.root)
        output = handlers["CA-O-134"]({"parameters": self.request("entities")})

        self.assertEqual("incomplete", output["result"])
        self.assertEqual([], output["effect_refs"])
        self.assertEqual("incomplete", output["graph_result"]["outcome"])
        self.assertIn("entities_graph", output["graph_result"])

    def test_quality_failures_never_return_built_or_no_op(self) -> None:
        self.write(
            "CA-R-005.md",
            current_atom("CA-R-005", governs="Cycle", depends_on=("Cycle",)),
        )
        frontier = graph.source_frontier_for(self.root, self.selected)
        result = graph.build_graph(
            self.root,
            self.request(
                "terms",
                source_frontier=frontier,
                selection={"atom_ids": ["CA-R-005"], "scope_unit_names": []},
            ),
        )
        self.assertIn(result["outcome"], {"incomplete", "conflicting", "stale", "blocked", "failed"})
        self.assertNotIn(result["outcome"], {"built", "no_op"})
        self.assertIn("fact-coverage-unresolved", {row["code"] for row in result["diagnostics"]})
        self.assertEqual("unresolved", result["quality_dispositions"]["validity"])

    def test_selected_project_structure_is_traced_from_the_authoritative_toml(self) -> None:
        structure = self.root / self.control_root / "project_structure.toml"
        structure.parent.mkdir(parents=True, exist_ok=True)
        structure.write_text(
            "schema_version = 1\n\n"
            "[[scope_units]]\n"
            'scope_unit_name = "TOOLS"\n'
            'parent = "PROGRAMMATIC"\n'
            'scope_unit_type = "Unordered"\n'
            'scope_unit_label = "FEATURE"\n'
            "structural_level = 3\n"
            "navigational_order_number = 1\n"
            'authority_path = ".caprmedio_caprmedio/tools"\n'
            'delivery_path = "tools"\n'
            'authority_mode = "strict"\n',
            encoding="utf-8",
            newline="\n",
        )
        result = graph.build_graph(
            self.root,
            self.request("entities", selection={"atom_ids": ["CA-R-001"], "scope_unit_names": ["TOOLS"]}),
        )
        self.assertEqual("incomplete", result["outcome"])
        row = result["entities_graph"]["project_structure"][0]
        self.assertEqual("TOOLS", row["scope_unit_name"])
        self.assertEqual("PROGRAMMATIC", row["parent"])
        self.assertEqual(f"{self.control_root}/project_structure.toml", row["source"]["carrier_path"])
        self.assertIn("carrier_sha256", row["source"])

    def test_nonempty_unsupported_context_never_publishes_and_stale_frontier_is_truthful(self) -> None:
        destination = f"{self.projection_root}/terms-checkpoint.json"
        first = graph.build_graph(self.root, self.request("terms", output_destination=destination))
        output = self.root / destination
        self.assertEqual("blocked", first["outcome"])
        self.assertFalse(output.exists())
        self.assertEqual("none", first["output_effects"]["state"])
        stale_frontier = self.request("entities")["source_frontier"]
        self.write("CA-R-001.md", current_atom("CA-R-001", governs="Entity", claim="Entity MEANS changed."))
        stale = graph.build_graph(self.root, self.request("entities", source_frontier=stale_frontier))
        self.assertEqual("stale", stale["outcome"])
        self.assertEqual([], stale["output_effects"]["paths"])

    def test_empty_selection_can_publish_only_with_actual_authorization_and_awaits_terminal_recording(self) -> None:
        destination = f"{self.projection_root}/entities-empty.json"
        blocked = graph.build_graph(self.root, self.request(
            "entities", selection={"atom_ids": [], "scope_unit_names": []}, output_destination=destination,
        ))
        self.assertEqual("blocked", blocked["outcome"])
        self.assertFalse((self.root / destination).exists())

        result = graph.build_graph(self.root, self.request(
            "entities", selection={"atom_ids": [], "scope_unit_names": []}, output_destination=destination,
            run_recording_context=self.authorized_start("entities"),
        ))
        self.assertEqual("incomplete", result["outcome"])
        self.assertEqual("created", result["output_effects"]["state"])
        self.assertEqual({"state": "awaiting_terminal_recording"}, result["completion"])
        self.assertTrue((self.root / destination).is_file())

        rejected = graph.build_graph(
            self.root,
            self.request("entities", output_destination=".caprmedio_runtime/graph_projections/entities.json"),
        )
        self.assertEqual("failed", rejected["outcome"])
        self.assertEqual("output-destination-unauthorized", rejected["diagnostics"][0]["code"])


if __name__ == "__main__":
    unittest.main()
