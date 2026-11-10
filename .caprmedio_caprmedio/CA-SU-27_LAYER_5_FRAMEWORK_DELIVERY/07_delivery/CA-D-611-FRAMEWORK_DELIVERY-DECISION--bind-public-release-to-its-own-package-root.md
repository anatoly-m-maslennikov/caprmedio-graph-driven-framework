---
atom_id: CA-D-611
ref_id: CA-D-611
container:
  scope_unit: CA-SU-27
role: Delivery
form: Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Carrier
tier: 4
relations:
  delivery_for:
  - CA-R-1921
status: Active
version: 15
updated_at: 2026-11-11 00:17:19 +0400
carrier_destination:
  file:
    name: CA-D-611-FRAMEWORK_DELIVERY-DECISION--bind-public-release-to-its-own-package-root.md
    path: .caprmedio_caprmedio/CA-SU-27_LAYER_5_FRAMEWORK_DELIVERY/07_delivery
current_scope_unit: FRAMEWORK_DELIVERY
claim_target_scope_unit: FRAMEWORK_DELIVERY
author: Anatoly Maslennikov
---

# Summary

Bind public release to its own package root

## Scope

the installed-source root of the public-release Tool.

## Claim

the public-release Tool **must** retain `LAYER_5_FRAMEWORK_DELIVERY/PUBLIC_RELEASE/` as its own installed package-relative root and resolve sibling `RELEASE_VERSION` evidence through the selected installed Framework package.

## Details

The rule does not alter `.caprmedio_install/releases/<digest>/manifest.toml`, `.caprmedio_install/current.toml`, or a Project runtime selection carrier; their owning installation authority remains separate.
