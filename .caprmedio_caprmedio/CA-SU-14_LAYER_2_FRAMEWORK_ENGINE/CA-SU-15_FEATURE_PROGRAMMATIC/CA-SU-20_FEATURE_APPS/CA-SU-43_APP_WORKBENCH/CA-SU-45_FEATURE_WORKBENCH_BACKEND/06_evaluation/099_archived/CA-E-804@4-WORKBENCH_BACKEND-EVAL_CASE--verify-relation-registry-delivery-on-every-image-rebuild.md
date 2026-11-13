---
identity:
  ref_id: CA-E-804@4
  id: CA-E-804
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ CFEL <+ Relation
  tier: 7
relations:
  evaluation_for:
  - CA-M-509
state:
  status: archived
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-804@4-WORKBENCH_BACKEND-EVAL_CASE--verify-relation-registry-delivery-on-every-image-rebuild.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation/099_archived
author: Anatoly Maslennikov
---
## Summary

Verify relation registry delivery on every image rebuild

## Claim

### Prose Claim

Verify every supported image-build entry point, including local release, generates the relation registry before image identity/context assembly. A selected Declaration change changes asset/build identity; identical inputs yield identical bytes. Record source IDs/versions/paths/fingerprints without changing timestamp, include asset/digest in staged package/image verification, and exclude Project authority carriers from image context.

A stale output regenerates; missing output or generation failure rejects the package/image rather than accepting stale metadata. Verify installed runtime consumes delivered metadata, and relevant Current Declaration change uses the same compiler to refresh Project registry/graph. MCP code/config tool registration stays separate from full Atom inventory scan. Use focused controlled build hooks plus one real selected-Project local-release check; generator success alone does not establish installed-image alignment.
