---
atom_id: CA-D-draft
content_role: Delivery
form: Decision
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs:
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Carrier
version: 1
relations: {}
tier: 3
updated_at: 2026-10-31 18:43:05 +0400
---
## Summary

Carry Scope Unit Declarations as Governing Atoms

## Claim

Carry a Scope Unit Declaration in a Markdown Atom file, with its operative prose, GFEL expressions or both in Claim. The file is the Carrier; the Declaration is the governed content. After an authorized migration, `project_structure.toml` ceases to be an independent governing authority; any compatibility file is derived from the governing Declaration.

Scope Units do not have Navigation Number. Keep their existing Local Order semantics; do not maintain a duplicate navigation position. Navigation Number is retained only for Steps and P (Plan) Atoms. This decision does not add new numbering or Carrier-format rules for those Atoms.

## Details

### Logical properties and proposed Carrier keys

Reuse the existing Node Declaration Carrier mapping: logical Role is carried as `role`, Form as `form`, and the active Subject as `subjects.active`. These are model properties and their Carrier encodings, not independently maintained duplicate values.

This packet’s legacy `content_role` and `subjects.governs` control headers are not an alternative future Declaration format. Normalize them to the proposed Carrier before promotion. Current readers are not claimed migrated.


This Draft neither performs nor authorizes migration, TOML deletion, code changes, or a new schema or file format.
