---
atom_id: CA-R-2565
ref_id: CA-R-2565
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2565-CORE_META_MODEL-RULE--preserve-atom-version-and-updated-at-when-archiving.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Preserve Atom Version and Updated At When Archiving

## Claim

### Prose Claim


When a Workflow archives an Atom:

1. Keep Atom.Header.Version unchanged.
2. Keep Atom.Header.Updated At unchanged.
3. Do not create a new Atom Version solely for archiving.
