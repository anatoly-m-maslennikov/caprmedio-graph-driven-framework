---
atom_id: CA-R-2749
ref_id: CA-R-2749@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ Execution
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 01:38:59 +0400
carrier_destination:
  file:
    name: CA-R-2749@1-draft-DECLARATION--declare-execution.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---

## Summary

Declare Execution

## Claim

### Formal Claim

```CFEL
# model
Execution ((NARROWER_THAN)) Occurrent;

# instances
Execution//$execution {::1+}((IS_EXECUTED_BY)) Runtime//$runtime;

Execution//$producer {::0+}((PRODUCES)) Event//$event
```

## Semantics

An Execution is the actual performance of work.
