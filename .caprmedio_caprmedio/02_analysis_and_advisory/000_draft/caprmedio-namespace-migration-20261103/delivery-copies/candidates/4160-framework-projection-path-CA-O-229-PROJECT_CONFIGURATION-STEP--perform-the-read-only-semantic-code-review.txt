---
atom_id: CA-O-229
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
version: 14
updated_at: 2026-10-30 03:11:58 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-229-PROJECT_CONFIGURATION-STEP--perform-the-read-only-semantic-code-review.md
  source_atom_id: CA-O-229
  source_atom_revision: 14
  source_sha256: b39f13c761b84def0fd5a0a343465fc627c7abd7c61b21587e5280aa350d13c7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Perform the read-only semantic code review

## Operation

This Step invokes CA-O-238 in Isolated context only when that context is admitted. Bind candidate, owned paths, all actual Evaluation/diagnosis results, selected Plan or actual admitted in-session P/task with instruction/Definition of Done/source context, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project-owned Tier 0 Atoms, permissions, allowed commands, source revisions/hashes, report, and Run ID. An optional legacy `method_projection` may accompany direct rows but is not required.

Check evidence coverage and selected Method-policy compliance without restating policy. Map `implementation_defect` and `test_implementation_defect` to completed `findings`; map `authority_change_required`, `environment_blocker`, and `unresolved` to `unresolved` with actual results retained; report `expected_initial_failure` as an expected-phase observation and never accept the candidate unless admitted expected-phase criteria genuinely hold. Return `passed`, completed `findings`, `partial`, or `unresolved` according to CA-O-238.

## Details

No auto-fix, source/Atom edit, expected-result edit, retry, promotion, release, or Journal-completeness gate. Temporary fixture writes require explicit permission.
