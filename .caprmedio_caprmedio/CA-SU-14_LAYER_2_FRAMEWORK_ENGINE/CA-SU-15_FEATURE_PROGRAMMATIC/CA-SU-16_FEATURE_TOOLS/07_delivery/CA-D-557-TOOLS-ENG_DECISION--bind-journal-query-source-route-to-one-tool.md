---
atom_id: CA-D-557
ref_id: CA-D-557
container:
  scope_unit: CA-SU-16
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool
tier: 4
relations:
  delivery_for:
  - CA-R-1872
status: Active
version: 14
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-557-TOOLS-ENG_DECISION--bind-journal-query-source-route-to-one-tool.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/07_delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
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
entrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/find_and_fetch_journal_events.py"
action_ids = ["CA-O-162"]
workflow_ids = ["CA-O-161"]
mcp_name = "find_and_fetch_journal_events"
```

This discovery binding identifies the existing read-only Tool and its existing
MCP route. MCP and orchestrator registration remain separate delivery work;
the binding creates no Workflow, Action, Run, or Journal.
