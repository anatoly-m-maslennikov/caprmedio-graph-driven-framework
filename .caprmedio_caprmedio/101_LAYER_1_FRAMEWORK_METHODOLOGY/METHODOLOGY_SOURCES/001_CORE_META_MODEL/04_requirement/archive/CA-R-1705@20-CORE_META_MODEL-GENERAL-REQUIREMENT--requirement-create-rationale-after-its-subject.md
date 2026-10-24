---
subjects:
  governs: artifact-model
  depends_on: []
version: 20
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-R-1702
atom_id: CA-R-1705@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Requirement — Create Rationale **after** its subject

## Scope

Rationale Atoms and their pre-existing specification subjects.

## Claim

a Rationale is an Analysis Atom created **only** **after** **every** specification Atom it explains already exists. the Rationale stores the directed relation **to** its subjects; specification Atoms contain **none** of (embedded Rationale, persisted Rationale backlink).

Rationale is explanatory rather than normative. Changing an obligation, boundary, Method, Evaluation condition, Delivery rule, **or** acceptance meaning requires a new applicable specification Atom rather than a Rationale.

## Primary claim

a Rationale follows **and** points **to** its pre-existing specification subjects **without** modifying them.

## Details
