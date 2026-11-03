---
atom_id: CA-R-1948
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Carrier.Canonical Address.Segment
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1948-CORE_META_MODEL-DEFINITION--define-carrier-canonical-address-segment.md
  source_atom_id: CA-R-1948
  source_atom_revision: 12
  source_sha256: 7a0cdaf0449b8ed1f87b4764067fe856b712a74a27a36a68dd0827a2b7c07fec
  original_relations_sha256: 2e54810b23dc6829999889d9dce55018a30d8606de806fb64b6f8578b2c66336
---
## Summary

Define Carrier.Canonical Address.Segment

## Claim scope

Carriers whose canonical address format has component segments.

## Claim

A Canonical Address Segment **means** one component of a Carrier's Canonical Address under its applicable address format.

### Formal claim

```text
Carrier.Canonical Address.Segment[string]{1}
```

## Details

CA-D-301 governs project-owned address segments; CA-D-352 treats status subdirectories as placement components. Filesystem separators and portable-name restrictions are not imposed on every database address by this definition.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
