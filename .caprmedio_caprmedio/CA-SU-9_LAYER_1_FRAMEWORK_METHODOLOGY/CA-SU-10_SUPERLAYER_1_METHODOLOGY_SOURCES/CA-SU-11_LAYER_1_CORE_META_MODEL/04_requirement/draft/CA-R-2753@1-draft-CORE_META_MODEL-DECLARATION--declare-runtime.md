---
atom_id: CA-R-2753
ref_id: CA-R-2753@1-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ Runtime
version: 1
tier: 3
role: Requirement
form: Declaration
updated_at: 2026-11-05 01:38:59 +0400
carrier_destination:
  file:
    name: CA-R-2753@1-draft-DECLARATION--declare-runtime.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---

## Summary

Declare Runtime

## Claim

### Formal Claim

```CFEL
# model
Runtime ((NARROWER_THAN)) Occurrent;

# instances
Runtime//$runtime {::0+}((EXECUTES)) Execution//$execution
```

## Semantics

A Runtime is an environment in which Executions run.
