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

from runtime_images import ImageError, ImageManager, RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY, STATUS_MODEL, CANDIDATE_SCHEMA  # noqa: E402


GOLDENS = Path(__file__).parent / "launcher_golden" / "image_cases.json"
IMAGE_ID = "sha256:" + "a" * 64
FRAMEWORK_VERSION = "0.4.4.9"


class ImageGoldenTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[2] / ".caprmedio_tmp/CA-P-2791/CA-P-2818/images"
        parent.mkdir(parents=True, exist_ok=True)
        self.fixture_root = Path(tempfile.mkdtemp(dir=parent))
        self.registry = patch("runtime_images._compile_relation_registry", return_value=b'{"schema_version":1}\n')
        self.registry.start()
        self.addCleanup(self.registry.stop)
        self.schema = patch("runtime_images._compile_workbench_schema", return_value=b'{"schema_version":1}\n')
        self.schema.start()
        self.addCleanup(self.schema.stop)
        self.tools = patch("runtime_images._compile_tool_registry", return_value=b'{"schema_version":1}\n')
        self.tools.start()
        self.addCleanup(self.tools.stop)
        lifecycle = patch("runtime_images._compile_lifecycle_assets", return_value=(b'{"schema_version":1}\n', b'{"schema_version":1}\n'))
        lifecycle.start()
        self.addCleanup(lifecycle.stop)

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
            source_root, executor=tagging_executor, timeout=7, uid=1000, gid=1000, platform="linux/amd64",
            project_root=APP.parents[2],
        )

    def source_fixture(self) -> Path:
        """Minimal admitted build closure; Project state never enters this tree."""
        root = self.fixture_root / "source"
        docker = root / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/docker"
        docker.mkdir(parents=True)
        (root / "pyproject.toml").write_text("[project]\nname = 'fixture'\n", encoding="utf-8")
        (root / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        (root / "version.toml").write_text(
            f'[framework]\nversion = "{FRAMEWORK_VERSION}"\n', encoding="utf-8"
        )
        (docker / "Dockerfile").write_text("FROM scratch\n", encoding="utf-8")
        (docker / "Dockerfile.dockerignore").write_text(".git\n", encoding="utf-8")
        (docker.parent / "server.py").write_text("SERVER = 'one'\n", encoding="utf-8")
        for relative in (RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY, STATUS_MODEL, CANDIDATE_SCHEMA):
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'{"schema_version":1}\n')
        return root

    def test_golden_corpus_covers_identity_and_exact_image_refusal_codes(self) -> None:
        cases = json.loads(GOLDENS.read_text(encoding="utf-8"))
        self.assertEqual(10, len(cases))
        self.assertEqual(
            {"IMAGE_INPUT_UNAVAILABLE", "IMAGE_REFUSED", "BUILD_FAILED"},
            {case["condition"] for case in cases if "condition" in case},
        )

    def test_identity_is_source_bound_but_independent_of_project_context(self) -> None:
        source = APP.parents[2]
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

    def test_lifecycle_assets_enter_context_and_fingerprint(self) -> None:
        source = self.source_fixture()
        manager = self.manager(source, lambda *_a, **_k: self.fail("Docker is not needed"))
        before = manager.identity()
        context = self.fixture_root / "context"
        context.mkdir()
        manager._assemble(context, before)
        self.assertEqual(before.status_model, (context / STATUS_MODEL).read_bytes())
        self.assertEqual(before.candidate_schema, (context / CANDIDATE_SCHEMA).read_bytes())
        for index in (0, 1):
            assets = [before.status_model, before.candidate_schema]
            assets[index] += b"changed"
            with patch("runtime_images._compile_lifecycle_assets", return_value=tuple(assets)):
                self.assertNotEqual(before.fingerprint, manager.identity().fingerprint)

    def test_admitted_source_change_changes_fingerprint(self) -> None:
        source = self.source_fixture()
        no_docker = lambda *_args, **_kwargs: self.fail("identity must not invoke Docker")
        before = self.manager(source, no_docker).identity()
        server = source / "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/server.py"
        server.write_text("SERVER = 'two'\n", encoding="utf-8")
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
                "org.opencontainers.image.version": identity.version,
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
                manager = ImageManager(source, executor=executor, uid=1000, gid=1000, platform="linux/amd64",
                                       build_temp_root=parent, project_root=APP.parents[2])
                with self.assertRaises(ImageError) as raised:
                    manager.resolve()
                self.assertEqual("BUILD_FAILED", raised.exception.code)
                self.assertFalse(any("build" in argv for argv in calls))
        self.assertEqual([], list(target.iterdir()))

    def test_matching_image_requires_the_exact_schema_and_source_fingerprint_labels(self) -> None:
        source = self.source_fixture()
        expected = self.manager(source, lambda *_a, **_k: None).identity()
        calls = []

        def executor(argv, **_kwargs):
            calls.append(tuple(argv))
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, IMAGE_ID + "\n", "")
            labels = {
                "org.caprmedio.runtime.schema": "1",
                "org.caprmedio.runtime.fingerprint": expected.fingerprint,
                "org.opencontainers.image.version": expected.version,
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

        manager = self.manager(APP.parents[2], executor)
        for value in ("caprmedio-runtime:local", "sha256:" + "b" * 64):
            with self.subTest(value=value), self.assertRaises(ImageError) as raised:
                manager.resolve(explicit_id=value)
            self.assertEqual("IMAGE_REFUSED", raised.exception.code)
        self.assertFalse(any("build" in command for command, _kwargs in calls))

    def test_no_build_refuses_missing_matching_image_and_default_build_failure_is_attributable(self) -> None:
        def empty_lookup(argv, **_kwargs):
            return subprocess.CompletedProcess(argv, 0, "", "")

        manager = self.manager(self.source_fixture(), empty_lookup)
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
            self.manager(APP.parents[2], failed_build).resolve()
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

    def test_packaged_assets_can_build_without_resolving_a_predecessor(self) -> None:
        source = self.source_fixture()
        assets = (RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY, STATUS_MODEL, CANDIDATE_SCHEMA)
        payloads = {path: json.dumps({"asset": Path(path).stem}).encode() for path in assets}
        for path, payload in payloads.items():
            (source / path).write_bytes(payload)
        builds = []

        def executor(argv, **_kwargs):
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "build" in argv:
                builds.append(argv)
                context = Path(argv[-1])
                self.assertEqual(payloads, {path: (context / path).read_bytes() for path in assets})
                Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE_ID, encoding="ascii")
                return subprocess.CompletedProcess(argv, 0, "", "")
            self.assertEqual(["docker", "image", "inspect", IMAGE_ID], argv)
            return subprocess.CompletedProcess(argv, 0, json.dumps([{
                "Id": IMAGE_ID,
                "Created": "2026-10-21T14:15:16Z",
                "Os": "linux",
                "Architecture": "amd64",
                "Config": {"Labels": {
                    "org.caprmedio.runtime.schema": "1",
                    "org.caprmedio.runtime.fingerprint": identity.fingerprint,
                    "org.opencontainers.image.version": identity.version,
                }},
            }]), "")

        manager = self.manager(source, executor)
        manager.build_temp_root = self.fixture_root / "builds"
        manager.build_temp_root.mkdir()
        with patch.object(manager, "_generated_assets", side_effect=AssertionError("asset refresh invoked")):
            identity = manager.identity(use_packaged_assets=True)
            with self.assertRaises(ImageError) as refused:
                manager.resolve(build_if_missing=False, use_packaged_assets=True)
            self.assertEqual("IMAGE_REFUSED", refused.exception.code)
            self.assertEqual([], builds)
            self.assertEqual(IMAGE_ID, manager.resolve(use_packaged_assets=True))
        self.assertEqual(1, len(builds))

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
