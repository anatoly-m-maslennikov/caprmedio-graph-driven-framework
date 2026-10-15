"""Obsolete cleanup is integrated around the native installed launcher."""

import subprocess
from pathlib import Path
import unittest
from unittest.mock import patch

import test_release_cleanup as docker_tests
import test_simple_local_release as local_tests
from local_release import run_local_release
from project_selection import resolve_project


class LocalReleaseCleanupTests(unittest.TestCase):
    def fixture(self) -> tuple[local_tests.SimpleLocalReleaseTests, docker_tests.DockerFixture]:
        fixture = local_tests.SimpleLocalReleaseTests("runTest")
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        project_id = resolve_project(fixture.root).instance_id
        return fixture, docker_tests.DockerFixture(fixture.root, project_id)

    def test_all_stopped_predecessors_removed_before_launch_images_after_launch(self) -> None:
        fixture, docker = self.fixture()
        docker.add("1")
        docker.add("2")
        order: list[str] = []

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            if argv[0] == "docker":
                order.append(" ".join(argv[1:3]))
                return docker.run(argv, root)
            if argv[-1] == "project-mcp":
                self.assertEqual(docker.containers, {})
                order.append("launch")
            return subprocess.CompletedProcess(argv, 0, "", "")

        with (
            fixture._compiler(),
            patch("local_release._launcher_image", side_effect=[None, fixture.image_id]),
        ):
            result = run_local_release(fixture.root, run_id="cleanup", runner=runner)
        self.assertEqual(result["outcome"], "completed", result)
        self.assertEqual(order.count("container rm"), 2)
        self.assertEqual(order.count("image rm"), 2)
        self.assertLess(order.index("container rm"), order.index("launch"))
        self.assertGreater(order.index("image rm"), order.index("launch"))

    def test_existing_current_image_container_is_reused_without_stop_or_removal(self) -> None:
        fixture, docker = self.fixture()
        docker.add("1", Image=fixture.image_id, State={"Running": True, "Status": "running"})

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            if argv[:2] == ("docker", "ps"):
                return subprocess.CompletedProcess(argv, 0, "\n".join(docker.containers), "")
            if argv[0] == "docker":
                return docker.run(argv, root)
            return subprocess.CompletedProcess(argv, 0, "", "")

        with (
            fixture._compiler(),
            patch("local_release._launcher_image", return_value=fixture.image_id),
        ):
            result = run_local_release(fixture.root, run_id="reuse", runner=runner)
        self.assertEqual(result["outcome"], "completed", (result, docker.calls))
        self.assertEqual(len(docker.containers), 1)
        self.assertFalse(
            any(
                argv[1:3] in {("container", "stop"), ("container", "rm"), ("image", "rm")}
                for argv in docker.calls
            )
        )

    def test_failed_launcher_retains_predecessor_images(self) -> None:
        fixture, docker = self.fixture()
        docker.add("1")

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            if argv[0] == "docker":
                return docker.run(argv, root)
            return subprocess.CompletedProcess(argv, int(argv[-1] == "project-mcp"), "", "")

        with fixture._compiler():
            result = run_local_release(fixture.root, run_id="launch-failed", runner=runner)
        self.assertEqual(result["outcome"], "failed")
        self.assertEqual(result["failed_step"], "start_mcp")
        self.assertFalse(any(argv[1:3] == ("image", "rm") for argv in docker.calls))
        report = (fixture.root / str(result["report_path"])).read_text()
        self.assertIn("Removed obsolete stopped Project container " + "1" * 64, report)

    def test_prior_path_does_not_retry_pre_start_removal_failure(self) -> None:
        fixture, docker = self.fixture()
        _, image = docker.add("1")
        docker.fail = ("docker", "container", "rm")

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            if argv[:2] == ("docker", "ps"):
                return subprocess.CompletedProcess(argv, 0, "\n".join(docker.containers), "")
            if argv[0] == "docker":
                return docker.run(argv, root)
            return subprocess.CompletedProcess(argv, 0, "", "")

        with (
            fixture._compiler(),
            patch("local_release._launcher_image", side_effect=[image, fixture.image_id]),
        ):
            result = run_local_release(fixture.root, run_id="no-retry", runner=runner)
        self.assertEqual(result["outcome"], "completed_with_cleanup_pending")
        self.assertEqual(sum(argv[1:3] == ("container", "rm") for argv in docker.calls), 1)

    def test_failed_launcher_reports_exact_prior_running_container_removal(self) -> None:
        fixture, docker = self.fixture()
        identifier, image = docker.add("1", State={"Running": True, "Status": "running"})

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            if argv[:2] == ("docker", "ps"):
                return subprocess.CompletedProcess(argv, 0, "\n".join(docker.containers), "")
            if argv[0] == "docker":
                return docker.run(argv, root)
            return subprocess.CompletedProcess(argv, int(argv[-1] == "project-mcp"), "", "")

        with fixture._compiler(), patch("local_release._launcher_image", return_value=image):
            result = run_local_release(fixture.root, run_id="prior-failed", runner=runner)
        self.assertEqual(result["outcome"], "failed")
        report = (fixture.root / str(result["report_path"])).read_text()
        self.assertIn("Stopped and removed prior Project MCP container " + identifier, report)

    def test_post_smoke_does_not_retry_failed_prior_running_container_removal(self) -> None:
        fixture, docker = self.fixture()
        identifier, image = docker.add("1", State={"Running": True, "Status": "running"})
        docker.fail = ("docker", "container", "rm")

        def runner(argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
            if argv[:2] == ("docker", "ps"):
                return subprocess.CompletedProcess(argv, 0, identifier, "")
            if argv[1:3] == ("container", "stop"):
                docker.containers[identifier]["State"] = {"Running": False, "Status": "exited"}
            if argv[0] == "docker":
                return docker.run(argv, root)
            return subprocess.CompletedProcess(argv, 0, "", "")

        with (
            fixture._compiler(),
            patch("local_release._launcher_image", side_effect=[image, fixture.image_id]),
        ):
            result = run_local_release(fixture.root, run_id="prior-no-retry", runner=runner)
        self.assertEqual(result["outcome"], "completed_with_cleanup_pending")
        self.assertEqual(sum(argv[1:3] == ("container", "rm") for argv in docker.calls), 1)


if __name__ == "__main__":
    unittest.main()
