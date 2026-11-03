---
atom_id: CA-O-226
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 12
updated_at: 2026-10-29 22:26:57 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-226-PROJECT_CONFIGURATION-STEP--bind-one-exact-code-candidate-and-review-boundary.md
  source_atom_id: CA-O-226
  source_atom_revision: 12
  source_sha256: f0c021318cda8e7aca9ffe69850fba601866b55b0dfbe4c9a14693de74b9feae
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Bind one exact code candidate and review boundary

## Operation

This Step invokes CA-O-224 in Integrated context. Bind candidate digest, owned paths, either an existing Plan or an actually admitted in-session P/task with instruction, Definition of Done, and source context, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project-owned Tier 0 Atoms, permissions, allowed commands, context authority, source revisions/hashes, report, and Run ID. An optional legacy `method_projection` may accompany direct rows but is not required.

Return the Action's `bound` or `blocked` result unchanged. Missing Plan/P-task content is blocked. No hidden next Step, retry, candidate substitution, Plan fabrication, or source edit.

## Details

The Step performs boundary inspection only and has no mutation authority.
