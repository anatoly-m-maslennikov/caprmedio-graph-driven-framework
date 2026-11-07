---
atom_id: CA-R-1873
ref_id: CA-R-1873
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Package/Implementation
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
tier: 1
status: Active
version: 22
updated_at: "2026-11-07 17:10:31 +0400"
carrier_destination:
  file:
    name: CA-R-1873-CORE_META_MODEL-RULE--derive-implementation-and-use-its-actual-state-as-source.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Derive Implementation and use its actual state as source

## Claim

### Prose Claim

Governed production of Implementation derives Implementation from current applicable RMED through governed Operations.

Actual Implementation can serve as source truth for its realized content, structure, dependencies and behavior. A view derived from it through Operations remains a non-authoritative Projection.

## Details

Generation need not be deterministic. Derivation is a relation to governing intent, not perpetual loss of actual-state authority. Actual code may predate CAPRMEDIO authority; its observations support adoption, reconciliation, and continuation without automatically accepting inferred CRMED drafts or changing governing RMED. Existing I is not a prerequisite for reconstructing I from current RMED. Ordinary view Projections never replace the authority of their represented sources.
