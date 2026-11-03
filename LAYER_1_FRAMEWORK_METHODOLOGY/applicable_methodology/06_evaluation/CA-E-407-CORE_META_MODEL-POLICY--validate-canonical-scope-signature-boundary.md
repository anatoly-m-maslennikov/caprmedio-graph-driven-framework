---
subjects:
  active: Aspects <+ Engineering <+ Data Handling <+ Data Transformation
  passive:
  - Aspects <+ Engineering <+ Authoring <+ Controlled English
  - 'Entity/Object/Continuant/Projection/Type: Canonical Scope Signature'
  - Carrier/File
version: 30
updated_at: 2026-11-02 18:35:20 +0400
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-407-CORE_META_MODEL-POLICY--validate-canonical-scope-signature-boundary.md
  source_atom_id: CA-E-407
  source_atom_revision: 30
  source_sha256: 119c374f8509b52187daa3a2885b2ddf352d89bd68349f82455073b61d30abe0
  original_relations_sha256: f67267d21eee2d6d0e9a34f7ed789a9d381444ce717666ef4ca06dbd9f78c50e
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
