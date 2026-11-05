---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL
version: 36
updated_at: 2026-11-05 14:25:52 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-R-1358
status: Draft
tier: 3
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-1358@36-draft-CORE_META_MODEL-RULE--consolidate-single-value-claims-as-one-value-set-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Claim

### Prose Claim


multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.


multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
