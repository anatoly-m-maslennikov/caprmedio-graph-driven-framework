---
atom_id: CA-P-2322
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
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

Bind declaration boundary consumers

## Objective

Every affected declaration consumer enforces and rechecks the shared Project boundary proof.

## Details

Estimated own work: up to 15 minutes. Split further work before exceeding this bound. Inherit the parent's accepted source, independent review and execution gates. Root owns Plans and Git; assigned file ownership stays disjoint.

After P2321, wire both authority_path and delivery_path checks through ProjectSelection, Project Structure normalization, graph Delivery binding, Scope reading and proposed-carrier validation. Preserve finite currentness evidence and reject changes before use. Do not rescan and silently reseal drift. Tests must exercise actual callers, not only the helper. Settings revision/Journal readiness remains separate.

### Definition of Done

The Plan is **not** Done if its stated outcome lacks exact source/code/test evidence and independent verification; required checks fail; a deferred policy is inferred; existing safety checks are bypassed; or source-only/isolated evidence is represented as live runtime or migration acceptance.
