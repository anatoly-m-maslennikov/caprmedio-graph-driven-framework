---
atom_id: CA-P-2690@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:00:14 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Migrate RMED body sections to logical properties

## Objective

Migrate RMED body sections to logical properties.

## Details

After CA-P-2689.

For the selected Current RMED sources, migrate to # Summary with its value below, optional ## Claim scope, required ## Claim, optional child ### Formal claim, optional ## Semantics and optional ## Details. Keep one Claim object. Its own text is prose; formal_claim is an optional fenced expression. At least one is substantive for a complete Claim. Both may contribute to the one unit defined by the Role/Type.

Map the actual Markdown outline to normalized property keys; ignore headings in fences and do not invent empty hierarchy levels. Detect normalization collisions and resolve them using the declared policy. Keep Semantics outside Claim, not another source of operative constraints. Do not introduce atom.property, property/text subgroups, an extra Prose claim field or a second frontmatter Claim.

Keep YAML properties, such as atom.version_number, separate from Markdown access such as atom.content.claim. Change no unrequested metadata meaning or Type-specific content just to satisfy an old reader. Use bounded per-source Draft/archive/promotion updates and preserve unrelated content.

## Definition of Done

All selected complete RMED carriers match their logical property layout, the normalized paths resolve without hidden collisions, and each has exactly one Claim with no duplicate representation fields.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.
