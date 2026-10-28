---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Relation/Type: DEPENDS_ON'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
version: 32
updated_at: 2026-10-27 19:59:52 +0400
relations:
  depends_on:
  - CA-R-1275
atom_id: CA-R-1200
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Definition
---
# Summary

Define DEPENDS_ON Subject Relation Kind

## Scope

the DEPENDS_ON Subject Relation Kind of an Atom.

## Claim

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Subject graph node mentioned **in** its applicable role-specific content or other registered content, other than its GOVERNS target. this reference does **not** make the Atom's content—or every Governing Configuration fact—authoritative about that Subject graph node; formal authority depends on the applicable registered content form and role. a formal Claim may be carried in Markdown, structured YAML, or Governing Configuration, but Governing Configuration facts are not automatically Atom Claims.

## Details

mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count, whether the logical Claim is carried in Markdown, structured YAML, or Governing Configuration. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-DEFINITION--define-plan-blocking.
