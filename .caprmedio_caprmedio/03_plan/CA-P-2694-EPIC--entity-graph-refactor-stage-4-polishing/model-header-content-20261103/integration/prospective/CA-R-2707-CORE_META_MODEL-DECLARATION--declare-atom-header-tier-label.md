---
atom_id: CA-R-2707
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier.Label
version: 1
relations: {}
tier: 3
updated_at: 2026-11-03 20:00:05 +0400
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2707-CORE_META_MODEL-DECLARATION--declare-atom-header-tier-label.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom.Header.Tier.Label

## Claim

### Formal Claim

```CFEL
Atom.Header.Tier.Label{:0..1}: [string]{:1};
Atom.Header.Tier.Label.*[]{:0};
IF ((Atom.Header.Tier.Label{=1}) AND (Atom.Header.Tier = 0)) THEN (Atom.Header.Tier.Label == Scope Contract);
IF ((Atom.Header.Tier.Label{=1}) AND (Atom.Header.Tier = 1)) THEN (Atom.Header.Tier.Label == Core);
IF ((Atom.Header.Tier.Label{=1}) AND (Atom.Header.Tier = 2)) THEN (Atom.Header.Tier.Label == General);
IF ((Atom.Header.Tier.Label{=1}) AND (Atom.Header.Tier = 3)) THEN (Atom.Header.Tier.Label == Standard);
IF ((Atom.Header.Tier.Label{=1}) AND (Atom.Header.Tier = 4)) THEN (Atom.Header.Tier.Label == Detail)
```
