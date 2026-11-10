---
identity:
  atom_id: CA-M-536
  ref_id: CA-M-536
context:
  container:
    scope_unit: CA-SU-21
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Data Validation
    dependencies: []
  tier: 2
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-536-MCP-DECISION--quarantine-invalid-tool-projections-while-publishing-valid-capabilities.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
relations:
  method_for:
  - CA-R-1110
  DERIVED_FROM:
  - CA-A-057
author: Anatoly Maslennikov
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
---
## Summary

Quarantine invalid Tool projections while publishing valid capabilities

## Claim scope

Apply **when** descriptor validation detects one invalid Tool **or** Workflow binding.

## Claim

### Prose Claim

Procedure:
1. Retain the complete candidate frontier and identify the invalid capability and exact invalid descriptor field.
2. Quarantine that capability, remove any stale projection for it, and emit its explicit diagnostic without repairing, invoking, or reinterpreting it.
3. Publish every independently valid current descriptor in the same generation and retain truthful unavailable-capability evidence for the quarantined descriptor.

Outcome:
MCP never exposes an invalid or stale descriptor as current, and one invalid descriptor does not withdraw an unrelated valid capability.

Failure or stop:
Stop exposure of the invalid capability until its source or ambiguity is resolved. Stop the entire registry only when generator integrity or the common activated descriptor frontier is unresolved.
