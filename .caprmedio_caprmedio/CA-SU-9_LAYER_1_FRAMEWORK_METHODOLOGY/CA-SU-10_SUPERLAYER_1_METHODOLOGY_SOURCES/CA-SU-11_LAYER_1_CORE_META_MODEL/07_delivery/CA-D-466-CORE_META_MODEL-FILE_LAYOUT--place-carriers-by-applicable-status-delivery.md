---
atom_id: CA-D-466
ref_id: CA-D-466
container:
  scope_unit: CA-SU-11
role: Delivery
form: file_layout
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom.Header.State.Status >| Status Group := Current'
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
tier: 3
status: Active
version: 27
updated_at: '2026-11-11T19:34:00+04:00'
carrier_destination:
  file:
    name: CA-D-466-CORE_META_MODEL-FILE_LAYOUT--place-carriers-by-applicable-status-delivery.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Place Carriers by Applicable Status Delivery

## Claim

### Prose Claim

Resolve the Current Atom's base directory from its logical Container.

- Scope Unit Container. Use the Atom's Role folder in that Scope Unit.
- Atom Container. Use the containing Atom's matching directory.

Place Active Atoms directly in the base directory. Place other Current Atoms in the derived Status folder within that base.

For other Artifacts, use the most specific applicable Delivery rule. Where a qualified Artifact Status model exists and no specific mapping applies, Active uses the canonical Current directory and another Status uses its lowercase Status subfolder. Where there is no qualified Status model, derive placement from the Artifact's Delivery rule.

### Formal Claim

```CFEL
# model
Atom/(.Header.State.Status >| Status Group = Current).Header.Destination.File.Path == PATH_TEMPLATE("<container>/<status folder>");
Atom/(.Header.State.Status := Active).Header.Destination.File.Path == PATH_TEMPLATE("<container>");
```
