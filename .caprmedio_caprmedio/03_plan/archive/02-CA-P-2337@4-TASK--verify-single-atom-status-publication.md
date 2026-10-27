---
atom_id: CA-P-2337@4
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
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Configuration
  - Workflow
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 4
updated_at: 2026-10-24 06:12:24 +0400
relations:
  is_decomposition_of:
  - CA-P-2318
tier: 3
---
# Summary

Verify single Atom Status publication

## Objective

Independent fixtures verify the single-target Status publisher's exact bytes, paths and truthful failure effects.

## Details

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; workers own disjoint implementation/test files and preserve other workers' edits. Inherit accepted parent RMEDO and independent review gates.

Prepare independently while P2336 is implemented; final execution and acceptance require its frozen production pins. Cover nested P/O, exact old history, matching directories, unchanged descendants, no-op, stale/collision refusals and failures at each changed boundary. Exercise the actual lifecycle entry where applicable; do not substitute mock admission for selected-execution acceptance. Existing selected Run/Journal integration remains a following slice. No live project mutation.

### Definition of Done

The outcome has exact current source/code/test evidence, actual positive/refusal checks and independent acceptance. Preparation, isolated helpers or source acceptance do not establish live/runtime completion. No unapproved policy, weakened guard, live Core migration or deferred capability is included.

### Accepted outcome — 2026-10-13

The final connected implementation is independently accepted in contained-status-and-plan-admission-acceptance.md under the Stage-2 Tools-first derived receipts. Full validator: 433/433. Independent real publication/placement: 33/33. Reference lifetime/closure: 28/28, including actual post-lookup mutation and namespace refusals. Real P2264 v6, P2256 v6 and P2272 v7 passed finite PRMEDO admission with exact bytes unchanged. This Task's bounded implementation/check scope is complete; selected lifecycle rebinding, cascade execution, Draft identity, runtime activation and live migration remain separate.
