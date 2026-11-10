---
atom_id: CA-R-1817@7
content_role: Requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run.Coverage
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
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
