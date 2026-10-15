"""Parse reuse never replaces the real identity frontier or byte-freshness checks."""
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(TOOLS / "ATOM_UPDATE/tests"))

import atom_operations as operations
import atom_subject_patch as subjects
from VALIDATE_ATOMS.validate_atoms_workers import parsing
import test_nonarchived_subject_preview as fixtures

STAMP = "2026-10-14 10:20:30 +0400"


class IdentityParseReuseTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.NonarchivedSubjectPreviewTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.source = self.fixture._plan("Active", number=7801)
        self.items = self.fixture._payload(self.source)
        self.unrelated = self.source.parent.parent / "01_concern/CA-C-7901--unrelated.md"
        self.unrelated.parent.mkdir(parents=True, exist_ok=True)
        self.unrelated.write_bytes(b"---\natom_id: CA-C-7901\nstatus: Active\n---\nLegacy concern\n")

    def preview(self):
        return subjects.preview_subject_patches(self.root, self.items, timestamp=STAMP)

    def count_path(self, spy):
        return sum(call.args[1] == self.unrelated for call in spy.call_args_list)

    def test_preview_parses_once_but_keeps_four_fresh_reads_and_four_inventories(self):
        original_read = subjects.ReadContext.read
        reads = []

        def read(reader, path, **kwargs):
            reads.append(path)
            return original_read(reader, path, **kwargs)

        with patch.object(operations, "parse_carrier", wraps=operations.parse_carrier) as parser, \
                patch.object(subjects.ReadContext, "read", read), \
                patch.object(subjects.ReadContext, "inventory", autospec=True,
                             side_effect=subjects.ReadContext.inventory) as inventory:
            result = self.preview()
        self.assertEqual(1, result["count"])
        self.assertEqual(1, self.count_path(parser))
        self.assertEqual(4, reads.count(self.unrelated))
        self.assertEqual(4, sum(call.args[1] == operations.control_root(self.root)
                                for call in inventory.call_args_list))

    def test_two_public_previews_do_not_share_parse_state(self):
        with patch.object(operations, "parse_carrier", wraps=operations.parse_carrier) as parser:
            first, second = self.preview(), self.preview()
        self.assertEqual(first, second)
        self.assertEqual(2, self.count_path(parser))

    def test_changed_bytes_are_reparsed_and_a_new_metadata_identity_claim_refuses(self):
        original_materialize = subjects._materialize_item

        def materialize(*args, **kwargs):
            result = original_materialize(*args, **kwargs)
            self.unrelated.write_bytes(self.unrelated.read_bytes().replace(b"CA-C-7901", b"CA-P-7801"))
            return result

        with patch.object(operations, "parse_carrier", wraps=operations.parse_carrier) as parser, \
                patch.object(subjects, "_materialize_item", materialize):
            with self.assertRaises(operations.ToolError) as caught:
                self.preview()
        self.assertEqual("subject-identity-duplicate", caught.exception.code)
        self.assertEqual(2, self.count_path(parser))

    def test_unrelated_parse_error_is_reused_without_suppressing_claim_checks(self):
        self.unrelated.write_bytes(b"---\natom_id: CA-C-7901\nbroken: [\n---\nLegacy concern\n")
        with patch.object(operations, "parse_carrier", wraps=operations.parse_carrier) as parser:
            self.assertEqual(1, self.preview()["count"])
        self.assertEqual(1, self.count_path(parser))

    def test_changed_cached_parse_error_cannot_hide_a_decoded_selected_claim(self):
        self.unrelated.write_bytes(b"---\natom_id: CA-C-7901\nbroken: [\n---\nLegacy concern\n")
        original_materialize = subjects._materialize_item

        def materialize(*args, **kwargs):
            result = original_materialize(*args, **kwargs)
            self.unrelated.write_bytes(b'---\natom_id: "CA-P-\\x37\\x38\\x30\\x31"\nbroken: [\n---\nLegacy concern\n')
            return result

        with patch.object(operations, "parse_carrier", wraps=operations.parse_carrier) as parser, \
                patch.object(subjects, "_materialize_item", materialize):
            with self.assertRaises(operations.ToolError) as caught:
                self.preview()
        self.assertEqual("subject-identity-inventory-unavailable", caught.exception.code)
        self.assertEqual(2, self.count_path(parser))

    def test_parser_resource_ceiling_is_executed_before_reusing_failure(self):
        raw = b"---\natom_id: CA-C-7901\nnested: " + b"[" * 70 + b"0" + b"]" * 70 + b"\n---\nLegacy\n"
        self.unrelated.write_bytes(raw)
        with self.assertRaises(parsing.CarrierError) as caught:
            operations.parse_carrier(raw, self.unrelated)
        self.assertEqual("YAML_UNSUPPORTED", caught.exception.code)
        with patch.object(operations, "parse_carrier", wraps=operations.parse_carrier) as parser:
            self.assertEqual(1, self.preview()["count"])
        self.assertEqual(1, self.count_path(parser))


if __name__ == "__main__":
    unittest.main()
