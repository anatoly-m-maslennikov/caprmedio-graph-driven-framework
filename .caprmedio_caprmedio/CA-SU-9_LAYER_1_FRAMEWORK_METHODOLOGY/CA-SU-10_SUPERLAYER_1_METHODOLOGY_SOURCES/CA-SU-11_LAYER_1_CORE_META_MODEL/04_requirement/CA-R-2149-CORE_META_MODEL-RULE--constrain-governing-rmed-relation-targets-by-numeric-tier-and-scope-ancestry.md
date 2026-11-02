---
subjects:
  active: Atom.Relations
  passive:
  - Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - Atom.Tier
  - Scope Unit
relations: {}
atom_id: CA-R-2149
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
version: 14
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Rule
---
## Summary

Constrain Governing RMED Relation Targets by Numeric Tier and Scope Ancestry

## Claim scope

Stored governing Requirement, Method, Evaluation and Delivery relation occurrences selected under CA-R-2148@10, and any independently admitted Operations-source relation within the narrow Tier 0 exception.

## Claim

Each stored governing RMED relation must target an Atom in the same ordering Scope Unit at a strictly lower numeric Tier or satisfy the narrow Tier 0 exception below, an Atom in a strict ancestor ordering Scope Unit, or the Core Meta-model prerequisite of Project Configuration explicitly declared by CA-R-1218@31. The prerequisite exception is one-way and non-transitive. Other descendant and sibling targets are forbidden. Unresolved membership, endpoint, Tier or Scope evidence does not pass. A verified Project Goal uses its Target Project for this ordering check; its owner remains the Operator.

As a narrow exception, within the same Local Scope Unit, a Tier `0` Method, Evaluation, Delivery or Operations source may target a Tier `0` Requirement only through a stored typed governing relation already admitted for those endpoints by its defining declaration. Equal Tier `0` does not otherwise pass: it does not admit Requirement-to-Requirement, Requirement-to-M/E/D/O, or M/E/D/O-to-M/E/D/O links. This exception creates no Relation Kind or Operations relation admission and does not establish an automatic conflict winner.

These constraints apply to the source-declared Selection “Stored Governing RMED Relation Occurrences”, not to arbitrary context or history links. There is no automatic conflict winner based on Tier, timestamp or these ordering rules.

## Semantics

A verified Project Goal uses its Target Project, while its owner remains the Operator Actor; ordinary endpoints use their Local Scope Unit. Apart from the explicitly stated equal-Tier-0 exception, the numeric comparison and strict-ancestor rule are unchanged. The exact Project Configuration → Core Meta-Model prerequisite alternative is the logical-role declaration in CA-R-1218@31; it does not authorize the reverse, another source-role pair, a transitive edge, or a relation from a containing Project or Methodology Sources Scope Unit.
