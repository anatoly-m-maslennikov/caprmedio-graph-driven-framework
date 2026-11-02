"""Regression checks for source-bound lifecycle dispatch."""

from __future__ import annotations

from pathlib import Path
import sys
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
if str(APP) not in sys.path:
    sys.path.insert(0, str(APP))

from selected_lifecycle_dispatch import (  # noqa: E402
    dispatch_lifecycle_action,
    ordinary_lifecycle_result,
)


class SelectedLifecycleDispatchTests(unittest.TestCase):
    def test_generic_fallback_keeps_only_changed_effects_and_prior_revision(self) -> None:
        def action(root: Path, parameters: dict[str, object], **call: object) -> dict[str, object]:
            del root, parameters, call
            return {
                "outcome": "applied",
                "effects": [
                    {"state": "unchanged", "carrier": {"path": "unchanged.md"}},
                    {"state": "unknown", "carrier": {"path": "unknown.md"}},
                    {"carrier": {"path": "missing-state.md"}},
                    "string-entry.md",
                    None,
                    17,
                    {"state": "changed", "carrier": {"path": "actual.md"}},
                    {"state": "changed", "path": "direct.md"},
                ],
                "history": {"prior_revision": {"path": "prior.md"}},
            }

        result = ordinary_lifecycle_result(
            Path("/tmp/project"), {"parameters": {}}, action, {"execute": True}
        )

        self.assertEqual(["actual.md", "direct.md", "prior.md"], result["effect_refs"])

    def test_nested_routes_return_canonical_helper_output_unchanged(self) -> None:
        context = {
            "route": "create_atom",
            "creation_requested_run_id": "child",
            "parameters": {},
        }
        expected = {"result": "no_op", "terminal_outcome": "no_op"}
        with patch(
            "selected_lifecycle_dispatch.execute_creation_atom", return_value=expected
        ) as creation:
            result = dispatch_lifecycle_action(
                Path("/tmp/project"), context, lambda *args, **kwargs: {}, {}
            )

        self.assertIs(result, expected)
        creation.assert_called_once()

        status_context = {
            "route": "change_atom_status",
            "lifecycle_current_state": True,
            "parameters": {},
        }
        status_expected = {"result": "no_op", "terminal_outcome": "no_op"}
        with patch(
            "selected_lifecycle_dispatch.execute_lifecycle_status_change_atom",
            return_value=status_expected,
        ) as status:
            result = dispatch_lifecycle_action(
                Path("/tmp/project"), status_context, lambda *args, **kwargs: {}, {}
            )

        self.assertIs(result, status_expected)
        status.assert_called_once()


if __name__ == "__main__":
    unittest.main()
