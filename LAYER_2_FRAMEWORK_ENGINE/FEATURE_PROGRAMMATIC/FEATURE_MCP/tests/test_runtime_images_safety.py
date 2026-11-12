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
from types import SimpleNamespace
from unittest.mock import MagicMock, patch


APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP / "docker"))
import runtime_images as images  # noqa: E402
import image_docker_client as docker_client  # noqa: E402
from image_relation_registry import compile_lifecycle_assets  # noqa: E402
from project_mcp_backend import ProjectMcpBackend  # noqa: E402


IMAGE_ID = "sha256:" + "a" * 64
PRIVATE_MARKER = "synthetic-private-diagnostic"
PROXY_ROUTING = {
    "HTTP_PROXY": "http://proxy.invalid:3128", "HTTPS_PROXY": "http://proxy.invalid:3128",
    "ALL_PROXY": "socks5://proxy.invalid:1080", "NO_PROXY": "localhost,127.0.0.1",
    "http_proxy": "http://proxy.invalid:3128", "https_proxy": "http://proxy.invalid:3128",
    "all_proxy": "socks5://proxy.invalid:1080", "no_proxy": "localhost,127.0.0.1",
}


def _tagging_executor(executor, calls):
    tagged, sources, inspections = set(), {}, {}

    def execute(argv, **kwargs):
        command = tuple(argv)
        if command[:3] == ("docker", "image", "tag"):
            calls.append(command)
            tagged.add(command[-1])
            sources[command[-1]] = command[-2]
            return subprocess.CompletedProcess(argv, 0, "", "")
        if command[:3] == ("docker", "image", "inspect") and command[-1].startswith("caprmedio-runtime:"):
            if command[-1] not in tagged:
                return subprocess.CompletedProcess(argv, 1, "", "")
            payload = json.loads(inspections[sources[command[-1]]])
            payload[0]["RepoTags"] = [command[-1]]
            return subprocess.CompletedProcess(argv, 0, json.dumps(payload), "")
        if command[:3] == ("docker", "image", "ls") and command[-1].startswith("caprmedio-runtime:"):
            return subprocess.CompletedProcess(argv, 0, "", "")
        result = executor(argv, **kwargs)
        if command[:3] == ("docker", "image", "inspect") and result.returncode == 0:
            inspections[command[-1]] = result.stdout
        return result

    return execute


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
        manager = images.ImageManager(APP.parents[2], platform="linux/amd64", project_root=APP.parents[2])
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
        client.update(PROXY_ROUTING)
        caller = dict(client, CAPRMEDIO_MCP_HTTP_SECRET_TOKEN=PRIVATE_MARKER,
                      AWS_SECRET_ACCESS_KEY=PRIVATE_MARKER, GITHUB_TOKEN=PRIVATE_MARKER,
                      LANG="en_US.UTF-8")
        manager = images.ImageManager(APP.parents[2], platform="linux/amd64", project_root=APP.parents[2])
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
                        patch.object(docker_client.selectors, "DefaultSelector") as selector:
                    selector.return_value.get_map.return_value = {}
                    self.assertEqual("", manager._run(command))
                child_environment = start.call_args.kwargs["env"]
                self.assertEqual(client, child_environment)
                self.assertNotIn("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", child_environment)
                self.assertNotIn(PRIVATE_MARKER, child_environment.values())
                for proxy in PROXY_ROUTING.values():
                    self.assertNotIn(proxy, start.call_args.args[0])

    def test_backend_environments_preserve_present_proxy_routing_without_ambient_credentials(self):
        selection = SimpleNamespace(root=APP.parents[2], control_relative=Path(".caprmedio_fixture"),
                                    instance_id="c" * 64)
        caller = dict(PROXY_ROUTING, PATH="/synthetic-bin",
                      CAPRMEDIO_MCP_HTTP_SECRET_TOKEN=PRIVATE_MARKER,
                      AWS_SECRET_ACCESS_KEY=PRIVATE_MARKER, GITHUB_TOKEN=PRIVATE_MARKER)
        with patch.dict(os.environ, caller, clear=True):
            client = ProjectMcpBackend._docker_client_environment()
            service = ProjectMcpBackend._environment(selection, IMAGE_ID, "b" * 64, 56317)
        self.assertEqual(dict(PROXY_ROUTING, PATH="/synthetic-bin"), client)
        for name, value in PROXY_ROUTING.items():
            self.assertEqual(value, service[name])
        self.assertNotIn("CAPRMEDIO_MCP_HTTP_SECRET_TOKEN", service)
        self.assertNotIn(PRIVATE_MARKER, client.values())
        self.assertNotIn(PRIVATE_MARKER, service.values())
        self.assertNotIn("AWS_SECRET_ACCESS_KEY", service)
        self.assertNotIn("GITHUB_TOKEN", service)
        with patch.dict(os.environ, {"PATH": "/synthetic-bin"}, clear=True):
            absent = ProjectMcpBackend._docker_client_environment()
        self.assertEqual({"PATH": "/synthetic-bin"}, absent)

    def test_mock_oversize_and_timeout_report_only_safe_conditions(self):
        def noisy(argv, **_kwargs):
            return subprocess.CompletedProcess(argv, 0, PRIVATE_MARKER * 300000, PRIVATE_MARKER)

        manager = images.ImageManager(APP.parents[2], executor=noisy, platform="linux/amd64", project_root=APP.parents[2])
        with self.assertRaises(images.ImageError) as raised:
            manager._run(("docker", "image", "ls"))
        self.assertEqual("IMAGE_REFUSED", raised.exception.code)
        self.assertNotIn(PRIVATE_MARKER, str(raised.exception))

        def timeout(argv, **_kwargs):
            raise subprocess.TimeoutExpired(argv, 1, PRIVATE_MARKER, PRIVATE_MARKER)

        manager = images.ImageManager(APP.parents[2], executor=timeout, platform="linux/amd64", project_root=APP.parents[2])
        with self.assertRaises(images.ImageError) as raised:
            manager._run(("docker", "build"), code="BUILD_FAILED")
        self.assertEqual("BUILD_FAILED", raised.exception.code)
        self.assertNotIn(PRIVATE_MARKER, str(raised.exception))
        self.assertTrue(raised.exception.__suppress_context__)
        self.assertIsNone(raised.exception.__cause__)


