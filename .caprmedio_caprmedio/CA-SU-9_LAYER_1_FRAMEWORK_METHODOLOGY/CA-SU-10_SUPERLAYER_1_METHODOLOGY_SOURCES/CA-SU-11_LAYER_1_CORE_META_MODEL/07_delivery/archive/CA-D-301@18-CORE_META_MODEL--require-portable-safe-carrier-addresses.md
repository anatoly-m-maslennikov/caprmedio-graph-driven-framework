---
subjects:
  governs: Subject/Engineering/Carrier.Canonical Address.Segment
  depends_on: []
version: 18
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-D-301@18
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
global_tier: 11
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
