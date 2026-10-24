"""Shared host Streamable HTTP transport for multiple Project gateways."""

from __future__ import annotations

import argparse
from collections.abc import Mapping
from contextlib import asynccontextmanager
from concurrent.futures import CancelledError as FutureCancelledError
from pathlib import Path
import sys
from typing import Any, Callable

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route

from health_page import render_health_page
from http_server import (
    MAX_REQUEST_BODY_SIZE,
    PATH,
    PORT,
    SECURITY,
    LoopbackGuard,
    _accepts_html,
)
from operation_error_boundary import FailureRecord
from runtime_failure_diagnostics import report_failure
from runtime_process_boundary import run_process

from shared_gateway import SharedGateway


def _snapshot_failure() -> None:
    _, secondary = report_failure(
        None,
        FailureRecord(
            "WARNING", "shared_health_snapshot_unavailable",
            "host health snapshot unavailable",
        ),
        component="MCP_HTTP",
        operation="shared_health_snapshot",
    )
    if secondary is not None:
        try:
            sys.stderr.write("caprmedio: host health snapshot unavailable\n")
            sys.stderr.flush()
        except Exception:
            pass


def _snapshot(gateway: Any) -> Mapping[str, Any]:
    """Read the already-published host frontier without probing a Project."""
    reader = getattr(gateway, "status", None)
    if not callable(reader):
        _snapshot_failure()
        return {}
    try:
        value = reader()
    except FutureCancelledError:
        raise
    except Exception:
        _snapshot_failure()
        return {}
    if not isinstance(value, Mapping):
        _snapshot_failure()
        return {}
    return value


def _ready(snapshot: Mapping[str, Any]) -> bool:
    initialized = snapshot.get("initialized")
    return type(initialized) is bool and initialized and isinstance(
        snapshot.get("advertised_tools"), list,
    )


async def _health(request: Request, gateway: Any):
    snapshot = _snapshot(gateway)
    ready = _ready(snapshot)
    status_code = 200 if ready else 503
    if not _accepts_html(request.headers.get("accept")):
        return JSONResponse({"ready": ready}, status_code=status_code)
    return HTMLResponse(
        render_health_page(snapshot, ready=ready, gateway=gateway),
        status_code=status_code,
        headers={"Cache-Control": "no-store"},
    )


async def health(request: Request, gateway: Any):
    """Serve one read-only host health snapshot."""
    return await _health(request, gateway)


def create_app(config: Any, *, gateway_factory: Callable[..., Any] = SharedGateway):
    """Create one guarded host app; Project selection stays inside the router."""
    gateway = gateway_factory(config)
    server = gateway.build_server()

    async def health_endpoint(request: Request):
        return await health(request, gateway)

    app = server.streamable_http_app(
        streamable_http_path=PATH,
        transport_security=SECURITY,
        max_request_body_size=MAX_REQUEST_BODY_SIZE,
        host="127.0.0.1",
        custom_starlette_routes=[Route("/health", health_endpoint)],
    )
    inner_lifespan = app.router.lifespan_context

    @asynccontextmanager
    async def lifespan(application):
        async with inner_lifespan(application):
            try:
                await gateway.initialize()
                yield
            finally:
                await gateway.close()

    app.router.lifespan_context = lifespan
    guarded = LoopbackGuard(app)
    guarded.gateway = gateway
    guarded.starlette_app = app
    return guarded


def _serve(args: argparse.Namespace) -> Any:
    from host_runtime_config import load_host_runtime_config

    config = load_host_runtime_config(args.host_settings)
    import uvicorn

    uvicorn.run(create_app(config), host="0.0.0.0", port=PORT, log_level="warning")


def main(argv: list[str] | None = None) -> Any:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host-settings", type=Path)
    args = parser.parse_args(argv)
    return run_process(
        lambda: _serve(args), operation="mcp.shared_http_startup", root=None,
    )


if __name__ == "__main__":
    raise SystemExit(main())


__all__ = ["create_app", "health", "main"]
