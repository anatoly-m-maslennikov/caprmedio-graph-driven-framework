---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
version: 30
updated_at: 2026-11-03 23:25:51 +0400
relations: {}
atom_id: CA-D-301
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-301-CORE_META_MODEL-ENG_DECISION--require-portable-safe-carrier-addresses.md
  source_atom_id: CA-D-301
  source_atom_revision: 30
  source_sha256: 568ce1b02357751b76871c32c6ce6d78c0d615b16c257d2de81d4b5d3f2bd7a2
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
