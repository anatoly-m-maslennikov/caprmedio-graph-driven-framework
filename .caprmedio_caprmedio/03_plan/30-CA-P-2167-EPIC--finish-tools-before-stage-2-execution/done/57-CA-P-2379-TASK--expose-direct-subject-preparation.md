---
atom_id: CA-P-2379
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Expose direct Subject preparation

## Objective

Expose approved direct preview and staging operations through the existing canonical Tool registration and preparation helpers.

## Details

Production edits begin only after CA-P-2378 source acceptance. Test preparation may start earlier. Preserve existing CLI and publication guards; resolve logical identities inside the bound Project, never accept arbitrary caller paths. Return source-pinned preview and actual scratch evidence. Require the exact reviewed preview before staging and refuse stale or invalid sources before candidate creation. Only implement patch shapes already supported by the helpers; no ordinary content edits.

Estimated own work: up to 15 minutes; split if necessary. Root owns Plans, integration and Git. Preserve unrelated work. Stage-specific gates are not whole-Task start blockers or Artifact depends_on Relations.

### Definition of Done

Independent review accepts the adapter and focused tests for closed input, current source identity, exact preview/staging match, scratch containment and refusal behavior. Existing relevant local preparation checks pass; no installed readiness is inferred.

### Acceptance — 2026-10-14

Implementation commit 15f9ce76e exposes the closed direct preview/stage provider using the existing helpers and six accepted source pins. Independent connected-code review passed after fixing exact no-op timestamp matching and live/dangling terminal role-directory links. Native seal checks precede all scratch creation. Final native checks passed 48 cases; seven provider checks and sixteen existing patch-preview checks passed Root's fresh combined 23-case run. Public logical inputs, unchanged sealed output, Project/source currentness and truthful partial-artifact evidence remain intact. No generic patch expansion, publication or installed activation is claimed.
