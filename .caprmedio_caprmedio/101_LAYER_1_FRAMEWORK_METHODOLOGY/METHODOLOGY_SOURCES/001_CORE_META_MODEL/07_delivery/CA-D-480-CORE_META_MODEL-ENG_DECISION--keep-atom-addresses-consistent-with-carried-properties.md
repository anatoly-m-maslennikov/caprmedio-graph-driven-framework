---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.ID
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
  - Subject/CAPRMEDIO/Carrier/File
version: 19
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-480
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
