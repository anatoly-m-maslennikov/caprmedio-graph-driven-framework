---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Verification <+ Coverage
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO_MODEL <+ Atom.Content
version: 25
updated_at: 2026-11-02 18:35:20 +0400
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

## Claim

### Prose Claim


coverage between Evaluation Atoms and their implementation realizations.


coverage between Evaluation Atoms **and** their realizations **may** be many-to-many **only** with explicit attribution:

- **`=1`** Evaluation Atom **may** be realized by multiple distinct implementations.
- **`=1`** implementation **may** realize multiple Evaluation Atoms **only** **when** its result remains attributable **to** **every** covered Claim.

## Details

a shared implementation **must not** make its covered Claims **or** their result attribution implicit. this Claim governs coverage, **not** a new Carrier **or** a second implementation registry.
