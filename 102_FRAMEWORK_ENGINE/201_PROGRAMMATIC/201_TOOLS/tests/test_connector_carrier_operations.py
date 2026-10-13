from __future__ import annotations

import dataclasses
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from types import SimpleNamespace

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from connector_carrier_reading import Location, observe
from connector_carrier_writing import CarrierPlan, execute
from connector_carrier_adapter import modify
from connector_bindings import ConnectorBindingError, ConnectorBindings


class CarrierTests(unittest.TestCase):
    def setUp(self):
        self.scratch = TOOLS.parents[2] / ".caprmedio_tmp"
        # Every deletion in this suite is confined to its newly created fixture.
        self.scratch.mkdir(exist_ok=True)
        self.fixture = tempfile.TemporaryDirectory(prefix="carrier-fixture-", dir=self.scratch)
        self.project = Path(self.fixture.name)
        self.root = self.project / "owned"
        self.root.mkdir()
        self.target = {"kind": "Artifact/Carrier", "identity": "scratch-carrier"}
        self.calls = []

    def tearDown(self):
        self.fixture.cleanup()

    def admit(self, plan):
        self.calls.append(plan.variant)

    def location(self, name):
        return Location(self.root, name)

    def file(self, name, content=b"untouched\n"):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return self.location(name)

    def plan(self, variant="rename", source=None, destination=None, inventory=None, **changes):
        source = source or self.file("source.txt")
        destination = None if variant == "remove" else destination or self.location("destination.txt")
        values = dict(
            variant=variant, project_root=self.project, source_binding=source,
            expected_source=observe(source, inventory), destination_binding=destination,
            expected_destination=None if destination is None else observe(destination, inventory if source == destination else None),
            entry_inventory=inventory, preservation_frontier=(), storage_owner=self,
            classification="approved_non_atom_cleanup" if variant == "remove" else "owned_non_atom",
            admission_evidence=self.admit,
        )
        return CarrierPlan(**(values | changes))

    def run_plan(self, plan):
        return execute(plan, logical_target=self.target)

    def test_exact_file_rename_move_and_preservation(self):
        protected = self.file("referrer.txt", b"source.txt stays as text\n")
        source = self.file("source.txt", b"actual bytes\x00\xff")
        os.chmod(self.root / "source.txt", 0o640)
        (self.root / "destination").mkdir()
        for variant, destination in (("rename", "renamed.txt"), ("move", "destination/explicit-name.txt")):
            plan = self.plan(variant, source, self.location(destination),
                             preservation_frontier=((protected, observe(protected)),))
            result = self.run_plan(plan)
            self.assertEqual(result["errors"], [])
            self.assertFalse((self.root / source.relative).exists())
            self.assertEqual((self.root / destination).read_bytes(), b"actual bytes\x00\xff")
            self.assertEqual((self.root / destination).stat().st_mode & 0o777, 0o640)
            self.assertEqual((self.root / "referrer.txt").read_bytes(), b"source.txt stays as text\n")
            self.assertEqual(result["effects"][0]["state"], "known")
            self.assertNotIn(str(self.project), str(result))
            source = self.location(destination)

    def test_folder_rename_and_move_with_exact_inventory(self):
        source = self.file("folder/entry.txt", b"approved")
        child = observe(source)["entry"]
        inventory = {"entry.txt": child}
        source = self.location("folder")
        (self.root / "other").mkdir()
        for variant, name in (("rename", "renamed"), ("move", "other/explicit")):
            result = self.run_plan(self.plan(variant, source, self.location(name), inventory))
            self.assertEqual(result["errors"], [])
            self.assertEqual((self.root / name / "entry.txt").read_bytes(), b"approved")
            source = self.location(name)

    def test_remove_exact_file_empty_folder_and_expected_absence(self):
        source = self.file("cleanup.txt")
        result = self.run_plan(self.plan("remove", source))
        self.assertEqual(result["errors"], [])
        self.assertFalse((self.root / source.relative).exists())
        self.assertEqual(result["effects"][0]["state"], "known")
        (self.root / "empty").mkdir()
        source = self.location("empty")
        result = self.run_plan(self.plan("remove", source, inventory={}))
        self.assertEqual(result["errors"], [])
        self.assertFalse((self.root / "empty").exists())
        result = self.run_plan(self.plan("remove", source, inventory={}))
        self.assertEqual(result["errors"], [])
        self.assertTrue(result["data"]["no_op"])
        self.assertEqual(result["effects"], [])

    def test_same_binding_noop_requires_exact_state(self):
        source = self.file("same.txt")
        for variant in ("rename", "move"):
            result = self.run_plan(self.plan(variant, source, source))
            self.assertEqual(result["errors"], [])
            self.assertEqual(result["effects"], [])
            self.assertTrue(result["data"]["no_op"])

    def test_refusals_are_effect_free(self):
        source = self.file("source.txt")
        (self.root / "other").mkdir()
        plan = self.plan(source=source)
        cases = [
            dataclasses.replace(plan, variant="recursive"),
            dataclasses.replace(plan, storage_owner=None),
            dataclasses.replace(plan, admission_evidence=None),
            dataclasses.replace(plan, source_binding=Location(self.project, "owned/source.txt")),
            dataclasses.replace(plan, source_binding=self.location("../outside")),
            dataclasses.replace(plan, source_binding=self.location(".")),
            dataclasses.replace(plan, destination_binding=self.location("source.txt/child")),
            dataclasses.replace(plan, destination_binding=self.location("other/name.txt")),
            dataclasses.replace(plan, expected_destination={"present": True}),
        ]
        for case in cases:
            with self.subTest(case=case):
                result = self.run_plan(case)
                self.assertTrue(result["errors"])
                self.assertEqual(result["effects"], [])
                self.assertEqual((self.root / "source.txt").read_bytes(), b"untouched\n")

    def test_missing_stale_collision_and_substituted_parent(self):
        for alteration in ("missing", "content", "collision", "parent"):
            with self.subTest(alteration=alteration):
                source = self.file("source.txt")
                plan = self.plan(source=source)
                if alteration == "missing":
                    (self.root / "source.txt").unlink()
                elif alteration == "content":
                    (self.root / "source.txt").write_bytes(b"changed")
                elif alteration == "collision":
                    self.file("destination.txt", b"occupied")
                else:
                    self.file("unlisted.txt")
                result = self.run_plan(plan)
                self.assertTrue(result["errors"])
                self.assertEqual(result["effects"], [])
                if alteration == "collision":
                    self.assertEqual((self.root / "destination.txt").read_bytes(), b"occupied")
                    (self.root / "destination.txt").unlink()
                if alteration == "parent":
                    (self.root / "unlisted.txt").unlink()

    def test_symlink_source_ancestor_and_destination(self):
        source = self.file("source.txt")
        plan = self.plan(source=source)
        (self.root / "alias").symlink_to(self.root, target_is_directory=True)
        for location in (self.location("alias/source.txt"), self.location("alias")):
            result = self.run_plan(dataclasses.replace(plan, source_binding=location))
            self.assertTrue(result["errors"])
            self.assertEqual(result["effects"], [])
        (self.root / "destination.txt").symlink_to(self.root / "source.txt")
        result = self.run_plan(plan)
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"], [])
        self.assertEqual((self.root / "source.txt").read_bytes(), b"untouched\n")

    def test_folder_frontier_changes_and_nonempty_removal_are_rejected(self):
        child = self.file("folder/entry.txt")
        inventory = {"entry.txt": observe(child)["entry"]}
        plan = self.plan(source=self.location("folder"), inventory=inventory)
        self.file("folder/unlisted.txt")
        result = self.run_plan(plan)
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"], [])
        remove = dataclasses.replace(plan, variant="remove", destination_binding=None,
                                     expected_destination=None, entry_inventory={},
                                     classification="approved_non_atom_cleanup")
        result = self.run_plan(remove)
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"], [])
        self.assertTrue((self.root / "folder/entry.txt").exists())

    def test_orphan_inventory_and_effect_boundary_collision_are_rejected(self):
        (self.root / "empty").mkdir()
        with self.assertRaises(ValueError):
            observe(self.location("empty"), {"missing/child": {}})
        plan = self.plan()
        from connector_carrier_writing import _move
        def collision(source_parent, source_name, destination_parent, destination_name):
            self.file("destination.txt", b"late collision")
            return _move(source_parent, source_name, destination_parent, destination_name)
        with patch("connector_carrier_writing._move", side_effect=collision):
            result = self.run_plan(plan)
        self.assertEqual(result["errors"][0]["code"], "stale_state")
        self.assertEqual(result["effects"], [])
        self.assertEqual((self.root / "source.txt").read_bytes(), b"untouched\n")
        self.assertEqual((self.root / "destination.txt").read_bytes(), b"late collision")

    def test_removal_never_accepts_atom_history_protected_or_uncertain_classification(self):
        source = self.file("carrier.md", b"---\natom_id: CA-R-123\n---\n")
        plan = self.plan("remove", source)
        for classification in ("atom", "historical_atom", "required_history", "protected_source", "unknown", "owned_non_atom"):
            result = self.run_plan(dataclasses.replace(plan, classification=classification))
            self.assertEqual(result["errors"][0]["code"], "permission_denied")
            self.assertEqual(result["effects"], [])
            self.assertTrue((self.root / "carrier.md").exists())
        result = self.run_plan(plan)
        self.assertEqual(result["errors"][0]["code"], "permission_denied")
        self.assertEqual(result["effects"], [])
        self.assertTrue((self.root / "carrier.md").exists())

    def test_admission_rechecked_and_effect_readback_failure_is_truthful(self):
        source = self.file("source.txt")
        plan = self.plan(source=source)
        def fail_readback(location, inventory=None):
            if (self.root / "destination.txt").exists():
                raise OSError("injected readback failure")
            return observe(location, inventory)
        with patch("connector_carrier_writing.observe", side_effect=fail_readback):
            result = self.run_plan(plan)
        self.assertTrue(result["errors"])
        self.assertEqual(result["effects"][0]["state"], "known")
        self.assertFalse((self.root / "source.txt").exists())
        self.assertEqual((self.root / "destination.txt").read_bytes(), b"untouched\n")
        self.assertGreaterEqual(len(self.calls), 2)

    def test_unknown_effect_has_uncertain_error_and_no_retry(self):
        plan = self.plan()
        with patch("connector_carrier_writing._move", side_effect=OSError("injected effect failure")) as move:
            result = self.run_plan(plan)
        self.assertEqual(move.call_count, 1)
        self.assertEqual(result["effects"][0]["state"], "unknown")
        self.assertIn("effect_uncertain", [item["code"] for item in result["errors"]])

    def test_adapter_has_no_unbound_physical_route(self):
        result = modify({"operation": "modify", "target": {"path": "source.txt"}},
                        bindings=None, resolve_plan=lambda bound: self.plan())
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["errors"][0]["code"], "input_invalid")
        self.assertEqual(result["current_state"], None)

    def test_adapter_preserves_admission_callback_refusal(self):
        plan = self.plan(admission_evidence=lambda current: False)
        request = {"operation": "modify", "target": self.target, "query": None,
                   "delta": {"explicit": "fixture"}, "expected_state": {"fixture": "before"},
                   "authorization": "fixture", "context": "fixture"}
        # Isolate callback propagation; this stand-in does not prove real admission.
        bound = SimpleNamespace(request=request, revalidate_before_effect=lambda: None)
        bindings = object.__new__(ConnectorBindings)
        with patch.object(bindings, "bind", return_value=bound):
            result = modify(request, bindings=bindings, resolve_plan=lambda current: plan)
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["errors"][0]["code"], "permission_denied")
        self.assertTrue((self.root / "source.txt").exists())
        self.assertFalse((self.root / "destination.txt").exists())

    def test_writer_retains_permission_denial_code_and_field(self):
        def refuse(plan):
            raise ConnectorBindingError("permission_denied", "Actual recheck refusal", "authorization")
        result = self.run_plan(self.plan(admission_evidence=refuse))
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["errors"][0]["code"], "permission_denied")
        self.assertEqual(result["errors"][0]["field"], "authorization")
        self.assertTrue((self.root / "source.txt").exists())


if __name__ == "__main__":
    unittest.main()
