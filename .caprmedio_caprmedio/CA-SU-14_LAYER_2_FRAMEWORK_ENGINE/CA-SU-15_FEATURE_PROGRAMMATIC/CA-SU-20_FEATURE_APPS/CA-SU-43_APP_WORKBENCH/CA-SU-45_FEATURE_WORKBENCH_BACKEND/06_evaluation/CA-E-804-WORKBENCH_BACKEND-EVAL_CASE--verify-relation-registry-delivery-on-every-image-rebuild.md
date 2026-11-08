---
identity:
  ref_id: CA-E-804
  id: CA-E-804
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  tier: 7
relations:
  evaluation_for:
  - CA-M-509
  - CA-D-705
state:
  status: Active
  version: 1
  updated_at: 2026-11-08 20:06:37 +0400
destination:
  file:
    name: CA-E-804-WORKBENCH_BACKEND-EVAL_CASE--verify-relation-registry-delivery-on-every-image-rebuild.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
author: Anatoly Maslennikov
---

## Summary

Verify relation registry delivery on every image rebuild

## Claim

### Prose Claim

Verify the generated relation registry on every supported image-build entry point, including local release:

- Generate before computing image identity and assembling its context. Changing a selected Declaration changes the generated asset and its recorded build identity.
- Identical selected inputs produce identical bytes. Record the selected source Atom IDs, versions, paths and fingerprints without a changing timestamp in the fingerprint.
- Include the asset and its digest in the staged package and image verification. Do not include Project authority carriers in the image context.
- A stale output is regenerated. A missing output or generator failure prevents acceptance of that build or package rather than accepting the stale asset.
- Verify the installed runtime consumes the delivered metadata. A later relevant Current Declaration change uses the same compiler and refreshes the selected Project's registry and graph.
- Keep the code/config MCP tool registry separate. Registering MCP tools does not scan the Project's full Atom inventory.

Run focused build-hook checks with controlled inputs and one local-release check with the real selected Project. Record the installed release, source registry fingerprint and observed relation-query results. A successful generator test alone does not prove the installed image is aligned.
