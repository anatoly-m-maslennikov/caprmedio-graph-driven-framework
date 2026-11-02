---
subjects:
  governs: 'Subject/Graph/Relation/Type: DEPENDS_ON'
  depends_on:
  - Subject/Graph/Relation/Type
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Domain/Node/Continuant/Atom.Substance
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 24
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
atom_id: CA-R-1200@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Define DEPENDS_ON Subject Relation Kind

## Scope

the DEPENDS_ON Subject Relation Kind of an Atom.

## Claim

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Subject Target mentioned **in** its Markdown Main Content other than its GOVERNS target. this reference does **not** make the Claim authoritative about that Subject Target.

## Details

mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-CORE-REQUIREMENT--define-plan-blocking.
