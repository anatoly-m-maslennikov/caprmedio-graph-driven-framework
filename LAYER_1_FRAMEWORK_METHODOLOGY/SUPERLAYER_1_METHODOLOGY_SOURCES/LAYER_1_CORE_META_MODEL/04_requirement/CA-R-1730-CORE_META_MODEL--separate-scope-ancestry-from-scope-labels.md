---
subjects:
  active: CAPRMEDIO_MODEL <+ Scope Unit
  passive:
  - CAPRMEDIO_MODEL <+ Scope Unit.Path
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  - CAPRMEDIO_MODEL <+ Scope Unit.Label
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 40
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1776
atom_id: CA-R-1730
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Separate scope ancestry from scope labels

## Claim

### Prose Claim


Scope Unit ancestry **and** Scope Unit Labels.


Scope Unit ancestry **must** follow declared Scope Unit parentage. CAPRMEDIO **must not** author or persist a Structural Level property; an optional derived depth or path rendering **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's ancestry, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.
