"""Exercise the existing source builder with a fixture-only Docker executor."""

from pathlib import Path
import json
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import full_suite_docker as docker  # noqa: E402
from runtime_images import DOCKERFILE, DOCKERIGNORE, FINGERPRINT_LABEL, SCHEMA_LABEL  # noqa: E402

IMAGE = "sha256:" + "a" * 64
FRAMEWORK_VERSION = "0.4.4.9"


class CurrentSourceImageBuildTests(unittest.TestCase):
    def setUp(self):
        parent = Path(__file__).resolve().parents[2] / ".caprmedio_tmp/tests/image-build"
        parent.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        for relative in ("pyproject.toml", "uv.lock", "version.toml", DOCKERFILE, DOCKERIGNORE):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            content = (
                f'[framework]\nversion = "{FRAMEWORK_VERSION}"\n'
                if relative == "version.toml" else "fixture-current-code"
            )
            path.write_text(content, encoding="utf-8")

    def test_real_builder_copies_current_bytes_and_passes_actual_immutable_id(self):
        labels, commands, tags = {}, [], set()

        def execute(argv, **_kwargs):
            commands.append(argv)
            if argv[:3] == ["docker", "image", "tag"]:
                tags.add(argv[-1])
                return subprocess.CompletedProcess(argv, 0, "")
            if argv[:3] == ["docker", "image", "inspect"] and argv[-1].startswith("caprmedio-runtime:"):
                if argv[-1] not in tags:
                    return subprocess.CompletedProcess(argv, 1, "")
                return subprocess.CompletedProcess(
                    argv, 0, json.dumps([{"Id": IMAGE, "Created": "2026-10-21T14:15:16.987654321Z",
                                          "RepoTags": [argv[-1]], "Config": {"Labels": labels},
                                          "Os": "linux", "Architecture": "arm64"}])
                )
            if argv[:2] == ["docker", "build"]:
                for index, argument in enumerate(argv):
                    if argument == "--label":
                        key, value = argv[index + 1].split("=", 1)
                        labels[key] = value
                context = Path(argv[-1])
                self.assertEqual("fixture-current-code", (context / DOCKERFILE).read_text())
                Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE)
                return subprocess.CompletedProcess(argv, 0, "")
            if argv[:3] == ["docker", "image", "inspect"]:
                value = {
                    "Id": IMAGE,
                    "Created": "2026-10-21T14:15:16.987654321Z",
                    "RepoTags": [],
                    "Config": {"Labels": labels},
                    "Os": "linux",
                    "Architecture": "arm64"
                    if docker.ImageManager(self.root).platform == "linux/arm64"
                    else "amd64",
                }
                return subprocess.CompletedProcess(argv, 0, json.dumps([value]))
            return subprocess.CompletedProcess(argv, 0, "")

        with patch.object(docker, "_bounded_run", side_effect=execute):
            with docker.current_code_test_image(self.root) as environment:
                self.assertEqual(IMAGE, environment["CAPRMEDIO_FIRST_CUT_HTTP_IMAGE"])
                self.assertEqual(IMAGE, environment["CAPRMEDIO_IMAGE"])
        self.assertEqual("1", labels[SCHEMA_LABEL])
        self.assertEqual(64, len(labels[FINGERPRINT_LABEL]))
        self.assertEqual(FRAMEWORK_VERSION, labels["org.opencontainers.image.version"])
        self.assertEqual(32, len(labels[docker.ATTEMPT_LABEL]))
        self.assertEqual(1, sum(argv[:2] == ["docker", "build"] for argv in commands))
        self.assertEqual(["docker", "image", "rm", IMAGE], commands[-1])
        expected = "caprmedio-runtime:0.4.4.9-20261021T141516Z-aaaaaaaaaaaa"
        self.assertEqual(["docker", "image", "tag", IMAGE, expected],
                         next(argv for argv in commands if argv[:3] == ["docker", "image", "tag"]))
        self.assertEqual([expected], [argv[-1] for argv in commands
                                      if argv[:3] == ["docker", "image", "ls"]])

    def test_symlink_scratch_parent_cannot_create_build_files_outside_project(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.root / ".caprmedio_tmp").symlink_to(outside, target_is_directory=True)
        with patch.object(docker, "ImageManager") as manager:
            with self.assertRaises(OSError):
                with docker.current_code_test_image(self.root):
                    self.fail("unsafe scratch admitted")
            manager.assert_not_called()
        self.assertEqual([], list(outside.iterdir()))


if __name__ == "__main__":
    unittest.main()
