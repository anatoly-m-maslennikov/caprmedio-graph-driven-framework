---
atom_id: CA-R-1817@8
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run.Coverage
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
type: Rule
---
# Summary

Pause on incomplete Base Revise coverage

## Scope

RMED Atoms Base Revise execution in WORKFLOW_ORCHESTRATOR.

## Claim

every Base Revise main phase **must** pass a Coverage Gate **before** continuation **or** completed status.

## Details

- gather covers the explicitly frozen selection **and** rules, **not** an inferred full Project corpus.
- check covers **all** **`=6`** checks for **all** selected Atoms; failed checks can be concluded, blocked checks cannot.
- fix covers every selected Atom **and** every recorded finding disposition, **not** a post-fix semantic pass.
- coverage below **`=100`** percent **or** unknown coverage pauses **and** exposes an Operator question with missing work. a client-side observer presents this question; an idle worker does **not** invent a chat notification.
