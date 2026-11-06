"""Native nested Header effects retain the exact predecessor and unrelated data."""
import copy
from pathlib import Path
import sys
import unittest

import yaml

TOOLS = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(TOOLS), str(TOOLS / "tests"), str(TOOLS / "VALIDATE_ATOMS/tests"), str(TOOLS / "ATOM_UPDATE/tests")]

import atom_operations as operations  # noqa: E402
import atom_subject_patch as subject_patch  # noqa: E402
from subject_notation import get_profile  # noqa: E402
from subject_grammar_corpus import grammar_carriers  # noqa: E402
from lifecycle_intents import (  # noqa: E402
    LifecycleError, carrier_descriptor, change_status_atom_action, create_atom_action, move_atom_action,
    update_atom_action,
)
from subject_batch_drafts import make_subject_edit_draft  # noqa: E402
from project_selection import bind_selection, resolve_project  # noqa: E402
import test_nested_header_admission as nested_fixture  # noqa: E402
import test_atom_move_lifecycle as move_fixture  # noqa: E402


class NestedHeaderLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.fixture = nested_fixture.NestedHeaderFunctionalTests("runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.binding = bind_selection(self.fixture.selection)
        self.binding.__enter__()
        self.addCleanup(self.binding.__exit__, None, None, None)
        self.root = self.fixture.root

    def write_current(self):
        self.fixture.path.write_text(nested_fixture.text_of(self.fixture.metadata))
        return self.fixture.path

    def status_request(self, path, status):
        return {"target": carrier_descriptor(self.root, path.relative_to(self.root).as_posix()),
                "status": status}

    def test_create_update_and_archive_keep_nested_state_and_exact_history(self):
        carrier = {"path": self.fixture.path.relative_to(self.root).as_posix(),
                   "frontmatter": yaml.safe_dump(dict(reversed(self.fixture.metadata.items())), sort_keys=False).rstrip("\n"),
                   "content": nested_fixture.projects.PLAN_BODY}
        created = create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
        path = self.root / created["observed"]["path"]
        atom = operations.atom_from_path(self.root, path)
        self.assertEqual(1, yaml.safe_load(atom.frontmatter)["state"]["version"])
        self.assertEqual(["identity", "context", "state", "destination"], list(yaml.safe_load(atom.frontmatter)))
        prior = path.read_bytes()
        result = update_atom_action(self.root, {
            "target": carrier_descriptor(self.root, atom),
            "proposed": {"frontmatter": atom.frontmatter, "content": atom.content + "\n"},
            "change_class": "carrier_only",
        }, execute=True, authorized=True)
        self.assertEqual(prior, (self.root / result["history"]["prior_revision"]["path"]).read_bytes())
        atom = operations.atom_from_path(self.root, path)
        residue = "\npriority: high\nlegacy_unmapped: {flag: false, count: 0} # retained\n"
        path.write_bytes(operations.render(atom.frontmatter + residue, atom.content))
        prior = path.read_bytes()
        archived = change_status_atom_action(self.root, self.status_request(path, "Archived"), execute=True, authorized=True)
        observed = self.root / archived["observed"]["path"]
        header = operations.atom_from_path(self.root, observed).frontmatter
        metadata = yaml.safe_load(header)
        self.assertEqual("Archived", metadata["state"]["status"])
        self.assertEqual(3, metadata["state"]["version"])
        self.assertNotIn("atom_id", metadata)
        self.assertNotIn("version", metadata)
        self.assertIn(residue.rstrip("\n"), header)
        self.assertEqual(prior, (self.root / archived["history"]["prior_revision"]["path"]).read_bytes())

    def test_create_rejects_new_root_residue_without_effect(self):
        metadata = copy.deepcopy(self.fixture.metadata)
        metadata["unadmitted_new_field"] = 3
        carrier = {"path": self.fixture.path.relative_to(self.root).as_posix(),
                   "frontmatter": yaml.safe_dump(metadata, sort_keys=False).rstrip("\n"),
                   "content": nested_fixture.projects.PLAN_BODY}
        with self.assertRaises(LifecycleError):
            create_atom_action(self.root, {"carrier": carrier}, execute=True, authorized=True)
        self.assertFalse(self.fixture.path.exists())

    def test_edit_draft_and_promotion_change_only_nested_identity_and_state(self):
        path = self.write_current()
        before = path.read_bytes()
        draft = make_subject_edit_draft(before, "CA-P-701", 1, root=self.root)
        self.assertEqual(before.replace(b"atom_id: CA-P-701", b'atom_id: "CA-P-701@1-draft"')
                         .replace(b"status: Active", b'status: "Draft"'), draft)
        canonical = operations.atom_from_path(self.root, path)
        marker = operations.DraftMarker("CA-P-701@1-draft", "CA-P-701", 1)
        binding = operations.ExistingDraftPromotion(canonical, marker, 2, False)
        frontmatter, _ = operations.split_frontmatter(draft.decode())
        prepared = operations.prepare_existing_draft_promotion_frontmatter(self.root, frontmatter, binding, "Active")
        metadata = yaml.safe_load(prepared)
        self.assertEqual("CA-P-701", metadata["identity"]["atom_id"])
        self.assertEqual(2, metadata["state"]["version"])
        self.assertEqual("Active", metadata["state"]["status"])
        self.assertNotIn("atom_id", metadata)
        self.assertEqual(before, path.read_bytes())
        lineage = {"origin": {"atom_id": "CA-P-700", "version": 1}}
        retained = operations.replace_draft_revision_lineage(prepared, lineage)
        self.assertEqual(lineage, operations.draft_revision_lineage(retained))
        revised = operations.replace_frontmatter_scalar(retained, "version", "3")
        self.assertEqual(lineage, operations.draft_revision_lineage(revised))

    def test_subject_intent_edits_nested_topics_and_state_spans(self):
        grammar = grammar_carriers()
        for pin in get_profile("approved").grammar_pins:
            role = {"R": "04_requirement", "M": "05_method", "E": "06_evaluation"}[pin.atom_id[3]]
            parent = self.fixture.core / role
            parent.mkdir(exist_ok=True)
            for existing in parent.glob(pin.atom_id + "*.md"):
                existing.unlink()
            (parent / Path(pin.path).name).write_bytes(grammar[pin.path])
        path = self.write_current()
        before = path.read_bytes()
        prepared = subject_patch.prepare_subject_intent(
            self.root, carrier_descriptor(self.root, path.relative_to(self.root).as_posix()),
            [{"field": "governs", "old": "Tool", "new": "Requirement"}],
            subject_profile="approved",
        )
        result = subject_patch.materialize_subject_intent(self.root, prepared, "2026-11-06 12:01:00 +0400")
        metadata = operations.parse_carrier(result["carrier_bytes"], path).metadata
        self.assertEqual("Requirement", metadata["context"]["topics"]["main_subject"])
        self.assertEqual(2, metadata["state"]["version"])
        self.assertNotIn("version", metadata)
        self.assertNotIn("subjects", metadata)
        self.assertEqual(before, path.read_bytes())

    def test_move_updates_context_container_and_nested_destination(self):
        fixture = move_fixture.AtomMoveLifecycleTest("runTest")
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        core = fixture.root / fixture.fixture.declarations["CORE_META_MODEL"]["authority_path"]
        encoding = next((core / "07_delivery").glob("CA-D-657*.md"))
        authority_header, _ = operations.split_frontmatter(encoding.read_text())
        reviewed = TOOLS / "VALIDATE_ATOMS/tests/fixtures/nested_encoding_d657_reviewed.md"
        _, authority_body = operations.split_frontmatter(reviewed.read_text())
        encoding.write_bytes(operations.render(authority_header, authority_body))
        source, destination = fixture.core_path, fixture._destination()
        frontmatter, body = operations.split_frontmatter(source.read_text())
        original = yaml.safe_load(frontmatter)
        metadata = copy.deepcopy(self.fixture.metadata)
        metadata["identity"] = {"atom_id": "CA-R-100", "ref_id": "CA-R-100"}
        metadata["context"].update(role="Requirement", form="Requirement")
        fixture.fixture._materialize_fixture_type_definition("Requirement", "Requirement")
        metadata["context"]["container"] = original["relations"]["IS_CONTAINED_BY"]
        metadata["destination"]["file"] = {"name": source.name, "path": source.parent.relative_to(fixture.root).as_posix()}
        source.write_bytes(operations.render(yaml.safe_dump(metadata, sort_keys=False).rstrip("\n"), body))
        before = source.read_bytes()
        with bind_selection(resolve_project(fixture.root)):
            result = move_atom_action(fixture.root, fixture._request(source, destination, "PROJECT_CONFIGURATION"),
                                      execute=True, authorized=True)
            metadata = yaml.safe_load(operations.atom_from_path(fixture.root, destination).frontmatter)
        self.assertEqual(fixture.fixture.declarations["PROJECT_CONFIGURATION"]["scope_id"],
                         metadata["context"]["container"]["scope_unit"])
        self.assertEqual({"name": destination.name, "path": destination.parent.relative_to(fixture.root).as_posix()},
                         metadata["destination"]["file"])
        self.assertEqual(before, (fixture.root / result["history"]["prior_revision"]["path"]).read_bytes())


if __name__ == "__main__":
    unittest.main()
