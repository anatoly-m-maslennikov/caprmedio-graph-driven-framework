---
atom_id: CA-O-021
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Repair"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Implementation Failure Diagnosis", "Implementation Retry Control", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Actor/Type: AI Agent", "Spec", "Entity/Node/Continuant/Atom/Content Role: Evaluation", "Entity/Node/Continuant/Atom/Content Role: Method", "Implementation", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Continuant/Atom.Author", "Local Tier"]
version: 13
updated_at: "2026-10-19 15:56:42 +0400"
relations:
  relates_to:
    - CA-R-1559
    - CA-O-024
    - CA-O-089
    - CA-M-002
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-021-PROJECT_CONFIGURATION-ACTION--repair-nonconforming-implementation.md
  source_atom_id: CA-O-021
  source_atom_revision: 13
  source_sha256: 16b271b25a8090aec798a1b770c12c655f9ca8450c636901c0b0ff31590d825d
  original_relations_sha256: 85b3fa441ff283c248bb5de5680f9ffa0fa644b2825d092607c8ca13e09066d6
---
# Summary

Repair nonconforming Implementation

## Operation

Implementation Repair **means** the Agentic Action that repairs a diagnosed code defect within the admitted work boundary **and** retry allowance, preserving the issue **and** verification evidence.

- inputs: the diagnosed implementation **or** test-implementation defect, failed candidate, governing R/E/D, active Method Projection, selected P/Plan item, verification commands, retained issue evidence, **and** an admitted fix-and-evaluate retry.
- require evidence sufficient **to** explain the cause **and** correction. unresolved diagnosis, conflicting authority, unmet confidence, **or** missing permission returns `blocked`; retry allowance grants no extra authority.
- reproduce the issue with an appropriate targeted test **before** the fix **when** possible. reuse an existing reproducer; add unit, integration, **or** another focused test according **to** governing Methods. distinguish the actual defect from a setup failure.
- correct the code under existing authority **and** permissions. test code is Implementation too; do **not** weaken an Evaluation, expected output, Requirement, **or** Delivery obligation **to** obtain a pass.
- return `repaired` with the changed candidate, failure evidence, diagnosis, actual correction, tests, expected outcomes, **and** replay commands for re-evaluation. passing targeted checks do **not** replace any other check retained **in** the admitted Evaluation portfolio.
- do **not** create, update, **or** promote corrective M Atoms **in** this Action. retain evidence for the separate Method-learning Workflow; learning is **not** a condition for accepting a verified implementation fix.
- return `authority_change_required` **if** a governing RMED change is necessary, for disposition under CA-R-1559 **before** changing that authority. authorized baseline changes require renewed preparation; do **not** reset retry accounting.

## Details
