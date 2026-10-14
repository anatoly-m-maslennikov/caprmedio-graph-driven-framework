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
from selected_workflows_docker_fixture import GoldenCase, GoldenProject, MANIFEST_REF, digest  # noqa: E402
from subject_notation import get_profile  # noqa: E402


TEST_TEMP_ROOT = REPOSITORY / ".caprmedio_tmp/tests/test_subject_apply_portfolio"
TEST_TEMP_ROOT.mkdir(parents=True, exist_ok=True)
CORE_OPERATIONS = ".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/09_operations/"
TOOL_WORKFLOWS = ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS/"
CURRENT_W02_PINS = {
    "CA-O-067": (CORE_OPERATIONS + "CA-O-067-CORE_META_MODEL-ACTION--assess-atom-update-identity.md", 7,
                 "5c2098027094df1837b3b48b112a56866e3bee927699a58156e51b53925e998d"),
    "CA-O-127": (CORE_OPERATIONS + "CA-O-127-CORE_META_MODEL-WORKFLOW--manage-atom-lifecycle.md", 4,
                 "cb06d919ac51982a7eba820f62939cabefb7e7698de208345f46a97c5283f557"),
    "CA-O-128": (CORE_OPERATIONS + "CA-O-128-CORE_META_MODEL-ACTION--apply-authorized-atom-lifecycle-changes.md", 6,
                 "48f0464400d198b0d914fbd2b76bd8d8ce616c94b41bd140ec5889ac6b9ac2e2"),
    "CA-O-129": (CORE_OPERATIONS + "CA-O-129-CORE_META_MODEL-STEP--apply-an-admitted-atom-lifecycle-change.md", 4,
                 "fd95ab7ee49b96d9a33ceb951934e274e087ba47f349a0455b7654fc8ff546a1"),
    "CA-O-145": (CORE_OPERATIONS + "CA-O-145-CORE_META_MODEL-STEP--assess-update-identity-for-atom-lifecycle.md", 2,
                 "e1da6f807f965d94bb2f6b829767fb23d34ea6dc600408f78408378caf208f89"),
}
PUBLICATION_PINS = {
    "CA-R-866": (TOOL_WORKFLOWS + "04_requirement/CA-R-866-TOOL_WORKFLOWS-STANDARD-REQUIREMENT--update-caprmedio-markdown-atoms.md", 23,
                 "98e303d6e0c09510d6dde40c10dc3d8ffa73e05296240bea6f238e480a30904a"),
    "CA-M-371": (TOOL_WORKFLOWS + "05_method/CA-M-371-TOOL_WORKFLOWS-STANDARD-METHOD--preview-exact-subject-patches.md", 11,
                 "5f775dcbbd365378731b7039b47c78d4c4eebaeb0991ed7850c0c44638d63d79"),
    "CA-E-304": (TOOL_WORKFLOWS + "06_evaluation/CA-E-304-TOOL_WORKFLOWS-STANDARD-QA_CASE--verify-update-sealed-caprmedio-atom-carriers.md", 22,
                 "8f72d065cf1a96791817bc412051cb5e14504c3462a08e4a0211c528fa1e854b"),
    "CA-O-030": (TOOL_WORKFLOWS + "09_operations/CA-O-030-TOOL_WORKFLOWS-STANDARD-ACTION--update-sealed-caprmedio-atom-carriers.md", 16,
                 "bf45abea494d78a59fa956fdccc5398408f4c4aaf114443cb92b0b510c22241f"),
    "CA-E-626": (TOOL_WORKFLOWS + "06_evaluation/CA-E-626-TOOL_WORKFLOWS-CORE-QA_CASE--verify-independent-atom-workflow-effects.md", 3,
                 "8cd555ffefdc8f59b80a5120b6b5e4fbe90fb9ea46396bea6d0bcbd1e7d081c5"),
}


