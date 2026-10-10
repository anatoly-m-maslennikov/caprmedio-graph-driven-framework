"""Reloadable Project-local stdio implementation behind the stable gateway."""
import argparse
from pathlib import Path
import sys
from typing import Any

from mcp.server import MCPServer
from mcp.server.mcpserver.exceptions import ToolError
from mcp.types import ToolAnnotations

TOOLS_ROOT = Path(__file__).resolve().parents[1] / '201_TOOLS'
TOOLS = TOOLS_ROOT / 'RMED_ATOMS_BASE_REVISE'
sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / 'VALIDATE_ATOMS'))
sys.path.insert(0, str(TOOLS))
from rmed_atoms_base_revise import Request, run  # noqa: E402 - repository path bootstrap
from capability_discovery.service import Service, Query, Context, Observation, Watch  # noqa: E402
sys.path.insert(0, str(TOOLS_ROOT.parent / '203_APPS/WORKFLOW_ORCHESTRATOR'))
from orchestrator import Request as OrchestratorRequest, run as orchestrate  # noqa: E402
from selected_routes import QUERY_ROUTE_NAMES, register_selected_routes  # noqa: E402
from framework_image_restoration_mcp import (  # noqa: E402
    MCP_NAME as RESTORATION_MCP_NAME,
    TOOL_NAME as RESTORATION_TOOL_NAME,
    register_framework_image_restoration,
)
from source_admission_mcp import (  # noqa: E402
    MCP_NAME as SOURCE_ADMISSION_MCP_NAME,
    TOOL_NAME as SOURCE_ADMISSION_TOOL_NAME,
    register_source_admission,
)
from hot_reload import startup_selection, bind_selection


def register_orchestrator(server, root):
    @server.tool(name='workflow_orchestrator', structured_output=True, annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=False, idempotent_hint=True, open_world_hint=False))
    def workflow_orchestrator(request: OrchestratorRequest) -> dict[str, Any]:
        """Enqueue or inspect an independent Run; requires an explicitly initialized local worker."""
        try:
            return orchestrate(root, request)
        except (ValueError, OSError, RuntimeError) as error:
            raise ToolError(str(error)) from error


def create_server(root):
    root = Path(root).resolve(strict=True)
    discovery = Service(root, exposed=('discover_tools', 'discover_operations',
        'get_execution_context', 'get_execution_status', 'resume_execution_context',
        'watch_execution', 'rmed_atoms_base_revise', 'workflow_orchestrator',
        *QUERY_ROUTE_NAMES))
    server = MCPServer('CAPRMEDIO', version='0.1.0', instructions=
        'Discovery and read-only Run observation; Operator-authorized, caller-coordinated '
        'gather/check/fix. workflow_orchestrator enqueues explicitly authorized Runs '
        'for a separately started worker. No recheck or automatically started Runs.')
    register_orchestrator(server, root)

    # O187 is a separately source-declared direct Action.  It must never be
    # inferred from the selected-route manifest, and a missing or altered
    # delivery binding leaves it unregistered and unresolved.
    restoration_bindings = [
        item for item in discovery.catalog()[1]
        if item.get('name') == RESTORATION_TOOL_NAME
    ]
    if len(restoration_bindings) == 1 and register_framework_image_restoration(
        server, root, binding=restoration_bindings[0],
    ):
        discovery.exposed.add(RESTORATION_MCP_NAME)

    # O199 is separately source-declared as well.  The adapter owns its closed
    # request schema, so discovery can expose it only after the one current
    # catalog binding has admitted the actual server registration.
    source_admission_bindings = [
        item for item in discovery.catalog()[1]
        if item.get('name') == SOURCE_ADMISSION_TOOL_NAME
    ]
    if len(source_admission_bindings) == 1 and register_source_admission(
        server, root, binding=source_admission_bindings[0],
    ):
        discovery.exposed.add(SOURCE_ADMISSION_MCP_NAME)

    @server.tool(name='rmed_atoms_base_revise', structured_output=True, annotations=ToolAnnotations(
        read_only_hint=False, destructive_hint=False, idempotent_hint=False, open_world_hint=False))
    def workflow(request: Request) -> dict[str, Any]:
        """Describe or coordinate RMED Atoms Base Revise; root is fixed at server startup."""
        try:
            return run(root, request)
        except (ValueError, OSError, RuntimeError, KeyError, TypeError, IndexError) as error:
            raise ToolError(str(error)) from error

    annotations = ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                  idempotent_hint=True, open_world_hint=False)

    @server.tool(name='discover_tools', annotations=annotations)
    def discover_tools(request: Query) -> dict[str, Any]:
        """Find declared Tools and observed source availability."""
        return discovery.discover(request)

    @server.tool(name='discover_operations', annotations=annotations)
    def discover_operations(request: Query) -> dict[str, Any]:
        """Find active methodology Actions and Workflows."""
        return discovery.discover(request, operations=True)

    @server.tool(name='get_execution_context', annotations=annotations)
    def get_execution_context(request: Context) -> dict[str, Any]:
        """Read an exact capability definition without executing it."""
        return discovery.context(request)

    @server.tool(name='get_execution_status', annotations=annotations)
    def get_execution_status(request: Observation) -> dict[str, Any]:
        """Read saved Run progress and optional results."""
        return discovery.status(request)[0]

    @server.tool(name='resume_execution_context', annotations=annotations)
    def resume_execution_context(request: Observation) -> dict[str, Any]:
        """Recover saved inputs and pending work without dispatch or replay."""
        return discovery.resume(request)

    @server.tool(name='watch_execution', annotations=annotations)
    async def watch_execution(request: Watch) -> dict[str, Any]:
        """Wait for saved Run changes and confirmed Journal events using a cursor."""
        return await discovery.watch(request)

    selected_routes = register_selected_routes(server, root)
    discovery.exposed.update(selected_routes.public_route_names)
    return server


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--project-root', required=True, type=Path)
    parser.add_argument('--control-root')
    parser.add_argument('--instance-id')
    parser.add_argument('--host-project-root')
    args = parser.parse_args()
    selection = startup_selection(args.project_root, args.control_root, args.instance_id, args.host_project_root)
    with bind_selection(selection):
        create_server(args.project_root).run(transport='stdio')
