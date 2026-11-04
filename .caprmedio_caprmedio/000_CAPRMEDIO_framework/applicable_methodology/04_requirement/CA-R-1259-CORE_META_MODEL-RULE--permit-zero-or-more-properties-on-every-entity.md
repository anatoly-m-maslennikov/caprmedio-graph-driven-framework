---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_PROPERTY
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1259
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1259-CORE_META_MODEL-RULE--permit-zero-or-more-properties-on-every-entity.md
  source_atom_id: CA-R-1259
  source_atom_revision: 24
  source_sha256: 55d09143de8f3e5fdbfbdfed181eae80dc0da051993cd34bb2567019a52e4707
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Permit Zero or More Properties on Every Entity

## Claim

### Prose Claim


Property occurrences borne by every Entity.


**every** Entity **may** bear **`>=0`** Property occurrences.


```text
Entity {:0+}((HAS_PROPERTY)){:1} Property
```
