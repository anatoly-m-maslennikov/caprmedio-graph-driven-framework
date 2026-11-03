---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL<+Operator//AllowedValue
  - CAPRMEDIO <+ MODEL <+ Term//Property
version: 28
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1245
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1245-CORE_META_MODEL-RULE--qualify-allowed-values-with-colon.md
  source_atom_id: CA-R-1245
  source_atom_revision: 28
  source_sha256: 7c19779a6dfef715a36e68c20bd1c1fbf572e3b71455ccb205895e5551dee6be
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Qualify Allowed Values with Colon

## Claim scope

allowed-value qualification in a Subject Expression.

## Claim

**in** a Subject Expression, `X:Y` **must** admit Y as one possible value of X in X's qualified context, irrespective of X's kind or path. This qualification is a CFEL operator, not a graph Relation. It does not assign Y to an occurrence or determine direct-value cardinality.
