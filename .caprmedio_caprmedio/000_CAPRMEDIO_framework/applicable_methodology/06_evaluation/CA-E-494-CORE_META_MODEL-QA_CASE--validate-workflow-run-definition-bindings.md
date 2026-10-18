---
subjects:
  governs: "Entity/Occurrent/Execution/Workflow Run"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Operations/Type: Workflow", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Occurrent/Execution/Step Run", "Entity/Continuant/Node/Atom", "Entity/Continuant/Node/History/Journal", "Entity/Continuant/Node/Actor/Type: Operator"]
version: 8
updated_at: "2026-10-18 03:34:28 +0400"
relations: {"evaluation_for": ["CA-R-1525"]}
atom_id: "CA-E-494"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-494-CORE_META_MODEL-QA_CASE--validate-workflow-run-definition-bindings.md
  source_atom_id: CA-E-494
  source_atom_revision: 8
  source_sha256: cc9232ab2d23929f7c0f65bbe990a7b010f5bc9ec782d4a9e1e529fe9743dd77
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate Workflow Run definition bindings

## Scope

a Workflow Run's declared definition bindings **and** revalidation evidence.

## Claim

the Evaluation **must** check a Workflow Run's declared definition bindings **and** revalidation evidence under CA-R-1525.

## Details

- a Run **and** its Step Runs identify their exact admitted Workflow graph, Step Atom, **and** Action Revisions: accept this binding evidence.
- change, withdraw, **or** make a bound definition unavailable **before** another dispatch **or** recovery: require a pause for revalidation, **not** silent use of a different Revision.
- provide a recorded revalidation that identifies admitted remaining-work bindings, checks compatibility with completed effects **and** inputs, **and** satisfies current authorization: admit continuation subject **to** remaining execution gates.
- supply missing compatibility evidence, revoked permission, **or** stale target inputs: keep the affected execution blocked even **if** definition binding is complete.
- revise a definition during an in-flight Action: retain the actual binding **and** outcome, follow the admitted interruption policy, **and** require revalidation **before** further dispatch.
- rewrite completed Step bindings, replay completed effects automatically, reset retries, **or** treat a recorded historical binding as continuing permission: reject.

these checks establish whether the binding evidence satisfies the model. a recorded assertion alone does **not** prove that an executor performed the required checks.
