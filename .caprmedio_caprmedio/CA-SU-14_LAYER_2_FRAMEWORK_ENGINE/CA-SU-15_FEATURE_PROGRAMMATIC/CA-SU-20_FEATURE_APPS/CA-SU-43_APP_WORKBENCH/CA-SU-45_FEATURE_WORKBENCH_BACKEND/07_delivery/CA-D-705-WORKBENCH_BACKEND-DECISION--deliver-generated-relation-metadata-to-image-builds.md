---
identity:
  ref_id: CA-D-705
  id: CA-D-705
context:
  container:
    scope_unit: CA-SU-45
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  tier: 6
relations:
  delivery_for:
  - CA-R-2724
  depends_on:
  - CA-M-509
state:
  status: Active
  version: 1
  updated_at: 2026-11-08 20:06:37 +0400
destination:
  file:
    name: CA-D-705-WORKBENCH_BACKEND-DECISION--deliver-generated-relation-metadata-to-image-builds.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery
author: Anatoly Maslennikov
---

## Summary

Deliver generated relation metadata to image builds

## Claim

### Prose Claim

Deliver the relation registry as a deterministic JSON asset. Keep declared names, unqualified inverse bindings, inverse aliases, and source Atom IDs, versions, paths and fingerprints. Do not include a changing generation timestamp in the fingerprint. Identical selected inputs produce identical bytes.

Provide one generator with an explicit selected Project root and output path. Generate the asset before computing the image fingerprint and assembling the build context on every supported image-build path, including local release. Local release also includes and verifies the asset in its staged package, alongside the existing code-owned tool registry. Do not use the post-start discovery catalog as an input.

Include only the generated metadata asset and its digest in the build context and image identity. Project authority files remain outside the image context. A missing or failed required generation prevents that image/package from being accepted; it is not silently replaced by a handwritten or stale list.

At runtime, use the selected Project's admitted declaration capture and the same compiler when relevant declarations change. Reuse existing owner synchronization and derived-asset storage. Keep MCP tool discovery's code/config registry separate; do not restore startup scans of all source Atoms just to register MCP tools.

## Details

The existing image/package identity verification covers the generated asset. Registry metadata does not add a source table, a second source of truth, a scheduler or a service.
