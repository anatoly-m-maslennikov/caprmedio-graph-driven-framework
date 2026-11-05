---
atom_id: CA-R-2530
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit.Path
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2530-CORE_META_MODEL-DECLARATION--declare-scope-unit-path.md
  source_atom_id: CA-R-2530
  source_atom_revision: 2
  source_sha256: 9abd4823d07e60b55d674823274fef480205f39e0eb5e193ac30d06c4f59a075
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Scope Unit Path

## Claim

### Formal Claim

```CFEL
# model
Scope Unit.Path{:1}: [string]{:1+};

Scope Unit.Path.*[]{:0}
```

### Prose Claim


The Path lists Scope Unit identities along the complete declared containment chain from the root to the addressed Scope Unit.

