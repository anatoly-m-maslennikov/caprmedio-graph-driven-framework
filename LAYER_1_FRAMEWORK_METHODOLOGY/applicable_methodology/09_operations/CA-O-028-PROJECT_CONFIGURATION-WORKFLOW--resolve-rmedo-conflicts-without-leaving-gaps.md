---
subjects:
  governs: Subject/caprmedio/Workflow//RMEDO Conflict Resolution
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Updated At
  - Subject/CAPRMEDIO/Graph/Relation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 27
updated_at: 2026-10-29 22:26:57 +0400
relations: {}
atom_id: CA-O-028
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Workflow
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-028-PROJECT_CONFIGURATION-WORKFLOW--resolve-rmedo-conflicts-without-leaving-gaps.md
  source_atom_id: CA-O-028
  source_atom_revision: 27
  source_sha256: 642e6f34c6d86e02ba84d03c691b2b6a3561e91efd1ecb09706baebbfb08b173
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
| select | CA-O-004 | the selected active RMEDO Atoms, applicable Atoms expressing applicable Project-wide foundational commitments, **and** affected authority |
| assess | CA-O-005 | the exact selected frontier **and** required conflict **and** coverage checks |
| propose | CA-O-006 | identified conflicts **or** gaps, applicable Atoms expressing applicable Project-wide foundational commitments, **and** permitted correction boundaries |
| decide | CA-O-007 | the exact proposal, current frontier, **and** unresolved decision **or** authorization |
| correct | CA-O-008 | the gap-free correction **and** its valid exact authorization for the current frontier |

### Transitions

the transitions below are declared in this Workflow's Step structure; result-based routing belongs to the applicable Conditional Step definition **when** the destination is a Step. a terminal outcome ends the Workflow Run; it is **not** another Step **or** Action.

| Step **and** Action reference | Result condition | Next Step **or** outcome |
|---|---|---|
| select — CA-O-004 | exact active RMEDO selection, applicable Atoms expressing applicable Project-wide foundational commitments, **and** affected authority identified | assess |
| select — CA-O-004 | incomplete **or** ambiguous selection | stop **and** ask the Operator |
| assess — CA-O-005 | complete checks; no unresolved conflict **or** affected coverage gap | complete |
| assess — CA-O-005 | conflict **or** gap has a supported correction route | propose |
| assess — CA-O-005 | conflicting active Atoms expressing applicable Project-wide foundational commitments, insufficient confidence, **or** unresolved authority | stop **and** ask the Operator |
| propose — CA-O-006 | exact gap-free correction ready; existing Operator delegation covers **every** action; effective confidence threshold met; no stricter approval gate | correct |
| propose — CA-O-006 | a concrete decision **or** authorization is still needed | decide |
| propose — CA-O-006 | coverage cannot be preserved **or** no supported correction exists | stop **and** ask the Operator |
| decide — CA-O-007 | valid authorization for the exact proposal **and** current frontier | correct |
| decide — CA-O-007 | requested proposal revision within admitted retry bounds | propose |
| decide — CA-O-007 | rejection, missing decision, invalid authorization, **or** exhausted retry allowance | stop; preserve the unresolved finding |
| correct — CA-O-008 | authorized correction completed, including **any** qualified archival | select **and** reassess the changed frontier |
| correct — CA-O-008 | failed **or** partial correction | stop **and** report actual effects **and** remaining gaps |

- **before** asking for a decision, use current active authority **and** Atoms expressing applicable Project-wide foundational commitments **to** resolve what is already settled.
- archive an obsolete conflicting Atom **when** removal improves applicable Project-wide foundational commitments alignment, CA-O-006's no-gap conditions hold, **and** the mutation is authorized. an already valid delegation does **not** require repeated per-Atom approval.
- use the effective Autonomous Confidence Threshold **and** accepted retry bounds from governing sources; this Workflow **must not** hard-code a percentage, reset a retry budget through reselection, **or** widen delegated scope.
- completion requires the selected conflicts resolved, **all** affected still-required Claims covered, valid active references **and** Relations, preserved required Evaluations, recoverable archival history, **and** no new applicable Project-wide foundational commitments conflict. an unperformed check **or** unresolved gap is **not** success.

## Details
