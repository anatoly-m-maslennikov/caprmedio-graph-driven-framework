---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Status: Done'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Work Sequence Number'
version: 18
updated_at: 2026-10-26 17:47:19 +0400
relations:
  evaluation_for:
  - CA-R-1580
  - CA-R-1583
  - CA-R-1592
  - CA-D-471
atom_id: CA-E-504@18
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 4
---
# Summary

Validate Plan blocking and parallel readiness

## Scope

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
