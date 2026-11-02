---
atom_id: CA-M-449@2
content_role: Method
type: Term Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Term//Empty
  depends_on:
  - Entity/Term
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Method)/(.Type: Term Definition)'
version: 2
updated_at: 2026-10-30 14:27:28 +0400
relations: {}
tier: 1
---
## Summary

Define Empty

## Claim scope

The reusable lexical Term `Empty` for Workflow input values and ID routing.

## Claim

Empty **means** an omitted input, null, **or** the empty string `""`. This Claim explicitly introduces the lexical Term instance named Empty at `Entity/Term//Empty`.

## Semantics

`undefined` denotes an omitted input value only; it does not add another supplied value to the admitted set. The literal string `"undefined"` is not Empty. A supplied null value and a supplied empty string `""` are Empty.

Whitespace-only strings, `0`, `false`, `[]`, and `{}` are not Empty. Do not trim, coerce, or apply a general truthiness test to extend this exact set. This definition does not establish programming-language-specific `None` semantics.

## Details

This Draft records the Operator-confirmed meaning and the initially flat lexical target under `Entity/Term`. The separate proposed Term branch and Method Type Term Definition declaration must be reconciled before adoption. It creates no Term groups, domain ID properties, Workflow definition, execution, or runtime implementation.

The role-only Draft marker allocates no canonical Method identity. Adoption requires the applicable source, Type, identity, naming, and lifecycle checks; this Draft supplies no evidence that those effects occurred. No dictionary Projection, extractor, or lookup service is required.

### Pending governing declarations

- [Entity root with the Term branch](../../04_requirement/draft/CA-R-1248@24-draft-CORE_META_MODEL-DEFINITION--define-entity.md).
- [Term kind and inherited structure](../../04_requirement/draft/CA-R-1318@30-draft-CORE_META_MODEL-DEFINITION--define-term.md).
- [Method Type Term Definition](../../04_requirement/draft/CA-R-draft-CORE_META_MODEL-ENTITY_DEFINITION--define-method-type-term-definition.md).
- [Dedicated Method meaning owner](../../04_requirement/draft/CA-R-1319@26-draft-CORE_META_MODEL--define-governed-term.md).

These links identify pending Draft dependencies, not Current admission.
