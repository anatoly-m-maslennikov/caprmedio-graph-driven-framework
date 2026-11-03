---
atom_id: CA-R-2520
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2520-CORE_META_MODEL-DECLARATION--declare-plan-work-sequence-number.md
  source_atom_id: CA-R-2520
  source_atom_revision: 2
  source_sha256: b034afc0b8c2eb478a65677f3e03360ecc4e9e95d8b4a74a6b3ceb43eb9db527
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom/(.Role := Plan).Work Sequence Number

## Claim

```CFEL
Atom/(.Role: Plan).Work Sequence Number{:0..1}: [int]{:1};
Atom/(.Role: Plan).Work Sequence Number.*[]{:0};
IF (Atom/(.Role: Plan).Work Sequence Number{=1})
THEN (Atom/(.Role: Plan).Work Sequence Number > 0);
UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.atom, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.atom{=1})
);
UNIQUE(
  Atom/(.Role: Plan)//,
  (.Relations.contained_by.scope_unit, .Work Sequence Number),
  (.Status = Active) AND (.Work Sequence Number{=1}) AND (.Relations.contained_by.scope_unit{=1})
)
```
