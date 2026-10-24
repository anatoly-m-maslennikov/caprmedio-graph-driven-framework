"""Foreground services with immutable code and explicit runtime-only credentials."""

import json
import os
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
import shutil
import sys
from urllib.request import urlopen

APP = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path("/project")
TOOLS = APP.parents[1] / "201_TOOLS"
sys.path.insert(0, str(APP))
sys.path.insert(0, str(TOOLS))

from operation_error_boundary import (  # noqa: E402
    ExplicitBlockingRuntimeFailure,
    FailureRecord,
    operation_error_boundary,
)
from runtime_failure_diagnostics import report_failure  # noqa: E402


RUNTIME_MODES = frozenset(
    {"agent", "agent-health", "health", "worker", "mcp", "mcp-http", "shared-mcp"}
)


def seed_authentication():
    if os.environ.get("CAPRMEDIO_AGENT_MODE") == "mock":
        return
    destination = Path.home() / ".codex/auth.json"
    if destination.is_file():
        return
    seed = Path("/run/secrets/codex_auth")
    if not seed.is_file():
        raise ExplicitBlockingRuntimeFailure(
            "agent_auth_unavailable", "agent credentials are unavailable"
        )
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(".initial")
        shutil.copyfile(seed, temporary)
        temporary.chmod(0o600)
        temporary.replace(destination)
    except OSError as error:
        raise ExplicitBlockingRuntimeFailure(
            "agent_auth_setup_failed", "agent credentials could not be initialized"
        ) from error


def worker_health():
    from engine import runtime_fingerprint

    directory = PROJECT_ROOT / ".caprmedio_install/workflow_orchestrator/docker"
    ready = json.loads((directory / "worker.ready").read_text())
    state = json.loads((directory / "worker.json").read_text())
    if ready["pid"] != state["pid"] or state["state"] != "starting":
        raise ExplicitBlockingRuntimeFailure("worker_unavailable", "worker is not ready")
    os.kill(ready["pid"], 0)
    if ready["runtime_fingerprint"] != runtime_fingerprint(PROJECT_ROOT):
        raise ExplicitBlockingRuntimeFailure("worker_unavailable", "worker is not ready")


def _process_failure(mode, error):
    if mode not in RUNTIME_MODES:
        error = FailureRecord("WARNING", "invalid_runtime_mode", "runtime mode is unsupported")
    root = (
        None
        if mode in {"agent-health", "shared-mcp"} or mode not in RUNTIME_MODES
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


def _run_agent():
    try:
        seed_authentication()
        import uvicorn
        from agent_service import app

        uvicorn.run(app, host="0.0.0.0", port=8091, log_level="warning")
    except FutureCancelledError:
        raise
    except ExplicitBlockingRuntimeFailure:
        raise
    except Exception as error:
        raise ExplicitBlockingRuntimeFailure(
            "agent_start_failed", "agent service could not start"
        ) from error


def _run_agent_health():
    try:
        with urlopen("http://127.0.0.1:8091/health", timeout=3) as response:
            if not json.load(response)["ready"]:
                raise RuntimeError("agent is not ready")
    except FutureCancelledError:
        raise
    except Exception as error:
        raise ExplicitBlockingRuntimeFailure(
            "agent_unavailable", "agent health is unavailable"
        ) from error


def _run_worker_health():
    try:
        worker_health()
    except FutureCancelledError:
        raise
    except ExplicitBlockingRuntimeFailure:
        raise
    except Exception as error:
        raise ExplicitBlockingRuntimeFailure("worker_unavailable", "worker is not ready") from error


def _shared_mcp_command():
    settings = os.environ.get("CAPRMEDIO_HOST_SETTINGS")
    if not settings:
        raise ExplicitBlockingRuntimeFailure(
            "shared_host_settings_unavailable", "shared host settings are unavailable"
        )
    return [
        sys.executable,
        str(APP.parents[1] / "204_MCP/shared_http_server.py"),
        "--host-settings",
        settings,
    ]


def _exec_service(mode):
    if mode == "shared-mcp":
        command = _shared_mcp_command()
    else:
        paths = {
            "worker": APP / "orchestrator.py",
            "mcp": APP.parents[1] / "204_MCP/server.py",
            "mcp-http": APP.parents[1] / "204_MCP/server.py",
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
        if mode == "worker":
            command.append("worker")
    try:
        os.execv(sys.executable, command)
    except FutureCancelledError:
        raise
    except OSError as error:
        raise ExplicitBlockingRuntimeFailure(
            "service_start_failed", "runtime service could not start"
        ) from error


def _dispatch(mode):
    if mode == "agent":
        _run_agent()
    elif mode == "agent-health":
        _run_agent_health()
    elif mode == "health":
        _run_worker_health()
    else:
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
