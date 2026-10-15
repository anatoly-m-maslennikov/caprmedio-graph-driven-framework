"""Independent P2298 checks: supplied bytes only, no publication authority."""

from __future__ import annotations

import copy
import hashlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_property_carrier import prepare_property_carrier
from connector_property_parse import PropertyEditError


FIELDS = {"Status": ("status",), "Dependencies": ("subjects", "depends_on"),
          "Optional": ("optional",), "Type": ("type",), "Identity": ("atom_id",)}
BODY = "# Summary\n\nKeep this body, including # text and trailing spaces.  \n"


def carrier(subjects=None, *, newline="\n"):
    subjects = subjects or (
        "subjects:\n  governs: Tool # untouched\n  depends_on:\n"
        "    - Atom # first\n    - Workflow # second\n"
    )
    return (
        "---\natom_id: CA-R-842\ntype: Requirement # unchanged type\n"
        "status: Active # status comment\nversion: 7\nupdated_at: exact-old-time\n"
        + subjects + 'unrelated: ["# literal", 17, null] # unrelated comment\n'
        + "---\n" + BODY
    ).replace("\n", newline).encode("utf-8")


def validate(metadata, body):
    if metadata.get("atom_id") != "CA-R-842" or metadata.get("type") != "Requirement":
        raise PropertyEditError("schema_invalid", "Complete identity/type changed.")
    if metadata.get("status") not in {"Active", "Archived"}:
        raise PropertyEditError("schema_invalid", "Complete Status is invalid or missing.")
    values = metadata["subjects"]["depends_on"]
    if type(values) is not list or any(type(value) is not str for value in values):
        raise PropertyEditError("schema_invalid", "Complete dependency type is invalid.")
    if len(set(values)) != len(values):
        raise PropertyEditError("schema_invalid", "Complete dependency uniqueness is invalid.")
    if body not in {BODY, BODY.replace("\n", "\r\n")}:
        raise PropertyEditError("schema_invalid", "Complete body changed.")


def prepare(raw, edits, *, validator=validate, expected=None):
    return prepare_property_carrier(
        raw, edits, expected_sha256=expected or hashlib.sha256(raw).hexdigest(),
        field_paths=FIELDS, list_fields={"Dependencies", "Optional"},
        list_entry_edit=lambda edit: edit["field"] == "Dependencies"
        and edit["operation"] != "replace_set", validate_final=validator,
    )


