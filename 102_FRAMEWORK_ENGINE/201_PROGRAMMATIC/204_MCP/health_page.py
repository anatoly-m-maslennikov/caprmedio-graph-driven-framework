"""Bounded, read-only HTML representation of the MCP health snapshot."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from html import escape


MAX_HISTORY = 32
MAX_FIELD_LENGTH = 160
UNKNOWN = "unknown"
SAFE_ERRORS = frozenset({
    "connection", "returned-error", "timeout", "uncertain",
})


def _text(value: object, default: str = UNKNOWN) -> str:
    if not isinstance(value, (bool, float, int, str)):
        return default
    value = str(value)
    return value[:MAX_FIELD_LENGTH] or default


def _cell(value: object, default: str = UNKNOWN) -> str:
    return escape(_text(value, default), quote=True)


def _error(row: Mapping[str, object]) -> str:
    value = row.get("error_category", row.get("error"))
    return value if isinstance(value, str) and value in SAFE_ERRORS else UNKNOWN


def _recent(value: object) -> list[Mapping[str, object]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    return [row for row in value[-MAX_HISTORY:] if isinstance(row, Mapping)]


def _field(row: Mapping[str, object], *names: str) -> object:
    for name in names:
        if name in row:
            return row[name]
    return None


def _availability(value: object) -> str:
    return (
        value
        if isinstance(value, str) and value in {"available", "unavailable", UNKNOWN}
        else UNKNOWN
    )


def _gateway_availability(gateway: object) -> str:
    generation = getattr(gateway, "active", None)
    if generation is None:
        return UNKNOWN
    task = getattr(generation, "task", None)
    if task is None or not callable(getattr(task, "done", None)):
        return UNKNOWN
    try:
        return "unavailable" if task.done() else "available"
    except Exception:
        return UNKNOWN


def _registry_availability(gateway: object) -> tuple[str, str]:
    generation = getattr(gateway, "active", None)
    tools = getattr(generation, "tools", None) if generation is not None else None
    if not isinstance(tools, Sequence) or isinstance(tools, (str, bytes, bytearray)):
        return UNKNOWN, UNKNOWN
    return "available", str(len(tools))


def _call_rows(calls: Sequence[Mapping[str, object]]) -> str:
    if not calls:
        return (
            '<tr><td colspan="5">No Tool observations since gateway start; '
            'outcome is unknown.</td></tr>'
        )
    rows = []
    for call in calls:
        rows.append(
            "<tr>"
            f"<td>{_cell(_field(call, 'observed_at', 'timestamp', 'at'))}</td>"
            f"<td>{_cell(_field(call, 'name', 'tool'))}</td>"
            f"<td>{_cell(_field(call, 'outcome', 'status'))}</td>"
            f"<td>{_cell(_field(call, 'returned_outcome', 'returned'))}</td>"
            f"<td>{_cell(_error(call))}</td>"
            "</tr>"
        )
    return "".join(rows)


def _workflow_rows(workflows: Sequence[Mapping[str, object]]) -> str:
    if not workflows:
        return (
            '<tr><td colspan="6">No Workflow observations since gateway start; '
            'outcome is unknown.</td></tr>'
        )
    rows = []
    for workflow in workflows:
        rows.append(
            "<tr>"
            f"<td>{_cell(_field(workflow, 'observed_at', 'timestamp', 'at'))}</td>"
            f"<td>{_cell(_field(workflow, 'workflow_run_id', 'run_id', 'workflow'))}</td>"
            f"<td>{_cell(workflow.get('scheduler_status'))}</td>"
            f"<td>{_cell(workflow.get('outcome'))}</td>"
            f"<td>{_cell(workflow.get('disposition'))}</td>"
            f"<td>{_cell(_error(workflow))}</td>"
            "</tr>"
        )
    return "".join(rows)


def render_health_page(snapshot: Mapping[str, object], *, ready: bool, gateway: object) -> str:
    """Render only admitted snapshot fields; this function performs no I/O."""
    if not isinstance(snapshot, Mapping):
        snapshot = {}
    gateway_status = _gateway_availability(gateway)
    registry_status, tool_count = _registry_availability(gateway)
    calls = _recent(snapshot.get("calls"))
    workflows = _recent(snapshot.get("workflows"))
    readiness = "ready" if ready else "not ready"
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MCP health and history</title><style>
:root{{color-scheme:light dark}}
body{{font:16px system-ui,sans-serif;line-height:1.4;margin:2rem;max-width:1100px}}
section{{margin:1.5rem 0}}
table{{border-collapse:collapse;width:100%}}
th,td{{border:1px solid #888;padding:.4rem;text-align:left;vertical-align:top}}
th{{background:#8882}}code{{overflow-wrap:anywhere}}.note{{color:#666}}
</style></head><body>
<h1>MCP health and history</h1>
<section aria-labelledby="availability"><h2 id="availability">Availability</h2>
<dl><dt>Active gateway generation readiness</dt><dd>{_cell(readiness)}</dd>
<dt>Gateway task availability</dt><dd>{_cell(_availability(gateway_status))}</dd>
<dt>Advertised registry availability</dt><dd>{_cell(_availability(registry_status))}
({_cell(tool_count)} tools advertised)</dd></dl></section>
<p class="note">Process-local history since gateway start: {_cell(snapshot.get('started_at'))}.
At most {MAX_HISTORY} Tool and {MAX_HISTORY} Workflow observations are retained;
history resets when the gateway restarts. Missing or unobserved state remains unknown.</p>
<p class="note">Provider and worker health are not probed; observations are historical and missing state is unknown.</p>
<p class="note">Safe error categories: timeout (deadline exceeded); connection (transport failure); returned-error (the Tool returned an error); uncertain (the call result could not be established).</p>
<section aria-labelledby="calls"><h2 id="calls">Recent Tool calls</h2><table>
<thead><tr><th>Observed</th><th>Tool</th><th>Outcome</th><th>Returned outcome</th>
<th>Safe error category</th></tr></thead><tbody>{_call_rows(calls)}</tbody></table></section>
<section aria-labelledby="workflows"><h2 id="workflows">Recent Workflow observations</h2><table>
<thead><tr><th>Observed</th><th>Run</th><th>Scheduler status</th><th>Actual outcome</th>
<th>Disposition</th><th>Safe error category</th></tr></thead>
<tbody>{_workflow_rows(workflows)}</tbody></table></section>
</body></html>"""


__all__ = ["MAX_HISTORY", "render_health_page"]
