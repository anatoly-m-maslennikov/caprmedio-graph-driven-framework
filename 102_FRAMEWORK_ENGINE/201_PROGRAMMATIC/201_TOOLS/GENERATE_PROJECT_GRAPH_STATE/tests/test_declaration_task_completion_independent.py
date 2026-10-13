"""P2302-P2304 completion checks at current declaration and boundary pins."""

from pathlib import Path
import sys
import tomllib
import unittest


TESTS = Path(__file__).resolve().parent
sys.path.insert(0, str(TESTS))
import test_declaration_graph_independent as declarations  # noqa: E402
import work_journal  # noqa: E402


graph = declarations.graph


class DeclarationTaskCompletionIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = declarations.DeclarationGraphIndependentTests()
        self.addCleanup(self.fixture.doCleanups)
        self.fixture.setUp()
        self.fixture.declarations[3]["authority_mode"] = "strict"
        self.fixture.write_structure()
        events = []
        for name, carrier, revision, lifecycle in (
            ("project", self.fixture.settings, 4, "recovered"),
            ("framework", self.fixture.framework, 6, "completed"),
        ):
            relative = carrier.relative_to(self.fixture.root).as_posix()
            event = {
                "schema_version": 3, "event_id": f"declared-{name}", "action_id": "action-declaration-settings",
                "event": lifecycle,
                "kind": "governed_project_state" if lifecycle == "recovered" else "governed_project_change",
                "subject_kind": "file", "author": "test-user", "occurred_at": "2026-10-13T18:04:05+04:00",
                "llm_session": {"app": "codex", "uuid": "declaration-completion-fixture"},
                "structural_scope": "independent",
                "result": {"state": "present", "filename": carrier.name, "version": revision,
                           "path": relative, "sha256": graph.sha(carrier)},
            }
            if lifecycle == "recovered":
                event["recovery_evidence"] = {"carrier": {
                    "path": relative, "sha256": graph.sha(carrier), "observed_at": event["occurred_at"],
                    "observer_run_id": "independent-declaration-observer",
                }}
            else:
                event.update(action_type="UPDATE", sources=[], previous_result_event="prior-framework")
            sealed = work_journal.with_event_digest(event)
            self.assertEqual(sealed, work_journal.validate_sealed_event(sealed))
            events.append(sealed)
        self.receipts = work_journal.append_sealed_events(
            self.fixture.root, events, author="test-user", local_date="2026-10-13", timezone="Asia/Tbilisi",
        )
        self.bindings = graph.settings_bindings()
        self.assertEqual({"resolved"}, {binding["status"] for binding in self.bindings.values()})
        self.config = graph.configuration()

    def snapshot(self):
        return {path.relative_to(self.fixture.root): path.read_bytes()
                for path in self.fixture.root.rglob("*") if path.is_file()}

    def serialize(self, rows, observations):
        return (
            graph.project_scope_unit_graph("2026-10-13 18:04:05", self.config, self.bindings, rows, [],
                                           observations=observations),
            graph.project_scope_unit_graph_sources("2026-10-13 18:04:05", self.bindings, rows, [],
                                                   observations=observations),
        )

    def test_complete_semantic_and_observation_attribution_uses_actual_settings_receipts(self):
        before = self.snapshot()
        rows = self.fixture.rows()
        observations = graph.directory_observations(self.fixture.control, self.fixture.root, rows)
        payload, sources = self.serialize(rows, observations)
        document = tomllib.loads(payload)
        self.assertEqual("exact_source_bound", document["projection"]["currentness"])
        self.assertEqual({item["scope_unit_name"] for item in self.fixture.declarations},
                         {item["scope_unit_name"] for item in document["scope_units"]})
        self.assertEqual(6, len(document["scope_units"]))
        by_field = {item["output_path"]: item for item in tomllib.loads(sources)["bindings"]}
        structure_digest = graph.sha(self.fixture.structure)
        for row in rows:
            for field in graph.SCOPE_UNIT_GRAPH_FIELDS:
                if row[field] is None:
                    continue
                with self.subTest(scope=row["scope_unit_name"], field=field):
                    binding = by_field["scope_units." + row["node_id"] + "." + field]
                    if field in {"authority_materialized", "numeric_prefix"}:
                        self.assertEqual("directory_observation", binding["source_kind"])
                    elif field == "authority_mode" and row["authority_mode_inherited"]:
                        self.assertEqual("framework_settings", binding["source_kind"])
                        self.assertEqual(self.receipts[1]["carrier"], binding["journal_carrier"])
                        self.assertEqual(self.receipts[1]["event_id"], binding["journal_event_id"])
                    else:
                        self.assertEqual("project_structure", binding["source_kind"])
                        self.assertEqual(".caprmedio_caprmedio/project_structure.toml", binding["source_carrier"])
                        self.assertEqual(structure_digest, binding["source_sha256"])
                        self.assertEqual("sha256:" + structure_digest, binding["source_revision"])
        for observation in observations:
            for field, value in observation.items():
                if value is not None:
                    with self.subTest(observation=observation["authority_path"], field=field):
                        binding = by_field["directory_observations." + observation["authority_path"] + "." + field]
                        self.assertEqual("directory_observation", binding["source_kind"])
                        self.assertEqual(graph.canonical_json_digest(observation), binding["source_sha256"])
        self.assertEqual(before, self.snapshot())
        self.assertFalse(graph.OUTPUT.exists())
        self.assertFalse(graph.SOURCE_MAP.exists())

    def test_previous_projection_edits_do_not_select_sources_or_change_regeneration(self):
        rows = self.fixture.rows()
        observations = graph.directory_observations(self.fixture.control, self.fixture.root, rows)
        first = self.serialize(rows, observations)
        graph.OUTPUT.parent.mkdir(parents=True)
        graph.OUTPUT.write_text('[project]\nname="poisoned"\n[[scope_units]]\nparent="wrong"\n')
        graph.SOURCE_MAP.write_text('[projection]\ncurrentness="forged"\n')
        before = self.snapshot()
        second_rows = self.fixture.rows()
        second_observations = graph.directory_observations(self.fixture.control, self.fixture.root, second_rows)
        self.assertEqual(first, self.serialize(second_rows, second_observations))
        self.assertEqual(before, self.snapshot())

    def test_both_serializers_refuse_foreign_marker_introduced_after_captured_absence(self):
        for field in ("authority_path", "delivery_path"):
            with self.subTest(field=field):
                foreign = self.fixture.root / ("vendor/" + field + "/.caprmedio_other")
                self.fixture.declarations[3][field] = foreign.relative_to(self.fixture.root).as_posix() + "/unit"
                self.fixture.write_structure()
                rows = self.fixture.rows()
                observations = graph.directory_observations(self.fixture.control, self.fixture.root, rows)
                pins = dict(rows._boundary_proof.marker_pins)
                foreign.mkdir(parents=True, exist_ok=True)
                (foreign / "caprmedio_project_settings.toml").write_text(
                    '[project]\nname="independent"\n[paths]\ncontrol_root=".caprmedio_other"\n',
                )
                before = self.snapshot()
                with self.subTest(serializer="graph"), self.assertRaises(SystemExit):
                    graph.project_scope_unit_graph("2026-10-13 18:04:05", self.config, self.bindings, rows, [],
                                                   observations=observations)
                with self.subTest(serializer="sources"), self.assertRaises(SystemExit):
                    graph.project_scope_unit_graph_sources("2026-10-13 18:04:05", self.bindings, rows, [],
                                                           observations=observations)
                self.assertEqual(pins, dict(rows._boundary_proof.marker_pins))
                self.assertEqual(before, self.snapshot())
                (foreign / "caprmedio_project_settings.toml").unlink()


if __name__ == "__main__":
    unittest.main()
