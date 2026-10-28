---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Carrier/File.Main Content
version: 22
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1465
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Summary as an Atom Property

## Scope

the Summary Property of an Atom.

## Claim

a Summary **means** a short, non-authoritative navigation Property of **`=1`** Atom, derived from the finalized primary contribution registered for its Content Role, read within its applicability. it belongs **to** that Atom **without** independent identity, lifecycle, **or** authority.

## Details

for ordinary RMED, the source is Claim read within Scope, **not** Scope alone; for Analysis, Question; for Concern, Concern; for Plan, Objective; for Operations, Operation. For a formal R/Type: Graph Rule, the source is the operative structured YAML under CA-D-637; Claim and Substance sections are not required or supplied by this definition. Summary is written last but remains displayed first. Analysis TLDR summarizes its Results; it is **not** the Atom Summary **and** does **not** replace Question as the Summary source.
