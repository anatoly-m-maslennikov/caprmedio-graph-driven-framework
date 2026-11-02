---
atom_id: CA-O-021@19
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Implementation Repair
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Implementation Failure Diagnosis'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Implementation Retry Control'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - 'Subject/Domain/Node/Continuant/Actor/Type: AI Agent'
  - Spec
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - Subject/Engineering/Implementation Reconstructability
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Domain/Node/Continuant/Atom.Author
  - Subject/Domain/Node/Continuant/Atom.Tier
version: 19
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-R-1559
  - CA-O-024
  - CA-O-089
  - CA-M-002
tier: 3
---
# Summary

Repair nonconforming Implementation

## Operation

Implementation Repair **means** the Agentic Action that repairs a diagnosed code defect within the admitted work boundary **and** retry allowance, preserving the issue **and** verification evidence.

- inputs: the diagnosed implementation **or** test-implementation defect, failed candidate, governing R/E/D, direct full `methods` rows, selected P/Plan item, verification commands, retained issue evidence, **and** an admitted fix-and-evaluate retry. An optional legacy `method_projection` may accompany those rows but is not required.
- require evidence sufficient **to** explain the cause **and** correction. unresolved diagnosis, conflicting authority, unmet confidence, **or** missing permission returns `blocked`; retry allowance grants no extra authority.
- reproduce the issue with an appropriate targeted test **before** the fix **when** possible. reuse an existing reproducer; add unit, integration, **or** another focused test according **to** governing Methods. distinguish the actual defect from a setup failure.
- correct the code under existing authority **and** permissions. test code is Implementation too; do **not** weaken an Evaluation, expected output, Requirement, **or** Delivery obligation **to** obtain a pass.
- return `repaired` with the changed candidate, failure evidence, diagnosis, actual correction, tests, expected outcomes, **and** replay commands for re-evaluation. passing targeted checks do **not** replace any other check retained **in** the admitted Evaluation portfolio.
- do **not** create, update, **or** promote corrective M Atoms **in** this Action. retain evidence for the separate Method-learning Workflow; learning is **not** a condition for accepting a verified implementation fix.
- return `authority_change_required` **if** a governing RMED change is necessary, for disposition under CA-R-1559 **before** changing that authority. authorized baseline changes require renewed preparation; do **not** reset retry accounting.

- confirmed semantic-review findings may supply the defect evidence without fabricating a failing test. On every correction retain the changed candidate and invalidated affected review/check bindings; route back through preparation for preliminary review, required final checks, and final review. One shared finite retry/resource/confidence state survives all such revisits.

## Details
