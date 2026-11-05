---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/Directory
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Carrier/Directory
version: 30
updated_at: 2026-11-05 06:15:15 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-D-264
status: Draft
tier: 3
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-264@30-draft-CORE_META_MODEL-DECISION--derive-direct-containment-from-the-nearest-directory-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/draft
---
## Summary

Derive Direct Containment from the Nearest Directory Carrier

## Claim

### Prose Claim

For an Atom whose `Header.Container` resolves to a Scope Unit or an Atom, derive the direct `IS_CONTAINED_BY` view from the nearest eligible Directory Carrier and its resolved container ID. The resolved ID must agree with the Atom’s declared `Header.Container`; its Carrier placement follows the corresponding Scope Unit or containing Atom folder. The derived view and its inverse `CONTAINS` represent the same declared containment fact, not a second authored fact.

## Details

Resolve `Header.Container` as a mapping with exactly one of `scope_unit` or `atom`; the Scope Unit reference uses its stable ID. Apply the admitted reference and placement rules. If placement and the declared Container disagree, report the disagreement without replacing the declared logical parent from a directory. Reading or refreshing the inverse view does not edit the containing Object’s Carrier or create a new Atom Version. Project Structure remains authoritative for declared Scope Unit parentage under CA-R-1660.