class CurrentSubjectGoldenProject(GoldenProject):
    """New isolated W02 manifest; not a refresh of accepted release evidence."""

    def _copy_reviewed_manifest(self):
        original = json.loads((self.source_root / MANIFEST_REF).read_bytes())
        route = copy.deepcopy(next(row for row in original["routes"] if row["route"] == "update_atom"))
        pins = [route["workflow"], *route["ordered_actions"], *route["native_action_calls"]]
        pins.extend(pin for pair in route["ordered_steps"] for pin in pair.values())
        current = {**CURRENT_W02_PINS, "CA-O-030": PUBLICATION_PINS["CA-O-030"]}
        assert {pin["atom_id"] for pin in pins} == set(current)
        for pin in pins:
            path, version, sha256 = current[pin["atom_id"]]
            self._copy_pinned(Path(path), sha256)
            frontmatter, _ = operations.split_frontmatter((self.root / path).read_text())
            assert operations.frontmatter_scalar(frontmatter, "atom_id") == pin["atom_id"]
            assert operations.frontmatter_scalar(frontmatter, "version") == str(version)
            pin.update(source_path=path, version=version, digest=sha256)
        for path, version, sha256 in PUBLICATION_PINS.values():
            self._copy_pinned(Path(path), sha256)
            frontmatter, _ = operations.split_frontmatter((self.root / path).read_text())
            assert operations.frontmatter_scalar(frontmatter, "version") == str(version)
        freshness = copy.deepcopy(original["source_freshness"])
        self._copy_pinned(Path(freshness["selected_source_registry_ref"]), freshness["selected_source_registry_digest"])
        freshness["selected_binding_digest"] = digest([route])
        manifest = {"routes": [route], "source_freshness": freshness}
        manifest["canonical_manifest_sha256"] = digest(manifest)
        self.manifest_path.parent.mkdir(parents=True, exist_ok=True)
        self.manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
        return manifest


class SubjectApplyProject:
    """One current-contract W02 fixture, retaining real admission and validation."""

    def __init__(self, root: Path, *, noop: bool = False, newline: str = "\n", subject_profile: str = "approved",
                 role: str = "Requirement", status: str = "Active") -> None:
        self.root = root
        self.golden = CurrentSubjectGoldenProject(REPOSITORY, root, GoldenCase("W02", "update_atom"))
        self.manifest = self.golden.prepare()
        settings = root / operations.SETTINGS_PATH
        settings.write_text(
            '[project]\nkey = "subject-apply-fixture"\nname = "subject-apply-fixture"\n'
            'repository_slug = "subject-apply-fixture"\n'
            '[artifacts.identity]\nproject_prefix = "CA"\n\n' + settings.read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        self.golden._write_complete_carrier_project_structure()
        self.golden._copy_complete_carrier_authority()
        for grammar_pin in get_profile(subject_profile).grammar_pins:
            original = REPOSITORY / grammar_pin.path
            assert hashlib.sha256(original.read_bytes()).hexdigest() == grammar_pin.sha256
            destination = root / grammar_pin.path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(original, destination)
        self.path = self.golden.status_atom(role, status, number=8100)
        assert newline in {"\n", "\r\n"}
        if newline == "\r\n":
            self.path.write_bytes(self.path.read_bytes().replace(b"\n", b"\r\n"))
        self.path.chmod(0o640)
        self.before = self.path.read_bytes()
        self.before_mode = self.path.stat().st_mode & 0o777
        self.target = carrier_descriptor(root, self.path.relative_to(root).as_posix())
        self.patches = [] if noop else [{"field": "governs", "old": "Atom/Test",
                                        "new": "Atom.State" if subject_profile == "approved" else "Atom/State"}]
        self.prepared = subject_patch.prepare_subject_intent(root, self.target, self.patches, subject_profile=subject_profile)
        self.parameters = {
            "target": self.target, "subject_patches": self.patches,
            "subject_intent_sha256": self.prepared["subject_intent_sha256"], "subject_profile": subject_profile,
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

    def confirmation(self, frozen):
        from atom_subject_stage import stage_subject_preview
        from subject_publication_authorization import authorize_subject_publication

        staged = stage_subject_preview(self.root, [{"selector": self.target["path"],
            "expected": {"atom_id": self.target["atom_id"], "version": self.target["version"],
                         "sha256": self.target["digest"]}, "subject_patches": self.patches}],
            timestamp="2026-10-13 14:00:00 +0400", subject_profile=self.parameters.get("subject_profile", "legacy"))
        self.staged = staged
        execution = frozen["request"]["execution"]
        return authorize_subject_publication(self.root, execution, operator_name="golden-operator",
            llm_session={"app": "run-support", "uuid": execution["request_id"]},
            staged_manifest={"path": staged["manifest_path"], "digest": staged["manifest_sha256"]})

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
