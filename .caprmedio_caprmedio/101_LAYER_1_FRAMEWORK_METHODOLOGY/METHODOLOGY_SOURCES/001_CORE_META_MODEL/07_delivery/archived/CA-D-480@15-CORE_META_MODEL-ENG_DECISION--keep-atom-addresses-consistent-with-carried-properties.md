---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Property
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Property
  - Subject/Graph Node/Domain/Continuant/Atom.Summary
  - Subject/Graph Node/Domain/Continuant/Atom.ID
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Engineering/Continuant/Carrier/File Carrier
version: 15
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-D-478
  - CA-D-282
  - CA-D-466
atom_id: CA-D-480@15
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Keep Atom addresses consistent with carried Properties

## Scope

Atom Properties represented by a filename, matching directory name, or placement.

## Claim

**every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.

- compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
- a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
- agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.

## Details
