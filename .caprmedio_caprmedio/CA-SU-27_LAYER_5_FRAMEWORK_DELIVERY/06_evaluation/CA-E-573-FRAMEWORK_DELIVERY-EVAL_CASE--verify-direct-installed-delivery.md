---
atom_id: CA-E-573
ref_id: CA-E-573
container:
  scope_unit: CA-SU-27
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  - Subject/CAPRMEDIO/Carrier/Docker Image
tier: 5
relations:
  evaluation_for:
  - CA-R-1878
  - CA-M-332
  - CA-R-1692
status: active
version: 19
updated_at: '2026-11-12T17:06:44.343111+00:00'
carrier_destination:
  file:
    name: CA-E-573-FRAMEWORK_DELIVERY-EVAL_CASE--verify-direct-installed-delivery.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/06_evaluation
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Verify direct installed delivery

## Claim scope

The installed project runtime and `ca` Skill after a direct Local release.

## Claim

### Prose Claim

The QA case verifies the installed package/runtime and project-local `ca` Skill, then runs the intended Docker/MCP smoke behavior. A failed check stops the release and is reported for manual handling.

Check both image modes. Existing mode must build with the selected asset bytes and no usable predecessor. Refresh mode must generate the assets from the selected declarations and retain the generated files in the checkout. Check that Docker tests use the selected mode, and that missing assets in existing mode stop the release.

## Details

This case does not require a sealed manifest, a separate full-suite aggregation protocol or promotion state. Verify the exact admitted immutable candidate, package Version and canonical version/build-date/digest tag using the existing runtime evidence.

Use independent synthetic Projects and Docker observations to check: a green full suite precedes release-image preparation on every Local Release route; failed suite or preparation causes no startup/image removal; cleanup requires verified exact candidate launch even with no prior image; retain that candidate and exactly one verified prior image when available. An unused, fully selected-Project-owned older rebuild is removable even with the same fingerprint. A same-fingerprint but different-image exact prior Project MCP is replaced by the existing ownership-checked path, while exact candidate reuse remains allowed. Foreign, unowned, incomplete/conflicting ownership, running containers outside that path, and images referenced by any container are preserved. Cover failed observation/removal, pending reporting, no force/global prune and no uncertain retry. These functional checks do not authorize an actual release or production Docker effects.



Verify that the selected Version remains mutable before the authorized release event succeeds and its exact candidate outcome is recorded. Readiness, implementation completion and candidate naming alone do not freeze it. A failed or unrecorded release does not count as the successful release event.
