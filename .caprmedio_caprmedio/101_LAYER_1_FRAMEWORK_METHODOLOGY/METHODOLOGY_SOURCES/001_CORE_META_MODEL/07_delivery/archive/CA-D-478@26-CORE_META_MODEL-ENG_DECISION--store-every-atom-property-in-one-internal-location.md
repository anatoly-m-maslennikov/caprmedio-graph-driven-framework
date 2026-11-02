---
atom_id: CA-D-478@26
content_role: Delivery
type: Policy
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Carrier/File
  - Entity/Carrier/File.YAML Frontmatter
  - Entity/Carrier/File.Main Content
version: 26
relations:
  delivery_for:
  - CA-R-1598
tier: 2
updated_at: 2026-10-29 07:51:41 +0400
---
## Summary

Store every Atom Property in one internal location

## Claim scope

Atom Property representation in an Atom Markdown File Carrier.

## Claim

Use YAML Frontmatter for an Atom's metadata properties. Use named Markdown
Main Content sections for `content.*` properties. Each applicable Atom Property
has one canonical internal location; its value is not duplicated between YAML
and Markdown.

This reusable Policy governs Atom representation. It does not create a Carrier
or a CARRIES fact for each property or section, and it does not change the
owning direction of an Atom-to-Atom Relation.

## Semantics

YAML and Markdown are carrier locations for different Atom properties, not
alternative authorities for the same value. A section's name identifies its
`content.*` property; a metadata property remains a YAML value.

## Details

This is the Policy-successor proposal for current CA-D-478. It incorporates
the reusable placement boundary supported by CA-D-357 without creating a
per-field representation entity.
