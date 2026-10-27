---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//RMEDO Conflict Resolution'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Atom.Updated At
  - Subject/Graph Relation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 25
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-O-028
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Workflow
tier: 3
---
# Summary

Resolve RMEDO conflicts without leaving gaps

## Operation

RMEDO Conflict Resolution **means** the Workflow that resolves conflicts among selected active Requirement, Method, Evaluation, Delivery, **and** Operations Atoms **without** leaving gaps **in** affected authority.

the Workflow reuses the following Actions through its Steps. it **must not** replace their definitions **or** require a Projection publication **to** resolve source authority.

the entry Step is select. interpret Step bindings **and** run boundaries under CA-R-1509, CA-R-1510, **and** CA-R-1511.

### Steps

| Step | Action reference | Parameters **and** inputs |
|---|---|---|
| select | CA-O-004 | the selected active RMEDO Atoms, applicable Principles, **and** affected authority |
| assess | CA-O-005 | the exact selected frontier **and** required conflict **and** coverage checks |
| propose | CA-O-006 | identified conflicts **or** gaps, applicable Principles, **and** permitted correction boundaries |
| decide | CA-O-007 | the exact proposal, current frontier, **and** unresolved decision **or** authorization |
| correct | CA-O-008 | the gap-free correction **and** its valid exact authorization for the current frontier |

### Transitions

the transitions below are declared in this Workflow's Step structure; result-based routing belongs to the applicable Conditional Step definition **when** the destination is a Step. a terminal outcome ends the Workflow Run; it is **not** another Step **or** Action.

| Step **and** Action reference | Result condition | Next Step **or** outcome |
|---|---|---|
| select — CA-O-004 | exact active RMEDO selection, applicable Principles, **and** affected authority identified | assess |
| select — CA-O-004 | incomplete **or** ambiguous selection | stop **and** ask the Operator |
| assess — CA-O-005 | complete checks; no unresolved conflict **or** affected coverage gap | complete |
| assess — CA-O-005 | conflict **or** gap has a supported correction route | propose |
| assess — CA-O-005 | conflicting active Principles, insufficient confidence, **or** unresolved authority | stop **and** ask the Operator |
| propose — CA-O-006 | exact gap-free correction ready; existing Operator delegation covers **every** action; effective confidence threshold met; no stricter approval gate | correct |
| propose — CA-O-006 | a concrete decision **or** authorization is still needed | decide |
| propose — CA-O-006 | coverage cannot be preserved **or** no supported correction exists | stop **and** ask the Operator |
| decide — CA-O-007 | valid authorization for the exact proposal **and** current frontier | correct |
| decide — CA-O-007 | requested proposal revision within admitted retry bounds | propose |
| decide — CA-O-007 | rejection, missing decision, invalid authorization, **or** exhausted retry allowance | stop; preserve the unresolved finding |
| correct — CA-O-008 | authorized correction completed, including **any** qualified archival | select **and** reassess the changed frontier |
| correct — CA-O-008 | failed **or** partial correction | stop **and** report actual effects **and** remaining gaps |

- **before** asking for a decision, use current active authority **and** Principles **to** resolve what is already settled.
- archive an obsolete conflicting Atom **when** removal improves Principle alignment, CA-O-006's no-gap conditions hold, **and** the mutation is authorized. an already valid delegation does **not** require repeated per-Atom approval.
- use the effective Autonomous Confidence Threshold **and** accepted retry bounds from governing sources; this Workflow **must not** hard-code a percentage, reset a retry budget through reselection, **or** widen delegated scope.
- completion requires the selected conflicts resolved, **all** affected still-required Claims covered, valid active references **and** Relations, preserved required Evaluations, recoverable archival history, **and** no new Principle conflict. an unperformed check **or** unresolved gap is **not** success.

## Details
