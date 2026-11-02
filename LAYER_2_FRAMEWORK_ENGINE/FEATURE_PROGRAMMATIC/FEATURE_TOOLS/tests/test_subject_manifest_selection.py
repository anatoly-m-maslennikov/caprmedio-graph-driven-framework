"""One approved Atom effect can select its exact entry from a staged batch."""

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "ATOM_UPDATE/tests"))

import atom_subject_patch as subjects  # noqa: E402
from atom_subject_stage import stage_subject_preview  # noqa: E402
from connector_bindings import ConnectorBindingError, capture_source  # noqa: E402
from lifecycle_intents import carrier_descriptor  # noqa: E402
import subject_publication_authorization as authorization  # noqa: E402
from test_subject_apply_portfolio import SubjectApplyProject  # noqa: E402

STAMP = "2026-10-13 14:00:00 +0400"


class SubjectManifestSelectionTests(unittest.TestCase):
    def setUp(self):
        scratch = Path.cwd() / ".caprmedio_tmp/tests/subject-manifest-selection"
        scratch.mkdir(parents=True, exist_ok=True)
        self.directory = tempfile.TemporaryDirectory(dir=scratch)
        self.addCleanup(self.directory.cleanup)
        self.fixture = SubjectApplyProject(Path(self.directory.name).resolve())
        self.root = self.fixture.root
        self.other = self.fixture.golden.status_atom("Requirement", "Active", number=8101)
        self.other_before = self.other.read_bytes()
        self.other_target = carrier_descriptor(
            self.root, self.other.relative_to(self.root).as_posix()
        )
        self.other_prepared = subjects.prepare_subject_intent(
            self.root, self.other_target, self.fixture.patches, subject_profile="approved"
        )
        self.other_request = {
            "target": self.other_target,
            "subject_patches": self.fixture.patches,
            "subject_profile": "approved",
            "subject_intent_sha256": self.other_prepared["subject_intent_sha256"],
        }
        items = [
            {
                "selector": target["path"],
                "expected": {
                    "atom_id": target["atom_id"],
                    "version": target["version"],
                    "sha256": target["digest"],
                },
                "subject_patches": self.fixture.patches,
            }
            for target in (self.fixture.target, self.other_target)
        ]
        self.staged = stage_subject_preview(
            self.root, items, timestamp=STAMP, subject_profile="approved"
        )
        self.manifest_path = self.root / self.staged["manifest_path"]
        self.manifest = json.loads(self.manifest_path.read_bytes())
        self.pin = {"path": self.staged["manifest_path"], "digest": self.staged["manifest_sha256"]}

    def reviewed(self, request=None, prepared=None, pin=None):
        return authorization._reviewed_subject_candidate(
            self.root,
            self.fixture.parameters if request is None else request,
            self.fixture.prepared if prepared is None else prepared,
            self.pin if pin is None else pin,
        )

    def changed_pin(self, manifest):
        self.manifest_path.write_bytes(json.dumps(manifest).encode())
        return {
            "path": self.pin["path"],
            "digest": hashlib.sha256(self.manifest_path.read_bytes()).hexdigest(),
        }

    def test_each_entry_selects_exact_candidate_and_keeps_whole_batch_pin(self):
        for request, prepared, ordinal in (
            (self.fixture.parameters, self.fixture.prepared, 0),
            (self.other_request, self.other_prepared, 1),
        ):
            staged, candidate, raw = self.reviewed(request, prepared)
            self.assertEqual(self.pin["digest"], staged.sha256)
            self.assertEqual(
                self.manifest["atoms"][ordinal]["candidate"]["path"],
                candidate.relative_path.as_posix(),
            )
            self.assertEqual(raw, (self.root / candidate.relative_path).read_bytes())
        self.fixture.assert_unchanged(self)
        self.assertEqual(self.other_before, self.other.read_bytes())

    def test_prior_unselected_source_change_does_not_rebind_or_repreview_batch(self):
        version = self.other_target["version"]
        changed = self.other_before.replace(
            f"version: {version}\n".encode(), f"version: {version + 1}\n".encode()
        )
        self.assertNotEqual(self.other_before, changed)
        self.other.write_bytes(changed)
        staged, _, _ = self.reviewed()
        self.assertEqual(self.pin["digest"], staged.sha256)
        self.assertEqual(self.manifest["preview_sha256"], self.staged["preview"]["preview_sha256"])

    def test_missing_ambiguous_or_mismatched_selected_entries_refuse(self):
        cases = [[], [self.manifest["atoms"][1]], [self.manifest["atoms"][0]] * 2]
        cases.append([self.manifest["atoms"][0]])  # A batch seal is not a singleton seal.
        for field, value in (
            ("path", self.other_target["path"]),
            ("atom_id", "CA-R-999999"),
            ("version", 999),
            ("sha256", "0" * 64),
        ):
            atoms = copy.deepcopy(self.manifest["atoms"])
            atoms[0]["source"][field] = value
            atoms[0]["validation"]["logical_source_path"] = atoms[0]["source"]["path"]
            cases.append(atoms)
        atoms = copy.deepcopy(self.manifest["atoms"])
        atoms[0]["subject_intent_sha256"] = "0" * 64
        cases.append(atoms)
        for atoms in cases:
            with self.subTest(atoms=atoms):
                manifest = {**self.manifest, "atoms": atoms}
                with self.assertRaises(authorization.SubjectPublicationAuthorizationError):
                    self.reviewed(pin=self.changed_pin(manifest))

    def test_closed_manifest_and_unselected_entry_schema_remain_required(self):
        cases = [
            {**self.manifest, "extra": True},
            {**self.manifest, "schema_version": True},
            {**self.manifest, "preview_sha256": "bad"},
        ]
        for key, value in (
            ("extra", True),
            ("validation", {"state": "passed"}),
            ("candidate", {"path": "../unsafe", "sha256": "0" * 64}),
        ):
            manifest = copy.deepcopy(self.manifest)
            manifest["atoms"][1][key] = value
            cases.append(manifest)
        for manifest in cases:
            with self.subTest(manifest=manifest):
                with self.assertRaises(authorization.SubjectPublicationAuthorizationError):
                    self.reviewed(pin=self.changed_pin(manifest))

    def test_candidate_tampering_or_rehashed_wrong_proposal_refuses(self):
        atom = self.manifest["atoms"][0]
        path = self.root / atom["candidate"]["path"]
        path.write_bytes(path.read_bytes() + b"\nchanged\n")
        with self.assertRaises(ConnectorBindingError):
            self.reviewed()
        manifest = copy.deepcopy(self.manifest)
        manifest["atoms"][0]["candidate"]["sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
        with self.assertRaises(authorization.SubjectPublicationAuthorizationError):
            self.reviewed(pin=self.changed_pin(manifest))

    def test_confirmation_keeps_entire_manifest_current_but_effect_is_one_atom(self):
        runner, frozen = self.fixture.execution("multi-entry-confirmation")
        confirmation = authorization.authorize_subject_publication(
            self.root,
            frozen["request"]["execution"],
            operator_name="golden-operator",
            llm_session={
                "app": "run-support",
                "uuid": frozen["request"]["execution"]["request_id"],
            },
            staged_manifest=self.pin,
        )
        self.assertIn(capture_source(self.root, self.pin["path"]), confirmation._record.authorities)
        result = runner._dispatch_confirmed_subject(frozen, confirmation)
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertEqual(self.other_before, self.other.read_bytes())

    def test_change_to_unselected_manifest_row_invalidates_confirmed_single_effect(self):
        runner, frozen = self.fixture.execution("multi-entry-manifest-drift")
        confirmation = authorization.authorize_subject_publication(
            self.root,
            frozen["request"]["execution"],
            operator_name="golden-operator",
            llm_session={
                "app": "run-support",
                "uuid": frozen["request"]["execution"]["request_id"],
            },
            staged_manifest=self.pin,
        )
        changed = copy.deepcopy(self.manifest)
        changed["atoms"][1]["candidate"]["sha256"] = "0" * 64
        self.changed_pin(changed)
        result = runner._dispatch_confirmed_subject(frozen, confirmation)
        self.assertNotEqual("completed", result.get("outcome"))
        self.fixture.assert_unchanged(self)
        self.assertEqual(self.other_before, self.other.read_bytes())


if __name__ == "__main__":
    unittest.main()
