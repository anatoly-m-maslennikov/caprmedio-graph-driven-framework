"""Root Plan placement proof against the exact current CA-D-461 fixture."""

import hashlib
from pathlib import Path
import sys
import unittest

HERE = Path(__file__).resolve().parent
TOOLS = HERE.parents[1]
sys.path.insert(0, str(TOOLS))

from authoritative_status_models import capture_status_models  # noqa: E402
from project_selection import bind_selection  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier  # noqa: E402
from contained_atom_targets import _bindings  # noqa: E402
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier  # noqa: E402
import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402


CURRENT_D461 = HERE / "fixtures/current_plan_placement/CA-D-461.md"
CURRENT_D461_SHA256 = "96282d2eaf40d663de404d5ef03cb8682a0506733f0c239308731198de0bd373"


class CurrentPlanPlacementAuthorityTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProposedCarrierAdmissionRegressions()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)

    def current_context(self):
        selection = self.fixture.project(source_ids=tuple(dict.fromkeys(
            (*proposed_carrier._FRONTIER_IDS, *proposed_carrier._GRAPH_IDS, "CA-D-378"),
        )))
        raw = CURRENT_D461.read_bytes()
        self.assertEqual(hashlib.sha256(raw).hexdigest(), CURRENT_D461_SHA256)
        next(self.fixture.root.rglob("CA-D-461.md")).write_bytes(raw)
        with bind_selection(selection):
            context = proposed_carrier.source_context_from_project(self.fixture.root)
            status_index = capture_status_models(self.fixture.root, context._reader)
        return selection, context, status_index

    def test_fixture_is_exact_current_d461_v16(self):
        raw = CURRENT_D461.read_bytes()
        parsed = parse_carrier(raw, CURRENT_D461)
        self.assertEqual(parsed.metadata["atom_id"], "CA-D-461")
        self.assertEqual(parsed.metadata["version"], 16)
        self.assertEqual(hashlib.sha256(raw).hexdigest(), CURRENT_D461_SHA256)

    def test_source_derived_root_draft_and_archived_callers_pass(self):
        selection, context, status_index = self.current_context()
        _, _, statuses = _bindings(context)
        self.assertEqual(statuses["Plan"]["Draft"], "draft")
        self.assertEqual(statuses["Plan"]["Archived"], "archived")
        for status, folder in (("Draft", "draft"), ("Archived", "archived")):
            metadata = self.fixture.metadata(status=status, relations={})
            if status == "Draft":
                metadata.pop("atom_id")
            relative = Path("03_plan") / folder / ("CA-P-701@1.md" if status == "Archived" else "CA-P-701.md")
            with self.subTest(status=status), bind_selection(selection):
                result = proposed_carrier.validate_proposed_carrier(
                    metadata, fixtures.PLAN_BODY, context, relative,
                    allow_existing_relations=True, _status_index=status_index,
                )
                self.assertEqual((result["findings"], result["gaps"]), ([], []))


if __name__ == "__main__":
    unittest.main()
