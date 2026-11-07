---
atom_id: CA-D-669
ref_id: CA-D-669
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Project.Settings
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 09:30:21 +0400
carrier_destination:
  file:
    name: CA-D-669-CORE_META_MODEL-ENG_DECISION--encode-configuration-surfaces-in-owning-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Encode configuration surfaces in owning Atoms

## Claim

### Prose Claim

An owning Atom may carry its defined machine-readable properties in YAML frontmatter. Its ordinary RMED Claim is a zero-value container with one or both Formal Claim and Prose Claim children, each with zero or one Markdown values. A Formal Claim value contains a CFEL-labelled fence. Frontmatter is not a second Claim or independent source. Project initialization inputs and applicable CAPRMEDIO behavior and configuration choices belong to Project Settings; Scope Unit declarations belong to Scope Unit Declaration Atoms.
