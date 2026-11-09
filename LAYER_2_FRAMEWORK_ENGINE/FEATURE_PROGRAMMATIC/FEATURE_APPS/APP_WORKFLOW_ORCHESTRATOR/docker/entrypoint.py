"""Foreground services with immutable code and explicit runtime-only state."""

# CA-M-504@2

import json
import os
from pathlib import Path
import sys

APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path("/project")
TOOLS = APP.parents[1] / "FEATURE_TOOLS"
sys.path.insert(0, str(APP))
sys.path.insert(0, str(TOOLS))

from operation_error_boundary import (  # noqa: E402
    ExplicitBlockingRuntimeFailure,
    FailureRecord,
    operation_error_boundary,
)
from runtime_failure_diagnostics import report_failure  # noqa: E402


RUNTIME_MODES = frozenset({"mcp", "mcp-http", "shared-mcp"})


def _process_failure(mode, error):
    if mode not in RUNTIME_MODES:
        error = FailureRecord("WARNING", "invalid_runtime_mode", "runtime mode is unsupported")
    root = (
        None if mode == "shared-mcp" or mode not in RUNTIME_MODES
        else PROJECT_ROOT
    )
    operation = f"docker.entrypoint.{mode}" if mode in RUNTIME_MODES else "docker.entrypoint"
    failure, secondary = report_failure(
        root, error, component="DOCKER_ENTRYPOINT", operation=operation
    )
    payload = {"error": failure.code, "severity": failure.severity}
    if secondary:
        payload["diagnostic_error"] = secondary
    print(json.dumps(payload, separators=(",", ":")), file=sys.stderr)
    return 1


def _shared_mcp_command():
    settings = os.environ.get("CAPRMEDIO_HOST_SETTINGS")
    if not settings:
        raise ExplicitBlockingRuntimeFailure(
            "shared_host_settings_unavailable", "shared host settings are unavailable"
        )
    return [
        sys.executable,
        str(APP.parents[1] / "FEATURE_MCP/shared_http_server.py"),
        "--host-settings",
        settings,
    ]


def _exec_service(mode):
    if mode == "shared-mcp":
        command = _shared_mcp_command()
    else:
        paths = {
            "mcp": APP.parents[1] / "FEATURE_MCP/server.py",
            "mcp-http": APP.parents[1] / "FEATURE_MCP/server.py",
        }
        if mode not in paths:
            raise ValueError("unsupported runtime mode")
        command = [sys.executable, str(paths[mode]), "--project-root", str(PROJECT_ROOT)]
        if mode == "mcp-http":
            command += ["--transport", "streamable-http"]
        if mode in {"mcp", "mcp-http"}:
            for flag, key in (
                ("--control-root", "CAPRMEDIO_CONTROL_ROOT"),
                ("--instance-id", "CAPRMEDIO_PROJECT_INSTANCE_ID"),
                ("--host-project-root", "CAPRMEDIO_HOST_PROJECT_ROOT"),
            ):
                if key in os.environ:
                    command += [flag, os.environ[key]]
    try:
        os.execv(sys.executable, command)
    except OSError as error:
        raise ExplicitBlockingRuntimeFailure(
            "service_start_failed", "runtime service could not start"
        ) from error


def _dispatch(mode):
    _exec_service(mode)


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""

    @operation_error_boundary(on_error=lambda error: _process_failure(mode, error))
    def dispatch():
        _dispatch(mode)

    result = dispatch()
    return 0 if result is None else result


if __name__ == "__main__":
    raise SystemExit(main())
