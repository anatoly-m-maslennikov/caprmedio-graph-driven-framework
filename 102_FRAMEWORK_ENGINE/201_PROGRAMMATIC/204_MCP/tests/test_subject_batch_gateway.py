"""Actual SDK batch requests use the ordinary selected route without elicitation."""

import copy
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from mcp import types
from mcp.client._memory import InMemoryTransport
from mcp.client.session import ClientSession

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
APP = MCP.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
for location in (MCP, TOOLS, APP, TOOLS / "tests"):
    sys.path.insert(0, str(location))

import hot_reload  # noqa: E402
import subject_batch_execution as batch  # noqa: E402
from backend import _selected_public_outcome  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_routes import SelectedRouteAdapter  # noqa: E402
from subject_batch_fixture import SubjectBatchProject  # noqa: E402
from subject_batch_stage import stage_subject_batch  # noqa: E402


class SubjectBatchGatewayTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.project = SubjectBatchProject(self)
        self.runner, self.frozen = self.project.execution("connected-subject-batch")
        self.forms, self.submissions = [], []
        self.gateway = hot_reload.Gateway(self.project.root)
        self.gateway.active = SimpleNamespace(
            client=SimpleNamespace(call_tool=self.child_call),
            fingerprint="fixture-generation",
            in_flight=0,
            tools=[types.Tool(name="update_atom", input_schema={"type": "object"})],
        )

    async def child_call(self, name, arguments, **_kwargs):
        value = SelectedRouteAdapter(self.project.root).invoke(name, arguments["request"])
        return hot_reload.result(value)

    def execute(self, root, request):
        self.submissions.append(copy.deepcopy(request))
        runner = SelectedExecution(root)
        return runner.dispatch(runner.freeze(request))

    def outcome(self, response):
        return _selected_public_outcome(self.frozen, response.structured_content,
                                        self.frozen["request"]["run_id"])[0]

    async def connected_call(self, *, enqueue=None):
        async def elicit(_context, parameters):
            self.forms.append(parameters)
            raise AssertionError("Subject batch requested an extra confirmation")

        with patch("orchestrator.run", side_effect=enqueue or self.execute):
            async with InMemoryTransport(
                self.gateway.build_server(), raise_exceptions=True
            ) as streams:
                async with ClientSession(*streams, elicitation_callback=elicit) as client:
                    await client.initialize()
                    return await client.call_tool(
                        "update_atom", {"request": self.frozen["request"]["execution"]}
                    )

    async def test_batch_uses_existing_authorization_without_form_or_fabricated_receipt(self):
        response = await self.connected_call()
        self.assertEqual("terminal", response.structured_content["disposition"])
        self.assertEqual("completed", self.outcome(response))
        self.assertEqual([], self.forms)
        self.assertEqual(1, len(self.submissions))
        self.assertFalse(list(self.project.root.rglob("subject_batch_confirmation.json")))
        for path in self.project.paths:
            self.assertNotEqual(self.project.before[path], path.read_bytes())

    async def test_draft_backed_packet_uses_the_same_route_without_extra_confirmation(self):
        staged = stage_subject_batch(self.project.root, self.project.parameters, limit=2)
        self.project.use_reviewed_packet(staged["reviewed_packet"])
        self.project.commit_drafts()
        self.runner, self.frozen = self.project.execution("connected-draft-subject-batch")
        response = await self.connected_call()
        self.assertEqual("terminal", response.structured_content["disposition"])
        self.assertEqual("completed", self.outcome(response))
        self.assertEqual([], self.forms)
        self.assertEqual(1, len(self.submissions))

    async def test_self_consistent_but_false_frontier_and_effects_cannot_publish(self):
        def narrow(request):
            request["target_frontier"] = request["target_frontier"][:1]

        def wrong_effect(request):
            request["effects"][0]["atom_id"] = "CA-R-999999"

        for ordinal, transform in enumerate((narrow, wrong_effect)):
            with self.subTest(transform=transform.__name__):
                self.runner, self.frozen = self.project.execution(
                    f"false-subject-batch-frontier-{ordinal}", request_transform=transform
                )
                with patch.object(batch, "subject_update_action") as publisher:
                    response = await self.connected_call()
                self.assertNotEqual("completed", self.outcome(response))
                publisher.assert_not_called()
                self.assertEqual([], self.forms)
                for path in self.project.paths:
                    self.assertEqual(self.project.before[path], path.read_bytes())

    async def test_changed_packet_is_rejected_without_publication(self):
        self.project.packet_path.write_bytes(self.project.packet_path.read_bytes() + b"\n")
        with patch.object(batch, "subject_update_action") as publisher:
            response = await self.connected_call()
        self.assertNotEqual("completed", self.outcome(response))
        publisher.assert_not_called()
        self.assertEqual([], self.forms)
        for path in self.project.paths:
            self.assertEqual(self.project.before[path], path.read_bytes())


if __name__ == "__main__":
    unittest.main()
