---
atom_id: CA-E-661
ref_id: CA-E-661@7
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Role
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role :=
    Operations)/(.Header.Form := Step)
  - CAPRMEDIO_MODEL <+ Carrier
tier: 2
relations:
  evaluation_for:
  - CA-R-1531@20
  - CA-R-2511
  - CA-R-2512
  - CA-R-2513
  - CA-R-2514
  - CA-R-2515
  - CA-R-2463
  - CA-R-1018
status: Archived
version: 7
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-E-661@7-CORE_META_MODEL-EVAL_POLICY--validate-tier-zero-content-role-semantics.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/archive
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Validate Tier Zero Content-role semantics

## Claim

### Prose Claim

A Tier `0` Atom fails this Evaluation when its complete Claim’s primary contribution does not match the applicable canonical Role Declaration Semantics. Tier `0` defines the Scope Unit internally; Tier does not change the Atom’s Role or Form. This Evaluation imposes no Role- or Form-specific Tier and does not require every Role in a Scope Unit.
