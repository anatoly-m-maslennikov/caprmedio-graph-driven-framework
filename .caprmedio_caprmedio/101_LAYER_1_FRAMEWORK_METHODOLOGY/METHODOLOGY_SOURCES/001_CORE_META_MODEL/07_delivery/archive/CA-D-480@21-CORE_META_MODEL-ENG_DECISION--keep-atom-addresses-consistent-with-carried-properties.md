---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
  - Entity/Object/Continuant/Governing Objects/Atom.ID
  - Entity/Object/Continuant/Governing Objects/Atom.Status
  - Entity/Carrier/File
version: 21
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
atom_id: CA-D-480@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Decision
---
## Summary

Keep Atom addresses consistent with carried Properties

## Claim scope

Atom Properties represented by a filename, matching directory name, or placement.

## Claim

**every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.

- compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
- a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
- agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.

## Details
