"""Owned orphan discovery never upgrades missing or foreign ownership claims."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import unittest

import test_release_cleanup as fixtures
from release_cleanup import Cleanup, cleanup_obsolete_images
from release_cleanup_identity import owner_labels


class OwnedDocker(fixtures.DockerFixture):
    def __init__(self) -> None:
        super().__init__()
        self.metadata_overrides: dict[str, dict[str, str]] = {}

    def run(self, argv: tuple[str, ...], root: Path) -> subprocess.CompletedProcess[str]:
        result = super().run(argv, root)
        if argv[1:3] == ("image", "inspect") and result.returncode == 0:
            value = json.loads(result.stdout)
            value["Config"]["Labels"].update(self.metadata_overrides.get(argv[-1], {}))
            result.stdout = json.dumps(value)
        return result


class ReleaseImageOwnershipTests(unittest.TestCase):
    def test_owned_orphan_removed_without_container_link_or_commit_gate(self) -> None:
        docker = OwnedDocker()
        image = "sha256:" + "1" * 64
        docker.images[image] = "1" * 64
        owner = owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio")
        docker.metadata_overrides[image] = owner
        cleanup = Cleanup(owner=owner)
        cleanup_obsolete_images(
            fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
        )
        self.assertIn(("docker", "image", "rm", image), docker.calls)
        self.assertFalse(cleanup.pending)

    def test_unlabelled_partial_or_conflicting_owner_is_retained_pending(self) -> None:
        owner = owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio")
        for metadata in (
            {},
            {"org.caprmedio.project": "c" * 64},
            {**owner, "org.caprmedio.host_project_root": "/different"},
        ):
            for linked in (False, True):
                if linked and not metadata:
                    continue
                with self.subTest(metadata=metadata, linked=linked):
                    docker = OwnedDocker()
                    image = "sha256:" + "1" * 64
                    docker.images[image] = "1" * 64
                    docker.metadata_overrides[image] = metadata
                    cleanup = Cleanup(owner=owner, images={image} if linked else set())
                    cleanup_obsolete_images(
                        fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
                    )
                    self.assertTrue(cleanup.pending)
                    self.assertNotIn(("docker", "image", "rm", image), docker.calls)

    def test_foreign_owned_image_retained_even_with_project_container_link(self) -> None:
        docker = OwnedDocker()
        image = "sha256:" + "1" * 64
        docker.images[image] = "1" * 64
        owner = owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio")
        docker.metadata_overrides[image] = owner_labels(Path("/foreign"), "f" * 64, ".caprmedio_foreign")
        cleanup = Cleanup(owner=owner, images={image})
        cleanup_obsolete_images(
            fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
        )
        self.assertFalse(cleanup.pending)
        self.assertNotIn(("docker", "image", "rm", image), docker.calls)

    def test_same_fingerprint_owned_rebuild_is_removed(self) -> None:
        docker = OwnedDocker()
        image = "sha256:" + "1" * 64
        docker.images[image] = fixtures.FINGER
        owner = owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio")
        docker.metadata_overrides[image] = owner
        cleanup = Cleanup(owner=owner)
        cleanup_obsolete_images(
            fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
        )
        self.assertIn(("docker", "image", "rm", image), docker.calls)
        self.assertFalse(cleanup.pending)

    def test_exact_candidate_is_protected_but_same_fingerprint_rebuild_is_not(self) -> None:
        docker = OwnedDocker()
        image = "sha256:" + "1" * 64
        docker.images[image] = fixtures.FINGER
        owner = owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio")
        docker.metadata_overrides[image] = owner
        cleanup = Cleanup(owner=owner, images={fixtures.CURRENT, image})
        cleanup_obsolete_images(
            fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
        )
        self.assertNotIn(("docker", "image", "rm", fixtures.CURRENT), docker.calls)
        self.assertIn(("docker", "image", "rm", image), docker.calls)

    def test_unowned_orphan_and_linked_image_are_retained_pending(self) -> None:
        for linked in (False, True):
            with self.subTest(linked=linked):
                docker = OwnedDocker()
                image = "sha256:" + "1" * 64
                docker.images[image] = "1" * 64
                cleanup = Cleanup(owner=owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio"))
                if linked:
                    cleanup.images.add(image)
                cleanup_obsolete_images(
                    fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
                )
                self.assertTrue(cleanup.pending)
                self.assertNotIn(("docker", "image", "rm", image), docker.calls)

    def test_owned_image_with_container_use_is_preserved_pending(self) -> None:
        docker = OwnedDocker()
        image = "sha256:" + "1" * 64
        docker.images[image] = "1" * 64
        docker.references.add(image)
        owner = owner_labels(fixtures.ROOT, "c" * 64, ".caprmedio_caprmedio")
        docker.metadata_overrides[image] = owner
        cleanup = Cleanup(owner=owner)
        cleanup_obsolete_images(
            fixtures.ROOT, fixtures.CURRENT, fixtures.FINGER, cleanup, docker.run
        )
        self.assertTrue(cleanup.pending)
        self.assertNotIn(("docker", "image", "rm", image), docker.calls)


if __name__ == "__main__":
    unittest.main()
