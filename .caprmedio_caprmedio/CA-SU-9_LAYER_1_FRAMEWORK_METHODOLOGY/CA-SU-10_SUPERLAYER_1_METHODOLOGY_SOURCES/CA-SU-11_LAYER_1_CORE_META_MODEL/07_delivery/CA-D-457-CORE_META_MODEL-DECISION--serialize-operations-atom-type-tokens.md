---
atom_id: CA-D-457
ref_id: CA-D-457
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations).Header.Context.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations).Header.Context.Form
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow) >{1+} Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step)
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 28
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-D-457-CORE_META_MODEL-DECISION--serialize-operations-atom-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Serialize Operations Atom Type tokens

## Claim

### Prose Claim

An Operations Atom File Carrier serializes its LABEL segment under CA-D-283: use its explicit Label when present, otherwise its Form name, and normalize the token under CA-D-284.

| Operations Atom Form | Fallback token when Label is absent |
|---|---|
| Action | Form token `ACTION` |
| Workflow | Form token `WORKFLOW` |
| Step | Form token `STEP` |
| Scope Delegation, Solution, Direct Policy, Approach Policy, Decision | Effective Label/Form fallback under CA-D-283, normalized under CA-D-284 |

An explicit Label takes precedence for every Form.
