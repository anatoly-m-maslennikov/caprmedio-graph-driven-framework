---
atom_id: CA-R-1117@20
ref_id: CA-R-1117@20
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution
    Control/Resource Limits
tier: 1
status: Archived
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1117@20-MCP-RULE--bound-and-control-mcp-requests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---
## Summary

Bound and control MCP requests

## Claim

### Prose Claim

MCP **must** validate **every** admitted protocol message **before** dispatch, apply declared time **and** resource bounds, support cancellation **without** corrupting Tool **or** project state, **and** expose progress for admitted long-running operations. Invalid, expired, cancelled, **or** resource-exhausted requests **must** terminate with explicit structured outcomes **and** **must not** leave an ungoverned background operation.
