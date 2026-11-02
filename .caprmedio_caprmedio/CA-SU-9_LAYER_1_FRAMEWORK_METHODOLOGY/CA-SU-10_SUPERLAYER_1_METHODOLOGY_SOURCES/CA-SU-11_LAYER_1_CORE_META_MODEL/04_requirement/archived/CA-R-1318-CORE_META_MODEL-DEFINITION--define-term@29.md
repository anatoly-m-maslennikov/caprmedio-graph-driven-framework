---
subjects:
  governs: Entity/Object/Continuant/Term
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 29
updated_at: 2026-10-29 14:12:43 +0400
relations: {}
atom_id: CA-R-1318
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Term

## Claim scope

Project-specific vocabulary used as reusable lexical components of complete or qualified entity names and authored content, including the word `Term` itself.

## Claim

A Term has one Name, the word or phrase used for its meaning. This declares the existing vocabulary properties and does not implement or review the deferred Terms Graph.

a Term **means** a reusable word **or** phrase component of complete **or** qualified entity names **and** authored content whose approved Project-specific meaning remains consistent across **all** its uses.

### Formal claim

```text
Entity/Object/Continuant/Term.Name[string]{1}
```

## Details

This Entity Definition defines the Term kind and its Name property. Using the word `Term` self-referentially does not require infinite definition layers. This Entity Definition does not itself supply the dedicated lexical Term Definition required for Governed Term status under CA-R-1319. Whether the word `Term` has that separate lexical authority remains a source-coverage question; this Claim introduces no `Term//Term` instance or additional Atom.

The Operator distinguished entities from their reusable lexical Terms: `Package` is reused in `Package`, `Eval Package`, and `Runtime Package`; `Unit` is reused in `Scope Unit` and `Code Unit`. A complete canonical entity name can consist of one Term or several Terms with registered qualification. Reusing `Package` inside `Eval Package` does not itself reference the separately named `Package` entity or establish a Relation. Lexical composition does not introduce another entity or require a separate `Unit` node.

`Package > Module > Code Unit` connects three entities whose complete names are `Package`, `Module`, and `Code Unit`. The accepted `atom.id` and `projection.id` identify distinct qualified property entities and reuse the Term `ID`. Their shared terminal label is not a collision. The dot remains an operator. Neither accepted name is replaced with `atom.atom_id` or another invented spelling. Arbitrary composite expressions are not one Term under CA-R-1325 or automatically one entity name. Literal source quotations and code identifiers are distinguished from authored entity mentions and are not automatically renamed.

A Governed Term has exactly one dedicated active Requirement Atom of Type Term Definition as its authoritative meaning owner under CA-R-1319 and CA-R-2229. The lexical Term target is distinct from an entity whose complete name uses it. A defining Atom may explicitly introduce its lexical target under CA-R-1194 and CA-R-1931; a parser or word occurrence does not introduce it. The current Term placement remains subject to the separate C605 reconciliation boundary. No dictionary Projection, extractor, lookup, or Terms Graph implementation is required.