class IndependentPropertyCarrierTests(unittest.TestCase):
    def assert_refused(self, raw, edits, code=None, **kwargs):
        before, requested = raw, copy.deepcopy(edits)
        with self.assertRaises(PropertyEditError) as raised:
            prepare(raw, edits, **kwargs)
        if code is not None:
            self.assertEqual(raised.exception.code, code)
        self.assertEqual(raw, before)
        self.assertEqual(edits, requested)

    def test_scalar_lf_crlf_preserves_all_other_bytes_and_metadata(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(newline=newline)
                output = prepare(raw, [{"field": "Status", "operation": "replace",
                                        "old": "Active", "new": "Archived"}])
                self.assertEqual(output, raw.replace(b"status: Active", b'status: "Archived"'))
                self.assertIn(("version: 7" + newline + "updated_at: exact-old-time").encode(), output)

    def test_unique_entry_add_replace_remove_preserves_unrelated_bytes(self):
        raw = carrier()
        replaced = prepare(raw, [{"field": "Dependencies", "operation": "replace",
                                  "old": "Workflow", "new": "Property"}])
        self.assertEqual(replaced, raw.replace(b"- Workflow", b'- "Property"'))
        added = prepare(raw, [{"field": "Dependencies", "operation": "add", "value": "Action"}])
        self.assertEqual(added, raw.replace(b"unrelated:", b'    - "Action"\nunrelated:'))
        removed = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
        self.assertEqual(removed, raw.replace(b"    - Atom # first", b"    # first"))

    def test_full_set_keeps_comments_and_exact_unrelated_frontier(self):
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(newline=newline)
                output = prepare(raw, [{"field": "Dependencies", "operation": "replace_set",
                                        "old": ["Atom", "Workflow"], "new": ["Action"]}])
                old = "    - Atom # first\n    - Workflow # second\n".replace("\n", newline).encode()
                new = '    ["Action"]\n    # first\n    # second\n'.replace("\n", newline).encode()
                self.assertEqual(output, raw.replace(old, new))

    def test_optional_whole_property_add_remove_preserves_body_comments_and_order(self):
        raw = carrier()
        added = prepare(raw, [{"field": "Optional", "operation": "add", "value": ["X", "Y"]}])
        self.assertEqual(added, raw.replace(b"\n---\n# Summary", b'\n"optional": ["X", "Y"]\n---\n# Summary'))
        removed = prepare(added, [{"field": "Optional", "operation": "remove", "old": ["X", "Y"]}])
        self.assertEqual(removed, raw.replace(b"\n---\n# Summary", b"\n\n---\n# Summary"))

    def test_no_ops_return_exact_original_bytes_with_complete_validation(self):
        raw = carrier(newline="\r\n")
        calls = []
        def validator(metadata, body):
            calls.append((copy.deepcopy(metadata), body))
            validate(metadata, body)
        for edits in ([], [{"field": "Status", "operation": "replace", "old": "Active", "new": "Active"}],
                      [{"field": "Dependencies", "operation": "add", "value": "Atom"}],
                      [{"field": "Dependencies", "operation": "replace_set", "old": ["Atom", "Workflow"],
                        "new": ["Atom", "Workflow"]}]):
            self.assertIs(prepare(raw, edits, validator=validator), raw)
        self.assertEqual(len(calls), 4)
        self.assertTrue(all(body == BODY.replace("\n", "\r\n") for _, body in calls))

    def test_complete_validator_observes_final_atom_and_exact_body_but_cannot_mutate_result(self):
        raw, calls = carrier(), []
        def validator(metadata, body):
            validate(metadata, body)
            calls.append((copy.deepcopy(metadata), body))
            metadata["status"] = "NOT-A-VALID-STATUS"
            metadata["unrelated"][0] = "tampered"
        output = prepare(raw, [{"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"}],
                         validator=validator)
        self.assertEqual(output, raw.replace(b"status: Active", b'status: "Archived"'))
        self.assertEqual(len(calls), 2)
        self.assertTrue(all(metadata["status"] == "Archived" and body == BODY for metadata, body in calls))

    def test_complete_validator_non_none_or_final_refusal_never_accepts(self):
        raw = carrier()
        edits = [{"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"}]
        for verdict in (False, True, "permission", [], {}, 1):
            for final_only in (False, True):
                with self.subTest(verdict=verdict, final_only=final_only):
                    calls = []
                    def validator(metadata, body):
                        calls.append(None)
                        return None if final_only and len(calls) == 1 else verdict
                    self.assert_refused(raw, edits, "schema_invalid", validator=validator)
                    self.assertEqual(len(calls), 2 if final_only else 1)
        self.assert_refused(raw, [{"field": "Status", "operation": "remove", "old": "Active"}], "schema_invalid")
        self.assert_refused(raw, [{"field": "Status", "operation": "replace", "old": "Active", "new": "Invalid"}], "schema_invalid")

    def test_ambiguous_stale_or_unbound_requests_are_pure_refusals(self):
        raw = carrier()
        self.assert_refused(raw, [], "stale_state", expected="0" * 64)
        self.assert_refused(raw.replace(b"status: Active", b"status: Active\nstatus: Active"), [], "schema_invalid")
        self.assert_refused(raw.replace(b"- Workflow", b"- Atom"),
                            [{"field": "Dependencies", "operation": "remove", "value": "Atom"}], "target_ambiguous")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "replace", "old": "Absent", "new": "Action"}], "stale_state")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "replace_set", "old": ["Workflow", "Atom"], "new": []}], "stale_state")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "replace", "old": "Atom", "new": "Action", "index": 0}], "input_invalid")
        self.assert_refused(raw, [{"field": "Unknown", "operation": "add", "value": "x"}], "schema_invalid")
        aliases = carrier("subjects:\n  governs: Tool\n  depends_on: &values [Atom, Workflow]\nother: *values\n")
        self.assert_refused(aliases, [], "schema_invalid")

    def test_identity_type_and_duplicate_dependency_changes_are_refused(self):
        raw = carrier()
        for field, old, new in (("Identity", "CA-R-842", "CA-R-843"), ("Type", "Requirement", "Method")):
            self.assert_refused(raw, [{"field": field, "operation": "replace", "old": old, "new": new}], "schema_invalid")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "replace", "old": "Workflow", "new": "Atom"}], "schema_invalid")

    def test_transform_has_no_file_io(self):
        raw = carrier()
        with patch("builtins.open", side_effect=AssertionError("Pure transform may not open files")), \
             patch.object(Path, "read_bytes", side_effect=AssertionError("Pure transform may not read")), \
             patch.object(Path, "write_bytes", side_effect=AssertionError("Pure transform may not write")):
            self.assertEqual(prepare(raw, [{"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"}]),
                             raw.replace(b"status: Active", b'status: "Archived"'))
            self.assert_refused(raw, [{"field": "Status", "operation": "replace", "old": "Absent", "new": "Archived"}], "stale_state")

    def test_block_list_add_before_next_nested_key_preserves_exact_bytes(self):
        subjects = "subjects:\n  depends_on:\n    - Atom # first\n    - Workflow # second\n  governs: Tool # untouched\n"
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(subjects, newline=newline)
                output = prepare(raw, [{"field": "Dependencies", "operation": "add", "value": "Action"}])
                self.assertEqual(output, raw.replace(b"  governs:", ('    - "Action"' + newline + "  governs:").encode()))

    def test_block_full_set_before_next_nested_key_preserves_exact_bytes(self):
        subjects = "subjects:\n  depends_on:\n    - Atom # first\n    - Workflow # second\n  governs: Tool # untouched\n"
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(subjects, newline=newline)
                output = prepare(raw, [{"field": "Dependencies", "operation": "replace_set",
                                        "old": ["Atom", "Workflow"], "new": ["Action"]}])
                old = "    - Atom # first\n    - Workflow # second\n".replace("\n", newline).encode()
                new = '    ["Action"]\n    # first\n    # second\n'.replace("\n", newline).encode()
                self.assertEqual(output, raw.replace(old, new))

    def test_flow_list_with_trailing_comma_add_preserves_exact_other_bytes(self):
        raw = carrier("subjects:\n  governs: Tool # untouched\n  depends_on: [Atom, Workflow,] # list comment\n")
        output = prepare(raw, [{"field": "Dependencies", "operation": "add", "value": "Action"}])
        self.assertEqual(output, raw.replace(b"[Atom, Workflow,]", b'[Atom, Workflow, "Action"]'))

    def test_flow_mapping_optional_property_removal_is_not_ambiguous(self):
        raw = carrier().replace(b"unrelated:", b'extras: {optional: [X], retained: "byte-exact"} # extra\nunrelated:')
        output = prepare_property_carrier(
            raw, [{"field": "Optional", "operation": "remove", "old": ["X"]}],
            expected_sha256=hashlib.sha256(raw).hexdigest(),
            field_paths={"Optional": ("extras", "optional")}, list_fields={"Optional"},
            list_entry_edit=lambda edit: False, validate_final=validate,
        )
        self.assertEqual(output, raw.replace(b'{optional: [X], retained: "byte-exact"}',
                                             b'{retained: "byte-exact"}'))

    def test_unique_multiline_block_value_removal_preserves_exact_other_bytes(self):
        subjects = "subjects:\n  governs: Tool # untouched\n  depends_on:\n    - >-\n      Atom\n    - Workflow # second\n"
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(subjects, newline=newline)
                output = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
                self.assertEqual(output, raw.replace("    - >-\n      Atom\n".replace("\n", newline).encode(), b""))

    def test_flow_map_first_middle_last_sole_and_trailing_comma_removal_exact_bytes(self):
        cases = (
            ('{optional: [X], left: "keep", right: \'# literal\'}',
             ('{left: "keep", right: \'# literal\'}', '{ left: "keep", right: \'# literal\'}')),
            ('{left: "keep", optional: [X], right: \'# literal\'}',
             ('{left: "keep", right: \'# literal\'}', '{left: "keep",  right: \'# literal\'}')),
            ('{left: "keep", right: \'# literal\', optional: [X]}',
             ('{left: "keep", right: \'# literal\'}', '{left: "keep", right: \'# literal\' }')),
            ('{optional: [X]}', ('{}',)),
            ('{left: "keep", optional: [X],}',
             ('{left: "keep",}', '{left: "keep", }', '{left: "keep"}')),
            ('{optional: [X],}', ('{}',)),
        )
        for source_map, expected_maps in cases:
            for newline in ("\n", "\r\n"):
                with self.subTest(source_map=source_map, newline=newline):
                    raw = carrier(newline=newline).replace(b"unrelated:", ("extras: " + source_map + " # outside" + newline + "unrelated:").encode())
                    output = prepare_property_carrier(
                        raw, [{"field": "Optional", "operation": "remove", "old": ["X"]}],
                        expected_sha256=hashlib.sha256(raw).hexdigest(),
                        field_paths={"Optional": ("extras", "optional")}, list_fields={"Optional"},
                        list_entry_edit=lambda edit: False, validate_final=validate,
                    )
                    # Separator-adjacent whitespace belongs to the removed entry,
                    # not a formatting rule for the untouched field lexemes.
                    self.assertIn(output, [raw.replace(source_map.encode(), value.encode()) for value in expected_maps])

    def test_flow_map_add_empty_or_trailing_comma_and_replace_set_exact_bytes(self):
        cases = (
            ('{}', {"operation": "add", "value": ["X"]}, '{"optional": ["X"]}'),
            ('{left: "keep",}', {"operation": "add", "value": ["X"]}, '{left: "keep", "optional": ["X"]}'),
            ('{left: "keep", optional: [X, Y],}',
             {"operation": "replace_set", "old": ["X", "Y"], "new": ["Z"]},
             '{left: "keep", optional: ["Z"],}'),
        )
        for source_map, edit, expected_map in cases:
            for newline in ("\n", "\r\n"):
                with self.subTest(source_map=source_map, newline=newline):
                    raw = carrier(newline=newline).replace(b"unrelated:", ("extras: " + source_map + " # outside" + newline + "unrelated:").encode())
                    output = prepare_property_carrier(
                        raw, [dict(edit, field="Optional")], expected_sha256=hashlib.sha256(raw).hexdigest(),
                        field_paths={"Optional": ("extras", "optional")}, list_fields={"Optional"},
                        list_entry_edit=lambda value: False, validate_final=validate,
                    )
                    self.assertEqual(output, raw.replace(source_map.encode(), expected_map.encode()))

    def test_flow_map_removal_retains_inside_and_outside_comments(self):
        source_map = 'extras: {left: "keep",\n  optional: [X], # selected comment\n  right: \'# literal\'} # outside\n'
        expected_map = 'extras: {left: "keep",\n  # selected comment\n  right: \'# literal\'} # outside\n'
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                source = source_map.replace("\n", newline).encode()
                raw = carrier(newline=newline).replace(b"unrelated:", source + b"unrelated:")
                output = prepare_property_carrier(
                    raw, [{"field": "Optional", "operation": "remove", "old": ["X"]}],
                    expected_sha256=hashlib.sha256(raw).hexdigest(),
                    field_paths={"Optional": ("extras", "optional")}, list_fields={"Optional"},
                    list_entry_edit=lambda edit: False, validate_final=validate,
                )
                self.assertIn(output, [raw.replace(source, value.replace("\n", newline).encode())
                                      for value in (expected_map, expected_map.replace("  # selected", "   # selected"))])

    def test_folded_literal_first_middle_last_sole_removal_retains_comments_exact_bytes(self):
        for style in (">-", "|-"):
            for before, after in (("", "    - Workflow # other\n"),
                                  ("    - Workflow # other\n", "    - Property # later\n"),
                                  ("    - Workflow # other\n", ""), ("", "")):
                for newline in ("\n", "\r\n"):
                    with self.subTest(style=style, before=before, after=after, newline=newline):
                        selected = f"    - {style} # selected header\n      Atom\n"
                        subjects = "subjects:\n  governs: Tool # untouched\n  depends_on:\n" + before + selected + after
                        raw = carrier(subjects, newline=newline)
                        output = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
                        replacement = ("    []\n" if not before and not after else "") + "    # selected header\n"
                        self.assertEqual(output, raw.replace(selected.replace("\n", newline).encode(), replacement.replace("\n", newline).encode()))

    def test_literal_hash_payload_is_value_not_comment_and_real_comments_survive(self):
        selected = "    - |- # selected header\n      Atom\n      # scalar payload\n"
        subjects = "subjects:\n  governs: Tool # untouched\n  depends_on:\n    # before\n" + selected + "    # after\n    - Workflow # other\n"
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(subjects, newline=newline)
                output = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom\n# scalar payload"}])
                self.assertEqual(output, raw.replace(selected.replace("\n", newline).encode(), ("    # selected header" + newline).encode()))

    def test_multiline_duplicate_missing_value_and_required_final_list_refusals(self):
        raw = carrier("subjects:\n  governs: Tool # untouched\n  depends_on:\n    - >-\n      Atom\n    - Atom\n")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}], "target_ambiguous")
        raw = carrier("subjects:\n  governs: Tool # untouched\n  depends_on:\n    - >-\n      Atom\n")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "remove", "value": "Absent"}], "stale_state")
        def required_nonempty(metadata, body):
            validate(metadata, body)
            if not metadata["subjects"]["depends_on"]:
                raise PropertyEditError("schema_invalid", "The bound complete schema requires a dependency.")
        self.assert_refused(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}], "schema_invalid", validator=required_nonempty)

    def test_unique_quoted_and_plain_multiline_scalar_removal_preserves_unrelated_bytes(self):
        cases = (
            ('    - "At\\\n      om" # selected trailing\n', "Atom"),
            ("    - 'Atom\n      Workflow' # selected trailing\n", "Atom Workflow"),
            ("    - Atom\n      Workflow # selected trailing\n", "Atom Workflow"),
        )
        for selected, value in cases:
            for newline in ("\n", "\r\n"):
                with self.subTest(selected=selected, newline=newline):
                    subjects = "subjects:\n  governs: Tool # untouched\n  depends_on:\n" + selected + "    - Property # retained\n"
                    raw = carrier(subjects, newline=newline)
                    output = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": value}])
                    # Either deleted-entry or original closing-line indentation
                    # preserves the genuine comment; neither is a style policy.
                    self.assertIn(output, [raw.replace(selected.replace("\n", newline).encode(),
                                                       (indent + "# selected trailing" + newline).encode())
                                           for indent in ("    ", "      ")])

    def test_privately_schema_allowed_multiline_mapping_and_list_entry_removal(self):
        cases = (
            ('    - name: "X" # selected comment\n      enabled: true\n', {"name": "X", "enabled": True}),
            ('    - - "X" # selected comment\n      - 2\n', ["X", 2]),
            ('    - {name: "X", # selected comment\n       enabled: true}\n', {"name": "X", "enabled": True}),
            ('    - ["X", # selected comment\n       2]\n', ["X", 2]),
        )
        for selected, value in cases:
            for newline in ("\n", "\r\n"):
                with self.subTest(selected=selected, newline=newline):
                    record_source = "records:\n" + selected + "    - retained # unrelated entry\n"
                    raw = carrier(newline=newline).replace(b"unrelated:", record_source.replace("\n", newline).encode() + b"unrelated:")
                    def validate_records(metadata, body):
                        validate(metadata, body)
                        if metadata["records"] != ["retained"]:
                            raise PropertyEditError("schema_invalid", "The supplied complete Records schema rejects this result.")
                    output = prepare_property_carrier(
                        raw, [{"field": "Records", "operation": "remove", "value": value}],
                        expected_sha256=hashlib.sha256(raw).hexdigest(),
                        field_paths={"Records": ("records",)}, list_fields={"Records"},
                        list_entry_edit=lambda edit: True, validate_final=validate_records,
                    )
                    expected = raw.replace(selected.replace("\n", newline).encode(), ("    # selected comment" + newline).encode())
                    self.assertEqual(output, expected)

    def test_literal_hash_then_real_inline_comment_survives_remove_and_full_set(self):
        subjects = 'subjects:\n  governs: Tool # untouched\n  depends_on:\n    - "Atom#literal" # keep\n    - Workflow # second\n'
        for newline in ("\n", "\r\n"):
            for operation in ("remove", "replace_set"):
                with self.subTest(newline=newline, operation=operation):
                    raw = carrier(subjects, newline=newline)
                    if operation == "remove":
                        edit = {"field": "Dependencies", "operation": "remove", "value": "Atom#literal"}
                        old = '    - "Atom#literal" # keep\n'
                        new = "    # keep\n"
                    else:
                        edit = {"field": "Dependencies", "operation": "replace_set",
                                "old": ["Atom#literal", "Workflow"], "new": ["Action"]}
                        old = '    - "Atom#literal" # keep\n    - Workflow # second\n'
                        new = '    ["Action"]\n    # keep\n    # second\n'
                    output = prepare(raw, [edit])
                    self.assertEqual(output, raw.replace(old.replace("\n", newline).encode(), new.replace("\n", newline).encode()))

    def test_explicit_flow_key_first_and_sole_removal_does_not_transfer_key_marker(self):
        for source_map, expected_map in (("{? optional: [X], retained: kept}", "{retained: kept}"),
                                         ("{? optional: [X]}", "{}")):
            for newline in ("\n", "\r\n"):
                with self.subTest(source_map=source_map, newline=newline):
                    raw = carrier(newline=newline).replace(b"unrelated:", ("extras: " + source_map + " # outside" + newline + "unrelated:").encode())
                    output = prepare_property_carrier(
                        raw, [{"field": "Optional", "operation": "remove", "old": ["X"]}],
                        expected_sha256=hashlib.sha256(raw).hexdigest(),
                        field_paths={"Optional": ("extras", "optional")}, list_fields={"Optional"},
                        list_entry_edit=lambda edit: False, validate_final=validate,
                    )
                    self.assertEqual(output, raw.replace(source_map.encode(), expected_map.encode()))

    def test_separate_line_block_entry_indicator_removal_preserves_unrelated_bytes(self):
        subjects = "subjects:\n  governs: Tool # untouched\n  depends_on:\n    -\n      Atom\n    - Workflow # retained\n"
        for newline in ("\n", "\r\n"):
            with self.subTest(newline=newline):
                raw = carrier(subjects, newline=newline)
                output = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
                self.assertEqual(output, raw.replace("    -\n      Atom\n".replace("\n", newline).encode(), b""))

    def test_separate_line_indicator_value_gap_comments_and_retained_entry_survive(self):
        selected = "    - # indicator comment\n      # gap comment\n      Atom # value comment\n"
        for before, after in (("", "    - Workflow # retained\n"),
                              ("    - Workflow # retained\n", "    - Property # later\n"),
                              ("    - Workflow # retained\n", ""), ("", "")):
            for newline in ("\n", "\r\n"):
                with self.subTest(before=before, after=after, newline=newline):
                    subjects = "subjects:\n  governs: Tool # untouched\n  depends_on:\n" + before + selected + after
                    raw = carrier(subjects, newline=newline)
                    output = prepare(raw, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
                    expected = []
                    for gap_indent in ("    ", "      "):
                        for value_indent in ("    ", "      "):
                            comments = ("    []\n" if not before and not after else "") + "    # indicator comment\n" + gap_indent + "# gap comment\n" + value_indent + "# value comment\n"
                            expected.append(raw.replace(selected.replace("\n", newline).encode(), comments.replace("\n", newline).encode()))
                    self.assertIn(output, expected)


if __name__ == "__main__":
    unittest.main()
