---
subjects:
  governs: "Entity/Carrier.Canonical Address.Segment"
  depends_on: []
version: 17
updated_at: "2026-10-15 18:51:04 +0000"
relations: {}
atom_id: "CA-D-301"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-301-CORE_META_MODEL--require-portable-safe-carrier-addresses.md
  source_atom_id: CA-D-301
  source_atom_revision: 17
  source_sha256: a4d4e32328eaa1f3f4a9ee2a7275710b00f7e87aa337af2e1b36f2ee1d3d7cb3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require Portable-Safe Carrier Addresses

## Scope

Project-owned Carrier address segments.

## Claim

**every** Project-owned Carrier address segment

- **must** use **only** portable automation-safe ASCII letters, digits, underscores, hyphens, **and** dots, with `@` admitted **only** **in** the `@<version>` Archive suffix immediately **before** the file extension, as specified by CA-D-289,
- **must not** contain whitespace, control characters, path separators, shell metacharacters, empty **or** reserved segments, **or** unsafe leading **or** trailing characters,
- **and** **must** remain sibling-unique under ASCII case folding.

## Details
