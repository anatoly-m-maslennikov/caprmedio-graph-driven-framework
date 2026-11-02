---
subjects:
  governs: Subject/Graph/Relation/Type
  depends_on:
  - CAPRMEDIO Graph
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Atom
version: 31
updated_at: 2026-10-24 05:54:58 +0400
relations: {}
atom_id: CA-R-806@31
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Register Complete Relation Kind Metadata

## Scope

admitted Relation Kinds.

## Claim

**every** admitted Relation Kind **must** have **`=1`** canonical descriptive metadata record derived from its governing authority that resolves its owning kind of CAPRMEDIO Graph, canonical name, meaning, declared direct direction, inverse direction, authority effect, transitivity, applicability, Status, **and** exclusive purpose.

## Details

Allowed source and target classes, allowed endpoint graph contexts, cardinality and other permissions or prohibitions belong in the governing Graph Rules, not in the Relation Kind definition. Descriptive meaning, transitivity and applicability explain the relation; any admissibility restriction belongs in its Graph Rules instead. A view may combine the definition with its governing Graph Rules without creating a second authoritative constraint. The declared direct direction identifies the one authored fact; its inverse is derived. A name such as IS_CONTAINED_BY does not make that direction an inverse. Moving existing constraints into formal Rule instances remains separate source work; this metadata contract does not itself rewrite them.
