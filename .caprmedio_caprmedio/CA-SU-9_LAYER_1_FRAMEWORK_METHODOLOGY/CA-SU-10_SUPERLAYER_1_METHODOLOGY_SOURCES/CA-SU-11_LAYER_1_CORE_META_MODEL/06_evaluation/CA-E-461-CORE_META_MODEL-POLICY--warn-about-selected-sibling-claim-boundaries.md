---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
version: 28
updated_at: 2026-11-02 00:18:22 +0400
atom_id: CA-E-461
ref_id: CA-E-461
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Evaluation
form: Eval Policy
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-E-461-CORE_META_MODEL-EVAL_POLICY--warn-about-selected-sibling-claim-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
---
## Summary

Warn About Selected-sibling Claim Boundaries

## Claim

### Prose Claim


an Atom Claim concerning **only** selected sibling Scope Units.


**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.