class ImageCredentialContextTests(unittest.TestCase):
    def test_known_credential_stores_are_neither_read_hashed_nor_copied(self):
        compiler = patch.object(images, "_compile_relation_registry", return_value=b'{"schema_version":1}\n')
        compiler.start()
        self.addCleanup(compiler.stop)
        schema = patch.object(images, "_compile_workbench_schema", return_value=b'{"schema_version":1}\n')
        schema.start()
        self.addCleanup(schema.stop)
        tools = patch.object(images, "_compile_tool_registry", return_value=b'{"schema_version":1}\n')
        tools.start()
        self.addCleanup(tools.stop)
        lifecycle = patch("runtime_images._compile_lifecycle_assets", return_value=(b'{"schema_version":1}\n', b'{"schema_version":1}\n'))
        lifecycle.start()
        self.addCleanup(lifecycle.stop)
        parent = APP.parents[2] / ".caprmedio_tmp/launcher-epic-1829/images"
        parent.mkdir(parents=True, exist_ok=True)
        source = Path(tempfile.mkdtemp(prefix="image-credentials-", dir=parent))
        docker = source / images.DOCKER_ROOT
        docker.mkdir(parents=True)
        (source / "pyproject.toml").write_text("[project]\nname='fixture'\n")
        (source / "uv.lock").write_text("version=1\n")
        (source / "version.toml").write_text('[framework]\nversion = "0.4.4.9"\n')
        (docker / "Dockerfile").write_text("FROM scratch\n")
        (docker / "Dockerfile.dockerignore").write_text(".git\n")
        (docker.parent / "engine.py").write_text("ENGINE=True\n")
        manager = images.ImageManager(source, executor=lambda *_a, **_k: None,
                                      uid=1000, gid=1000, platform="linux/amd64",
                                      project_root=APP.parents[2])
        before = manager.identity()
        with patch.dict(os.environ, PROXY_ROUTING):
            self.assertEqual(before, manager.identity(), "proxy routing is not an image input")
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
            inspection = [{"Id": IMAGE_ID, "Created": "2026-10-21T14:15:16.987654321Z",
                           "RepoTags": [], "Os": "linux", "Architecture": "amd64",
                           "Config": {"Labels": {images.SCHEMA_LABEL: images.SCHEMA,
                                                 images.FINGERPRINT_LABEL: before.fingerprint,
                                                 "org.opencontainers.image.version": "0.4.4.9"}}}]
            return subprocess.CompletedProcess(argv, 0, json.dumps(inspection), PRIVATE_MARKER)

        manager.executor = _tagging_executor(executor, calls)
        with patch.object(Path, "read_bytes", guarded_read):
            self.assertEqual(before, manager.identity())
            self.assertEqual(IMAGE_ID, manager.resolve())
        self.assertEqual(1, sum("build" in call for call in calls))
        self.assertEqual(1, sum("tag" in call for call in calls))
        self.assertFalse(any("run" in call for call in calls))


