---
identity:
  atom_id: CA-E-750
  ref_id: CA-E-750
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Source Retrieval
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 6
relations:
  evaluation_for:
  - CA-C-700
  - CA-M-465
  - CA-R-2725
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-750-WORKBENCH_BACKEND-EVAL_CASE--verify-role-only-draft-reference-identity.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Verify role-only Draft reference identity.

## Claim

### Prose Claim

When multiple role-only Draft carriers use the same Atom ID, preserve every carrier and keep that ID unchanged. Give each a unique technical reference formed from the role-only ID plus project-relative carrier path; retain all without a duplicate reference. Verify six `CA-O-draft` lifecycle carriers under distinct paths, while numbered Draft and Current canonical references remain unchanged.
