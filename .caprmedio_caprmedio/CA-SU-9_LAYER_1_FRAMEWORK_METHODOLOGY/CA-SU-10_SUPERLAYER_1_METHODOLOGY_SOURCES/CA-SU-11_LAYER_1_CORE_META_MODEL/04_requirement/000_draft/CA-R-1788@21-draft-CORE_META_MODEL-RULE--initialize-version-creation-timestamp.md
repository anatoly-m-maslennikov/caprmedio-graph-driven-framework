---
atom_id: CA-R-1788
ref_id: CA-R-1788@21-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Updated At
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-R-1416
status: draft
version: 21
updated_at: '2026-11-13T07:31:04.146015+00:00'
carrier_destination:
  file:
    name: CA-R-1788@21-draft-CORE_META_MODEL-RULE--initialize-version-creation-timestamp.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
claim_target_scope_unit: CORE_META_MODEL
current_scope_unit: CORE_META_MODEL
---
## Summary

Initialize Version creation timestamp

## Claim

### Prose Claim

Initialize Updated At to the actual Project-time creation instant when a new Atom Version is created. Accepted business updates, including promotion, use the latest happened_at of the applicable accepted create and update Event Records under CA-R-2567 and the Updated At Declaration. Archival, no-ops and Carrier-only changes preserve Updated At. An ancestor-only move preserves a descendant's Updated At. Timestamp encoding follows CA-D-270.
