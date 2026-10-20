from __future__ import annotations

import argparse
import hashlib
import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[2]
UPDATE_TESTS = TOOLS / "ATOM_UPDATE/tests"
for directory in (TOOLS, TOOLS / "ATOM_UPDATE", UPDATE_TESTS):
    if str(directory) not in sys.path:
        sys.path.insert(0, str(directory))

import atom_operations as operations  # noqa: E402
import atom_update as update_provider  # noqa: E402
from atom_subject_lookup import run_subject_search  # noqa: E402
import test_nonarchived_subject_preview as fixtures  # noqa: E402
from frozen_selected_workflows import frozen_preparation_bindings, frozen_source_bytes  # noqa: E402


class InstanceSubjectFlowTests(unittest.TestCase):
    """Exercise named-instance notation through public search and subject staging."""

    def setUp(self) -> None:
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.path = self.fixture._plan("Done", number=7901)
        self.kind_and_instance = "Entity/Node/Continuant/Atom//Fixture Rule"
        self.governs_subject = f"{self.kind_and_instance}.Status"
        self.dependency_subject = f"{self.kind_and_instance}.Version Number"
        self.new_governs_subject = f"{self.kind_and_instance}.Summary"
        self.new_dependency_subject = f"{self.kind_and_instance}.Updated At"
        self.path.write_bytes(
            self.path.read_bytes()
            .replace(b'governs: "Atom/Status"', f'governs: "{self.governs_subject}"'.encode())
            .replace(b'"Atom/Revision"', f'"{self.dependency_subject}"'.encode())
        )
        self.original = self.path.read_bytes()
        for pin in update_provider.SOURCE_PINS:
            binding = frozen_preparation_bindings()[pin["atom_id"]]
            destination = self.root / pin["path"]
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(frozen_source_bytes(pin["path"], binding["sha256"]))
        self.adapter = update_provider.create_adapter(self.root)
        self.patches = [
            {"field": "governs", "old": self.governs_subject, "new": self.new_governs_subject},
            {"field": "depends_on", "old": self.dependency_subject, "new": self.new_dependency_subject},
        ]
        self.item = {
            "atom_id": "CA-P-7901",
            "version": 7,
            "sha256": hashlib.sha256(self.original).hexdigest(),
            "subject_patches": self.patches,
        }
        self.request = {
            "operation": "preview_subjects",
            "subject_profile": "approved",
            "atoms": [self.item],
        }

    def test_named_instance_subject_search_preview_and_stage(self) -> None:
        search = run_subject_search(
            self.root,
            argparse.Namespace(
                subject=self.kind_and_instance,
                subject_field="both",
                subject_match="prefix",
                content_role=["Plan"],
                scope_unit=None,
                under=None,
                lifecycle="all",
                atom=None,
                query=None,
                limit=None,
                subject_profile="approved",
            ),
        )
        occurrences = [row for row in search["occurrences"] if row["atom_id"] == "CA-P-7901"]
        self.assertEqual(2, search["count"])
        self.assertEqual({"CA-P-7901"}, {row["atom_id"] for row in search["occurrences"]})
        self.assertEqual({"governs", "depends_on"}, {row["field"] for row in occurrences}, search)
        self.assertEqual({self.governs_subject, self.dependency_subject},
                         {row["value"] for row in occurrences})

        before = {path.relative_to(self.root).as_posix(): path.read_bytes()
                  for path in self.root.rglob("*") if path.is_file()}
        preview = self.adapter.invoke(self.request).model_dump(mode="json")
        self.assertEqual([], preview["errors"])
        proposal = preview["preview"]["atoms"][0]["proposed_carrier"].encode("utf-8")
        expected = self.original.replace(
            f'governs: "{self.governs_subject}"'.encode(),
            f'governs: "{self.new_governs_subject}"'.encode(),
        ).replace(
            f'"{self.dependency_subject}"'.encode(),
            f'"{self.new_dependency_subject}"'.encode(),
        )
        expected = expected.replace(b"version: 7\r\n", b"version: 8\r\n")
        expected = expected.replace(
            b'updated_at: "2026-01-01 00:00:00 +0000"',
            f'updated_at: "{preview["preview"]["illustrative_updated_at"]}"'.encode(),
        )
        self.assertEqual(expected, proposal)
        parsed = operations.parse_carrier(proposal, self.path)
        self.assertEqual("CA-P-7901", parsed.metadata["atom_id"])
        self.assertEqual(self.new_governs_subject, parsed.metadata["subjects"]["governs"])
        self.assertEqual(["Atom", self.new_dependency_subject], parsed.metadata["subjects"]["depends_on"])
        self.assertEqual("Done", parsed.metadata["status"])
        self.assertIn(b"The exact body mentions Atom/Status.", proposal)
        self.assertEqual(self.original, self.path.read_bytes())
        self.assertEqual(before, {path.relative_to(self.root).as_posix(): path.read_bytes()
                                  for path in self.root.rglob("*") if path.is_file()})

        stage_request = {
            **self.request,
            "operation": "stage_subjects",
            "preview_sha256": preview["preview"]["preview_sha256"],
            "illustrative_updated_at": preview["preview"]["illustrative_updated_at"],
        }
        staged = self.adapter.invoke(stage_request).model_dump(mode="json")
        self.assertEqual([], staged["errors"])
        self.assertTrue(staged["staging"]["sources_unchanged"])
        self.assertEqual(self.original, self.path.read_bytes())
        self.assertEqual("CA-P-7901", parsed.metadata["atom_id"])


if __name__ == "__main__":
    unittest.main()
