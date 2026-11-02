---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Relations
  depends_on:
  - Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - Entity/Object/Continuant/Structural Unit/Scope Unit
relations: {}
atom_id: CA-R-2149@12
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-29 17:09:47 +0400
---
## Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

## Claim scope

Stored governing Requirement, Method, Evaluation and Delivery relation occurrences.

## Claim

Each stored governing RMED relation must target an Atom in the same ordering Scope Unit at a strictly lower numeric Tier, an Atom in a strict ancestor ordering Scope Unit, or the Core Meta-model prerequisite of Project Configuration explicitly declared by CA-R-1218. The prerequisite exception is one-way and non-transitive. Other descendant and sibling targets are forbidden. Unresolved membership, endpoint, Tier or Scope evidence does not pass. A verified Project Goal uses its Target Project for this ordering check; its owner remains the Operator.

These constraints apply to the source-declared Selection “Stored Governing RMED Relation Occurrences”, not to arbitrary context or history links. There is no automatic conflict winner based on Tier, timestamp or these ordering rules.

## Semantics

A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. The numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.
