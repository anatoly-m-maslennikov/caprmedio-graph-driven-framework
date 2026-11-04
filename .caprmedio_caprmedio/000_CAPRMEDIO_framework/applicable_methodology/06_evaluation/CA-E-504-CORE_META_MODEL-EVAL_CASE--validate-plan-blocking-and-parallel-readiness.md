---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Done'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
version: 24
updated_at: 2026-11-04 16:52:59 +0400
relations:
  evaluation_for:
  - CA-R-1580
  - CA-R-1583@26
  - CA-R-1592
  - CA-D-471
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-E-504
status: Active
tier: 4
role: Evaluation
form: Eval Case
carrier_destination:
  file:
    name: CA-E-504-CORE_META_MODEL-EVAL_CASE--validate-plan-blocking-and-parallel-readiness.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-504-CORE_META_MODEL-EVAL_CASE--validate-plan-blocking-and-parallel-readiness.md
  source_atom_id: CA-E-504
  source_atom_revision: 24
  source_sha256: b3621864df3860e830f721906e0f05aa63dfaca3a7f19663387e07fb11c1fc83
  original_relations_sha256: e1d38a0e60ccd1d7410beca301283f7adc983f4b266fc7e176a55f3f0df71b50
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
