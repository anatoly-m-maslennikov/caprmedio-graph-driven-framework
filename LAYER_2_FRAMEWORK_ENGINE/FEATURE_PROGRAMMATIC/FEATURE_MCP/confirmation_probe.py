"""Opt-in Codex form diagnostic; no publication or authorization capability."""
from __future__ import annotations

import asyncio
import json

import anyio
from mcp import types
from mcp.shared.exceptions import MCPError, NoBackChannelError
from pydantic import ValidationError


WAIT_SECONDS = 60
MESSAGE = (
    "Codex confirmation UI test only. No files will change and no publication "
    "will run. A response is not authorization or authenticated human evidence."
)
FORM_SCHEMA = {
    "type": "object",
    "properties": {
        "acknowledge": {"type": "boolean", "title": "I understand this is only a UI test"},
    },
    "required": ["acknowledge"],
    "additionalProperties": False,
}
TOOL = types.Tool(
    name="probe_codex_confirmation",
    description="Test the host's confirmation form UI without files, publication or authorization.",
    annotations=types.ToolAnnotations(read_only_hint=True, destructive_hint=False,
                                     idempotent_hint=False, open_world_hint=False),
    input_schema={
        "type": "object",
        "properties": {"request": {"type": "object", "properties": {}, "additionalProperties": False}},
        "required": ["request"],
        "additionalProperties": False,
    },
)


def _result(status, *, action=None, content=None):
    data = {"status": status, "action": action, "content": content,
            "authorization": False, "effects": [],
            "diagnostics": ["UI diagnostic only; not authorization or authenticated human evidence."]}
    return types.CallToolResult(content=[types.TextContent(type="text", text=json.dumps(data))],
                                structured_content=data, is_error=status != "observed")


async def run_confirmation_probe(context, arguments):
    """Use this invocation's outer session; never infer trust from client identity."""
    if (type(arguments) is not dict or set(arguments) != {"request"}
            or type(arguments["request"]) is not dict or arguments["request"]):
        return _result("invalid_input")
    session = getattr(context, "session", None)
    request_id = getattr(context, "request_id", None)
    capabilities = getattr(session, "client_capabilities", None)
    elicitation = getattr(capabilities, "elicitation", None)
    if (request_id is None or not getattr(session, "can_send_request", False)
            or getattr(elicitation, "form", None) is None):
        return _result("unsupported")
    try:
        reply = await asyncio.wait_for(
            session.elicit_form(MESSAGE, FORM_SCHEMA, related_request_id=request_id), WAIT_SECONDS,
        )
    except TimeoutError:
        return _result("timed_out")
    except NoBackChannelError:
        return _result("unsupported")
    except ValidationError:
        return _result("malformed_response")
    except (ConnectionError, anyio.EndOfStream, anyio.ClosedResourceError, anyio.BrokenResourceError):
        return _result("disconnected")
    except MCPError:
        return _result("elicitation_failed")
    if not isinstance(reply, types.ElicitResult) or reply.action not in {"accept", "decline", "cancel"}:
        return _result("malformed_response")
    if reply.action == "accept":
        if (type(reply.content) is not dict or set(reply.content) != {"acknowledge"}
                or type(reply.content["acknowledge"]) is not bool):
            return _result("malformed_response")
    elif reply.content is not None:
        return _result("malformed_response")
    return _result("observed", action=reply.action, content=reply.content)
