# CA-R-1106@21
# CA-R-1108@21
# CA-M-322@13
# CA-R-1820@9
# CA-M-506@2
# CA-D-704@1

"""Project-local MCP implementation for direct or optional reload serving."""

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

TOOLS_ROOT = Path(__file__).resolve().parents[1] / "FEATURE_TOOLS"
sys.path.insert(0, str(TOOLS_ROOT))
sys.path.insert(0, str(TOOLS_ROOT / "VALIDATE_ATOMS"))
from capability_discovery.service import Service  # noqa: E402
from operation_error_boundary import (  # noqa: E402
    operation_error_boundary,
)
from runtime_failure_diagnostics import report_failure  # noqa: E402
from runtime_process_boundary import run_process  # noqa: E402

sys.path.insert(0, str(TOOLS_ROOT.parent / "FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR"))
from orchestrator import Request as OrchestratorRequest, run as orchestrate  # noqa: E402
from selected_routes import register_selected_routes  # noqa: E402
from registered_tool_runtime import register_generated_tools  # noqa: E402
from tool_registry_asset import load_generated_registry  # noqa: E402
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
    @server.tool(
        name="workflow_orchestrator",
        structured_output=True,
        annotations=ToolAnnotations(
            read_only_hint=False,
            destructive_hint=False,
            idempotent_hint=True,
            open_world_hint=False,
        ),
    )
    def workflow_orchestrator(request: OrchestratorRequest) -> dict[str, Any]:
        """Enqueue or inspect an independent Run; requires an explicitly initialized local worker."""

        def on_error(error: Exception) -> object:
            failure, secondary = report_failure(
                Path(root),
                error,
                component="MCP_ORCHESTRATOR",
                operation="workflow_orchestrator",
                correlation_id=getattr(request, "run_id", None),
            )
            message = f"{failure.code}: {failure.message}"
            if secondary:
                message += "; technical diagnostic unavailable"
            raise ToolError(message) from error

        @operation_error_boundary(on_error=on_error)
        def guarded() -> dict[str, Any]:
            return orchestrate(root, request)

        return guarded()


def create_server(root):
    root = Path(root).resolve(strict=True)
    blacklist = Service(root).tool_blacklist()
    generated_registry, selected_route_names = load_generated_registry(
        Path(__file__).resolve().parents[3]
    )
    server = MCPServer(
        "CAPRMEDIO",
        version="0.1.0",
        instructions="Discovery and read-only Run observation; Operator-authorized, caller-coordinated "
        "gather/check/fix. workflow_orchestrator enqueues explicitly authorized Runs "
        "for a separately started worker. No recheck or automatically started Runs.",
    )
    if "workflow_orchestrator" not in blacklist:
        register_orchestrator(server, root)

    # Selected Workflow routes own their already-admitted public request
    # protocols.  Generic Tool descriptors may still compile for the same
    # capability, but never overwrite one of those public endpoints.
    with _startup_phase("selected_registration"):
        selected_routes = register_selected_routes(
            server,
            root,
            route_names=selected_route_names,
            tool_blacklist=blacklist,
        )

    # The generated asset chooses providers; the registry only checks installed
    # code and projects those canonical adapters into the MCP transport.
    with _startup_phase("registry_registration"):
        register_generated_tools(
            server,
            root,
            generated_registry,
            occupied_public_names=selected_routes.public_route_names,
            registered_public_names=("workflow_orchestrator", *selected_routes.public_route_names),
            tool_blacklist=blacklist,
        )
    return server


def _serve(args):
    selection = startup_selection(
        args.project_root, args.control_root, args.instance_id, args.host_project_root
    )
    with bind_selection(selection):
        create_server(args.project_root).run(transport="stdio")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--control-root")
    parser.add_argument("--instance-id")
    parser.add_argument("--host-project-root")
    args = parser.parse_args(argv)
    return run_process(
        lambda: _serve(args),
        operation="mcp.implementation_startup",
        root=args.project_root,
    )


if __name__ == "__main__":
    raise SystemExit(main())
