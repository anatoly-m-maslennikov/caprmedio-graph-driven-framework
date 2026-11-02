"""Nested Operations stay in their owner, not every enclosing Scope Unit."""
from pathlib import Path
import unittest

import test_nested_operation_placement_independent as nested
from project_selection import bind_selection, resolve_project
from scope_declaration_test_support import write_scope_unit_declarations

admission = nested.scoped.admission


class OperationsOwnerBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = nested.NestedOperationPlacementIndependentTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.control = self.fixture.root, self.fixture.control
        self.owner = self.role_root = self.path = None
        self.rows = [
            ("FRAMEWORK_METHODOLOGY", "PROJECT"),
            ("METHODOLOGY_SOURCES", "FRAMEWORK_METHODOLOGY"),
            ("CORE_META_MODEL", "METHODOLOGY_SOURCES"),
        ]

    def context(self, extra=()):
        for path in (self.root / self.control).rglob("*.md"):
            if "Scope Unit Declaration" in path.read_text(encoding="utf-8"):
                path.unlink()
        rows = tuple(
            {"scope_unit_name": name, "parent": parent, "scope_unit_label": "Layer"}
            for name, parent in (*self.rows, *extra)
        )
        declared = write_scope_unit_declarations(
            self.root, rows, control_root=self.root / self.control,
        )
        self.owner = declared["CORE_META_MODEL"]["authority_path"]
        self.role_root = self.owner / "09_operations"
        self.path = self.role_root / "workflow/step.md"
        self.fixture.fixture.fixture.put(
            self.role_root / "workflow.md",
            self.fixture.raw(atom_id="CA-O-721", type="Workflow",
                             current_scope_unit="CORE_META_MODEL", claim_target_scope_unit="CORE_META_MODEL"),
        )
        selection = resolve_project(self.root)
        with bind_selection(selection):
            return admission.source_context_from_project(self.root)

    def validate(self, context):
        parsed = nested.parse_carrier(
            self.fixture.raw(current_scope_unit="CORE_META_MODEL", claim_target_scope_unit="CORE_META_MODEL"),
            self.root / self.path,
        )
        return admission.validate_proposed_carrier(
            parsed.metadata, parsed.body, context, self.path.relative_to(self.root / self.control),
            reference_roles=nested.scoped.PRMEDO,
        )

    def test_declared_scope_ancestors_do_not_disown_nested_step(self):
        context = self.context()
        result = self.validate(context)
        self.assertEqual(([], []), (result["findings"], result["gaps"]))

    def test_nested_foreign_scope_still_refuses(self):
        context = self.context([("FOREIGN", "CORE_META_MODEL")])
        foreign = Path(next(
            row["authority_path"] for row in context.inputs["structure"]["scope_units"]
            if row["scope_unit_name"] == "FOREIGN"
        ))
        self.role_root = self.root / foreign / "09_operations"
        self.path = self.role_root / "workflow/step.md"
        self.fixture.fixture.fixture.put(
            self.role_root / "workflow.md",
            self.fixture.raw(atom_id="CA-O-721", type="Workflow",
                             current_scope_unit="CORE_META_MODEL", claim_target_scope_unit="CORE_META_MODEL"),
        )
        with self.assertRaisesRegex(admission.ProposedCarrierError, "crosses a declared Scope Unit"):
            self.validate(context)

    def test_equal_authority_path_with_foreign_name_still_refuses(self):
        context = self.context()
        # Direct guard control: ambiguous Structure is not silently accepted even
        # if an upstream declaration check supplied duplicate owner roots.
        rows = [*context.inputs["structure"]["scope_units"],
                {"scope_unit_name": "FOREIGN", "authority_path": self.owner.as_posix()}]
        metadata = self.fixture.metadata(current_scope_unit="CORE_META_MODEL", claim_target_scope_unit="CORE_META_MODEL")
        with self.assertRaisesRegex(admission.ProposedCarrierError, "crosses a declared Scope Unit"):
            admission._operations_placement(
                context, metadata, self.path, self.role_root, "CORE_META_MODEL", rows, self.owner,
            )


if __name__ == "__main__":
    unittest.main()
