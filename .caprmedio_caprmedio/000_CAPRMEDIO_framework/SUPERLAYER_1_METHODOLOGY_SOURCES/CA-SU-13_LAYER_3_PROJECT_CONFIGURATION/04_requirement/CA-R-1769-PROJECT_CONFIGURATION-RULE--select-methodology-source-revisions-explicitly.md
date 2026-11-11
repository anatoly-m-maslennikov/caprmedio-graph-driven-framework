---
atom_id: CA-R-1769
ref_id: CA-R-1769
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Selection"
tier: 2
relations:
  child_of:
  - CA-R-686
  depends_on:
  - CA-R-1502
  - CA-R-1698
status: Active
version: 36
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1769-PROJECT_CONFIGURATION-RULE--select-methodology-source-revisions-explicitly.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Select Methodology Source revisions explicitly

## Claim

### Prose Claim


Methodology Source updates or downgrades applied by a Project.


a Project **must** apply a Methodology Source update **or** downgrade **only** by selecting an identified source revision **and** reconciling affected Project authority; the selection **must not** silently rewrite other Methodology Sources **or** Project-owned Atoms.
