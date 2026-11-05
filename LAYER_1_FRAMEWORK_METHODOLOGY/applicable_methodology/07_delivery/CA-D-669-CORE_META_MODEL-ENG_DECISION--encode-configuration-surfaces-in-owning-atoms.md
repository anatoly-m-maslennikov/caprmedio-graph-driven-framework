---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Project.Settings
version: 2
updated_at: 2026-11-04 09:30:21 +0400
relations: {}
atom_id: CA-D-669
status: Active
tier: 3
role: Delivery
form: Eng Decision
carrier_destination:
  file:
    name: CA-D-669-CORE_META_MODEL-ENG_DECISION--encode-configuration-surfaces-in-owning-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-669-CORE_META_MODEL-ENG_DECISION--encode-configuration-surfaces-in-owning-atoms.md
  source_atom_id: CA-D-669
  source_atom_revision: 2
  source_sha256: b7d2b918e8462f28c4cd1e011ef96f4f90b798447785638ce6818b7e55f2717c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Encode configuration surfaces in owning Atoms

## Claim

### Prose Claim

An owning Atom may carry its defined machine-readable properties in YAML frontmatter. Its ordinary RMED Claim is a zero-value container with one or both Formal Claim and Prose Claim children, each with zero or one Markdown values. A Formal Claim value contains a CFEL-labelled fence. Frontmatter is not a second Claim or independent source. Project initialization inputs and applicable CAPRMEDIO behavior and configuration choices belong to Project Settings; Scope Unit declarations belong to Scope Unit Declaration Atoms.
