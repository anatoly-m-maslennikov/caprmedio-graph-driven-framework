from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_property_parse import PropertyEditError, apply_property_edits


FIELDS = {
    "Status": ("properties", "status"), "Optional": ("properties", "optional"),
    "Type": ("properties", "type"), "Summary": ("summary",),
    "Atom ID": ("properties", "atom_id"), "Version": ("properties", "version"),
    "Updated At": ("properties", "updated_at"),
    "Dependencies": ("properties", "subjects", "depends_on"),
    "Numbers": ("properties", "numbers"),
}


def atom():
    return {
        "properties": {"atom_id": "CA-R-42", "type": "Requirement", "status": "Active",
                       "version": 3, "updated_at": "old time", "numbers": [1, 2],
                       "subjects": {"governs": "Tool", "depends_on": ["Atom", "Workflow"]}},
        "summary": "Keep this exact Summary", "body": "Unrelated body\r\nwith whitespace.  ",
        "other": {"unknown": [True, None]},
    }


def validate(value):
    if value["properties"].get("status") not in {"Active", "Archived"}:
        raise PropertyEditError("schema_invalid", "Status is required and has a fixed membership.")


def apply(value, edits, validator=validate):
    return apply_property_edits(value, edits, field_paths=FIELDS,
                                list_fields={"Dependencies", "Numbers"},
                                list_entry_edit=lambda edit: edit["field"] in {"Dependencies", "Numbers"}
                                and edit.get("operation") != "replace_set", validate_final=validator)


