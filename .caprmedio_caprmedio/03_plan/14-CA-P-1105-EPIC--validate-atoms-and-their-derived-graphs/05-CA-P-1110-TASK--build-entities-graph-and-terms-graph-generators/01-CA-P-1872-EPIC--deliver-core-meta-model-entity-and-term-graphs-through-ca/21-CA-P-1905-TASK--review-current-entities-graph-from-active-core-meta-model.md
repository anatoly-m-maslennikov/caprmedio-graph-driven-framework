---
atom_id: CA-P-1905
content_role: Plan
type: Plan
label: Task
work_sequence_number: 21
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
  blocks: [CA-P-1906]
---
# Summary

Review current Entities Graph from Active Core Meta-model

## Objective

Review the current Entities Graph derived from Active Atoms owned by CORE_META_MODEL, and produce a source-pinned baseline for candidate design.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Inputs: the current registered CORE_META_MODEL authority path, current exact-Active Core-owned Atom selection, step1.graph.json, step1.entities.indented.txt, and the Operator's edited Continuant/Occurrent draft.

Check the current source selection and hashes before reusing the saved step-1 graph. If sources changed, report the drift and prepare a fresh separate baseline without overwriting historical output. Exclude Project Configuration and Extensions. Do not transfer source Atom metadata to the model objects those Atoms describe.

Inventory all current model nodes, literal prefixes, relation candidates, common fields, independent roots and duplicate-looking branches. Distinguish a declared Subject path from an admitted native Entity or Relation. Identify where source Main Content is needed to interpret the old slash notation.

Output: a source-pinned review report and complete baseline inventory for CA-P-1906. Record the source frontier, selected and excluded source counts, root/node counts, and unresolved findings.

Exclusive scope: read Core authority, existing code and projections; write review evidence and a separate derived baseline only. Do not classify the candidate as accepted, edit Core Atoms or their Subjects, delete nodes, migrate grammar or activate a runtime.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. These Tasks are created now; their work has not started.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability **or** required handoff is missing) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).

