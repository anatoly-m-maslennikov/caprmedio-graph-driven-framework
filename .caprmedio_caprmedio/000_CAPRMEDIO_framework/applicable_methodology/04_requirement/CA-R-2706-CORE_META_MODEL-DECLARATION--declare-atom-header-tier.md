---
atom_id: CA-R-2706
ref_id: CA-R-2706
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-2706-CORE_META_MODEL-DECLARATION--declare-atom-header-tier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2706-CORE_META_MODEL-DECLARATION--declare-atom-header-tier.md
  source_atom_id: CA-R-2706
  source_atom_revision: 2
  source_sha256: 728d031a666c4b3b78ef6285ea84751847d444c4a773abdc95165e5cd39df177
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Tier

## Claim

### Prose Claim

Atom.Header.Tier stores one integer value and an optional Tier Label; the Formal Claim defines their representation.

### Formal Claim

```CFEL
# model
Atom.Header.Tier{::1}:: [int]{::1};

Atom.Header.Tier.*[in(Label)]{::0..1};

Atom.Header.Tier >= -1
```
