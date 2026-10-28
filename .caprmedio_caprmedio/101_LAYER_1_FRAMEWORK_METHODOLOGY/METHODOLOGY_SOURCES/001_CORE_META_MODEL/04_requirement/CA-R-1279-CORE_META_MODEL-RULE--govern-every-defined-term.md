---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: GOVERNS'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Semantics
  - Subject
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 27
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1279
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Govern Every Defined Term

## Scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

when an Atom's Claim explicitly defines a Term, it **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by that Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim, source use, **and** applicable Atom.Semantics establish that Term's meaning; the other Term components **in** the path are references **to** their own meanings, **not** additional meanings supplied by this Atom.

## Details
