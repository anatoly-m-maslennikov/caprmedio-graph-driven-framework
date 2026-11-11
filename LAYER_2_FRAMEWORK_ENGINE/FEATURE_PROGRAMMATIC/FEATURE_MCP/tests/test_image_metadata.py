"""Functional image naming checks through the controlled Docker seam."""
import json
import io
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
sys.path.insert(0, str(DOCKER))

from runtime_images import (  # noqa: E402
    DOCKERFILE,
    DOCKERIGNORE,
    FINGERPRINT_LABEL,
    ImageError,
    ImageManager,
    OCI_VERSION_LABEL,
    RELATION_REGISTRY,
    SCHEMA_LABEL,
    TOOL_REGISTRY,
    WORKBENCH_SCHEMA,
)
import runtime_images  # noqa: E402
import runtime  # noqa: E402

IMAGE, OTHER_IMAGE = "sha256:" + "a" * 64, "sha256:" + "b" * 64
VERSION, CREATED = "0.4.4.9", "2026-10-21T14:15:16.987654321Z"
EXPECTED_TAG = "caprmedio-runtime:0.4.4.9-20261021T141516Z-aaaaaaaaaaaa"


class DockerProbe:
    """A bounded Docker image executor with inspectable public effects."""

    def __init__(self, *, tags=(), listed=(IMAGE,), collision=False, missing_tag=False):
        self.calls: list[tuple[str, ...]] = []
        self.tags = set(tags)
        self.listed = tuple(listed)
        self.collision = collision
        self.missing_tag = missing_tag
        self.labels: dict[str, str] = {}
        self.build_context: Path | None = None
        self.architecture = "amd64"

    @staticmethod
    def _labels(argv: list[str]) -> dict[str, str]:
        labels = {}
        for index, value in enumerate(argv):
            if value == "--label":
                key, label = argv[index + 1].split("=", 1)
                labels[key] = label
        return labels

    def _inspect(self, image: str) -> str:
        inspected = OTHER_IMAGE if self.collision and image == EXPECTED_TAG else IMAGE
        tags = [] if self.missing_tag and image == EXPECTED_TAG else sorted(self.tags)
        return json.dumps([{"Id": inspected, "RepoTags": tags if inspected == IMAGE else [EXPECTED_TAG],
                            "Created": CREATED, "Config": {"Labels": self.labels}, "Os": "linux",
                            "Architecture": self.architecture}])

    def __call__(self, argv, **_kwargs):
        command = tuple(argv)
        self.calls.append(command)
        if argv[:2] == ["docker", "build"]:
            self.labels = self._labels(argv)
            self.build_context = Path(argv[-1])
            self.architecture = argv[argv.index("--platform") + 1].split("/")[1]
            Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE, encoding="ascii")
            return subprocess.CompletedProcess(argv, 0, "", "")
        if argv[:3] == ["docker", "image", "ls"]:
            output = "" if argv[-1] == EXPECTED_TAG else "\n".join(self.listed)
            return subprocess.CompletedProcess(argv, 0, output, "")
        if argv[:3] == ["docker", "image", "inspect"]:
            if argv[-1] == EXPECTED_TAG and not self.tags and not self.collision and not self.missing_tag:
                return subprocess.CompletedProcess(argv, 1, "", "")
            return subprocess.CompletedProcess(argv, 0, self._inspect(argv[-1]), "")
        if argv[:3] == ["docker", "image", "tag"]:
            self.tags.add(argv[-1])
            return subprocess.CompletedProcess(argv, 0, "", "")
        return subprocess.CompletedProcess(argv, 1, "", "")

    def commands(self, *prefix: str) -> list[tuple[str, ...]]:
        return [call for call in self.calls if call[: len(prefix)] == prefix]


class ImageMetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[2] / ".caprmedio_tmp/CA-P-2791/CA-P-2818/image-metadata"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project_temp = self.root / ".caprmedio_tmp"
        self.project_temp.mkdir()
        self.scratch = Path(tempfile.mkdtemp(dir=self.project_temp))
        compiler = patch.object(runtime_images, "_compile_relation_registry", return_value=b'{"schema_version":1}\n')
        compiler.start()
        self.addCleanup(compiler.stop)
        schema = patch.object(runtime_images, "_compile_workbench_schema", return_value=b'{"schema_version":1}\n')
        schema.start()
        self.addCleanup(schema.stop)
        tools = patch.object(runtime_images, "_compile_tool_registry", return_value=b'{"schema_version":1}\n')
        tools.start()
        self.addCleanup(tools.stop)
        lifecycle = patch("runtime_images._compile_lifecycle_assets", return_value=(b'{"schema_version":1}\n', b'{"schema_version":1}\n'))
        lifecycle.start()
        self.addCleanup(lifecycle.stop)
        self._write_fixture(VERSION)

    def _write_fixture(self, version: str) -> None:
        (self.root / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")
        (self.root / "uv.lock").write_text("version = 1\n", encoding="utf-8")
        (self.root / "version.toml").write_text(f'[framework]\nversion = "{version}"\n', encoding="utf-8")
        for relative, content in (
            (DOCKERFILE, "FROM scratch\n"),
            (DOCKERIGNORE, ".git\n"),
            ("LAYER_2_FRAMEWORK_ENGINE/marker.py", "fixture-current-code\n"),
        ):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
        for relative in (RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY, runtime_images.STATUS_MODEL, runtime_images.CANDIDATE_SCHEMA):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b'{"schema_version":1}\n')

    def _manager(self, probe: DockerProbe) -> ImageManager:
        manager = ImageManager(self.root, executor=probe, timeout=5, uid=1000, gid=1000,
                               platform="linux/amd64", build_temp_root=self.scratch,
                               project_root=self.root)
        identity = manager.identity()
        probe.labels.update({SCHEMA_LABEL: "1", FINGERPRINT_LABEL: identity.fingerprint,
                             OCI_VERSION_LABEL: identity.version})
        return manager

    def _assert_no_mutation(self, probe: DockerProbe) -> None:
        for command in (("docker", "build"), ("docker", "image", "tag"), ("docker", "image", "rm"), ("docker", "rmi")):
            self.assertEqual([], probe.commands(*command))

    def test_version_toml_is_in_source_identity(self) -> None:
        probe = DockerProbe(listed=())
        before = self._manager(probe).identity()
        self.assertIn("version.toml", {row.path for row in before.manifest})
        self.assertIn(TOOL_REGISTRY, {row.path for row in before.manifest})
        self._write_fixture("0.4.4.10")
        after = self._manager(probe).identity()
        self.assertNotEqual(before.fingerprint, after.fingerprint)

    def test_build_emits_oci_version_and_created_utc_tag_after_inspection(self) -> None:
        probe = DockerProbe(listed=())
        self.assertEqual(IMAGE, self._manager(probe).resolve())
        build = probe.commands("docker", "build")
        self.assertEqual(1, len(build))
        self.assertEqual(VERSION, probe.labels["org.opencontainers.image.version"])
        self.assertEqual("1", probe.labels[SCHEMA_LABEL])
        self.assertEqual(64, len(probe.labels[FINGERPRINT_LABEL]))
        self.assertIsNotNone(probe.build_context)
        self.assertTrue(probe.build_context.is_relative_to(self.scratch))
        self.assertIn(f'version = "{VERSION}"', (probe.build_context / "version.toml").read_text())
        tag = probe.commands("docker", "image", "tag")
        self.assertEqual([("docker", "image", "tag", IMAGE, EXPECTED_TAG)], tag)
        self.assertGreater(probe.calls.index(tag[0]), probe.calls.index(build[0]))

    def test_validated_reuse_adds_missing_created_tag_without_rebuild(self) -> None:
        probe = DockerProbe(tags=(), listed=(IMAGE,))
        self.assertEqual(IMAGE, self._manager(probe).resolve(build_if_missing=False))
        self.assertEqual([("docker", "image", "tag", IMAGE, EXPECTED_TAG)],
                         probe.commands("docker", "image", "tag"))
        self.assertEqual([], probe.commands("docker", "build"))

    def test_no_build_uses_packaged_assets_without_project_or_compilers(self) -> None:
        probe = DockerProbe(tags=(EXPECTED_TAG,))
        manager = self._manager(probe)
        manager.project_root = self.root / "absent-project"
        with (patch.object(runtime_images, "_compile_relation_registry", side_effect=AssertionError),
              patch.object(runtime_images, "_compile_workbench_schema", side_effect=AssertionError),
              patch.object(runtime_images, "_compile_tool_registry", side_effect=AssertionError)):
            self.assertEqual(IMAGE, manager.resolve(explicit_id=IMAGE, build_if_missing=False))

    def test_no_build_rejects_missing_symlinked_or_changed_packaged_assets(self) -> None:
        for relative in (RELATION_REGISTRY, WORKBENCH_SCHEMA, TOOL_REGISTRY, runtime_images.STATUS_MODEL, runtime_images.CANDIDATE_SCHEMA):
            with self.subTest(relative=relative):
                path = self.root / relative
                original = path.read_bytes()
                path.unlink()
                with self.assertRaises(ImageError) as missing:
                    ImageManager(self.root, project_root=self.root).identity(use_packaged_assets=True)
                self.assertEqual("IMAGE_INPUT_UNAVAILABLE", missing.exception.code)
                path.symlink_to(self.root / "version.toml")
                with self.assertRaises(ImageError) as unsafe:
                    ImageManager(self.root, project_root=self.root).identity(use_packaged_assets=True)
                self.assertEqual("IMAGE_INPUT_UNAVAILABLE", unsafe.exception.code)
                path.unlink()
                path.write_bytes(original)

        probe = DockerProbe(tags=(EXPECTED_TAG,))
        manager = self._manager(probe)
        def tampering_executor(argv, **kwargs):
            result = probe(argv, **kwargs)
            if argv[:3] == ["docker", "image", "inspect"]:
                (self.root / WORKBENCH_SCHEMA).write_bytes(b"tampered")
            return result
        manager.executor = tampering_executor
        with self.assertRaises(ImageError) as changed:
            manager.resolve(explicit_id=IMAGE, build_if_missing=False)
        self.assertEqual("IMAGE_INPUT_UNAVAILABLE", changed.exception.code)

    def test_explicit_sha_reuses_existing_display_tag_without_build_or_alias_move(self) -> None:
        probe = DockerProbe(tags=(EXPECTED_TAG,), listed=())
        self.assertEqual(IMAGE, self._manager(probe).resolve(explicit_id=IMAGE))
        self._assert_no_mutation(probe)

    def test_exact_tag_for_same_sha_is_a_noop(self) -> None:
        probe = DockerProbe(tags=(EXPECTED_TAG,), listed=(IMAGE,))
        self.assertEqual(IMAGE, self._manager(probe).resolve(build_if_missing=False))
        self._assert_no_mutation(probe)

    def test_existing_tag_collision_refuses_without_moving_or_deleting(self) -> None:
        probe = DockerProbe(tags=(), listed=(IMAGE,), collision=True)
        with self.assertRaises(ImageError) as raised:
            self._manager(probe).resolve(build_if_missing=False)
        self.assertEqual("IMAGE_REFUSED", raised.exception.code)
        self._assert_no_mutation(probe)

    def test_successful_tag_inspect_missing_requested_tag_refuses_without_mutation(self) -> None:
        probe = DockerProbe(listed=(IMAGE,), missing_tag=True)
        with self.assertRaises(ImageError) as raised:
            self._manager(probe).resolve(build_if_missing=False)
        self.assertEqual("IMAGE_REFUSED", raised.exception.code)
        self._assert_no_mutation(probe)

    def test_runtime_build_uses_the_same_created_version_sha_tag(self) -> None:
        probe = DockerProbe(listed=())
        docker_directory = (self.root / DOCKERFILE).parent
        with (
            patch.object(runtime, "SOURCE_ROOT", self.root),
            patch.object(runtime, "DIRECTORY", docker_directory),
            patch.object(runtime_images, "_bounded_run", side_effect=probe),
        ):
            runtime_instance = runtime.Runtime(self.root)
            self.assertEqual(IMAGE, runtime_instance.build())
        self.assertEqual(IMAGE, runtime_instance.image)
        self.assertTrue(probe.build_context.is_relative_to(self.project_temp))
        self.assertEqual([("docker", "image", "tag", IMAGE, EXPECTED_TAG)],
                         probe.commands("docker", "image", "tag"))
        self.assertFalse(probe.commands("docker", "image", "rm"))

    def test_runtime_cli_build_prints_immutable_digest(self) -> None:
        output = io.StringIO()
        with patch.object(runtime.Runtime, "build", return_value=IMAGE), patch.object(sys, "argv", ["runtime.py", "build"]), redirect_stdout(output):
            runtime.main()
        self.assertEqual(IMAGE + "\n", output.getvalue())
