"""Focused regression tests for the bounded Atom-authority pin refresh."""

from __future__ import annotations

import hashlib
import sys
import unittest
from pathlib import Path


TOOLS = Path(__file__).resolve().parents[1]
VALIDATE = TOOLS / "VALIDATE_ATOMS"
sys.path.insert(0, str(TOOLS))
sys.path.insert(0, str(VALIDATE))

from atom_operations import ToolError, prepare_create_atom_revision  # noqa: E402
from project_selection import bind_selection  # noqa: E402
from VALIDATE_ATOMS.tests.golden_authority import frozen_entry  # noqa: E402
from VALIDATE_ATOMS.tests import test_proposed_carrier_admission_regressions as fixtures  # noqa: E402
from validate_atoms_workers.registry_refresh import (  # noqa: E402
    APPROVED_REFRESH_IDS,
    refresh_entries,
)


class RegistryRefreshTest(unittest.TestCase):
    def setUp(self) -> None:
        fixture = fixtures.ProposedCarrierAdmissionRegressions()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.root = fixture.root
        selection = fixture.project()
        self.entries = {
            identity: frozen_entry(identity)
            for identity in ("CA-D-274", "CA-D-276")
        }
        for entry in self.entries.values():
            entry["source_path"] = selection.control_relative.joinpath(
                *Path(entry["source_path"]).parts[1:]
            ).as_posix()

    def test_refreshes_only_uniquely_active_approved_sources(self) -> None:
        expected_version = self.entries["CA-D-276"]["version"]
        self.entries["CA-D-276"].update(version=1, sha256="0" * 64)
        refreshed = refresh_entries(self.root, self.entries, ["CA-D-276"])

        source = self.root / refreshed["CA-D-276"]["source_path"]
        self.assertEqual(expected_version, refreshed["CA-D-276"]["version"])
        self.assertEqual(
            refreshed["CA-D-276"]["sha256"], hashlib.sha256(source.read_bytes()).hexdigest()
        )
        self.assertEqual(refreshed["CA-D-274"], self.entries["CA-D-274"])

    def test_refuses_unapproved_or_ambiguous_sources(self) -> None:
        with self.assertRaisesRegex(ValueError, "not approved"):
            refresh_entries(self.root, {}, ["CA-D-999"])
        with self.assertRaisesRegex(ValueError, "unique"):
            refresh_entries(self.root, {}, ["CA-D-276", "CA-D-276"])

    def test_authorized_set_is_exact(self) -> None:
        self.assertEqual(
            APPROVED_REFRESH_IDS,
            frozenset({
                "CA-D-276", "CA-D-269", "CA-D-268", "CA-D-270", "CA-D-274",
                "CA-D-446", "CA-D-479", "CA-D-482", "CA-D-483",
            }),
        )


