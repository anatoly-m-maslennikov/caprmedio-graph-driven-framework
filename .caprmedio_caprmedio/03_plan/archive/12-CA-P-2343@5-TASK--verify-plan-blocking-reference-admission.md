---
atom_id: CA-P-2343@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Graph/Relation
version: 5
updated_at: 2026-10-24 07:52:46 +0400
relations:
  is_decomposition_of:
  - CA-P-2307
tier: 3
---
# Summary

Verify Plan blocking reference admission

## Objective

Independent tests prove typed Plan blocking references admit valid pending/history endpoints while preserving ordinary authority constraints.

## Details

Prepare explicit source-admitted Plan fixtures and full proposed-carrier calls. Reproduce the current Backlog blocker failure first. Include non-Plan and ordinary inactive RMED refusal, same ID reached by different kinds, authenticated placement, duplicate/current-history ambiguity and stale frontier. Final verification requires P2342 frozen code plus actual finite admission of affected current parent Plans. No mutation of Plan edges/statuses to make tests pass.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git; implementation and independent tests use disjoint files. Current source authority remains unchanged; C/A legacy migration stays deferred.

### Definition of Done

Exact current source/code/test evidence, actual positive/refusal checks and independent review establish the outcome. No guessed policy, weakened unrelated guard or unsupported runtime claim. Preparation alone is not completion.

### Accepted outcome — 2026-10-13

The final connected implementation is independently accepted in contained-status-and-plan-admission-acceptance.md under the Stage-2 Tools-first derived receipts. Full validator: 433/433. Independent real publication/placement: 33/33. Reference lifetime/closure: 28/28, including actual post-lookup mutation and namespace refusals. Real P2264 v6, P2256 v6 and P2272 v7 passed finite PRMEDO admission with exact bytes unchanged. This Task's bounded implementation/check scope is complete; selected lifecycle rebinding, cascade execution, Draft identity, runtime activation and live migration remain separate.
