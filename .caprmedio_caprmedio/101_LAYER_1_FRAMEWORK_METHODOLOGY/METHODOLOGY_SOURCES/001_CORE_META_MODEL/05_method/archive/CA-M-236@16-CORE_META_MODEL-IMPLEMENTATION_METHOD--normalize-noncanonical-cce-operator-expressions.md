---
subjects:
  governs: Subject/Graph/Rule/CCE Operator Expression Normalization
  depends_on:
  - Subject/Graph/Rule/CCE Operator Expression
  - Subject/Graph/Rule/CCE Operator Registry
version: 16
updated_at: 2026-10-24 11:58:20 +0400
relations: {}
atom_id: CA-M-236@16
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Normalize Noncanonical CCE Operator Expressions

## Scope

noncanonical CCE Operator Expressions.

## Claim

**to** normalize one noncanonical CCE Operator Expression, the Author **must** apply **all** applicable rewrites:

- `each` **to** **every**.
- `equals` **to** **`=`**.
- `does not equal` **to** **`!=`**.
- `both <A> and <B>` **to** `(<A>` **and** `<B>)`.
- `either <A> or <B>` **to** `(<A>` **or** `<B>)`.
- `neither <A> nor <B>` **to** **not** `(<A>` **or** `<B>)`.

## Details
