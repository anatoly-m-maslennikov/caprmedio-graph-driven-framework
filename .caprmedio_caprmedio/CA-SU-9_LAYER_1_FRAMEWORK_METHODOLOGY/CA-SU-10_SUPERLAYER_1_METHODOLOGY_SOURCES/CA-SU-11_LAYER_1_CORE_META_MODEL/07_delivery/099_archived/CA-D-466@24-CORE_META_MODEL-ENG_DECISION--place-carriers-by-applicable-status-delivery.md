---
atom_id: CA-D-466
ref_id: CA-D-466@24
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
tier: 3
status: Archived
version: 24
updated_at: '2026-11-11T17:45:31+04:00'
carrier_destination:
  file:
    name: CA-D-466@24-CORE_META_MODEL-ENG_DECISION--place-carriers-by-applicable-status-delivery.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Place Carriers by Applicable Status Delivery

## Claim

### Prose Claim


Carrier placement where an applicable qualified Artifact Status model exists or does not exist.


For a Current Atom, derive the Markdown Carrier directory from its logical Container.

- Scope Unit Container. Use `<scope unit>/<role number>_<role name lowercase>/` as the base directory.
- Atom Container. Use `<scope unit>/<role number>_<role name lowercase>/<container folder path>/` as the base directory. The Container folder path is relative to the Role folder and identifies the containing Atom's matching Directory Carrier.

Use the declared Role folder spelling. Place Active Atoms in the base directory. Append the applicable Status subfolder for other Current Statuses. Use the lowercase Status name when no specific subfolder spelling applies. For example, a Done Plan directly contained by a Scope Unit uses `<scope unit>/03_plan/done/`. A Canceled Plan in an Epic uses `<scope unit>/03_plan/<epic folder path>/canceled/`.

For other Artifacts, use the most specific applicable Delivery rule. Where a qualified Artifact Status model exists and no specific mapping applies, Active uses the canonical Current directory and another Status uses its lowercase Status subfolder. Where there is no qualified Status model, derive placement from the Artifact's Delivery rule. Legacy Carrier moves and rewrites require their own authorization.
