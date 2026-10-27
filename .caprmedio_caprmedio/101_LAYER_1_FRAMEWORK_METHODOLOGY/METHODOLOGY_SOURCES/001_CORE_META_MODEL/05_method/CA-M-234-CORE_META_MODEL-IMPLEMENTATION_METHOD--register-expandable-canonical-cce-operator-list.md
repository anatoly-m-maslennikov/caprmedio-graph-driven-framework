---
subjects:
  governs: Subject/Graph Rule/CCE Operator Registry
  depends_on:
  - Subject/Graph Node/Engineering/Authoring/Controlled English
  - Subject/Graph Rule/CCE Operator Registry
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-M-234
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Register Expandable Canonical CCE Operator List

## Scope

the canonical CCE Operator Registry.

## Claim

the current canonical CCE Operator Registry **must** contain this expandable set:

1. statement form: **to**, **means**.
2. modality: **must**, **must not**, **may**.
3. condition: **if**, **then**, **when**, **otherwise**.
4. temporal condition: **before**, **after**, **until**, **unless**.
5. quantification: **all**, **every**, **any**, **none**.
6. logical/set: **and**, **or**, **not**, **without**, **where**.
7. restriction: **only**.
8. predicate: **in**, **not in**, **is empty**, **is not empty**, **contains**, **starts with**, **ends with**.
9. comparison: **`=`**, **`!=`**, **`<`**, **`<=`**, **`>`**, **`>=`**.

## Details

another token **may** enter the CCE Operator Registry **when** one active CCE Method assigns the token one syntactic **or** logical function.
