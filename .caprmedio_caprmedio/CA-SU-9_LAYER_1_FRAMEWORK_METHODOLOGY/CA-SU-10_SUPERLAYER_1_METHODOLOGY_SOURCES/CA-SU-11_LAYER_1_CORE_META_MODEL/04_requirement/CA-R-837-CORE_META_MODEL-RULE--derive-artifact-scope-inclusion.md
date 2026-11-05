---
atom_id: CA-R-837
ref_id: CA-R-837
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 36
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-837-CORE_META_MODEL-RULE--derive-artifact-scope-inclusion.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive Artifact scope inclusion

## Claim

### Prose Claim


Artifacts contained **in** a Scope Unit.


the resolver **must** resolve **`=1`** direct Scope Unit from the Atom's internally carried ownership, checked against its canonical Carrier address, **or** from the registered canonical Carrier authority for a non-Atom Artifact **and** include that Artifact **in** **every** Scope Unit on the direct Unit's complete ancestor path; missing, multiple, unknown, **or** cyclic scope ownership is invalid.

## Details

an Atom with no containing Scope Unit uses the external-Atom Author fallback under CA-D-657-CORE_META_MODEL-ENG_DECISION--use-economical-yaml-frontmatter; a failed Scope Unit resolution does **not** establish that no containing Scope Unit exists.
