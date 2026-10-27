---
atom_id: CA-P-1838
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Image
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1839
tier: 3
---
# Summary

Implement compatible image selection

## Objective

the AI Agent implements the accepted image-compatibility check for the requested Framework runtime.

## Details

- input: the image RMED, image golden tests, **and** `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/image_reference.py`.
- output: one resolver that distinguishes image absence from an incompatible existing image, checks the accepted runtime/source identity, **and** returns an immutable admitted image ID.
- verification: prove compatible reuse, stale-source handling, unknown identity, **and** explicit image selection; a familiar mutable tag alone is insufficient evidence.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: strict immutable-image resolution **and** source fingerprinting are implemented; the resolver-only golden tests passed with exact OS/architecture admission. Build behavior remains the next Task.

the Plan is **not** Done **if** ((tag existence alone admits an image) **or** (the selected image identity is mutable **or** ambiguous) **or** (the image-admission tests fail)).
