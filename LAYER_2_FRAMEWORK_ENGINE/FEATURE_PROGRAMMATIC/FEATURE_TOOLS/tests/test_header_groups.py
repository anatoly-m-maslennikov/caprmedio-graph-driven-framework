"""Small independent goldens for Header layout compatibility and scalar spans."""

from copy import deepcopy
from pathlib import Path
import sys
import unittest

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from carrier_aliases import carrier_read_view
from header_groups import header_field_paths, header_path, nested_header
from header_yaml import (header_scalar, header_scalar_node, parse_header,
                         remove_header_scalar, replace_header_scalar)


GROUPED = ("identity:\n  atom_id: CA-P-42\n  ref_id: P42\n"
           "context:\n  role: Plan\n  form: Task\n  plan:\n    work_sequence_number: 2\n"
           "state:\n  status: Active # keep\n  version: 3\n  updated_at: old\n"
           "destination:\n  file:\n    name: task.md\n    path: plans/task.md\n"
           "priority: legacy\nunknown: {keep: [1, two]}\n")


class HeaderGroupsTests(unittest.TestCase):
    def test_identity_id_and_legacy_locations_are_read_as_atom_id(self):
        for raw in ({"identity": {"id": "CA-R-42"}},
                    {"identity": {"atom_id": "CA-R-42"}},
                    {"atom_id": "CA-R-42"}):
            with self.subTest(raw=raw):
                before = deepcopy(raw)
                self.assertEqual(carrier_read_view(raw)["atom_id"], "CA-R-42")
                self.assertEqual(raw, before)

    def test_identity_aliases_accept_equal_values_and_reject_type_conflicts(self):
        raw = {"identity": {"id": "CA-R-42", "atom_id": "CA-R-42"},
               "atom_id": "CA-R-42"}
        self.assertEqual(carrier_read_view(raw)["atom_id"], "CA-R-42")
        with self.assertRaises(ValueError):
            carrier_read_view({"identity": {"id": False, "atom_id": 0}})

    def test_identity_id_is_preferred_when_present_but_old_new_keys_stay_old(self):
        new = {"identity": {"id": "CA-R-42"}}
        self.assertEqual(header_field_paths("atom_id", new),
                         (("identity", "id"), ("identity", "atom_id"), ("atom_id",)))
        self.assertEqual(header_path("atom_id", new), ("identity", "id"))
        for name in ("identity.id", "identity.atom_id"):
            with self.subTest(name=name), self.assertRaises(ValueError):
                header_path(name, {"identity": {"id": "CA-R-42", "atom_id": "CA-R-43"}})
        self.assertEqual(header_path("atom_id", {"identity": {"ref_id": "R42"}}),
                         ("identity", "atom_id"))
        self.assertEqual(header_path("atom_id", {"role": "Requirement"}), ("atom_id",))

    def test_new_identity_id_roundtrips_without_reintroducing_old_atom_id(self):
        raw = {"identity": {"id": "CA-R-42", "atom_id": "CA-R-42"}, "role": "Requirement"}
        before = deepcopy(raw)
        result = nested_header(raw)
        self.assertEqual(result["identity"]["id"], "CA-R-42")
        self.assertNotIn("atom_id", result["identity"])
        self.assertNotIn("atom_id", result)
        self.assertEqual(raw, before)
        self.assertEqual(nested_header(result), result)

    def test_nested_semantic_view_leaves_original_mapping_untouched(self):
        raw = yaml.safe_load(GROUPED)
        before = deepcopy(raw)
        view = carrier_read_view(raw)
        self.assertEqual((view["atom_id"], view["version"], view["content_role"], view["type"]),
                         ("CA-P-42", 3, "Plan", "Task"))
        self.assertEqual(view["carrier_destination"], raw["destination"])
        self.assertEqual(raw, before)
        self.assertNotIn("atom_id", raw)
        self.assertEqual(view["priority"], "legacy")

    def test_ordered_authoring_preserves_residue_and_missing_fields(self):
        raw = {"author": "A", "updated_at": "old", "role": "Plan", "atom_id": "CA-P-42",
               "carrier_destination": {"file": {"path": "x", "name": "x.md"}},
               "priority": 5, "work_sequence_number": 2, "autonomous_confidence_threshold": 90,
               "status": "Active", "current_scope_unit": "TOOLS", "subjects": {"active": "Tool"}}
        before = deepcopy(raw)
        result = nested_header(raw)
        self.assertEqual(list(result), ["identity", "context", "state", "destination", "author",
                                        "priority", "current_scope_unit", "subjects"])
        self.assertEqual(list(result["context"]), ["role", "plan"])
        self.assertEqual(list(result["context"]["plan"]), ["work_sequence_number", "ai_agent_confidence_threshold"])
        self.assertEqual(list(result["destination"]["file"]), ["name", "path"])
        self.assertEqual(result["priority"], 5)
        self.assertNotIn("version", result["state"])
        self.assertNotIn("current_scope_unit", result["context"])
        self.assertEqual(nested_header(result), result)
        self.assertEqual(raw, before)

    def test_concern_priority_maps_with_role_or_identity_evidence(self):
        for raw in ({"role": "Concern", "priority": 2}, {"atom_id": "CA-C-42", "priority": 2}):
            self.assertEqual(nested_header(raw)["context"]["concern"], {"priority": 2})
        self.assertEqual(nested_header({"priority": 2}), {"priority": 2})

    def test_equal_mixed_aliases_canonicalize_and_conflicts_are_type_sensitive(self):
        raw = {"identity": {"atom_id": "CA-R-42"}, "atom_id": "CA-R-42",
               "context": {"role": "Requirement", "form": "Rule"},
               "content_role": "Requirement", "type": "Rule"}
        result = nested_header(raw)
        self.assertNotIn("atom_id", result)
        self.assertNotIn("content_role", result)
        for metadata in ({"identity": {"atom_id": "CA-R-42"}, "atom_id": "CA-R-43"},
                         {"state": {"version": 1}, "version": True},
                         {"context": {"role": "Plan"}, "content_role": "Concern"}):
            with self.subTest(metadata=metadata), self.assertRaises(ValueError):
                carrier_read_view(metadata)

    def test_topics_are_read_aliases_without_reauthoring_subject_residue(self):
        raw = {"context": {"topics": {"main_subject": "Node", "dependencies": ["Property"]}}}
        expected = {"active": "Node", "governs": "Node", "passive": ["Property"], "depends_on": ["Property"]}
        self.assertEqual(carrier_read_view(raw)["subjects"], expected)
        self.assertNotIn("subjects", raw)
        mixed = {**raw, "subjects": {"governs": "Node", "depends_on": ["Property"]}}
        self.assertEqual(nested_header(mixed)["subjects"], mixed["subjects"])
        with self.assertRaises(ValueError):
            carrier_read_view({**raw, "subjects": {"active": "Wrong"}})
        for malformed in (None, 4, "bad"):
            with self.subTest(malformed=malformed), self.assertRaises(ValueError):
                carrier_read_view({**raw, "subjects": malformed})
        self.assertEqual(carrier_read_view({"topics": raw["context"]["topics"]})["subjects"], expected)

    def test_container_and_destination_paths_keep_legacy_locations_distinct(self):
        raw = yaml.safe_load(GROUPED)
        self.assertEqual(header_path("carrier_destination.file.name", raw), ("destination", "file", "name"))
        self.assertEqual(header_field_paths("container.scope_unit", raw),
                         (("context", "container", "scope_unit"), ("container", "scope_unit")))
        self.assertEqual(header_path("version", {"version": 1}), ("version",))
        self.assertEqual(header_path("version", {"context": {"role": "Plan"}}), ("state", "version"))


