---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - Atom Scope
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
version: 23
updated_at: 2026-10-23 03:06:32 +0400
relations:
  child_of:
  - CA-R-932
atom_id: CA-R-916@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary
Restrict ordered Demands to earlier Producers

## Scope

Demand Atoms whose Consumer Atom Scope Unit and Producer Claim Target Scope Unit are ordered siblings.

## Claim

**if** a Demand Atom's Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit are ordered siblings, **then** its Producer Claim Target Scope Unit **must** precede its Consumer Atom Scope Unit.

## Details
