---
atom_id: CA-R-2160@6
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 6
updated_at: 2026-10-29 08:06:42 +0400
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.content.claim_scope
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
relations: {}
---
## Summary

Define Atom Content Scope

## Claim scope

The applicability boundary of an Atom's role-specific content.

## Claim

Content Scope means the part of an Atom's content that states which cases, parts or conditions its primary contribution governs. For RMED its logical path is atom.content.claim_scope and its Markdown heading is ## Claim scope. It is present zero or one time and may be omitted for full applicability only when the Claim covers the whole governed thing/topic and the whole owning context under the applicable rules; otherwise its exact boundary must be explicit. Claim scope is not another Scope Unit and is not a copy of the Local or Target Scope Unit reference. Other Content Roles retain their applicable content-scope contracts.

## Semantics

Do not invent a Local Scope Unit for the Operator-owned Project Goal. Read Claim, Semantics and Details within the stated boundary; do not maintain a second scope declaration.

## Details

This Draft registers the RMED name without restoring Substance or adding another property/text grouping layer.
