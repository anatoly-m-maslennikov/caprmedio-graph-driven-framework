---
atom_id: CA-R-2548
ref_id: CA-R-2548
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2548-CORE_META_MODEL-RULE--deliver-objects-to-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Deliver Objects to Carriers

## Claim

### Prose Claim


- `>>` delivers an Object to the referenced Carrier or Carrier part.
- A selection delivers its selected Objects.
- A bare qualified address refers to its declared target.
- `!(selectors)` excludes those branches from a selection.
- Relative exclusions use the selection's base.
- `=` states an equality condition.
