---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Selection
  depends_on: []
version: 22
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-M-121@22
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Implementation Method
---
# Summary
Evaluate Scope Expressions

## Scope
evaluation of a Scope Expression.

## Claim
**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve **every** exact Atom ID **or** other atomic identity **to** **`=1`** Governed Entity.
2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Atom Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of **only** members whose field predicate evaluates **to** true according **to** `CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions`.
7. evaluate the innermost parenthesized set function **before** its containing set function.
8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.

## Details
