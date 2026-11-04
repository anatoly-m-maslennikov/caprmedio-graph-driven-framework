---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Status
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Entity
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1308
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Resolve Status Domains from Complete Qualified Paths

## Claim

### Prose Claim


Status domains resolved from complete qualified paths.


a global Status value domain **must not** override the Status domain resolved from the complete qualified path of an Artifact Type **or** Atom Content Role **and** Type.

## Details

for Atoms, resolution from the complete qualified Content Role and Type path includes the allowed values inherited from Atom.Header.Status and the additional values admitted for that path. Inheritance does **not** replace the qualified model with a flat global domain or remove its additions. A narrower Atom kind **must not** remove inherited Status values.
