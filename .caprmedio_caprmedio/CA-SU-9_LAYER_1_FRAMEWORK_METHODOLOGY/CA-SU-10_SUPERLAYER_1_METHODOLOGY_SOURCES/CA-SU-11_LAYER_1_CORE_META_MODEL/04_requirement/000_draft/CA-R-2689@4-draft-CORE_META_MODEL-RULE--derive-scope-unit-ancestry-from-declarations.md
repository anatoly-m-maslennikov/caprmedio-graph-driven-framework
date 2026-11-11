---
identity:
  id: CA-R-2689
  ref_id: CA-R-2689@4-draft
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: rule
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Path
    dependencies:
    - CAPRMEDIO_MODEL <+ Scope Unit
    - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
    - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
  tier: 2
state:
  status: draft
  version: 4
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-R-2689@4-draft-CORE_META_MODEL-RULE--derive-scope-unit-ancestry-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---


## Summary

Derive Scope Unit ancestry from Declarations

## Claim

### Prose Claim

Scope Unit ancestry is derived from the Scope Unit Declarations and their direct parent relations. CAPRMEDIO does not author or persist a Structural Level property for a Scope Unit. A displayed path or depth is derived from that parent chain only. It does not establish or override parentage, ownership, or authority. Conflicting or unresolved parent inputs remain unresolved.
