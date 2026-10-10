---
atom_id: CA-P-1937
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
status: Done
subjects:
  governs: Projection
  depends_on: [Entity, Term, Atom, Property, Carrier, Plan]
version: 6
updated_at: "2026-10-10 04:48:00 +0400"
relations:
  is_decomposition_of: [CA-P-1907]
  blocks: [CA-P-1938]
---
# Summary

Integrate the complete Core node disposition review

## Objective

Join the complete source-pinned node review and annotate the preserved relation ledger for the candidate handoff.

## Details

Review context: the Operator chose **Finish against the captured snapshot only**. Use the original CA-P-1905 source pins and immutable Git commit `a971d0e00c33c779f485fc8cad63194894d440fb`; read `nodes/snapshot.context.md` and `nodes/support/snapshot_sources.py`. CA-D-494 revision 2 remains the review input; live revision 3 is outside this snapshot. Preserve originals and label receipts as captured-snapshot checks, not current-Core checks. Any currentness or source-pin requirement below means exact validity against this selected captured snapshot. Do not silently rebind or overwrite live Core.

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisites: CA-P-1928, CA-P-1929, CA-P-1930, CA-P-1931, CA-P-1932, CA-P-1933, CA-P-1934, CA-P-1935, CA-P-1936, CA-P-1952, CA-P-1953, CA-P-1954, CA-P-1955, CA-P-1956. Each required prerequisite explicitly BLOCKS this Task. Read the final repaired outputs; original Done batch receipts remain historical and do not pin the later repaired review bytes. CA-P-1956 supplies a post-join batch-3 correction, not a fresh original join receipt.

Join all nine Done review outputs, covering 706 baseline identities exactly once. Preserve original evidence, questions, dispositions and every row in CA-P-1906's 3093-segment ledger. Annotate affected and unaffected qualified endpoints without inventing a native relation or changing original reasons. Output `nodes.dispositions.json`, `relations.marked.ledger.json` and a marked candidate structure, plus a reproducible create-only producer in the node-review directory. Preserve requested Revision/Projection/Substance examples and Scope-omission default. Shared RMED pointers, additional separately evidenced relations, inherited constraints and historical references remain traceable. No actual deletion or source migration.

Inputs are under `.caprmedio_caprmedio/_projection/core-entity-review/nodes/`; the complete baseline and design remain under its parent review directory. The Scope-omission decision SHA-256 is `d4ea636d540b0558c1a0fbb8263760947e1f0768840c43b3ed1d05c96b497453`. Scope may be omitted only for full Subject AND full owning Scope Unit; omission retains that resolved default. New names and rules are Operator-backed candidate direction, not retroactive Core evidence or migration approval.

Exclusive scope: assigned derived review output and temporary helper only; root owns Plans, integration receipts and Git. You are not alone; preserve other work. No Core, Subjects, baseline, history, schema, implementation, runtime, MCP or FPF changes. Below 90% confidence, preserve a specific unresolved Operator question instead of deciding. Use uv only and record actual checks; return an incomplete checkpoint if the bounded work cannot be finished. This Task is created before execution and does not accept candidate semantics.

### Completion receipt

Create-only integration completed against final review receipt commit `67d83ebaeeeae6cd2c2e260947c8ffc926d7a329` and captured Core commit `a971d0e00c33c779f485fc8cad63194894d440fb`. All 14 prerequisites were verified by exact current Atom ID, Done status and captured hash; all nine committed review byte identities and all 951 captured source pins passed.

Outputs: `nodes/nodes.dispositions.json` SHA-256 `1b9d751f95aa71486908b53b3d7f3f9825defae137be3d8792d45177587c48f8`; `nodes/relations.marked.ledger.json` SHA-256 `f6efdcaddfbbb4d9f4607084ee77ca83c75de2566fd9506da51dac2493e02371`; `nodes/candidate.structure.marked.json` SHA-256 `04f2b8d3606ac30b74850ab9ff53ebebfcbcffd1cda1e5ad2d948662c085e34b`.

Preserved 706 identities, 4534 occurrences, 3093 original relation segments and every original ledger/candidate field. Added 6186 endpoint annotations. Dispositions: 584 retain, 3 consolidation proposals, 2 generalization proposals and 117 questions, including two unresolved potential-drop marks. Dry-run, persistence and exact read-only reproduction passed; root independently confirmed original-field preservation and counts. Producer SHA-256 `9f53c3bdeb5987522d2345cda2c8441f58b6903af9da8c198f2f91c67355a178`. Core/Subjects/baseline and the user's edited Step 1 tree remain untouched by this work. Independent overall acceptance CA-P-1938 remains a separate gate.

### Definition of Done

the Plan is **not** Done **if** ((the assigned output, exact identity coverage, five checks, required traceability or handoff is missing) **or** (a positive semantic mark lacks current Main Content evidence or documented preserved/lost distinctions) **or** (an unresolved row is silently decided or loses its question) **or** (original source, occurrence or segment data is omitted or altered) **or** (a required start prerequisite is **not** Done) **or** (verification or current pin checks fail) **or** (the exclusive boundary is exceeded) **or** (any direct decomposing Plan is **not** Done)).
