---
subjects:
  active: Atom.Content
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Term//Property
  - CFEL<+Operator//AllowedValue
version: 35
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
atom_id: CA-R-1358
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1358-CORE_META_MODEL-RULE--consolidate-single-value-claims-as-one-value-set-claim.md
  source_atom_id: CA-R-1358
  source_atom_revision: 35
  source_sha256: c076c72f1611ca775b30d5b3dedc8d6e3e7199847e9f279bb9c2df9a8a4e2c88
  original_relations_sha256: e5ef375fa10a5f7fff5563acdf3d28805f5472119b8d66cdd96b86a22f04cbd8
---
## Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Claim scope

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.

## Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
