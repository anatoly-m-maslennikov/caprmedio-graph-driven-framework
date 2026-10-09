---
atom_id: CA-P-1950
content_role: Plan
type: Plan
label: Task
work_sequence_number: 7
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
  is_decomposition_of: [CA-P-1931]
---
# Summary

Join the reviewed Core node batch 3 slices

## Objective

Join all completed coherent slices into the preserved 80-node parent review with exact pins and questions.

## Details

Review context: the Operator chose **Finish against the captured snapshot only**. Use the original CA-P-1905 source pins and immutable Git commit `a971d0e00c33c779f485fc8cad63194894d440fb`; read `nodes/snapshot.context.md` and `nodes/support/snapshot_sources.py`. CA-D-494 revision 2 remains the review input; live revision 3 is outside this snapshot. Preserve originals and label receipts as captured-snapshot checks, not current-Core checks. Any currentness or source-pin requirement below means exact validity against this selected captured snapshot. Do not silently rebind or overwrite live Core.

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisites: CA-P-1939, CA-P-1940, CA-P-1941, CA-P-1942, CA-P-1943, CA-P-1944. Each explicitly BLOCKS this Task.

Verify all child Tasks are Done, union exactly equals the parent 80-identity partition, and each identity appears once. Join evidence catalogues without accidental reference collisions; preserve every check, meaning, replacement, confidence and question. Revalidate current source and input pins. Output `nodes.batch-3.review.json` under the node-review directory; no other batch change or semantic inference. Use the shared contract and record complete source/child completion pins. No generic placeholder rows.

Exclusive scope: this derived join and temporary helper. You are not alone; root owns Plans/Git. No Core, Subjects, baseline, history, schema, implementation, runtime, MCP or FPF writes. Use uv only; unresolved meanings stay questions, not decisions.

### Definition of Done

the Plan is **not** Done **if** ((coverage or source traceability is incomplete or duplicated) **or** (an original child field, proposal or question is lost or changed) **or** (current pin or independent checks fail) **or** (a required start prerequisite is **not** Done) **or** (the output/handoff is missing) **or** (the exclusive scope is exceeded) **or** (any direct decomposing Plan is **not** Done)).
