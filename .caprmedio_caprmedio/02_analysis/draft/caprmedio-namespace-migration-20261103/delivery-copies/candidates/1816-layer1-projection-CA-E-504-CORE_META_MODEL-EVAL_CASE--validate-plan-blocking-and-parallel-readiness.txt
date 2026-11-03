---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status: Done'
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan).Work Sequence Number
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1580
  - CA-R-1583@26
  - CA-R-1592
  - CA-D-471
atom_id: CA-E-504
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-504-CORE_META_MODEL-EVAL_CASE--validate-plan-blocking-and-parallel-readiness.md
  source_atom_id: CA-E-504
  source_atom_revision: 22
  source_sha256: 8b1cb7a74dbed09855407875b5434ddf731a9da38327981410034461647a1cf8
  original_relations_sha256: 16439a02e9b16e78cd3237b12f6c8445cc5504208a38a44ce29a9dad5973c4ed
---
## Summary

Validate Plan blocking and parallel readiness

## Claim scope

Plan blocking **and** parallel readiness.

## Claim

the blocking Evaluation **must** reject a start **unless** **all** explicit blockers are Done **and** the applicable execution permissions hold.

## Details

- `A BLOCKS B`, `B BLOCKS C`: permit `A`, **then** `B`, **then** `C` **only** **after** the preceding Plan is Done.
- `A BLOCKS C`, `B BLOCKS C`: allow `A` **and** `B` **to** be ready concurrently; `C` waits for both.
- reorder leading navigation numbers **or** give two Plans the same Hub: do **not** invent another blocking edge.
- reject a self-edge, cycle, unresolved **or** non-Plan target, duplicate direct declaration, inverse declaration, **or** Plan scheduling encoded as `depends_on`.
- accept a Done blocker; Backlog, Active, Canceled, **and** Archived **must not** satisfy its completion gate.
- combine contained-Plan terminal prerequisites (Done **or** Canceled; mixed statuses allowed) with blocking for deadlock detection: **if** containing Plan `H` contains Plan `A` **and** `H BLOCKS A`, reject the unsatisfiable cycle even though the blocking graph alone is acyclic. `IS_CONTAINED_BY`/derived `CONTAINS` does **not** establish `BLOCKS` by itself.
- distinguish readiness from forced execution: a deterministic display order does **not** prohibit concurrent independent work **or** grant execution authority.

report the failing endpoints **and**, for a cycle, its complete prerequisite chain.
