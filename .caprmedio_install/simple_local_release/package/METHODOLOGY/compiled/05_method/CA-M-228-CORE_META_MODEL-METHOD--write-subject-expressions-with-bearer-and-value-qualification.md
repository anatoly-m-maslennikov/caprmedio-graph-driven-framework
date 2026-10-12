---
subjects:
  governs: "Subject Expression Writing"
  depends_on:
    - "Subject Path"
    - "Entity"
    - "Relation"
    - "Term"
    - "Subject"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 16
updated_at: "2026-10-11 18:04:47 +0400"
relations: {}
atom_id: "CA-M-228"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-228-CORE_META_MODEL-METHOD--write-subject-expressions-with-bearer-and-value-qualification.md
  source_atom_id: CA-M-228
  source_atom_revision: 16
  source_sha256: 0f398721d7d15aaf8e0b0f69a20b1b541e8d306839073c98eea4b80f9580b40d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Write Subject Expressions with Bearer and Value Qualification

## Scope

authoring one Subject Expression.

## Claim

**to** write a Subject Expression, start with either a canonical Entity reference **or** the exact approved initial lowercase `atom(...)` selector under CA-R-1321, **and** apply `/` in broader-to-narrower order, `.` in bearer-to-dependent order, **and** `:` in Property-to-allowed-value order. resolve **every** ordinary named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. in `atom(content_role="Plan").Status`, `Status` is the dependent Property borne by the selected Atom; `Plan` remains the Content Role allowed value qualifying that Atom, **not** Status's bearer **or** Status's allowed value. `.` retains the mechanical native fact Dependent IS_BORNE_BY Bearer, **and** `:` retains AllowedValue IS_ALLOWED_VALUE_OF Property; `/` admits no native Subject or Entity relation. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.

## Details
