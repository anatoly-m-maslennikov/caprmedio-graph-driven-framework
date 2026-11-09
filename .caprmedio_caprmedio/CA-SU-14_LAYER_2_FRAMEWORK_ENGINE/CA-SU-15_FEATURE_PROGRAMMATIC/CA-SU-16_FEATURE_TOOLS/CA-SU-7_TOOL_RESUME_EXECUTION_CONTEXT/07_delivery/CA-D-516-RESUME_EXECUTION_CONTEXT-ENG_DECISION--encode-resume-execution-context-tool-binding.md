---
atom_id: CA-D-516
ref_id: CA-D-516
container:
  scope_unit: CA-SU-7
role: Delivery
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Recovery"
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Serialization"
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 14
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-516-RESUME_EXECUTION_CONTEXT-ENG_DECISION--encode-resume-execution-context-tool-binding.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/CA-SU-7_TOOL_RESUME_EXECUTION_CONTEXT/07_delivery
current_scope_unit: RESUME_EXECUTION_CONTEXT
author: Anatoly Maslennikov
---
# Summary

Encode RESUME_EXECUTION_CONTEXT Tool binding

## Scope

the RESUME_EXECUTION_CONTEXT capability for Tool/RESUME_EXECUTION_CONTEXT/Carrier.

## Claim

the RESUME_EXECUTION_CONTEXT Tool binding **must** be carried **in** the following TOML table **in** this Atom's Details, with JSON request **and** response Carriers.

## Details

accept a supported Run ID; return original request, frozen selection and criteria bindings, pending check or fix work, saved handoffs, current-source observations, and recording blockers.

```toml
[tool_binding]
name = "RESUME_EXECUTION_CONTEXT"
entrypoint = "LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/TOOL_RESUME_EXECUTION_CONTEXT/resume_execution_context.py"
action_ids = ["CA-O-116"]
mcp_name = "resume_execution_context"
```

- the MCP boundary exposes the Implementation's strict input schema. unknown fields **and** invalid selectors are explicit errors.
- return repository-relative source paths **and** SHA-256 bindings. full content is loaded **only** **when** requested.
- observation cursors bind the Run ID, saved Event frontier **and** saved status fingerprint; a cursor from another Run is invalid.
