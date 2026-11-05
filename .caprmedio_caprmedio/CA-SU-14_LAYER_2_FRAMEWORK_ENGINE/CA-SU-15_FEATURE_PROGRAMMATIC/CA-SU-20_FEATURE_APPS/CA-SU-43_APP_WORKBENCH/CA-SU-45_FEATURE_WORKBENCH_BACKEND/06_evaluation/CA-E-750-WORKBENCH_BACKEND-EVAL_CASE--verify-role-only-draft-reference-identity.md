---
atom_id: CA-E-750
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 6
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  evaluation_for:
  - CA-C-700
  - CA-M-465
  - CA-R-2725
carrier_destination:
  file:
    name: CA-E-750-WORKBENCH_BACKEND-EVAL_CASE--verify-role-only-draft-reference-identity.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
updated_at: 2026-11-05 17:43:47 +0400
---

## Summary

Verify role-only Draft reference identity.

## Claim

### Prose Claim

When multiple role-only Draft carriers use the same Atom ID, source capture
preserves every carrier and keeps that Atom ID unchanged. Each carrier receives
a unique technical `ref` formed from the role-only ID and its project-relative
carrier path, and the derived Projection retains all of the carriers without a
duplicate technical reference.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Six lifecycle Draft carriers with `atom_id: CA-O-draft` under distinct paths | All six carriers remain in capture and materialization; each has a distinct `CA-O-draft:<relative path>` reference. |
| Numbered Draft and Current carriers | Their existing canonical references remain unchanged. |
