---
atom_id: CA-R-2355
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation.Name
version: 5
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2355-CORE_META_MODEL-ENTITY_DEFINITION--define-relation-name.md
  source_atom_id: CA-R-2355
  source_atom_revision: 5
  source_sha256: e1e4f4ed28a5c8a98c421306e3d7211875d49d7e59dd46897d9d9a872fe3f354
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Relation Name

## Claim

### Formal Claim

```CFEL
# model
Relation.Name{:1}: [string]{:1};

Relation.Name.*[]{:0}
```

### Prose Claim


Relation Name is the canonical name of a reusable Relation Type. The named
Type can connect many endpoint pairs. An actual edge remains the
source/Type/target tuple and does not create a separate Relation ID.



