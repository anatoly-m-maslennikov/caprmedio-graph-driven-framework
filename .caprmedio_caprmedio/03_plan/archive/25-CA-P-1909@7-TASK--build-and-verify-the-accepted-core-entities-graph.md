---
atom_id: CA-P-1909@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 25
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - Entity
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 7
updated_at: 2026-10-24 06:12:10 +0400
relations:
  is_decomposition_of:
  - CA-P-1872
  blocks:
  - CA-P-1910
  - CA-P-1967
tier: 3
---
# Summary

Build and verify the accepted Core Entities Graph

## Objective

Apply only the Operator's accepted candidate decisions to a separately saved Core Entities Graph and verify it before preparing source migration.

## Details

### Accepted current derived-graph basis — 2026-10-14

The Operator answered YES to the exact current-basis question through Codex question call `call_39ad769db88944b9808d27ceed4168fa`. The accepted basis is:

- [Current Candidate #4](../../../../_projection/core-entity-review/presentation/operator.model.candidate-4.md), SHA-256 `a23019a1ee6cd3586640d6c3d9e211091f3683ac5f136058d745650570e78ca7`.
- [Current Subject map](../../../../../.caprmedio_tmp/stage2-migration-20261014/subject-map/subject-map.current.json), SHA-256 `647f7a91ca166a9cfd08560f1303cfb2cc7d2724848dc50794cd1eee78e062f8`.
- [Current source-coverage manifest](../../../../../.caprmedio_tmp/stage2-migration-20261014/journal-rule-refresh/manifest.json), SHA-256 `8c7f2d5a8a43a8defd02c2746b200f33a34a4e861a6f6757562725be547f7abe`.

This binds the reviewed 906 owners and 4,530 occurrences: 611 supported change candidates, 266 unchanged owners and 29 whole-owner holds preserved unchanged. The three file hashes were rechecked against their actual current bytes when recording this answer.

Acceptance is limited to the exact inputs for this separately derived graph. The graph has not yet been built or independently verified; its canonical hash, complete ledgers and decision comparison remain required. Tool readiness and currentness checks remain binding. No Core Subject/content change, native admission, staging, runtime activation or live publication is authorized by this answer. Live application retains its separate exact sealed-packet approval.

Estimated own work: 15 minutes. Assignee: AI Agent.

Stage-2 integration gate: CA-P-2167's independent receipt for the current migration-readiness scope and CA-P-1975's post-grammar Tool readiness must be complete before this accepted-graph work. CA-P-1966's current mapping-disposition and source-rebind evidence must be independently accepted; its explicitly retained Active status does not reopen the completed mapping gate. The exact current candidate/map/source basis has the explicit Operator acceptance recorded above; this does not satisfy Tool readiness, graph construction or independent graph verification.

Readiness conditions: CA-P-1908 is Done, and an explicit recorded Operator decision identifies the exact candidate hash, source pins, occurrence-to-proposed-relation ledger and node-disposition ledger. Handoff, silence, confidence or Plan creation is not acceptance. If the decision or its bindings are missing, ambiguous or stale, remain deferred and ask the Operator; do not apply the candidate.

Inputs: current Candidate #4, the recorded Operator decision and complete current Core mapping-disposition/source-rebind evidence, with CA-P-1908's preserved captured review package retained as historical context. Recheck their bindings before work. Apply only explicitly accepted decisions; keep rejected, unaccepted and unresolved proposals separately visible with their reasons and questions. Preserve complete qualified identities, graph ownership, relation directions, inherited constraints and source-backed Carrier bindings.

Save the accepted derived graph separately from the step-1 baseline and candidate. Retain every old identity and occurrence through the ledgers. Marked drop, consolidation and generalization candidates are not automatic deletions of nodes, source Atoms or history. Record the exact accepted treatment and any separately approved representation change without erasing the baseline or the marked evidence.

Output: the separately saved accepted derived graph, its canonical hash and source pins, a decision-to-graph comparison, complete ledgers and verified acceptance report. Confirm that only accepted changes were applied and unresolved regions remain identified. Operator acceptance of this derived graph is not native semantic admission or authorization to migrate source Atoms.

Exclusive scope: derived graph and decision-verification evidence only. Do not change Core Atoms, Subjects, grammar contracts, YAML keys, runtime, source bindings or historical outputs. Full native MCP delivery remains separate and pending.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold. Split into bounded direct child Plans before execution if the ready work cannot fit 15 minutes. Creation of this Task does not start, authorize or complete this stage, and implies no MCP Run or Journal receipt.

### Definition of Done

the Plan is **not** Done **if** ((CA-P-1908 is **not** Done **or** the explicit Operator decision is missing, ambiguous **or** not bound to the exact candidate and evidence) **or** (the separate accepted graph, canonical hash, current source pins, complete ledgers **or** verified decision comparison is missing) **or** (an unaccepted decision was applied, an unresolved condition was hidden **or** a marked identity lost its traceability) **or** (the baseline, source Atoms, Subjects, grammar **or** history changed outside this Task's authority) **or** (a required check is failed, stale **or** unverified) **or** (uncertainty below the confidence threshold was silently resolved **or** work exceeds the admitted boundary) **or** (any direct decomposing Plan is **not** Done)).
