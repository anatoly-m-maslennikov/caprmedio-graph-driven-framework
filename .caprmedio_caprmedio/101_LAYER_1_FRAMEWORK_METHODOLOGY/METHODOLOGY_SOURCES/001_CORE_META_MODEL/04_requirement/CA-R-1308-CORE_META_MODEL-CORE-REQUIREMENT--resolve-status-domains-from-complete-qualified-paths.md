---
subjects:
  governs: Artifact.Status
  depends_on:
  - Artifact/Type
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Type
version: 16
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1308
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Resolve Status Domains from Complete Qualified Paths

## Scope

Status domains resolved from complete qualified paths.

## Claim

a global Status value domain **must not** override the Status domain resolved from the complete qualified path of an Artifact Type **or** Atom Content Role **and** Type.

## Details

for Atoms, resolution from the complete qualified Content Role and Type path includes the allowed values inherited from Atom.Status and the additional values admitted for that path. Inheritance does **not** replace the qualified model with a flat global domain or remove its additions. A narrower Atom kind **must not** remove inherited Status values.

