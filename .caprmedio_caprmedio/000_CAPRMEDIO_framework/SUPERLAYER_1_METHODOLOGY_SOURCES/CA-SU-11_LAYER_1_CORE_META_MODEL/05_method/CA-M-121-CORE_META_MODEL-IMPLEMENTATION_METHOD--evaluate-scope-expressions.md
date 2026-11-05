---
atom_id: CA-M-121
ref_id: CA-M-121
container:
  scope_unit: CA-SU-11
role: Method
form: Implementation Method
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
tier: 3
status: Active
version: 28
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-121-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-scope-expressions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Evaluate Scope Expressions

## Claim

### Prose Claim

evaluation of a Scope Expression.

**to** evaluate one Scope Expression, the Resolver **must** perform **all** of:

1. resolve **every** exact Atom ID **or** other atomic identity **to** **`=1`** Governed Entity.
2. interpret **all** `<ENTITY_KIND>` as **every** Governed Entity of that kind within Atom Scope.
3. interpret **or** as set union.
4. interpret **and** as set intersection.
5. interpret **without** as left-side set exclusion.
6. interpret **where** as retention of **only** members whose field predicate evaluates **to** true according **to** `CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions`.
7. evaluate the innermost parenthesized set function **before** its containing set function.
8. use another Scope function **only** **when** an active CCE Method gives that function **`=1`** set meaning.
