# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
"""Real in-memory MCP journey support for the current direct packet."""

from __future__ import annotations

from contextlib import asynccontextmanager
import copy
import json
from pathlib import Path
import sys
import tempfile
from typing import Any, AsyncIterator, Mapping


MCP_TESTS = Path(__file__).resolve().parent
PROGRAMMATIC = MCP_TESTS.parents[1]
MCP = PROGRAMMATIC / "204_MCP"
WFO = PROGRAMMATIC / "203_APPS" / "WORKFLOW_ORCHESTRATOR"
WFO_TESTS = WFO / "tests"
for location in (MCP, WFO, WFO_TESTS):
    if str(location) not in sys.path:
        sys.path.insert(0, str(location))

from implementation_server import create_server  # noqa: E402
from interactive_direct_fixture import (  # noqa: E402
    InteractiveDirectFixture,
    build_interactive_direct_fixture,
)
from mcp.client._memory import InMemoryTransport as SDKInMemoryTransport  # noqa: E402
from mcp.client.session import ClientSession  # noqa: E402
from selected_execution import SelectedExecution  # noqa: E402
from selected_graph_validation import validate_graph  # noqa: E402
from selected_route_manifest import canonical_digest  # noqa: E402


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
@asynccontextmanager
async def journey_session() -> AsyncIterator[tuple[InteractiveDirectFixture, Any]]:
    with tempfile.TemporaryDirectory(prefix="direct-mcp-journey-") as temporary:
        fixture = build_interactive_direct_fixture(Path(temporary))
        server = create_server(fixture.root)  # type: ignore[no-untyped-call]
        async with SDKInMemoryTransport(server, raise_exceptions=True) as streams:
            async with ClientSession(*streams) as client:
                await client.initialize()
                yield fixture, client


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
async def call_tool(client: Any, name: str, request: Mapping[str, Any]) -> dict[str, Any]:
    response = await client.call_tool(name, {"request": dict(request)})
    if response.is_error or not isinstance(response.structured_content, dict):
        raise AssertionError(f"MCP tool {name} returned a protocol or structured-result error")
    return dict(response.structured_content)


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def build_execute_request(
    fixture: InteractiveDirectFixture,
    preview: Mapping[str, Any],
    request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    execute = copy.deepcopy(dict(request or fixture.execution_request))
    execute["mode"] = "execute"
    execute["proposal_receipt"] = copy.deepcopy(preview["proposal_receipt"])
    execute["proposal_receipt_digest"] = preview["proposal_receipt_digest"]
    graph = validate_graph(fixture.root, execute)
    run_id = str(execute["request_id"])
    limits = execute["parameters"].get("run_visit_limits")
    execute["requested_runs"] = SelectedExecution.build_requested_runs(graph, run_id, limits)
    execute["assigned_action_id"] = "CA-O-017"
    bindings = {
        key: copy.deepcopy(execute[key])
        for key in (
            "request_id",
            "operation_route",
            "proposal_receipt_digest",
            "parameters_digest",
            "target_frontier_digest",
            "effects_digest",
            "definition_manifest",
            "source_freshness",
        )
    }
    execute["operator_authorization"] = {
        "authorization_ref": "interactive-direct-fixture-operator",
        "authorization_freshness": {
            "state": "current",
            "digest": canonical_digest(execute["source_freshness"]),
        },
        **bindings,
    }
    return execute


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def assert_direct_method_rows(
    fixture: InteractiveDirectFixture, packet: Mapping[str, Any]
) -> None:
    methods = packet.get("methods")
    trusted = fixture.trusted_methods
    if not isinstance(methods, list) or len(methods) != 41 or len(trusted) != 41:
        raise AssertionError("the current direct packet and trusted inventory must each contain 41 Methods")
    expected_fields = {"atom_id", "version", "path", "sha256", "content"}
    if any(set(row) != expected_fields for row in (*methods, *trusted)):
        raise AssertionError("direct Method rows must use the exact five-field SourceRow shape")
    packet_pins = {(row.get("atom_id"), row.get("version"), row.get("sha256")) for row in methods}
    trusted_pins = {(row.get("atom_id"), row.get("version"), row.get("sha256")) for row in trusted}
    if packet_pins != trusted_pins or any(not row.get("content") for row in methods):
        raise AssertionError("direct Methods are not full SourceRows matching trusted inventory")


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def pending_capture(result: Mapping[str, Any], fixture: InteractiveDirectFixture) -> dict[str, Any]:
    if result.get("disposition") != "started" or result.get("status") != "pending_action":
        raise AssertionError(f"expected a pending Integrated capture, got {result}")
    capture = result.get("capture")
    if not isinstance(capture, Mapping):
        raise AssertionError("pending Integrated response has no capture")
    packet = capture.get("packet")
    if not isinstance(packet, Mapping):
        raise AssertionError("pending capture lacks its public packet")
    assert_direct_method_rows(fixture, packet)
    return dict(capture)


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def result_payload(
    result: str, outputs: Mapping[str, Any], *, blockers: list[str] | None = None
) -> dict[str, Any]:
    return {
        "result": result,
        "outputs": dict(outputs),
        "evidence": [{"kind": "interactive-fixture", "result": result}],
        "blockers": list(blockers or []),
    }


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def submit_request(
    pending: Mapping[str, Any], response: Mapping[str, Any]
) -> dict[str, Any]:
    capture = pending.get("capture")
    binding = capture.get("run_binding") if isinstance(capture, Mapping) else None
    run_id = pending.get("workflow_run_id")
    action_run_id = pending.get("action_run_id")
    continuation_id = pending.get("continuation_id")
    if not isinstance(run_id, str) and isinstance(binding, Mapping):
        run_id = binding.get("workflow_run_id")
    if not isinstance(action_run_id, str) and isinstance(binding, Mapping):
        action_run_id = binding.get("action_run_id")
    if not isinstance(continuation_id, str) and isinstance(capture, Mapping):
        continuation_id = capture.get("continuation_id")
    if not all(isinstance(value, str) and value for value in (run_id, action_run_id, continuation_id)):
        raise AssertionError("pending response did not expose submission Run identities")
    return {
        "operation": "submit_result",
        "run_id": run_id,
        "action_run_id": action_run_id,
        "continuation_id": continuation_id,
        "result": dict(response),
    }


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def diagnostic_text(result: Mapping[str, Any]) -> str:
    return json.dumps(result, ensure_ascii=False, sort_keys=True).lower()


# implementation of:
# Requirement: CA-R-2117
# Method: CA-M-431
def source_drift_path(fixture: InteractiveDirectFixture) -> Path:
    route = next(
        row for row in fixture.manifest["routes"] if row["route"] == "run_implementation_workflow"
    )
    return fixture.root / str(route["workflow"]["source_path"])