class LifecycleImageAssetsTests(unittest.TestCase):
    def test_predecessor_pins_selected_ready_receipt(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            project_id = "c" * 64
            state = root / ".caprmedio_runtime/runtime/project_mcp" / project_id
            state.mkdir(parents=True)
            control = root / ".caprmedio_project"
            selection = SimpleNamespace(root=root, control_root=control, instance_id=project_id, launcher_state=state)
            receipt = {"project_root": str(root), "control_root": str(control), "project_id": project_id,
                       "image_id": IMAGE_ID, "readiness": True}
            path = state / "ready.json"
            path.write_text(json.dumps(receipt))
            with patch.dict(sys.modules, {"project_selection": SimpleNamespace(resolve_project=lambda _: selection)}):
                manager = images.ImageManager(root, project_root=root)
                self.assertEqual(IMAGE_ID, manager._build_predecessor())
                path.write_text("{}")
                self.assertEqual(IMAGE_ID, manager._build_predecessor())
                with self.assertRaises(images.ImageError):
                    images.ImageManager(root, project_root=root)._build_predecessor()

    def test_unrelated_or_unsafe_receipt_is_not_accepted(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary).resolve()
            project_id = "d" * 64
            state = root / ".caprmedio_runtime/runtime/project_mcp" / project_id
            state.mkdir(parents=True)
            control = root / ".caprmedio_project"
            selection = SimpleNamespace(root=root, control_root=control, instance_id=project_id, launcher_state=state)
            path = state / "ready.json"
            receipt = {"project_root": str(root), "control_root": str(control), "project_id": "e" * 64,
                       "image_id": IMAGE_ID, "readiness": True}
            with patch.dict(sys.modules, {"project_selection": SimpleNamespace(resolve_project=lambda _: selection)}):
                path.write_text(json.dumps(receipt))
                with self.assertRaises(images.ImageError):
                    images.ImageManager(root, project_root=root)._build_predecessor()
                path.unlink()
                path.symlink_to(root / "missing")
                with self.assertRaises(images.ImageError):
                    images.ImageManager(root, project_root=root)._build_predecessor()

    def test_first_build_without_state_does_not_resolve_project(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            resolver = MagicMock(side_effect=AssertionError("unexpected Project read"))
            with patch.dict(sys.modules, {"project_selection": SimpleNamespace(resolve_project=resolver)}):
                manager = images.ImageManager(root, project_root=root)
                self.assertIsNone(manager._build_predecessor())
                self.assertIsNone(manager._build_predecessor())
                resolver.assert_not_called()

    def test_image_manager_passes_explicit_predecessor(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            manager = images.ImageManager(root, project_root=root, previous_image=IMAGE_ID)
            with patch.object(images, "_compile_relation_registry", return_value=b"{}"), \
                 patch.object(images, "_compile_workbench_schema", return_value=b"{}"), \
                 patch.object(images, "_compile_tool_registry", return_value=b"{}"), \
                 patch.object(images, "_compile_lifecycle_assets", return_value=(b"{}", b"{}")) as compile_assets:
                manager._generated_assets(root)
            self.assertEqual(IMAGE_ID, compile_assets.call_args.kwargs["previous_image"])
            with self.assertRaises(images.ImageError):
                images.ImageManager(root, project_root=root, previous_image="mutable:tag")

    def test_previous_image_runs_staged_read_only_selector_for_candidate_only(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".caprmedio_tmp").mkdir()
            model = root / "METHODOLOGY/sources"
            model.mkdir(parents=True)
            (model / "source.md").write_text("source", encoding="utf-8")
            lifecycle = root / images.LIFECYCLE_ROOT
            lifecycle.mkdir(parents=True)
            for name in ("placement_sources", "status_model", "candidate_schema"):
                (lifecycle / f"{name}.py").write_text("# fixture", encoding="utf-8")
            calls, compilers = [], []

            def docker(argv, **kwargs):
                calls.append(argv)
                self.assertEqual(1024, kwargs["max_output"])
                if argv[1:3] == ["image", "inspect"]:
                    payload = [{"Id": IMAGE_ID, "Os": "linux", "Architecture": "arm64",
                                "Config": {"Labels": {images.SCHEMA_LABEL: images.SCHEMA}}}]
                else:
                    self.assertTrue({"--rm", "--pull=never", "--network=none", "--read-only"} <= set(argv))
                    self.assertEqual(IMAGE_ID, argv[-3])
                    mounts = [argv[i + 1] for i, value in enumerate(argv) if value == "--mount"]
                    self.assertEqual(2, len(mounts))
                    self.assertTrue(all(value.endswith(",readonly") for value in mounts))
                    staged = Path(mounts[0].split(",")[1].removeprefix("src="))
                    self.assertNotEqual(model, staged)
                    self.assertEqual("source", (staged / "source.md").read_text())
                    payload = {"placement": []}
                return subprocess.CompletedProcess(argv, 0, json.dumps(payload), "")

            def compiler(argv, **_kwargs):
                compilers.append(argv)
                Path(argv[argv.index("--output") + 1]).write_text("{}", encoding="utf-8")
                if argv[2].endswith("candidate_schema.py"):
                    selected = Path(argv[argv.index("--placement-selection") + 1])
                    self.assertEqual({"placement": []}, json.loads(selected.read_text()))
                else:
                    self.assertNotIn("--placement-selection", argv)
                return subprocess.CompletedProcess(argv, 0)

            with patch("image_relation_registry.bounded_run", side_effect=docker), \
                 patch("image_relation_registry.verify_status_workflow_asset"), \
                 patch("image_relation_registry.subprocess.run", side_effect=compiler):
                self.assertEqual((b"{}", b"{}"), compile_lifecycle_assets(
                    root, root, timeout=5, max_output=1024, previous_image=IMAGE_ID))
            self.assertEqual(2, len(calls))
            self.assertEqual(2, len(compilers))

    def test_missing_previous_image_fails_without_native_fallback(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".caprmedio_tmp").mkdir()
            (root / "METHODOLOGY/sources").mkdir(parents=True)
            failed = subprocess.CompletedProcess([], 1, "", "")
            with patch("image_relation_registry.bounded_run", return_value=failed), \
                 patch("image_relation_registry.verify_status_workflow_asset"), \
                 patch("image_relation_registry.subprocess.run") as compiler:
                with self.assertRaisesRegex(ValueError, "previous image is unavailable"):
                    compile_lifecycle_assets(root, root, timeout=5, max_output=1024, previous_image=IMAGE_ID)
                compiler.assert_not_called()

    def test_image_compiles_the_packaged_sources_after_workflow_verification(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / ".caprmedio_tmp").mkdir()
            sources = root / "METHODOLOGY/sources"
            sources.mkdir(parents=True)
            pin = sources / "workflow.md"
            pin.write_text("reviewed", encoding="utf-8")
            lifecycle = root / images.LIFECYCLE_ROOT
            (lifecycle / "assets").mkdir(parents=True)
            (lifecycle / "assets/change_current_status.py").touch()
            sidecar = lifecycle / "assets/change_current_status_sources.json"
            sidecar.write_text("{}", encoding="utf-8")
            (lifecycle / "status_workflow_definition.py").write_text(
                "from pathlib import Path\nimport sys\n"
                "assert (Path(sys.argv[2]) / 'workflow.md').read_text() == 'reviewed'\n",
                encoding="utf-8",
            )
            for name in ("status_model", "candidate_schema"):
                (lifecycle / f"{name}.py").write_text(
                    "from pathlib import Path\nimport sys\n"
                    "Path(sys.argv[4]).write_bytes((Path(sys.argv[2]) / 'workflow.md').read_bytes())\n",
                    encoding="utf-8",
                )
            self.assertEqual(
                (b"reviewed", b"reviewed"),
                compile_lifecycle_assets(root, root, timeout=5, max_output=1024),
            )
            pin.write_text("changed", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "workflow verification failed"):
                compile_lifecycle_assets(root, root, timeout=5, max_output=1024)
            sidecar.unlink()
            with self.assertRaisesRegex(ValueError, "workflow files are unavailable"):
                compile_lifecycle_assets(root, root, timeout=5, max_output=1024)
            sidecar.symlink_to(pin)
            with self.assertRaisesRegex(ValueError, "workflow files are unavailable"):
                compile_lifecycle_assets(root, root, timeout=5, max_output=1024)
            sidecar.unlink()
            (lifecycle / "status_cascade.py").write_text(
                "from ATOM_LIFECYCLE.assets.change_current_status import change_current_status\n",
                encoding="utf-8",
            )
            (lifecycle / "assets/change_current_status.py").unlink()
            (lifecycle / "status_workflow_definition.py").unlink()
            with self.assertRaisesRegex(ValueError, "workflow files are missing from the routed pilot"):
                compile_lifecycle_assets(root, root, timeout=5, max_output=1024)


if __name__ == "__main__":
    unittest.main()
