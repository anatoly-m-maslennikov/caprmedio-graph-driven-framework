---
atom_id: CA-R-2355
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation.Name
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2355-CORE_META_MODEL-ENTITY_DEFINITION--define-relation-name.md
  source_atom_id: CA-R-2355
  source_atom_revision: 4
  source_sha256: c06246eb54fb597996273f4cb1dee58c68e2b7f44f2c6997fb179e66ecfb61fe
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Relation Name

## Claim

Relation Name is the canonical name of a reusable Relation Type. The named
Type can connect many endpoint pairs. An actual edge remains the
source/Type/target tuple and does not create a separate Relation ID.


```CFEL
Relation.Name{:1}: [string]{:1};
Relation.Name.*[]{:0}
```

## Details

Source meaning: CA-R-2247. Scope-specific constraints remain in the governing
Relation Declarations.
