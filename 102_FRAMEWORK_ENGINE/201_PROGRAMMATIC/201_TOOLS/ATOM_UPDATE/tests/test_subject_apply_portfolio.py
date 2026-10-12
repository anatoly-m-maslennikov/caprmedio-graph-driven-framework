"""Real-authority Subject preparation and fail-closed native execution."""

from __future__ import annotations

import copy
import hashlib
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
REPOSITORY = TOOLS.parents[2]
APP = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for location in (TOOLS, APP, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
import atom_subject_apply as native  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
from lifecycle_intents import LifecycleError, carrier_descriptor, update_assessment_seal  # noqa: E402
from selected_workflows_docker_fixture import GoldenCase, GoldenProject, digest  # noqa: E402
from subject_notation import get_profile  # noqa: E402


TEST_TEMP_ROOT = REPOSITORY / ".caprmedio_tmp/tests/test_subject_apply_portfolio"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
O030_V7_SHA256 = "c2d70fa275a075d2fbc978cab246158cfd8413cec88716521336736d0bf060cc"


class SubjectApplyProject:
    """One reviewed W02 fixture with only its O030 native binding resealed."""

    def __init__(self, root: Path, *, noop: bool = False) -> None:
        self.root = root
        self.golden = GoldenProject(REPOSITORY, root, GoldenCase("W02", "update_atom"))
        self.manifest = self.golden.prepare()
        self.golden._write_complete_carrier_project_structure()
        self.golden._copy_complete_carrier_authority()
        route = next(row for row in self.manifest["routes"] if row["route"] == "update_atom")
        pin = route["native_action_calls"][0]
        assert pin["atom_id"] == "CA-O-030" and pin["version"] == 7 and pin["digest"] == O030_V7_SHA256
        source = REPOSITORY / pin["source_path"]
        current_raw = source.read_bytes()
        assert "version: 10\n" in current_raw.decode("utf-8")
        shutil.copyfile(source, root / pin["source_path"])
        pin.update(version=10, digest=hashlib.sha256(current_raw).hexdigest())
        self.manifest["source_freshness"]["selected_binding_digest"] = digest(self.manifest["routes"])
        self.manifest["canonical_manifest_sha256"] = digest({
            key: value for key, value in self.manifest.items() if key != "canonical_manifest_sha256"
        })
        self.golden.manifest_path.write_text(json.dumps(self.manifest), encoding="utf-8")
        for grammar_pin in get_profile("approved").grammar_pins:
            original = REPOSITORY / grammar_pin.path
            assert hashlib.sha256(original.read_bytes()).hexdigest() == grammar_pin.sha256
            destination = root / grammar_pin.path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, destination)
        self.path = self.golden.status_atom("Requirement", "Active", number=8100)
        self.path.chmod(0o640)
        self.before = self.path.read_bytes()
        self.before_mode = self.path.stat().st_mode & 0o777
        self.target = carrier_descriptor(root, self.path.relative_to(root).as_posix())
        self.patches = [] if noop else [{"field": "governs", "old": "Atom/Test", "new": "Atom.State"}]
        self.prepared = subject_patch.prepare_subject_intent(root, self.target, self.patches, subject_profile="approved")
        self.parameters = {
            "target": self.target, "subject_patches": self.patches,
            "subject_intent_sha256": self.prepared["subject_intent_sha256"], "subject_profile": "approved",
        }
        if not noop:
            self.parameters["semantic_assessment_report"] = self.golden._semantic_assessment_report(self.target, self.prepared["proposed"])
        self.golden._semantic_update_parameters = self.parameters
        self.archive = None if noop else root / self.prepared["subject_intent"]["predecessorArchive"]["path"]

    def execution(self, run_id: str, *, request_transform=None):
        from selected_execution import SelectedExecution

        request = self.golden.request(request_id=run_id)
        intent = self.prepared["subject_intent"]
        request["target_frontier"] = [self.target["path"]]
        request["effects"] = []
        if not intent["noop"]:
            archive = intent["predecessorArchive"]
            request["target_frontier"].append(archive["path"])
            request["effects"] = [
                {"type": "subjectUpdate", "path": self.target["path"], "atom_id": self.target["atom_id"],
                 "before_version": self.target["version"], "version": self.target["version"] + 1,
                 "subject_intent_sha256": self.parameters["subject_intent_sha256"]},
                {"type": "predecessorArchive", **archive},
            ]
        if request_transform is not None:
            request_transform(request)
        request["target_frontier_digest"] = digest(request["target_frontier"])
        request["effects_digest"] = digest(request["effects"])
        runner = SelectedExecution(self.root)
        graph_request = {**request, "mode": "execute"}
        graph = runner._validate_graph(graph_request)
        tracker = runner._shared_tracker({"graph": graph, "request": {"execution": graph_request}})
        preview = tracker.run_selected_operation(request)
        execute = self.golden.request(request_id=run_id, mode="execute",
                                      receipt=preview["proposal_receipt"], receipt_digest=preview["proposal_receipt_digest"])
        for field in ("target_frontier", "target_frontier_digest", "effects", "effects_digest"):
            execute[field] = request[field]
        for field in ("target_frontier_digest", "effects_digest"):
            execute["operator_authorization"][field] = request[field]
        frozen = runner.freeze({"operation": "enqueue_selected", "run_id": run_id, "execution": execute})
        return runner, frozen

    def assert_unchanged(self, case: unittest.TestCase) -> None:
        case.assertEqual(self.before, self.path.read_bytes())
        case.assertEqual(self.before_mode, self.path.stat().st_mode & 0o777)
        if self.archive is not None:
            case.assertFalse(self.archive.exists())


