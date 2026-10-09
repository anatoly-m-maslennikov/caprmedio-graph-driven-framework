---
atom_id: CA-P-1906
content_role: Plan
type: Plan
label: Task
work_sequence_number: 22
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
  blocks: [CA-P-1907]
---
# Summary

Design Continuant Occurrent groups and inherited constraints

## Objective

Design a smaller-root Entities Graph candidate with Continuant/Occurrent grouping and inherited common constraints, using the reviewed Core baseline.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent.

Required start prerequisite: CA-P-1905. Inputs: its complete pinned inventory and review, the Operator's draft, and current Core definitions.

Group model objects under Continuant and Occurrent. Separate reusable Action/Step/Workflow definitions and Analysis Reports from actual Action/Step/Workflow Runs and analysis activity. Keep a model object's identity separate from its representation.

Use inheritance of common constraints through justified narrower-than specializations. A Plan Atom or Requirement Atom inherits the common Atom Carrier obligation; it does not inherit another Atom's concrete file. Define shared rules once and show subtype additions or differences. Preserve type-specific Status domains and stricter constraints.

Use as few genuine root entities as the evidence permits. Do not invent relations, collapse incompatible identities or force an uncertain classification merely to reduce the count. Report top-level display groups separately from independent model roots and justify each retained root.

Keep Carrier separate from the carried Entity and its binding metadata. Reuse CARRIES/IS_CARRIED_BY rather than invent another equivalent primitive. Carrier-specific fields such as Basename apply only where the relevant Carrier kind supports them.

Output: a proposed grouped structure, inherited-constraint map, old-to-candidate identity mapping and explicit questions. This is candidate design, not BFO adoption or Core authority.

Exclusive scope: read baseline and Core definitions; write candidate structure and design evidence only. Do not update the authoritative Subjects or step-1 graph, or silently remove nodes.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. These Tasks are created now; their work has not started.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability **or** required handoff is missing) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).

