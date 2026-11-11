---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
version: 34
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-M-231
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-231-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-navigation-projections-from-the-cce-claim.md
  source_atom_id: CA-M-231
  source_atom_revision: 34
  source_sha256: 519de12389840e82976acec079bd14579e8c337d012d5fea231cab0eb764cabe
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Derive Navigation Projections from the CCE Claim

## Claim scope

derivation of an Atom's navigation values from its authoritative content.

## Claim

**to** derive an Atom's navigation values, derive them from authoritative content rather than another navigation value:

- derive a new Atom's Summary from its finalized primary contribution within its applicability under CA-R-2499 **and** CA-M-442. for RMED, use Claim read within Scope, **not** Scope alone.
- derive **every** requested Projection from its applicable complete source content, including relevant textual applicability restrictions, **not** from the Summary.
- for an existing Atom identity, retain its Summary **and** check source faithfulness. a needed Summary change follows CA-R-1464 **and** **must not** be applied as a same-identity refresh.
