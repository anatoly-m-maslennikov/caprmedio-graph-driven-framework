"""Loopback-only Streamable HTTP transport for the MCP gateway."""
import argparse
import asyncio
from contextlib import asynccontextmanager
from contextlib import nullcontext
from pathlib import Path
import re

from starlette.requests import Request
from starlette.responses import HTMLResponse, JSONResponse, Response
from starlette.routing import Route

from health_page import render_health_page
from hot_reload import Gateway, startup_selection, bind_selection
from mcp.server.transport_security import TransportSecuritySettings

PATH = "/mcp"
PORT = 8092
# A sealed Release carries its complete source inventory in the request.  Keep
# a finite transport bound while allowing that inventory and its authorization.
MAX_REQUEST_BODY_SIZE = 16 * 1024 * 1024
SECURITY = TransportSecuritySettings(
    enable_dns_rebinding_protection=True,
    allowed_hosts=["127.0.0.1:*", "localhost:*", "[::1]:*"],
    allowed_origins=["http://127.0.0.1:*", "http://localhost:*", "http://[::1]:*"],
)


class LoopbackGuard:
    """Apply loopback Host and Origin admission before the MCP ASGI application."""
    def __init__(self, app, selection=None):
        self.app = app
        self.selection = selection

    async def __call__(self, scope, receive, send):
        with bind_selection(self.selection) if self.selection is not None else nullcontext():
            await self._call(scope, receive, send)

    async def _call(self, scope, receive, send):
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        request = Request(scope, receive)
        host = request.headers.get("host", "")
        origin = request.headers.get("origin")
        valid_host = re.fullmatch(r"(?:127\.0\.0\.1|localhost|\[::1\])(?::\d+)?", host)
        valid_origin = origin is None or re.fullmatch(
            r"http://(?:127\.0\.0\.1|localhost|\[::1\])(?::\d+)?", origin)
        if not valid_host:
            await Response(status_code=421)(scope, receive, send)
            return
        if not valid_origin:
            await Response(status_code=403)(scope, receive, send)
            return
        await self.app(scope, receive, send)


def _accepts_html(value):
    """Honor explicit text/html only when its quality is not lower than JSON."""
    if not isinstance(value, str):
        return False
    html_quality = None
    explicit_json_quality = None
    wildcard_quality = 0.0
    for item in value.split(","):
        parts = [part.strip() for part in item.split(";")]
        if not parts:
            continue
        quality = 1.0
        for parameter in parts[1:]:
            key, separator, raw = parameter.partition("=")
            if key.strip().lower() != "q" or not separator:
                continue
            try:
                quality = float(raw.strip())
            except ValueError:
                quality = 0.0
        media_type = parts[0].lower()
        if media_type == "text/html":
            html_quality = max(html_quality or 0.0, quality)
        elif media_type == "application/json":
            explicit_json_quality = max(explicit_json_quality or 0.0, quality)
        elif media_type == "*/*":
            wildcard_quality = max(wildcard_quality, quality)
    json_quality = (
        explicit_json_quality if explicit_json_quality is not None else wildcard_quality
    )
    return (
        html_quality is not None
        and 0.0 < html_quality <= 1.0
        and html_quality >= json_quality
    )


def _gateway_ready(gateway):
    generation = gateway.active
    return generation is not None and not generation.task.done()


async def health(request, gateway):
    ready = _gateway_ready(gateway)
    status_code = 200 if ready else 503
    if not _accepts_html(request.headers.get("accept")):
        return JSONResponse({"ready": ready}, status_code=status_code)
    observer = getattr(gateway, "health_observations", None)
    try:
        snapshot = observer.snapshot() if observer is not None else {}
    except Exception:
        snapshot = {}
    return HTMLResponse(
        render_health_page(snapshot, ready=ready, gateway=gateway),
        status_code=status_code,
        headers={"Cache-Control": "no-store"},
    )


def create_app(root, implementation=None, *, selection=None):
    gateway = Gateway(root, implementation=implementation, selection=selection)
    server = gateway.build_server()
    async def readiness(request):
        return await health(request, gateway)

    app = server.streamable_http_app(
        streamable_http_path=PATH,
        transport_security=SECURITY,
        max_request_body_size=MAX_REQUEST_BODY_SIZE,
        host="127.0.0.1",
        custom_starlette_routes=[Route("/health", readiness)],
    )
    inner_lifespan = app.router.lifespan_context

    @asynccontextmanager
    async def lifespan(application):
        async with inner_lifespan(application):
            await gateway.initialize()
            try:
                yield
            finally:
                await gateway.close()

    app.router.lifespan_context = lifespan
    guarded = LoopbackGuard(app, selection)
    guarded.gateway = gateway
    guarded.starlette_app = app
    return guarded


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True, type=Path)
    parser.add_argument("--control-root")
    parser.add_argument("--instance-id")
    parser.add_argument("--host-project-root")
    parser.add_argument("--host", default="0.0.0.0")
    parser.add_argument("--port", default=PORT, type=int)
    args = parser.parse_args()
    if args.host != "0.0.0.0" or args.port != PORT:
        raise ValueError("HTTP MCP requires the container bind 0.0.0.0:8092")
    import uvicorn
    selection = startup_selection(args.project_root, args.control_root, args.instance_id, args.host_project_root)
    uvicorn.run(create_app(args.project_root, selection=selection), host=args.host, port=args.port, log_level="warning")


if __name__ == "__main__":
    main()
