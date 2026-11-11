---
identity:
  id: CA-D-442
  ref_id: CA-D-442@30-draft
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
    dependencies:
    - CAPRMEDIO_MODEL <+ Carrier
  tier: 3
state:
  status: draft
  version: 30
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-D-442@30-draft-CORE_META_MODEL-DECISION--encode-scope-unit-declaration-fields.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/000_draft
---


## Summary

Encode Scope Unit declaration fields

## Claim

### Prose Claim

Carry each Scope Unit’s structural Declaration as a Requirement / Scope Unit Declaration Markdown Atom.

Header.Context.Topics.Main Subject identifies the declared Scope Unit. The Claim carries its declared structural facts in CFEL where expressible.

The shared model supplies field formats and cardinalities. Project inherits its unordered state and absence of order.number. Every Scope Unit has one stable ID. Folder names follow the shared Delivery Policy.
