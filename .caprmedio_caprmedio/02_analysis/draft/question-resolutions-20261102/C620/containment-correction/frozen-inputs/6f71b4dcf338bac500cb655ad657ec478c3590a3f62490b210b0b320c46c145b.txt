---
subjects:
  active: Entity/Aspect/Engineering/Data Handling/Data Transformation
  passive:
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - 'Entity/Object/Continuant/Projection/Type: Canonical Scope Signature'
  - Carrier/File
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1361@29
  - CA-M-241
atom_id: CA-E-407
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Evaluation
form: Eval Policy
---
## Summary

Validate Canonical Scope Signature Boundary

## Claim scope

Canonical Scope Signature derivations.

## Claim

the Evaluation **must** reject a Canonical Scope Signature derivation **if** **any** of the following holds:

- it rewrites one source Carrier.
- it treats one Signature as authority **or** Claim equivalence.
- it accepts mixed **and** **or** groups, **without**, **where**, **all**, **any** other CCE Operator, function, Entity-kind selector, descendant **or** dynamic selector, unresolved identity, changing source frontier, **or** unparseable prose.
- it fails **to** flatten nested same-operator groups, retains duplicate exact Atom IDs, loses the distinction between **and** **and** **or**, **or** yields different Signatures from same-operator groups that differ **only** by operand order.
