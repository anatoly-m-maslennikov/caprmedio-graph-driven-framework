---
atom_id: CA-R-1110
ref_id: CA-R-1110
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data
    Validation
tier: 1
relations:
  IS_REPLACEMENT_FOR:
  - CA-M-172
status: Active
version: 22
updated_at: 2026-11-09 21:15:45 +0400
author: Anatoly Maslennikov
current_scope_unit: MCP
destination:
  file:
    name: CA-R-1110-MCP-RULE--fail-closed-on-invalid-tool-projections.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
---

## Summary

Fail closed on invalid Tool projections

## Claim

### Prose Claim

MCP **must** fail closed for each invalid Tool **or** Workflow descriptor. A missing contract field, name collision, invalid canonical-model-derived schema, unresolved binding, **or** ambiguous capability identity **must** make only that capability unavailable with explicit diagnostics. MCP **must not** expose the invalid capability, retain its stale projection as current, **or** reinterpret it as another capability.

MCP **must** publish the complete set of independently valid current descriptors despite an unrelated invalid descriptor. One quarantined capability **must not** disable, withdraw, **or** misrepresent an unrelated valid Tool **or** Workflow binding. Registry output **must** identify each unavailable capability and its attributable diagnostic without claiming that client refresh has occurred.

## Details

Retain the complete candidate frontier and identify the invalid capability and exact field. Quarantine it, remove its stale projection, emit its diagnostic without repairing, invoking, or reinterpreting it, and publish independently valid descriptors in the same generation. Stop the whole registry only when generator integrity or the common activated descriptor frontier is unresolved.
