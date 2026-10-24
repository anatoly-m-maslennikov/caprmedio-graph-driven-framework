---
subjects:
  governs: 'Subject/Graph/Relation/Type: GOVERNS'
  depends_on:
  - Definition Atom
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject Path
  - Subject/Domain/Node/Continuant/Atom.Substance
version: 19
updated_at: 2026-10-24 00:51:05 +0400
relations: {}
atom_id: CA-R-1279@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Govern Every Defined Term

## Scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

**every** Definition Atom **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by its Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim establishes that Term's meaning; the other Term components **in** the path are references **to** their own definitions, **not** additional definitions supplied by this Atom.

## Details
