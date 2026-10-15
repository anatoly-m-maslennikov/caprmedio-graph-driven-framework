"""Connected SDK form and native temporary fixtures; no live Codex/UI claim."""
from __future__ import annotations

import asyncio
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import threading
from types import SimpleNamespace
import unittest
from unittest.mock import AsyncMock, patch

import anyio
from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server.lowlevel import Server
from mcp.shared.exceptions import MCPError, NoBackChannelError

MCP_ROOT = Path(__file__).resolve().parents[1]
TOOLS_ROOT = MCP_ROOT.parent / "201_TOOLS"
WORKFLOW_ROOT = MCP_ROOT.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for path in (MCP_ROOT, TOOLS_ROOT, WORKFLOW_ROOT, TOOLS_ROOT / "ATOM_UPDATE/tests", TOOLS_ROOT / "tests"):
    sys.path.insert(0, str(path))

import atom_operations as operations
from atom_subject_stage import stage_subject_preview
from lifecycle_intents import LifecycleError
import subject_publication_authorization as authorization
import subject_publication_confirmation as host
from test_subject_apply_portfolio import SubjectApplyProject, PUBLICATION_PINS
from work_journal import read_records


class SubjectPublicationConfirmationTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.fixture = SubjectApplyProject(Path(self.directory.name).resolve())
        self.runner, self.frozen = self.fixture.execution("connected-subject-fixture")
        staged = stage_subject_preview(self.fixture.root, [{"selector": self.fixture.target["path"],
            "expected": {"atom_id": self.fixture.target["atom_id"], "version": self.fixture.target["version"],
                         "sha256": self.fixture.target["digest"]}, "subject_patches": self.fixture.patches}],
            timestamp="2026-10-13 14:00:00 +0400", subject_profile=self.fixture.parameters.get("subject_profile", "legacy"))
        self.manifest = {"path": staged["manifest_path"], "digest": staged["manifest_sha256"]}
        self.staged_atom = json.loads((self.fixture.root / self.manifest["path"]).read_bytes())["atoms"][0]

    @staticmethod
    def context(reply=None):
        session = SimpleNamespace(
            client_capabilities=types.ClientCapabilities(
                elicitation=types.ElicitationCapability(form=types.FormElicitationCapability())),
            can_send_request=True, elicit_form=AsyncMock(return_value=reply),
            client_params=SimpleNamespace(client_info=SimpleNamespace(name="spoofed-codex")),
        )
        return SimpleNamespace(session=session, request_id="exact-outer-request")

    async def confirm(self, context, **overrides):
        inputs = {"operator_name": "golden-operator", "staged_manifest": self.manifest, **overrides}
        return await host.confirm_subject_publication(context, self.runner, self.frozen, **inputs)

    async def assert_refusal(self, context, status, **overrides):
        with patch.object(host, "authorize_subject_publication", side_effect=AssertionError("issuer called")) as issuer, patch.object(
            self.runner, "_dispatch_confirmed_subject", side_effect=AssertionError("dispatch called")) as dispatch:
            response = await self.confirm(context, **overrides)
        self.assertEqual(status, response.structured_content["status"])
        self.assertEqual([], response.structured_content["effects"])
        issuer.assert_not_called()
        dispatch.assert_not_called()
        self.fixture.assert_unchanged(self)
        return response

    async def test_actual_sdk_form_drives_same_process_native_selected_publication(self):
        requested = []

        async def elicit(_context, params):
            requested.append(params)
            self.fixture.assert_unchanged(self)
            return types.ElicitResult(action="accept", content={"review": True, "pause": True})

        async def call_tool(context, params):
            self.assertEqual({"request": {}}, params.arguments)
            return await self.confirm(context)

        async def list_tools(_context, _params):
            return types.ListToolsResult(tools=[types.Tool(name="fixture-only", description="Offline fixture only",
                input_schema={"type": "object", "properties": {"request": {"type": "object"}},
                              "required": ["request"], "additionalProperties": False})])

        server = Server("fixture-only-subject-confirmation", on_call_tool=call_tool, on_list_tools=list_tools)
        with patch.object(host, "authorize_subject_publication", wraps=host.authorize_subject_publication) as issuer:
            async with InMemoryTransport(server, raise_exceptions=True) as streams:
                async with ClientSession(*streams, elicitation_callback=elicit) as client:
                    await client.initialize()
                    response = await client.call_tool("fixture-only", {"request": {}})
        self.assertEqual("dispatched", response.structured_content["status"])
        issuer.assert_called_once()
        self.assertEqual({"app": "run-support", "uuid": self.frozen["request"]["execution"]["request_id"]},
                         issuer.call_args.kwargs["llm_session"])
        self.assertEqual(1, len(requested))
        self.assertEqual(host.FORM_SCHEMA, requested[0].requested_schema)
        message = requested[0].message
        for value in (self.frozen["request"]["run_id"], self.fixture.target["atom_id"],
                      self.fixture.target["path"], self.fixture.archive.relative_to(self.fixture.root).as_posix(),
                      self.manifest["path"], self.staged_atom["candidate"]["path"],
                      '-  governs: Atom/Test', '+  governs: "Atom.State"'):
            self.assertIn(value, message)
        result = response.structured_content["result"]
        self.assertEqual("terminal", result["disposition"])
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())
        self.assertEqual(self.fixture.before_mode, self.fixture.archive.stat().st_mode & 0o777)
        current = self.fixture.path.read_bytes()
        frontmatter, body = operations.split_frontmatter(current.decode())
        self.assertEqual(str(self.fixture.target["version"] + 1), operations.frontmatter_scalar(frontmatter, "version"))
        self.assertEqual(self.fixture.prepared["proposed"]["content"], body)
        child = next(row["requested_run_id"] for row in self.frozen["request"]["execution"]["requested_runs"]
                     if row["definition"]["atom_id"] == "CA-O-030")
        terminal = next(row for row in result["terminal_runs"] if row["run_id"] == child)
        self.assertEqual("completed", terminal["outcome"])
        self.assertEqual(sorted([self.fixture.target["path"], self.fixture.archive.relative_to(self.fixture.root).as_posix()]),
                         terminal["effect_refs"])
        retained = json.loads((self.fixture.root / terminal["result_ref"]).read_bytes())
        self.assertEqual("admitted", retained["lifecycle_recording"]["state"])
        self.assertEqual(hashlib.sha256(current).hexdigest(), retained["native_result"]["observed"]["digest"])
        self.assertTrue(any(row.get("event") == "completed" and row.get("run", {}).get("run_id") == child
                            for row in read_records(self.fixture.root)))

    async def test_exact_outer_request_and_both_booleans_are_required(self):
        for content in ({"review": False, "pause": True}, {"review": True, "pause": False}):
            with self.subTest(content=content):
                context = self.context(types.ElicitResult(action="accept", content=content))
                await self.assert_refusal(context, "unconfirmed")
                context.session.elicit_form.assert_awaited_once()
                self.assertEqual(context.request_id, context.session.elicit_form.call_args.kwargs["related_request_id"])
        for action in ("decline", "cancel"):
            await self.assert_refusal(self.context(types.ElicitResult(action=action)), action)

    async def test_malformed_reply_cannot_mint_confirmation(self):
        replies = (None, {"action": "accept", "content": {"review": True, "pause": True}},
            types.ElicitResult(action="accept", content=None),
            types.ElicitResult(action="accept", content={"review": "yes", "pause": True}),
            types.ElicitResult(action="accept", content={"review": True, "pause": True, "confirmed": True}),
            types.ElicitResult(action="decline", content={"review": True, "pause": True}),
            types.ElicitResult.model_construct(action="approve", content=None))
        for reply in replies:
            with self.subTest(reply=reply):
                await self.assert_refusal(self.context(reply), "malformed_response")

    async def test_absent_outer_context_refuses_before_form_even_with_spoofed_client(self):
        for field in ("request", "channel", "form"):
            context = self.context()
            if field == "request":
                context.request_id = None
            elif field == "channel":
                context.session.can_send_request = False
            else:
                context.session.client_capabilities = types.ClientCapabilities()
            await self.assert_refusal(context, "unsupported")
            context.session.elicit_form.assert_not_called()

    async def test_transport_failure_timeout_and_cancellation_leave_sources_unchanged(self):
        for error, status in ((NoBackChannelError("elicitation/create"), "unsupported"),
                             (ConnectionError(), "disconnected"), (anyio.EndOfStream(), "disconnected"),
                             (MCPError(types.INTERNAL_ERROR, "fixture"), "elicitation_failed")):
            context = self.context()
            context.session.elicit_form.side_effect = error
            await self.assert_refusal(context, status)
        entered = asyncio.Event()

        async def wait(*_args, **_kwargs):
            entered.set()
            await asyncio.Event().wait()

        context = self.context()
        context.session.elicit_form.side_effect = wait
        with patch.object(host, "WAIT_SECONDS", 0.01):
            await self.assert_refusal(context, "timed_out")
        entered.clear()
        task = asyncio.create_task(self.confirm(context))
        await entered.wait()
        task.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await task
        self.fixture.assert_unchanged(self)

    async def test_displayed_manifest_candidate_authority_and_saved_request_drift_refuse(self):
        paths = [self.manifest["path"], self.staged_atom["candidate"]["path"], PUBLICATION_PINS["CA-R-866"],
                 (self.runner.run_directory(self.frozen["request"]["run_id"]) / "selected_request.json").relative_to(self.fixture.root).as_posix()]
        for relative in paths:
            with self.subTest(path=relative):
                path = self.fixture.root / relative
                before = path.read_bytes()

                async def changed(*_args, **_kwargs):
                    path.write_bytes(before + b"\nfixture drift\n")
                    return types.ElicitResult(action="accept", content={"review": True, "pause": True})

                context = self.context()
                context.session.elicit_form.side_effect = changed
                try:
                    await self.assert_refusal(context, "refused")
                    self.assertEqual(before + b"\nfixture drift\n", path.read_bytes())
                finally:
                    path.write_bytes(before)

    async def test_host_inputs_and_preform_pins_cannot_substitute_for_confirmation(self):
        context = self.context(types.ElicitResult(action="accept", content={"review": True, "pause": True}))
        await self.assert_refusal(context, "refused", staged_manifest={**self.manifest, "confirmed": True})
        context.session.elicit_form.assert_not_called()
        self.frozen["request"]["execution"]["confirmed"] = True
        await self.assert_refusal(context, "refused")
        context.session.elicit_form.assert_not_called()

    async def test_changed_outer_context_or_current_source_refuses_after_form(self):
        context = self.context()

        async def changed_context(*_args, **_kwargs):
            context.request_id = "another-outer-request"
            return types.ElicitResult(action="accept", content={"review": True, "pause": True})

        context.session.elicit_form.side_effect = changed_context
        await self.assert_refusal(context, "refused")
        changed = self.fixture.before + b"\nfixture current source drift\n"

        async def changed_source(*_args, **_kwargs):
            self.fixture.path.write_bytes(changed)
            return types.ElicitResult(action="accept", content={"review": True, "pause": True})

        context = self.context()
        context.session.elicit_form.side_effect = changed_source
        with patch.object(host, "authorize_subject_publication", side_effect=AssertionError("issuer called")) as issuer, patch.object(
            self.runner, "_dispatch_confirmed_subject", side_effect=AssertionError("dispatch called")) as dispatch:
            response = await self.confirm(context)
        self.assertEqual("refused", response.structured_content["status"])
        issuer.assert_not_called()
        dispatch.assert_not_called()
        self.assertEqual(changed, self.fixture.path.read_bytes())
        self.assertFalse(self.fixture.archive.exists())

    async def test_unavailable_issuer_refuses_after_form_without_dispatch(self):
        context = self.context(types.ElicitResult(action="accept", content={"review": True, "pause": True}))
        with patch.object(host, "authorize_subject_publication", None), patch.object(
            self.runner, "_dispatch_confirmed_subject", side_effect=AssertionError("dispatch called")) as dispatch:
            self.assertEqual("refused", (await self.confirm(context)).structured_content["status"])
        dispatch.assert_not_called()
        self.fixture.assert_unchanged(self)

    async def test_exception_after_native_effect_reports_uncertain_without_zero_effect_claim(self):
        context = self.context(types.ElicitResult(action="accept", content={"review": True, "pause": True}))
        write = self.runner._write

        def failed_after_effect(path, payload):
            if path.name in {"accepted.json", "dispatch_uncertain.json"}:
                raise OSError("fixture selected result write failure after effect")
            return write(path, payload)

        with patch.object(self.runner, "_write", side_effect=failed_after_effect):
            response = await self.confirm(context)
        data = response.structured_content
        self.assertEqual("uncertain", data["status"])
        self.assertNotIn("effects", data)
        self.assertNotIn("effect_refs", data["result"])
        self.assertEqual({"automatic_retry": False, "inspection_required": True}, data["result"]["recovery"])
        self.assertEqual([self.fixture.target["path"], self.fixture.archive.relative_to(self.fixture.root).as_posix()],
                         data["result"]["unknown_remainder"])
        self.assertNotEqual(self.fixture.before, self.fixture.path.read_bytes())
        self.assertEqual(self.fixture.before, self.fixture.archive.read_bytes())

    async def test_confirmation_is_consumed_after_failed_unchanged_attempt(self):
        confirmation = authorization.authorize_subject_publication(self.fixture.root,
            self.frozen["request"]["execution"], operator_name="golden-operator",
            llm_session={"app": "run-support", "uuid": self.frozen["request"]["execution"]["request_id"]},
            staged_manifest=self.manifest)
        calls = []

        @authorization.with_subject_publication_window
        def failed_unchanged(_root, _parameters, **_kwargs):
            calls.append("attempt")
            return {"outcome": "failed"}

        def attempt():
            with authorization.bind_subject_publication_confirmation(confirmation):
                return failed_unchanged(self.fixture.root, self.fixture.parameters, execute=True,
                    session=SimpleNamespace(request=self.frozen["request"]["execution"]))

        self.assertEqual({"outcome": "failed"}, attempt())
        with self.assertRaises(authorization.SubjectPublicationAuthorizationError) as refused:
            attempt()
        self.assertIn("already been consumed", str(refused.exception))
        self.assertEqual(["attempt"], calls)
        self.fixture.assert_unchanged(self)

    async def test_confirmation_claim_refuses_overlap_without_excluding_distinct_confirmation(self):
        def issue():
            return authorization.authorize_subject_publication(self.fixture.root,
                self.frozen["request"]["execution"], operator_name="golden-operator",
                llm_session={"app": "run-support", "uuid": self.frozen["request"]["execution"]["request_id"]},
                staged_manifest=self.manifest)

        confirmation, distinct = issue(), issue()
        entered, release = threading.Event(), threading.Event()
        calls = []

        @authorization.with_subject_publication_window
        def failed_unchanged(_root, _parameters, **_kwargs):
            calls.append("attempt")
            if len(calls) == 1:
                entered.set()
                self.assertTrue(release.wait(30), "First action was not released")
            return {"outcome": "failed"}

        def attempt(confirmed):
            with authorization.bind_subject_publication_confirmation(confirmed):
                return failed_unchanged(self.fixture.root, self.fixture.parameters, execute=True,
                    session=SimpleNamespace(request=self.frozen["request"]["execution"]))

        with ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(attempt, confirmation)
            try:
                self.assertTrue(await asyncio.to_thread(entered.wait, 30), "First action did not enter")
                with self.assertRaises(LifecycleError) as refused:
                    pool.submit(attempt, confirmation).result(timeout=30)
                self.assertIn("already been consumed", str(refused.exception))
                self.assertEqual(["attempt"], calls)
                self.assertEqual({"outcome": "failed"}, pool.submit(attempt, distinct).result(timeout=30))
            finally:
                release.set()
            self.assertEqual({"outcome": "failed"}, first.result(timeout=30))
        self.assertEqual(["attempt", "attempt"], calls)
        self.fixture.assert_unchanged(self)


if __name__ == "__main__":
    unittest.main()
