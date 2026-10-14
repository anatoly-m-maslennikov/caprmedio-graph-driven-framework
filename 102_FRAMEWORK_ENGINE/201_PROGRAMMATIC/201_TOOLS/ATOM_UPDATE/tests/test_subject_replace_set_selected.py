"""Whole dependency-set replacement through real selected native publication."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[2]
APP = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for location in (TOOLS, APP, Path(__file__).resolve().parent):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

import atom_operations as operations  # noqa: E402
import atom_subject_apply as native  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
import work_journal  # noqa: E402
from lifecycle_intents import LifecycleError, carrier_descriptor  # noqa: E402
from test_subject_apply_portfolio import REPOSITORY, SubjectApplyProject  # noqa: E402


SCRATCH = REPOSITORY / ".caprmedio_tmp/tests/subject-replace-set-selected"
SCRATCH.mkdir(parents=True, exist_ok=True)
EFFECT_TIME = "2026-10-14 12:20:21 +0400"


class SubjectReplaceSetSelectedTests(unittest.TestCase):
    def fixture(self, *, newline="\n"):
        directory = tempfile.TemporaryDirectory(dir=SCRATCH, ignore_cleanup_errors=True)
        self.addCleanup(directory.cleanup)
        fixture = SubjectApplyProject(Path(directory.name), newline=newline)
        source = fixture.before.replace(b"  depends_on: []", b'  depends_on: [Atom, "Atom/Revision"]')
        self.assertNotEqual(fixture.before, source)
        fixture.path.write_bytes(source)
        fixture.before = source
        fixture.target = carrier_descriptor(fixture.root, fixture.path.relative_to(fixture.root).as_posix())
        fixture.patches = [{"field": "depends_on", "operation": "replace_set",
                            "old": ["Atom/Revision", "Atom"], "new": ["Atom"]}]
        fixture.prepared = subject_patch.prepare_subject_intent(
            fixture.root, fixture.target, fixture.patches, subject_profile="approved")
        fixture.parameters = {
            "target": fixture.target, "subject_patches": fixture.patches, "subject_profile": "approved",
            "subject_intent_sha256": fixture.prepared["subject_intent_sha256"],
            "semantic_assessment_report": fixture.golden._semantic_assessment_report(
                fixture.target, fixture.prepared["proposed"]),
        }
        fixture.golden._semantic_update_parameters = fixture.parameters
        fixture.archive = fixture.root / fixture.prepared["subject_intent"]["predecessorArchive"]["path"]
        return fixture

    def terminal_native(self, fixture, frozen, result):
        child = next(row["requested_run_id"] for row in frozen["request"]["execution"]["requested_runs"]
                     if row["definition"]["atom_id"] == "CA-O-030")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == child)
        retained = json.loads((fixture.root / terminal["result_ref"]).read_bytes())
        return child, terminal, retained

    def test_collapsed_set_publishes_exact_current_predecessor_and_journal(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                fixture = self.fixture(newline=newline)
                self.assertEqual(fixture.patches, fixture.prepared["subject_intent"]["subject_patches"])
                runner, frozen = fixture.execution(f"replace-set-selected-{len(newline)}")
                confirmation = fixture.confirmation(frozen)
                fixture.assert_unchanged(self)
                with patch.object(native, "current_timestamp", return_value=EFFECT_TIME):
                    result = runner._dispatch_confirmed_subject(frozen, confirmation)
                child, terminal, retained = self.terminal_native(fixture, frozen, result)
                actual = retained["native_result"]
                expected = fixture.before.replace(
                    b'  depends_on: [Atom, "Atom/Revision"]', b'  depends_on: ["Atom"]', 1
                ).replace(
                    f"version: {fixture.target['version']}{newline}".encode(),
                    f"version: {fixture.target['version'] + 1}{newline}".encode(), 1
                ).replace(
                    f"updated_at: '{fixture.target['updated_at']}'".encode(),
                    f'updated_at: "{EFFECT_TIME}"'.encode(), 1
                )
                self.assertEqual("terminal", result["disposition"])
                self.assertEqual("completed", terminal["outcome"])
                self.assertEqual("applied", actual["outcome"])
                self.assertEqual("admitted", retained["lifecycle_recording"]["state"])
                self.assertEqual(expected, fixture.path.read_bytes())
                self.assertEqual(fixture.before, fixture.archive.read_bytes())
                for path in (fixture.path, fixture.archive):
                    self.assertEqual(fixture.before_mode, path.stat().st_mode & 0o777)
                subjects = operations.parse_carrier(expected, fixture.path).metadata["subjects"]
                self.assertEqual({"governs": "Atom/Test", "depends_on": ["Atom"]}, subjects)
                observed = {**fixture.target, "version": fixture.target["version"] + 1,
                            "digest": hashlib.sha256(expected).hexdigest(), "updated_at": EFFECT_TIME}
                predecessor = {**fixture.target, "path": fixture.archive.relative_to(fixture.root).as_posix(),
                               "filename": fixture.archive.name, "lifecycle": "archived"}
                self.assertEqual(observed, actual["observed"])
                self.assertEqual(predecessor, actual["history"]["prior_revision"])
                self.assertEqual([
                    {"state": "changed", "carrier": observed},
                    {"state": "changed", "carrier": predecessor},
                ], actual["effects"])
                refs = sorted([fixture.target["path"], fixture.archive.relative_to(fixture.root).as_posix()])
                self.assertEqual(refs, terminal["effect_refs"])
                events = work_journal.read_records(fixture.root)
                child_events = [event for event in events if event.get("run", {}).get("run_id") == child]
                self.assertEqual(["started", "completed"], [event["event"] for event in child_events])
                self.assertEqual(refs, child_events[-1]["effect_refs"])

    def test_changed_set_with_original_intent_seal_is_refused_without_writes(self):
        fixture = self.fixture()
        parameters = copy.deepcopy(fixture.parameters)
        parameters["subject_patches"][0]["new"] = ["Object"]
        with self.assertRaises(LifecycleError) as caught:
            native.subject_update_action(fixture.root, parameters)
        self.assertEqual("subject-intent-stale", caught.exception.code)
        fixture.assert_unchanged(self)

    def test_changed_reviewed_candidate_refuses_selected_publication_without_effects(self):
        fixture = self.fixture()
        runner, frozen = fixture.execution("replace-set-selected-candidate-stale")
        confirmation = fixture.confirmation(frozen)
        manifest = json.loads((fixture.root / fixture.staged["manifest_path"]).read_bytes())
        candidate = fixture.root / manifest["atoms"][0]["candidate"]["path"]
        changed = candidate.read_bytes() + b"\nchanged reviewed candidate\n"
        candidate.write_bytes(changed)
        original = native.subject_update_action
        errors = []

        def observed(root, parameters, **kwargs):
            try:
                return original(root, parameters, **kwargs)
            except LifecycleError as error:
                if kwargs.get("execute") is True:
                    errors.append(error.code)
                raise

        with patch.object(native, "subject_update_action", side_effect=observed):
            result = runner._dispatch_confirmed_subject(frozen, confirmation)
        child = next(row["requested_run_id"] for row in frozen["request"]["execution"]["requested_runs"]
                     if row["definition"]["atom_id"] == "CA-O-030")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == child)
        self.assertEqual("interrupted_pending", terminal["outcome"])
        self.assertTrue(all(row["effect_refs"] == [] for row in result["terminal_runs"]))
        self.assertEqual(["subject-publication-window-unconfirmed"], errors)
        self.assertEqual(changed, candidate.read_bytes())
        fixture.assert_unchanged(self)


if __name__ == "__main__":
    unittest.main()
