---
atom_id: CA-D-301
ref_id: CA-D-301
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 30
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-301-CORE_META_MODEL-DECISION--require-portable-safe-carrier-addresses.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-301-CORE_META_MODEL-ENG_DECISION--require-portable-safe-carrier-addresses.md
  source_atom_id: CA-D-301
  source_atom_revision: 30
  source_sha256: 031106bed16dd75065180c7ed39ff254451e11fd21fc89f450aa73ac87ac1ffd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require Portable-Safe Carrier Addresses

## Claim

### Prose Claim


Project-owned Carrier address segments.


**every** Project-owned Carrier address segment

- **must** use **only** portable automation-safe ASCII letters, digits, underscores, hyphens, **and** dots, with `@` admitted **only** **in** the `@<version>` Archive suffix immediately **before** the file extension, as specified by CA-D-289,
- **must not** contain whitespace, control characters, path separators, shell metacharacters, empty **or** reserved segments, **or** unsafe leading **or** trailing characters,
- **and** **must** remain sibling-unique under ASCII case folding.
