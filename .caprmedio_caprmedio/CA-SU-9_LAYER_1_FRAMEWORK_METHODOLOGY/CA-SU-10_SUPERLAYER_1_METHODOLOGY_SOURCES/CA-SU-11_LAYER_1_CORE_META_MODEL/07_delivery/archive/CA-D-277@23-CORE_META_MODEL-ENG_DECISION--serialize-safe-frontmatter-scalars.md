---
subjects:
  governs: Entity/Carrier/File.YAML Frontmatter.Scalar
  depends_on:
  - Entity/Carrier/File.Main Content
version: 23
updated_at: 2026-10-29 10:13:50 +0400
relations: {}
atom_id: CA-D-277@23
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Serialize Safe Frontmatter Scalars

## Claim scope

YAML Frontmatter of Markdown Atom Carriers.

## Claim

the YAML Frontmatter of a Markdown Atom Carrier **must** serialize registered YAML-safe controlled string values as plain scalars **and** **must** place uncontrolled human prose **in** Main Content.
