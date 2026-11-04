"""Current move changes containment without inventing target-scope metadata."""
import unittest

import yaml
import test_atom_move_lifecycle
from lifecycle_intents import LifecycleError, move_atom_action


class CurrentMoveScopeTest(unittest.TestCase):
    def test_direct_scope_move_retains_subject_and_uses_canonical_containment(self):
        fixture = test_atom_move_lifecycle.AtomMoveLifecycleTest("runTest")
        fixture.setUp()
        try:
            destination = fixture._destination()
            before = yaml.safe_load(fixture.core_path.read_text().split("---", 2)[1])
            request = fixture._request(fixture.core_path, destination, "PROJECT_CONFIGURATION")
            request["placement"]["claim_target_scope_unit"] = "a-distinct-subject-target"
            result = move_atom_action(fixture.root, request, execute=True, authorized=True)
            after = yaml.safe_load(destination.read_text().split("---", 2)[1])
            self.assertEqual(result["outcome"], "applied")
            self.assertEqual(after["subjects"], before["subjects"])
            self.assertEqual(after["relations"]["IS_CONTAINED_BY"]["scope_unit"],
                             fixture.fixture.declarations["PROJECT_CONFIGURATION"]["scope_id"])
            self.assertNotIn("current_scope_unit", after)
            self.assertNotIn("claim_target_scope_unit", after)
        finally:
            fixture.tearDown()

    def test_present_destination_updates_only_successor_and_preserves_predecessor(self):
        fixture = test_atom_move_lifecycle.AtomMoveLifecycleTest("runTest")
        fixture.setUp()
        try:
            source = fixture.core_path
            destination = fixture._destination()
            original = source.read_text()
            old_directory = source.parent.relative_to(fixture.root).as_posix()
            original = original.replace("subjects:\n", f"carrier_destination:\n  file:\n    name: {source.name}\n    path: {old_directory}\nsubjects:\n", 1)
            source.write_text(original)
            before = source.read_bytes()
            request = fixture._request(source, destination, "PROJECT_CONFIGURATION")
            result = move_atom_action(fixture.root, request, execute=True, authorized=True)
            self.assertEqual(result["outcome"], "applied")
            archive = fixture.root / result["history"]["prior_revision"]["path"]
            current = yaml.safe_load(destination.read_text().split("---", 2)[1])
            self.assertEqual(current["carrier_destination"]["file"], {
                "name": destination.name, "path": destination.parent.relative_to(fixture.root).as_posix(),
            })
            self.assertEqual(archive.read_bytes(), before)
            historical = yaml.safe_load(archive.read_text().split("---", 2)[1])
            self.assertEqual(historical["carrier_destination"]["file"], {"name": source.name, "path": old_directory})
        finally:
            fixture.tearDown()

    def test_atom_contained_plan_refuses_implicit_reparent(self):
        fixture = test_atom_move_lifecycle.AtomMoveLifecycleTest("runTest")
        fixture.setUp()
        try:
            scope_id = fixture.fixture.declarations["LIFECYCLE_FIXTURE"]["scope_id"]
            fixture.fixture._plan_containment_atom(
                "CA-P-981", "parent", relations=f"relations:\n  IS_CONTAINED_BY:\n    scope_unit: {scope_id}")
            child = fixture.fixture._plan_containment_atom(
                "CA-P-982", "child", relations="relations:\n  IS_CONTAINED_BY:\n    atom: CA-P-981")
            destination = fixture.project_plans / "CA-P-982-PROJECT_CONFIGURATION--child.md"
            before = child.read_bytes()
            with self.assertRaisesRegex(LifecycleError, "parent-aware operation"):
                move_atom_action(fixture.root, fixture._request(child, destination, "PROJECT_CONFIGURATION"),
                                 execute=True, authorized=True)
            self.assertEqual(child.read_bytes(), before)
            self.assertFalse(destination.exists())
        finally:
            fixture.tearDown()


if __name__ == "__main__":
    unittest.main()
