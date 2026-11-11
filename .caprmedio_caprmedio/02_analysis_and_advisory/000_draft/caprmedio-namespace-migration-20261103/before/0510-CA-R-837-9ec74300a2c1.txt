---
subjects:
  active: Scope Unit
version: 36
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-837
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Derive Artifact scope inclusion

## Claim scope

Artifacts contained **in** a Scope Unit.

## Claim

the resolver **must** resolve **`=1`** direct Scope Unit from the Atom's internally carried ownership, checked against its canonical Carrier address, **or** from the registered canonical Carrier authority for a non-Atom Artifact **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.

## Details

an Atom with no containing Scope Unit uses the external-Atom Author fallback under CA-D-657-CORE_META_MODEL-ENG_DECISION--use-economical-yaml-frontmatter; a failed Scope Unit resolution does **not** establish that no containing Scope Unit exists.
