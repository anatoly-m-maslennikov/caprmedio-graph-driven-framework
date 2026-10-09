---
atom_id: CA-P-1909
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
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
updated_at: "2026-10-10 01:17:19 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1910]
---
# Summary

Build and verify the accepted Core Entities Graph

## Objective

Apply only the Operator's accepted candidate decisions to a separately saved Core Entities Graph and verify it before preparing source migration.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Readiness conditions: CA-P-1908 is Done, and an explicit recorded Operator decision identifies the exact candidate hash, source pins, occurrence-to-proposed-relation ledger and node-disposition ledger. Handoff, silence, confidence or Plan creation is not acceptance. If the decision or its bindings are missing, ambiguous or stale, remain deferred and ask the Operator; do not apply the candidate.

Inputs: the pinned CA-P-1908 review package, the recorded decision and current Core source evidence. Recheck their bindings before work. Apply only explicitly accepted decisions; keep rejected, unaccepted and unresolved proposals separately visible with their reasons and questions. Preserve complete qualified identities, graph ownership, relation directions, inherited constraints and source-backed Carrier bindings.

Save the accepted derived graph separately from the step-1 baseline and candidate. Retain every old identity and occurrence through the ledgers. Marked drop, consolidation and generalization candidates are not automatic deletions of nodes, source Atoms or history. Record the exact accepted treatment and any separately approved representation change without erasing the baseline or the marked evidence.

Output: the separately saved accepted derived graph, its canonical hash and source pins, a decision-to-graph comparison, complete ledgers and verified acceptance report. Confirm that only accepted changes were applied and unresolved regions remain identified. Operator acceptance of this derived graph is not native semantic admission or authorization to migrate source Atoms.

Exclusive scope: derived graph and decision-verification evidence only. Do not change Core Atoms, Subjects, grammar contracts, YAML keys, runtime, source bindings or historical outputs. Full native MCP delivery remains separate and pending.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold. Split into bounded direct child Plans before execution if the ready work cannot fit 15 minutes. Creation of this Task does not start, authorize or complete this stage, and implies no MCP Run or Journal receipt.

### Definition of Done

the Plan is **not** Done **if** ((CA-P-1908 is **not** Done **or** the explicit Operator decision is missing, ambiguous **or** not bound to the exact candidate and evidence) **or** (the separate accepted graph, canonical hash, current source pins, complete ledgers **or** verified decision comparison is missing) **or** (an unaccepted decision was applied, an unresolved condition was hidden **or** a marked identity lost its traceability) **or** (the baseline, source Atoms, Subjects, grammar **or** history changed outside this Task's authority) **or** (a required check is failed, stale **or** unverified) **or** (uncertainty below the confidence threshold was silently resolved **or** work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
