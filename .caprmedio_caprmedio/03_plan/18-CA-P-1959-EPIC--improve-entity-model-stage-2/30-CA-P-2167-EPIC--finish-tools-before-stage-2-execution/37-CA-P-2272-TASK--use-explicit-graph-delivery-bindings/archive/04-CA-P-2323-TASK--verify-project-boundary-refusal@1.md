---
atom_id: CA-P-2323
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Backlog
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Configuration, Workflow, Plan]
version: 1
updated_at: "2026-10-13 19:01:00 +0400"
relations:
  is_decomposition_of: [CA-P-2272]
---
# Summary

Verify Project boundary refusal

## Objective

Independent tests prove cross-Project paths are refused without rejecting ordinary lookalikes.

## Details

Estimated own work: up to 15 minutes. Split further work before exceeding this bound. Inherit the parent's accepted source, independent review and execution gates. Root owns Plans and Git; assigned file ownership stays disjoint.

Prepare fixtures independently while implementation proceeds; final acceptance waits for P2321/P2322. Cover both path fields, foreign roots/descendants, same-name distinct Project instances, missing foreign Structure, owning paths, empty lookalikes, absent paths, malformed/conflicting/symlink/unreadable Settings, and Settings introduction/change/removal. Verify actual Selection, Structure, Graph, Scope and complete-carrier callers and no write effects.

### Definition of Done

The Plan is **not** Done if its stated outcome lacks exact source/code/test evidence and independent verification; required checks fail; a deferred policy is inferred; existing safety checks are bypassed; or source-only/isolated evidence is represented as live runtime or migration acceptance.
