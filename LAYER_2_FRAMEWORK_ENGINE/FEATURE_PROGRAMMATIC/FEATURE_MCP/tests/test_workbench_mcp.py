# CA-E-673@3

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from workbench_tools import CHECK, PAGE, RUN, WorkbenchTools, native_tools  # noqa: E402
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402


class FakeService:
    def __init__(self):
        self.calls = []
        self.closed = False

    def run(self, sql, page_size=100):
        self.calls.append((RUN, sql, page_size))
        return {
            "query_id": "q-1", "columns": [{"name": "sql", "type": "VARCHAR"}],
            "rows": [[sql]], "row_count": 1, "column_count": 1,
            "offset": 0, "page_size": page_size, "has_more": False,
        }

    def check(self, sql):
        self.calls.append((CHECK, sql))
        return {"valid": True, "row_count": 1, "column_count": 1}

    def page(self, query_id, offset, page_size=100):
        self.calls.append((PAGE, query_id, offset, page_size))
        return {
            "query_id": query_id, "columns": [{"name": "sql", "type": "VARCHAR"}],
            "rows": [[query_id]], "row_count": 1, "column_count": 1,
            "offset": offset, "page_size": page_size, "has_more": False,
        }

    def close(self):
        self.closed = True


class WorkbenchToolsTests(unittest.TestCase):
    def test_native_descriptors_and_one_owner_handle_run_page_check_and_close(self):
        self.assertEqual([RUN, CHECK, PAGE], [tool.name for tool in native_tools()])
        owner = WorkbenchTools(Path("/project"))
        fake = FakeService()
        owner._service = fake

        async def exercise():
            run = await owner.call(RUN, {"sql": "SELECT 1"})
            self.assertEqual("q-1", run["query_id"])
            self.assertEqual(1, run["row_count"])
            page = await owner.call(PAGE, {"query_id": run["query_id"], "offset": 0, "page_size": 1})
            self.assertEqual(0, page["offset"])
            self.assertTrue((await owner.call(CHECK, {"sql": "SELECT 1"}))["valid"])
            await owner.close()

        asyncio.run(exercise())
        self.assertEqual(
            [(RUN, "SELECT 1", 100), (PAGE, "q-1", 0, 1), (CHECK, "SELECT 1")], fake.calls
        )
        self.assertTrue(fake.closed)

    def test_invalid_arguments_are_not_sent_to_the_service(self):
        owner = WorkbenchTools(Path("/project"))
        owner._service = FakeService()
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(RUN, {"sql": 1}))
        self.assertEqual("query_error", caught.exception.code)
        self.assertEqual("sql must be a string", caught.exception.message)
        self.assertEqual([], owner._service.calls)

    def test_arguments_and_tool_name_are_strict(self):
        owner = WorkbenchTools(Path("/project"))
        owner._service = FakeService()
        for name, arguments, message in (
            (PAGE, {"query_id": "q", "offset": True}, "offset must be a non-negative integer"),
            (PAGE, {"query_id": "q", "offset": -1}, "offset must be a non-negative integer"),
            (PAGE, {"query_id": "q", "offset": 0, "page_size": True}, "page_size must be an integer"),
            (PAGE, {"query_id": "q", "offset": 0, "unknown": 1}, "Expected query_id, offset, and optional page_size"),
            (RUN, {"sql": "SELECT 1", "page_size": True}, "page_size must be an integer"),
            ("query_unknown", {"sql": "SELECT 1"}, "Unknown Workbench tool"),
        ):
            with self.subTest(name=name, arguments=arguments), self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
                asyncio.run(owner.call(name, arguments))
            self.assertEqual("query_error", caught.exception.code)
            self.assertEqual(message, caught.exception.message)
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

        owner._service.page = Mock(side_effect=RuntimeError("query page failed: query_id not found"))
        with self.assertRaises(ExplicitBlockingRuntimeFailure) as caught:
            asyncio.run(owner.call(PAGE, {"query_id": "expired", "offset": 0}))
        self.assertEqual("query_error", caught.exception.code)


if __name__ == "__main__":
    unittest.main()
