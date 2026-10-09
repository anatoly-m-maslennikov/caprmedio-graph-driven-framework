---
atom_id: CA-P-1922
content_role: Plan
type: Plan
label: Task
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 1
updated_at: "2026-10-10 02:10:14 +0400"
relations:
  is_decomposition_of: [CA-P-1906]
---
# Summary

Verify the Core grouping and relation design

## Objective

Independently verify the joined candidate design, complete ledger and both RMED views before the next top-level review Task.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1921. Independently check hashes, source spans and partition coverage, every original node/occurrence/segment, qualified endpoint rewrites, graph ownership, unresolved dispositions, additional Carrier evidence, both RMED views and all no-source-change boundaries. Verify aliases/inverse views do not duplicate native facts. Record PASS or exact failures in `design.acceptance.md` under `.caprmedio_caprmedio/_projection/core-entity-review/design/`. A failed or incomplete check is not acceptance. Do not adopt candidate semantics or write authoritative sources.

Read current Core Main Content and verify exact source pins before proposing meaning. Earlier classification caches are preparation only. Below 90% confidence, leave a proposal unresolved, state the missing evidence and put the question to the Operator before deciding. A diagnostic or proposed view is not native admission. Preserve all qualified identities and do not infer Entity facts from source Atom metadata or Subject incidence. Work locally without MCP or FPF; do not change Core Atoms, Subjects, history, baseline outputs, implementation, runtime or unrelated work.

### Definition of Done

the Plan is **not** Done **if** ((any required independent check is failed, stale or unverified **or** evidence is only a worker completion claim **or** a source change or omitted identity is unreported) **or** (a required start prerequisite is **not** Done) **or** (the stated output or handoff is missing) **or** (uncertainty below 90% is silently decided or its question is not put to the Operator) **or** (source pins or checks are stale) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
