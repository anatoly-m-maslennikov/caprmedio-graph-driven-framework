"""Exact finite supporting sources for one explicit Atom section edit."""

from pathlib import Path
import sys
import tempfile
import unittest

TOOL = Path(__file__).resolve().parents[1]
TOOLS = TOOL.parent
REPOSITORY = TOOLS.parents[2]
sys.path[:0] = [str(TOOLS), str(TOOL)]

from project_selection import bind_selection
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier
from VALIDATE_ATOMS.validate_atoms_workers.read_io import ReadContext
from VALIDATE_ATOMS.validate_atoms_workers.settings import CEILINGS
import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402


SECTION_SOURCES = ("CA-R-1933", "CA-M-373", "CA-D-623")


class SectionAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.project(source_ids=SECTION_SOURCES)
        self.root = self.selection.root

    def test_selected_context_lazily_reads_exact_section_sources(self):
        context = proposed_carrier.source_context_from_project(self.root)
        initial_ids = {source["binding"]["atom_id"] for source in context.inputs["sources"]}
        self.assertTrue(set(SECTION_SOURCES).isdisjoint(initial_ids))
        report = {"bindings": {}, "coverage": {"gaps": []}}
        with bind_selection(context._selection):
            for identifier in SECTION_SOURCES:
                with self.subTest(identifier=identifier):
                    source = proposed_carrier._source(
                        context.root, identifier, context._reader, report
                    )
                    entry = proposed_carrier._entry(identifier)
                    self.assertEqual(source["binding"]["sha256"], entry["sha256"])
                    path = self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:])
                    self.assertEqual(source["binding"]["path"], str(path))
        self.assertEqual(context._reader.currentness()["state"], "unchanged")

    def test_missing_and_wrong_identity_section_sources_refuse(self):
        for identifier in SECTION_SOURCES:
            entry = proposed_carrier._entry(identifier)
            original = fixtures.authority_fixture_bytes(identifier, entry)
            with tempfile.TemporaryDirectory(dir=self.root) as directory:
                root = Path(directory).resolve()
                path = root / entry["source_path"]
                path.parent.mkdir(parents=True)
                for raw in (None, original.replace(identifier.encode(), b"CA-R-999999")):
                    with self.subTest(identifier=identifier, missing=raw is None):
                        if raw is not None:
                            path.write_bytes(raw)
                        reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
                        report = {"bindings": {}, "coverage": {"gaps": []}}
                        with self.assertRaises(proposed_carrier.ProposedCarrierError):
                            proposed_carrier._source(root, identifier, reader, report)


if __name__ == "__main__":
    unittest.main()
