---
atom_id: CA-P-2317@7
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
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
version: 7
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2264
tier: 3
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

### Acceptance — 2026-10-13

The private read-only contained-target inventory passed 21 combined tests and a separate 11-test independent run. Review found and fixed orphan Directory Carrier and invalid newer-carrier suppression defects; both have failing-baseline regressions. Exact final implementation/test hashes and boundaries are recorded in `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/contained-target-discovery-acceptance.md`. No Status mutation, publication or runtime activation is included. P2318 must rediscover and rebind after preceding independent actions.
