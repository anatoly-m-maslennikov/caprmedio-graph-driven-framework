"""Contract tests for D588's private selected-source refresh host command."""
from __future__ import annotations

from contextlib import redirect_stderr
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch, sentinel


MCP = Path(__file__).resolve().parents[1]
if str(MCP) not in sys.path:
    sys.path.insert(0, str(MCP))

import selected_source_refresh_host as host  # noqa: E402


_UUID = "019f591f-04f6-70f2-8de7-828b7cccc69d"


class SelectedSourceRefreshHostTest(unittest.TestCase):
    def test_plan_is_the_exact_effect_free_plan_call(self) -> None:
        expected = {"mode": "plan", "candidate": "unchanged"}
        resolved_root = Path("/trusted-project")
        with patch.object(host, "plan_release_manifest_refresh", return_value=expected) as plan, patch.object(
            host, "_project_root", return_value=resolved_root
        ) as root, patch.object(host, "_operator_context") as operator:
            result = host.refresh_selected_release_binding("untrusted-root")
        self.assertIs(expected, result)
        root.assert_called_once_with("untrusted-root")
        plan.assert_called_once_with(resolved_root)
        operator.assert_not_called()

    def test_plan_rejects_unsafe_root_before_planning(self) -> None:
        with patch.object(
            host, "_project_root", side_effect=host.SelectedSourceRefreshHostError("selected-source-refresh Project root is unsafe")
        ), patch.object(host, "plan_release_manifest_refresh") as plan, self.assertRaisesRegex(
            host.SelectedSourceRefreshHostError, "Project root is unsafe"
        ):
            host.refresh_selected_release_binding("unsafe-root")
        plan.assert_not_called()

    def test_execute_uses_fresh_plan_and_opaque_context_only(self) -> None:
        root = Path("/trusted-project")
        plan = {"mode": "plan", "observed_input_sha256": "a" * 64}
        calls: list[str] = []

        def derive_plan(value: Path) -> dict[str, str]:
            calls.append("derive")
            self.assertEqual(root, value)
            return plan

        def authorize(*args: object, **kwargs: object) -> object:
            calls.append("authorize")
            self.assertEqual((root, plan), args)
            self.assertEqual("authority.md", kwargs["authorization_ref"])
            return sentinel.context

        def publish(*args: object, **kwargs: object) -> dict[str, bool]:
            calls.append("publish")
            self.assertEqual((root,), args)
            self.assertEqual({"execute": True, "authorization": sentinel.context}, kwargs)
            return {"published": False}

        with patch.dict("os.environ", {"CODEX_THREAD_ID": _UUID}, clear=True), patch.object(host, "_project_root", return_value=root), patch.object(host, "_operator_context", return_value=("Anatoly Maslennikov", "anatoly-m-maslennikov")), patch.object(
                host, "registered_source_refresh", return_value={"authorization_ref": "authority.md"}
            ), patch.object(host, "plan_release_manifest_refresh", side_effect=derive_plan), patch.object(
                host, "authorize_operator_refresh", side_effect=authorize
            ), patch.object(host, "refresh_release_manifest", side_effect=publish):
            result = host.refresh_selected_release_binding(root, "execute")
        self.assertEqual({"published": False}, result)
        self.assertEqual(["derive", "authorize", "publish"], calls)

    def test_execute_rejects_conflicting_native_codex_identity_before_effects(self) -> None:
        root = Path("/trusted-project")
        with patch.dict("os.environ", {"CODEX_THREAD_ID": _UUID, "CODEX_SESSION_ID": "019f5920-04f6-70f2-8de7-828b7cccc69d"}, clear=True), patch.object(host, "_project_root", return_value=root), patch.object(host, "_operator_context") as operator, self.assertRaisesRegex(
                host.SelectedSourceRefreshHostError, "identifiers conflict"
            ):
            host.refresh_selected_release_binding(root, "execute")
        operator.assert_not_called()

    def test_native_codex_identity_rejects_missing_and_malformed_values(self) -> None:
        cases = (
            ({}, "session is missing"),
            ({"CODEX_THREAD_ID": "not-a-uuid"}, "CODEX_THREAD_ID must be a UUID"),
            ({"CODEX_SESSION_ID": "not-a-uuid"}, "CODEX_SESSION_ID must be a UUID"),
        )
        for environment, message in cases:
            with self.subTest(environment=environment), patch.dict("os.environ", environment, clear=True), self.assertRaisesRegex(
                host.SelectedSourceRefreshHostError, message
            ):
                host._codex_session()

    def test_operator_context_rejects_missing_duplicate_or_blank_mapping(self) -> None:
        cases = (
            (b'[[operators]]\nname = "Someone Else"\nrole = "project owner"\njournal_author = "someone-else"\n', "missing or ambiguous"),
            (b'[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\njournal_author = "anatoly-m-maslennikov"\n[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\njournal_author = "other-author"\n', "registry is invalid"),
            (b'[[operators]]\nname = "Anatoly Maslennikov"\nrole = "project owner"\njournal_author = ""\n', "registry is invalid"),
        )
        for payload, message in cases:
            with self.subTest(payload=payload), patch.object(host, "_read_regular", return_value=payload), self.assertRaisesRegex(
                host.SelectedSourceRefreshHostError, message
            ):
                host._operator_context(Path("/trusted-project"))

    def test_cli_rejects_untrusted_identity_and_context_arguments(self) -> None:
        forbidden = ("--operator", "--journal-author", "--llm-session", "--authorization-ref", "--context")
        for argument in forbidden:
            with self.subTest(argument=argument), patch.object(host, "refresh_selected_release_binding") as command, redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as raised:
                host.main(("/trusted-project", argument, "untrusted"))
            self.assertEqual(2, raised.exception.code)
            command.assert_not_called()

    def test_execute_rejects_unsafe_root_before_identity_or_effects(self) -> None:
        unsafe = Path("/unsafe-project")
        with patch.dict("os.environ", {"CODEX_THREAD_ID": _UUID}, clear=True), patch.object(
            host, "_project_root", side_effect=host.SelectedSourceRefreshHostError("selected-source-refresh Project root is unsafe")
        ), patch.object(host, "_operator_context") as operator, self.assertRaisesRegex(
                host.SelectedSourceRefreshHostError, "Project root is unsafe"
            ):
            host.refresh_selected_release_binding(unsafe, "execute")
        operator.assert_not_called()
