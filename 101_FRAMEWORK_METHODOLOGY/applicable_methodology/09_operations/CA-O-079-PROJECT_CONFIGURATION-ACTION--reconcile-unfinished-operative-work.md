---
atom_id: CA-O-079
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Reconcile Unfinished Work"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Atom.Summary", "Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom/Content Role: Plan.Definition of Done", "Entity/Continuant/Object/Atom/Content Role: Plan.Status", "Entity/Continuant/Object/Atom/Content Role: Plan.Label", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom.Target Scope Unit", "Entity/Continuant/Object/Relation", "Entity/Continuant/History/Journal", "Entity/Continuant/History/Journal.Record", "Entity/Carrier", "Entity/Continuant/Actor/Type: Operator", "Entity/Occurrent/Execution/Workflow Run"]
version: 7
updated_at: "2026-10-18 07:47:18 +0400"
relations: {"relates_to": ["CA-R-1715", "CA-M-306", "CA-R-1574", "CA-R-1576", "CA-R-1577", "CA-R-1579", "CA-R-1580", "CA-R-1583", "CA-R-1599", "CA-R-1539", "CA-R-1464", "CA-D-461", "CA-D-470", "CA-D-481", "CA-R-1490", "CA-R-1720"]}
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-079-PROJECT_CONFIGURATION-ACTION--reconcile-unfinished-operative-work.md
  source_atom_id: CA-O-079
  source_atom_revision: 7
  source_sha256: eb82aff2c29515c3170939a67a71a5561e1a1bde2d9f4ddb57ea3af50bfac5e8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Reconcile unfinished operative work

## Operation

Reconcile Unfinished Work **means** the Action that reconciles still-valid remaining work with its applicable Plan representation under CA-R-1715, **without** duplicating existing Plans **or** authorizing execution of that work.

### Inputs and preconditions

- the selected work, its source context, available completion evidence, **and** the reason it remains unfinished.
- current relevant Plan Revisions, their Claims, Definitions of Done, Status values, decomposition, blocking Relations, **and** evidence references.
- applicable Scope Unit ownership, Claim Target Scope Unit, authoring rules, **and** authorization for the proposed Plan changes.

### Behavior

1. distinguish the still-valid remaining work from completed results, canceled work, obsolete requests, **and** uncertain completion claims. use available evidence; missing evidence is **not** proof of completion **or** permission **to** replay an effect.
2. find whether the remaining work is already represented by a Plan. check the originating Plan first **when** available, **then** other relevant Plans by Claim **and** applicability rather than Label **or** folder name. reuse an applicable existing Plan; **if** several competing representations remain unresolved, report them rather than create another duplicate.
3. reconcile necessary progress, remaining-work details, blockers, **and** source references within the authorized change. retain the existing Claim boundary **and** identity; a Summary change requires replacement under CA-R-1464. reference completed Plan Atoms **and** canonical Journal events using existing preservation authority CA-D-461, CA-R-1490, **and** CA-R-1720; do **not** copy those Atoms **or** historical events into another authoritative record.
4. **if** no applicable Plan represents still-valid work, create a Plan **only** within existing creation authority **and** under CA-M-306, CA-R-1599, **and** CA-D-470. select admitted Status **and** placement under CA-R-1539 **and** CA-D-461. use an explicitly justified `IS_DECOMPOSITION_OF` Relation under CA-D-481 **when** the work contributes required work **to** another Plan; a standalone Plan remains permitted. do **not** introduce a Version Plan **or** Change Plan authoring model merely from its Label.
5. retain explicit blocking under CA-R-1580 independently of decomposition **and** navigation order. do **not** silently reopen Done, Canceled, **or** Archived work, change another Plan's Status, **or** infer readiness from moving a Carrier. unresolved authority, applicability, validity, **or** destination selection remains a reported blocker.
6. **before** applying an authorized change, confirm the selected Plan Revisions remain current. apply **only** the bounded reconciliation, check its resulting references **and** Carrier placement, **and** record actual change events under the existing Journal authority. an already reconciled item is a no-change result, **not** another Plan **or** duplicate historical event.

### Results and effects

- reconciled: the existing **or** newly created Plan IDs, the remaining-work disposition, actual authorized changes **or** no-change result, **and** references **to** existing completion evidence.
- blocked: the preserved source context, unresolved item, relevant Plan IDs, missing evidence **or** authority, **and** the decision required from the Operator **when** current authority cannot settle it.
- failed: the exact completed **and** incomplete effects, recoverable evidence, **and** required recovery; do **not** report partial reconciliation as completion.

this Action maintains the representation of unfinished work. it does **not** execute that work, restart a Workflow Run, replay completed effects, mark the work Done, **or** introduce another completed-work preservation policy. resulting Plan Atoms remain subject **to** their existing Definition of Done, Status, authorization, **and** execution rules.

## Details
