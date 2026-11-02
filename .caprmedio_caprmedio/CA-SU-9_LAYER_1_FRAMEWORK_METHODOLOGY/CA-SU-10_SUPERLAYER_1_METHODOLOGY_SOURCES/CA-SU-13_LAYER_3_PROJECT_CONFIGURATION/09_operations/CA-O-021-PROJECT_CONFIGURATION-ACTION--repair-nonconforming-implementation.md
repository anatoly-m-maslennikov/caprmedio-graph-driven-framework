---
atom_id: CA-O-021
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Action//Implementation Repair
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/caprmedio/Action//Implementation Failure Diagnosis
  - Subject/caprmedio/Action//Implementation Retry Control
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Failure Handling
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Author
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
version: 25
updated_at: 2026-10-27 19:59:44 +0400
relations: {}
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
