---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Carrier/File
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
version: 27
updated_at: 2026-11-03 20:00:05 +0400
atom_id: CA-D-495
ref_id: CA-D-495
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-495-CORE_META_MODEL-DECISION--carry-applicability-in-the-registered-body-sections.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
container:
  scope_unit: CA-SU-11
---
## Summary

Carry applicability in the registered body sections

## Claim

### Prose Claim

Applicability: applicability restrictions of Claims carried by Markdown Atom Carriers.

A Markdown Atom Carrier must carry the Claim's applicability in its registered body content, not as a duplicate frontmatter value. For ordinary RMED, carry textual applicability in Prose Claim together with the qualified contribution; carry formal content in the CFEL fence within Formal Claim and supporting information in Details. Do not maintain a second applicability declaration in Details or frontmatter. For other Roles, retain applicability in their registered primary content; this rule does not change their body-section layouts.

## Details

Applicability identifies what the Claim applies to, including relevant conditions and exclusions. It does not select another structural target, change ownership, or introduce a separate Claim.

