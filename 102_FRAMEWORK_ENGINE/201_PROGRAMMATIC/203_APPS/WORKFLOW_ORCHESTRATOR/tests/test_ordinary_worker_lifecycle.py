"""Current ordinary worker ready publication and shutdown, without a real worker."""

from pathlib import Path
import sys
import tempfile
import types
import unittest
from unittest.mock import MagicMock, patch

APP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(APP))
import backend  # noqa: E402


class OrdinaryWorkerLifecycleTests(unittest.TestCase):
    def setUp(self):
        parent = APP.parents[3] / ".caprmedio_tmp/tests/ordinary-worker-lifecycle"
        parent.mkdir(parents=True, exist_ok=True)
        directory = tempfile.TemporaryDirectory(dir=parent)
        self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)

    def test_ordinary_ready_has_no_release_identity_and_scheduler_is_destroyed(self):
        engine, dbos, stop = MagicMock(), MagicMock(), MagicMock()
        module = types.ModuleType("dbos")
        module.DBOS = dbos
        ready = self.root / "worker.ready"
        scheduler = {
            "application": "ordinary-app",
            "queue": "base-revise",
            "app_version": "ordinary-v1",
        }
        with (
            patch.dict(sys.modules, {"dbos": module}),
            patch.object(backend, "Coordinator", return_value=engine),
            patch.object(
                backend, "database", return_value=(self.root / "db.sqlite", "sqlite:///fixture")
            ),
            patch.object(backend, "_scheduler_identity", return_value=scheduler),
            patch.object(backend, "implementation_mock_runtime", return_value=False),
            patch.object(backend, "docker_runtime", return_value=False),
            patch.object(backend, "CodexAgent"),
            patch.object(backend, "runtime_fingerprint", return_value="f" * 64),
            patch.object(backend, "register_execution"),
            patch.object(backend, "SelectedNativeProviders"),
            patch.object(backend.threading, "Event", return_value=stop),
            patch.object(backend.signal, "getsignal"),
            patch.object(backend.signal, "signal"),
            patch("os.getpid", return_value=4321),
        ):
            backend.worker(self.root, ready_file=ready)
        engine.save.assert_called_once_with(
            ready,
            {
                "state": "ready",
                "pid": 4321,
                "application_version": "ordinary-v1",
                "runtime_fingerprint": "f" * 64,
            },
        )
        self.assertNotIn("start_token", engine.save.call_args.args[1])
        stop.wait.assert_called_once_with()
        dbos.destroy.assert_called_once_with()


if __name__ == "__main__":
    unittest.main()
