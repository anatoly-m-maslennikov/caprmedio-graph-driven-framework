---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1686
ref_id: CA-R-1686
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-1686-CORE_META_MODEL-RULE--propagate-caprmedio-change-forward.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Propagate CAPRMEDIO change forward

## Claim

### Prose Claim


an accepted upstream change in the ordered layer graph.


the change propagates **only** forward through the ordered layer graph. it:

1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Operations consumers;
2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
3. routes required reconciliation **to** the artifact's owning layer; **and**
4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.

## Details

refreshing a Projection alone does **not** complete propagation. downstream Method, Evaluation, Delivery, Implementation, **and** Operations remain independently accountable. Feedback from a later layer **may** create a new upstream Concern, but cannot rewrite upstream authority **or** introduce a backward dependency.
