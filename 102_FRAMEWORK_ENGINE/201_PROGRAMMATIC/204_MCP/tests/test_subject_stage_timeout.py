"""Only direct Subject staging receives the longer completion budget."""
import asyncio
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))
import hot_reload


class SubjectStageTimeoutTests(unittest.IsolatedAsyncioTestCase):
    def gateway(self, client, name="atom_update"):
        gateway = hot_reload.Gateway(MCP_ROOT)
        gateway.active = SimpleNamespace(
            client=client, fingerprint="test", in_flight=0,
            tools=[SimpleNamespace(name=name)],
        )
        return gateway

    async def test_exact_selection_and_other_or_malformed_requests(self):
        response = hot_reload.result({"outcome": "prepared"})
        calls = []

        class Child:
            async def call_tool(self, name, arguments, *, read_timeout_seconds):
                calls.append((name, arguments, read_timeout_seconds))
                return response

        cases = [
            ("atom_update", {"request": {"operation": "stage_subjects"}}, 180),
            ("atom_update", {"request": {"operation": "preview_subjects"}}, 90),
            ("update_atom", {"request": {"operation": "stage_subjects"}}, 90),
            ("atom_update_extra", {"request": {"operation": "stage_subjects"}}, 90),
            ("atom_update", {"request": {"operation": "stage_subjects_extra"}}, 90),
            ("discover_tools", {"request": {}}, 90),
        ]
        for arguments in (None, [], "stage_subjects", {}, {"request": None},
                          {"request": []}, {"request": "stage_subjects"},
                          {"request": {}}, {"request": {"operation": ["stage_subjects"]}},
                          {"operation": "stage_subjects"}):
            cases.append(("atom_update", arguments, 90))
        for name, arguments, timeout in cases:
            with self.subTest(name=name, arguments=arguments):
                gateway = self.gateway(Child(), name)
                actual = await gateway.call(None, SimpleNamespace(name=name, arguments=arguments))
                self.assertIs(response, actual)
                self.assertEqual((name, arguments, timeout), calls[-1])
                self.assertEqual(0, gateway.active.in_flight)
        self.assertEqual(len(cases), len(calls))
        self.assertEqual(90, hot_reload.IMPLEMENTATION_CALL_TIMEOUT_SECONDS)
        self.assertEqual(180, hot_reload.SUBJECT_STAGE_CALL_TIMEOUT_SECONDS)

    async def test_pending_stage_returns_the_child_completion_without_replay(self):
        entered, release = asyncio.Event(), asyncio.Event()
        response = hot_reload.result({"operation": "stage_subjects", "errors": []})
        calls = []

        class Child:
            async def call_tool(self, name, arguments, *, read_timeout_seconds):
                calls.append(read_timeout_seconds)
                entered.set()
                await release.wait()
                return response

        gateway = self.gateway(Child())
        pending = asyncio.create_task(gateway.call(None, SimpleNamespace(
            name="atom_update", arguments={"request": {"operation": "stage_subjects"}})))
        try:
            await entered.wait()
            self.assertFalse(pending.done())
            self.assertEqual(1, gateway.active.in_flight)
            release.set()
            self.assertIs(response, await pending)
            self.assertEqual([180], calls)
            self.assertEqual(0, gateway.active.in_flight)
        finally:
            release.set()
            await pending

    async def test_late_failure_remains_uncertain_without_replay(self):
        entered, release = asyncio.Event(), asyncio.Event()
        calls = []

        class Child:
            async def call_tool(self, name, arguments, *, read_timeout_seconds):
                calls.append(read_timeout_seconds)
                entered.set()
                await release.wait()
                raise TimeoutError("injected completion failure")

        gateway = self.gateway(Child())
        pending = asyncio.create_task(gateway.call(None, SimpleNamespace(
            name="atom_update", arguments={"request": {"operation": "stage_subjects"}})))
        try:
            await entered.wait()
            self.assertEqual(1, gateway.active.in_flight)
            release.set()
            actual = await pending
            self.assertTrue(actual.is_error)
            self.assertEqual("uncertain", actual.structured_content["outcome"])
            self.assertIn("no automatic replay", actual.structured_content["diagnostics"][0])
            self.assertEqual([180], calls)
            self.assertEqual(0, gateway.active.in_flight)
        finally:
            release.set()
            await pending


if __name__ == "__main__":
    unittest.main()
