---
atom_id: CA-R-2237@2
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Package > Asset
version: 2
updated_at: 2026-10-29 10:28:52 +0400
relations: {}
tier: 1
---
## Summary

Define Implementation Asset

## Claim

An Asset is non-executable Implementation content needed by runtime or evaluations and contained in one Package. Descriptive Documentation, rather than required runtime/evaluation input, is a separate Package part.

### Formal claim

```text
Package > Asset
```

## Semantics

Asset names logical content. File and other Carriers represent that content; they are distinct from the Asset itself. An executable permission bit or file extension alone does not decide the item's role. Runtime or evaluation necessity distinguishes this kind from Documentation; it does not automatically classify every non-executable repository file as an Asset.

## Details

CA-A-1266 narrows the previous broad Asset proposal. CA-A-1267 confirms runtime and test Assets. CA-A-1278 retires the broad Resources kind. Non-executable runtime/evaluation Configuration, Schema, Template and Test Fixture specialize Asset; executable LLM instructions remain Prompts and explanatory material remains Documentation. Governing Configuration stays separate. The defining identity is adopted; reusable D Policies govern representation. No new primitive Format or runtime implementation is introduced.

CA-A-1271 restores the logical name Asset and supersedes the Asset File spelling. This is the sole prepared Asset Definition promotion target, not an alias for another kind.
