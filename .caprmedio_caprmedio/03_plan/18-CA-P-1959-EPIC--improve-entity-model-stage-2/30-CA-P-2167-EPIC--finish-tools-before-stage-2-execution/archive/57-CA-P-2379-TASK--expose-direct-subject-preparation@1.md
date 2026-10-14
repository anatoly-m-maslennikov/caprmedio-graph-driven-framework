---
atom_id: CA-P-2379
content_role: Plan
type: Plan
label: Task
work_sequence_number: 57
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-14 10:38:15 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
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
