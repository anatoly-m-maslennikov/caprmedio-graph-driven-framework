"""One connected SDK form persists batch approval before durable queue admission."""

from pathlib import Path
import sys
import unittest
from unittest.mock import patch

from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession
from mcp.server.lowlevel import Server

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
APP = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for location in (MCP, TOOLS, APP, TOOLS / "tests"):
    sys.path.insert(0, str(location))

import subject_batch_confirmation as host  # noqa: E402
from subject_batch_authorization import CONFIRMATION  # noqa: E402
from subject_batch_fixture import SubjectBatchProject  # noqa: E402
from subject_batch_stage import stage_subject_batch  # noqa: E402


class SubjectBatchConfirmationTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.project = SubjectBatchProject(self)
        self.runner, self.frozen = self.project.execution("connected-subject-batch")
        self.forms, self.queued = [], []
        self.reply = types.ElicitResult(action="accept", content={"review": True, "pause": True})

    def receipt(self):
        return self.runner.run_directory(self.frozen["request"]["run_id"]) / CONFIRMATION

    def enqueue(self, runner, frozen):
        self.assertTrue(self.receipt().is_file(), "queue admission preceded persisted approval")
        self.queued.append(frozen["request"]["run_id"])
        return {"workflow_run_id": frozen["request"]["run_id"], "status": "queued"}

    async def connected_call(self, *, enqueue=None):
        async def elicit(_context, parameters):
            self.forms.append(parameters)
            self.assertFalse(self.receipt().exists())
            self.assertEqual([], self.queued)
            for path in self.project.paths:
                self.assertEqual(self.project.before[path], path.read_bytes())
            return self.reply

        async def call_tool(context, _parameters):
            return await host.confirm_subject_batch_publication(
                context, self.runner, self.frozen, operator_name="golden-operator"
            )

        async def list_tools(_context, _parameters):
            return types.ListToolsResult(
                tools=[
                    types.Tool(
                        name="fixture-batch",
                        input_schema={"type": "object", "additionalProperties": False},
                    )
                ]
            )

        server = Server("fixture-batch", on_call_tool=call_tool, on_list_tools=list_tools)
        with patch.object(host, "_enqueue", side_effect=enqueue or self.enqueue):
            async with InMemoryTransport(server, raise_exceptions=True) as streams:
                async with ClientSession(*streams, elicitation_callback=elicit) as client:
                    await client.initialize()
                    return await client.call_tool("fixture-batch", {})

    async def test_single_actual_form_then_reconnect_reuses_persisted_approval(self):
        response = await self.connected_call()
        self.assertEqual("dispatched", response.structured_content["status"])
        self.assertEqual(1, len(self.forms))
        message = self.forms[0].message
        self.assertIn(self.project.parameters["subject_batch"]["path"], message)
        self.assertIn(self.project.parameters["subject_batch"]["digest"], message)
        self.assertIn(self.project.packet["git_checkpoint"], message)
        with patch.object(host, "_enqueue", side_effect=self.enqueue):
            reconnect = await host.confirm_subject_batch_publication(
                None, self.runner, self.frozen, operator_name="golden-operator"
            )
        self.assertEqual("dispatched", reconnect.structured_content["status"])
        self.assertEqual(1, len(self.forms))
        self.assertEqual(["connected-subject-batch"] * 2, self.queued)

    async def test_declined_form_does_not_persist_or_enqueue(self):
        self.reply = types.ElicitResult(action="decline")
        response = await self.connected_call()
        self.assertEqual("decline", response.structured_content["status"])
        self.assertFalse(self.receipt().exists())
        self.assertEqual([], self.queued)

    async def test_draft_backed_packet_uses_one_form_for_the_complete_batch(self):
        staged = stage_subject_batch(self.project.root, self.project.parameters, limit=2)
        self.project.use_reviewed_packet(staged["reviewed_packet"])
        self.runner, self.frozen = self.project.execution("connected-draft-subject-batch")
        response = await self.connected_call()
        self.assertEqual("dispatched", response.structured_content["status"])
        self.assertEqual(1, len(self.forms))
        self.assertIn(staged["reviewed_packet"]["path"], self.forms[0].message)

    async def test_changed_packet_during_form_refuses_without_queue(self):
        original_reply = self.reply

        async def changed(_context, _parameters):
            self.project.packet_path.write_bytes(self.project.packet_path.read_bytes() + b"\n")
            return original_reply

        async def call_tool(context, _parameters):
            return await host.confirm_subject_batch_publication(
                context, self.runner, self.frozen, operator_name="golden-operator"
            )

        server = Server("fixture-batch-drift", on_call_tool=call_tool)
        with patch.object(host, "_enqueue", side_effect=self.enqueue):
            async with InMemoryTransport(server, raise_exceptions=True) as streams:
                async with ClientSession(*streams, elicitation_callback=changed) as client:
                    await client.initialize()
                    response = await client.call_tool("fixture-batch", {})
        self.assertEqual("refused", response.structured_content["status"])
        self.assertFalse(self.receipt().exists())
        self.assertEqual([], self.queued)


if __name__ == "__main__":
    unittest.main()
