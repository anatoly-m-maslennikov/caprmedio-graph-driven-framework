"""Cleanup uses exact ownership and immutable IDs, without a Docker daemon."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "RELEASE_VERSION"))
from release_cleanup import (  # noqa: E402
    Cleanup,
    cleanup_obsolete_images,
    cleanup_stopped_containers,
)
from release_cleanup_identity import FINGERPRINT, SCHEMA  # noqa: E402

ROOT = Path("/project")
CURRENT = "sha256:" + "a" * 64
FINGER = "b" * 64


class DockerFixture:
    def __init__(self, root: Path = ROOT, project_id: str = "project") -> None:
        self.root = root
        self.project_id = project_id
        self.containers: dict[str, dict[str, object]] = {}
        self.images: dict[str, str] = {CURRENT: FINGER}
        self.references: set[str] = set()
        self.calls: list[tuple[str, ...]] = []
        self.fail: tuple[str, ...] | None = None

    def add(self, digit: str, **changes: object) -> tuple[str, str]:
        identifier, image = digit * 64, "sha256:" + digit * 64
        labels = {
            "org.caprmedio.project": self.project_id,
            "org.caprmedio.service": "mcp-http",
            "org.caprmedio.control_root": ".caprmedio_caprmedio",
            "org.caprmedio.host_project_root": str(self.root),
            FINGERPRINT: digit * 64,
        }
        row: dict[str, object] = {
            "Image": image,
            "State": {"Running": False, "Status": "exited"},
            "Config": {"Labels": labels},
        }
        row.update(changes)
        self.containers[identifier] = row
        if row["Image"] == image:
            self.images[image] = digit * 64
        return identifier, image

    def run(self, argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
        self.calls.append(argv)
        if self.fail is not None and argv[: len(self.fail)] == self.fail:
            return subprocess.CompletedProcess(argv, 1, "", "failure")
        output = ""
        if argv[1:3] == ("container", "ls"):
            output = (
                "in-use"
                if any(f"ancestor={image}" in argv for image in self.references)
                or any(f"ancestor={row['Image']}" in argv for row in self.containers.values())
                else ""
            )
            if "--no-trunc" in argv:
                output = "\n".join(self.containers)
        elif argv[1:3] == ("container", "inspect"):
            output = json.dumps(self.containers[argv[-1]])
        elif argv[1:3] == ("container", "rm"):
            del self.containers[argv[-1]]
        elif argv[1:3] == ("image", "ls"):
            output = "\n".join(self.images)
        elif argv[1:3] == ("image", "inspect"):
            image = argv[-1]
            output = json.dumps(
                {
                    "Id": image,
                    "Config": {
                        "Labels": {
                            SCHEMA: "1",
                            FINGERPRINT: self.images[image],
                        }
                    },
                }
            )
        return subprocess.CompletedProcess(argv, 0, output, "")


class ReleaseCleanupTests(unittest.TestCase):
    def sweep(self, docker: DockerFixture) -> Cleanup:
        return cleanup_stopped_containers(
            ROOT, "project", ".caprmedio_caprmedio", CURRENT, FINGER, docker.run
        )

    def test_multiple_obsolete_resources_and_unproven_orphans(self) -> None:
        docker = DockerFixture()
        _, first = docker.add("1")
        _, second = docker.add("2")
        orphan = "sha256:" + "f" * 64
        docker.images[orphan] = "f" * 64
        cleanup = self.sweep(docker)
        self.assertEqual(cleanup.images, {first, second})
        self.assertEqual(docker.containers, {})
        cleanup_obsolete_images(ROOT, CURRENT, FINGER, cleanup, docker.run)
        removed = {argv[-1] for argv in docker.calls if argv[1:3] == ("image", "rm")}
        self.assertEqual(removed, {first, second})
        self.assertTrue(cleanup.pending)
        self.assertTrue(any("without Project ownership" in note for note in cleanup.notes))

    def test_running_current_code_foreign_and_unknown_states_are_preserved(self) -> None:
        docker = DockerFixture()
        docker.add("1", State={"Running": True, "Status": "running"})
        docker.add("2", Image=CURRENT)
        _, matching = docker.add("3")
        docker.images[matching] = FINGER
        docker.add("4", Config={"Labels": {"org.caprmedio.project": "other"}})
        docker.add("5", State={"Running": False, "Status": "paused"})
        docker.add("6", State={"Running": "false", "Status": "exited"})
        cleanup = self.sweep(docker)
        self.assertEqual(len(docker.containers), 6)
        self.assertEqual(cleanup.images, set())
        self.assertTrue(cleanup.pending)
        self.assertFalse(any(argv[1:3] == ("container", "rm") for argv in docker.calls))

    def test_in_use_current_id_and_current_fingerprint_images_are_preserved(self) -> None:
        docker = DockerFixture()
        _, used = docker.add("1")
        docker.references.add(used)
        matching = "sha256:" + "2" * 64
        docker.images[matching] = FINGER
        cleanup = Cleanup(images={used, CURRENT, matching})
        cleanup_obsolete_images(ROOT, CURRENT, FINGER, cleanup, docker.run)
        self.assertTrue(cleanup.pending)
        self.assertFalse(any(argv[1:3] == ("image", "rm") for argv in docker.calls))

    def test_failed_discovery_inspection_and_removal_are_reported_without_retry(self) -> None:
        for command in (
            ("docker", "container", "ls"),
            ("docker", "container", "inspect"),
            ("docker", "container", "rm"),
        ):
            with self.subTest(command=command):
                docker = DockerFixture()
                docker.add("1")
                docker.fail = command
                cleanup = self.sweep(docker)
                self.assertTrue(cleanup.pending)
                self.assertEqual(len(docker.containers), 1)
                self.assertEqual(sum(argv[: len(command)] == command for argv in docker.calls), 1)

    def test_failed_image_removal_and_unproven_image_are_reported(self) -> None:
        for failed in (True, False):
            with self.subTest(failed=failed):
                docker = DockerFixture()
                _, old = docker.add("1")
                docker.containers.clear()
                if failed:
                    docker.fail = ("docker", "image", "rm")
                else:
                    docker.images[old] = "invalid"
                cleanup = Cleanup(images={old})
                cleanup_obsolete_images(ROOT, CURRENT, FINGER, cleanup, docker.run)
                self.assertTrue(cleanup.pending)
                self.assertLessEqual(sum(argv[1:3] == ("image", "rm") for argv in docker.calls), 1)

    def test_default_docker_invocation_has_timeout_and_no_force(self) -> None:
        with patch(
            "release_cleanup.subprocess.run",
            return_value=subprocess.CompletedProcess([], 0, "", ""),
        ) as run:
            cleanup = cleanup_stopped_containers(
                ROOT, "project", ".caprmedio_caprmedio", CURRENT, FINGER
            )
        self.assertFalse(cleanup.pending)
        self.assertEqual(run.call_args.kwargs["timeout"], 30)
        self.assertNotIn("--force", run.call_args.args[0])

    def test_post_smoke_repeat_does_not_retry_failed_container_removal(self) -> None:
        docker = DockerFixture()
        docker.add("1")
        docker.fail = ("docker", "container", "rm")
        cleanup = self.sweep(docker)
        cleanup_stopped_containers(
            ROOT,
            "project",
            ".caprmedio_caprmedio",
            CURRENT,
            FINGER,
            docker.run,
            cleanup=cleanup,
        )
        self.assertTrue(cleanup.pending)
        self.assertEqual(sum(argv[1:3] == ("container", "rm") for argv in docker.calls), 1)


if __name__ == "__main__":
    unittest.main()
