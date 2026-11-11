---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Relations
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1686
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1686-CORE_META_MODEL-RULE--propagate-caprmedio-change-forward.md
  source_atom_id: CA-R-1686
  source_atom_revision: 33
  source_sha256: 4bd8b1c1dec1841b6b7953359293c1da2c755e2de96ad3694d6ae17db48604b5
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Propagate CAPRMEDIO change forward

## Claim scope

an accepted upstream change in the ordered layer graph.

## Claim

the change propagates **only** forward through the ordered layer graph. it:

1. identifies affected downstream Projections, Methods, Evaluation criteria, Delivery rules, Implementations, **and** Operations consumers;
2. marks **every** affected downstream artifact potentially stale **without** mutating historical atoms;
3. routes required reconciliation **to** the artifact's owning layer; **and**
4. closes **only** **when** **every** affected currentness **or** evaluation gate reaches its required disposition.

## Details

refreshing a Projection alone does **not** complete propagation. downstream Method, Evaluation, Delivery, Implementation, **and** Operations remain independently accountable. Feedback from a later layer **may** create a new upstream Concern, but cannot rewrite upstream authority **or** introduce a backward dependency.
