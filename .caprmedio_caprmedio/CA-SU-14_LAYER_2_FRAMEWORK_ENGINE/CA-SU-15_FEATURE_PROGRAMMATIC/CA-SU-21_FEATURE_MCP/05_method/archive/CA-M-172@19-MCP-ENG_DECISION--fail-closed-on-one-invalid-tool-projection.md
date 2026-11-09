---
atom_id: CA-M-172@19
ref_id: CA-M-172@19
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data
    Validation
tier: 2
relations:
  method_for:
  - CA-R-1110
  derived_from:
  - CA-A-057
status: Archived
version: 19
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-M-172@19-MCP-ENG_DECISION--fail-closed-on-one-invalid-tool-projection.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method/archive
---
# Fail closed on one invalid Tool projection

## Applicable when

Apply **when** descriptor validation detects one invalid Tool **or** Workflow binding.

## Procedure

1. Retain the complete candidate frontier and identify the invalid capability and exact invalid descriptor field.
2. Quarantine that capability, remove any stale projection for it, and emit its explicit diagnostic without repairing, invoking, or reinterpreting it.
3. Publish every independently valid current descriptor in the same generation and retain truthful unavailable-capability evidence for the quarantined descriptor.

## Outcome

MCP never exposes an invalid or stale descriptor as current, and one invalid descriptor does not withdraw an unrelated valid capability.

## Failure or stop

Stop exposure of the invalid capability until its source or ambiguity is resolved. Stop the entire registry only when generator integrity or the common activated descriptor frontier is unresolved.
