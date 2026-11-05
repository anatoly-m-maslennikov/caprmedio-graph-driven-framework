---
atom_id: CA-R-2706
ref_id: CA-R-2706
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 2
tier: 3
updated_at: 2026-11-04 09:19:08 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2706-CORE_META_MODEL-DECLARATION--declare-atom-header-tier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
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
