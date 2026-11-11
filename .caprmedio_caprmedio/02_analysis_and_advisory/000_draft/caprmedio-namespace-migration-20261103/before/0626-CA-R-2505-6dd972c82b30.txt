---
atom_id: CA-R-2505
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom.Tier.Label
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Tier.Label

## Claim

```CFEL
Atom.Tier.Label{:0..1}: [string]{:1};
Atom.Tier.Label.*[]{:0};
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 0)) THEN (Atom.Tier.Label == Scope Contract);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 1)) THEN (Atom.Tier.Label == Core);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 2)) THEN (Atom.Tier.Label == General);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 3)) THEN (Atom.Tier.Label == Standard);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 4)) THEN (Atom.Tier.Label == Detail)
```
