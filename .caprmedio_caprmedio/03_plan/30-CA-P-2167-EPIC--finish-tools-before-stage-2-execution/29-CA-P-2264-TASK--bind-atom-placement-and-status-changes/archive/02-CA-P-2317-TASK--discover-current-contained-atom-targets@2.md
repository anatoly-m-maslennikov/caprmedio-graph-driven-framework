---
atom_id: CA-P-2317
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Configuration, Workflow, Plan]
version: 2
updated_at: "2026-10-13 20:19:05 +0400"
relations:
  is_decomposition_of: [CA-P-2264]
---
# Summary

Discover current contained Atom targets

## Objective

A source-bound read-only inventory selects the latest contained P/O Atom targets for an explicit parent.

## Details

Estimated own work: up to 15 minutes. Split further work before exceeding this bound. Inherit the parent's accepted source, independent review and execution gates. Root owns Plans and Git; assigned file ownership stays disjoint.

Start after P2316's independently accepted receiving packet and applicable review. Reuse admitted-container discovery, explicit stored identities/statuses and current-source checks. Preserve containment order and matching directory relationships without taking native relation links as containment. Exclude old history and outside referenced Atoms; refuse ambiguity, duplicate current identity or unsupported source placement. Do not modify source metadata or invent inherited Status. Prove nested P/O, no children, history and stale-source cases.

### Definition of Done

The Plan is **not** Done if its stated outcome lacks exact source/code/test evidence and independent verification; required checks fail; a deferred policy is inferred; existing safety checks are bypassed; or source-only/isolated evidence is represented as live runtime or migration acceptance.