class CompleteCarrierPreflightTest(unittest.TestCase):
    relative = ".caprmedio_selected/07_delivery/CA-D-987654--carrier-preflight.md"

    def setUp(self) -> None:
        fixture = fixtures.ProposedCarrierAdmissionRegressions()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.root = fixture.root
        self.enterContext(
            bind_selection(fixture.project(source_ids=("CA-R-1309", "CA-R-1397", "CA-R-1399")))
        )

    @staticmethod
    def frontmatter(
        *, author: bool = True, status: bool = True, role: str = "Delivery", relations: str = "relations: {}"
    ) -> str:
        rows = [
            'atom_id: "CA-D-987654"',
            f'content_role: "{role}"',
            'current_scope_unit: "amber"',
            'claim_target_scope_unit: "amber"',
            'local_tier: "Standard"',
            'global_tier: 2',
        ]
        if author:
            rows.append('author: "Fixture Operator"')
        if status:
            rows.append('status: "Active"')
        return "\n".join(rows + [
            "subjects:", '  governs: "Atom/Test"', "  depends_on: []", relations,
        ])

    @staticmethod
    def body() -> str:
        return "# Summary\n\nTest\n\n## Scope\n\nTest\n\n## Claim\n\nTest\n\n## Details\n"

    def test_missing_required_author_or_status_refuses_before_write(self) -> None:
        destination = self.root / self.relative
        self.assertFalse(destination.exists())
        for frontmatter in (self.frontmatter(author=False), self.frontmatter(status=False)):
            with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
                prepare_create_atom_revision(self.root, self.relative, frontmatter, self.body())
        self.assertFalse(destination.exists())

    def test_empty_body_refuses_before_write(self) -> None:
        destination = self.root / self.relative
        with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
            prepare_create_atom_revision(self.root, self.relative, self.frontmatter(), "")
        self.assertFalse(destination.exists())

    def test_complete_author_status_and_relational_scope_pass_preflight(self) -> None:
        path, frontmatter, atom_id = prepare_create_atom_revision(
            self.root, self.relative, self.frontmatter(), self.body()
        )
        self.assertEqual(path, self.root / self.relative)
        self.assertEqual(atom_id, "CA-D-987654")
        self.assertIn('updated_at: "', frontmatter)
        self.assertIn("version: 1", frontmatter)

    def test_requirement_and_method_status_models_pass_preflight(self) -> None:
        for role, directory in (("Requirement", "04_requirement"), ("Method", "05_method")):
            relative = self.relative.replace("07_delivery", directory)
            _, frontmatter, _ = prepare_create_atom_revision(
                self.root, relative, self.frontmatter(role=role), self.body()
            )
            self.assertIn("version: 1", frontmatter)

    def test_nonempty_relation_refuses_before_write(self) -> None:
        destination = self.root / self.relative
        with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
            prepare_create_atom_revision(
                self.root,
                self.relative,
                self.frontmatter(relations='relations:\n  made_up: ["CA-R-1"]'),
                self.body(),
            )
        self.assertFalse(destination.exists())

    def test_role_or_archived_status_path_mismatch_refuses_before_write(self) -> None:
        with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
            prepare_create_atom_revision(
                self.root,
                self.relative.replace("07_delivery", "04_requirement"),
                self.frontmatter(),
                self.body(),
            )

    def test_wrong_owner_authority_path_refuses_before_write(self) -> None:
        with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
            prepare_create_atom_revision(
                self.root,
                self.relative.replace(
                    "07_delivery", "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/07_delivery"
                ),
                self.frontmatter(),
                self.body(),
            )

    def test_plan_backlog_requires_d461_directory(self) -> None:
        plan_path = self.relative.replace("07_delivery/CA-D-987654", "03_plan/001_backlog/CA-P-987654")
        plan_frontmatter = self.frontmatter(role="Plan").replace('atom_id: "CA-D-987654"', 'atom_id: "CA-P-987654"').replace('status: "Active"', 'status: "Backlog"') + '\ntype: "Plan"'
        plan_body = "# Summary\n\nTest\n\n## Objective\n\nTest\n\n## Details\n\n### Definition of Done\n\nTest\n"
        _, _, atom_id = prepare_create_atom_revision(self.root, plan_path, plan_frontmatter, plan_body)
        self.assertEqual(atom_id, "CA-P-987654")
        with self.assertRaisesRegex(ToolError, "incomplete, invalid, or unresolved"):
            prepare_create_atom_revision(self.root, plan_path.replace("001_backlog/", ""), plan_frontmatter, plan_body)

    def test_relocation_preflight_preserves_existing_revision(self) -> None:
        _, frontmatter, _ = prepare_create_atom_revision(
            self.root,
            self.relative,
            self.frontmatter() + '\nversion: 8\nupdated_at: "2026-10-08 12:00:00 +0400"',
            self.body(),
            creating=False,
        )
        self.assertIn("version: 8", frontmatter)
        self.assertIn('updated_at: "2026-10-08 12:00:00 +0400"', frontmatter)
        with self.assertRaisesRegex(ToolError, "Archived carrier requires its Revision suffix"):
            prepare_create_atom_revision(
                self.root,
                self.relative,
                self.frontmatter().replace('status: "Active"', 'status: "Archived"'),
                self.body(),
            )


if __name__ == "__main__":
    unittest.main()
