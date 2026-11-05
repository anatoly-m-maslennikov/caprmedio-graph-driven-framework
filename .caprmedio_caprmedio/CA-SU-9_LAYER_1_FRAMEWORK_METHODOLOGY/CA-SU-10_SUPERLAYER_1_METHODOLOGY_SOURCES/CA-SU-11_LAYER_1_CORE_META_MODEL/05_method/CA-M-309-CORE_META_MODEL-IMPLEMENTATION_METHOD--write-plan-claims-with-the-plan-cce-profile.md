---
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Definition of Done'
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Authoring <+ Controlled English
version: 23
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-307
  depends_on:
  - CA-M-306
atom_id: CA-M-309
ref_id: CA-M-309
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Method
form: Implementation Method
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-M-309-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-plan-claims-with-the-plan-cce-profile.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
---
## Summary

Write Plan Claims with the Plan CCE Profile

## Claim

### Prose Claim


Plan Claims written with the Plan CCE Role Profile.


**to** write a Plan Claim with the Plan CCE Role Profile, the Author **must** perform **all** of:

1. state the Plan's primary contribution as intended work, an intended outcome, **or** their governed composition under CA-M-306-CORE_META_MODEL-GENERAL-METHOD--author-plan-atoms.
2. **if** the Plan has own work, identify the action, its object, intended result, Assignee, **and** applicable boundary explicitly. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** qualify that intended work.
3. **if** the Plan is supported **only** by decomposition, state its intended outcome **without** inventing own work.
4. keep reusable procedure authority, normative product boundaries, current realization facts, **and** reusable operational behavior outside the Plan's primary contribution.
5. write the Definition of Done as the subordinate falsifying Condition Expression under CA-M-123-CORE_META_MODEL-IMPLEMENTATION_METHOD--write-definitions-of-done. condition, temporal, quantification, logical, predicate, restriction, **and** comparison Operators **may** occur **in** that slot **only** to determine whether the Plan remains **not** Done.
6. keep optional Details subordinate **to** the same intended work **or** outcome; Details **must not** introduce another intended outcome **or** a second Definition of Done.

## Details

an action word **in** a Plan identifies intended work. it does **not** define a reusable Operations Action.
