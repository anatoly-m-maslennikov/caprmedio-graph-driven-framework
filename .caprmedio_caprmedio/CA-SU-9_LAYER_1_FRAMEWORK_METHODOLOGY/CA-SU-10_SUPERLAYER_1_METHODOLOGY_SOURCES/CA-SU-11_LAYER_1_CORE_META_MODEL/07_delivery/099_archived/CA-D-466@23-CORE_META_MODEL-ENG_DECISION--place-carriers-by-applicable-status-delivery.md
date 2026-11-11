---
atom_id: CA-D-466
ref_id: CA-D-466@23
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
version: 23
updated_at: '2026-11-11 15:27:11 +0400'
carrier_destination:
  file:
    name: CA-D-466@23-CORE_META_MODEL-ENG_DECISION--place-carriers-by-applicable-status-delivery.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Place Carriers by Applicable Status Delivery

## Claim

### Prose Claim


Carrier placement where an applicable qualified Artifact Status model exists or does not exist.


**when** an Atom has Draft or Archived Status, place its Markdown Carrier in the owning Scope Unit’s shared Content Role `draft` or `archived` directory respectively, regardless of its logical container. For a Current Atom, place its Carrier locally in its actual container according to its applicable Status mapping; CA-D-461 retains its stated boundary for root Plan terminal Statuses. **when** an applicable qualified Artifact Status model exists for another Artifact, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more-specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** no applicable qualified Status model exists, Carrier placement **must not** derive a Status directory from absent Status. These placement rules do not authorize independent legacy moves or rewrites.
