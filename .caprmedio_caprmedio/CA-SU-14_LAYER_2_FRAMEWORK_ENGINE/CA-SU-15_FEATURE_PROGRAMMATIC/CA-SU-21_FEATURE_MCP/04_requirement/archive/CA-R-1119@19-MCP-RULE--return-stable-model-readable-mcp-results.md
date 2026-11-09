---
atom_id: CA-R-1119@19
ref_id: CA-R-1119@19
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Result and Status Presentation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface
    Contracts
tier: 1
status: Archived
version: 19
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1119@19-MCP-RULE--return-stable-model-readable-mcp-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
---
## Summary

Return stable model-readable MCP results

## Claim

### Prose Claim

MCP **must** map Tool results, diagnostics, empty results, partial results, **and** failures into stable model-readable protocol responses while preserving their governed meaning **and** provenance. Responses **must** remain usable **without** a user interface, distinguish protocol failure from Tool failure, **and** **must not** expose internal implementation details as part of the public MCP contract.
