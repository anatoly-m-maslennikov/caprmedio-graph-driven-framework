---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content.Semantics
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Atom.Content
version: 32
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1279
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Govern Every Defined Term

## Claim

### Prose Claim


defined Terms and their canonical direct GOVERNS Subject Relation.


when an Atom's Claim explicitly defines a Term, it **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by that Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim, source use, **and** applicable Atom.Semantics establish that Term's meaning; the other Term components **in** the path are references **to** their own meanings, **not** additional meanings supplied by this Atom.
