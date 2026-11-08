"""Relation-registry image input stays generated, bound, and non-authoritative."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]
DOCKER = APP / "docker"
sys.path.insert(0, str(DOCKER))

import project_mcp_backend  # noqa: E402
import runtime  # noqa: E402
import runtime_images as images  # noqa: E402


IMAGE_ID = "sha256:" + "a" * 64


class RelationRegistryImageInputTests(unittest.TestCase):
    def setUp(self) -> None:
        parent = APP.parents[3] / ".caprmedio_tmp/relation-registry-image-input"
        parent.mkdir(parents=True, exist_ok=True)
        self.temporary = Path(tempfile.mkdtemp(dir=parent))
        self.project = self.temporary / "project"
        (self.project / ".caprmedio_tmp").mkdir(parents=True)
        (self.project / ".caprmedio_caprmedio").mkdir()
        (self.project / ".caprmedio_caprmedio/authority.md").write_text("must not enter image", encoding="utf-8")
        self.source = self.temporary / "source"
        docker = self.source / images.DOCKER_ROOT
        docker.mkdir(parents=True)
        (self.source / "pyproject.toml").write_text("[project]\nname='fixture'\n", encoding="utf-8")
        (self.source / "uv.lock").write_text("version=1\n", encoding="utf-8")
        (self.source / "version.toml").write_text('[framework]\nversion="0.4.4.9"\n', encoding="utf-8")
        (docker / "Dockerfile").write_text("FROM scratch\n", encoding="utf-8")
        (docker / "Dockerfile.dockerignore").write_text(".git\n", encoding="utf-8")
        (docker.parent / "engine.py").write_text("ENGINE = True\n", encoding="utf-8")

    def manager(self, executor=lambda *_args, **_kwargs: None):
        return images.ImageManager(
            self.source,
            executor=executor,
            uid=1000,
            gid=1000,
            platform="linux/amd64",
            project_root=self.project,
        )

    def compiler_source(self, name: str, registry: bytes) -> Path:
        source = self.temporary / name
        compiler = source / images.RELATION_REGISTRY_COMPILER
        compiler.parent.mkdir(parents=True)
        compiler.write_text(
            "import argparse\n"
            "from pathlib import Path\n"
            "parser = argparse.ArgumentParser()\n"
            "parser.add_argument('--project-root')\n"
            "parser.add_argument('--output')\n"
            "args = parser.parse_args()\n"
            f"Path(args.output).write_bytes({registry!r})\n",
            encoding="utf-8",
        )
        return source

    def test_independent_source_roots_run_their_own_registry_compiler(self):
        first = self.compiler_source("source-one", b'{"source":"one"}\n')
        second = self.compiler_source("source-two", b'{"source":"two"}\n')
        self.assertEqual(
            b'{"source":"one"}\n',
            images._compile_relation_registry(first, self.project, timeout=5, max_output=1024),
        )
        self.assertEqual(
            b'{"source":"two"}\n',
            images._compile_relation_registry(second, self.project, timeout=5, max_output=1024),
        )
        self.assertEqual(
            b'{"source":"one"}\n',
            images._compile_relation_registry(first, self.project, timeout=5, max_output=1024),
        )
        self.assertEqual([], list((self.project / ".caprmedio_tmp").iterdir()))

    def test_registry_bytes_change_fingerprint_and_replace_a_handwritten_source_asset(self):
        stale = self.source / images.RELATION_REGISTRY
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.write_bytes(b"stale-handwritten-registry")
        with patch.object(images, "_compile_relation_registry", return_value=b'{"input_digest":"one"}\n'):
            before = self.manager().identity()
        with patch.object(images, "_compile_relation_registry", return_value=b'{"input_digest":"two"}\n'):
            after = self.manager().identity()
        rows = {row.path: row for row in after.manifest}
        self.assertNotEqual(before.fingerprint, after.fingerprint)
        self.assertEqual(
            images.RELATION_REGISTRY,
            next(path for path in rows if path == images.RELATION_REGISTRY),
        )
        self.assertNotEqual("stale-handwritten-registry", after.relation_registry.decode())

    def test_context_has_only_fresh_registry_metadata_not_project_authority(self):
        registry = b'{"input_digest":"current","schema_version":1}\n'
        contexts = []
        manager = self.manager()
        with patch.object(images, "_compile_relation_registry", return_value=registry):
            identity = manager.identity()

            def executor(argv, **_kwargs):
                command = tuple(argv)
                if "ls" in command:
                    return subprocess.CompletedProcess(argv, 0, "", "")
                if "build" in command:
                    context = Path(argv[-1])
                    contexts.append(context)
                    self.assertEqual(registry, (context / images.RELATION_REGISTRY).read_bytes())
                    self.assertFalse(any(".caprmedio_caprmedio" in path.parts for path in context.rglob("*")))
                    Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE_ID, encoding="ascii")
                    return subprocess.CompletedProcess(argv, 0, "", "")
                labels = {
                    images.SCHEMA_LABEL: images.SCHEMA,
                    images.FINGERPRINT_LABEL: identity.fingerprint,
                    "org.opencontainers.image.version": identity.version,
                }
                return subprocess.CompletedProcess(argv, 0, json.dumps([{
                    "Id": IMAGE_ID,
                    "Created": "2026-10-21T14:15:16.987654321Z",
                    "RepoTags": [command[-1]] if command[-1].startswith("caprmedio-runtime:") else [],
                    "Os": "linux",
                    "Architecture": "amd64",
                    "Config": {"Labels": labels},
                }]), "")

            manager.executor = executor
            self.assertEqual(IMAGE_ID, manager.resolve())
        self.assertEqual(1, len(contexts))

    def test_missing_or_failed_generation_refuses_before_docker_or_stale_asset_use(self):
        stale = self.source / images.RELATION_REGISTRY
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.write_text("stale", encoding="utf-8")
        for compiler in (ValueError("invalid declarations"), b""):
            with self.subTest(compiler=type(compiler).__name__):
                calls = []
                with patch.object(images, "_compile_relation_registry", side_effect=compiler):
                    with self.assertRaises(images.ImageError) as raised:
                        self.manager(lambda argv, **_kwargs: calls.append(argv)).resolve()
                self.assertEqual("IMAGE_INPUT_UNAVAILABLE", raised.exception.code)
                self.assertEqual([], calls)

    def test_runtime_and_backend_pass_the_explicit_selected_project_root(self):
        runtime_root = self.temporary / "runtime-project"
        runtime_root.mkdir()
        observed = []

        class RuntimeManager:
            def __init__(self, source_root, **kwargs):
                observed.append((source_root, kwargs["project_root"]))

            def resolve(self):
                return IMAGE_ID

        with patch.object(images, "ImageManager", RuntimeManager):
            self.assertEqual(IMAGE_ID, runtime.Runtime(runtime_root).build())
        self.assertEqual([(runtime.SOURCE_ROOT, runtime_root.resolve())], observed)

        class BackendManager:
            def __init__(self, source_root, **kwargs):
                observed.append((source_root, kwargs["project_root"]))

            def resolve(self, **_kwargs):
                return IMAGE_ID

            def identity(self):
                return type("Identity", (), {"fingerprint": "b" * 64})()

        with patch.object(project_mcp_backend, "ImageManager", BackendManager):
            image_id, fingerprint = project_mcp_backend.ProjectMcpBackend().resolve_image(
                self.source, None, project_root=self.project
            )
        self.assertEqual((IMAGE_ID, "b" * 64), (image_id, fingerprint))
        self.assertEqual((self.source, self.project), observed[-1])


if __name__ == "__main__":
    unittest.main()
