---
subjects:
  governs: "Entity/Occurrent/Execution/Step Run.Invocation Context"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Occurrent/Execution/Step Run.Execution Context", "Entity/Continuant/Node/Atom", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/History/Journal"]
version: 5
updated_at: "2026-10-18 03:33:58 +0400"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1789"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1789-CORE_META_MODEL-GENERAL--provide-self-contained-agentic-step-invocation-payloads.md
  source_atom_id: CA-R-1789
  source_atom_revision: 5
  source_sha256: 35d35e95b9d758851dbb07140775f715035bc029505d98a367fb647be3db9fe9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Provide self-contained Agentic Step Invocation payloads

## Scope

an executor dispatching **or** resuming an Agentic Step.

## Claim

the executor **must** provide a self-contained Invocation sufficient for the receiving context **to** perform the admitted Action **without** remembering the Workflow procedure from earlier conversation.

- identify the Workflow Run **and** Step Run, exact admitted definition bindings, bound inputs **or** accessible references, relevant prior results **and** actual effects, applicable permissions, **and** required output.
- provide the instruction derived from the Action **and** its Step binding, including how **to** return the result **or** request missing input. the instruction is a derived presentation of governing authority, **not** another independently maintained procedure.
- an Integrated Invocation returns this context **and** instruction through the session interface; an Isolated Invocation supplies it **to** the separate context. no particular transport is required by this core rule.

## Details
