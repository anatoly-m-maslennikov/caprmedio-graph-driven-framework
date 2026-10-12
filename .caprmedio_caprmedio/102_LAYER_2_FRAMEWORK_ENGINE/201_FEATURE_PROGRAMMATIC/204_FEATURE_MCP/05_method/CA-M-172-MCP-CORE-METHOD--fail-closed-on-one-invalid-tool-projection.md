---
cce_version: cce_1
cce_form: method
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
version: 6
updated_at: 2026-10-11 01:09:00 +0400
relations:
  method_for:
    - CA-R-1110
  derived_from:
    - CA-A-057
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
