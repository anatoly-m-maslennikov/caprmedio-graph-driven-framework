"""Frozen functional checks for the current shared-context packet validator."""

from __future__ import annotations

import copy
from pathlib import Path
import sys
import tempfile
from typing import Any
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = APP.parents[3]
for location in (APP, APP / "tests"):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from shared_context_current_fixture import CurrentSharedContextFixture  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402
from shared_context_validation import (  # noqa: E402
    SharedContextValidation,
    validate_current_shared_packet,
)
from shared_context_validation_sources import is_current_shared_workflow_profile  # noqa: E402


class SharedContextValidationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = CurrentSharedContextFixture.load()
        self.temporary = tempfile.TemporaryDirectory(
            dir=PROJECT_ROOT / ".caprmedio_tmp", ignore_cleanup_errors=True
        )
        self.addCleanup(self.temporary.cleanup)
        self.root = self.fixture.materialize(Path(self.temporary.name) / "project")
        self._materialize_support()
        pins = {pin["atom_id"]: dict(pin) for pin in self.fixture.source_pins()}
        self.trusted_methods = self.fixture.support_inventory["method_projection"]
        self.profile: dict[str, Any] = {
            "workflow": pins["CA-O-016"],
            "entry_step": "CA-O-231",
            "steps": {
                step: {"step": pins[step], "action": pins[action]}
                for step, action in ACTIONS.items()
            },
        }

    def _materialize_support(self) -> None:
        for row in self.fixture._support_rows():
            target = self.root / str(row["path"])
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(self.fixture.support_source_bytes(str(row["atom_id"])))

    def _packet(self, step: str = "CA-O-231") -> dict[str, Any]:
        parameters = self.fixture.native_implementation_parameters()
        return copy.deepcopy({**parameters["base_packet"], **parameters["step_packets"][step]})

    def _validate(self, packet: object, step: str = "CA-O-231") -> SharedContextValidation:
        row = self.profile["steps"][step]
        return validate_current_shared_packet(
            packet,
            workflow_definition=self.profile["workflow"],
            step_definition=row["step"],
            action_definition=row["action"],
            trusted_workflow_binding=self.profile,
            selected_project_root=self.root,
            trusted_method_projection=self.trusted_methods,
        )

    def test_current_o231_packet_is_source_bound_and_structured(self) -> None:
        result = self._validate(self._packet())
        self.assertTrue(result.accepted)
        self.assertEqual(
            {"status": "accepted", "warnings": [], "step_id": "CA-O-231", "action_id": "CA-O-017"},
            result.as_result(),
        )

    def test_profile_refuses_legacy_o091_and_untrusted_step_selection(self) -> None:
        self.assertTrue(is_current_shared_workflow_profile(self.profile))
        legacy = copy.deepcopy(self.profile)
        legacy["steps"] = {**legacy["steps"], "CA-O-091": legacy["steps"].pop("CA-O-231")}
        result = validate_current_shared_packet(
            self._packet(),
            workflow_definition=self.profile["workflow"],
            step_definition=self.profile["steps"]["CA-O-231"]["step"],
            action_definition=self.profile["steps"]["CA-O-231"]["action"],
            trusted_workflow_binding=legacy,
            selected_project_root=self.root,
        )
        self.assertFalse(result.accepted)
        self.assertEqual("profile", result.warnings[0]["code"])

    def test_profile_accepts_only_reviewed_legacy_and_direct_versions(self) -> None:
        direct = copy.deepcopy(self.profile)
        direct["workflow"]["version"] = 18
        self.assertTrue(is_current_shared_workflow_profile(direct))
        for version in (16, 19):
            rejected = copy.deepcopy(self.profile)
            rejected["workflow"]["version"] = version
            self.assertFalse(is_current_shared_workflow_profile(rejected))

    def test_boundary_preserves_absent_optional_fields(self) -> None:
        packet = self._packet()
        packet.pop("plan_item")
        absent = {"plan_item", "review_phase", "required_obligation_map", "operator_authorization"}
        with patch("shared_context_validation.validate_plan_candidate") as validate_plan:
            self.assertTrue(self._validate(packet).accepted)
        accepted_packet = validate_plan.call_args.args[0]
        self.assertTrue(absent.isdisjoint(accepted_packet))
        self.assertEqual(packet, accepted_packet)

    def test_stale_current_source_pin_is_an_invalid_packet_not_a_runtime_fault(self) -> None:
        packet = self._packet()
        packet["source_bindings"][1]["sha256"] = "0" * 64
        result = self._validate(packet)
        self.assertFalse(result.accepted)
        self.assertEqual("source_bindings", result.warnings[0]["code"])

    def test_full_method_projection_and_rmed_content_are_checked(self) -> None:
        packet = self._packet()
        packet["method_projection"]["content"] += "\nchanged"
        result = self._validate(packet)
        self.assertFalse(result.accepted)
        self.assertEqual("methods", result.warnings[0]["code"])

    def test_plan_candidate_and_permission_gaps_return_structured_warnings(self) -> None:
        for field, code in (
            ("candidate", "candidate"),
            ("permissions", "permissions"),
        ):
            with self.subTest(field=field):
                packet = self._packet()
                packet[field] = {} if field != "candidate" else ""
                result = self._validate(packet)
                self.assertFalse(result.accepted)
                self.assertEqual(code, result.warnings[0]["code"])
        plan = self._packet("CA-O-232")
        plan["plan_item"] = {}
        result = self._validate(plan, "CA-O-232")
        self.assertFalse(result.accepted)
        self.assertEqual("plan", result.warnings[0]["code"])

    def test_retry_and_review_inputs_are_gated_without_release_fallback(self) -> None:
        retry = self._packet("CA-O-096")
        retry["retry"]["consumed"] = retry["retry"]["effective_limit"]
        retry_result = self._validate(retry, "CA-O-096")
        self.assertTrue(retry_result.accepted)
        self.assertEqual("retry_blocked", retry_result.as_result()["status"])
        review = self._packet("CA-O-230")
        result = self._validate(review, "CA-O-230")
        self.assertFalse(result.accepted)
        self.assertEqual("review_phase", result.warnings[0]["code"])
        self.assertNotIn("release", result.as_result())


if __name__ == "__main__":
    unittest.main()
