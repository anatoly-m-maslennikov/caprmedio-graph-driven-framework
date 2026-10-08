"""Bounded process output and known credential-store image negatives."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP / "docker"))
import runtime_images as images  # noqa: E402


IMAGE_ID = "sha256:" + "a" * 64
PRIVATE_MARKER = "synthetic-private-diagnostic"


class ImageOutputSafetyTests(unittest.TestCase):
    def python(self, source):
        return [sys.executable, "-B", "-c", source]

    def test_real_reader_rejects_oversize_stdout_before_collecting_it(self):
        with self.assertRaises(ValueError) as raised:
            images._bounded_run(self.python("import sys; sys.stdout.write('x' * 1000000)"),
                                cwd=APP, timeout=2, max_output=32)
        self.assertNotIn(PRIVATE_MARKER, str(raised.exception))

    def test_real_reader_discards_noisy_stderr(self):
        source = ("import sys; sys.stderr.write('" + PRIVATE_MARKER + "' * 100000); "
                  "sys.stdout.write('safe')")
        result = images._bounded_run(self.python(source), cwd=APP, timeout=2, max_output=32)
        self.assertEqual(0, result.returncode)
        self.assertEqual("safe", result.stdout)
        self.assertEqual("", result.stderr)

    def test_real_build_reader_discards_both_streams(self):
        source = "import sys; sys.stdout.write('x' * 1000000); sys.stderr.write('y' * 1000000)"
        result = images._bounded_run(self.python(source), cwd=APP, timeout=2,
                                     capture_stdout=False, max_output=32)
        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertEqual("", result.stderr)

    def test_real_reader_timeout_is_finite_and_keeps_no_diagnostics(self):
        source = ("import sys,time; sys.stderr.write('" + PRIVATE_MARKER + "'); "
                  "sys.stderr.flush(); time.sleep(5)")
        before = time.monotonic()
        with self.assertRaises(subprocess.TimeoutExpired) as raised:
            images._bounded_run(self.python(source), cwd=APP, timeout=0.05, max_output=32)
        self.assertLess(time.monotonic() - before, 2)
        self.assertIsNone(raised.exception.output)
        self.assertIsNone(raised.exception.stderr)

    def test_default_executor_routes_to_bounded_reader(self):
        manager = images.ImageManager(APP.parents[3], platform="linux/amd64")
        with patch.object(images, "_bounded_run", return_value=subprocess.CompletedProcess([], 0, "[]", "")) as reader:
            self.assertEqual("[]", manager._run(("docker", "image", "ls")))
        self.assertTrue(reader.call_args.kwargs["capture_stdout"])
        self.assertEqual(4 * 1024 * 1024, reader.call_args.kwargs["max_output"])
        with patch.object(images, "_bounded_run", return_value=subprocess.CompletedProcess([], 0, "", "")) as reader:
            self.assertEqual("", manager._run(("docker", "build"), code="BUILD_FAILED"))
        self.assertFalse(reader.call_args.kwargs["capture_stdout"])

    def test_default_image_commands_receive_only_the_docker_client_environment(self):
        client = {
            "HOME": "/synthetic-home", "PATH": "/synthetic-bin",
            "DOCKER_HOST": "unix:///synthetic/docker.sock", "DOCKER_CONTEXT": "fixture",
            "DOCKER_CONFIG": "/synthetic-docker-config", "XDG_RUNTIME_DIR": "/synthetic-runtime",
            "TMPDIR": "/synthetic-tmp",
        }
        caller = dict(client, CAPRMEDIO_MCP_HTTP_SECRET_TOKEN=PRIVATE_MARKER,
                      AWS_SECRET_ACCESS_KEY=PRIVATE_MARKER, GITHUB_TOKEN=PRIVATE_MARKER,
                      HTTP_PROXY=PRIVATE_MARKER, LANG="en_US.UTF-8")
        manager = images.ImageManager(APP.parents[3], platform="linux/amd64")
        commands = (("docker", "image", "ls"), ("docker", "image", "inspect", IMAGE_ID),
                    ("docker", "build"))
        for command in commands:
            with self.subTest(command=command):
                process = MagicMock()
                process.wait.return_value = 0
                process.poll.return_value = 0
                process.stdout = None if command[1] == "build" else MagicMock()
                with patch.dict(os.environ, caller, clear=True), \
                        patch.object(images.subprocess, "Popen", return_value=process) as start, \
                        patch.object(images.selectors, "DefaultSelector") as selector:
                    selector.return_value.get_map.return_value = {}
                    self.assertEqual("", manager._run(command))
                child_environment = start.call_args.kwargs["env"]
                self.assertEqual(client, child_environment)
                self.assertNotIn("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", child_environment)
                self.assertNotIn(PRIVATE_MARKER, child_environment.values())

    def test_mock_oversize_and_timeout_report_only_safe_conditions(self):
        def noisy(argv, **_kwargs):
            return subprocess.CompletedProcess(argv, 0, PRIVATE_MARKER * 300000, PRIVATE_MARKER)

        manager = images.ImageManager(APP.parents[3], executor=noisy, platform="linux/amd64")
        with self.assertRaises(images.ImageError) as raised:
            manager._run(("docker", "image", "ls"))
        self.assertEqual("IMAGE_REFUSED", raised.exception.code)
        self.assertNotIn(PRIVATE_MARKER, str(raised.exception))

        def timeout(argv, **_kwargs):
            raise subprocess.TimeoutExpired(argv, 1, PRIVATE_MARKER, PRIVATE_MARKER)

        manager = images.ImageManager(APP.parents[3], executor=timeout, platform="linux/amd64")
        with self.assertRaises(images.ImageError) as raised:
            manager._run(("docker", "build"), code="BUILD_FAILED")
        self.assertEqual("BUILD_FAILED", raised.exception.code)
        self.assertNotIn(PRIVATE_MARKER, str(raised.exception))
        self.assertTrue(raised.exception.__suppress_context__)
        self.assertIsNone(raised.exception.__cause__)


class ImageCredentialContextTests(unittest.TestCase):
    def test_known_credential_stores_are_neither_read_hashed_nor_copied(self):
        parent = APP.parents[3] / ".caprmedio_tmp/launcher-epic-1829/images"
        parent.mkdir(parents=True, exist_ok=True)
        source = Path(tempfile.mkdtemp(prefix="image-credentials-", dir=parent))
        docker = source / images.DOCKER_ROOT
        docker.mkdir(parents=True)
        (source / "pyproject.toml").write_text("[project]\nname='fixture'\n")
        (source / "uv.lock").write_text("version=1\n")
        (docker / "Dockerfile").write_text("FROM scratch\n")
        (docker / "Dockerfile.dockerignore").write_text(".git\n")
        (docker.parent / "engine.py").write_text("ENGINE=True\n")
        manager = images.ImageManager(source, executor=lambda *_a, **_k: None,
                                      uid=1000, gid=1000, platform="linux/amd64")
        before = manager.identity()
        engine = source / images.ENGINE_ROOT
        protected = set()
        for name in ("auth.json", "credentials.json", "token.txt", "token.json", "secrets.json", "secrets.txt"):
            path = engine / name
            path.write_text(PRIVATE_MARKER)
            protected.add(path)
        for name in ("vault", ".vault", "secrets", ".secrets", "credentials", ".credentials"):
            directory = engine / name
            directory.mkdir()
            path = directory / "unclassified-store.txt"
            path.write_text(PRIVATE_MARKER)
            protected.add(path)
        generated = engine / ".caprmedio_runtime"
        generated.mkdir()
        path = generated / "generated-output.json"
        path.write_text(PRIVATE_MARKER)
        protected.add(path)

        read_bytes = Path.read_bytes

        def guarded_read(path):
            self.assertNotIn(path, protected, "excluded store bytes must not be opened")
            return read_bytes(path)

        calls = []

        def executor(argv, **_kwargs):
            calls.append(tuple(argv))
            if "ls" in argv:
                return subprocess.CompletedProcess(argv, 0, "", "")
            if "build" in argv:
                context = Path(argv[-1])
                actual = {path.relative_to(context).as_posix() for path in context.rglob("*") if path.is_file()}
                self.assertEqual({row.path for row in before.manifest}, actual)
                for row in before.manifest:
                    staged = context / row.path
                    self.assertEqual(row.mode, staged.stat().st_mode & 0o777)
                Path(argv[argv.index("--iidfile") + 1]).write_text(IMAGE_ID + "\n")
                return subprocess.CompletedProcess(argv, 0, PRIVATE_MARKER, PRIVATE_MARKER)
            inspection = [{"Id": IMAGE_ID, "Os": "linux", "Architecture": "amd64",
                           "Config": {"Labels": {images.SCHEMA_LABEL: images.SCHEMA,
                                                 images.FINGERPRINT_LABEL: before.fingerprint}}}]
            return subprocess.CompletedProcess(argv, 0, json.dumps(inspection), PRIVATE_MARKER)

        manager.executor = executor
        with patch.object(Path, "read_bytes", guarded_read):
            self.assertEqual(before, manager.identity())
            self.assertEqual(IMAGE_ID, manager.resolve())
        self.assertEqual(1, sum("build" in call for call in calls))
        self.assertFalse(any("tag" in call or "run" in call for call in calls))


if __name__ == "__main__":
    unittest.main()
