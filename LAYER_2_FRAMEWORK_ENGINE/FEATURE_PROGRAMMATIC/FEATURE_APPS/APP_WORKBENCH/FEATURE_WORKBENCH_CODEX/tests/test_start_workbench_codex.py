"""The release-owned starter creates a bounded host bridge process."""

# Implemented by:
# CA-R-2791@1
# CA-M-475@1
# CA-D-680@1
from __future__ import annotations

from contextlib import redirect_stdout
import importlib.util
import io
from pathlib import Path
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch


STARTER = Path(__file__).resolve().parents[1] / "start_workbench_codex.py"
SPEC = importlib.util.spec_from_file_location("start_workbench_codex_test", STARTER)
assert SPEC is not None and SPEC.loader is not None
starter = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(starter)


class StartWorkbenchCodexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory(ignore_cleanup_errors=True)
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()

    def test_starts_installed_bridge_and_returns_ready_url(self) -> None:
        output = io.StringIO()
        process = SimpleNamespace(pid=7001)
        with (
            patch.object(starter.subprocess, "Popen", return_value=process) as popen,
            patch.object(starter, "_wait_until_ready", return_value="http://127.0.0.1:43210") as ready,
            redirect_stdout(output),
        ):
            self.assertEqual(0, starter.main([
                "--project-root", str(self.root), "--mcp-url", "http://127.0.0.1:56317/caprmedio/mcp",
            ]))

        argv = popen.call_args.args[0]
        self.assertEqual(sys.executable, argv[0])
        self.assertTrue(argv[1].endswith("bridge_server.py"))
        self.assertEqual(str(self.root), argv[argv.index("--project-root") + 1])
        self.assertEqual("http://127.0.0.1:56317/caprmedio/mcp", argv[argv.index("--mcp-url") + 1])
        self.assertTrue(popen.call_args.kwargs["start_new_session"])
        ready.assert_called_once_with(starter._state_path(self.root), self.root, process.pid)
        self.assertEqual("http://127.0.0.1:43210\n", output.getvalue())

    def test_only_matching_project_bridge_is_an_owned_process(self) -> None:
        server = STARTER.with_name("bridge_server.py").resolve()
        command = f"{sys.executable} {server} --project-root {self.root} --mcp-url http://127.0.0.1:56317/caprmedio/mcp"
        with patch.object(starter.subprocess, "run", return_value=subprocess.CompletedProcess((), 0, command, "")):
            self.assertEqual(7001, starter._owned_bridge(
                {"pid": 7001, "project_root": str(self.root)}, self.root, server,
            ))
        self.assertIsNone(starter._owned_bridge(
            {"pid": 7001, "project_root": "/another-project"}, self.root, server,
        ))


if __name__ == "__main__":
    unittest.main()
