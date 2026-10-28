---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Author
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/caprmedio/Workflow//Implementation Workflow
version: 20
updated_at: 2026-10-27 19:59:57 +0400
relations:
  child_of:
  - CA-M-261
atom_id: CA-R-1559
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
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
