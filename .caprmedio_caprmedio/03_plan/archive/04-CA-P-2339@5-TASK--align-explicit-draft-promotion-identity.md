---
atom_id: CA-P-2339@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Configuration
  - Subject/Engineering/Workflow
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2318
tier: 3
---
# Summary

Align explicit Draft promotion identity

## Objective

Draft promotion uses the explicit identity admitted by current O066/O128 rather than allocating a new identity silently.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; workers own disjoint implementation/test files and preserve other workers' edits. Inherit accepted parent RMEDO and independent review gates.

Inspect actual promotion request, lineage and collision contracts; preserve separately accepted history behavior. Replace the conflicting implicit max-plus-one choice only after exact receiving binding is established. Cover explicit assigned ID, collision, wrong request/head, no-op and observed failure without inventing retry. Matching-carrier handling must follow accepted single-target rules. Ask the Operator if source contracts disagree; do not infer a new identity policy.

### Definition of Done

The outcome has exact current source/code/test evidence, actual positive/refusal checks and independent acceptance. Preparation, isolated helpers or source acceptance do not establish live/runtime completion. No unapproved policy, weakened guard, live Core migration or deferred capability is included.
