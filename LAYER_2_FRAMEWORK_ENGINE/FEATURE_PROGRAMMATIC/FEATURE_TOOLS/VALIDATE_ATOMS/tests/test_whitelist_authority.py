"""Exact current authority bindings for the proposed reference whitelist."""

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


CONSUMED = (
    "CA-D-324", "CA-D-461", "CA-D-466", "CA-D-460", "CA-D-481", "CA-D-467", "CA-D-434",
    "CA-R-1309", "CA-R-1397", "CA-R-1398", "CA-R-1399", "CA-R-1539", "CA-R-1608",
    "CA-R-1874", "CA-R-1875",
)


class WhitelistAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.selection = self.fixture.project(source_ids=CONSUMED)
        self.root = self.selection.root

    def test_real_selected_context_reads_all_consumed_exact_source_bindings(self):
        context = proposed_carrier.source_context_from_project(self.root)
        report = {"bindings": {}, "coverage": {"gaps": []}}
        with bind_selection(context._selection):
            for identifier in CONSUMED:
                with self.subTest(identifier=identifier):
                    source = proposed_carrier._source(self.root, identifier, context._reader, report)
                    entry = proposed_carrier._entry(
                        identifier, graph=identifier in proposed_carrier.APPROVED_GRAPH_AUTHORITY_IDS,
                    )
                    self.assertEqual(source["binding"]["sha256"], entry["sha256"])
                    path = self.selection.control_root.joinpath(*Path(entry["source_path"]).parts[1:])
                    self.assertEqual(source["binding"]["path"], str(path))
        self.assertEqual(context._reader.currentness()["state"], "unchanged")

    def test_missing_and_wrong_identity_new_authority_refuse(self):
        identifier = "CA-D-434"
        entry = proposed_carrier._entry(identifier)
        original = fixtures.authority_fixture_bytes(identifier, entry)
        with tempfile.TemporaryDirectory(dir=self.root) as directory:
            root = Path(directory).resolve()
            path = root / entry["source_path"]
            path.parent.mkdir(parents=True)
            for raw in (None, original.replace(identifier.encode(), b"CA-R-999999")):
                with self.subTest(raw=raw):
                    if raw is not None:
                        path.write_bytes(raw)
                    reader = ReadContext(roots=[str(root)], limits=dict(CEILINGS))
                    report = {"bindings": {}, "coverage": {"gaps": []}}
                    with self.assertRaises(proposed_carrier.ProposedCarrierError):
                        proposed_carrier._source(root, identifier, reader, report)


if __name__ == "__main__":
    unittest.main()