class SubjectApplyPortfolioTests(unittest.TestCase):
    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory(dir=TEST_TEMP_ROOT, ignore_cleanup_errors=True)
        self.addCleanup(self.directory.cleanup)
        self.fixture = SubjectApplyProject(Path(self.directory.name))

    def assert_refused(self, code: str, parameters: dict | None = None, **kwargs) -> None:
        with self.assertRaises((LifecycleError, operations.ToolError)) as raised:
            native.subject_update_action(self.fixture.root, self.fixture.parameters if parameters is None else parameters, **kwargs)
        self.assertEqual(code, raised.exception.code)
        self.fixture.assert_unchanged(self)

    def test_preview_uses_real_report_and_old_metadata_proposal_without_effects(self) -> None:
        result = native.subject_update_action(self.fixture.root, self.fixture.parameters)
        self.assertEqual("preview", result["outcome"])
        self.assertEqual("semantic_revision", result["assessment_evidence"]["admitted_change_class"])
        self.assertEqual(self.fixture.prepared["subject_intent_sha256"], result["subject_intent_sha256"])
        self.assertEqual(self.fixture.before.replace(b"governs: Atom/Test", b'governs: "Atom.State"'),
                         self.fixture.prepared["intended_carrier"].encode())
        self.assertEqual(self.fixture.before.split(b"\n---\n", 1)[1], self.fixture.prepared["proposed"]["content"].encode())
        self.fixture.assert_unchanged(self)

    def test_caller_boolean_and_current_assessment_seal_are_not_a_selected_session(self) -> None:
        preview = native.subject_update_action(self.fixture.root, self.fixture.parameters)
        assessment = update_assessment_seal(self.fixture.parameters, preview["assessment_evidence"])
        self.assert_refused("subject-session-required", execute=True, authorized=True, assessment=assessment)

    def test_closed_parameters_reject_mixed_generic_and_forged_evidence(self) -> None:
        for field in ("proposed", "frontmatter", "content", "change_class", "successors", "assessment", "session", "authorized"):
            with self.subTest(field=field):
                self.assert_refused("subject-update-parameters-invalid", {**self.fixture.parameters, field: True})
        for value in (None, True, [], {}, "unknown"):
            with self.subTest(profile=value):
                self.assert_refused("subject-profile-invalid", {**self.fixture.parameters, "subject_profile": value})

    def test_full_intent_hash_and_source_snapshot_are_required(self) -> None:
        self.assert_refused("subject-intent-stale", {**self.fixture.parameters, "subject_intent_sha256": "0" * 64})
        self.fixture.path.write_bytes(self.fixture.before + b"\nconcurrent fixture edit\n")
        with self.assertRaises(LifecycleError) as raised:
            native.subject_update_action(self.fixture.root, self.fixture.parameters)
        self.assertEqual("subject-pin-stale", raised.exception.code)
        self.assertEqual(self.fixture.before + b"\nconcurrent fixture edit\n", self.fixture.path.read_bytes())
        self.assertFalse(self.fixture.archive.exists())

    def test_duplicate_original_is_preserved_on_refusal(self) -> None:
        duplicate = self.fixture.path.with_name("CA-R-8100--competing-original.md")
        duplicate.write_bytes(self.fixture.before)
        self.assert_refused("subject-identity-duplicate")
        self.assertEqual(self.fixture.before, duplicate.read_bytes())

    def test_stale_or_missing_report_is_unresolved_and_cannot_apply(self) -> None:
        report = self.fixture.root / self.fixture.parameters["semantic_assessment_report"]["path"]
        report.write_bytes(report.read_bytes() + b"\nchanged fixture report\n")
        for parameters in (self.fixture.parameters, {key: value for key, value in self.fixture.parameters.items() if key != "semantic_assessment_report"}):
            with self.subTest(report_present="semantic_assessment_report" in parameters):
                result = native.subject_update_action(self.fixture.root, parameters, execute=True, authorized=True)
                self.assertEqual("unresolved", result["outcome"])
                self.assertEqual("semantic-assessment-unverified", result["classification"]["reason"])
                self.fixture.assert_unchanged(self)

    def test_empty_patch_noop_keeps_version_time_hash_and_has_no_archive(self) -> None:
        parameters = copy.deepcopy(self.fixture.parameters)
        parameters["subject_patches"] = []
        prepared = subject_patch.prepare_subject_intent(self.fixture.root, self.fixture.target, [], subject_profile="approved")
        parameters["subject_intent_sha256"] = prepared["subject_intent_sha256"]
        parameters.pop("semantic_assessment_report")
        result = native.subject_update_action(self.fixture.root, parameters)
        self.assertEqual("no-op", result["outcome"])
        self.assertIsNone(result["subject_intent"]["predecessorArchive"])
        self.assertEqual({"version": self.fixture.target["version"], "updated_at": self.fixture.target["updated_at"],
                          "after_sha256": self.fixture.target["digest"]}, result["materialization"])
        self.fixture.assert_unchanged(self)


if __name__ == "__main__":
    unittest.main()
