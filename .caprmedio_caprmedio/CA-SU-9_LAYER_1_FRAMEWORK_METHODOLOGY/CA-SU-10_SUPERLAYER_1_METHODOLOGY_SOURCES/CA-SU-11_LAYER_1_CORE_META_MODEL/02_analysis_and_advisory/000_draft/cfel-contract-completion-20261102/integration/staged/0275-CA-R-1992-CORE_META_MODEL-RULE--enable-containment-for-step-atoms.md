---
atom_id: CA-R-1992
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Operations)/Step
  passive:
  - Atom/(.Role := Operations)/Substep
  - Atom/(.Role := Operations)/Action
  - CFEL <+ Relation//IS_CONTAINED_BY
relations:
  child_of:
  - CA-R-2478
version: 15
updated_at: 2026-11-02 07:49:21 +0400
tier: 3
role: Requirement
form: Rule
---
## Summary

Enable containment for Step Atoms

## Claim scope

the declared Relation whitelist of the Step model kind, including nested Substeps.

## Claim

a Step declaration **must** whitelist the canonical direct `IS_CONTAINED_BY` Relation from a Substep model kind to that Step. It **must not** introduce `Enabled Relations.Contains` as a Property. `CONTAINS` remains the derived inverse declared by CA-R-2478 and **must not** be authored as a second containment fact.

## Details

the Step declaration permits the following exclusive model alternatives:

- one or more Substep model-kind children and no RUN relation to an Action model kind; **or**
- no Substep model-kind child and exactly **`1`** RUN relation to an Action model kind.

the direct containment fact is written once, with `Substep +> Step` denoting the part-to-whole form and `Step <+ Substep` the same fact read whole-to-part. Any written named relation follows `A((R))B` forward or `B<((R))A` reverse, with the count attached to the written end. This rule does not introduce a storage layout, execution protocol, or actual Workflow-instance constraint.
