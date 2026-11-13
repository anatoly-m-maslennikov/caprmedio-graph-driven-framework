---
atom_id: CA-D-564
ref_id: CA-D-564
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
tier: 6
relations:
  delivery_for:
  - CA-M-332
  - CA-E-573
status: active
version: 20
updated_at: '2026-11-12T17:09:54.081558+00:00'
carrier_destination:
  file:
    name: CA-D-564-FRAMEWORK_DELIVERY-DECISION--carry-project-owned-docker-image-cleanup.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---
## Summary

Carry project-owned Docker image cleanup

## Claim scope

Direct Docker/MCP smoke for the installed project runtime and cleanup of superseded project-owned images.

## Claim

### Prose Claim

After a green full suite and successful installed Docker/MCP smoke, delivery retains the exact admitted candidate of the current package Version and one known-good previous Project image, when available. It removes other eligible images only when they are positively identified as owned by the selected Project and unused by any container. It never prunes broadly, removes an unrelated image, or forces container deletion.

## Details

Canonical image names carry the exact framework Version, actual Docker build date in UTC and digest suffix; they never replace immutable admission or establish ownership. Ownership requires matching inspected Project identity, host Project root and control root together with positive runtime schema/fingerprint classification; a container link is insufficient. Use actual prior runtime evidence to select the rollback image. Matching Version or fingerprint alone does not earn retention. Preserve other Projects' images, unknown or conflicting ownership and every container reference, including stopped containers. Report the exact kept candidate, removed IDs and retained reasons with truthful pending failures; never force, prune or retry uncertain effects. Build output alone does not prove a working runtime.
