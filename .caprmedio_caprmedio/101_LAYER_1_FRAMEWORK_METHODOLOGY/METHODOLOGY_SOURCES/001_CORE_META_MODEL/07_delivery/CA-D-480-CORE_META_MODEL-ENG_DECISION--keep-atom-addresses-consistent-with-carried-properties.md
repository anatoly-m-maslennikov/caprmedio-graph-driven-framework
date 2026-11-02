---
subjects:
  active: Atom
  passive:
  - Atom.Content.Summary
  - Atom.ID
  - Atom.Status
  - Carrier/File
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-480
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
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
