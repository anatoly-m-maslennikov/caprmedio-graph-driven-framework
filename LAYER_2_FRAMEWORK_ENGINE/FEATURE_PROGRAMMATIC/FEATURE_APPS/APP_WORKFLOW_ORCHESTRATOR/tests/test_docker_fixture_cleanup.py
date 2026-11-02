"""Fixture cleanup checks without starting Docker or collecting its E2E TestCase."""

from types import SimpleNamespace
import unittest
from unittest.mock import Mock, call, patch

import test_docker_e2e as fixtures


class DockerFixtureCleanupTests(unittest.IsolatedAsyncioTestCase):
    def fixture(self, *, worker=False, http=False):
        return SimpleNamespace(
            started=worker,
            http_started=http,
            runtime=Mock(),
            temporary=Mock(),
        )

    async def test_started_fixtures_remove_their_exact_compose_services(self):
        for worker, http in ((True, False), (False, True), (True, True)):
            with self.subTest(worker=worker, http=http):
                fixture = self.fixture(worker=worker, http=http)
                await fixtures.DockerEndToEnd.asyncTearDown(fixture)
                fixture.runtime.call.assert_called_once_with(
                    "down", "--volumes", http=http, timeout=60
                )
                fixture.runtime.mcp_http_stop.assert_not_called()
                fixture.temporary.cleanup.assert_called_once_with()

    async def test_partial_worker_start_is_still_removed(self):
        fixture = self.fixture()
        fixture.runtime.start.side_effect = RuntimeError("startup failed")
        fixture.runtime.call.return_value = ""
        with (
            patch.object(fixtures, "print"),
            self.assertRaisesRegex(RuntimeError, "startup failed"),
        ):
            await fixtures.DockerEndToEnd.start(fixture)
        self.assertTrue(fixture.started)
        await fixtures.DockerEndToEnd.asyncTearDown(fixture)
        self.assertEqual(
            fixture.runtime.call.call_args,
            call("down", "--volumes", http=False, timeout=60),
        )
        fixture.temporary.cleanup.assert_called_once_with()

    async def test_partial_http_start_is_still_removed(self):
        fixture = self.fixture()
        fixture.http_environment = Mock(return_value=12345)
        fixture.addCleanup = fixture.restore_http_environment = Mock()
        fixture.runtime.mcp_http_start.side_effect = RuntimeError("startup failed")
        with (
            patch.dict(fixtures.os.environ),
            self.assertRaisesRegex(RuntimeError, "startup failed"),
        ):
            await fixtures.DockerEndToEnd.test_anonymous_http_mcp_isolated_from_worker_and_agent(
                fixture
            )
        self.assertTrue(fixture.http_started)
        await fixtures.DockerEndToEnd.asyncTearDown(fixture)
        fixture.runtime.call.assert_called_once_with("down", "--volumes", http=True, timeout=60)
        fixture.temporary.cleanup.assert_called_once_with()

    async def test_temporary_directory_is_removed_even_when_docker_cleanup_fails(self):
        fixture = self.fixture(http=True)
        fixture.runtime.call.side_effect = RuntimeError("cleanup failed")
        with self.assertRaisesRegex(RuntimeError, "cleanup failed"):
            await fixtures.DockerEndToEnd.asyncTearDown(fixture)
        fixture.runtime.call.assert_called_once_with("down", "--volumes", http=True, timeout=60)
        fixture.temporary.cleanup.assert_called_once_with()

    async def test_unstarted_fixture_only_cleans_up_its_temporary_directory(self):
        fixture = self.fixture()
        await fixtures.DockerEndToEnd.asyncTearDown(fixture)
        fixture.runtime.call.assert_not_called()
        fixture.temporary.cleanup.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
