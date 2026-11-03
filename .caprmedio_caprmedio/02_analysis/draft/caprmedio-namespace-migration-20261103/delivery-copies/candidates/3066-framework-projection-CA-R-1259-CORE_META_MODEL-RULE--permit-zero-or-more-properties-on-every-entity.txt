---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Property
  - CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_PROPERTY
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
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1259-CORE_META_MODEL-RULE--permit-zero-or-more-properties-on-every-entity.md
  source_atom_id: CA-R-1259
  source_atom_revision: 24
  source_sha256: abfe5955d5743858661b55eb6d5175b93614ab5cfecf7bf44213979e18644178
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Permit Zero or More Properties on Every Entity

## Claim scope

Property occurrences borne by every Entity.

## Claim

**every** Entity **may** bear **`>=0`** Property occurrences.

### Formal claim

```text
Entity {0+}((HAS_PROPERTY)){1} Property
```
