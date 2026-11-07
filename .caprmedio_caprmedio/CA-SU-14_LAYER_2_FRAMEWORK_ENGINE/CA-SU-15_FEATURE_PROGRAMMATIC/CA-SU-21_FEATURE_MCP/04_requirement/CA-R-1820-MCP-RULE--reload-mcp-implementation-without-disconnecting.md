---
atom_id: CA-R-1820
ref_id: CA-R-1820
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
tier: 3
status: Active
version: 9
updated_at: 2026-11-07 04:28:07 +0400
carrier_destination:
  file:
    name: CA-R-1820-MCP-RULE--reload-mcp-implementation-without-disconnecting.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
author: Anatoly Maslennikov
---
# Summary

reload MCP implementation **without** disconnecting

## Scope

server-side hot reload for the Project-local MCP gateway.

automatic file watching **and** operating-system startup hooks are outside this initial capability.

## Claim

When optional hot reload is explicitly enabled, the MCP gateway **must** provide Operator-requested implementation reload while preserving the established transport connection **and** its fixed Project boundary.

Hot reload is disabled by default; normal restart applies code changes in that mode. When enabled, the reload capability has these required outcomes:

- a successful reload makes **`=1`** validated implementation generation available for new calls.
- a failed reload retains the previously serving generation **and** reports the failure.
- an in-flight call retains its admitted generation **until** it finishes; reload does **not** replay, cancel **or** migrate that call.

## Details

- reload **only** changes executable capability availability; it grants **no** new authority **to** mutate Atoms, start Workflows **or** launch workers.

