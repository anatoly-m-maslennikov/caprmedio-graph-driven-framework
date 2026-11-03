---
atom_id: CA-R-2511
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2511-CORE_META_MODEL-DECLARATION--declare-plan.md
  source_atom_id: CA-R-2511
  source_atom_revision: 2
  source_sha256: 1174658161330991919f8306661b1faf5b18ea0a611fc0fb0792d6ada2eae8e3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Role := Plan)

## Claim

```CFEL
Atom/(.Role: Plan);
IF ((Atom/(.Role: Plan).Status = Active) AND (Atom/(.Role: Plan).Work Sequence Number{=1}))
THEN (Atom/(.Role: Plan).Relations.contained_by{==1})
```

## Semantics

A Plan describes bounded intended work or an intended outcome.
