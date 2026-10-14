"""Local SDK registration checks for the minimal launcher Project corpus."""

from collections.abc import Iterator
from contextlib import contextmanager
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from mcp.server.mcpserver.exceptions import ToolError

import test_project_launcher_docker_e2e as launcher
from project_mcp_backend import BackendError, ProjectMcpBackend

sys.path.insert(0, str(launcher.TOOLS.parent / "204_MCP"))
from hot_reload import CONTROL, STATUS  # noqa: E402
from implementation_server import create_server  # noqa: E402


@contextmanager
def fixture_pair() -> Iterator[list[launcher.ProjectFixture]]:
    parent = launcher.ROOT / ".caprmedio_tmp" / "launcher-fixture-capability-checks"
    parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=parent) as directory:
        with patch.object(launcher, "_available_port", side_effect=(45121, 45122)):
            yield launcher._fixtures(Path(directory), "two-repositories")


class FixtureCapabilityTests(unittest.IsolatedAsyncioTestCase):
    async def test_minimal_sdk_registration_context_isolation_and_no_effect_refusal(self) -> None:
        with fixture_pair() as fixtures:
            before = [fixture.snapshot() for fixture in fixtures]
            for index, fixture in enumerate(fixtures):
                with launcher.bind_selection(
                    launcher.resolve_project(fixture.root, fixture.control)
                ):
                    server = create_server(fixture.root)
                    names = {tool.name for tool in await server.list_tools()}
                    gateway_names = names | {CONTROL.name, STATUS.name}
                    self.assertLessEqual(launcher.LAUNCHER_REQUIRED_TOOLS, gateway_names)
                    self.assertNotIn("create_atom", names)
                    result = await server.call_tool(
                        "get_execution_context", {"request": {"id": fixture.atom_id}}
                    )
                    context = launcher._structured_tool_result(result)
                    self.assertTrue(context["context_complete"])
                    self.assertEqual(fixture.source_ref, context["definition"]["source_path"])
                    self.assertEqual(fixture.source_sha256, context["definition"]["sha256"])
                    self.assertIn(fixture.marker, context["definition"]["content"])
                    with self.assertRaises(ToolError):
                        await server.call_tool(
                            "get_execution_context",
                            {"request": {"id": fixtures[1 - index].atom_id}},
                        )
                    with self.assertRaises(ToolError):
                        await server.call_tool(
                            "create_atom",
                            {
                                "request": {
                                    "operation_route": "create_atom",
                                    "request_id": "unconfigured",
                                }
                            },
                        )
            self.assertEqual(before, [fixture.snapshot() for fixture in fixtures])

    async def test_missing_context_declaration_does_not_register_the_tool(self) -> None:
        with fixture_pair() as fixtures:
            fixture = fixtures[0]
            declaration = (
                fixture.root
                / fixture.control
                / "GET_EXECUTION_CONTEXT"
                / "07_delivery"
                / launcher._CONTEXT_DECLARATION_PATH.name
            )
            declaration.unlink()
            with launcher.bind_selection(launcher.resolve_project(fixture.root, fixture.control)):
                names = {tool.name for tool in await create_server(fixture.root).list_tools()}
            self.assertNotIn("get_execution_context", names)

    def test_collision_inspection_refuses_foreign_project_identity(self) -> None:
        with fixture_pair() as fixtures:
            selection = launcher.resolve_project(fixtures[0].root, fixtures[0].control)
            labels = {
                "org.caprmedio.project": selection.instance_id,
                "org.caprmedio.service": "mcp-http",
                "org.caprmedio.control_root": selection.control_relative.as_posix(),
                "org.caprmedio.host_project_root": str(selection.root),
            }
            row = {
                "Id": "a" * 64,
                "Image": "sha256:" + "b" * 64,
                "Config": {"Labels": labels},
                "Mounts": [
                    {"Type": "bind", "Source": str(selection.root), "Destination": "/project"}
                ],
                "State": {"Status": "created"},
                "NetworkSettings": {"Ports": {}},
            }
            self.assertTrue(ProjectMcpBackend._projection_matches_selection(row, selection))
            labels["org.caprmedio.project"] = "f" * 64
            with patch("project_mcp_backend._bounded_run", side_effect=("a" * 64, json.dumps(row))):
                with self.assertRaises(BackendError) as raised:
                    ProjectMcpBackend().inspect(selection)
            self.assertEqual("RUNTIME_MISMATCH", raised.exception.code)


if __name__ == "__main__":
    unittest.main()
