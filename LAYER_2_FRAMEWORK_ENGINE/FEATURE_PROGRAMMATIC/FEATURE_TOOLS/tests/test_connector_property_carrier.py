from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from connector_property_carrier import prepare_property_carrier
from connector_property_parse import PropertyEditError
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier


SOURCE = (
    "---\r\natom_id: CA-R-42\r\ntype: Requirement # keep type\r\n"
    "status: Active # keep status comment\r\nversion: 3\r\nupdated_at: old-time\r\n"
    "subjects:\r\n  governs: Tool\r\n  depends_on:\r\n"
    "    - Atom # first\r\n    # between\r\n    - Workflow # second\r\n"
    "unrelated: [\"# this is a value\", 3]\r\n---\r\n"
    "# Summary\r\n\r\nExact body.  \r\n"
).encode()
FIELDS = {"Status": ("status",), "Version": ("version",), "Type": ("type",),
          "Optional": ("optional",), "Dependencies": ("subjects", "depends_on")}


def validate(metadata, body):
    if metadata.get("status") not in {"Active", "Archived"}:
        raise PropertyEditError("schema_invalid", "Invalid complete Status.")
    if len(set(metadata["subjects"]["depends_on"])) != len(metadata["subjects"]["depends_on"]):
        raise PropertyEditError("schema_invalid", "Duplicate dependencies.")


def prepare(source, edits, *, entry=True, expected=None):
    return prepare_property_carrier(
        source, edits, expected_sha256=expected or hashlib.sha256(source).hexdigest(),
        field_paths=FIELDS, list_fields={"Dependencies", "Optional"},
        list_entry_edit=lambda edit: entry and edit["field"] == "Dependencies"
        and edit["operation"] != "replace_set", validate_final=validate,
    )


class PropertyCarrierTests(unittest.TestCase):
    def test_validator_false_and_stateful_final_refusal_are_rejected(self):
        edit = {"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"}
        for final_only in (False, True):
            calls = []
            def verdict(metadata, body):
                calls.append((metadata, body))
                return None if final_only and len(calls) == 1 else False
            with self.subTest(final_only=final_only), self.assertRaises(PropertyEditError) as error:
                prepare_property_carrier(
                    SOURCE, [edit], expected_sha256=hashlib.sha256(SOURCE).hexdigest(),
                    field_paths=FIELDS, list_fields={"Dependencies", "Optional"},
                    list_entry_edit=lambda value: False, validate_final=verdict,
                )
            self.assertEqual(error.exception.code, "schema_invalid")
            self.assertEqual(len(calls), 2 if final_only else 1)

    def test_scalar_and_unique_entry_replacement_preserve_every_other_byte(self):
        output = prepare(SOURCE, [
            {"field": "Status", "operation": "replace", "old": "Active", "new": "Archived"},
            {"field": "Dependencies", "operation": "replace", "old": "Workflow", "new": "Property"},
        ])
        expected = SOURCE.replace(b"status: Active", b'status: "Archived"').replace(b"- Workflow", b'- "Property"')
        self.assertEqual(output, expected)
        self.assertIn(b"version: 3\r\nupdated_at: old-time", output)

    def test_block_entry_add_remove_preserve_comments_body_and_order(self):
        added = prepare(SOURCE, [{"field": "Dependencies", "operation": "add", "value": "Action"}])
        self.assertEqual(added, SOURCE.replace(b"unrelated:", b'    - "Action"\r\nunrelated:'))
        removed = prepare(SOURCE, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
        self.assertEqual(removed, SOURCE.replace(b"    - Atom # first", b"    # first"))

    def test_full_set_keeps_comments_and_unrelated_bytes(self):
        output = prepare(SOURCE, [{"field": "Dependencies", "operation": "replace_set",
                                  "old": ["Atom", "Workflow"], "new": ["Property", "Action"]}])
        self.assertIn(b'["Property", "Action"]\r\n', output)
        for comment in (b"# first\r\n", b"# between\r\n", b"# second\r\n"):
            self.assertIn(comment, output)
        self.assertTrue(output.endswith(SOURCE[SOURCE.index(b"unrelated:"):]))
        self.assertNotIn(b"\n", output.replace(b"\r\n", b""))

    def test_whole_list_property_add_remove_and_no_op(self):
        added = prepare(SOURCE, [{"field": "Optional", "operation": "add", "value": ["A", "B"]}], entry=False)
        self.assertIn(b'"optional": ["A", "B"]\r\n---', added)
        removed = prepare(added, [{"field": "Optional", "operation": "remove", "old": ["A", "B"]}], entry=False)
        self.assertEqual(parse_carrier(removed, Path("supplied.md")).metadata,
                         parse_carrier(SOURCE, Path("supplied.md")).metadata)
        self.assertEqual(prepare(SOURCE, [{"field": "Dependencies", "operation": "add", "value": "Atom"}]), SOURCE)

    def test_flow_list_entry_operations_keep_other_fields_and_comments(self):
        source = SOURCE.replace(b"    - Atom # first\r\n    # between\r\n    - Workflow # second\r\n",
                                b'    [Atom, "Workflow"] # outside\r\n')
        added = prepare(source, [{"field": "Dependencies", "operation": "add", "value": "Action"}])
        self.assertEqual(added, source.replace(b'[Atom, "Workflow"]', b'[Atom, "Workflow", "Action"]'))
        replaced = prepare(source, [{"field": "Dependencies", "operation": "replace", "old": "Atom", "new": "Action"}])
        self.assertEqual(replaced, source.replace(b"[Atom,", b'["Action",'))
        removed = prepare(source, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
        self.assertEqual(removed, source.replace(b'[Atom, "Workflow"]', b'["Workflow"]'))

    def test_single_block_entry_remove_retains_comment_and_valid_empty_list(self):
        source = SOURCE.replace(b"    # between\r\n    - Workflow # second\r\n", b"")
        output = prepare(source, [{"field": "Dependencies", "operation": "remove", "value": "Atom"}])
        self.assertEqual(parse_carrier(output, Path("supplied.md")).metadata["subjects"]["depends_on"], [])
        self.assertIn(b"# first\r\n", output)
        self.assertTrue(output.endswith(source[source.index(b"unrelated:"):]))

    def test_refusals_are_pure_and_preserve_input(self):
        cases = [
            (SOURCE, [{"field": "Type", "operation": "replace", "old": "Requirement", "new": "Method"}]),
            (SOURCE, [{"field": "Dependencies", "operation": "replace", "old": "Absent", "new": "Action"}]),
            (SOURCE, [{"field": "Dependencies", "operation": "replace", "old": "Atom", "new": "Workflow"}]),
            (SOURCE.replace(b"status: Active", b"status: Active\r\nstatus: Active"), []),
            (SOURCE.replace(b"- Workflow", b"- Atom"), [{"field": "Dependencies", "operation": "remove", "value": "Atom"}]),
        ]
        with patch.object(Path, "read_bytes", side_effect=AssertionError("Parser must not read")), \
             patch.object(Path, "write_bytes", side_effect=AssertionError("Parser must not write")):
            self.assertEqual(prepare(SOURCE, []), SOURCE)
            for source, edits in cases:
                with self.subTest(edits=edits), self.assertRaises(PropertyEditError):
                    prepare(source, edits)
        with self.assertRaises(PropertyEditError) as error:
            prepare(SOURCE, [], expected="0" * 64)
        self.assertEqual(error.exception.code, "stale_state")


if __name__ == "__main__":
    unittest.main()
