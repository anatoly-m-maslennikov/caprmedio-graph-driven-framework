---
atom_id: CA-D-557@5
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: FIND_AND_FETCH_JOURNAL_EVENTS/source binding
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Tool
  - Implementation
relations:
  delivery_for:
  - CA-R-1872
type: Eng Decision
tier: 3
---
# Summary

Bind Journal query source route to one Tool

## Scope

The one-route binding.

## Claim

The delivered Journal query Tool **must** bind CA-O-161, CA-O-163, and CA-O-162 as one route without defining a second Workflow, Action, or Journal.

## Details

```toml
[tool_binding]
name = "FIND_AND_FETCH_JOURNAL_EVENTS"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/find_and_fetch_journal_events.py"
action_ids = ["CA-O-162"]
workflow_ids = ["CA-O-161"]
mcp_name = "find_and_fetch_journal_events"
```

This discovery binding identifies the existing read-only Tool and its existing
MCP route. MCP and orchestrator registration remain separate delivery work;
the binding creates no Workflow, Action, Run, or Journal.
