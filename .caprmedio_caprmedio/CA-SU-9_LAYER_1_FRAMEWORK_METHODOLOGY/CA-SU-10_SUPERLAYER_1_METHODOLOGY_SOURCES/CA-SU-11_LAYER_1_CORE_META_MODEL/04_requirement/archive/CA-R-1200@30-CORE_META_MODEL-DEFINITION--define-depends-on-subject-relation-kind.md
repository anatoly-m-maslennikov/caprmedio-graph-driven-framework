---
subjects:
  governs: 'Subject/Graph Relation/Type: DEPENDS_ON'
  depends_on:
  - Subject/Graph Relation/Type
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 30
updated_at: 2026-10-26 05:28:37 +0400
relations:
  depends_on:
  - CA-R-1275
atom_id: CA-R-1200@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Definition
---
# Summary

Define DEPENDS_ON Subject Relation Kind

## Scope

the DEPENDS_ON Subject Relation Kind of an Atom.

## Claim

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Subject graph node mentioned **in** its logical Claim or other registered content, other than its GOVERNS target. this reference does **not** make the Claim authoritative about that Subject graph node.

## Details

mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count, whether the logical Claim is carried in Markdown, structured YAML, or Governing Configuration. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-DEFINITION--define-plan-blocking.
