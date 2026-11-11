---
atom_id: CA-E-661
ref_id: CA-E-661
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Tier
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role:=Operations)/Workflow
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role :=
    Operations)/(.Header.Context.Form := Step)
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
status: Active
version: 8
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-E-661-CORE_META_MODEL-EVAL_POLICY--validate-tier-zero-content-role-semantics.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Validate Tier Zero Content-role semantics

## Claim

### Prose Claim

A Tier `0` Atom fails this Evaluation when its complete Claim’s primary contribution does not match the applicable canonical Role Declaration Semantics. Tier `0` defines the Scope Unit internally; Tier does not change the Atom’s Role or Form. This Evaluation imposes no Role- or Form-specific Tier and does not require every Role in a Scope Unit.
