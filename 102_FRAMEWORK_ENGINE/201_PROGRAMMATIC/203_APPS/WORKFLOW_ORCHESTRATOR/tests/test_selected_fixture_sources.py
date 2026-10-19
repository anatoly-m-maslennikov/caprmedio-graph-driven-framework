"""The selected-workflow golden Project is a closed checked-in corpus."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from frozen_selected_workflows import (
    frozen_base_revise_binding,
    frozen_complete_carrier_authority,
    frozen_source_bytes,
    frozen_source_paths,
    frozen_source_root,
)
from selected_workflows_docker_fixture import (
    GoldenCase,
    GoldenCorpusError,
    GoldenProject,
    _RUNTIME_READINESS_O104,
    _RUNTIME_READINESS_O104_SNAPSHOT,
    _RMED_PROMPTS,
)


REPOSITORY = Path(__file__).resolve().parents[5]
LIVE_AUTHORITY = REPOSITORY / ".caprmedio_caprmedio"
MCP = REPOSITORY / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP"
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))


class SelectedFixtureSourcesTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = REPOSITORY / ".caprmedio_tmp/tests/selected-fixture-sources"
        parent.mkdir(parents=True, exist_ok=True)
        temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name) / "fixture"
        self.root.mkdir()
        self.project = GoldenProject(REPOSITORY, self.root, GoldenCase("W02", "update_atom"))

    def test_w02_prepared_parameters_are_deep_copied_without_a_descriptor_scan(self) -> None:
        prepared = {"target": {"path": "prepared-subject.md"}}
        self.project._semantic_update_parameters = prepared
        with patch.object(self.project, "_descriptor", side_effect=AssertionError("unused scan")) as descriptor:
            first = self.project.native_parameters()
            self.assertEqual(prepared, first)
            first["target"]["path"] = "caller-change.md"
            self.assertEqual(prepared, self.project.native_parameters())
        self.assertEqual("prepared-subject.md", prepared["target"]["path"])
        descriptor.assert_not_called()

    def test_w02_missing_preparation_still_refuses_without_a_descriptor_scan(self) -> None:
        with patch.object(self.project, "_descriptor", side_effect=AssertionError("unused scan")) as descriptor:
            with self.assertRaisesRegex(GoldenCorpusError, "semantic assessment carrier was not prepared"):
                self.project.native_parameters()
        descriptor.assert_not_called()

    def test_other_target_route_reopens_disposable_descriptor_and_propagates_failure(self) -> None:
        project = GoldenProject(REPOSITORY, self.root, GoldenCase("W04", "change_atom_status"))
        observations = [{"path": "first.md"}, {"path": "changed.md"}, GoldenCorpusError("missing target")]
        with patch.object(project, "_descriptor", side_effect=observations) as descriptor:
            self.assertEqual({"target": observations[0], "status": "Archived"}, project.native_parameters())
            self.assertEqual({"target": observations[1], "status": "Archived"}, project.native_parameters())
            with self.assertRaisesRegex(GoldenCorpusError, "missing target"):
                project.native_parameters()
        self.assertEqual([("CA-R-100",)] * 3, [call.args for call in descriptor.call_args_list])

    def test_every_complete_carrier_pin_has_exact_checked_in_bytes(self) -> None:
        closure = frozen_complete_carrier_authority()
        self.assertGreater(len(closure), 30)
        for atom_id, entry in closure.items():
            with self.subTest(atom_id=atom_id):
                self.assertEqual(entry["sha256"], hashlib.sha256(
                    frozen_source_bytes(entry["source_path"])
                ).hexdigest())

    def test_shared_frozen_root_materializes_each_advertised_authority(self) -> None:
        with tempfile.TemporaryDirectory(dir=self.root) as temporary:
            frozen_root = frozen_source_root(Path(temporary))
            for atom_id, entry in frozen_complete_carrier_authority().items():
                with self.subTest(atom_id=atom_id):
                    actual = frozen_root / entry["source_path"]
                    self.assertEqual(entry["sha256"], hashlib.sha256(actual.read_bytes()).hexdigest())

    def test_prepare_never_reads_or_scans_real_project_authority(self) -> None:
        def forbid(method):
            def guarded(path: Path, *args: object, **kwargs: object):
                if path == LIVE_AUTHORITY or LIVE_AUTHORITY in path.parents:
                    raise AssertionError(f"golden fixture read real authority: {path}")
                return method(path, *args, **kwargs)
            return guarded

        with (
            patch.object(Path, "read_bytes", forbid(Path.read_bytes)),
            patch.object(Path, "read_text", forbid(Path.read_text)),
            patch.object(Path, "glob", forbid(Path.glob)),
            patch.object(Path, "rglob", forbid(Path.rglob)),
            patch.object(Path, "iterdir", forbid(Path.iterdir)),
        ):
            for case, route in (("W01", "create_atom"), ("W09", "run_implementation_workflow"),
                                ("W10", "revert_changes")):
                with self.subTest(case=case), tempfile.TemporaryDirectory(dir=self.root) as temporary:
                    project = GoldenProject(REPOSITORY, Path(temporary), GoldenCase(case, route))
                    self.assertEqual(15, len(project.prepare()["routes"]))

    def test_fixture_mutation_does_not_change_the_next_golden_project(self) -> None:
        relative = next(path for path in frozen_source_paths() if path.endswith("CA-O-016-CORE_META_MODEL-WORKFLOW--implement-evaluations-before-required-behavior.md"))
        with tempfile.TemporaryDirectory(dir=self.root) as first, tempfile.TemporaryDirectory(dir=self.root) as second:
            one = GoldenProject(REPOSITORY, Path(first), GoldenCase("W09", "run_implementation_workflow"))
            one.prepare()
            copied = one.root / relative
            copied.write_text("mutated disposable source", encoding="utf-8")
            two = GoldenProject(REPOSITORY, Path(second), GoldenCase("W09", "run_implementation_workflow"))
            two.prepare()
            self.assertEqual(frozen_source_bytes(relative), (two.root / relative).read_bytes())

    def test_readiness_materializes_current_pin_and_keeps_historical_frozen(self) -> None:
        self.project.prepare()
        historical = frozen_base_revise_binding()
        historical_path = Path(historical["path"])
        current_manifest = json.loads((_RMED_PROMPTS / "source_bindings.json").read_text(encoding="utf-8"))
        current = next(row for row in current_manifest["sources"] if row["atom_id"] == "CA-O-104")
        current_path = Path(current["path"])
        historical_bytes = frozen_source_bytes(historical_path, historical["sha256"])

        self.assertNotEqual(historical_path, current_path)
        self.assertEqual(historical["sha256"], hashlib.sha256(historical_bytes).hexdigest())
        self.assertFalse((self.root / historical_path).exists())
        copied = (self.root / current_path).read_bytes()
        self.assertEqual(_RUNTIME_READINESS_O104, current)
        self.assertEqual(_RUNTIME_READINESS_O104_SNAPSHOT.read_bytes(), copied)
        self.assertEqual(current["sha256"], hashlib.sha256(copied).hexdigest())
        app = Path(__file__).resolve().parents[1]
        if str(app) not in sys.path:
            sys.path.insert(0, str(app))
        from engine import runtime_fingerprint
        self.assertRegex(runtime_fingerprint(self.root), r"^[0-9a-f]{64}$")

    def test_disposable_source_change_rejects_a_held_preview_receipt(self) -> None:
        from selected_routes import SelectedRouteAdapter, load_selected_manifest

        self.project.prepare()
        adapter = SelectedRouteAdapter(self.root)
        preview_request = self.project.request(request_id="sealed-preview")
        preview = adapter.invoke("update_atom", preview_request)
        self.assertEqual("preview", preview["disposition"], preview)
        execute = self.project.request(
            request_id="sealed-preview", mode="execute",
            receipt=preview["proposal_receipt"], receipt_digest=preview["proposal_receipt_digest"],
        )
        route = next(row for row in self.project.manifest["routes"] if row["route"] == "update_atom")
        pin = next(item for item in route["native_action_calls"] if item["atom_id"] == "CA-O-030")
        source = self.root / pin["source_path"]
        source.write_text(source.read_text(encoding="utf-8") + "\ntampered\n", encoding="utf-8")
        refreshed = load_selected_manifest(self.root)
        self.assertNotEqual(preview_request["definition_manifest"]["manifest_digest"],
                            refreshed["canonical_manifest_sha256"])
        rejected = adapter.invoke("update_atom", execute)
        self.assertEqual("rejected", rejected["disposition"], rejected)
        self.assertIn("stale", rejected["diagnostics"][0])


if __name__ == "__main__":
    unittest.main()
