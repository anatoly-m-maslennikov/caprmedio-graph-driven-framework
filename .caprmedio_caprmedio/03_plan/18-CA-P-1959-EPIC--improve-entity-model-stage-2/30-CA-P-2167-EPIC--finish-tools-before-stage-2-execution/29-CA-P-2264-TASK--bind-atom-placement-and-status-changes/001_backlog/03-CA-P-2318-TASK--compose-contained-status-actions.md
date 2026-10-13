---
atom_id: CA-P-2318
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
  is_decomposition_of: [CA-P-2264]
---
# Summary

Compose contained Status actions

## Objective

Contained Status changes execute as independent admitted per-Atom actions with truthful observed results.

## Details

Estimated own work: up to 15 minutes. Split further work before exceeding this bound. Inherit the parent's accepted source, independent review and execution gates. Root owns Plans and Git; assigned file ownership stays disjoint.

Start after P2316 and P2317 acceptance. Reuse M372 composition and O127/O129/O128; retain one target per Action. Preserve matching directories and nested carriers, exact predecessor bytes, Version +1 and actual time for each change. No-op preserves metadata. Rebind current paths after parent moves; stop on first failed or uncertain outcome, preserve earlier completed effects, and never auto-replay. Refuse unsupported child Status before falsely reporting a completed cascade. Cover general Status and applicable Draft promotion without changing explicit identity admission. Split if code exceeds this bound.

### Definition of Done

The Plan is **not** Done if its stated outcome lacks exact source/code/test evidence and independent verification; required checks fail; a deferred policy is inferred; existing safety checks are bypassed; or source-only/isolated evidence is represented as live runtime or migration acceptance.
