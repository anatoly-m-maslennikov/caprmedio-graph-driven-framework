"""Offline SDK form round trips; no claim of actual Codex UI or human approval."""
from __future__ import annotations

import asyncio
from contextlib import ExitStack
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

import anyio
from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server.lowlevel import Server
from mcp.shared.exceptions import MCPError, NoBackChannelError
from pydantic import ValidationError


MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
WORKFLOW_ROOT = MCP_ROOT.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for path in (MCP_ROOT, TOOLS_ROOT, WORKFLOW_ROOT):
    sys.path.insert(0, str(path))
import confirmation_probe as probe


class ConfirmationProbeTests(unittest.IsolatedAsyncioTestCase):
    @staticmethod
    def context(reply=None):
        session = SimpleNamespace(
            client_capabilities=types.ClientCapabilities(
                elicitation=types.ElicitationCapability(form=types.FormElicitationCapability())),
            can_send_request=True,
            elicit_form=AsyncMock(return_value=reply),
            client_params=SimpleNamespace(client_info=SimpleNamespace(name="spoofed-codex")),
        )
        return SimpleNamespace(session=session, request_id="exact-outer-request")

    def diagnostic(self, response, status):
        data = response.structured_content
        self.assertEqual({"status", "action", "content", "authorization", "effects", "diagnostics"}, set(data))
        self.assertEqual(status, data["status"])
        self.assertIs(False, data["authorization"])
        self.assertEqual([], data["effects"])
        self.assertIn("not authorization", data["diagnostics"][0])
        self.assertEqual(data, json.loads(response.content[0].text))
        self.assertEqual(status != "observed", response.is_error)
        return data

    async def test_real_sdk_accept_decline_cancel_round_trips_are_diagnostics_only(self):
        for action in ("accept", "decline", "cancel"):
            with self.subTest(action=action):
                requested = []

                async def elicit(_context, params):
                    requested.append(params)
                    return types.ElicitResult(action=action,
                        content={"acknowledge": True} if action == "accept" else None)

                async def list_tools(_context, _params):
                    return types.ListToolsResult(tools=[probe.TOOL])

                async def call_tool(context, params):
                    self.assertEqual(probe.TOOL.name, params.name)
                    return await probe.run_confirmation_probe(context, params.arguments)

                server = Server("offline-confirmation-probe", on_list_tools=list_tools, on_call_tool=call_tool)
                async with InMemoryTransport(server, raise_exceptions=True) as streams:
                    async with ClientSession(*streams, elicitation_callback=elicit) as client:
                        await client.initialize()
                        self.assertEqual([probe.TOOL.name], [t.name for t in (await client.list_tools()).tools])
                        data = self.diagnostic(await client.call_tool(probe.TOOL.name, {"request": {}}), "observed")
                self.assertEqual(action, data["action"])
                self.assertEqual(1, len(requested))
                self.assertEqual("form", requested[0].mode)
                self.assertEqual(probe.MESSAGE, requested[0].message)
                self.assertEqual(probe.FORM_SCHEMA, requested[0].requested_schema)

    async def test_exact_request_context_is_used_and_accept_is_not_trust(self):
        contexts = [self.context(types.ElicitResult(action="accept", content={"acknowledge": acknowledged}))
                    for acknowledged in (True, False)]
        for index, context in enumerate(contexts):
            context.request_id = f"outer-request-{index}"
        responses = await asyncio.gather(*(probe.run_confirmation_probe(context, {"request": {}})
                                           for context in contexts))
        for context, response, acknowledged in zip(contexts, responses, (True, False), strict=True):
            data = self.diagnostic(response, "observed")
            context.session.elicit_form.assert_awaited_once_with(
                probe.MESSAGE, probe.FORM_SCHEMA, related_request_id=context.request_id)
            self.assertEqual({"acknowledge": acknowledged}, data["content"])

    async def test_nonempty_unknown_or_wrong_input_refuses_before_elicitation(self):
        context = self.context()
        for arguments in (None, {}, [], {"request": None}, {"request": []},
                          {"request": {"confirmed": True}}, {"request": {}, "path": "source.md"}):
            with self.subTest(arguments=arguments):
                self.diagnostic(await probe.run_confirmation_probe(context, arguments), "invalid_input")
        context.session.elicit_form.assert_not_called()

    async def test_missing_form_backchannel_or_request_refuses_even_spoofed_codex(self):
        for field in ("capability", "channel", "request"):
            context = self.context()
            if field == "capability":
                context.session.client_capabilities = types.ClientCapabilities(
                    elicitation=types.ElicitationCapability(url=types.UrlElicitationCapability()))
            elif field == "channel":
                context.session.can_send_request = False
            else:
                context.request_id = None
            self.diagnostic(await probe.run_confirmation_probe(context, {"request": {}}), "unsupported")
            context.session.elicit_form.assert_not_called()

    async def test_malformed_responses_do_not_become_confirmation(self):
        replies = [None, {"action": "accept", "content": {"acknowledge": True}},
                   types.ElicitResult(action="accept", content=None),
                   types.ElicitResult(action="accept", content={"acknowledge": "yes"}),
                   types.ElicitResult(action="accept", content={"acknowledge": True, "confirmed": True}),
                   types.ElicitResult(action="decline", content={"acknowledge": True}),
                   types.ElicitResult.model_construct(action="approve", content=None)]
        for reply in replies:
            with self.subTest(reply=reply):
                self.diagnostic(await probe.run_confirmation_probe(self.context(reply), {"request": {}}),
                                "malformed_response")

    async def test_unsupported_disconnect_and_remote_error_return_no_permission(self):
        try:
            types.ElicitResult.model_validate({"action": "automatic-approval"})
        except ValidationError as error:
            malformed = error
        for error, status in ((NoBackChannelError("elicitation/create"), "unsupported"),
                              (ConnectionError("private details"), "disconnected"),
                              (anyio.EndOfStream(), "disconnected"),
                              (anyio.ClosedResourceError(), "disconnected"),
                              (anyio.BrokenResourceError(), "disconnected"),
                              (malformed, "malformed_response"),
                              (MCPError(types.INTERNAL_ERROR, "private details"), "elicitation_failed")):
            context = self.context()
            context.session.elicit_form.side_effect = error
            data = self.diagnostic(await probe.run_confirmation_probe(context, {"request": {}}), status)
            self.assertNotIn("private details", json.dumps(data))

    async def test_wait_is_bounded_and_caller_cancellation_is_not_acceptance(self):
        started, cancelled = asyncio.Event(), asyncio.Event()

        async def wait(*_args, **_kwargs):
            started.set()
            try:
                await asyncio.Event().wait()
            finally:
                cancelled.set()

        context = self.context()
        context.session.elicit_form.side_effect = wait
        with patch.object(probe, "WAIT_SECONDS", 0.01):
            self.diagnostic(await probe.run_confirmation_probe(context, {"request": {}}), "timed_out")
        self.assertTrue(started.is_set())
        self.assertTrue(cancelled.is_set())
        started.clear()
        task = asyncio.create_task(probe.run_confirmation_probe(context, {"request": {}}))
        await started.wait()
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task

    async def test_probe_never_calls_publication_dispatch_preparation_or_files(self):
        import subject_publication_authorization
        import selected_execution
        import atom_subject_patch
        import atom_subject_stage

        with ExitStack() as stack:
            traps = [stack.enter_context(patch.object(owner, name, side_effect=AssertionError("effect path called")))
                     for owner, name in (
                         (subject_publication_authorization, "authorize_subject_publication"),
                         (selected_execution.SelectedExecution, "_dispatch_confirmed_subject"),
                         (selected_execution.SelectedExecution, "dispatch"),
                         (atom_subject_patch, "preview_subject_patches"),
                         (atom_subject_stage, "stage_subject_preview"),
                         (Path, "open"), (Path, "read_bytes"), (Path, "write_bytes"),
                         (Path, "read_text"), (Path, "write_text"), (Path, "mkdir"),
                     )]
            traps.append(stack.enter_context(patch("builtins.open", side_effect=AssertionError("file path called"))))
            for action in ("accept", "decline", "cancel"):
                reply = types.ElicitResult(action=action,
                    content={"acknowledge": True} if action == "accept" else None)
                self.diagnostic(await probe.run_confirmation_probe(self.context(reply), {"request": {}}), "observed")
            for trap in traps:
                trap.assert_not_called()


if __name__ == "__main__":
    unittest.main()
