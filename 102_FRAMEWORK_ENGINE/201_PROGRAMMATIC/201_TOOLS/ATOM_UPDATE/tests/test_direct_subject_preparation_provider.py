"""Canonical preparation provider over real source-bound native helpers."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[2]
REPOSITORY = TOOLS.parents[2]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "ATOM_UPDATE"))

import atom_update as provider
import atom_operations as operations
import atom_subject_patch as subjects
import test_nonarchived_subject_preview as fixtures


class DirectSubjectPreparationProviderTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan("Done", number=7801)
        self.original = self.path.read_bytes()
        for pin in provider.SOURCE_PINS:
            destination = self.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(REPOSITORY / pin["path"], destination)
            metadata = operations.parse_carrier(destination.read_bytes(), destination).metadata
            self.assertEqual(pin["atom_id"], metadata["atom_id"])
            self.assertIs(type(metadata["version"]), int)
            self.assertGreater(metadata["version"], 0)
        self.adapter = provider.create_adapter(self.root)
        self.item = {"atom_id": "CA-P-7801", "version": 7, "sha256": hashlib.sha256(self.original).hexdigest(),
                     "subject_patches": [{"field": "governs", "old": "Atom/Status", "new": "Atom/State"}]}
        self.request = {"operation": "preview_subjects", "subject_profile": "legacy", "atoms": [self.item]}

    def ledger(self, directory=None):
        base = self.root if directory is None else directory
        return {p.relative_to(self.root).as_posix(): (p.read_bytes(), p.stat().st_mode & 0o777)
                for p in base.rglob("*") if p.is_file()}

    def invoke(self, request=None):
        before = self.ledger(self.root / ".caprmedio_caprmedio")
        result = self.adapter.invoke(self.request if request is None else request).model_dump(mode="json")
        self.assertEqual(before, self.ledger(self.root / ".caprmedio_caprmedio"))
        return result

    def stage_request(self, preview, **overrides):
        request = {**self.request, "operation": "stage_subjects", "preview_sha256": preview["preview_sha256"],
                   "illustrative_updated_at": preview["illustrative_updated_at"]}
        request.update(overrides)
        return request

    def test_preview_retains_exact_native_seal_and_changes_no_files(self):
        before = self.ledger()
        result = self.invoke()
        self.assertEqual(before, self.ledger())
        self.assertEqual({"operation", "preview", "staging", "errors"}, set(result))
        self.assertEqual("preview_subjects", result["operation"])
        self.assertIsNone(result["staging"])
        self.assertEqual([], result["errors"])
        preview = result["preview"]
        items = self.fixture._payload(self.path)
        expected = subjects.preview_subject_patches(self.root, items, subject_profile="legacy",
                                                    timestamp=preview["illustrative_updated_at"])
        self.assertEqual(expected, preview)
        unsigned = {key: value for key, value in preview.items() if key != "preview_sha256"}
        seal = hashlib.sha256(operations.canonical_json(unsigned).encode()).hexdigest()
        self.assertEqual(seal, preview["preview_sha256"])
        self.assertEqual(self.original, self.path.read_bytes())

    def test_stage_reuses_reviewed_seal_time_and_only_exports_scratch(self):
        preview = self.invoke()["preview"]
        before = self.ledger()
        result = self.invoke(self.stage_request(preview))
        self.assertEqual([], result["errors"])
        self.assertEqual(preview, result["preview"])
        staging = result["staging"]
        self.assertEqual({"staging_only", "illustrative", "sources_unchanged", "stage_root", "manifest_path", "manifest_sha256"}, set(staging))
        stage_root = Path(staging["stage_root"])
        self.assertEqual(Path(".caprmedio_tmp/subject-preview"), stage_root.parent)
        manifest_path = self.root / staging["manifest_path"]
        manifest_raw = manifest_path.read_bytes()
        self.assertEqual(staging["manifest_sha256"], hashlib.sha256(manifest_raw).hexdigest())
        manifest = json.loads(manifest_raw)
        self.assertEqual(preview["preview_sha256"], manifest["preview_sha256"])
        candidate = self.root / manifest["atoms"][0]["candidate"]["path"]
        self.assertEqual(preview["atoms"][0]["proposed_carrier"].encode(), candidate.read_bytes())
        after = self.ledger()
        self.assertTrue(set(after) - set(before))
        self.assertTrue(all(Path(name).is_relative_to(stage_root) for name in set(after) - set(before)))
        for name, state in before.items():
            self.assertEqual(state, after[name])

    def test_stage_wrong_seal_refuses_before_scratch_creation(self):
        preview = self.invoke()["preview"]
        before = self.ledger()
        result = self.invoke(self.stage_request(preview, preview_sha256="0" * 64))
        self.assertIsNone(result["preview"])
        self.assertIsNone(result["staging"])
        self.assertEqual("subject-stage-preview-mismatch", result["errors"][0]["code"])
        self.assertEqual(before, self.ledger())
        self.assertFalse((self.root / ".caprmedio_tmp/subject-preview").exists())
        self.assertEqual({"code", "message", "stage_root", "retained_artifacts", "unverified_artifacts"}, set(result["errors"][0]))
        self.assertIsNone(result["errors"][0]["stage_root"])
        self.assertEqual([], result["errors"][0]["retained_artifacts"])

    def test_noop_preview_and_stage_keep_source_metadata_and_null_time(self):
        request = copy.deepcopy(self.request)
        request["atoms"][0]["subject_patches"] = []
        result = self.invoke(request)
        preview = result["preview"]
        self.assertTrue(preview["noop"])
        self.assertIsNone(preview["illustrative_updated_at"])
        self.assertEqual(self.original, preview["atoms"][0]["proposed_carrier"].encode())
        stage = {**request, "operation": "stage_subjects", "preview_sha256": preview["preview_sha256"], "illustrative_updated_at": None}
        staged = self.invoke(stage)
        self.assertEqual([], staged["errors"])
        self.assertEqual(preview, staged["preview"])
        self.assertEqual(self.original, self.path.read_bytes())

    def test_closed_requests_reject_physical_mixed_unsupported_and_duplicate_ids(self):
        invalid = [{**self.request, key: value} for key, value in (
            ("root", str(self.root)), ("selector", "source.md"), ("destination", "scratch"),
            ("session_id", "session"), ("apply", True), ("subject_profile", None),
        )]
        for change in ({"version": True}, {"version": 0}, {"selector": "source.md"}, {"content": "changed"},
                       {"subject_patches": [{"field": "depends_on", "operation": "add", "value": "Atom"}]},
                       {"subject_patches": [{"field": "governs", "index": 0, "old": "Atom/Status", "new": "Atom"}]}):
            invalid.append({**self.request, "atoms": [{**self.item, **change}]})
        invalid.extend([{**self.request, "atoms": [self.item, self.item]},
                        {**self.request, "operation": "stage_subjects"},
                        {key: value for key, value in self.request.items() if key != "subject_profile"}])
        for request in invalid:
            with self.subTest(request=request), self.assertRaises(ValueError):
                provider.SubjectPreparationRequest.model_validate(request)

    def test_invalid_definition_refuses_before_native_preparation(self):
        definition = self.root / provider.SOURCE_PINS[0]["path"]
        definition.write_bytes(definition.read_bytes().replace(b"atom_id: CA-R-866", b"atom_id: CA-R-999", 1))
        before = self.ledger()
        with patch.object(provider.subjects, "preview_subject_patches", side_effect=AssertionError("stale definition reached preview")):
            result = self.invoke()
        self.assertIsNone(result["preview"])
        self.assertIsNone(result["staging"])
        self.assertTrue(result["errors"])
        self.assertEqual(before, self.ledger())

    def test_current_same_identity_rule_revision_is_accepted(self):
        definition = self.root / provider.SOURCE_PINS[0]["path"]
        definition.write_text(re.sub(r"(?m)^version: .*", "version: 123", definition.read_text()) + "\nUpdated rule.\n")
        self.assertEqual([], self.invoke()["errors"])

    def test_current_rule_metadata_is_validated(self):
        definition = self.root / provider.SOURCE_PINS[0]["path"]
        original = definition.read_text()
        for field, value in (("content_role", "Plan"), ("status", "Archived"),
                             ("version", "0"), ("version", "true"), ("version", "'2'")):
            with self.subTest(field=field, value=value):
                definition.write_text(re.sub(rf"(?m)^{field}: .*", f"{field}: {value}", original))
                with patch.object(provider.subjects, "preview_subject_patches", side_effect=AssertionError("invalid definition reached preview")):
                    result = self.invoke()
                self.assertIsNone(result["preview"])
                self.assertTrue(result["errors"])
        definition.write_text(re.sub(r"(?m)^status: .*\n", "", original))
        with patch.object(provider.subjects, "preview_subject_patches", side_effect=AssertionError("missing Status reached preview")):
            result = self.invoke()
        self.assertIsNone(result["preview"])
        self.assertTrue(result["errors"])

    def test_captured_rule_drift_during_preparation_refuses(self):
        definition = self.root / provider.SOURCE_PINS[0]["path"]
        original = definition.read_bytes()
        native_preview = provider.subjects.preview_subject_patches

        def drift_after_native_preview(*args, **kwargs):
            preview = native_preview(*args, **kwargs)
            definition.write_bytes(original + b"\nExternal mid-call rule drift.\n")
            return preview

        try:
            with patch.object(provider.subjects, "preview_subject_patches", drift_after_native_preview):
                result = self.adapter.invoke(self.request).model_dump(mode="json")
            self.assertIsNone(result["preview"])
            self.assertEqual("subject-source-changed", result["errors"][0]["code"])
            self.assertEqual(self.original, self.path.read_bytes())
        finally:
            definition.write_bytes(original)

    def test_descriptor_advertises_only_preparation_binding_and_scratch_effects(self):
        before = self.ledger()
        descriptor = provider.describe_tool()
        self.assertEqual(before, self.ledger())
        self.assertEqual("ATOM_UPDATE", descriptor["identity"]["name"])
        self.assertEqual({"read_only_hint": False, "destructive_hint": False,
                          "idempotent_hint": False, "open_world_hint": False}, descriptor["effect_hints"])
        self.assertEqual(["CA-O-030"], descriptor["binding"]["action_ids"])
        binding = {"name": "ATOM_UPDATE", "mcp_name": "atom_update", "entrypoint": provider.ENTRYPOINT,
                   "source_atom": "CA-D-425", "action_ids": ["CA-O-030"]}
        self.assertTrue(provider.binding_is_admitted(binding))
        self.assertFalse(provider.binding_is_admitted({**binding, "mcp_name": "update_atom"}))


if __name__ == "__main__":
    unittest.main()
