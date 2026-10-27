---
atom_id: CA-P-2333@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 8
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Graph/Relation
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 07:52:46 +0400
relations:
  is_decomposition_of:
  - CA-P-2307
tier: 3
---
# Summary

Accept unordered relation targets

## Objective

Relation target order has no semantic meaning and does not block Atom admission.

## Details

Estimated own work: up to 15 minutes. Apply the Operator decision through D268, with an exact predecessor archive and Version increment. Remove only the obsolete validation requirement for a canonical target-list order. Refresh affected current source bindings and fixtures. Keep uniqueness, valid targets, Relation Kind semantics and stale-source checks.

Independent lanes: governing-source review; checker and bindings implementation; regression tests. Root owns integration and Git. Verify target permutations, duplicates, missing targets, unsupported kinds and stale authority. Recheck the finite TOML packet; report any remaining unsupported relation separately. Do not sort authored lists, change relation meaning, amend unsupported kinds or enable live publication.

### Definition of Done

The Plan is not Done if order alone rejects an otherwise valid relation list, duplicate or invalid references become accepted, required current pins are stale, or focused independent verification is missing.

### Accepted outcome

D268 v13 and exact v12 history passed independent source review. The checker removes only the ordering gap; current source pins and fixtures match. Author focused tests: 53 passed. Independent tests: four passed, including 24 complete-carrier permutations and invalid/stale controls. See unordered-relation-targets-acceptance.md in the tools-first evidence directory. Unsupported relates_to remains a separate gate; no live publication is accepted.
