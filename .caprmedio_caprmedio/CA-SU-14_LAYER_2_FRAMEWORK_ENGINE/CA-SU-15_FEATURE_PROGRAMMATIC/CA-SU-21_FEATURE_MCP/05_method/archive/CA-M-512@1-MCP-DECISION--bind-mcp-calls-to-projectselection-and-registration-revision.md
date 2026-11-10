---
atom_id: CA-M-512
ref_id: CA-M-512@1
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source
    Selection
tier: 2
relations:
  method_for:
  - CA-R-1115
  derived_from:
  - CA-A-057
  IS_REPLACEMENT_FOR:
  - CA-M-177
status: Archived
version: 1
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-512@1-MCP-DECISION--bind-mcp-calls-to-projectselection-and-registration-revision.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---

## Summary


Bind MCP calls to ProjectSelection and registration revision

## Claim

### Prose Claim

Resolve one explicit ProjectSelection and the current generated registration revision for each MCP call. Preserve the native request and result, carry the trusted Project root only at the outer schema root, and retain enough provenance to attribute the operation. Reject foreign roots, unresolved bindings and stale registration before invocation; operation-specific source checks remain at the operation boundary.
