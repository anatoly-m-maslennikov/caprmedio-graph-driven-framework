---
subjects:
  governs: Entity/Object/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/History/Journal
  - Entity/Object/Continuant/Actor/Operator
version: 18
updated_at: 2026-10-29 07:17:23 +0400
relations:
  evaluation_for:
  - CA-R-1525
atom_id: CA-E-494@18
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary

Validate Workflow Run definition bindings

## Scope

a Workflow Run's declared definition bindings **and** revalidation evidence.

## Claim

the Evaluation **must** check a Workflow Run's declared definition bindings **and** revalidation evidence under CA-R-1525.

## Details

- a Workflow Run identifies its exact admitted Workflow graph, Step Atom, **and** Action Revisions; each Step Run identifies its exact Step Atom Revision. a leaf Step Run additionally identifies the exact Action Revision it launches; a containing Step Run groups its nested Step Runs without an own Action Revision. accept this binding evidence.
- change, withdraw, **or** make a bound definition unavailable **before** another dispatch **or** recovery: require a pause for revalidation, **not** silent use of a different Revision.
- provide a recorded revalidation that identifies admitted remaining-work bindings, checks compatibility with completed effects **and** inputs, **and** satisfies current authorization: admit continuation subject **to** remaining execution gates.
- supply missing compatibility evidence, revoked permission, **or** stale target inputs: keep the affected execution blocked even **if** definition binding is complete.
- revise a definition during an in-flight Action: retain the actual binding **and** outcome, follow the admitted interruption policy, **and** require revalidation **before** further dispatch.
- rewrite completed Step bindings, replay completed effects automatically, reset retries, **or** treat a recorded historical binding as continuing permission: reject.

these checks establish whether the binding evidence satisfies the model. a recorded assertion alone does **not** prove that an executor performed the required checks.
