---
atom_id: CA-P-2332@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Domain/Node/Continuant/Atom.Updated At
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 4
updated_at: 2026-10-24 17:05:24 +0400
relations:
  is_decomposition_of:
  - CA-P-2264
tier: 3
---
# Summary

Clarify ancestor-only carrier movement

## Objective

Apply the Operator's universal distinction: moving an ancestor without changing an Atom's own content, metadata, direct owner or placement relative to that owner does not revise the Atom.

## Details

Estimated own work: up to 15 minutes. Resolve only receiving-rule audit RR-I1/RR-F1 through a narrow governing-source clarification and independent targeted review. Update R1432 and R1788 with exact predecessor archives, Version +1 and actual Updated At; inspect direct dependent rules before proposing any additional amendment.

For example, moving an Epic leaves an unchanged Task's path relative to that Epic unchanged; moving an owning Scope Unit leaves an unchanged Requirement's direct owner unchanged. Keep that child's Version and Updated At. Actual changes to the Atom's own bytes, metadata, direct ownership or local placement still follow the existing revision rules. This does not exempt changes caused by an owner rename or reassignment, add a new ownership model, or mutate historical revisions.

Check existing O029/O066 receiving clauses and independently verify affected source pins and examples: unchanged child, child needing a Status change, direct placement change, and old history. No broad FPF rerun, cascade implementation or live migration.

### Definition of Done

The Plan is not Done if the distinction remains ambiguous, an actual own-Atom update avoids revision, old history changes, required current consumers are stale, or targeted independent review is missing.
