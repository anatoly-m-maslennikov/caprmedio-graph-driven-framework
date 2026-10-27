---
atom_id: CA-P-1831
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Occurrent/Runtime/Docker Runtime
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1832
tier: 3
---
# Summary

Specify image admission **and** runtime startup

## Objective

the AI Agent defines one admitted startup operation for the selected CAPRMEDIO Framework Instance, including compatible-image selection **and** healthy-runtime reuse.

## Details

- input: the reviewed Project-selection contract **and** current Docker **and** HTTP RMED.
- output: reviewed source RMED **and** a bounded O Action for explicit launcher invocation. specify immutable image admission, build **if** missing, Docker-owned loopback port allocation, same-Project serialization, matching healthy-runtime reuse, **and** truthful mismatch/failure outcomes.
- verification: amend the existing explicit-port Delivery constraint rather than create conflicting authority; distinguish endpoint startup from Workflow execution **and** worker startup.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: R1901, M356, E600, D594 **and** amended D578; independent launcher_security review passed immutable-image, missing-build, lock/reuse, Docker publication, credentials **and** endpoint-only boundaries.

the Plan is **not** Done **if** ((image compatibility **or** startup effects have an unspecified admission boundary) **or** (automatic port allocation conflicts with retained Delivery authority) **or** (the O Action can replay a queue **or** replace a healthy runtime **without** explicit authorization)).
