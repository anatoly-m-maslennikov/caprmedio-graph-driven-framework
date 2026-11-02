---
subjects:
  active: Carrier.Canonical Address.Segment
  passive: []
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-301@28
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Delivery
form: Decision
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
