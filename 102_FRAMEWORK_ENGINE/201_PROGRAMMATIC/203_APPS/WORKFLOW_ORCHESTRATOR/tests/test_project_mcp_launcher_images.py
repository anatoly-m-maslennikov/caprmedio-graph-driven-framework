"""Golden contract for Project MCP image identity and admission."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
sys.path.insert(0, str(DOCKER))

from runtime_images import ImageError, ImageManager  # noqa: E402


GOLDENS = Path(__file__).parent / "launcher_golden" / "image_cases.json"
IMAGE_ID = "sha256:" + "a" * 64


class ImageGoldenTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp" / "launcher-epic-1829" / "images"
        parent.mkdir(parents=True, exist_ok=True)
        self.fixture_root = Path(tempfile.mkdtemp(dir=parent))

    def manager(self, source_root: Path, executor) -> ImageManager:
        return ImageManager(
            source_root, executor=executor, timeout=7, uid=1000, gid=1000, platform="linux/amd64"
        )

    def source_fixture(self) -> Path:
        """Minimal admitted build closure; Project state never enters this tree."""
        root = self.fixture_root / "source"
        docker = root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker"
        docker.mkdir(parents=True)
        (root / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
        (root / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        (docker / "Dockerfile").write_text("FROM scratch\n", encoding="utf-8")
        (docker / "Dockerfile.dockerignore").write_text(".git\n", encoding="utf-8")
        (docker.parent / "engine.py").write_text("ENGINE = 'one'\n", encoding="utf-8")
        return root

    def test_golden_corpus_covers_identity_and_exact_image_refusal_codes(self) -> None:
        cases = json.loads(GOLDENS.read_text(encoding="utf-8"))
        self.assertEqual(10, len(cases))
        self.assertEqual(
            {"IMAGE_INPUT_UNAVAILABLE", "IMAGE_REFUSED", "BUILD_FAILED"},
            {case["condition"] for case in cases if "condition" in case},
        )

    def test_identity_is_source_bound_but_independent_of_project_context(self) -> None:
        source = APP.parents[3]
        no_docker = lambda *_args, **_kwargs: self.fail("identity must not invoke Docker")
        before = self.manager(source, no_docker).identity()

        project_state = self.fixture_root / "project" / ".caprmedio_demo"
        project_state.mkdir(parents=True)
        (project_state / "caprmedio_project_settings.toml").write_text("changed", encoding="utf-8")
        (project_state / "generated-output.json").write_text("changed", encoding="utf-8")
        after = self.manager(source, no_docker).identity()

        self.assertEqual(before.fingerprint, after.fingerprint)
        self.assertEqual("linux/amd64", before.platform)
        self.assertTrue(before.manifest)

    def test_admitted_source_change_changes_fingerprint(self) -> None:
        source = self.source_fixture()
        no_docker = lambda *_args, **_kwargs: self.fail("identity must not invoke Docker")
        before = self.manager(source, no_docker).identity()
        engine = source / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/engine.py"
        engine.write_text("ENGINE = 'two'\n", encoding="utf-8")
        after = self.manager(source, no_docker).identity()
        self.assertNotEqual(before.fingerprint, after.fingerprint)

    def test_missing_or_changed_required_source_input_is_attributable(self) -> None:
        missing_source = self.fixture_root / "missing-source"
        missing_source.mkdir()
        with self.assertRaises(ImageError) as raised:
            self.manager(missing_source, lambda *_a, **_k: None).identity()
        self.assertEqual("IMAGE_INPUT_UNAVAILABLE", raised.exception.code)

    def test_matching_image_requires_the_exact_schema_and_source_fingerprint_labels(self) -> None:
        source = APP.parents[3]
        expected = self.manager(source, lambda *_a, **_k: None).identity()
        calls = []

        def executor(argv, **_kwargs):
            calls.append(tuple(argv))
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, IMAGE_ID + "\n", "")
            labels = {
                "org.caprmedio.runtime.schema": "1",
                "org.caprmedio.runtime.fingerprint": expected.fingerprint,
            }
            inspection = json.dumps([{"Id": IMAGE_ID, "Config": {"Labels": labels}}])
            return subprocess.CompletedProcess(argv, 0, inspection, "")

        resolved = self.manager(source, executor).resolve(build_if_missing=False)
        self.assertEqual(IMAGE_ID, resolved)
        flattened = " ".join(" ".join(call) for call in calls)
        self.assertIn("label=org.caprmedio.runtime.schema=1", flattened)
        self.assertIn(
            f"label=org.caprmedio.runtime.fingerprint={expected.fingerprint}", flattened
        )
        self.assertNotIn(" build ", f" {flattened} ")

    def test_mutable_or_stale_explicit_images_refuse_without_docker_build(self) -> None:
        calls = []

        def executor(argv, **kwargs):
            calls.append((tuple(argv), kwargs))
            return subprocess.CompletedProcess(argv, 0, "", "")

        manager = self.manager(APP.parents[3], executor)
        for value in ("caprmedio-runtime:local", "sha256:" + "b" * 64):
            with self.subTest(value=value), self.assertRaises(ImageError) as raised:
                manager.resolve(explicit_id=value)
            self.assertEqual("IMAGE_REFUSED", raised.exception.code)
        self.assertFalse(any("build" in command for command, _kwargs in calls))

    def test_no_build_refuses_missing_matching_image_and_default_build_failure_is_attributable(self) -> None:
        def empty_lookup(argv, **_kwargs):
            return subprocess.CompletedProcess(argv, 0, "", "")

        manager = self.manager(APP.parents[3], empty_lookup)
        with self.assertRaises(ImageError) as refused:
            manager.resolve(build_if_missing=False)
        self.assertEqual("IMAGE_REFUSED", refused.exception.code)

        calls = []

        def failed_build(argv, **_kwargs):
            calls.append(tuple(argv))
            if "build" in argv:
                return subprocess.CompletedProcess(argv, 1, "", "safe builder failure")
            return subprocess.CompletedProcess(argv, 0, "", "")

        with self.assertRaises(ImageError) as failed:
            self.manager(APP.parents[3], failed_build).resolve()
        self.assertEqual("BUILD_FAILED", failed.exception.code)
        self.assertTrue(any("build" in command for command in calls))

    def test_default_build_captures_iidfile_and_reinspects_linux_amd64_image(self) -> None:
        source = self.source_fixture()
        initial = self.manager(source, lambda *_a, **_k: None).identity()
        calls = []

        def executor(argv, **_kwargs):
            argv = tuple(argv)
            calls.append(argv)
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "build" in argv:
                iidfile = Path(argv[argv.index("--iidfile") + 1])
                iidfile.write_text(IMAGE_ID + "\n", encoding="utf-8")
                return subprocess.CompletedProcess(argv, 0, "", "")
            inspection = json.dumps([{
                "Id": IMAGE_ID,
                "Os": "linux",
                "Architecture": "amd64",
                "Config": {"Labels": {
                    "org.caprmedio.runtime.schema": "1",
                    "org.caprmedio.runtime.fingerprint": initial.fingerprint,
                }},
            }])
            return subprocess.CompletedProcess(argv, 0, inspection, "")

        self.assertEqual(IMAGE_ID, self.manager(source, executor).resolve())
        build = next(command for command in calls if "build" in command)
        self.assertIn("--iidfile", build)
        self.assertIn("--platform", build)
        self.assertIn("linux/amd64", build)
        inspections = [command for command in calls if "inspect" in command]
        self.assertTrue(inspections, calls)
        self.assertTrue(any(IMAGE_ID in command for command in inspections))


if __name__ == "__main__":
    unittest.main()
