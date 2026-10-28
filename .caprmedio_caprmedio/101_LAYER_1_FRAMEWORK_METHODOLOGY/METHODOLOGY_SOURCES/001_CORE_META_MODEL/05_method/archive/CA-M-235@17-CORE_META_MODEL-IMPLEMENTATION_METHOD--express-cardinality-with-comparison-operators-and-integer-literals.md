---
subjects:
  governs: Subject/Graph Rule/CCE Operator Expression
  depends_on:
  - Subject/Graph Rule/CCE
  - Subject/Graph Rule/CCE Operator Registry
  - Subject/Graph Rule/CCE Operator Expression
version: 17
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-M-235@17
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary

Express Cardinality with Comparison Operators **and** Integer Literals

## Scope

numeric Cardinality Constraint authoring.

## Claim

**to** author one numeric Cardinality Constraint, the Author **must** serialize one canonical comparison CCE Operator immediately followed by one Nonnegative Integer Literal as a prefix immediately **before** the counted Entity **or** expression; examples: **`=1`** Author, **`>=1`** Requirement Atom, **`<=1`** Type, **`>=0`** Property.

## Details
