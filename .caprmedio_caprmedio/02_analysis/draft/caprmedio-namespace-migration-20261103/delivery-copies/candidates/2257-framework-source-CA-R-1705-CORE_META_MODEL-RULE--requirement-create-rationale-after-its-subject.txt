---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := "Analysis & Advisory")/(.Form := Rationale)
version: 33
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1705
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
---
## Summary

Requirement — Create Rationale **after** its subject

## Claim scope

Rationale Atoms and their pre-existing specification subjects.

## Claim

a Rationale is an Analysis & Advisory Atom created **only** **after** **every** specification Atom it explains already exists. the Rationale stores the directed relation **to** its subjects; specification Atoms contain **none** of (embedded Rationale, persisted Rationale backlink).

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, **or** acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

a Rationale follows **and** points **to** its pre-existing specification subjects **without** modifying them.

