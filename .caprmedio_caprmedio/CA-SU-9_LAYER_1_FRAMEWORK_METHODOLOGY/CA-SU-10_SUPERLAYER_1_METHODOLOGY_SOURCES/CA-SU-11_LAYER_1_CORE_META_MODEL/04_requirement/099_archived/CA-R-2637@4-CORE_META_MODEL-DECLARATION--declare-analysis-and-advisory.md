---
atom_id: CA-R-2637
ref_id: CA-R-2637@4
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis and Advisory")
tier: 3
status: archived
version: 4
updated_at: '2026-11-11T18:56:17+04:00'
carrier_destination:
  file:
    name: CA-R-2637@4-CORE_META_MODEL-DECLARATION--declare-analysis-and-advisory.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Analysis & Advisory

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Context.Role :: "Analysis and Advisory";

Atom/(.Header.Context.Role := "Analysis and Advisory") >| (Role Order Number == 2);
```

## Semantics

Analysis and Advisory covers analysis reports, rationales and spec proposals. It establishes findings, explanations, comparisons, reasons or proposed changes.

For reading historical Atom carriers, `Analysis & Advisory` is an alias for this same Role. New and updated Atom carriers use the canonical Role value `Analysis and Advisory`.
