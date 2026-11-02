---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Governed Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - Subject
  - Relation Kind
  - Subject Target
  - Subject/Domain/Node/Continuant/Atom.Substance
version: 17
updated_at: 2026-10-22 16:26:09 +0000
relations:
  child_of:
  - CA-R-1269
  - CA-R-1199
  - CA-R-2100
  - CA-R-1202
atom_id: CA-R-1363@17
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

Define Atom Governed Subject

## Scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's optional **`0..1`** Subject Relation whose Relation Kind is GOVERNS. when present, its target is the canonical Subject Target governed by the Atom's Claim; the Relation **and** its target are distinct.

## Details
