---
subjects:
  active: Entity/Aspect/Engineering/Verification/Coverage
  passive:
  - Atom/(.Role := Evaluation)
  - Entity/Object/Continuant/Package/Project Implementation
  - Atom.Content
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1504
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep Evaluation implementation coverage explicit

## Claim scope

coverage between Evaluation Atoms and their implementation realizations.

## Claim

coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

## Details

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
