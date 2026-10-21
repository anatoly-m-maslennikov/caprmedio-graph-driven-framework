"""Focused pure checks for source-bound contained lifecycle admission."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import call, patch


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from contained_atom_targets import ContainedAtomInventory, ContainedAtomTarget  # noqa: E402
from container_lifecycle_admission import (  # noqa: E402
    ContainerLifecycleAdmissionError,
    seal_contained_status_changes,
)
from VALIDATE_ATOMS.validate_atoms_workers.proposed_references import TargetCarrier  # noqa: E402


ROOT = Path("/tmp/container-lifecycle-admission")
PARENT_PATH = ".caprmedio_caprmedio/fixture/03_plan/01-CA-P-701-EPIC--parent.md"
PARENT_DIGEST = "a" * 64


def _prior(*, role: str = "Plan", atom_type: str = "Plan", digest: str = PARENT_DIGEST) -> dict[str, object]:
    return {
        "atom_id": "CA-P-701" if role == "Plan" else "CA-O-701",
        "path": PARENT_PATH,
        "filename": Path(PARENT_PATH).name,
        "version": 1,
        "digest": digest,
        "lifecycle": "active",
        "status": "Active",
        "updated_at": "2026-01-01 00:00:00 +0000",
        "content_role": role,
        "type": atom_type,
    }


def _admission(prior: dict[str, object], requested: str = "Archived") -> dict[str, object]:
    return {
        "operation": "change_status",
        "prior": prior,
        "requested_status": requested,
        "current_status": "Active",
        "status_model": {
            "content_role": prior["content_role"],
            "type": prior["type"],
            "statuses": ["Active", "Archived", "Done", "Canceled"],
            "requested_status": requested,
        },
        "archive": requested == "Archived",
    }


def _parent_carrier(prior: dict[str, object], *, digest: str | None = None) -> TargetCarrier:
    return TargetCarrier(
        str(prior["atom_id"]),
        str(prior["status"]),
        int(prior["version"]),
        str(prior["path"]),
        digest or str(prior["digest"]),
        {
            "atom_id": prior["atom_id"],
            "content_role": prior["content_role"],
            "type": prior["type"],
            "status": prior["status"],
            "version": prior["version"],
        },
    )


def _target(atom_id: str, parent: str, path: str, *, role: str = "Plan") -> ContainedAtomTarget:
    return ContainedAtomTarget(
        atom_id, role, "Plan" if role == "Plan" else "Step", "Active", 1,
        path, atom_id[0].lower() * 64, parent, path, None,
    )


def _descriptor(target: ContainedAtomTarget) -> dict[str, object]:
    return {
        "atom_id": target.atom_id,
        "path": target.path,
        "filename": Path(target.path).name,
        "version": target.version,
        "digest": target.sha256,
        "lifecycle": "active",
        "status": target.status,
        "updated_at": "2026-01-01 00:00:00 +0000",
        "content_role": target.content_role,
        "type": target.atom_type,
    }


class ContainerLifecycleAdmissionTests(unittest.TestCase):
    def test_seals_deepest_first_with_independent_native_child_preflights(self):
        prior = _prior()
        child = _target("CA-P-702", "CA-P-701", PARENT_PATH[:-3] + "child.md")
        grandchild = _target("CA-P-703", "CA-P-702", PARENT_PATH[:-3] + "grandchild.md")
        operation = _target(
            "CA-O-704", "CA-P-701", ".caprmedio_caprmedio/fixture/09_operations/step.md", role="Operations"
        )
        inventory = ContainedAtomInventory(
            _parent_carrier(prior), (child, operation, grandchild),
        )
        parent_admission = _admission(prior, "Done")
        requests: list[dict[str, object]] = []

        def descriptor(_root: Path, selector: str) -> dict[str, object]:
            target = next(item for item in inventory.targets if item.path == selector)
            return _descriptor(target)

        def preflight(_root: Path, operation_name: str, request: dict[str, object]) -> dict[str, object]:
            self.assertEqual("change_status", operation_name)
            requests.append(request)
            target = request["target"]
            self.assertIsInstance(target, dict)
            return _admission(dict(target), str(request["status"]))

        with (
            patch(
                "container_lifecycle_admission.source_context_from_project",
                return_value=SimpleNamespace(_reader=object(), _selection=object()),
            ) as context,
            patch("container_lifecycle_admission.discover_contained_atom_targets", return_value=inventory) as discover,
            patch("container_lifecycle_admission._current"),
            patch("container_lifecycle_admission.lifecycle_intents.carrier_descriptor", side_effect=descriptor),
            patch("container_lifecycle_admission.lifecycle_intents.preflight_atom_lifecycle", side_effect=preflight) as native,
        ):
            seal = seal_contained_status_changes(
                ROOT, {"target": prior, "status": "Done"}, parent_admission,
            )

        self.assertIsNotNone(seal)
        assert seal is not None
        self.assertEqual(
            ["CA-P-703", "CA-P-702", "CA-O-704"],
            [row["target"]["atom_id"] for row in seal["descendants"]],
        )
        self.assertEqual(
            ["Canceled", "Canceled", "Done"],
            [row["status"] for row in seal["descendants"]],
        )
        self.assertEqual(
            ("operation", "prior", "requested_status", "current_status", "status_model", "archive"),
            tuple(seal["parent"]),
        )
        self.assertEqual(3, native.call_count)
        self.assertEqual(3, len(requests))
        self.assertEqual(["Canceled", "Canceled", "Done"], [request["status"] for request in requests])
        self.assertTrue(all(set(request["target"]) == {
            "atom_id", "path", "filename", "version", "digest", "lifecycle", "status",
            "updated_at", "content_role", "type",
        } for request in requests))
        context.assert_called_once_with(ROOT.resolve())
        self.assertEqual(2, discover.call_count)
        self.assertEqual(discover.call_args_list[0], discover.call_args_list[1])
        self.assertEqual(discover.call_args_list[0], call(
            context.return_value,
            "CA-P-701",
            expected_version=1,
            expected_sha256=PARENT_DIGEST,
        ))
        json.dumps(seal)

    def test_noncontainer_parent_returns_none_without_source_discovery(self):
        prior = _prior(role="Requirement", atom_type="Requirement")
        parent_admission = _admission(prior)
        with (
            patch("container_lifecycle_admission.source_context_from_project") as context,
            patch("container_lifecycle_admission.discover_contained_atom_targets") as discover,
        ):
            self.assertIsNone(seal_contained_status_changes(ROOT, {"status": "Archived"}, parent_admission))
        context.assert_not_called()
        discover.assert_not_called()

    def test_empty_container_inventory_returns_none_after_parent_binding(self):
        prior = _prior()
        inventory = ContainedAtomInventory(_parent_carrier(prior), ())
        with (
            patch(
                "container_lifecycle_admission.source_context_from_project",
                return_value=SimpleNamespace(_reader=object(), _selection=object()),
            ),
            patch("container_lifecycle_admission.discover_contained_atom_targets", return_value=inventory),
            patch("container_lifecycle_admission.lifecycle_intents.preflight_atom_lifecycle") as native,
        ):
            self.assertIsNone(seal_contained_status_changes(ROOT, {"status": "Archived"}, _admission(prior)))
        native.assert_not_called()

    def test_parent_snapshot_drift_refuses_instead_of_returning_none(self):
        prior = _prior()
        inventory = ContainedAtomInventory(_parent_carrier(prior, digest="b" * 64), ())
        with (
            patch(
                "container_lifecycle_admission.source_context_from_project",
                return_value=SimpleNamespace(_reader=object(), _selection=object()),
            ),
            patch("container_lifecycle_admission.discover_contained_atom_targets", return_value=inventory),
        ):
            with self.assertRaises(ContainerLifecycleAdmissionError):
                seal_contained_status_changes(ROOT, {"status": "Archived"}, _admission(prior))

    def test_nonhex_parent_digest_refuses_before_discovery(self):
        prior = _prior(digest="z" * 64)
        with (
            patch("container_lifecycle_admission.source_context_from_project") as context,
            patch("container_lifecycle_admission.discover_contained_atom_targets") as discover,
        ):
            with self.assertRaises(ContainerLifecycleAdmissionError):
                seal_contained_status_changes(ROOT, {"status": "Archived"}, _admission(prior))
        context.assert_not_called()
        discover.assert_not_called()

    def test_valid_container_source_error_refuses_instead_of_returning_none(self):
        prior = _prior()
        with patch(
            "container_lifecycle_admission.source_context_from_project",
            side_effect=ValueError("source unavailable"),
        ):
            with self.assertRaises(ContainerLifecycleAdmissionError):
                seal_contained_status_changes(ROOT, {"status": "Archived"}, _admission(prior))

    def test_child_snapshot_drift_refuses_before_native_preflight(self):
        prior = _prior()
        target = _target("CA-P-702", "CA-P-701", PARENT_PATH[:-3] + "child.md")
        inventory = ContainedAtomInventory(_parent_carrier(prior), (target,))
        stale = _descriptor(target)
        stale["digest"] = "f" * 64
        with (
            patch("container_lifecycle_admission.source_context_from_project", return_value=object()),
            patch("container_lifecycle_admission.discover_contained_atom_targets", return_value=inventory),
            patch("container_lifecycle_admission.lifecycle_intents.carrier_descriptor", return_value=stale),
            patch("container_lifecycle_admission.lifecycle_intents.preflight_atom_lifecycle") as native,
        ):
            with self.assertRaises(ContainerLifecycleAdmissionError):
                seal_contained_status_changes(ROOT, {"status": "Archived"}, _admission(prior))
        native.assert_not_called()

    def test_frontier_drift_after_child_admission_refuses_before_return(self):
        prior = _prior()
        target = _target("CA-P-702", "CA-P-701", PARENT_PATH[:-3] + "child.md")
        initial = ContainedAtomInventory(_parent_carrier(prior), (target,))
        drifted_target = ContainedAtomTarget(
            target.atom_id, target.content_role, target.atom_type, target.status,
            target.version, target.path, "e" * 64, target.parent_atom_id,
            target.container_path, target.directory_path,
        )
        drifted = ContainedAtomInventory(_parent_carrier(prior), (drifted_target,))

        def descriptor(_root: Path, selector: str) -> dict[str, object]:
            self.assertEqual(target.path, selector)
            return _descriptor(target)

        def preflight(_root: Path, _operation: str, request: dict[str, object]) -> dict[str, object]:
            return _admission(dict(request["target"]), str(request["status"]))

        with (
            patch(
                "container_lifecycle_admission.source_context_from_project",
                return_value=SimpleNamespace(_reader=object(), _selection=object()),
            ),
            patch(
                "container_lifecycle_admission.discover_contained_atom_targets",
                side_effect=[initial, drifted],
            ) as discover,
            patch("container_lifecycle_admission._current"),
            patch("container_lifecycle_admission.lifecycle_intents.carrier_descriptor", side_effect=descriptor),
            patch("container_lifecycle_admission.lifecycle_intents.preflight_atom_lifecycle", side_effect=preflight),
        ):
            with self.assertRaises(ContainerLifecycleAdmissionError):
                seal_contained_status_changes(ROOT, {"status": "Archived"}, _admission(prior))
        self.assertEqual(2, discover.call_count)


if __name__ == "__main__":
    unittest.main()

