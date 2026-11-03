---
atom_id: CA-R-2505@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier.Label
version: 3
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
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
