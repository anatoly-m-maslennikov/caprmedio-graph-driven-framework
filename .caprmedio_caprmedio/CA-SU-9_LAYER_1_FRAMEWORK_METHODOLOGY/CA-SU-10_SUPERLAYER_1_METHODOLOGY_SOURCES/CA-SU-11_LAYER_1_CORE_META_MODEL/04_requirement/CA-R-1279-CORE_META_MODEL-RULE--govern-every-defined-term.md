---
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content.Semantics
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Atom.Content
version: 32
updated_at: 2026-11-02 00:18:22 +0400
atom_id: CA-R-1279
ref_id: CA-R-1279
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Govern Every Defined Term

## Claim

### Prose Claim


defined Terms and their canonical direct GOVERNS Subject Relation.


when an Atom's Claim explicitly defines a Term, it **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by that Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim, source use, **and** applicable Atom.Semantics establish that Term's meaning; the other Term components **in** the path are references **to** their own meanings, **not** additional meanings supplied by this Atom.
