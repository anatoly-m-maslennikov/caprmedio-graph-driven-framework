import asyncio
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from runtime_request_context import (  # noqa: E402
    RuntimeRequestContext,
    bind_request_context,
    current_request_context,
)


class RuntimeRequestContextTest(unittest.TestCase):
    def test_nested_context_and_exception_restore_previous_binding(self):
        self.assertIsNone(current_request_context())
        outer = RuntimeRequestContext("native session")
        with bind_request_context(outer):
            self.assertIs(current_request_context(), outer)
            with self.assertRaisesRegex(RuntimeError, "failure"):
                with bind_request_context(RuntimeRequestContext("another")):
                    raise RuntimeError("failure")
            self.assertIs(current_request_context(), outer)
        self.assertIsNone(current_request_context())

    def test_optional_context_and_invalid_ids(self):
        with bind_request_context(RuntimeRequestContext()):
            self.assertIsNone(current_request_context().session_id)
        for invalid in ("", " ", 1, False):
            with self.subTest(invalid=invalid), self.assertRaises(ValueError):
                RuntimeRequestContext(invalid)
        with self.assertRaises(TypeError):
            with bind_request_context(None):
                pass

    def test_concurrent_async_calls_do_not_share_session_context(self):
        async def exercise():
            entered = asyncio.Event()
            proceed = asyncio.Event()

            async def first():
                with bind_request_context(RuntimeRequestContext("first")):
                    entered.set()
                    await proceed.wait()
                    return current_request_context().session_id

            async def second():
                await entered.wait()
                self.assertIsNone(current_request_context())
                with bind_request_context(RuntimeRequestContext("second")):
                    proceed.set()
                    await asyncio.sleep(0)
                    return current_request_context().session_id

            return await asyncio.gather(first(), second())

        self.assertEqual(["first", "second"], asyncio.run(exercise()))
        self.assertIsNone(current_request_context())


if __name__ == "__main__":
    unittest.main()
