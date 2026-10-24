"""Deterministic lifecycle checks for the bounded shared Project pool."""

from __future__ import annotations

import asyncio
from concurrent.futures import CancelledError as FutureCancelledError
from importlib import import_module
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

MCP = Path(__file__).resolve().parents[1]
TOOLS = MCP.parent / "201_TOOLS"
FIXTURES = Path(__file__).resolve().parent
sys.path[:0] = [str(MCP), str(TOOLS), str(TOOLS / "VALIDATE_ATOMS"), str(FIXTURES)]

shared_project_pool = import_module("shared_project_pool")
shared_pool_fixtures = import_module("shared_pool_fixtures")
ProjectCapacityError = shared_project_pool.ProjectCapacityError
SharedProjectPool = shared_project_pool.SharedProjectPool
_Factory = shared_pool_fixtures._Factory
_selection = shared_pool_fixtures._selection


class SharedProjectPoolTests(unittest.IsolatedAsyncioTestCase):
    async def test_loaded_gateway_reuses_entry_and_tracks_two_leases(self):
        factory = _Factory()
        pool = SharedProjectPool(1, factory)
        first = await pool.acquire(_selection("alpha"))
        second = await pool.acquire(_selection("alpha"))
        self.assertIs(first, second)
        self.assertEqual(2, first.in_flight)
        await pool.release(first)
        await pool.release(second)
        await pool.close()

    async def test_cancelled_initializer_closes_created_gateway(self):
        started = asyncio.Event()
        release = asyncio.Event()
        factory = _Factory(
            {
                "/projects/alpha": {"initialize_started": started, "initialize_release": release},
            }
        )
        pool = SharedProjectPool(1, factory)
        pending = asyncio.create_task(pool.acquire(_selection("alpha")))
        await started.wait()
        pending.cancel()
        with self.assertRaises(asyncio.CancelledError):
            await pending
        self.assertEqual(1, factory.gates["/projects/alpha"].closed)
        self.assertFalse(pool._pending)

    async def test_close_cancels_pending_initializer_without_publishing(self):
        started = asyncio.Event()
        release = asyncio.Event()
        factory = _Factory(
            {
                "/projects/alpha": {"initialize_started": started, "initialize_release": release},
            }
        )
        pool = SharedProjectPool(1, factory)
        pending = asyncio.create_task(pool.acquire(_selection("alpha")))
        await started.wait()
        await pool.close()
        result = await asyncio.gather(pending, return_exceptions=True)
        self.assertIsInstance(result[0], asyncio.CancelledError)
        self.assertEqual(1, factory.gates["/projects/alpha"].closed)
        self.assertEqual(0, pool.status()["loaded_projects"])
        self.assertFalse(pool._pending)

    async def test_initializer_finishing_after_shutdown_is_closed_and_not_published(self):
        started = asyncio.Event()
        release = asyncio.Event()
        factory = _Factory(
            {
                "/projects/alpha": {
                    "initialize_started": started,
                    "initialize_release": release,
                    "ignore_initialize_cancel": True,
                },
            }
        )
        pool = SharedProjectPool(1, factory)
        pending = asyncio.create_task(pool.acquire(_selection("alpha")))
        await started.wait()
        close_task = asyncio.create_task(pool.close())
        await asyncio.sleep(0)
        release.set()
        result = await asyncio.gather(pending, return_exceptions=True)
        await close_task
        self.assertIsInstance(result[0], ProjectCapacityError)
        self.assertEqual(1, factory.gates["/projects/alpha"].closed)
        self.assertFalse(pool._pending)

    async def test_initializer_failure_closes_gateway_and_reports_actual_root(self):
        error = RuntimeError("init failed")
        factory = _Factory({"/projects/alpha": {"initialize_error": error}})
        pool = SharedProjectPool(1, factory)
        with patch("shared_project_pool.report_failure", return_value=(None, None)) as report:
            with self.assertRaisesRegex(RuntimeError, "init failed"):
                await pool.acquire(_selection("alpha"))
        self.assertEqual(1, factory.gates["/projects/alpha"].closed)
        report.assert_called_once()
        self.assertEqual(Path("/projects/alpha"), report.call_args.args[0])
        self.assertFalse(pool._pending)

    async def test_secondary_diagnostic_is_written_as_fixed_safe_stderr(self):
        factory = _Factory(
            {
                "/projects/alpha": {"initialize_error": RuntimeError("private detail")},
            }
        )
        pool = SharedProjectPool(1, factory)
        stream = io.StringIO()
        with patch("shared_project_pool.report_failure", return_value=(None, "sink failed")):
            with patch("shared_project_pool.sys.stderr", stream):
                with self.assertRaisesRegex(RuntimeError, "private detail"):
                    await pool.acquire(_selection("alpha"))
        self.assertEqual("caprmedio: technical diagnostics unavailable\n", stream.getvalue())

    async def test_eviction_close_failure_warns_and_does_not_leak_reservation(self):
        factory = _Factory(
            {
                "/projects/alpha": {"close_error": RuntimeError("eviction failed")},
            }
        )
        pool = SharedProjectPool(1, factory)
        first = await pool.acquire(_selection("alpha"))
        await pool.release(first)
        with patch("shared_project_pool.report_failure", return_value=(None, None)) as report:
            second = await pool.acquire(_selection("beta"))
        self.assertEqual(1, factory.gates["/projects/alpha"].closed)
        self.assertEqual(Path("/projects/alpha"), report.call_args.args[0])
        self.assertEqual("/projects/beta", str(second.selection.root))
        self.assertFalse(pool._pending)
        await pool.close()

    async def test_pending_and_busy_admissions_refuse_without_replay(self):
        started = asyncio.Event()
        factory = _Factory({"/projects/alpha": {"initialize_started": started}})
        pool = SharedProjectPool(1, factory)
        pending = asyncio.create_task(pool.acquire(_selection("alpha")))
        await started.wait()
        with self.assertRaises(ProjectCapacityError):
            await pool.acquire(_selection("beta"))
        self.assertNotIn("/projects/beta", factory.gates)
        await pool.close()
        await asyncio.gather(pending, return_exceptions=True)

    async def test_close_reports_gateway_failure_and_release_keeps_pool_empty(self):
        factory = _Factory({"/projects/alpha": {"close_error": RuntimeError("close failed")}})
        pool = SharedProjectPool(1, factory)
        entry = await pool.acquire(_selection("alpha"))
        with patch("shared_project_pool.report_failure", return_value=(None, None)) as report:
            await pool.close()
        await pool.release(entry)
        self.assertEqual(0, pool.status()["loaded_projects"])
        self.assertEqual(Path("/projects/alpha"), report.call_args.args[0])

    async def test_future_cancelled_gateway_close_propagates(self):
        factory = _Factory(
            {
                "/projects/alpha": {"close_error": FutureCancelledError()},
            }
        )
        pool = SharedProjectPool(1, factory)
        await pool.acquire(_selection("alpha"))
        with self.assertRaises(FutureCancelledError):
            await pool.close()


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
