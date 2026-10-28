---
atom_id: CA-O-079
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Action//Reconcile Unfinished Work
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Definition of Done'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Status'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Label'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
version: 20
updated_at: 2026-10-27 19:59:45 +0400
relations: {}
tier: 3
---
# Summary

Reconcile unfinished operative work

## Operation

Reconcile Unfinished Work **means** the Action that reconciles still-valid remaining work with its applicable Plan representation under CA-R-1715, **without** duplicating existing Plans **or** authorizing execution of that work.

### Inputs and preconditions

- the selected work, its source context, available completion evidence, **and** the reason it remains unfinished.
- current relevant Plan Revisions, their Claims, Definitions of Done, Status values, Plan containment, blocking Relations, **and** evidence references.
- applicable Scope Unit ownership, Claim Target Scope Unit, authoring rules, **and** authorization for the proposed Plan changes.

### Behavior

1. distinguish the still-valid remaining work from completed results, canceled work, obsolete requests, **and** uncertain completion claims. use available evidence; missing evidence is **not** proof of completion **or** permission **to** replay an effect.
2. find whether the remaining work is already represented by a Plan. check the originating Plan first **when** available, **then** other relevant Plans by Claim **and** applicability rather than Label **or** folder name. reuse an applicable existing Plan; **if** several competing representations remain unresolved, report them rather than create another duplicate.
3. reconcile necessary progress, remaining-work details, blockers, **and** source references within the authorized change. retain the existing Claim boundary **and** identity; a Summary change requires replacement under CA-R-1464. reference completed Plan Atoms **and** canonical Journal events using existing preservation authority CA-D-461, CA-R-1490, **and** CA-R-1720; do **not** copy those Atoms **or** historical events into another authoritative record.
4. **if** no applicable Plan represents still-valid work, create a Plan **only** within existing creation authority **and** under CA-M-306, CA-R-1599, **and** CA-D-470. select admitted Status **and** placement under CA-R-1539 **and** CA-D-461. use an explicitly justified `IS_CONTAINED_BY` connection on the child Plan **when** the work belongs under another Plan; derive `CONTAINS`; a standalone Plan remains permitted. do **not** introduce a Version Plan **or** Change Plan authoring model merely from its Label.
5. retain explicit blocking under CA-R-1580 independently of Plan containment **and** navigation order. do **not** silently reopen Done, Canceled, **or** Archived work, change another Plan's Status, **or** infer readiness from moving a Carrier. unresolved authority, applicability, validity, **or** destination selection remains a reported blocker.
6. **before** applying an authorized change, confirm the selected Plan Revisions remain current. apply **only** the bounded reconciliation, check its resulting references **and** Carrier placement, **and** record actual change events under the existing Journal authority. an already reconciled item is a no-change result, **not** another Plan **or** duplicate historical event.

### Results and effects

- reconciled: the existing **or** newly created Plan IDs, the remaining-work disposition, actual authorized changes **or** no-change result, **and** references **to** existing completion evidence.
- blocked: the preserved source context, unresolved item, relevant Plan IDs, missing evidence **or** authority, **and** the decision required from the Operator **when** current authority cannot settle it.
- failed: the exact completed **and** incomplete effects, recoverable evidence, **and** required recovery; do **not** report partial reconciliation as completion.

this Action maintains the representation of unfinished work. it does **not** execute that work, restart a Workflow Run, replay completed effects, mark the work Done, **or** introduce another completed-work preservation policy. resulting Plan Atoms remain subject **to** their existing Definition of Done, Status, authorization, **and** execution rules.

## Details
