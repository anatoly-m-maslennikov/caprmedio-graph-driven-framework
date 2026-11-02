---
subjects:
  governs: Entity/Object/Continuant/Actor/AI Agent
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Author
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/Actor/AI Agent
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Entity/Object/Continuant/Governing Objects/Atom
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow'
version: 23
updated_at: 2026-10-29 10:13:49 +0400
relations:
  child_of:
  - CA-M-261
atom_id: CA-R-1559@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
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
- a missing **or** unresolved Author **must not** be treated as proof of AI authorship; apply the Author default under CA-R-1080.
- an authorized RMED change establishes a new baseline under CA-M-262, **and** the applicable work **and** Evaluations **must** be resolved again against it.
