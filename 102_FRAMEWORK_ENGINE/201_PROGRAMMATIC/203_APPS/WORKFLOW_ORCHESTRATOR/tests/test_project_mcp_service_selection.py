"""Service-scoped Docker roster selection for the Project MCP backend."""

import json
from pathlib import Path
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch


APP = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(APP / "docker"))
from project_mcp_backend import BackendError, ProjectMcpBackend  # noqa: E402


_WORKER_ID = "1" * 64
_MCP_ID = "2" * 64
_SECOND_MCP_ID = "3" * 64


class ProjectMcpServiceSelectionTests(unittest.TestCase):
    def _selection(self, root: Path):
        return SimpleNamespace(
            root=root,
            control_relative=Path("control"),
            instance_id="a" * 64,
        )

    def _row(self, selection, identifier: str) -> dict[str, object]:
        return {
            "Id": identifier,
            "Image": "sha256:" + "b" * 64,
            "Config": {
                "Labels": {
                    "org.caprmedio.project": selection.instance_id,
                    "org.caprmedio.service": "mcp-http",
                    "org.caprmedio.control_root": "control",
                    "org.caprmedio.host_project_root": str(selection.root),
                }
            },
            "State": {"Status": "running", "Health": {"Status": "healthy"}},
            "NetworkSettings": {"Ports": {}},
            "Mounts": [
                {
                    "Type": "bind",
                    "Source": str(selection.root),
                    "Destination": "/project",
                }
            ],
        }

    def _docker_roster(self, selection, mcp_identifiers: list[str], *, foreign_project=False):
        def run(argv, *, timeout, env):
            if argv[:3] == ["docker", "ps", "--all"]:
                service_filter = "label=org.caprmedio.service=mcp-http"
                identifiers = (
                    mcp_identifiers if service_filter in argv else [_WORKER_ID, *mcp_identifiers]
                )
                return "\n".join(identifiers)
            if argv[:3] == ["docker", "container", "inspect"]:
                if argv[-1] == _WORKER_ID:
                    self.fail("worker must not be inspected as the MCP service")
                row = self._row(selection, argv[-1])
                if foreign_project:
                    row["Config"]["Labels"]["org.caprmedio.project"] = "f" * 64
                return json.dumps(row)
            self.fail(f"unexpected Docker command: {argv!r}")

        return run

    def test_inspect_selects_mcp_service_from_shared_project_roster(self) -> None:
        selection = self._selection(APP)
        with patch(
            "project_mcp_backend._bounded_run",
            side_effect=self._docker_roster(selection, [_MCP_ID]),
        ):
            rows = ProjectMcpBackend().inspect(selection)
        self.assertEqual([_MCP_ID], [row["Id"] for row in rows])

    def test_inspect_ignores_worker_only_project_roster(self) -> None:
        selection = self._selection(APP)
        with patch(
            "project_mcp_backend._bounded_run", side_effect=self._docker_roster(selection, [])
        ):
            rows = ProjectMcpBackend().inspect(selection)
        self.assertEqual([], rows)

    def test_inspect_refuses_duplicate_mcp_services(self) -> None:
        selection = self._selection(APP)
        with patch(
            "project_mcp_backend._bounded_run",
            side_effect=self._docker_roster(selection, [_MCP_ID, _SECOND_MCP_ID]),
        ):
            with self.assertRaises(BackendError) as raised:
                ProjectMcpBackend().inspect(selection)
        self.assertEqual("DOCKER_PUBLICATION_FAILED", raised.exception.code)

    def test_inspect_refuses_foreign_project_row(self) -> None:
        selection = self._selection(APP)
        with patch(
            "project_mcp_backend._bounded_run",
            side_effect=self._docker_roster(
                selection,
                [_MCP_ID],
                foreign_project=True,
            ),
        ):
            with self.assertRaises(BackendError) as raised:
                ProjectMcpBackend().inspect(selection)
        self.assertEqual("RUNTIME_MISMATCH", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
