---
atom_id: CA-P-1929
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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
updated_at: "2026-10-10 03:21:47 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1937]
---
# Summary

Review first Core node disposition batch

## Objective

Review the assigned candidate nodes for duplication, redundancy, emptiness, distinct meaning and generalization without adopting or deleting them.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1906. Each required prerequisite explicitly BLOCKS this Task.

Review only batch 1: 80 exact identities from `nodes.batch-1.input.json` in the durable node-review inputs. Read the shared `contract.md`, pinned baseline, source Main Content, Substance decision record and newer Scope-omission decision. Record all five checks and a source-backed disposition for each assigned identity; preserve qualified names and all uncertainty. Output `nodes.batch-1.review.json` with exact input and evidence pins. Repeated labels and bare or support-only Subject nodes require actual meaning review, not default drops or fabricated parentage.

Inputs are under `.caprmedio_caprmedio/_projection/core-entity-review/nodes/`; the complete baseline and design remain under its parent review directory. The Scope-omission decision SHA-256 is `d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453`. Scope may be omitted only for full Subject AND full owning Scope Unit; omission retains that resolved default. New names and rules are Operator-backed candidate direction, not retroactive Core evidence or migration approval.

Exclusive scope: assigned derived review output and temporary helper only; root owns Plans, integration receipts and Git. You are not alone; preserve other work. No Core, Subjects, baseline, history, schema, implementation, runtime, MCP or FPF changes. Below 90% confidence, preserve a specific unresolved Operator question instead of deciding. Use uv only and record actual checks; return an incomplete checkpoint if the bounded work cannot be finished. This Task is created before execution and does not accept candidate semantics.

### Definition of Done

the Plan is **not** Done **if** ((the assigned output, exact identity coverage, five checks, required traceability or handoff is missing) **or** (a positive semantic mark lacks current Main Content evidence or documented preserved/lost distinctions) **or** (an unresolved row is silently decided or loses its question) **or** (original source, occurrence or segment data is omitted or altered) **or** (a required start prerequisite is **not** Done) **or** (verification or current pin checks fail) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
