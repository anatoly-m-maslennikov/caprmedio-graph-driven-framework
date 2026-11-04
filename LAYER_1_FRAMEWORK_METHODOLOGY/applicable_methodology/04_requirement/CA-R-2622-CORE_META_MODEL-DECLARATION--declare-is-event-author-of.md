---
atom_id: CA-R-2622
role: Requirement
form: Declaration
status: Active
version: 2
updated_at: 2026-11-03 20:00:05 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_EVENT_AUTHOR_OF
relations: {}
carrier_destination:
  file:
    name: CA-R-2622-CORE_META_MODEL-DECLARATION--declare-is-event-author-of.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2622-CORE_META_MODEL-DECLARATION--declare-is-event-author-of.md
  source_atom_id: CA-R-2622
  source_atom_revision: 2
  source_sha256: ccad12aa39c516e384ebd4ae9ee64eb7d4fe772548a0efa42609164774503eea
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare IS_EVENT_AUTHOR_OF

## Claim

### Formal Claim

```CFEL
# model
Relation//IS_EVENT_AUTHOR_OF <((HAS_INVERSE)) Relation//HAS_EVENT_AUTHOR
```
