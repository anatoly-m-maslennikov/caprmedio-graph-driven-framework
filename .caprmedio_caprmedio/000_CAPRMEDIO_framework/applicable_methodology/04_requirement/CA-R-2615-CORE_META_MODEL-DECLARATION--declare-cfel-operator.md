---
atom_id: CA-R-2615
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL<+Operator//SubjectValueSelection
version: 1
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2615-CORE_META_MODEL-DECLARATION--declare-cfel-operator.md
  source_atom_id: CA-R-2615
  source_atom_revision: 1
  source_sha256: 31da9c3927f1e8bd2bfab42511c7b80fcffd3547022ef5a18bdd3984dc0259ef
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare CFEL operator :=

## Claim

### Formal Claim

```CFEL
# model
Operator//SubjectValueSelection == ":="
```

## Semantics

In a Subject or a filtered Node expression in a Formal Claim, combine an admitted Property value with selection; for example, `Workflow/(.Purpose := Runtime)`. It is not assignment.
