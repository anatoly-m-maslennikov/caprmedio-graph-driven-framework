"""Reloadable Project-local stdio implementation behind the stable gateway."""
import argparse
from contextlib import contextmanager
from pathlib import Path
import sys
import time
from typing import Any, Iterator

# Include SDK and registry imports in this child-startup measurement.
_IMPORT_STARTED = time.monotonic()
from mcp.server import MCPServer  # noqa: E402
from mcp.server.mcpserver.exceptions import ToolError  # noqa: E402
from mcp.types import ToolAnnotations  # noqa: E402

TOOLS_ROOT = Path(__file__).resolve().parents[1] / '201_TOOLS'
sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / 'VALIDATE_ATOMS'))
from capability_discovery.service import Service  # noqa: E402
sys.path.insert(0, str(TOOLS_ROOT.parent / '203_APPS/WORKFLOW_ORCHESTRATOR'))
from orchestrator import Request as OrchestratorRequest, run as orchestrate  # noqa: E402
from selected_routes import register_selected_routes  # noqa: E402
from registered_tool_registry import register_catalog_tools  # noqa: E402
from hot_reload import (  # noqa: E402
    startup_selection,
    bind_selection,
    _startup_telemetry_enabled,
    _startup_timing,
)

_startup_timing(_startup_telemetry_enabled(), "implementation_import", _IMPORT_STARTED)


@contextmanager
def _startup_phase(phase: str) -> Iterator[None]:
    enabled, started = _startup_telemetry_enabled(), time.monotonic()
    try:
        yield
    except BaseException:
        _startup_timing(enabled, phase, started, "failed")
        raise
    else:
        _startup_timing(enabled, phase, started)


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
    discovery = Service(root, exposed=('workflow_orchestrator',))
    server = MCPServer('CAPRMEDIO', version='0.1.0', instructions=
        'Discovery and read-only Run observation; Operator-authorized, caller-coordinated '
        'gather/check/fix. workflow_orchestrator enqueues explicitly authorized Runs '
        'for a separately started worker. No recheck or automatically started Runs.')
    register_orchestrator(server, root)

    # Selected Workflow routes own their already-admitted public request
    # protocols.  Generic Tool descriptors may still compile for the same
    # capability, but never overwrite one of those public endpoints.
    with _startup_phase("selected_registration"):
        selected_routes = register_selected_routes(server, root)
        discovery.exposed.update(selected_routes.public_route_names)

    # Compile one effect-free descriptor frontier.  Registration is generic:
    # no capability name or adapter implementation is selected by this server.
    with _startup_phase("catalog"):
        _atoms, catalog_tools, _issues = discovery.catalog()
    with _startup_phase("catalog_registration"):
        registry = register_catalog_tools(
            server,
            root,
            [tool for tool in catalog_tools if not tool.get('selected_route')],
            occupied_public_names=selected_routes.public_route_names,
            registered_public_names=('workflow_orchestrator', *selected_routes.public_route_names),
        )
        discovery.registry_quarantined = registry.quarantined
        discovery.registry_withheld = registry.withheld
        discovery.exposed.update(registry.registered_names)
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
