---
identity:
  id: CA-D-666
  ref_id: CA-D-666@4-draft
context:
  container:
    scope_unit: CA-SU-11
  role: delivery
  form: policy
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
    dependencies:
    - CAPRMEDIO_MODEL <+ Carrier
  tier: 3
state:
  status: draft
  version: 4
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-D-666@4-draft-CORE_META_MODEL-POLICY--carry-scope-unit-declarations-as-governing-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/000_draft
---


## Summary

Carry Scope Unit Declarations as Governing Atoms

## Claim

### Prose Claim


Carry each Scope Unit Declaration in a Markdown Atom file. Its Atom is the governing structural source. Carry each Scope Delegation in its own Markdown Atom file as a responsibility source.

Frontmatter carries its Role, Form and active Subject. Claim carries its operative prose, CFEL expressions, or both. `project_structure.toml` is not a governing source.
