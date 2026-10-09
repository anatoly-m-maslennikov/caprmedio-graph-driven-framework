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
version: 2
updated_at: "2026-10-10 01:17:19 +0400"
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

Output: a proposed grouped structure, inherited-constraint map, old-to-candidate identity mapping, complete occurrence-to-proposed-relation ledger and explicit questions. This is candidate design, not BFO adoption or Core authority.

The relation ledger must retain **every** old source Subject relation segment, including every `/` occurrence, each supporting qualified prefix and unchanged `:` row. It is not a deduplicated graph-edge list or a ledger only for affected nodes. Each row must record the source Atom ID, Revision and Carrier hash; Subjects field index, complete path and exact segment; original qualified endpoints and graph kind; and disposition with confidence. For an evidenced proposal, record the proposed display operator, canonical Relation and direction, proposed qualified endpoints and evidence span. For an `unresolved` or `not-native` row, leave the asserted native proposal, direction and new endpoints explicitly absent; record the missing-evidence or inapplicability reason, what was checked and any required Operator question. Do not invent a proposal or positive evidence to complete a row.

Classify an old `/` as `/` or `.` only from source Main Content evidence. Propose `@` only where independent Core-declared Carrier-binding evidence supports it, never from Atom incidence or matching spelling. Record aliases and inverse views once as the same underlying Relation, not duplicate facts. Preserve every old occurrence without silent omission, and do not serialize raw `@` into Atom Subjects.

Exclusive scope: read baseline and Core definitions; write candidate structure and design evidence only. Do not update the authoritative Subjects or step-1 graph, or silently remove nodes.

Inherit CA-P-1872's explicit 90% confidence threshold and local-without-MCP authorization. Ask the Operator before deciding below that threshold; do not disguise uncertainty as an accepted fact. If the ready workload exceeds 15 minutes, split it into bounded direct child Plans before execution. These Tasks are created now; their work has not started.

### Definition of Done

the Plan is **not** Done **if** ((the stated output, complete source traceability, complete occurrence-to-proposed-relation ledger **or** required handoff is missing) **or** (any old relation segment lacks its source coordinates, original qualified endpoints, graph kind **or** disposition) **or** (a proposed relation lacks its proposal fields **or** evidence span) **or** (an unresolved **or** not-native row asserts an invented native proposal **or** lacks its reason, checks performed **or** required Operator question) **or** (a required start prerequisite is **not** Done) **or** (the stated acceptance conditions are failed, stale **or** unverified) **or** (uncertainty below the inherited confidence threshold is silently resolved **or** not put to the Operator) **or** (work exceeds the admitted boundary **or** any source, Subject, history **or** marked Entity was changed **or** deleted without separate authorization) **or** (any direct decomposing Plan is **not** Done)).
