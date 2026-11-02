"""Author controls for current Operations proposals inside authenticated bundles."""

from copy import deepcopy
from pathlib import Path
import unittest
from unittest.mock import patch

import yaml

import test_proposed_reference_scope_independent as scoped_fixture
from VALIDATE_ATOMS.validate_atoms_workers import proposed_carrier
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier
from golden_authority import write_frozen_authority


BODY = ("# Summary\n\nInvoke one selected Action\n\n## Scope\n\nOne explicit input.\n\n"
        "## Operation\n\nInvoke CA-O-702 with that input.\n\n## Details\n\nReturn its result.\n")


class NestedOperationsPlacementTests(unittest.TestCase):
    def setUp(self):
        self.fixture = scoped_fixture.ExplicitReferenceScopeIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        write_frozen_authority(self.fixture.root, self.fixture.control, ("CA-D-289", "CA-D-378"))

    def metadata(self, **changes):
        value = self.fixture.fixture.metadata(
            atom_id="CA-O-730", content_role="Operations", type="Step",
            relations={"depends_on": ["CA-O-702"]},
        )
        value.pop("label")
        value.update(changes)
        return value

    def raw(self, **changes):
        return ("---\n" + yaml.safe_dump(self.metadata(**changes), sort_keys=False)
                + "---\n" + BODY).encode()

    def put(self, relative, **changes):
        return self.fixture.fixture.put(self.fixture.control / relative, self.raw(**changes))

    def validate(self, relative, **changes):
        path = Path(relative)
        parsed = parse_carrier(self.raw(**changes), self.fixture.root / self.fixture.control / path)
        before = deepcopy(parsed.metadata)
        result = proposed_carrier.validate_proposed_carrier(
            parsed.metadata, parsed.body, self.fixture.context, path,
            reference_roles=scoped_fixture.PRMEDO,
        )
        self.assertEqual(parsed.metadata, before)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertTrue(all(row["outcome"] == "passed" for row in result["outcomes"]))

    def test_standalone_complete_step_remains_admitted(self):
        self.validate("09_operations/step.md")

    def test_current_nested_archive_and_active_local_placement_preserve_sources(self):
        self.put("09_operations/workflow.md", atom_id="CA-O-731", type="Workflow")
        before = scoped_fixture.fixtures.snapshot(self.fixture.root)
        self.validate("09_operations/workflow/archived/step@4.md", status="Archived", version=4)
        self.validate("09_operations/workflow/step.md")
        self.assertEqual(scoped_fixture.fixtures.snapshot(self.fixture.root), before)

    def test_recursive_step_and_archived_ancestor_do_not_override_child_status(self):
        self.put("09_operations/archived/workflow@4.md", atom_id="CA-O-731",
                 type="Workflow", status="Archived", version=4)
        self.put("09_operations/archived/workflow@4/first.md", atom_id="CA-O-732")
        self.validate("09_operations/archived/workflow@4/first/leaf.md")

    def test_local_draft_status_resets_inside_each_step_container(self):
        self.put("09_operations/draft/workflow.md", atom_id="CA-O-731",
                 type="Workflow", status="Draft")
        self.put("09_operations/draft/workflow/draft/first.md", atom_id="CA-O-732", status="Draft")
        self.validate("09_operations/draft/workflow/draft/first/leaf.md")

    def test_nested_archive_requires_current_naming_authority(self):
        self.put("09_operations/workflow.md", atom_id="CA-O-731", type="Workflow")
        pin = proposed_carrier._entry("CA-D-289")
        path = self.fixture.root / self.fixture.control.joinpath(*Path(pin["source_path"]).parts[1:])
        path.write_bytes(path.read_bytes().replace(b"atom_id:", b"invalid_atom_id:", 1))
        with self.assertRaises(proposed_carrier.ProposedCarrierError):
            self.validate("09_operations/workflow/archived/step@4.md", status="Archived", version=4)

    def test_naming_authority_drift_after_capture_refuses(self):
        self.put("09_operations/workflow.md", atom_id="CA-O-731", type="Workflow")
        pin = proposed_carrier._entry("CA-D-289")
        path = self.fixture.root / self.fixture.control.joinpath(*Path(pin["source_path"]).parts[1:])
        original = path.read_bytes()
        place = proposed_carrier._operations_placement
        observed = []

        def place_then_drift(*args, **kwargs):
            place(*args, **kwargs)
            path.write_bytes(original + b"\nChanged after naming authority capture.\n")
            observed.append(True)

        try:
            with patch.object(proposed_carrier, "_operations_placement", place_then_drift):
                with self.assertRaises(proposed_carrier.ProposedCarrierError):
                    self.validate("09_operations/workflow/archived/step@4.md", status="Archived", version=4)
            self.assertTrue(observed)
        finally:
            path.write_bytes(original)

    def test_active_chain_does_not_require_archive_naming_authority(self):
        self.put("09_operations/workflow.md", atom_id="CA-O-731", type="Workflow")
        pin = proposed_carrier._entry("CA-D-289")
        path = self.fixture.root / self.fixture.control.joinpath(*Path(pin["source_path"]).parts[1:])
        path.unlink()
        self.validate("09_operations/workflow/step.md")

    def test_parent_identity_must_use_its_operations_namespace(self):
        self.put("09_operations/workflow.md", atom_id="CA-P-731", type="Workflow")
        with self.assertRaises(proposed_carrier.ProposedCarrierError):
            self.validate("09_operations/workflow/step.md")

    def test_arbitrary_or_wrong_typed_container_cannot_admit_current_step(self):
        for kind in (None, "Action", "Workflow"):
            with self.subTest(parent=kind):
                parent = None if kind is None else self.put(
                    "09_operations/workflow.md", atom_id="CA-O-731", type=kind)
                if kind == "Workflow":
                    for child_kind in ("Action", "Workflow"):
                        with self.subTest(child_kind=child_kind), self.assertRaises(proposed_carrier.ProposedCarrierError):
                            self.validate("09_operations/workflow/child.md", type=child_kind)
                    with self.assertRaises(proposed_carrier.ProposedCarrierError):
                        self.validate("09_operations/workflow/arbitrary/step.md")
                else:
                    with self.assertRaises(proposed_carrier.ProposedCarrierError):
                        self.validate("09_operations/workflow/step.md")
                if parent is not None:
                    parent.unlink()


if __name__ == "__main__":
    unittest.main()
