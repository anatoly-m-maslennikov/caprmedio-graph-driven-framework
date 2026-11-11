---
atom_id: CA-R-1686
ref_id: CA-R-1686
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations
tier: 3
relations:
  child_of:
  - CA-M-447
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1686-CORE_META_MODEL-RULE--propagate-caprmedio-change-forward.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1686-CORE_META_MODEL-RULE--propagate-caprmedio-change-forward.md
  source_atom_id: CA-R-1686
  source_atom_revision: 33
  source_sha256: 9523e5d1916b1d20310669469ec6cd7be9743321fda7eeade785423f06ee7ffe
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
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
