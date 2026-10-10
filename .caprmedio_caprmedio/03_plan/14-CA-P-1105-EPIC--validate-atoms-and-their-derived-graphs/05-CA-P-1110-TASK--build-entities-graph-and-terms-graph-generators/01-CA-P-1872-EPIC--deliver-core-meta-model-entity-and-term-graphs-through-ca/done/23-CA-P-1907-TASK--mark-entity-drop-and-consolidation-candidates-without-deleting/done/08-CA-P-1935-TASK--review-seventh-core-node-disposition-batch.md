---
atom_id: CA-P-1935
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 4
updated_at: "2026-10-10 04:14:46 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1937]
---
# Summary

Review seventh Core node disposition batch

## Objective

Review the assigned candidate nodes for duplication, redundancy, emptiness, distinct meaning and generalization without adopting or deleting them.

## Details

Review context: the Operator chose **Finish against the captured snapshot only**. Use the original CA-P-1905 source pins and immutable Git commit `a971d0e00c33c779f485fc8cad63194894d440fb`; read `nodes/snapshot.context.md` and `nodes/support/snapshot_sources.py`. CA-D-494 revision 2 remains the review input; live revision 3 is outside this snapshot. Preserve originals and label receipts as captured-snapshot checks, not current-Core checks. Any currentness or source-pin requirement below means exact validity against this selected captured snapshot. Do not silently rebind or overwrite live Core.

Child work only; no separately executable own work. The broad batch is split into coherent source-review slices before further execution.

Required start prerequisite: CA-P-1906. Each required prerequisite explicitly BLOCKS this Task.

Review only batch 7: 80 exact identities from `nodes.batch-7.input.json` in the durable node-review inputs. Read the shared `contract.md`, pinned baseline, source Main Content, Substance decision record and newer Scope-omission decision. Record all five checks and a source-backed disposition for each assigned identity; preserve qualified names and all uncertainty. Output `nodes.batch-7.review.json` with exact input and evidence pins. Repeated labels and bare or support-only Subject nodes require actual meaning review, not default drops or fabricated parentage.

Inputs are under `.caprmedio_caprmedio/_projection/core-entity-review/nodes/`; the complete baseline and design remain under its parent review directory. The Scope-omission decision SHA-256 is `d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453`. Scope may be omitted only for full Subject AND full owning Scope Unit; omission retains that resolved default. New names and rules are Operator-backed candidate direction, not retroactive Core evidence or migration approval.

Exclusive scope: assigned derived review output and temporary helper only; root owns Plans, integration receipts and Git. You are not alone; preserve other work. No Core, Subjects, baseline, history, schema, implementation, runtime, MCP or FPF changes. Below 90% confidence, preserve a specific unresolved Operator question instead of deciding. Use uv only and record actual checks; return an incomplete checkpoint if the bounded work cannot be finished. This Task is created before execution and does not accept candidate semantics.

### Bounded direct Tasks

The first executor returned a truthful unexecuted checkpoint; no complete review was fabricated. The following coherent subsets are disjoint and cover all 80 parent identities. Each child starts only after CA-P-1906 Done; the join waits for every review child Done. This parent stays Active until all its direct children and Definition of Done pass.

- [CA-P-1945](08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch/done/01-CA-P-1945-TASK--review-rmed-reconciliation-node-candidates.md): Review RMED reconciliation node candidates (12 nodes); 15 minutes.
- [CA-P-1946](08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch/done/02-CA-P-1946-TASK--review-relation-kind-node-candidates.md): Review Relation kind node candidates (12 nodes); 15 minutes.
- [CA-P-1947](08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch/done/03-CA-P-1947-TASK--review-operation-and-scope-expression-node-candidates.md): Review operation and Scope expression node candidates (16 nodes); 15 minutes.
- [CA-P-1948](08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch/done/04-CA-P-1948-TASK--review-scope-unit-operation-node-candidates.md): Review Scope Unit operation node candidates (20 nodes); 15 minutes.
- [CA-P-1949](08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch/done/05-CA-P-1949-TASK--review-source-spec-and-run-node-candidates.md): Review source spec and Run node candidates (20 nodes); 15 minutes.
- [CA-P-1951](08-CA-P-1935-TASK--review-seventh-core-node-disposition-batch/done/06-CA-P-1951-TASK--join-the-reviewed-core-node-batch-7-slices.md): Join the reviewed Core node batch 7 slices; 15 minutes.

### Completion receipt

All five semantic slice reviews and CA-P-1951 join are Done. Complete batch-7 output covers 80 original identities (72 retain, 8 question), with 115 exact captured Main Content spans; SHA-256 `190f91dccbf5e8009f2956e7c8b3cf52ca4e72b64129393b9c5a5f2b60ec28e3`. Original child decisions, quotes, questions and proposals remain unchanged. This is captured-snapshot review only, not current-Core or adoption acceptance.

### Definition of Done

the Plan is **not** Done **if** ((the assigned output, exact identity coverage, five checks, required traceability or handoff is missing) **or** (a positive semantic mark lacks current Main Content evidence or documented preserved/lost distinctions) **or** (an unresolved row is silently decided or loses its question) **or** (original source, occurrence or segment data is omitted or altered) **or** (a required start prerequisite is **not** Done) **or** (verification or current pin checks fail) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
