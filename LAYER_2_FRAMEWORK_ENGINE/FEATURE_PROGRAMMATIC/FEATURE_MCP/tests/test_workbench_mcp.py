# CA-E-676@11

from __future__ import annotations

import asyncio
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock

MCP_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MCP_ROOT))

from workbench_tools import (  # noqa: E402
    CHECK, LOAD, NATIVE_TOOLS, PAGE, QUERY_LOG_LIST, RUN, SAVED_LIST, SAVE_VIEW, SCHEMA,
    VIEW_CREATE, WORKSPACE_OPEN,
    WorkbenchTools, native_tools,
)
from operation_error_boundary import ExplicitBlockingRuntimeFailure  # noqa: E402


class FakeService:
    def __init__(self):
        self.calls = []
        self.closed = False

    def run(self, sql, page_size=100, cursor_position=None, *, save=False, preview=None, name=None):
        self.calls.append((RUN, sql, page_size, cursor_position, save, preview, name))
        result = {
            "query_id": "q-1", "columns": [{"name": "sql", "type": "VARCHAR"}],
            "rows": [[sql]], "row_count": 1, "column_count": 1,
            "offset": 0, "page_size": page_size, "has_more": False,
        }
        if save:
            result.update({"saved_query_id": "q_1", "kind": "query", "sql": sql, "name": name})
        return result

    def check(self, sql, cursor_position=None):
        self.calls.append((CHECK, sql, cursor_position))
        return {"valid": True, "row_count": 1, "column_count": 1}

    def page(self, query_id, offset, page_size=100):
        self.calls.append((PAGE, query_id, offset, page_size))
        return {
            "query_id": query_id, "columns": [{"name": "sql", "type": "VARCHAR"}],
            "rows": [[query_id]], "row_count": 1, "column_count": 1,
            "offset": offset, "page_size": page_size, "has_more": False,
        }

    def schema(self):
        self.calls.append((SCHEMA,))
        return {"atoms": []}

    def save_view(self, sql, name=None):
        self.calls.append((SAVE_VIEW, sql, name))
        return {"saved_query_id": "w_1", "kind": "view", "sql": sql, "name": name}

    def load(self, reference):
        self.calls.append((LOAD, reference))
        return {"saved_query_id": reference, "kind": "query", "sql": "SELECT 1"}

    def saved_list(self, limit=20):
        self.calls.append((SAVED_LIST, limit))
        return {"items": []}

    def interface_call(self, name, arguments):
        self.calls.append((name, arguments))
        return {"operation": name, **arguments}

    def close(self):
        self.closed = True


class WorkbenchToolsTests(unittest.TestCase):
    def test_native_descriptors_and_one_owner_handle_all_calls_and_close(self):
        self.assertEqual(list(NATIVE_TOOLS), [tool.name for tool in native_tools()])
        tools = {tool.name: tool for tool in native_tools()}
        self.assertNotIn("query_save", tools)
        self.assertFalse(tools[RUN].annotations.read_only_hint)
        self.assertTrue(tools[CHECK].annotations.read_only_hint)
        self.assertTrue(tools[SCHEMA].annotations.read_only_hint)
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
            saved = await owner.call(RUN, {
                "sql": "SELECT 2", "cursor_position": 2, "save": True, "name": "saved",
            })
            self.assertEqual("q_1", saved["saved_query_id"])
            self.assertEqual("w_1", (await owner.call(SAVE_VIEW, {"sql": "SELECT 3", "name": "view"}))["saved_query_id"])
            await owner.call(RUN, {"sql": "SELECT 4", "save": True, "name": "   "})
            self.assertEqual("q_2", (await owner.call(LOAD, {"reference": "q_2"}))["saved_query_id"])
            self.assertEqual({"atoms": []}, await owner.call(SCHEMA, {}))
            self.assertEqual({"items": []}, await owner.call(SAVED_LIST, {"limit": 3}))
            self.assertEqual("session-1", (await owner.call(WORKSPACE_OPEN, {"session_id": "session-1"}))["session_id"])
            self.assertEqual("view_create", (await owner.call(VIEW_CREATE, {"workspace_id": "session-1"}))["operation"])
            self.assertEqual("query_log_list", (await owner.call(QUERY_LOG_LIST, {}))["operation"])
            await owner.close()

        asyncio.run(exercise())
        self.assertEqual(
            [(RUN, "SELECT 1", 100, None, False, None, None), (PAGE, "q-1", 0, 1), (CHECK, "SELECT 1", None),
             (RUN, "SELECT 2", 100, 2, True, None, "saved"), (SAVE_VIEW, "SELECT 3", "view"),
             (RUN, "SELECT 4", 100, None, True, None, "   "), (LOAD, "q_2"),
             (SCHEMA,), (SAVED_LIST, 3), (WORKSPACE_OPEN, {"session_id": "session-1"}),
             (VIEW_CREATE, {"workspace_id": "session-1"}), (QUERY_LOG_LIST, {})], fake.calls
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
            (RUN, {"sql": "SELECT 1", "name": "forbidden"}, "name is only valid when save is true"),
            (RUN, {"sql": "SELECT 1", "save": "yes"}, "save must be a boolean"),
            (RUN, {"sql": "SELECT 1", "preview": -1}, "preview must be a non-negative integer"),
            (CHECK, {"sql": "SELECT 1", "name": "forbidden"}, "Expected only cursor_position and sql"),
            (SAVE_VIEW, {"sql": "SELECT 1", "name": 1}, "name must be a string"),
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
