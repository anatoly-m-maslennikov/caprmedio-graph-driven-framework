"""Preparation completion across the gateway, plus deterministic late effects."""
from __future__ import annotations

import asyncio
import copy
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

from mcp import Client, StdioServerParameters

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

import hot_reload
import test_direct_subject_preparation_protocol as protocol


class SubjectPreparationGatewayTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.fixture = protocol.DirectSubjectPreparationProtocolTests(methodName="runTest")
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root = self.fixture.root

    async def test_real_gateway_child_returns_completed_fixture_stage(self):
        # The production child, catalog admission, and provider are not replaced.
        code = (
            "import asyncio,sys;sys.path.insert(0,sys.argv[1]);"
            "from hot_reload import Gateway,startup_selection;"
            "selection=startup_selection(sys.argv[2]);"
            "asyncio.run(Gateway(sys.argv[2],selection=selection).serve())"
        )
        parameters = StdioServerParameters(
            command=sys.executable,
            args=["-B", "-c", code, str(MCP_ROOT), str(self.root)],
            env={"PYTHONDONTWRITEBYTECODE": "1"},
        )
        async with Client(parameters, cache=None, mode="legacy", read_timeout_seconds=120) as client:
            names = {tool.name for tool in (await client.list_tools()).tools}
            self.assertIn("atom_update", names)
            self.assertIn("get_mcp_reload_status", names)
            before_preview = protocol._snapshot(self.root)
            request = copy.deepcopy(self.fixture.request)
            request["atoms"] = request["atoms"][:1]
            response = await client.call_tool("atom_update", {"request": request})
            preview = self.fixture._preview(response)
            self.assertEqual(before_preview, protocol._snapshot(self.root))
            before_stage = protocol._snapshot(self.root)
            response = await client.call_tool(
                "atom_update", {"request": self.fixture._stage_request(request, preview)}
            )
            stage = self.fixture._stage(response, preview, before_stage)
            self.assertTrue((self.root / stage["manifest_path"]).is_file())

    async def test_uncertain_response_does_not_mean_child_effects_drained_or_replayed(self):
        started, release = asyncio.Event(), asyncio.Event()
        artifact = self.root / ".caprmedio_tmp/late-effect-evidence"
        calls, tasks = [], []

        async def child_work():
            started.set()
            await release.wait()
            artifact.parent.mkdir(parents=True, exist_ok=True)
            artifact.write_bytes(b"one retained child effect\n")

        class ChildClient:
            async def call_tool(self, name, arguments, *, read_timeout_seconds):
                calls.append((name, arguments, read_timeout_seconds))
                tasks.append(asyncio.create_task(child_work()))
                await started.wait()
                # Model lost completion, without guessing the production exception.
                raise TimeoutError("injected child-client completion failure")

        gateway = hot_reload.Gateway(self.root)
        generation = SimpleNamespace(
            client=ChildClient(), fingerprint="fixture-generation", in_flight=0,
            tools=[SimpleNamespace(name="atom_update")],
        )
        gateway.active = generation
        arguments = {"request": {"operation": "stage_subjects"}}
        try:
            response = await gateway.call(
                None, SimpleNamespace(name="atom_update", arguments=arguments)
            )
            self.assertTrue(response.is_error)
            self.assertEqual("uncertain", response.structured_content["outcome"])
            self.assertEqual(0, generation.in_flight)
            self.assertFalse(artifact.exists())
            self.assertFalse(tasks[0].done())
            self.assertEqual(
                [("atom_update", arguments, hot_reload.IMPLEMENTATION_CALL_TIMEOUT_SECONDS)], calls
            )
            release.set()
            await tasks[0]
            self.assertEqual(b"one retained child effect\n", artifact.read_bytes())
            self.assertEqual(1, len(calls), "an uncertain response must not replay the call")
        finally:
            release.set()
            await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    unittest.main()
