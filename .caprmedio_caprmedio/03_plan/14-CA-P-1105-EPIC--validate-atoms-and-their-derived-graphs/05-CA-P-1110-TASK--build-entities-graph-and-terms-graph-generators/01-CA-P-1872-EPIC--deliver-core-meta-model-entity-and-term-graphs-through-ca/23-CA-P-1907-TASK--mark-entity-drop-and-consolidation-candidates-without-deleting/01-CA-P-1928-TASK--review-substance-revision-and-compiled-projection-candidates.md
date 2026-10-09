---
atom_id: CA-P-1928
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
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
version: 2
updated_at: "2026-10-10 03:47:57 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1937]
---
# Summary

Review Substance Revision and compiled Projection candidates

## Objective

Review the assigned candidate nodes for duplication, redundancy, emptiness, distinct meaning and generalization without adopting or deleting them.

## Details

Review context: the Operator chose **Finish against the captured snapshot only**. Use the original CA-P-1905 source pins and immutable Git commit `a971d0e00c33c779f485fc8cad63194894d440fb`; read `nodes/snapshot.context.md` and `nodes/support/snapshot_sources.py`. CA-D-494 revision 2 remains the review input; live revision 3 is outside this snapshot. Preserve originals and label receipts as captured-snapshot checks, not current-Core checks. Any currentness or source-pin requirement below means exact validity against this selected captured snapshot. Do not silently rebind or overwrite live Core.

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1906. Each required prerequisite explicitly BLOCKS this Task.

Review only batch 0: 62 exact identities from `nodes.batch-0.input.json` in the durable node-review inputs. Read the shared `contract.md`, pinned baseline, source Main Content, Substance decision record and newer Scope-omission decision. Record all five checks and a source-backed disposition for each assigned identity; preserve qualified names and all uncertainty. Output `nodes.batch-0.review.json` with exact input and evidence pins. Explicitly review Revision versus Version Number/Updated At, Applicable Methodology as one compiled Projection, and Claim versus Substance; preserve required distinctions and current role/type constraints.

Inputs are under `.caprmedio_caprmedio/_projection/core-entity-review/nodes/`; the complete baseline and design remain under its parent review directory. The Scope-omission decision SHA-256 is `d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453`. Scope may be omitted only for full Subject AND full owning Scope Unit; omission retains that resolved default. New names and rules are Operator-backed candidate direction, not retroactive Core evidence or migration approval.

Exclusive scope: assigned derived review output and temporary helper only; root owns Plans, integration receipts and Git. You are not alone; preserve other work. No Core, Subjects, baseline, history, schema, implementation, runtime, MCP or FPF changes. Below 90% confidence, preserve a specific unresolved Operator question instead of deciding. Use uv only and record actual checks; return an incomplete checkpoint if the bounded work cannot be finished. This Task is created before execution and does not accept candidate semantics.

### Definition of Done

the Plan is **not** Done **if** ((the assigned output, exact identity coverage, five checks, required traceability or handoff is missing) **or** (a positive semantic mark lacks current Main Content evidence or documented preserved/lost distinctions) **or** (an unresolved row is silently decided or loses its question) **or** (original source, occurrence or segment data is omitted or altered) **or** (a required start prerequisite is **not** Done) **or** (verification or current pin checks fail) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
