"""Nested Operations stay in their owner, not every enclosing Scope Unit."""
import unittest

import test_nested_operation_placement_independent as nested
from project_selection import bind_selection, resolve_project

admission = nested.scoped.admission


class OperationsOwnerBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.fixture = nested.NestedOperationPlacementIndependentTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.control = self.fixture.root, self.fixture.control
        self.owner = self.control / "101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL"
        self.role_root = self.owner / "09_operations"
        self.path = self.role_root / "workflow/step.md"
        self.fixture.fixture.fixture.put(
            self.role_root / "workflow.md",
            self.fixture.raw(atom_id="CA-O-721", type="Workflow",
                             current_scope_unit="CORE_META_MODEL", claim_target_scope_unit="CORE_META_MODEL"),
        )
        self.rows = [
            ("FRAMEWORK_METHODOLOGY", "PROJECT", self.owner.parents[1]),
            ("METHODOLOGY_SOURCES", "FRAMEWORK_METHODOLOGY", self.owner.parent),
            ("CORE_META_MODEL", "METHODOLOGY_SOURCES", self.owner),
        ]

    def context(self, extra=()):
        rows = [*self.rows, *extra]
        text = "schema_version = 1\n"
        for index, (name, parent, path) in enumerate(rows, 1):
            text += (
                f'[[scope_units]]\nscope_unit_name = "{name}"\nparent = "{parent}"\n'
                'scope_unit_type = "Unordered"\nscope_unit_label = "Layer"\n'
                f'structural_level = {min(index, 4)}\nnavigational_order_number = 0\n'
                f'authority_path = "{path.as_posix()}"\ndelivery_path = "native/{name}"\n'
            )
        (self.root / self.control / "project_structure.toml").write_text(text)
        selection = resolve_project(self.root)
        with bind_selection(selection):
            return admission.source_context_from_project(self.root)

    def validate(self, context):
        parsed = nested.parse_carrier(
            self.fixture.raw(current_scope_unit="CORE_META_MODEL", claim_target_scope_unit="CORE_META_MODEL"),
            self.root / self.path,
        )
        return admission.validate_proposed_carrier(
            parsed.metadata, parsed.body, context, self.path.relative_to(self.control),
            reference_roles=nested.scoped.PRMEDO,
        )

    def test_declared_scope_ancestors_do_not_disown_nested_step(self):
        context = self.context()
        result = self.validate(context)
        self.assertEqual(([], []), (result["findings"], result["gaps"]))

    def test_nested_foreign_scope_still_refuses(self):
        context = self.context([("FOREIGN", "CORE_META_MODEL", self.role_root / "workflow")])
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
