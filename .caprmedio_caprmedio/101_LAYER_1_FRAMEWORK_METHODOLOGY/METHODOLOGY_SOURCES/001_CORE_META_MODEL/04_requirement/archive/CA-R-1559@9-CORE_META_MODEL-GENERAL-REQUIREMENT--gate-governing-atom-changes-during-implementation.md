---
subjects:
  governs: 'Entity/Node/Continuant/Actor/Type: AI Agent'
  depends_on:
  - Entity/Node/Continuant/Atom.Author
  - 'Entity/Node/Continuant/Actor/Type: Operator'
  - 'Entity/Node/Continuant/Actor/Type: AI Agent'
  - AI Agent Confidence
  - 'Entity/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Spec
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Entity/Node/Continuant/Project
  - Implementation Workflow
version: 9
updated_at: 2026-10-23 03:06:32 +0400
relations: {"child_of":["CA-M-261"],"relates_to":["CA-R-1591","CA-R-1552","CA-R-1080","CA-M-262"]}
atom_id: CA-R-1559@9
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Gate governing Atom changes during implementation

## Scope

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

## Details
