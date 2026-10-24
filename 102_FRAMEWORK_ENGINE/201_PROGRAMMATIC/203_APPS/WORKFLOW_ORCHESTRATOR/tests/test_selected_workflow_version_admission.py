"""Focused admission checks for reviewed O016 Workflow revisions."""

# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431

from __future__ import annotations

import copy
import hashlib
from pathlib import Path
import sys
from typing import Any, cast


APP = Path(__file__).resolve().parents[1]
TOOLS = APP.parents[1] / "201_TOOLS"
for location in (APP, APP / "tests", TOOLS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from selected_execution_contracts import SelectedExecutionError  # noqa: E402
from selected_integrated_entry import owns  # noqa: E402
from selected_integrated_dispatch import dispatch_integrated  # noqa: E402
from selected_integrated_dispatch_profile import profile_from_frozen  # noqa: E402
from selected_integrated_dispatch_test_support import (  # noqa: E402
    IntegratedDispatchTestCase,
    PendingProvider,
)  # noqa: E402
from selected_execution_run_plan import build_requested_runs  # noqa: E402
from shared_context_direct_fixture import DirectSharedContextFixture  # noqa: E402
from shared_context_packets import ACTIONS  # noqa: E402
from shared_context_validation_sources import (  # noqa: E402
    CURRENT_DIRECT_WORKFLOW_VERSIONS,
    WORKFLOW_VERSION_PROFILES,
    is_current_shared_workflow_profile,
    workflow_version_profile,
)  # noqa: E402
from workflow_run_support import _canonical_digest  # noqa: E402


def _metadata_only_o016_v20(frozen: dict[str, Any], root: Any) -> dict[str, Any]:
    """Derive O016@20 in a disposable Project from the frozen O016@18 bytes."""

    adapted = copy.deepcopy(frozen)
    workflow = adapted["graph"]["workflow"]
    source = root / workflow["path"]
    raw = source.read_bytes()
    updated = raw.replace(b"version: 18\n", b"version: 20\n", 1)
    if updated == raw:
        raise AssertionError("the frozen O016@18 source did not contain its version marker")
    source.write_bytes(updated)
    digest = hashlib.sha256(updated).hexdigest()
    workflow["version"] = 20
    workflow["sha256"] = digest
    parameters = adapted["request"]["execution"]["parameters"]
    bindings = parameters["base_packet"]["source_bindings"]
    for binding in bindings:
        if binding.get("atom_id") == "CA-O-016":
            binding["version"] = 20
            binding["sha256"] = digest
    references = parameters["base_packet"]["selected_project"]["source_references"]
    for reference in references:
        if reference.get("atom_id") == "CA-O-016":
            reference["version"] = 20
            reference["sha256"] = digest
    execution = adapted["request"]["execution"]
    execution["parameters_digest"] = _canonical_digest(parameters)
    execution["requested_runs"] = build_requested_runs(
        adapted["graph"],
        str(adapted["request"]["run_id"]),
        parameters["run_visit_limits"],
    )
    execution["operator_authorization"]["parameters_digest"] = execution["parameters_digest"]
    proposal = execution["proposal_receipt"]
    proposal["parameters_digest"] = execution["parameters_digest"]
    execution["proposal_receipt_digest"] = _canonical_digest(proposal)
    execution["operator_authorization"]["proposal_receipt_digest"] = execution[
        "proposal_receipt_digest"
    ]
    return adapted


class SelectedWorkflowVersionAdmissionTests(IntegratedDispatchTestCase):
    fixture_loader = DirectSharedContextFixture

    def test_version_profile_map_is_exact_and_does_not_admit_newer_versions(self) -> None:
        self.assertEqual(
            {17: "legacy_projection", 18: "direct_methods", 20: "direct_methods"},
            WORKFLOW_VERSION_PROFILES,
        )
        self.assertEqual({18, 20}, set(CURRENT_DIRECT_WORKFLOW_VERSIONS))
        self.assertIsNone(workflow_version_profile(19))
        self.assertIsNone(workflow_version_profile(21))

    def test_o016_v20_direct_path_reaches_the_existing_pending_contract(self) -> None:
        frozen, tracker = self.frozen("integrated-v20")
        adapted = _metadata_only_o016_v20(frozen, self.root)
        provider = PendingProvider()

        result = dispatch_integrated(
            self.root,
            adapted,
            tracker=tracker,
            trusted_method_projection=None,
            trusted_methods=None,
            action=provider,
        )
        repeated = dispatch_integrated(
            self.root,
            adapted,
            tracker=tracker,
            trusted_method_projection=None,
            trusted_methods=None,
            action=provider,
        )

        self.assertEqual("started", result["disposition"])
        self.assertEqual("pending_action", result["status"])
        self.assertEqual(result, repeated)
        self.assertEqual(1, provider.calls)

    def test_legacy_and_unknown_profiles_keep_their_existing_boundaries(self) -> None:
        frozen, _tracker = self.frozen("version-boundaries")
        self.assertTrue(owns(frozen))
        self.assertTrue(is_current_shared_workflow_profile(self._profile(18)))

        legacy = cast(dict[str, Any], copy.deepcopy(frozen))
        legacy["graph"]["workflow"]["version"] = 17
        self.assertFalse(owns(legacy))
        self.assertTrue(is_current_shared_workflow_profile(self._profile(17)))

        for version in (19, 21):
            unknown = cast(dict[str, Any], copy.deepcopy(frozen))
            unknown["graph"]["workflow"]["version"] = version
            self.assertFalse(owns(unknown))
            self.assertFalse(is_current_shared_workflow_profile(self._profile(version)))
            with self.assertRaises(SelectedExecutionError):
                profile_from_frozen(self.root, unknown)

    def _profile(self, version: int) -> dict[str, Any]:
        pins = {row["atom_id"]: dict(row) for row in self.fixture.source_pins()}
        pins["CA-O-016"]["version"] = version
        return {
            "workflow": pins["CA-O-016"],
            "entry_step": "CA-O-231",
            "steps": {
                step: {"step": pins[step], "action": pins[action]}
                for step, action in ACTIONS.items()
            },
        }


if __name__ == "__main__":
    import unittest

    unittest.main()
