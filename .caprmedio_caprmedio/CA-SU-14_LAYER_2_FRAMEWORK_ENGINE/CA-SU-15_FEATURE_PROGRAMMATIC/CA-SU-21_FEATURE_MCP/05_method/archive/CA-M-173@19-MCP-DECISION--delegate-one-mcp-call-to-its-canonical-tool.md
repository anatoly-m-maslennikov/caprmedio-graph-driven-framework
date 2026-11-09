---
atom_id: CA-M-173@19
ref_id: CA-M-173@19
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
tier: 2
relations:
  method_for:
  - CA-R-1111
  derived_from:
  - CA-A-057
status: Archived
version: 19
updated_at: 2026-11-09 07:45:15 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-173@19-MCP-DECISION--delegate-one-mcp-call-to-its-canonical-tool.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---

## Summary

Delegate one MCP call to its canonical Tool

## Claim

### Prose Claim

#### Applicable when

Apply **when** MCP receives one validated request for an exposed Tool.

#### Procedure

1. Select the canonical Tool executable from the current registry.
2. Forward the admitted request **without** reimplementing target resolution, project meaning, validation, mutation, recovery, **or** lifecycle semantics.
3. Transport the Tool result as a Tool result, retaining **every** failure **and** side-effect boundary.

#### Outcome

MCP is a transport boundary **and** the canonical Tool remains the sole operation owner.

#### Failure or stop

Stop **when** canonical selection, request validation, **or** delegated execution fails; do **not** substitute MCP behavior.
