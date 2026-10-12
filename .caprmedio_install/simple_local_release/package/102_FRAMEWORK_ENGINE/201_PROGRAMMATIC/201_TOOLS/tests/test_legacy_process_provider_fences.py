"""Physical writer-fence tests for retained legacy-process coverage.

These tests start no Docker service or Workflow worker.  They use each
production namespace's real start lock, verify a collector owns it, and then
verify a fresh writer can acquire it after ``close``.
"""
from __future__ import annotations

import asyncio
import fcntl
import os
from pathlib import Path
import sys
import tempfile
import time
import unittest
from unittest.mock import patch


TOOLS = Path(__file__).resolve().parents[1]
MCP = TOOLS.parent / "204_MCP"
WORKFLOW = TOOLS.parent / "203_APPS/WORKFLOW_ORCHESTRATOR"
DOCKER = WORKFLOW / "docker"
sys.path[:0] = [str(TOOLS), str(MCP), str(WORKFLOW), str(DOCKER)]

from legacy_process_providers import LegacyProcessAdmission  # noqa: E402
import legacy_process_providers as provider_module  # noqa: E402
from project_selection import resolve_project  # noqa: E402
from project_mcp_launcher import (  # noqa: E402
    Launcher,
    open_legacy_process_fence as open_project_mcp_fence,
)
from hot_reload import Gateway, open_legacy_process_fence as open_gateway_fence  # noqa: E402
import hot_reload as hot_reload_module  # noqa: E402
import release_host_shutdown as release_shutdown  # noqa: E402
import workflow_process_inspection as workflow_inspection  # noqa: E402


class _Fence:
    def revalidate(self) -> None:
        return None


class _Backend:
    """Production launcher seam with no Docker subprocesses."""

    image_id = "sha256:" + "a" * 64
    fingerprint = "b" * 64

    def __init__(self) -> None:
        self.rows: list[dict[str, object]] = []
        self.starts = 0

    def resolve_image(self, _source, _image):
        return self.image_id, self.fingerprint

    def inspect(self, _selection):
        return list(self.rows)

    def start(self, selection, _image_id, _fingerprint, _timeout, port=None):
        self.starts += 1
        self.rows = [{
            "Id": "container-for-fence-test",
            "Image": self.image_id,
            "Config": {"Labels": {
                "org.caprmedio.project": selection.instance_id,
                "org.caprmedio.runtime.fingerprint": self.fingerprint,
                "org.caprmedio.service": "mcp-http",
            }},
            "State": {"Status": "running", "Health": {"Status": "healthy"}},
            "NetworkSettings": {"Ports": {
                "8092/tcp": [{"HostIp": "127.0.0.1", "HostPort": str(port or 8099)}]
            }},
        }]

    def health(self, _url, _timeout):
        return True


class LegacyProcessProviderFenceTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        sandbox = TOOLS.parents[2] / ".caprmedio_tmp/tests/legacy-process-provider-fences"
        sandbox.mkdir(parents=True, exist_ok=True)
        self.temporary = tempfile.TemporaryDirectory(dir=sandbox, ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        control = self.root / ".caprmedio_test"
        control.mkdir()
        (control / "caprmedio_project_settings.toml").write_text(
            "[project]\nname=\"test\"\nkey=\"test\"\nrepository_slug=\"test\"\n"
            "[paths]\ncontrol_root=\".caprmedio_test\"\n"
            "[artifacts.identity]\nproject_prefix=\"TEST\"\n"
            "[artifact_timestamps]\ntimezone=\"UTC\"\n",
            encoding="utf-8",
        )
        (control / "project_structure.toml").write_text("schema_version=1\nscope_units=[]\n", encoding="utf-8")
        self.selection = resolve_project(self.root)
        self.admission = LegacyProcessAdmission(
            project_root=self.root,
            project_instance_id=self.selection.instance_id,
            target_context_sha256="1" * 64,
            prior_target_context_sha256="2" * 64,
            prior_selector_bytes=b"physically-reopened-prior-selector",
            fence=_Fence(),
            selection=self.selection,
        )

    async def test_project_mcp_fence_blocks_real_launcher_then_releases_it(self):
        backend = _Backend()
        launcher = Launcher(backend=backend)
        fence = open_project_mcp_fence(self.admission, time.monotonic() + 1)
        try:
            with patch("project_mcp_launcher.resolve_project", return_value=self.selection):
                blocked = launcher.launch(self.root, source_root=self.root, timeout=0.01)
            self.assertEqual("PROJECT_LOCK_BUSY", blocked["condition"])
            self.assertEqual(0, backend.starts)
        finally:
            fence.close()
        with patch("project_mcp_launcher.resolve_project", return_value=self.selection):
            released = launcher.launch(self.root, source_root=self.root, timeout=1)
        self.assertEqual("READY_STARTED", released["condition"])
        self.assertEqual(1, backend.starts)

    async def test_gateway_singleton_blocks_initialize_then_releases_it(self):
        implementation = self.root / "implementation.py"
        implementation.write_text("# test-only implementation\n", encoding="utf-8")
        gateway = Gateway(self.root, implementation=implementation, selection=self.selection)
        # The production reader is separately tested as fail-closed below.
        # Inject only its OS-reader boundary here so this lock-contention test
        # stays independent of the sandbox's process-table permission.
        with patch.object(hot_reload_module, "_legacy_gateway_pids", return_value=()):
            fence = open_gateway_fence(self.admission, time.monotonic() + 1)
            try:
                self.assertEqual({"outcome": "complete", "records": []}, fence.snapshot(time.monotonic() + 1))
                with self.assertRaisesRegex(RuntimeError, "singleton fence is busy"):
                    await gateway.initialize()
            finally:
                fence.close()

        class Generation:
            def __init__(self, _params, _fingerprint):
                self.ready = asyncio.get_running_loop().create_future()
                self.ready.set_result(None)
                self.tools = []
            async def close(self):
                return None

        with patch("hot_reload.Generation", Generation), patch.object(gateway, "fingerprint", return_value="f" * 64):
            await gateway.initialize()
        self.assertTrue(gateway._initialized)
        await gateway.close()

    async def test_prefence_gateway_candidate_remains_unknown_after_new_lease_acquires(self):
        # A gateway predating the lifetime lease cannot own its new lock.  The
        # bounded OS-process seam reports its actual Project-bound candidate;
        # that lacks the sealed predecessor/shutdown proof and must block zero.
        with patch.object(hot_reload_module, "_legacy_gateway_pids", return_value=(741,)):
            fence = open_gateway_fence(self.admission, time.monotonic() + 1)
            try:
                raw = fence.snapshot(time.monotonic() + 1)
            finally:
                fence.close()
        self.assertEqual({"outcome": "complete", "records": [{"pid": 741}]}, raw)
        row = provider_module._coverage_from_result("mcp_hot_reload", self.admission, raw)
        self.assertEqual("unknown", row["state"])
        self.assertFalse(provider_module.dormant_predecessor_is_absent(
            (row, row, row), self.admission,
        ))

    async def test_supported_gateway_command_forms_do_not_discard_relative_bindings(self):
        root = str(self.root)
        output = (
            "741 python /opt/caprmedio/204_MCP/server.py --project-root .\n"
            f"742 python server.py --project-root {root}\n"
            "743 python server.py --project-root /another/project\n"
            "744 python -B -c import sys,asyncio;sys.path.insert(0,sys.argv[1]);from hot_reload import Gateway;asyncio.run(Gateway(sys.argv[2],sys.argv[3]).serve())\n"
            f"745 python server.py --project-root /another/project --project-root {root}\n"
        ).encode("utf-8")

        # The first form has a supported absolute entrypoint but a relative
        # root, so it remains unknown without a bounded CWD proof.  The second
        # uses the supported relative script spelling and exact absolute root.
        # The inline source has the real Gateway import flattened by ``ps``;
        # the repeated-root form is ambiguous even when argparse's final root
        # would name this Project (so a first-value parser cannot discard it).
        self.assertEqual((741, 742, 744, 745),
                         hot_reload_module._gateway_pids_from_process_output(output, root))

    async def test_workflow_fence_holds_both_start_locks_and_admission_then_releases(self):
        fence = workflow_inspection.open_legacy_process_fence(self.admission, time.monotonic() + 1)
        normal = self.root / ".caprmedio_install/workflow_orchestrator/worker.lock"
        release = self.root / ".caprmedio_install/workflow_orchestrator/release-host/worker.lock"
        try:
            self.assertEqual({"outcome": "complete", "records": []}, fence.snapshot(time.monotonic() + 1))
            for path in (normal, release):
                descriptor = os.open(path, os.O_RDWR | os.O_NOFOLLOW)
                try:
                    with self.assertRaises(BlockingIOError):
                        fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                finally:
                    os.close(descriptor)
            with self.assertRaises(release_shutdown.ShutdownError):
                with release_shutdown.admission_fence(self.root, timeout=0):
                    self.fail("coverage fence must block release admission")
        finally:
            fence.close()
        for path in (normal, release):
            descriptor = os.open(path, os.O_RDWR | os.O_NOFOLLOW)
            try:
                fcntl.flock(descriptor, fcntl.LOCK_EX | fcntl.LOCK_NB)
                fcntl.flock(descriptor, fcntl.LOCK_UN)
            finally:
                os.close(descriptor)
        with release_shutdown.admission_fence(self.root, timeout=0.1):
            pass


if __name__ == "__main__":
    unittest.main()
