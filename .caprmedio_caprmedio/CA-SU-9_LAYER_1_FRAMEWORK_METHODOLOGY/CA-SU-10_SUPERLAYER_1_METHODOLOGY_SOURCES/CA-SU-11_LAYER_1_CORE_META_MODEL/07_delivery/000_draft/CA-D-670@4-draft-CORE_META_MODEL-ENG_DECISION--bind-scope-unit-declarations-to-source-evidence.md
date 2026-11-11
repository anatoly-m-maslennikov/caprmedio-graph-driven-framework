---
identity:
  id: CA-D-670
  ref_id: CA-D-670@4-draft
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: eng_decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
    dependencies:
    - Entity/Object/Continuant/History
    - CAPRMEDIO_MODEL <+ Journal
    - CAPRMEDIO_MODEL <+ Carrier
  tier: 3
state:
  status: draft
  version: 4
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-D-670@4-draft-CORE_META_MODEL-ENG_DECISION--bind-scope-unit-declarations-to-source-evidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/000_draft
---


## Summary

Bind Scope Unit Declarations to source evidence

## Claim

### Prose Claim

A Scope Unit structural source binding identifies the exact Current Scope Unit Declaration bytes by SHA-256 digest. Readers determine current structure from those bytes. Bind each Scope Delegation separately to its own Current bytes for responsibility evidence. Journal events record history and do not determine whether the current structural Atom is readable.
