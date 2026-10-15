"""Fresh build metadata is verified without changing source cache identity."""

from __future__ import annotations

import json
from dataclasses import replace
from pathlib import Path
import subprocess
import sys
import unittest

import test_project_mcp_launcher_images as fixtures

sys.path.insert(0, str(fixtures.DOCKER))
from image_provenance import ImageBuildProvenance  # noqa: E402
from runtime_images import FINGERPRINT_LABEL, SCHEMA_LABEL, ImageError, ImageManager  # noqa: E402


class ImageProvenanceTests(unittest.TestCase):
    def setUp(self) -> None:
        fixture = fixtures.ImageGoldenTests("runTest")
        fixture.setUp()
        self.source = fixture.source_fixture()
        self.temporary = fixture.fixture_root
        self.owner = ImageBuildProvenance(
            "c" * 64,
            "/owning-repository",
            ".caprmedio_caprmedio",
            "Named Project",
            "d" * 40,
        )

    def test_provenance_rejects_incomplete_ids_and_unsafe_owner_paths(self) -> None:
        for changes in (
            {"head_commit": "short"},
            {"project_id": "short"},
            {"project_root": "/owner/../other"},
            {"control_root": "../other"},
            {"project_name": " "},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                replace(self.owner, **changes)

    def test_fresh_build_attaches_and_verifies_owner_name_and_head(self) -> None:
        labels: dict[str, str] = {}
        calls: list[list[str]] = []

        def executor(argv: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
            calls.append(argv)
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "build" in argv:
                labels.update(
                    dict(
                        argv[index + 1].split("=", 1)
                        for index, value in enumerate(argv)
                        if value == "--label"
                    )
                )
                Path(argv[argv.index("--iidfile") + 1]).write_text(fixtures.IMAGE_ID)
            inspection = [
                {
                    "Id": fixtures.IMAGE_ID,
                    "Os": "linux",
                    "Architecture": "amd64",
                    "Config": {"Labels": labels},
                }
            ]
            return subprocess.CompletedProcess(argv, 0, json.dumps(inspection), "")

        manager = ImageManager(
            self.source,
            executor=executor,
            platform="linux/amd64",
            build_temp_root=self.temporary,
            build_provenance=self.owner,
        )
        self.assertEqual(manager.resolve(), fixtures.IMAGE_ID)
        self.assertEqual({key: labels[key] for key in self.owner.labels()}, self.owner.labels())
        plain = ImageManager(self.source, platform="linux/amd64")
        self.assertEqual(manager.identity(), plain.identity())
        self.assertEqual(sum("build" in call for call in calls), 1)

    def test_cached_unlabelled_and_foreign_images_are_reused_without_claiming_owner(self) -> None:
        for metadata in ({}, {"org.caprmedio.project": "f" * 64}):
            with self.subTest(metadata=metadata):
                calls: list[list[str]] = []
                manager = ImageManager(
                    self.source, platform="linux/amd64", build_provenance=self.owner
                )
                labels = {
                    SCHEMA_LABEL: "1",
                    FINGERPRINT_LABEL: manager.identity().fingerprint,
                    **metadata,
                }

                def executor(argv: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
                    calls.append(argv)
                    output = (
                        fixtures.IMAGE_ID
                        if "ls" in argv
                        else json.dumps(
                            [
                                {
                                    "Id": fixtures.IMAGE_ID,
                                    "Os": "linux",
                                    "Architecture": "amd64",
                                    "Config": {"Labels": labels},
                                }
                            ]
                        )
                    )
                    return subprocess.CompletedProcess(argv, 0, output, "")

                manager.executor = executor
                self.assertEqual(manager.resolve(), fixtures.IMAGE_ID)
                self.assertFalse(any("build" in call for call in calls))
                self.assertNotIn("org.caprmedio.source.head_commit", labels)

    def test_fresh_build_with_missing_provenance_label_is_refused(self) -> None:
        labels: dict[str, str] = {}

        def executor(argv: list[str], **kwargs: object) -> subprocess.CompletedProcess[str]:
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "build" in argv:
                labels.update(
                    dict(
                        argv[index + 1].split("=", 1)
                        for index, value in enumerate(argv)
                        if value == "--label"
                    )
                )
                labels.pop("org.caprmedio.source.head_commit")
                Path(argv[argv.index("--iidfile") + 1]).write_text(fixtures.IMAGE_ID)
            return subprocess.CompletedProcess(
                argv,
                0,
                json.dumps(
                    [
                        {
                            "Id": fixtures.IMAGE_ID,
                            "Os": "linux",
                            "Architecture": "amd64",
                            "Config": {"Labels": labels},
                        }
                    ]
                ),
                "",
            )

        manager = ImageManager(
            self.source,
            executor=executor,
            platform="linux/amd64",
            build_temp_root=self.temporary,
            build_provenance=self.owner,
        )
        with self.assertRaises(ImageError) as raised:
            manager.resolve()
        self.assertEqual(raised.exception.code, "BUILD_FAILED")


if __name__ == "__main__":
    unittest.main()
