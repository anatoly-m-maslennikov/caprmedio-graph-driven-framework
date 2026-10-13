"""Exact current authority bindings for the proposed reference whitelist."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1]
TOOLS = TOOL.parent
REPOSITORY = TOOLS.parents[2]
sys.path[:0] = [str(TOOLS), str(TOOL)]

from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers.authority import _domain
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS


CONSUMED = (
    "CA-D-324", "CA-D-461", "CA-D-466", "CA-D-460", "CA-D-481", "CA-D-467", "CA-D-434",
    "CA-R-1309", "CA-R-1397", "CA-R-1398", "CA-R-1399", "CA-R-1539", "CA-R-1608",
    "CA-R-1874", "CA-R-1875",
)
MANIFESTS = (
    "registry.json", "schema_authority.json", "graph_authority.json",
    "structure_authority.json", "context_authority.json",
)


class WhitelistAuthorityTests(unittest.TestCase):
    def test_consumed_pins_match_exact_current_unprojected_carriers(self):
        manifests = [json.loads((TOOL / "validate_atoms_workers" / name).read_text())["sources"]
                     for name in MANIFESTS]
        canonical = Path(".caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES")
        for identifier in CONSUMED:
            with self.subTest(identifier=identifier):
                entries = [manifest[identifier] for manifest in manifests if identifier in manifest]
                self.assertTrue(entries)
                pins = {(row["version"], row["sha256"], row["source_path"]) for row in entries}
                self.assertEqual(len(pins), 1)
                entry = proposed_carrier._entry(identifier)
                self.assertIn((entry["version"], entry["sha256"], entry["source_path"]), pins)
                relative = Path(entry["source_path"])
                self.assertTrue(relative.is_relative_to(canonical))
                self.assertFalse({"archive", "_projection", "APPLICABLE_METHODOLOGY"} & set(relative.parts))
                path = REPOSITORY / relative
                raw = path.read_bytes()
                metadata = parse_carrier(raw, path).metadata
                self.assertEqual(metadata["atom_id"], identifier)
                self.assertEqual(metadata["version"], entry["version"])
                self.assertIn(metadata["status"], {"Active", "active"})
                self.assertNotIn("projection", metadata)
                self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])

    def test_status_domains_retain_the_exact_source_values(self):
        domains = {
            **{identifier: ("Draft", "Active", "Archived") for identifier in
               ("CA-R-1309", "CA-R-1397", "CA-R-1398", "CA-R-1399", "CA-R-1874")},
            "CA-R-1539": ("Active", "Backlog", "Done", "Canceled", "Archived"),
            "CA-R-1608": ("draft", "active", "resolved", "canceled"),
            "CA-R-1875": ("Draft", "Done", "Archived"),
        }
        for identifier, expected in domains.items():
            with self.subTest(identifier=identifier):
                entry = proposed_carrier._entry(identifier)
                self.assertEqual(_domain((REPOSITORY / entry["source_path"]).read_text()), expected)

    def test_real_selected_context_reads_all_consumed_exact_source_bindings(self):
        context = proposed_carrier.source_context_from_project(REPOSITORY)
        report = {"bindings": {}, "coverage": {"gaps": []}}
        with bind_selection(context._selection):
            for identifier in CONSUMED:
                with self.subTest(identifier=identifier):
                    source = proposed_carrier._source(REPOSITORY, identifier, context._reader, report)
                    entry = proposed_carrier._entry(identifier)
                    self.assertEqual(source["binding"]["sha256"], entry["sha256"])
                    self.assertEqual(source["binding"]["path"], str(REPOSITORY / entry["source_path"]))
        self.assertEqual(context._reader.currentness()["state"], "unchanged")

    def test_missing_and_changed_new_authority_refuse(self):
        identifier = "CA-D-434"
        entry = proposed_carrier._entry(identifier)
        original = (REPOSITORY / entry["source_path"]).read_bytes()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory).resolve()
            path = root / entry["source_path"]
            path.parent.mkdir(parents=True)
            for raw in (None, original + b"\nchanged\n"):
                with self.subTest(raw=raw):
                    if raw is not None:
                        path.write_bytes(raw)
                    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
                    report = {"bindings": {}, "coverage": {"gaps": []}}
                    with self.assertRaises(proposed_carrier.ProposedCarrierError):
                        proposed_carrier._source(root, identifier, reader, report)


if __name__ == "__main__":
    unittest.main()
