from __future__ import annotations

import unittest
from pathlib import Path


import sys

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from lifecycle_intents import LifecycleError, create_atom_action  # noqa: E402
from project_selection import bind_selection  # noqa: E402
from VALIDATE_ATOMS.tests import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402


class CreateAtomConflictTests(unittest.TestCase):
    def setUp(self) -> None:
        fixture = fixtures.ProposedCarrierAdmissionRegressions()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.root = fixture.root
        self.enterContext(
            bind_selection(fixture.project(source_ids=("CA-R-1309", "CA-R-1397", "CA-R-1399")))
        )
        self.destination = self.root / ".caprmedio_selected/04_requirement/CA-R-901--occupied.md"
        self.destination.parent.mkdir(parents=True)
        self.destination.write_text(
            "---\n"
            "atom_id: CA-R-901\n"
            "content_role: Requirement\n"
            "status: Active\n"
            "version: 2\n"
            "updated_at: 2026-10-06 00:00:00 +0000\n"
            "---\n"
            "# Summary\n\n"
            "Existing occupied carrier\n",
            encoding="utf-8",
        )

    def carrier(self, atom_id: str, path: Path, summary: str) -> dict[str, str]:
        return {
            "path": path.relative_to(self.root).as_posix(),
            "frontmatter": (
                f"atom_id: {atom_id}\ncontent_role: Requirement\ncurrent_scope_unit: amber\n"
                "claim_target_scope_unit: amber\nlocal_tier: Standard\nglobal_tier: 2\n"
                "author: Fixture Operator\nstatus: Active\nsubjects:\n"
                "  governs: Atom/Test\n  depends_on: []\nrelations: {}"
            ),
            "content": (
                f"# Summary\n\n{summary}\n\n## Scope\n\nFixture.\n\n"
                "## Claim\n\nFixture claim.\n\n## Details\n\nFixture details.\n"
            ),
        }

    def test_occupied_destination_with_different_carrier_is_a_conflict_without_write(self) -> None:
        request = {
            "carrier": self.carrier("CA-R-901", self.destination, "Requested new carrier")
        }
        before = self.destination.read_bytes()

        with self.assertRaisesRegex(LifecycleError, "destination-collision"):
            create_atom_action(self.root, request, execute=True, authorized=True)

        self.assertEqual(before, self.destination.read_bytes())

    def test_malformed_preserved_history_reserves_identity_without_inferring_an_atom(self) -> None:
        history = self.destination.parent / "archive" / "CA-R-902--retained@1.md"
        history.parent.mkdir()
        history.write_bytes(b"retained but malformed historical bytes")
        destination = self.destination.with_name("CA-R-902--new.md")
        request = {
            "carrier": self.carrier("CA-R-902", destination, "New carrier")
        }

        with self.assertRaisesRegex(LifecycleError, "atom-id-collision"):
            create_atom_action(self.root, request, execute=True, authorized=True)

        self.assertEqual(b"retained but malformed historical bytes", history.read_bytes())
        self.assertFalse(destination.exists())


if __name__ == "__main__":
    unittest.main()
