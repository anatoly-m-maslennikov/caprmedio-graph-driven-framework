"""Retired public selected-session requests cannot fall through to execution."""
from __future__ import annotations

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))

from selected_execution import SelectedExecutionError  # noqa: E402
from selected_native_providers import SelectedNativeProviders  # noqa: E402


class SelectedPublicDispatchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.frozen = {
            "request": {"run_id": "public-fixture", "execution": {
                "operation_route": "public.release", "parameters": {},
            }},
        }
        self.providers = SelectedNativeProviders(self.root, implementation_agent=lambda *_args: {})

    def test_retired_selected_session_provider_refuses_without_starting_a_run(self) -> None:
        with patch("selected_native_providers.SelectedExecution", side_effect=AssertionError("generic start")) as generic:
            with self.assertRaisesRegex(
                SelectedExecutionError,
                "Release selected-session providers are disabled; use direct Release commands",
            ):
                self.providers.execution(self.frozen)
        generic.assert_not_called()
        self.assertEqual([], list(self.root.iterdir()))

    def test_ordinary_route_keeps_its_existing_provider(self) -> None:
        self.frozen["request"]["execution"]["operation_route"] = "create_atom"
        with patch("selected_native_providers.SelectedExecution") as generic:
            result = self.providers.execution(self.frozen)
        self.assertIs(result, generic.return_value)
        self.assertEqual(self.root, generic.call_args.args[0])
        self.assertEqual({"CA-O-131"}, set(generic.call_args.kwargs["handlers"]))
        self.assertIs(self.providers.implementation_agent, generic.call_args.kwargs["implementation_agent"])

if __name__ == "__main__":
    unittest.main()