class HeaderYamlTests(unittest.TestCase):
    def test_identity_id_scalar_roundtrip_and_old_missing_key_insertion(self):
        source = "identity:\n  id: CA-R-42\n  ref_id: R42\ncontext:\n  role: Requirement\n"
        self.assertEqual(header_scalar(source, "atom_id"), "CA-R-42")
        changed = replace_header_scalar(source, "atom_id", "CA-R-43")
        self.assertIn("  id: CA-R-43", changed)
        self.assertNotIn("atom_id:", changed)
        self.assertEqual(nested_header(parse_header(changed)), parse_header(changed))

        inserted = replace_header_scalar("identity:\n  ref_id: R42\n", "atom_id", "CA-R-42")
        self.assertIn("  atom_id: CA-R-42", inserted)
        self.assertNotIn("  id:", inserted)

    def test_nested_scalar_and_marks_are_actual_source_spans(self):
        self.assertEqual(header_scalar(GROUPED, "content_role"), "Plan")
        self.assertEqual(header_scalar(GROUPED, "version"), "3")
        self.assertEqual(header_scalar(GROUPED, "carrier_destination.file.path"), "plans/task.md")
        node = header_scalar_node(yaml.compose(GROUPED), "atom_id")
        self.assertEqual(GROUPED[node.start_mark.index:node.end_mark.index], "CA-P-42")
        self.assertIsNone(header_scalar(GROUPED, "label"))
        self.assertIsNone(header_scalar("", "atom_id"))

    def test_replace_retains_comments_unknown_values_and_crlf(self):
        source = GROUPED.replace("\n", "\r\n")
        changed = replace_header_scalar(source, "status", "Resolved")
        self.assertEqual(changed, source.replace("status: Active", "status: Resolved"))
        changed = replace_header_scalar(changed, "version", 4)
        self.assertEqual(header_scalar(changed, "version"), "4")
        self.assertNotIn("\n", changed.replace("\r\n", ""))
        self.assertIn("unknown: {keep: [1, two]}", changed)

    def test_missing_nested_scalar_creates_ordered_group_without_flat_copy(self):
        source = "identity:\n  atom_id: CA-R-42\ncontext:\n  role: Requirement\nunknown: keep"
        changed = replace_header_scalar(source, "version", 1)
        self.assertEqual(changed, "identity:\n  atom_id: CA-R-42\ncontext:\n  role: Requirement\nstate:\n  version: 1\nunknown: keep")
        changed = replace_header_scalar(changed, "status", "Active")
        self.assertIn("state:\n  status: Active\n  version: 1\n", changed)
        self.assertNotIn("\nversion:", changed)
        changed = replace_header_scalar(changed, "updated_at", "2026-11-06 12:00:00 +0000")
        self.assertIsInstance(parse_header(changed)["state"]["updated_at"], str)

    def test_legacy_flat_edits_stay_flat(self):
        source = "atom_id: CA-P-42\nversion: 2\nupdated_at: old\nunknown: keep"
        changed = replace_header_scalar(source, "version", 3)
        self.assertEqual(changed, source.replace("version: 2", "version: 3"))
        self.assertEqual(replace_header_scalar("", "version", 1), "version: 1")
        self.assertNotIn("state:", replace_header_scalar(source, "status", "Active"))

    def test_flow_header_insert_replace_remove_and_empty_parent_pruning(self):
        source = "identity: {atom_id: CA-R-42}\nstate: {version: 2}\nunknown: keep"
        changed = replace_header_scalar(source, "status", "Active")
        self.assertEqual(header_scalar(changed, "status"), "Active")
        changed = remove_header_scalar(changed, "version")
        self.assertIsNone(header_scalar(changed, "version"))
        changed = remove_header_scalar(changed, "status")
        self.assertNotIn("state:", changed)
        self.assertIn("unknown: keep", changed)
        self.assertEqual(remove_header_scalar("identity:\n  atom_id: CA-R-42\nother: keep", "atom_id"), "other: keep")

    def test_mixed_equal_replacements_and_removals_stay_consistent(self):
        source = "identity:\n  atom_id: CA-R-42\natom_id: CA-R-42\nunknown: keep"
        changed = replace_header_scalar(source, "atom_id", "CA-R-43")
        self.assertEqual(header_scalar(changed, "atom_id"), "CA-R-43")
        self.assertEqual(remove_header_scalar(changed, "atom_id"), "unknown: keep")

    def test_multiline_scalar_edits_preserve_next_nested_sibling(self):
        source = "state:\n  status: |-\n    Active\n  version: 2\nunknown: keep"
        changed = replace_header_scalar(source, "status", "Done")
        self.assertEqual(changed, "state:\n  status: Done\n  version: 2\nunknown: keep")
        self.assertEqual(remove_header_scalar(source, "status"), "state:\n  version: 2\nunknown: keep")

    def test_duplicate_merge_alias_mapping_and_conflict_refusals(self):
        sources = ("state: {version: 1, version: 1}", "identity: {atom_id: X}\natom_id: Y",
                   "state: {version: 1}\nversion: true", "x: &x [one]\ny: *x", "x: {<<: {a: 1}}",
                   "state: wrong", "1: bad", "!!python/object:thing {}")
        for source in sources:
            with self.subTest(source=source), self.assertRaises(ValueError):
                header_scalar(source, "version")
        with self.assertRaises(ValueError):
            header_scalar("context: {container: {atom: CA-R-42}}", "container")


if __name__ == "__main__":
    unittest.main()
