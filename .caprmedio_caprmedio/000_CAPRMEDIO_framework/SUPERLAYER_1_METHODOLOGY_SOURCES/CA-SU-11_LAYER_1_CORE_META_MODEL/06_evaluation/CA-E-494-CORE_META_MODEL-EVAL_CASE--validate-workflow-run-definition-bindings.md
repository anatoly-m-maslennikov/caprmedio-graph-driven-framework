---
atom_id: CA-E-494
ref_id: CA-E-494
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 3
relations:
  evaluation_for:
  - CA-R-1525
status: Active
version: 20
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-494-CORE_META_MODEL-EVAL_CASE--validate-workflow-run-definition-bindings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Validate Workflow Run definition bindings

## Claim

### Prose Claim


a Workflow Run's declared definition bindings **and** revalidation evidence.


the Evaluation **must** check a Workflow Run's declared definition bindings **and** revalidation evidence under CA-R-1525.

## Details

- a Workflow Run identifies its exact admitted Workflow graph, Step Atom, **and** Action Revisions; each Step Run identifies its exact Step Atom Revision. a leaf Step Run additionally identifies the exact Action Revision it launches; a containing Step Run groups its nested Step Runs without an own Action Revision. accept this binding evidence.
- change, withdraw, **or** make a bound definition unavailable **before** another dispatch **or** recovery: require a pause for revalidation, **not** silent use of a different Revision.
- provide a recorded revalidation that identifies admitted remaining-work bindings, checks compatibility with completed effects **and** inputs, **and** satisfies current authorization: admit continuation subject **to** remaining execution gates.
- supply missing compatibility evidence, revoked permission, **or** stale target inputs: keep the affected execution blocked even **if** definition binding is complete.
- revise a definition during an in-flight Action: retain the actual binding **and** outcome, follow the admitted interruption policy, **and** require revalidation **before** further dispatch.
- rewrite completed Step bindings, replay completed effects automatically, reset retries, **or** treat a recorded historical binding as continuing permission: reject.

these checks establish whether the binding evidence satisfies the model. a recorded assertion alone does **not** prove that an executor performed the required checks.
