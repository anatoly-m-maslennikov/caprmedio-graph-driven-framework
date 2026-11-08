---
atom_id: CA-E-504
ref_id: CA-E-504
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Done'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
tier: 4
relations:
  evaluation_for:
  - CA-R-1580
  - CA-R-1583@26
  - CA-R-1592
  - CA-D-471
status: Active
version: 24
updated_at: 2026-11-04 16:52:59 +0400
carrier_destination:
  file:
    name: CA-E-504-EVAL_CASE--validate-plan-blocking-and-parallel-readiness.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-504-CORE_META_MODEL-EVAL_CASE--validate-plan-blocking-and-parallel-readiness.md
  source_atom_id: CA-E-504
  source_atom_revision: 24
  source_sha256: 9826bf04b9b27c451a40b0e20d909b607d2e2cf2b04ec03c3475182b862268ca
  original_relations_sha256: 16439a02e9b16e78cd3237b12f6c8445cc5504208a38a44ce29a9dad5973c4ed
---
## Summary

Validate Plan blocking and parallel readiness

## Claim

### Prose Claim


Plan blocking **and** parallel readiness.


the blocking Evaluation **must** reject a start **unless** **all** explicit blockers are Done **and** the applicable execution permissions hold.

## Details

- `A BLOCKS B`, `B BLOCKS C`: permit `A`, **then** `B`, **then** `C` **only** **after** the preceding Plan is Done.
- `A BLOCKS C`, `B BLOCKS C`: allow `A` **and** `B` **to** be ready concurrently; `C` waits for both.
- reorder leading navigation numbers **or** give two Plans the same Hub: do **not** invent another blocking edge.
- reject a self-edge, cycle, unresolved **or** non-Plan target, duplicate direct declaration, independently authored `BLOCKS` inverse fact, **or** Plan scheduling encoded as `depends_on`; accept a valid derived `BLOCKS` view from a direct `IS_BLOCKED_BY` fact authored on the dependent Plan.
- accept a Done blocker; Backlog, Active, Canceled, **and** Archived **must not** satisfy its completion gate.
- combine contained-Plan terminal prerequisites (Done **or** Canceled; mixed statuses allowed) with blocking for deadlock detection: **if** containing Plan `H` contains Plan `A` **and** `H BLOCKS A`, reject the unsatisfiable cycle even though the blocking graph alone is acyclic. `IS_CONTAINED_BY`/derived `CONTAINS` does **not** establish `BLOCKS` by itself.
- distinguish readiness from forced execution: a deterministic display order does **not** prohibit concurrent independent work **or** grant execution authority.

report the failing endpoints **and**, for a cycle, its complete prerequisite chain.
