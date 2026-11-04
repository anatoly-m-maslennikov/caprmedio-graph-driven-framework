# CA-E-673@2

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from workbench_tools import CHECK, RUN, WorkbenchTools, native_tools  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402


class FakeService:
    def __init__(self):
        self.calls = []
        self.closed = False

    def run(self, sql):
        self.calls.append((RUN, sql))
        return {"rows": [[sql]], "row_count": 1, "column_count": 1}

    def check(self, sql):
        self.calls.append((CHECK, sql))
        return {"valid": True, "row_count": 1, "column_count": 1}

    def close(self):
        self.closed = True


class WorkbenchToolsTests(unittest.TestCase):
    def test_two_native_descriptors_and_one_owner_handle_run_check_and_close(self):
        self.assertEqual([RUN, CHECK], [tool.name for tool in native_tools()])
        owner = WorkbenchTools(Path("/project"))
        fake = FakeService()
        owner._service = fake

        async def exercise():
            self.assertEqual(1, (await owner.call(RUN, {"sql": "SELECT 1"}))["row_count"])
            self.assertTrue((await owner.call(CHECK, {"sql": "SELECT 1"}))["valid"])
            await owner.close()

        asyncio.run(exercise())
        self.assertEqual([(RUN, "SELECT 1"), (CHECK, "SELECT 1")], fake.calls)
        self.assertTrue(fake.closed)

    def test_invalid_arguments_are_not_sent_to_the_service(self):
        owner = WorkbenchTools(Path("/project"))
        owner._service = FakeService()
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(RUN, {"sql": 1}))
        self.assertEqual("query_error", caught.exception.code)
        self.assertEqual("sql must be a string", caught.exception.message)
        self.assertEqual([], owner._service.calls)

    def test_known_query_and_unavailable_failures_are_explicit_but_unexpected_failure_is_not(self):
        owner = WorkbenchTools(Path("/project"))
        owner._service = Mock(run=Mock(side_effect=RuntimeError("query failed: Parser Error")))
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(RUN, {"sql": "SELECT FROM"}))
        self.assertEqual("query_error", caught.exception.code)
        self.assertEqual("query failed: Parser Error", caught.exception.message)

        owner._service.run.side_effect = RuntimeError("query failed: missing column 'restart required'")
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(RUN, {"sql": 'SELECT "restart required"'}))
        self.assertEqual("query_error", caught.exception.code)

        owner._service.run.side_effect = ValueError("query result delivery failed: unsupported value")
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(RUN, {"sql": "SELECT unsupported"}))
        self.assertEqual("query_error", caught.exception.code)
        self.assertEqual("query result delivery failed: unsupported value", caught.exception.message)

        owner._service.run.side_effect = RuntimeError("query store unavailable; Workbench restart required")
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(RUN, {"sql": "SELECT 1"}))
        self.assertEqual("workbench_unavailable", caught.exception.code)
        self.assertEqual("Workbench unavailable; restart required", caught.exception.message)

        owner._service.run.side_effect = RuntimeError("unexpected connector fault")
        with self.assertRaisesRegex(RuntimeError, "unexpected connector fault"):
            asyncio.run(owner.call(RUN, {"sql": "SELECT 1"}))

        owner._service.run.side_effect = RuntimeError("unexpected connector fault: restart required")
        with self.assertRaisesRegex(RuntimeError, "unexpected connector fault"):
            asyncio.run(owner.call(RUN, {"sql": "SELECT 1"}))


if __name__ == "__main__":
    unittest.main()
