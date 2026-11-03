---
subjects:
  active: Entity/Object/Continuant/Actor/AI Agent
  passive:
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
  - Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Atom
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Atom/(.Role := Evaluation)
  - Atom/(.Role := Requirement)
  - Atom/(.Role := Method)
  - Atom/(.Role := Delivery)
  - Project
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow'
version: 26
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-261
atom_id: CA-R-1559
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1559-CORE_META_MODEL-RULE--gate-governing-atom-changes-during-implementation.md
  source_atom_id: CA-R-1559
  source_atom_revision: 26
  source_sha256: d725038d59d218fd21b8370d5dd74a6dcc03ee0ca521f7841ac84b3896d618b2
  original_relations_sha256: 94899af1df3add3533bb824b693365050895abf0a071adfe4339109a042cf4cb
---
## Summary

Gate governing Atom changes during implementation

## Claim scope

changes to governing RMED Atoms during implementation.

## Claim

authorization **to** change a governing RMED Atom during implementation **must** satisfy the following Actor policy:

- resolve the Atom's effective Author **before** the proposed change, its governing permissions, the effective Plan Autonomous Confidence Threshold under CA-R-1591, **and** **all** additional Operator rules.
- obtain Operator approval **before** changing an Operator-authored Atom.
- request Operator disposition **before** changing an AI-authored Atom **when** confidence is below the threshold **or** an additional rule requires approval.
- an AI-authored Atom **may** change autonomously **only** **when** confidence is at **or** above the threshold **and** **all** applicable permissions **and** Operator rules allow it.
- a prohibition remains a prohibition; authorship **or** confidence **must not** create permission.
- a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080@29.
- an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.