class PropertyEditTests(unittest.TestCase):
    def test_absent_optional_list_property_add_and_whole_property_remove(self):
        source = atom()
        del source["properties"]["numbers"]
        kwargs = {"field_paths": FIELDS, "list_fields": {"Numbers"},
                  "list_entry_edit": lambda edit: False, "validate_final": validate}
        created = apply_property_edits(source, [{"field": "Numbers", "operation": "add", "value": [3, 4]}], **kwargs)
        self.assertEqual(created["properties"]["numbers"], [3, 4])
        self.assertEqual(created["properties"]["version"], 3)
        removed = apply_property_edits(created, [{"field": "Numbers", "operation": "remove", "old": [3, 4]}], **kwargs)
        self.assertEqual(removed, source)
        with self.assertRaises(PropertyEditError):
            apply_property_edits(source, [{"field": "Numbers", "operation": "add", "value": 3}], **kwargs)

    def test_scalar_add_replace_remove_and_explicit_metadata_only(self):
        source = atom()
        before = copy.deepcopy(source)
        proposed = apply(source, [
            {"field": "Optional", "operation": "add", "value": "new"},
            {"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"},
            {"field": "Version", "operation": "replace", "old": 3, "new": 4},
            {"field": "Updated At", "operation": "replace", "old": "old time", "new": "supplied time"},
        ])
        self.assertEqual(proposed["properties"]["status"], "Archived")
        self.assertEqual(proposed["properties"]["version"], 4)
        self.assertEqual(proposed["body"], source["body"])
        self.assertEqual(proposed["other"], source["other"])
        self.assertEqual(source, before)
        removed = apply(proposed, [{"field": "Optional", "operation": "remove", "old": "new"}])
        self.assertNotIn("optional", removed["properties"])

    def test_list_add_value_replace_remove_and_full_set_preserve_order(self):
        source = atom()
        proposed = apply(source, [
            {"field": "Dependencies", "operation": "add", "value": "Property"},
            {"field": "Dependencies", "operation": "replace", "old": "Workflow", "new": "Action"},
            {"field": "Dependencies", "operation": "remove", "value": "Atom"},
        ])
        self.assertEqual(proposed["properties"]["subjects"]["depends_on"], ["Action", "Property"])
        full = apply(proposed, [{"field": "Dependencies", "operation": "replace_set",
                                 "old": ["Action", "Property"], "new": ["Property", "Action"]}])
        self.assertEqual(full["properties"]["subjects"]["depends_on"], ["Property", "Action"])

    def test_no_op_preserves_all_data_and_does_not_invent_version_or_time(self):
        source = atom()
        edits = [
            {"field": "Status", "operation": "replace", "old": "Active", "new": "Active"},
            {"field": "Dependencies", "operation": "add", "value": "Atom"},
            {"field": "Dependencies", "operation": "replace_set",
             "old": ["Atom", "Workflow"], "new": ["Atom", "Workflow"]},
            {"field": "Type", "operation": "replace", "old": "Requirement", "new": "Requirement"},
        ]
        self.assertEqual(apply(source, edits), source)
        changed = apply(source, [{"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"}])
        self.assertEqual(changed["properties"]["version"], 3)
        self.assertEqual(changed["properties"]["updated_at"], "old time")

    def test_missing_ambiguous_and_stale_current_values(self):
        for values, old, code in [(["Atom"], "Workflow", "stale_state"),
                                  (["Atom", "Atom"], "Atom", "target_ambiguous")]:
            for operation in ("replace", "remove"):
                with self.subTest(values=values, operation=operation):
                    source = atom()
                    source["properties"]["subjects"]["depends_on"] = values
                    edit = {"field": "Dependencies", "operation": operation}
                    edit.update({"old": old, "new": "Tool"} if operation == "replace" else {"value": old})
                    with self.assertRaises(PropertyEditError) as raised:
                        apply(source, [edit])
                    self.assertEqual(raised.exception.code, code)
        for edit in [
            {"field": "Status", "operation": "replace", "old": "Archived", "new": "Active"},
            {"field": "Dependencies", "operation": "replace_set", "old": ["Workflow", "Atom"], "new": []},
            {"field": "Optional", "operation": "remove", "old": None},
        ]:
            with self.assertRaises(PropertyEditError) as raised:
                apply(atom(), [edit])
            self.assertEqual(raised.exception.code, "stale_state")

    def test_caller_index_unknown_fields_and_bad_operations_fail(self):
        cases = [
            {"field": "Dependencies", "operation": "replace", "old": "Atom", "new": "Tool", "index": 0},
            {"field": "Dependencies", "operation": "replace", "index": 0, "new": "Tool"},
            {"field": "Unknown", "operation": "add", "value": "x"},
            {"field": "Status", "operation": "delete"},
            {"field": "Status", "operation": "add", "value": "Active", "extra": True},
        ]
        for edit in cases:
            with self.subTest(edit=edit), self.assertRaises(PropertyEditError):
                apply(atom(), [edit])

    def test_summary_type_identity_changes_require_replacement(self):
        for field, old, new in [("Summary", "Keep this exact Summary", "Worded differently"),
                                ("Type", "Requirement", "Method"), ("Atom ID", "CA-R-42", "CA-R-43")]:
            with self.subTest(field=field), self.assertRaises(PropertyEditError) as raised:
                apply(atom(), [{"field": field, "operation": "replace", "old": old, "new": new}])
            self.assertEqual(raised.exception.code, "schema_invalid")

    def test_complete_validation_and_subject_duplicates_fail_without_mutating_input(self):
        source = atom()
        before = copy.deepcopy(source)
        for edit in [
            {"field": "Status", "operation": "remove", "old": "Active"},
            {"field": "Status", "operation": "replace", "old": "Active", "new": "Invalid"},
            {"field": "Dependencies", "operation": "replace", "old": "Workflow", "new": "Atom"},
            {"field": "Dependencies", "operation": "replace_set", "old": ["Atom", "Workflow"], "new": ["Atom", "Atom"]},
        ]:
            with self.subTest(edit=edit), self.assertRaises(PropertyEditError):
                apply(source, [edit])
            self.assertEqual(source, before)

    def test_exact_values_distinguish_booleans_integers_and_floats(self):
        for old in (True, 1.0):
            with self.subTest(old=old), self.assertRaises(PropertyEditError):
                apply(atom(), [{"field": "Numbers", "operation": "replace", "old": old, "new": 4}])
        proposed = apply(atom(), [{"field": "Numbers", "operation": "replace", "old": 1, "new": 4}])
        self.assertEqual(proposed["properties"]["numbers"], [4, 2])

    def test_validator_cannot_mutate_returned_result(self):
        def malicious(value):
            value["properties"]["version"] = 999
        self.assertEqual(apply(atom(), [], malicious), atom())

    def test_validator_non_none_return_refuses_invalid_proposal(self):
        for verdict in (False, True, "approved", 1, [], {}):
            with self.subTest(verdict=verdict), self.assertRaises(PropertyEditError) as error:
                apply(atom(), [{"field": "Status", "operation": "replace", "old": "Active", "new": "INVALID"}],
                      lambda value: verdict)
            self.assertEqual(error.exception.code, "schema_invalid")


if __name__ == "__main__":
    unittest.main()
