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
version: 15
updated_at: "2026-10-11 03:56:26 +0400"
relations: {}
atom_id: "CA-M-228"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Write Subject Expressions with Bearer and Value Qualification

## Scope

authoring one Subject Expression.

## Claim

**to** write a Subject Expression, start with a canonical Entity reference **and** apply `/` in broader-to-narrower order, `.` in bearer-to-dependent order, **and** `:` in Property-to-allowed-value order. resolve **every** named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. `.` retains the mechanical native fact Dependent IS_BORNE_BY Bearer, **and** `:` retains AllowedValue IS_ALLOWED_VALUE_OF Property; `/` admits no native Subject or Entity relation. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.

## Details
