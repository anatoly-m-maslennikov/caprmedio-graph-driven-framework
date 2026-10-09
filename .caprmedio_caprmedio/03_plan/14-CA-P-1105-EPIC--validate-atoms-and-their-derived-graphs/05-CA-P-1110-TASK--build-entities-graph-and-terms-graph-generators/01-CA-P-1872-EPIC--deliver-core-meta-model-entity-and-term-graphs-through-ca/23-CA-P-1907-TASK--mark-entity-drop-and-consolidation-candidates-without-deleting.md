---
atom_id: CA-P-1907
content_role: Plan
type: Plan
label: Task
work_sequence_number: 23
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
updated_at: "2026-10-10 00:36:36 +0400"
relations:
  is_decomposition_of: [CA-P-1872]
  blocks: [CA-P-1908]
---
# Summary

Mark Entity drop and consolidation candidates without deleting

## Objective

Mark excessive or redundant Entities in the proposed graph for dropping or consolidation, preserving every reviewed source identity and its evidence.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1906. Inputs: CA-P-1905's pinned inventory and CA-P-1906's proposed structure and inheritance map.

Review repeated fields, Carrier bindings, serialization details, helper labels and operation-definition/run distinctions. Distinguish an unnecessary independent Entity from a useful Property, inherited constraint, relation, allowed value or detail that should only be hidden in a particular view.

Record a disposition for every baseline identity: retain, move, inherit, consolidate, drop candidate, or question. Every drop/consolidation mark needs its source references, reason, proposed replacement and impact on Relations, historical references and queries. Mark affected nodes visibly; do not delete them or their governing Atoms.

Explicit example: mark Revision as a drop/consolidation candidate because Version Number and Updated At can describe an Atom's selected state. Propose Atom.Version Number and Atom.Updated At as replacements where appropriate, while preserving distinct historical states and exact reference information. Do not remove revision history or rename serialization keys in this Task.

Output: a complete disposition ledger and marked candidate graph. Keep marked identities visible and traceable; count retained independent roots separately from marked drop candidates.

Exclusive scope: candidate annotations and review evidence only. No source, Subject, schema, implementation or historical-artifact deletions or migrations.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. These Tasks are created now; their work has not started.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability **or** required handoff is missing) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).

