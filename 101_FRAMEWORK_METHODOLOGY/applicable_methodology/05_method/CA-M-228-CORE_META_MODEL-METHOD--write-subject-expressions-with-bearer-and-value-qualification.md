---
subjects:
  governs: "Subject Expression Writing"
  depends_on:
    ["Subject Path", "Subject Target", "Entity/Relation", "Entity/Node/Continuant/Term", "Subject", "GOVERNS", "DEPENDS_ON"]
version: 20
updated_at: "2026-10-21 01:47:52 +0400"
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
  source_atom_revision: 20
  source_sha256: d63be0ef54fea2a662679bc61290ed460c81ee1e7e686eb9614687a99826b209
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Write Subject Expressions with Bearer and Value Qualification

## Scope

authoring one Subject Expression.

## Claim

**to** write a Subject Expression, start with either a canonical Subject Target reference **or** the exact approved initial lowercase `atom(...)` selector under CA-R-1321, **and** apply `/` in broader-to-narrower order, `//` from an Entity kind to its following named instance, `.` in bearer-to-dependent order, **and** `:` in Property-to-allowed-value order. resolve ordinary named components **other than** the RHS instance name after `//` as Term references under CA-R-1321. The RHS is the existing instance's name under its separately governed naming/source authority, not an Atom ID and not automatically a Term; the whole qualified path must still resolve to one existing canonical Subject Target. In `atom(content_role="Plan").Status`, `Status` is the dependent Property borne by the selected Atom; `Plan` remains the Content Role allowed value qualifying that Atom, **not** Status's bearer **or** Status's allowed value. `.` retains the mechanical native fact Dependent IS_BORNE_BY Bearer, **and** `:` retains AllowedValue IS_ALLOWED_VALUE_OF Property; `/` admits no native Subject or Entity relation. `//` denotes the separate kind/instance EntityGraph connection but syntax alone does not assert or admit an INSTANCE_OF fact, which requires its own Core definition. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.

## Details
