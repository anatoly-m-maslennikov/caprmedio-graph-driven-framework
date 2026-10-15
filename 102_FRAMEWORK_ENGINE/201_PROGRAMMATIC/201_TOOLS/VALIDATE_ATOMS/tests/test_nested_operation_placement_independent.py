"""Independent complete-carrier controls for D467's nested Step placement."""

from copy import deepcopy
import hashlib
from pathlib import Path
import unittest
from unittest.mock import patch

import yaml

import test_proposed_reference_scope_independent as scoped
from VALIDATE_ATOMS.validate_atoms_workers.parsing import parse_carrier


BODY = (
    "# Summary\n\nRead the selected configuration\n\n## Scope\n\n"
    "One selected configuration.\n\n## Operation\n\n"
    "Invoke CA-O-702 with the selected configuration as input.\n\n"
    "## Details\n\nReturn the complete observed configuration.\n"
)


class NestedOperationPlacementIndependentTests(unittest.TestCase):
    def setUp(self):
        self.fixture = scoped.ExplicitReferenceScopeIndependentTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root
        self.control = self.fixture.control
        for identifier in ("CA-D-289", "CA-D-378"):
            entry = scoped.admission._entry(identifier)
            raw = (scoped.fixtures.REPOSITORY / entry["source_path"]).read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), entry["sha256"])
            self.fixture.fixture.put(
                self.control.joinpath(*Path(entry["source_path"]).parts[1:]), raw,
            )

    def metadata(self, **changes):
        metadata = self.fixture.fixture.metadata(
            atom_id="CA-O-720", content_role="Operations", type="Step",
            relations={"depends_on": ["CA-O-702"]},
        )
        metadata.pop("label")
        metadata.update(changes)
        return metadata

    def raw(self, **changes):
        return ("---\n" + yaml.safe_dump(self.metadata(**changes), sort_keys=False)
                + "---\n" + BODY).encode()

    def parent(self, relative="09_operations/workflow.md", **changes):
        return self.fixture.fixture.put(
            self.control / relative,
            self.raw(atom_id="CA-O-721", type="Workflow", **changes),
        )

    def validate(self, relative="09_operations/workflow/step.md", **changes):
        path = Path(relative)
        parsed = parse_carrier(self.raw(**changes), self.root / self.control / path)
        original = deepcopy(parsed.metadata)
        result = scoped.admission.validate_proposed_carrier(
            parsed.metadata, parsed.body, self.fixture.context, path,
            reference_roles=scoped.PRMEDO,
        )
        self.assertEqual(parsed.metadata, original)
        self.assertEqual((result["findings"], result["gaps"]), ([], []))
        self.assertTrue(all(row["outcome"] == "passed" for row in result["outcomes"]))
        return result

    def test_standalone_step_still_passes_complete_admission(self):
        self.validate("09_operations/step.md")

    def test_active_step_under_authenticated_workflow_passes_without_writes(self):
        self.parent()
        before = scoped.fixtures.snapshot(self.root)
        self.validate()
        self.assertEqual(scoped.fixtures.snapshot(self.root), before)

    def test_all_active_nested_chain_does_not_require_archive_policy_source(self):
        self.parent()
        self.fixture.fixture.put(self.control / "09_operations/workflow/first.md",
                                 self.raw(atom_id="CA-O-722"))
        entry = scoped.admission._entry("CA-D-289")
        source = self.root / self.control.joinpath(*Path(entry["source_path"]).parts[1:])
        source.unlink()
        before = scoped.fixtures.snapshot(self.root)
        self.validate("09_operations/workflow/first/leaf.md")
        self.assertEqual(scoped.fixtures.snapshot(self.root), before)

    def test_operations_parent_with_plan_namespace_identity_refuses(self):
        self.fixture.fixture.put(self.control / "09_operations/workflow.md",
                                 self.raw(atom_id="CA-P-721", type="Workflow"))
        before = scoped.fixtures.snapshot(self.root)
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()
        self.assertEqual(scoped.fixtures.snapshot(self.root), before)

    def test_recursive_step_containers_pass_complete_admission(self):
        self.parent()
        for relative, identifier in (
            ("09_operations/workflow/first.md", "CA-O-722"),
            ("09_operations/workflow/first/second.md", "CA-O-723"),
        ):
            self.fixture.fixture.put(self.control / relative,
                                     self.raw(atom_id=identifier))
        self.validate("09_operations/workflow/first/second/leaf.md")

    def test_local_archived_step_uses_own_status_and_version_suffix(self):
        self.parent()
        self.validate("09_operations/workflow/archived/step@2.md",
                      status="Archived", version=2)

    def test_archived_ancestor_does_not_override_active_child_status(self):
        self.parent("09_operations/archived/workflow@2.md", status="Archived", version=2)
        self.validate("09_operations/archived/workflow@2/step.md")

    def test_unchanged_older_revision_does_not_replace_current_step(self):
        self.parent()
        historical = self.fixture.fixture.put(
            self.control / "09_operations/workflow/archived/step@1.md",
            self.raw(version=1),
        )
        before = historical.read_bytes()
        self.validate(version=2)
        self.assertEqual(historical.read_bytes(), before)

    def test_archived_step_requires_matching_version_suffix(self):
        self.parent()
        for filename in ("step.md", "step@1.md"):
            with self.subTest(filename=filename):
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate(f"09_operations/workflow/archived/{filename}",
                                  status="Archived", version=2)

    def test_missing_or_differently_named_workflow_parent_refuses(self):
        for relative in (None, "09_operations/other-workflow.md"):
            with self.subTest(parent=relative):
                parent = self.parent(relative) if relative else None
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate()
                if parent:
                    parent.unlink()

    def test_wrong_parent_role_type_owner_status_or_version_refuses(self):
        for change in (
            {"content_role": "Plan"}, {"type": "Action"},
            {"current_scope_unit": "foreign"}, {"status": "Archived"},
            {"version": 0}, {"version": True},
        ):
            with self.subTest(change=change):
                self.fixture.fixture.put(self.control / "09_operations/workflow.md",
                    self.raw(atom_id="CA-O-721", **{"type": "Workflow", **change}))
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate()

    def test_missing_intermediate_step_parent_refuses(self):
        self.parent()
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate("09_operations/workflow/missing/leaf.md")

    def test_action_or_second_workflow_inside_container_refuses(self):
        self.parent()
        for kind in ("Action", "Workflow"):
            with self.subTest(kind=kind), self.assertRaises(scoped.admission.ProposedCarrierError):
                self.validate(type=kind)

    def test_child_owner_role_and_local_status_mismatch_refuse(self):
        self.parent()
        for relative, changes in (
            ("09_operations/workflow/step.md", {"current_scope_unit": "foreign"}),
            ("09_operations/workflow/step.md", {"content_role": "Method"}),
            ("09_operations/workflow/step.md", {"status": "Archived"}),
            ("09_operations/workflow/unrecognized/step.md", {}),
        ):
            with self.subTest(relative=relative, changes=changes):
                with self.assertRaises(scoped.admission.ProposedCarrierError):
                    self.validate(relative, **changes)

    def test_recursive_container_must_be_step_not_another_workflow(self):
        self.parent()
        self.fixture.fixture.put(self.control / "09_operations/workflow/second.md",
                                 self.raw(atom_id="CA-O-722", type="Workflow"))
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate("09_operations/workflow/second/leaf.md")

    def test_symlinked_parent_file_or_container_refuses(self):
        parent = self.parent("09_operations/elsewhere.md")
        alias = parent.with_name("workflow.md")
        alias.symlink_to(parent)
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()
        alias.unlink()
        self.parent()
        elsewhere = self.root / self.control / "elsewhere"
        elsewhere.mkdir()
        (parent.parent / "workflow").symlink_to(elsewhere, target_is_directory=True)
        with self.assertRaises(scoped.admission.ProposedCarrierError):
            self.validate()

    def test_current_workflow_delivery_authority_is_observed_before_use(self):
        self.parent()
        entry = scoped.admission._entry("CA-D-467")
        path = self.root / self.control.joinpath(*Path(entry["source_path"]).parts[1:])
        raw = path.read_bytes()
        version = parse_carrier(raw, path).metadata["version"]
        current = raw.replace(f"version: {version}\n".encode(), f"version: {version + 1}\n".encode())
        path.write_bytes(current)
        self.validate()
        self.assertEqual(hashlib.sha256(current).hexdigest(),
                         self.fixture.context._reader.fingerprints[str(path)])

    def test_workflow_delivery_authority_drift_after_capture_refuses(self):
        self.parent()
        entry = scoped.admission._entry("CA-D-467")
        authority_path = self.root / self.control.joinpath(*Path(entry["source_path"]).parts[1:])
        original = scoped.admission.ReadContext.read
        changed = False

        def read(reader, path, *args, **kwargs):
            nonlocal changed
            raw = original(reader, path, *args, **kwargs)
            if Path(path) == authority_path and not changed:
                changed = True
                authority_path.write_bytes(raw + b"\nChanged after observation.\n")
            return raw

        with patch.object(scoped.admission.ReadContext, "read", read):
            with self.assertRaises(scoped.admission.ProposedCarrierError):
                self.validate()
        self.assertTrue(changed)

    def test_parent_change_after_observation_refuses(self):
        parent = self.parent()
        original = scoped.admission.ReadContext.read
        changed = False

        def read(reader, path, *args, **kwargs):
            nonlocal changed
            raw = original(reader, path, *args, **kwargs)
            if Path(path) == parent and not changed:
                changed = True
                parent.write_bytes(raw + b"\nChanged after observation.\n")
            return raw

        with patch.object(scoped.admission.ReadContext, "read", read):
            with self.assertRaises(scoped.admission.ProposedCarrierError):
                self.validate()
        self.assertTrue(changed, "The placement check must observe its parent Carrier.")


if __name__ == "__main__":
    unittest.main()
