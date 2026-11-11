---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier.Canonical Address.Segment
version: 29
updated_at: 2026-11-02 19:44:26 +0400
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
  source_atom_revision: 29
  source_sha256: 656d0311427c7586503dcea2e9a2be81ae33804e3e4783cb5c51629582bb9677
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require Portable-Safe Carrier Addresses

## Claim scope

Project-owned Carrier address segments.

## Claim

**every** Project-owned Carrier address segment

- **must** use **only** portable automation-safe ASCII letters, digits, underscores, hyphens, **and** dots, with `@` admitted **only** **in** the `@<version>` Archive suffix immediately **before** the file extension, as specified by CA-D-289,
- **must not** contain whitespace, control characters, path separators, shell metacharacters, empty **or** reserved segments, **or** unsafe leading **or** trailing characters,
- **and** **must** remain sibling-unique under ASCII case folding.
