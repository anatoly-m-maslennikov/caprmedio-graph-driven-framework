"""Golden contract for Project MCP image identity and admission."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
sys.path.insert(0, str(DOCKER))

from runtime_images import ImageError, ImageManager  # noqa: E402


GOLDENS = Path(__file__).parent / "launcher_golden" / "image_cases.json"
IMAGE_ID = "sha256:" + "a" * 64
FRAMEWORK_VERSION = "0.4.4.9"


class ImageGoldenTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp" / "launcher-epic-1829" / "images"
        parent.mkdir(parents=True, exist_ok=True)
        self.fixture_root = Path(tempfile.mkdtemp(dir=parent))

    def manager(self, source_root: Path, executor) -> ImageManager:
        tagged, sources, inspections = set(), {}, {}

        def tagging_executor(argv, **kwargs):
            command = tuple(argv)
            if command[:3] == ("docker", "image", "tag"):
                tagged.add(command[-1])
                sources[command[-1]] = command[-2]
                return subprocess.CompletedProcess(argv, 0, "", "")
            if command[:3] == ("docker", "image", "inspect") and command[-1].startswith("caprmedio-runtime:"):
                tag = command[-1]
                if tag not in tagged:
                    return subprocess.CompletedProcess(argv, 1, "", "")
                payload = json.loads(inspections[sources[tag]])
                payload[0]["RepoTags"] = sorted(set(payload[0].get("RepoTags", [])) | {tag})
                return subprocess.CompletedProcess(argv, 0, json.dumps(payload), "")
            if command[:3] == ("docker", "image", "ls") and command[-1].startswith("caprmedio-runtime:"):
                return subprocess.CompletedProcess(argv, 0, "", "")
            result = executor(argv, **kwargs)
            if command[:3] == ("docker", "image", "inspect") and result.returncode == 0:
                inspections[command[-1]] = result.stdout
            return result

        return ImageManager(
            source_root, executor=tagging_executor, timeout=7, uid=1000, gid=1000, platform="linux/amd64"
        )

    def source_fixture(self) -> Path:
        """Minimal admitted build closure; Project state never enters this tree."""
        root = self.fixture_root / "source"
        docker = root / "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker"
        docker.mkdir(parents=True)
        (root / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
        (root / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        (root / "version.toml").write_text(
            f'[framework]\nversion = "{FRAMEWORK_VERSION}"\n', encoding="utf-8"
        )
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

    def test_explicit_private_build_root_preserves_image_identity_and_contains_attempt(self) -> None:
        source = self.source_fixture()
        parent = self.fixture_root / "project-temp/run-private-images"
        parent.mkdir(parents=True)
        identity = self.manager(source, lambda *_a, **_k: None).identity()
        def executor(argv, **_kwargs):
            if "build" in argv:
                iid = Path(argv[argv.index("--iidfile") + 1])
                self.assertTrue(iid.is_relative_to(parent))
                iid.write_text(IMAGE_ID, encoding="ascii")
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            inspection = [{"Id": IMAGE_ID, "Created": "2026-10-21T14:15:16.987654321Z", "RepoTags": [],
                           "Os": "linux", "Architecture": "amd64", "Config": {"Labels": {
                "org.caprmedio.runtime.schema": "1", "org.caprmedio.runtime.fingerprint": identity.fingerprint,
                "org.opencontainers.image.version": FRAMEWORK_VERSION,
            }}}]
            return subprocess.CompletedProcess(argv, 0, json.dumps(inspection), "")
        manager = self.manager(source, executor)
        manager.build_temp_root = parent
        self.assertEqual(identity, manager.identity())
        self.assertEqual(IMAGE_ID, manager.resolve())
        self.assertEqual(1, len(list(parent.iterdir())))

    def test_explicit_missing_or_symlink_build_root_refuses_without_fallback(self) -> None:
        source = self.source_fixture()
        target = self.fixture_root / "real-temp"
        target.mkdir()
        alias = self.fixture_root / "alias-temp"
        alias.symlink_to(target, target_is_directory=True)
        for parent in (self.fixture_root / "missing-temp", alias):
            with self.subTest(parent=parent):
                calls = []
                def executor(argv, **_kwargs):
                    calls.append(tuple(argv))
                    return subprocess.CompletedProcess(argv, 0, "", "")
                manager = ImageManager(source, executor=executor, uid=1000, gid=1000, platform="linux/amd64", build_temp_root=parent)
                with self.assertRaises(ImageError) as raised:
                    manager.resolve()
                self.assertEqual("BUILD_FAILED", raised.exception.code)
                self.assertFalse(any("build" in argv for argv in calls))
        self.assertEqual([], list(target.iterdir()))

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
                "org.opencontainers.image.version": FRAMEWORK_VERSION,
            }
            inspection = json.dumps([{
                "Id": IMAGE_ID,
                "Created": "2026-10-21T14:15:16.987654321Z",
                "RepoTags": [],
                "Os": "linux",
                "Architecture": "amd64",
                "Config": {"Labels": labels},
            }])
            return subprocess.CompletedProcess(argv, 0, inspection, "")

        resolved = self.manager(source, executor).resolve(build_if_missing=False)
        self.assertEqual(IMAGE_ID, resolved)
        flattened = " ".join(" ".join(call) for call in calls)
        self.assertIn("label=org.caprmedio.runtime.schema=1", flattened)
        self.assertIn(
            f"label=org.caprmedio.runtime.fingerprint={expected.fingerprint}", flattened
        )
        self.assertNotIn(" build ", f" {flattened} ")

    def test_untagged_matching_image_is_reused_without_building(self) -> None:
        source = self.source_fixture()
        identity = self.manager(source, lambda *_a, **_k: None).identity()
        calls = []

        def executor(argv, **_kwargs):
            calls.append(tuple(argv))
            if "ls" in argv:
                # Docker's default listing omits intermediate untagged images.
                output = IMAGE_ID + "\n" if "--all" in argv else ""
                return subprocess.CompletedProcess(argv, 0, output, "")
            self.assertIn("inspect", argv)
            inspection = json.dumps([{
                "Id": IMAGE_ID, "Created": "2026-10-21T14:15:16.987654321Z", "RepoTags": [],
                "Os": "linux", "Architecture": "amd64",
                "Config": {"Labels": {
                    "org.caprmedio.runtime.schema": "1",
                    "org.caprmedio.runtime.fingerprint": identity.fingerprint,
                    "org.opencontainers.image.version": FRAMEWORK_VERSION,
                }},
            }])
            return subprocess.CompletedProcess(argv, 0, inspection, "")

        self.assertEqual(IMAGE_ID, self.manager(source, executor).resolve(build_if_missing=False))
        self.assertFalse(any("build" in call for call in calls))

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
                "Created": "2026-10-21T14:15:16.987654321Z",
                "RepoTags": [],
                "Os": "linux",
                "Architecture": "amd64",
                "Config": {"Labels": {
                    "org.caprmedio.runtime.schema": "1",
                    "org.caprmedio.runtime.fingerprint": initial.fingerprint,
                    "org.opencontainers.image.version": FRAMEWORK_VERSION,
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

    def test_build_uses_private_sibling_buildx_client_state_only_for_that_subprocess(self) -> None:
        source = self.source_fixture()
        manager = self.manager(source, lambda *_a, **_k: None)
        identity = manager.identity()
        calls = []
        client = {"HOME": "/synthetic-home", "PATH": "/synthetic-bin",
                  "DOCKER_CONFIG": "/synthetic-docker-config"}
        caller = dict(client, AWS_SECRET_ACCESS_KEY="synthetic-private-secret")

        def executor(argv, **kwargs):
            argv = tuple(argv)
            calls.append((argv, kwargs))
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "build" in argv:
                iidfile = Path(argv[argv.index("--iidfile") + 1])
                iidfile.write_text(IMAGE_ID + "\n", encoding="utf-8")
                return subprocess.CompletedProcess(argv, 0, "", "")
            inspection = json.dumps([{
                "Id": IMAGE_ID, "Created": "2026-10-21T14:15:16.987654321Z", "RepoTags": [],
                "Os": "linux", "Architecture": "amd64",
                "Config": {"Labels": {
                    "org.caprmedio.runtime.schema": "1",
                    "org.caprmedio.runtime.fingerprint": identity.fingerprint,
                    "org.opencontainers.image.version": FRAMEWORK_VERSION,
                }},
            }])
            return subprocess.CompletedProcess(argv, 0, inspection, "")

        manager = self.manager(source, executor)
        with patch.dict(os.environ, caller, clear=True):
            self.assertEqual(IMAGE_ID, manager.resolve())
        self.assertEqual(identity, manager.identity())
        build, build_kwargs = next((call for call in calls if "build" in call[0]))
        state = Path(build_kwargs["env"]["BUILDX_CONFIG"])
        self.assertEqual(build[build.index("--iidfile") + 1], str(state.parent / "image.id"))
        self.assertEqual("buildx", state.name)
        self.assertTrue(state.is_dir())
        self.assertEqual(dict(client, BUILDX_CONFIG=str(state)), build_kwargs["env"])
        self.assertNotIn("synthetic-private-secret", build_kwargs["env"].values())
        self.assertNotIn(str(state), build)
        self.assertNotIn(str(state), " ".join(build))
        for command, kwargs in calls:
            if "build" not in command:
                self.assertNotIn("env", kwargs)


if __name__ == "__main__":
    unittest.main()
